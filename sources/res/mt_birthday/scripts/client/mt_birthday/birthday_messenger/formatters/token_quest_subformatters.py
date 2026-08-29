from adisp import adisp_async, adisp_process
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency
from messenger import g_settings
from messenger.formatters.token_quest_subformatters import AsyncTokenQuestsSubFormatter
from messenger.formatters.service_channel import QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData
from mt_birthday_common.constants import MT_BIRTHDAY_QUEST_PROGRESSION_ID
from mt_birthday.skeletons.mt_birthday_controller import ITanksBirthdayController
MAX_LEVEL = b'max'
DEFAULT_LEVEL = b'default'
INFINITY_LEVEL = b'infinity'

class BirthdayLevelUpFormatter(AsyncTokenQuestsSubFormatter):
    __birthdayController = dependency.descriptor(ITanksBirthdayController)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if isSynced:
            messages = []
            data = message.data or {}
            questIDs = filter(self._isQuestOfThisGroup, data.get(b'completedQuestIDs', set()))
            messageSettings = self._getGuiSettings(message, self._getTemplateName(), priorityLevel=NotificationPriorityLevel.MEDIUM)
            questsMap = {int(questID.split(b'_')[-1]): questID for questID in questIDs}
            for level in sorted(questsMap.keys()):
                rewardsData = data.get(b'detailedRewards', {}).get(questsMap[level], {})
                rewardsData[b'popUpRecords'] = data.get(b'popUpRecords', [])
                rewards = QuestAchievesFormatter.formatQuestAchieves(rewardsData, asBattleFormatter=False, processTokens=True)
                header = backport.text(R.strings.mt_birthday.notification.levelUp.congrats.header())
                text = backport.text(R.strings.mt_birthday.notification.levelUp.congrats.dyn(self._getLevel(level)).body(), level=level + 1, rewards=rewards)
                if rewards is not None:
                    formatted = g_settings.msgTemplates.format(self._getTemplateName(), ctx={b'header': header, 
                       b'text': text})
                    messages.append(MessageData(formatted, messageSettings))

            callback(messages)
        else:
            callback([MessageData(None, None)])
        return

    def _getTemplateName(self):
        return b'InformationHeaderSysMessage'

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID.startswith(MT_BIRTHDAY_QUEST_PROGRESSION_ID)

    @classmethod
    def _getLevel(cls, level):
        if level < cls.__birthdayController.getMaxProgressionLevel():
            return DEFAULT_LEVEL
        if level > cls.__birthdayController.getMaxProgressionLevel():
            return INFINITY_LEVEL
        return MAX_LEVEL
