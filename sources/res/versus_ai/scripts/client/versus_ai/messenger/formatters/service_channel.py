from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from messenger import g_settings
from messenger.formatters.service_channel import BattleResultsFormatter
from skeletons.gui.server_events import IEventsCache
from gui.server_events.bonuses import VersusAIProgressionsTokenBonus
from helpers import dependency

class VersusAIBattleResultsFormatter(BattleResultsFormatter):
    __eventsCache = dependency.descriptor(IEventsCache)
    _battleResultKeys = {(-1): b'versusAIBattleDefeatResult', 
       0: b'versusAIBattleDrawGameResult', 
       1: b'versusAIBattleVictoryResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(VersusAIBattleResultsFormatter, self)._prepareFormatData(message)
        ctx[b'progressionPoints'] = self.__makeProgressionPointsString(message)
        return (
         templateName, ctx)

    def __makeProgressionPointsString(self, message):
        value, progressionName = self.__getProgressionTokenQuestBonus(message.data)
        if value:
            stringResource = R.strings.versus_ai_messenger.battleResults.progressionPoints
            progressionNameText = backport.text(stringResource.dyn(progressionName)())
            if progressionNameText:
                progressionNameText = b'<br/>' + progressionNameText
            text = backport.text(stringResource(), progressionName=progressionNameText, value=text_styles.neutral(value))
            return g_settings.htmlTemplates.format(b'versusAIBattleResultProgressionPoints', ctx={b'progressionPoints': text})
        return b''

    def __getProgressionTokenQuestBonus(self, battleResults):
        bonusCount = 0
        progressionName = b''
        for questID in battleResults.get(b'completedQuestIDs', []):
            quest = self.__eventsCache.getQuestByID(questID)
            if quest is not None:
                for bonus in quest.getBonuses():
                    if isinstance(bonus, VersusAIProgressionsTokenBonus):
                        bonusCount += bonus.getCount()
                        progressionName = bonus.getProgressionName()

        return (
         bonusCount, progressionName)
