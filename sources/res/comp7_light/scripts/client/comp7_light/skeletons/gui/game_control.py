import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event

class IComp7LightProgressionController(IGameController):
    onProgressPointsUpdated = None
    onSettingsChanged = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isFinished(self):
        raise NotImplementedError
        return

    @property
    def progressionToken(self):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def setSettings(self, settings):
        raise NotImplementedError
        return

    def saveCurPoints(self):
        raise NotImplementedError
        return

    def getPrevPoints(self):
        raise NotImplementedError
        return

    def getCurPoints(self):
        raise NotImplementedError
        return

    def getCurrentStageData(self):
        raise NotImplementedError
        return

    def getProgressionLevelsData(self):
        raise NotImplementedError
        return

    def getProgessionPointsData(self):
        raise NotImplementedError
        return

    def getProgressionData(self):
        raise NotImplementedError
        return
