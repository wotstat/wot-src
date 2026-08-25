from copy import deepcopy
from battle_royale.notification.decorators import BRProgressionLockButtonDecorator
from constants import LOOTBOX_TOKEN_PREFIX
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from helpers import dependency
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter, QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData
from skeletons.gui.game_control import IBattleRoyaleController

class BRProgressionAchievesFormatter(QuestAchievesFormatter):
    _BULLET = u'\u2022 '
    _SEPARATOR = b'<br/>' + _BULLET
    __LOOTBOX_TEMPLATE = b'SHPLootBoxReceived'
    __STPCOIN_TEMPLATE = b'StPCoinReceived'
    __BATTLE_PASS_TEMPLATE = b'battlePassBR'

    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        result = super(BRProgressionAchievesFormatter, cls).formatQuestAchieves(data, asBattleFormatter, processCustomizations, processTokens)
        if result:
            return cls._BULLET + result
        return result

    @classmethod
    def getFormattedAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        copiedData = deepcopy(data)
        copiedData.get(b'currencies', {}).pop(b'stpcoin', None)
        result = super(BRProgressionAchievesFormatter, cls).getFormattedAchieves(copiedData, asBattleFormatter, processCustomizations, processTokens)
        stpcoinsCount = data.get(b'currencies', {}).get(b'stpcoin', {}).get(b'count', 0)
        if stpcoinsCount:
            stpcoinResult = g_settings.htmlTemplates.format(cls.__STPCOIN_TEMPLATE, {b'text': (backport.text(R.strings.messenger.progression.received.stpcoin(), value=text_styles.stPatrick(stpcoinsCount)))})
            idx = 1 if [t for t in data.get(b'tokens', {}) if t.startswith(LOOTBOX_TOKEN_PREFIX)] else 0
            result.insert(idx, stpcoinResult)
        battlePassPoints = sum(points for points in data.get(b'battlePassPoints', {}).get(b'vehicles', {}).itervalues())
        if battlePassPoints > 0:
            result.append(g_settings.htmlTemplates.format(cls.__BATTLE_PASS_TEMPLATE, ctx={b'battlePassProgression': (backport.text(R.strings.messenger.serviceChannelMessages.BRbattleResults.battlePass(), pointsDiff=text_styles.neutral(battlePassPoints)))}))
        return result


class BRProgressionSystemMessageFormatter(ServiceChannelFormatter):
    __BATTLE_ROYALE_TEMPLATE = b'battleRoyaleProgressionSystemMessage'
    __ST_PATRICK_TEMPLATE = b'stPatrickProgressionSystemMessage'
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def __init__(self):
        super(BRProgressionSystemMessageFormatter, self).__init__()
        self._achievesFormatter = BRProgressionAchievesFormatter()
        return

    def format(self, message, *args):
        return self._format(message, args)

    def _format(self, message, *_):
        messageData = message.data or {}
        stages = messageData.get(b'stages', set())
        messageDataList = []
        for stage in sorted(stages, key=(lambda result: result.get(b'stage', {}))):
            messageData = self._formatSingleStageCompletion(message, stage)
            if messageData:
                messageDataList.append(messageData)

        return messageDataList

    def _formatSingleStageCompletion(self, message, stageInfo):
        rewardsData = stageInfo.get(b'detailedRewards', {})
        if not rewardsData:
            return None
        else:
            serviceMsg = R.strings.battle_royale_extention.serviceChannelMessages
            decorator = BRProgressionLockButtonDecorator
            messageHeader = backport.text(serviceMsg.header())
            stage = stageInfo.get(b'stage')
            progressionName = backport.text(serviceMsg.progressionName())
            messageBody = backport.text(serviceMsg.body(), stage=str(stage), progressionName=progressionName)
            formattedRewards = self._achievesFormatter.formatQuestAchieves(rewardsData, asBattleFormatter=False)
            if self.__battleRoyaleController.isStPatrick():
                template = self.__ST_PATRICK_TEMPLATE
            else:
                template = self.__BATTLE_ROYALE_TEMPLATE
            return MessageData(g_settings.msgTemplates.format(template, ctx={b'header': messageHeader, b'body': messageBody, 
               b'awards': formattedRewards}, data={}), self._getGuiSettings(message, template, decorator=decorator))
