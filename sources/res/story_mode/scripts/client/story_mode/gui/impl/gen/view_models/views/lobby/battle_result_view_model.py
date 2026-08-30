from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from story_mode.gui.impl.gen.view_models.views.lobby.mission_progress_level_model import MissionProgressLevelModel
from story_mode.gui.impl.gen.view_models.views.lobby.progress_level_model import ProgressLevelModel
from story_mode.gui.impl.gen.view_models.views.lobby.reward_model import RewardModel

class BattleResultViewModel(ViewModel):
    __slots__ = (b'onQuit', b'onContinue')

    def __init__(self, properties=14, commands=2):
        super(BattleResultViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def missionProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getMissionProgressType():
        return MissionProgressLevelModel

    def getMissionId(self):
        return self._getNumber(1)

    def setMissionId(self, value):
        self._setNumber(1, value)
        return

    def getIsVictory(self):
        return self._getBool(2)

    def setIsVictory(self, value):
        self._setBool(2, value)
        return

    def getTitle(self):
        return self._getResource(3)

    def setTitle(self, value):
        self._setResource(3, value)
        return

    def getSubTitle(self):
        return self._getResource(4)

    def setSubTitle(self, value):
        self._setResource(4, value)
        return

    def getInfoName(self):
        return self._getString(5)

    def setInfoName(self, value):
        self._setString(5, value)
        return

    def getInfoDescription(self):
        return self._getString(6)

    def setInfoDescription(self, value):
        self._setString(6, value)
        return

    def getVehicleName(self):
        return self._getString(7)

    def setVehicleName(self, value):
        self._setString(7, value)
        return

    def getPlayerStatus(self):
        return self._getString(8)

    def setPlayerStatus(self, value):
        self._setString(8, value)
        return

    def getHasAutoCompleteTasks(self):
        return self._getBool(9)

    def setHasAutoCompleteTasks(self, value):
        self._setBool(9, value)
        return

    def getIsOnboarding(self):
        return self._getBool(10)

    def setIsOnboarding(self, value):
        self._setBool(10, value)
        return

    def getProgressLevels(self):
        return self._getArray(11)

    def setProgressLevels(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getProgressLevelsType():
        return ProgressLevelModel

    def getMainRewards(self):
        return self._getArray(12)

    def setMainRewards(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getMainRewardsType():
        return RewardModel

    def getOtherRewards(self):
        return self._getArray(13)

    def setOtherRewards(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getOtherRewardsType():
        return RewardModel

    def _initialize(self):
        super(BattleResultViewModel, self)._initialize()
        self._addViewModelProperty(b'missionProgress', MissionProgressLevelModel())
        self._addNumberProperty(b'missionId', 0)
        self._addBoolProperty(b'isVictory', False)
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        self._addStringProperty(b'infoName', b'')
        self._addStringProperty(b'infoDescription', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'playerStatus', b'')
        self._addBoolProperty(b'hasAutoCompleteTasks', False)
        self._addBoolProperty(b'isOnboarding', False)
        self._addArrayProperty(b'progressLevels', Array())
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'otherRewards', Array())
        self.onQuit = self._addCommand(b'onQuit')
        self.onContinue = self._addCommand(b'onContinue')
        return
