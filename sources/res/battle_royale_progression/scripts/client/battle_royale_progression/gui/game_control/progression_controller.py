import logging, typing, Event
from PlayerEvents import g_playerEvents
from account_helpers import AccountSettings
from account_helpers.AccountSettings import BR_PROGRESSION_POINTS_SEEN
from gui.server_events.bonuses import getNonQuestBonuses
from helpers import dependency
from skeletons.gui.game_control import IBRProgressionOnTokensController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
_logger = logging.getLogger(__name__)

class ProgressionOnTokensController(IBRProgressionOnTokensController):
    PREV_POINTS_ACC_SETTINGS_KEY = b'exampleLastPointsSeen'
    eventsCache = dependency.descriptor(IEventsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)
    progressionToken = b''

    def __init__(self):
        super(ProgressionOnTokensController, self).__init__()
        self.onProgressPointsUpdated = Event.Event()
        self.onSettingsChanged = Event.Event()
        return

    def init(self):
        g_playerEvents.onClientUpdated += self.__onTokensUpdate
        return

    def fini(self):
        g_playerEvents.onClientUpdated -= self.__onTokensUpdate
        self.onProgressPointsUpdated.clear()
        self.onSettingsChanged.clear()
        return

    def __onTokensUpdate(self, diff, _):
        tokens = diff.get(b'tokens', {})
        if not tokens:
            return
        if self.progressionToken and self.progressionToken in tokens:
            self.onProgressPointsUpdated()
        return

    def saveCurPoints(self):
        self._cachePoints(self.getCurPoints())
        return

    def getPrevPoints(self):
        return self._getCachedPoints()

    def getCurPoints(self):
        return self.eventsCache.questsProgress.getTokenCount(self.progressionToken)

    def getProgessionPointsData(self):
        curPoings = self.getCurPoints()
        prevPoint = self.getPrevPoints()
        if curPoings < prevPoint:
            prevPoint = 0
        return {b'curPoints': curPoings, b'pointsForLevel': (self._getPointsForLevel()), 
           b'prevPoints': prevPoint, 
           b'progressionLevels': (self.getProgressionLevelsData())}

    def getProgressionData(self):
        return self.getProgessionPointsData()

    def _cachePoints(self, curPoints):
        AccountSettings.setSettings(self.PREV_POINTS_ACC_SETTINGS_KEY, curPoints)
        return

    def _getCachedPoints(self):
        return AccountSettings.getSettings(self.PREV_POINTS_ACC_SETTINGS_KEY)

    def _getPointsForLevel(self):
        raise NotImplementedError
        return


class ProgressionOnConfig(ProgressionOnTokensController):

    def __init__(self):
        super(ProgressionOnConfig, self).__init__()
        self.settings = {}
        return

    def fini(self):
        self.settings = None
        super(ProgressionOnConfig, self).fini()
        return

    @property
    def isEnabled(self):
        return bool(self.settings)

    @property
    def isFinished(self):
        if not self.isEnabled:
            return False
        return self.getCurPoints() >= self._getPointsForLevel() * len(self._getStages())

    def _getStages(self):
        return sorted([stage for stage in self.settings.get(b'awardList', []) if stage[0] is not None], key=(lambda stage: stage[0]))

    def setSettings(self, settings):
        self.settings = settings
        if self.settings.get(b'token'):
            self.progressionToken = self.settings.get(b'token')
        self.onSettingsChanged()
        return

    def getCurrentStageData(self):
        if not self.isEnabled:
            return {}
        curPoints = self.getCurPoints()
        curStage = 0
        stagePoints = 0
        stageMaxPoints = 0
        prevStageMaxPoints = 0
        for stage, maxPoints in enumerate(zip(*self._getStages())[0], 1):
            curStage = stage
            stagePoints = curPoints - prevStageMaxPoints
            stageMaxPoints = maxPoints - prevStageMaxPoints
            prevStageMaxPoints = maxPoints
            if curPoints < maxPoints:
                break
        else:
            stagePoints = min(stagePoints, stageMaxPoints)

        results = {b'currentStage': curStage, 
           b'stagePoints': stagePoints, 
           b'stageMaxPoints': stageMaxPoints}
        return results

    def _getPointsForLevel(self):
        stages = self._getStages()
        if len(self.settings) < 2:
            _logger.error(b'ProgressionOnConfig cant find stages')
            return 0
        firstStageInfo, secondStageInfo = stages[:2]
        return secondStageInfo[0] - firstStageInfo[0]

    def getProgressionLevelsData(self):
        result = []
        for stageAwards in zip(*self._getStages())[1]:
            bonuses = []
            for key, value in stageAwards.iteritems():
                bonuses.extend(getNonQuestBonuses(key, value))

            result.append({b'rewards': bonuses})

        return result


class _QuestInListContainer(object):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        self.questsIds = {}
        return

    def getQuests(self):
        return self.eventsCache.getAllQuests(self._filterFunc)

    def setQuestsIds(self, questsIds):
        self.questsIds = questsIds
        return

    def _filterFunc(self, quest):
        return quest.getID() in self.questsIds and quest.accountReqs.isAvailable()


class BaseProgressionWithBattleQuests(ProgressionOnConfig):
    ProgressionFilterFuncKey = b'BRFuncKey'

    def __init__(self):
        super(BaseProgressionWithBattleQuests, self).__init__()
        self.questContainer = self._getQuestContainer()
        return

    def _getQuestContainer(self):
        return _QuestInListContainer()

    def setSettings(self, settings):
        questsIds = settings.get(b'questIds', ())
        self.questContainer.setQuestsIds(questsIds)
        filterFunc = lambda quest: quest.getID() in questsIds
        self.eventsCache.questsProgress.addFilterFunc(filterFunc, key=self.ProgressionFilterFuncKey)
        super(BaseProgressionWithBattleQuests, self).setSettings(settings)
        return

    def getBattleQuestData(self):
        return {b'battleQuests': (self.questContainer.getQuests())}

    def getProgressionData(self):
        result = self.getProgessionPointsData()
        result.update(self.getBattleQuestData())
        return result


class BRQuests(_QuestInListContainer):
    pass


class BRProgressionController(BaseProgressionWithBattleQuests):
    PREV_POINTS_ACC_SETTINGS_KEY = BR_PROGRESSION_POINTS_SEEN
    progressionToken = b'img:battle_royale:progression'
    PROGRESSION_QUEST_PREFIX = b'battle_royale:ticket:progression:'

    def _getQuestContainer(self):
        return BRQuests()
