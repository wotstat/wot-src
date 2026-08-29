from battle_royale_progression.notification.decorators import BRProgressionLockButtonDecorator
from gui.impl import backport
from gui.impl.gen import R
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter, QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData

class BRProgressionAchievesFormatter(QuestAchievesFormatter):
    _BULLET = u'\u2022 '
    _SEPARATOR = b'<br/>' + _BULLET

    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        result = super(BRProgressionAchievesFormatter, cls).formatQuestAchieves(data, asBattleFormatter, processCustomizations, processTokens)
        if result:
            return cls._BULLET + result
        return result


class BRProgressionSystemMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'BattleRoyaleProgressionSystemMessage'

    def __init__(self):
        super(BRProgressionSystemMessageFormatter, self).__init__()
        self._achievesFormatter = BRProgressionAchievesFormatter()
        return

    def format(self, message, *args):
        return self._format(message, args)

    def _format(self, message, *_):
        messageData = message.data or {}
        results = messageData.get(b'stages', set())
        messageDataList = []
        for result in sorted(results, key=(lambda result: result.get(b'stage', {}))):
            messageDataList.append(self._formatSingleStageCompletion(message, result))

        return messageDataList

    def _formatSingleStageCompletion(self, message, stageInfo):
        decorator = BRProgressionLockButtonDecorator
        messageHeader = backport.text(R.strings.battle_royale_progression.serviceChannelMessages.header())
        stage = stageInfo.get(b'stage')
        progressionName = backport.text(R.strings.battle_royale_progression.serviceChannelMessages.progressionName())
        messageBody = backport.text(R.strings.battle_royale_progression.serviceChannelMessages.body(), stage=str(stage), progressionName=progressionName)
        rewardsData = stageInfo.get(b'detailedRewards', {})
        if not rewardsData:
            return None
        else:
            formattedRewards = self._achievesFormatter.formatQuestAchieves(rewardsData, asBattleFormatter=False)
            return MessageData(g_settings.msgTemplates.format(self.__TEMPLATE, ctx={b'header': messageHeader, b'body': messageBody, 
               b'awards': formattedRewards}, data={}), self._getGuiSettings(message, self.__TEMPLATE, decorator=decorator))
