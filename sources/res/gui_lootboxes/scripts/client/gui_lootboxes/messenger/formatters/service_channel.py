import typing
from adisp import adisp_async, adisp_process
from constants import LOOTBOX_TOKEN_PREFIX, LOOTBOX_KEY_PREFIX
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.loot_box.loot_box_helper import getLootBoxIDFromToken
from gui.shared.formatters import text_styles
from gui.shared.formatters.currency import applyAll
from gui_lootboxes.skeletons.statistic_lootbox_controller import IStatisticLootBoxController
from helpers import time_utils, dependency
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter, QuestAchievesFormatter, WaitItemsSyncFormatter, LootBoxAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData, getRewardsForBoxes
from skeletons.gui.shared import IItemsCache
from skeletons.gui.game_control import IGuiLootBoxesController
from gui_lootboxes.gui.bonuses.bonuses_helpers import TOKEN_COMPENSATION_PREFIX
from gui_lootboxes.gui.bonuses.bonuses_helpers import parseCompenstaionToken
from gui.shared.gui_items.loot_box import LootBoxKeyType
if typing.TYPE_CHECKING:
    from typing import List

class LootBoxOpenedFormatter(ServiceChannelFormatter):
    __itemsCache = dependency.descriptor(IItemsCache)
    __guiLootbox = dependency.descriptor(IGuiLootBoxesController)
    __MESSAGE_TEMPLATE = b'LootBoxOpenedSysMessage'
    __SEPARATOR = b'<br/>'

    def format(self, message, *args):
        allRewards = message.get(b'rewards')
        openedLootBoxes = message.get(b'openedLootBoxes')
        failedKeys = message.get(b'failedKeys')
        usedKeys = message.get(b'usedKeys')
        self.__lootboxesAsRewards = self.__getLootboxesAsReceivedRewards(allRewards)
        header = message.get(b'header', self.__formHeader(openedLootBoxes))
        infoText = message.get(b'infoText', b'')
        receivedRewards, vehicleCompensatedRewards, collectionCompensatedRewards = self.__splitRewards(allRewards)
        dateFmt = backport.getDateTimeFormat(time_utils.getServerRegionalTime())
        openedFmt = self.__formOpenedBoxesSection(openedLootBoxes)
        failFmt = self.__formFailBoxesSection(openedLootBoxes, failedKeys)
        receivedRewardsFmt = self.__formReceivedRewardsSection(receivedRewards)
        compensationFmt = self.__formCompensationSection(vehicleCompensatedRewards, collectionCompensatedRewards)
        failKeyFmt = self.__formFailKeySection(usedKeys)
        mainText = openedFmt + failFmt + receivedRewardsFmt + compensationFmt + failKeyFmt
        formatted = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx={b'header': header, 
           b'infoText': infoText, 
           b'date': dateFmt, 
           b'mainText': mainText})
        settings = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
        return [MessageData(formatted, settings)]

    def __formHeader(self, openedLootBoxes):
        allCount = 0
        for boxID in openedLootBoxes:
            if boxID not in self.__lootboxesAsRewards:
                allCount += openedLootBoxes[boxID]

        headerStr = backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBox.header()) if allCount == 1 else backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBoxes.header())
        return headerStr

    def __formOpenedBoxesSection(self, openedLootBoxes):
        openedBoxes = []
        for boxID, count in openedLootBoxes.iteritems():
            if self.__lootboxesAsRewards and boxID in self.__lootboxesAsRewards:
                continue
            lootBox = self.__itemsCache.items.tokens.getLootBoxByID(boxID)
            if lootBox is not None and count > 0:
                openedStr = makeHtmlString(b'html_templates:lobby/quests/bonuses', b'lootBox', {b'name': (lootBox.getUserName()), b'count': count})
                openedBoxes.append(openedStr)

        title = text_styles.titleFont(backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBox.opened()))
        if not openedBoxes:
            return b''
        else:
            return title + self.__SEPARATOR + self.__SEPARATOR.join(openedBoxes) + self.__SEPARATOR

    def __formFailBoxesSection(self, openedLootBoxes, failedKeys):
        failBoxes = []
        for boxID, _ in openedLootBoxes.iteritems():
            if self.__lootboxesAsRewards and boxID in self.__lootboxesAsRewards:
                continue
            lootBox = self.__itemsCache.items.tokens.getLootBoxByID(boxID)
            if lootBox.openedWithKey() and lootBox is not None:
                boxKeys = lootBox.getUnlockKeyIDs()
                countFail = 0
                for keyID, countK in failedKeys.iteritems():
                    if keyID in boxKeys and countK > 0:
                        countFail += countK

                if countFail:
                    openedStr = makeHtmlString(b'html_templates:lobby/quests/bonuses', b'lootBox', {b'name': (lootBox.getUserName()), b'count': countFail})
                    failBoxes.append(openedStr)

        if not failBoxes:
            return b''
        else:
            title = text_styles.titleFont(backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBox.failopened()))
            return self.__SEPARATOR + title + self.__SEPARATOR + self.__SEPARATOR.join(failBoxes) + self.__SEPARATOR

    def __formFailKeySection(self, usedKeys):
        lockpick = []
        countKey = 0
        countLockpick = 0
        for keyID, count in usedKeys.iteritems():
            key = self.__guiLootbox.getKeyByID(keyID)
            if key:
                if key.keyType == LootBoxKeyType.SIMPLE:
                    countKey += count
                else:
                    countLockpick += count

        if countLockpick:
            lockpick.append(makeHtmlString(b'html_templates:lobby/quests/bonuses', b'lootBoxKey', {b'name': (backport.text(R.strings.quests.bonuses.item.lockpick())), b'count': countLockpick}))
        if countKey:
            lockpick.append(makeHtmlString(b'html_templates:lobby/quests/bonuses', b'lootBoxKey', {b'name': (backport.text(R.strings.quests.bonuses.item.lootBoxKey())), 
               b'count': countKey}))
        title = text_styles.titleFont(backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBox.draw()))
        if not lockpick:
            return b''
        return self.__SEPARATOR + title + self.__SEPARATOR + self.__SEPARATOR.join(lockpick)

    def __splitRewards(self, allRewards):
        receivedRewards = {}
        vehicleCompensatedRewards = {}
        collectionCompensatedRewards = {}
        for vehicleDict in allRewards.get(b'vehicles', []):
            vehData = next(vehicleDict.itervalues())
            if b'rentCompensation' in vehData or b'customCompensation' in vehData:
                vehicleCompensatedRewards.setdefault(b'vehicles', []).append(vehicleDict)
            else:
                receivedRewards.setdefault(b'vehicles', []).append(vehicleDict)

        for token in allRewards.get(b'tokens', {}).keys():
            if token.startswith(TOKEN_COMPENSATION_PREFIX):
                collectionCompensatedRewards[token] = allRewards[b'tokens'][token]
            elif not token.startswith(LOOTBOX_TOKEN_PREFIX) and not token.startswith(LOOTBOX_KEY_PREFIX) or allRewards[b'tokens'][token].get(b'count', 0) > 0:
                receivedRewards.setdefault(b'tokens', {})[token] = allRewards[b'tokens'][token]

        for k, v in allRewards.iteritems():
            if k not in (b'vehicles', b'tokens', b'meta'):
                receivedRewards[k] = v

        return (
         receivedRewards, vehicleCompensatedRewards, collectionCompensatedRewards)

    def __formReceivedRewardsSection(self, receivedRewards):
        if not receivedRewards:
            return b''
        title = text_styles.titleFont(backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBox.receivedRewards.header()))
        receivedRewardsFmt = QuestAchievesFormatter.formatQuestAchieves(receivedRewards, False) or b''
        return self.__SEPARATOR + title + self.__SEPARATOR + receivedRewardsFmt + self.__SEPARATOR

    def __getVehicleCompensationString(self, compensatedVehicles):
        vehicleCompensationFmt = QuestAchievesFormatter.formatQuestAchieves(compensatedVehicles, False)
        return vehicleCompensationFmt

    def __getCollectionCompensationString(self, compensatedCollections):
        result = []
        for token, data in compensatedCollections.iteritems():
            htmlTemplates = g_settings.htmlTemplates
            currency, value, _, _ = parseCompenstaionToken(token)
            count = data.get(b'count', 1)
            key = (b'{}Compensation').format(currency)
            comp = htmlTemplates.format(key + b'InvoiceReceived', ctx={b'amount': (applyAll(currency, value * count))})
            result.append(htmlTemplates.format(b'collectionsCompensation', ctx={b'amount': (str(count)), 
               b'compensation': comp}))

        return self.__SEPARATOR.join(result)

    def __formCompensationSection(self, vehicleCompensatedRewards, collectionCompensatedRewards):
        if not vehicleCompensatedRewards and not collectionCompensatedRewards:
            return b''
        title = text_styles.titleFont(backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.openedLootBox.compensation.header()))
        vehicleCompensationFmt = self.__getVehicleCompensationString(vehicleCompensatedRewards)
        collectionsCompensationFmt = self.__getCollectionCompensationString(collectionCompensatedRewards)
        compensationFmt = title + self.__SEPARATOR
        if vehicleCompensationFmt:
            compensationFmt += vehicleCompensationFmt + self.__SEPARATOR
        if collectionsCompensationFmt:
            compensationFmt += collectionsCompensationFmt + self.__SEPARATOR
        return self.__SEPARATOR + compensationFmt

    def __getLootboxesAsReceivedRewards(self, allRewards):
        result = []
        for token in allRewards.get(b'tokens', {}).keys():
            lootBoxID = getLootBoxIDFromToken(token)
            if lootBoxID and allRewards[b'tokens'][token].get(b'count', 0) > 0:
                result.append(lootBoxID)

        return result


