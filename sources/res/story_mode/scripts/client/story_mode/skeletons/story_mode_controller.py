import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from story_mode_common.configs.story_mode_missions import MissionsModel, MissionModel
    from story_mode_common.configs.story_mode_settings import SettingsModel
    from Event import Event

class IStoryModeController(IGameController):
    onSyncDataUpdated = None

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

    @selectedMissionId.setter
    def selectedMissionId(self, value):
        raise NotImplementedError
        return

    def isEnabled(self):
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

    def getFirstMission(self):
        raise NotImplementedError
        return

    def isMissionCompleted(self, missionId):
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
    def goToBattle():
        raise NotImplementedError
        return

    def goToHangar(self, guiCtx=None):
        raise NotImplementedError
        return

    def skipOnboarding(self):
        raise NotImplementedError
        return

    def awardShown(self):
        raise NotImplementedError
        return

    def startOnboardingMusic(self, event=None):
        raise NotImplementedError
        return

    def stopOnboardingMusic(self):
        raise NotImplementedError
        return
