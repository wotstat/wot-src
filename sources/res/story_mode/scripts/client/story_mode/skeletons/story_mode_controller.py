import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from story_mode_common.configs.story_mode_missions import MissionsModel, MissionModel
    from story_mode_common.configs.story_mode_settings import SettingsModel
    from Event import Event
    from story_mode_common.story_mode_constants import MissionType

class IStoryModeController(IGameController):
    onSyncDataUpdated = None
    onMissionsConfigUpdated = None
    onSettingsUpdated = None

    @property
    def isOnboarding(self):
        raise NotImplementedError
        return

    @property
    def isQuittingBattle(self):
        raise NotImplementedError
        return

    @property
    def selectedMissionId(self):
        raise NotImplementedError
        return

    @property
    def isSelectedMissionOnboarding(self):
        raise NotImplementedError
        return

    @property
    def storyModeInfoPageKey(self):
        raise NotImplementedError
        return

    @selectedMissionId.setter
    def selectedMissionId(self, value):
        raise NotImplementedError
        return

    def isEventEntryPointVisible(self):
        raise NotImplementedError
        return

    def isShowActiveModeState(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isInPrb(self):
        raise NotImplementedError
        return

    def switchPrb(self):
        raise NotImplementedError
        return

    @property
    def settings(self):
        raise NotImplementedError
        return

    @property
    def missions(self):
        raise NotImplementedError
        return

    @property
    def needToShowAward(self):
        raise NotImplementedError
        return

    @property
    def newMissionIdForNewbies(self):
        raise NotImplementedError
        return

    def popMissionProgressDiff(self, missionId):
        raise NotImplementedError
        return

    def getFirstMission(self):
        raise NotImplementedError
        return

    def isMissionCompleted(self, missionId):
        raise NotImplementedError
        return

    def isEventMissionSuitable(self, mission):
        raise NotImplementedError
        return

    def isFirstTaskNotCompleted(self, mission):
        raise NotImplementedError
        return

    def isAnyTaskNotCompleted(self, mission):
        raise NotImplementedError
        return

    def isSelectedMissionLocked(self):
        raise NotImplementedError
        return

    def getNextMission(self, missionId):
        raise NotImplementedError
        return

    @staticmethod
    def goToQueue():
        raise NotImplementedError
        return

    @staticmethod
    def exitQueue():
        raise NotImplementedError
        return

    @staticmethod
    def goToBattle():
        raise NotImplementedError
        return

    def goToHangar(self, guiCtx=None):
        raise NotImplementedError
        return

    def onOutroVideoComplete(self, arenaUniqueID):
        raise NotImplementedError
        return

    def quitBattle(self):
        raise NotImplementedError
        return

    def popWaitingToBeShownAwardData(self):
        raise NotImplementedError
        return

    def awardShown(self):
        raise NotImplementedError
        return

    def startMusic(self):
        raise NotImplementedError
        return

    def stopMusic(self, forceStop=False):
        raise NotImplementedError
        return

    def startBattleMusic(self):
        raise NotImplementedError
        return

    def stopBattleMusic(self):
        raise NotImplementedError
        return

    def isMissionTaskCompleted(self, missionId, taskId):
        raise NotImplementedError
        return

    def filterMissions(self, missionType=None):
        raise NotImplementedError
        return

    def isNewbieGuidanceNeeded(self):
        raise NotImplementedError
        return

    def isNewNeededForNewbies(self):
        raise NotImplementedError
        return

    def isMissionLocked(self, mission):
        raise NotImplementedError
        return

    def setNewForNewbiesSeen(self):
        raise NotImplementedError
        return

    def chooseSelectedMissionId(self, isEvent=False):
        raise NotImplementedError
        return
