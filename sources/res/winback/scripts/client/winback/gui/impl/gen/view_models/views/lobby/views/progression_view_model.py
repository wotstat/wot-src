from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from winback.gui.impl.gen.view_models.views.lobby.missions.battle_quests_model import BattleQuestsModel
from winback.gui.impl.gen.view_models.views.lobby.views.progress_level_model import ProgressLevelModel

class ProgressionState(Enum):
    INPROGRESS = b'inProgress'
    COMPLETED = b'completed'


class ProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAboutClicked', b'onShowSelectableRewardView')
    ARG_STAGE_NUMBER = b'stage'
    WITHOUT_STAGE = -1

    def __init__(self, properties=8, commands=3):
        super(ProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleQuests(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleQuestsType():
        return BattleQuestsModel

    def getState(self):
        return ProgressionState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getCurProgressPoints(self):
        return self._getNumber(2)

    def setCurProgressPoints(self, value):
        self._setNumber(2, value)
        return

    def getPrevProgressPoints(self):
        return self._getNumber(3)

    def setPrevProgressPoints(self, value):
        self._setNumber(3, value)
        return

    def getPointsForLevel(self):
        return self._getNumber(4)

    def setPointsForLevel(self, value):
        self._setNumber(4, value)
        return

    def getProgressLevels(self):
        return self._getArray(5)

    def setProgressLevels(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getProgressLevelsType():
        return ProgressLevelModel

    def getIsClaimRewardsAvailable(self):
        return self._getBool(6)

    def setIsClaimRewardsAvailable(self, value):
        self._setBool(6, value)
        return

    def getProgressionName(self):
        return self._getString(7)

    def setProgressionName(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(ProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'battleQuests', BattleQuestsModel())
        self._addStringProperty(b'state')
        self._addNumberProperty(b'curProgressPoints', 0)
        self._addNumberProperty(b'prevProgressPoints', 0)
        self._addNumberProperty(b'pointsForLevel', 0)
        self._addArrayProperty(b'progressLevels', Array())
        self._addBoolProperty(b'isClaimRewardsAvailable', False)
        self._addStringProperty(b'progressionName', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onAboutClicked = self._addCommand(b'onAboutClicked')
        self.onShowSelectableRewardView = self._addCommand(b'onShowSelectableRewardView')
        return