class LootBoxAutoOpenFormatter(WaitItemsSyncFormatter):
    __MESSAGE_TEMPLATE = b'LootBoxRewardsSysMessage'
    __SEPARATOR = b'<br/>'
    __statLootBoxCtrl = dependency.descriptor(IStatisticLootBoxController)

    def __init__(self, subFormatters=()):
        super(LootBoxAutoOpenFormatter, self).__init__()
        self._achievesFormatter = LootBoxAchievesFormatter()
        self.__subFormatters = subFormatters
        return

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        messageDataList = []
        if isSynced and message.data:
            openedBoxesIDs = set(message.data.keys())
            for subFormatter in self.__subFormatters:
                subBoxesIDs = subFormatter.getBoxesOfThisGroup(openedBoxesIDs)
                if subBoxesIDs:
                    if subFormatter.isAsync():
                        result = yield subFormatter.format(message)
                    else:
                        result = subFormatter.format(message)
                    if result:
                        messageDataList.extend(result)
                    openedBoxesIDs.difference_update(subBoxesIDs)

            if openedBoxesIDs:
                data = message.data
                rewards = getRewardsForBoxes(message, openedBoxesIDs)
                openedLootBoxes = {boxID: data[boxID][b'count'] for boxID in openedBoxesIDs}
                failedKeys = {}
                usedKeys = {}
                for boxID in openedBoxesIDs:
                    failedKeys.update(data[boxID].get(b'failedKeys', {}))
                    usedKeys.update(data[boxID].get(b'usedKeys', {}))

                self.__calculateLootBoxKey(failedKeys, usedKeys)
                self.__formatTokensRewards(rewards, usedKeys)
                header = self.__formHeader(openedLootBoxes)
                infoText = self.__SEPARATOR + backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.autoOpenedLootBox.opened())
                messageData = LootBoxOpenedFormatter().format({b'header': header, 
                   b'infoText': infoText, 
                   b'rewards': rewards, 
                   b'openedLootBoxes': openedLootBoxes, 
                   b'failedKeys': failedKeys, 
                   b'usedKeys': usedKeys})[0]
                if messageData is not None:
                    messageDataList.append(messageData)
        if messageDataList:
            self.__statLootBoxCtrl._statLocalCache.requestBaseStat()
            callback(messageDataList)
            return
        else:
            callback([MessageData(None, None)])
            return

    def __calculateLootBoxKey(self, failedKeys, usedKeys):
        for key in usedKeys.iterkeys():
            usedKeys[key] += failedKeys.get(key, 0)

        for key in failedKeys.iterkeys():
            if key not in usedKeys.keys():
                usedKeys[key] = failedKeys[key]

        return

    def __formatTokensRewards(self, rewards, usedKeys):
        for token in rewards.get(b'tokens', {}).keys():
            if token.startswith(LOOTBOX_KEY_PREFIX):
                _, keyID = token.split(b':')
                count = rewards[b'tokens'][token].get(b'count', 0)
                rewardKeyCount = max(0, usedKeys.get(int(keyID), 0) + count)
                rewards[b'tokens'][token][b'count'] = rewardKeyCount

        return

    def __formHeader(self, boxesData):
        allCount = sum([boxesData[boxID] for boxID in boxesData])
        headerStr = backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.autoOpenedLootBox.header()) if allCount == 1 else backport.text(R.strings.lb_messenger.serviceChannelMessages.lootbox.autoOpenedLootBoxes.header())
        return headerStr
