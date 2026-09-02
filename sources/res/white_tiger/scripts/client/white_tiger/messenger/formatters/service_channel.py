import logging, typing
from adisp import adisp_async, adisp_process
from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.money import ZERO_MONEY, Money, Currency
from gui.shared.notifications import NotificationPriorityLevel
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
from messenger import g_settings
from gui.shared.formatters import text_styles
from constants import LOOTBOX_TOKEN_PREFIX
from helpers import dependency
from messenger.formatters.service_channel import WaitItemsSyncFormatter, BattleResultsFormatter, ServiceChannelFormatter, QuestAchievesFormatter, InvoiceReceivedFormatter
from messenger.formatters.service_channel_helpers import MessageData, getCustomizationItemData
from skeletons.gui.game_control import IWhiteTigerController
from client_constants import EVENT_STATES
from white_tiger_common import wt_constants
if typing.TYPE_CHECKING:
    from typing import Dict
_logger = logging.getLogger(__name__)

class WTBattleResultsFormatter(BattleResultsFormatter):
    __gameEventController = dependency.descriptor(IWhiteTigerController)
    __WT_BATTLE_QUEST_PREFIX = b'wtevent:battle_quest:event'
    _battleResultKeys = {(-1): b'WTEventBattleDefeatResult', 
       0: b'WTEventBattleDefeatResult', 
       1: b'WTEventBattleVictoryResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(WTBattleResultsFormatter, self)._prepareFormatData(message)
        battleResults = message.data
        self.__fillWTEventMsgCtx(battleResults, ctx)
        return (
         templateName, ctx)

    def _getBackgroundIconSource(self, battleResults):
        if battleResults.get(b'isWinner', 0):
            return b'bgVictory'
        return b'bgDefeat'

    def __fillWTEventMsgCtx(self, battleResults, ctx):
        strRes = R.strings.white_tiger.notifications.battleResults
        mainResultName = b'victory' if battleResults.get(b'isWinner', -1) == 1 else b'defeat'
        ctx[b'mainResultName'] = backport.text(strRes.dyn(mainResultName).header())
        ctx[b'eventName'] = backport.text(strRes.eventName())
        team = battleResults.get(b'team', -1)
        if team == wt_constants.WT_TEAMS.BOSS_TEAM:
            teamName = backport.text(strRes.team.boss())
        elif team == wt_constants.WT_TEAMS.HUNTERS_TEAM:
            teamName = backport.text(strRes.team.hunters())
        else:
            teamName = b''
            _logger.warning(b'Unexpected team type: %r', team)
        ctx[b'teamName'] = teamName
        ctx[b'quests'] = b''
        completedQuestIDs = battleResults.get(b'completedQuestIDs', ())
        if self.__containsWTBattleQuest(completedQuestIDs):
            ctx[b'quests'] = b'<br>%s' % text_styles.main(backport.text(strRes.questCompleted()))
        ctx[b'customizations'] = b''
        custStrs = self.__formatCustomizationMessage(battleResults)
        if custStrs:
            ctx[b'customizations'] = b'<br>%s' % text_styles.main((b'<br>').join(custStrs))
        ctx[b'stamps'] = b''
        tokens = battleResults.get(b'tokens', {})
        stampToken = self.__gameEventController.getConfig().stamp
        if stampToken in tokens:
            earnedCount = tokens[stampToken].get(b'count', 0)
            if earnedCount > 0:
                ctx[b'stamps'] = b'<br>%s' % text_styles.main(backport.text(strRes.stamp(), count=text_styles.expText(earnedCount)))
        resultStr = []
        ctx[b'tickets'] = b''
        for token in self.__gameEventController.getBossTokenIDList():
            if token in tokens:
                earnedCount = tokens[token].get(b'count', 0)
                if earnedCount > 0:
                    tokenStr = token.split(b':')[1]
                    resultStr.append(b'<br>%s' % text_styles.main(backport.text(strRes.dyn(tokenStr)(), count=text_styles.expText(earnedCount))))
                    self.__pushTicketsEarnedMessage(token)

        if resultStr:
            ctx[b'tickets'] = b'%s' % text_styles.main((b'').join(resultStr))
        ctx[b'lootboxes'] = b''
        lootboxesStrs = []
        for tID, tVal in tokens.items():
            if tID.startswith(LOOTBOX_TOKEN_PREFIX):
                lootBox = self._itemsCache.items.tokens.getLootBoxByTokenID(tID)
                if lootBox is not None:
                    lootboxesStrs.append(backport.text(strRes.lootboxes.dyn(lootBox.getType())(), count=text_styles.expText(tVal.get(b'count', 0))))

        if lootboxesStrs:
            ctx[b'lootboxes'] = b'<br>%s' % text_styles.main((b'<br>').join(lootboxesStrs))
        return

    def __pushTicketsEarnedMessage(self, token):
        tokenStr = token.split(b':')[1]
        strRes = R.strings.white_tiger.notifications.dyn(tokenStr).received
        SystemMessages.pushMessage(text=backport.text(strRes.body(), ticketsCount=str(self.__gameEventController.getBossTokenCount(token))), messageData={b'header': (backport.text(strRes.header()))}, type=SM_TYPE.WarningHeader, priority=NotificationPriorityLevel.HIGH)
        return

    def __containsWTBattleQuest(self, questIDs):
        for questID in questIDs:
            if questID.startswith(self.__WT_BATTLE_QUEST_PREFIX):
                return True

        return False

    def __formatCustomizationMessage(self, data):
        customizations = data.get(b'customizations', [])
        custItems = []
        for customizationItem in customizations:
            splittedCustType = customizationItem.get(b'custType', b'').split(b':')
            custType = splittedCustType[0]
            custValue = customizationItem[b'value']
            if custValue > 0:
                operation = b'added'
            elif custValue < 0:
                operation = b'removed'
            else:
                operation = None
            if operation is not None:
                guiItemType, itemUserName, tags = getCustomizationItemData(customizationItem[b'id'], custType)
                if b'hiddenInUI' in tags:
                    continue
                custValue = abs(custValue)
                if custValue > 1:
                    custItems.append(backport.text(R.strings.system_messages.customization.dyn(operation).dyn((b'{}Value').format(guiItemType))(), itemUserName, custValue))
                else:
                    custItems.append(backport.text(R.strings.system_messages.customization.dyn(operation).dyn(guiItemType)(), itemUserName))

        return custItems


class WTEventTicketTokenWithdrawnFormatter(WaitItemsSyncFormatter):
    __wtController = dependency.descriptor(IWhiteTigerController)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        data = message.data
        isSynced = yield self._waitForSyncItems()
        if isSynced and data:
            token = data[b'token']
            amountDelta = data[b'amount_delta']
            if amountDelta >= 0:
                raise SoftException(b'Unexpected ticket amount to withdraw')
            strRes = R.strings.event.notifications
            config = self.__wtController.getConfig()
            if token in self.__wtController.getBossTokenIDList():
                ticketTokenStr = token.split(b':')[1]
                text = backport.text(strRes.dyn(ticketTokenStr).withdrawn.body(), ticketsCount=str(self.__wtController.getBossTokenCount(token)))
            elif token == config.quickBossTicketToken:
                text = backport.text(strRes.quickBossTicketToken.withdrawn.body())
            else:
                raise SoftException((b'Unexpected ticket token {}').format(token))
            xmlKey = b'WTEventTicketTokenWithdrawn'
            formatted = g_settings.msgTemplates.format(xmlKey, ctx={b'text': text})
            callback([MessageData(formatted, self._getGuiSettings(message, xmlKey))])
        else:
            callback([MessageData(None, None)])
        return


class WTEventStateMessageFormatter(ServiceChannelFormatter):
    __TEMPLATES = {(EVENT_STATES.START): b'WTEventStartedMessage', 
       (EVENT_STATES.FINISH): b'WTEventEndedMessage'}

    def format(self, message, *args):
        state = message.get(b'state', None)
        if state is None:
            _logger.error(b'[WTEventStateMessageFormatter] message.state is missing')
            return []
        else:
            template = self.__TEMPLATES.get(state, None)
            if template is None:
                _logger.error(b'[WTEventStateMessageFormatter] Missing template for state %s', state)
                return []
            formatted = g_settings.msgTemplates.format(template)
            return [MessageData(formatted, self._getGuiSettings(message, template))]


class WTEventProgressionFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'WTEventProgressionSysMessage'

    def canBeEmpty(self):
        return True

    def format(self, data, *args):
        messageDataList = []
        messageDataList.append(self._formatSingleStageCompletion(data))
        return messageDataList

    def _formatSingleStageCompletion(self, data):
        text = data.get(b'text', b'')
        data = {b'priority': (data.get(b'priority', b''))}
        return MessageData(g_settings.msgTemplates.format(self.__TEMPLATE, ctx={b'text': text}, data=data), self._getGuiSettings(data, self.__TEMPLATE))


class WTLootBoxesNotificationsFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'WTEventSwitchOnLootboxesSysMessage'

    def canBeEmpty(self):
        return True

    def format(self, data, *args):
        messageDataList = []
        messageDataList.append(self._formatSingleStageCompletion(data))
        return messageDataList

    def _formatSingleStageCompletion(self, data):
        text = data.get(b'text', b'')
        return MessageData(g_settings.msgTemplates.format(self.__TEMPLATE, ctx={b'text': text}), self._getGuiSettings(data, self.__TEMPLATE))


class WTEventLootBoxMessageFormatter(object):
    __itemsCache = dependency.descriptor(IItemsCache)
    __strRes = R.strings.white_tiger.notifications.lootBoxes

    @classmethod
    def formatLootBoxRewards(cls, rewards):
        rewardsReceived = text_styles.titleFont(backport.text(cls.__strRes.rewardsReceived()))
        compensation, compensatedVehicles = cls.__formatCompensation(rewards)
        lootBoxesStr = cls.__formatLootBoxesTokens(rewards.get(b'tokens', {}))
        rewardsStr = QuestAchievesFormatter.formatQuestAchieves(rewards, False)
        rewards.get(b'vehicles', []).extend(compensatedVehicles)
        return (b'{0}<br/>{1}<br/>{2}{3}').format(lootBoxesStr, rewardsReceived, rewardsStr, compensation)

    @classmethod
    def formatTankPortalRewards(cls, ctx):
        compensation, compensatedVehicles = cls.__formatCompensation(ctx)
        lootBoxesStr = cls.__formatLootBoxesTokens(ctx.get(b'tokens', {}), ctx.get(b'price', 0))
        vehiclesList = ctx.get(b'vehicles', [])
        vehMsg = InvoiceReceivedFormatter.getVehiclesString(vehiclesList, htmlTplPostfix=b'QuestsReceived')
        ctx.get(b'vehicles', []).extend(compensatedVehicles)
        return (b'{0}<br/>{1}<br/>{2}').format(lootBoxesStr, vehMsg, compensation)

    @classmethod
    def __formatCompensation(cls, rewards):
        compensationHeader = text_styles.titleFont(backport.text(cls.__strRes.compensation.header()))
        cls.__preformatCompensationValue(rewards)
        compensation = cls.__formatVehiclesCompensation(rewards)
        compensatedVehicles = []
        if compensation:
            compensation = (b'<br/><br/>{0}<br/>{1}').format(compensationHeader, compensation)
            compensatedVehicles = cls.__filterRewardsByVehicleCompensation(rewards)
        return (compensation, compensatedVehicles)

    @classmethod
    def __formatLootBoxesTokens(cls, tokens, price=0):
        for tokenID, tokenValue in tokens.items():
            if tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                lootBox = cls.__itemsCache.items.tokens.getLootBoxByTokenID(tokenID)
                if lootBox is not None:
                    if lootBox.getType() == b'wt_tank' and price > 0:
                        count = price
                    else:
                        count = abs(tokenValue.get(b'count', 0))
                    return backport.text(cls.__strRes.dyn(lootBox.getType())(), count=count)

        return b''

    @classmethod
    def __formatVehiclesCompensation(cls, rewards):
        vehiclesList = rewards.get(b'vehicles', {})
        compensation = InvoiceReceivedFormatter.getVehiclesCompensationString(vehiclesList, htmlTplPostfix=b'QuestsReceived')
        return compensation

    @classmethod
    def __filterRewardsByVehicleCompensation(cls, rewards):
        compensatedVehicles = []
        vehiclesList = rewards.get(b'vehicles', {})
        for ind, vehicleDict in enumerate(vehiclesList):
            for vehicleData in vehicleDict.values():
                if b'customCompensation' in vehicleData:
                    compensatedVehicles.append(vehicleDict)
                    vehiclesList.pop(ind)

        return compensatedVehicles

    @classmethod
    def __preformatCompensationValue(cls, rewards):
        vehiclesList = rewards.get(b'vehicles', [])
        compValue = cls.__getCompensationValue(vehiclesList)
        for currency in Currency.ALL:
            if compValue.get(currency, 0) > 0:
                currencyValue = rewards.pop(currency, None)
                if currencyValue is not None:
                    newCurrencyValue = currencyValue - compValue.get(currency, 0)
                    if newCurrencyValue:
                        rewards[currency] = newCurrencyValue

        return

    @classmethod
    def __getCompensationValue(cls, vehicles):
        comp = ZERO_MONEY
        for vehicleDict in vehicles:
            for vehData in vehicleDict.values():
                if b'customCompensation' in vehData:
                    comp += Money.makeFromMoneyTuple(vehData[b'customCompensation'])

        return comp


class WTArenaBanSystemMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'WTArenaBanSystemMessage'

    def canBeEmpty(self):
        return True

    def format(self, data, *args):
        messageDataList = []
        messageDataList.append(self._formatSingleStageCompletion(data))
        return messageDataList

    def _formatSingleStageCompletion(self, data):
        isStarted = data.get(b'isStarted', False)
        if isStarted:
            header = backport.text(R.strings.white_tiger.sysMessageFairPlayMsg.arenaBanStart.header())
            body = backport.text(R.strings.white_tiger.sysMessageFairPlayMsg.arenaBanStart.body())
            icon = b'wtBanIcon'
        else:
            header = backport.text(R.strings.white_tiger.sysMessageFairPlayMsg.arenaBanStop.header())
            body = backport.text(R.strings.white_tiger.sysMessageFairPlayMsg.arenaBanStop.body())
            icon = b'InformationIcon'
        data = {b'savedData': {b'isStarted': isStarted, 
                          b'reason': (data.get(b'reason', b'')), 
                          b'duration': (data.get(b'duration', 0)), 
                          b'banExpiryTime': (data.get(b'banExpiryTime', 0))}, 
           b'icon': icon}
        return MessageData(g_settings.msgTemplates.format(self.__TEMPLATE, ctx={b'header': header, b'body': body}, data=data), self._getGuiSettings(data, self.__TEMPLATE))


class WTArenaWarningSystemMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'WTArenaWarningSystemMessage'

    def canBeEmpty(self):
        return True

    def format(self, data, *args):
        messageDataList = []
        messageDataList.append(self._formatSingleStageCompletion(data))
        return messageDataList

    def _formatSingleStageCompletion(self, data):
        header = backport.text(R.strings.white_tiger.sysMessageFairPlayMsg.arenaWarning.header())
        body = backport.text(R.strings.white_tiger.sysMessageFairPlayMsg.arenaWarning.body())
        data = {b'savedData': {b'reason': (data.get(b'reason', b'')), 
                          b'duration': (data.get(b'duration', 0)), 
                          b'banExpiryTime': (data.get(b'banExpiryTime', 0))}}
        return MessageData(g_settings.msgTemplates.format(self.__TEMPLATE, ctx={b'header': header, b'body': body}, data=data), self._getGuiSettings(data, self.__TEMPLATE))


class WTEventLootBoxRerollRewardsMessageFormatter(object):
    __itemsCache = dependency.descriptor(IItemsCache)
    __strRes = R.strings.white_tiger.notifications.lootBoxes

    @classmethod
    def formatLootBoxRewards(cls, rewards):
        rewardsStr = QuestAchievesFormatter.formatQuestAchieves(rewards, False)
        return (b'<br/>{0}').format(rewardsStr)
