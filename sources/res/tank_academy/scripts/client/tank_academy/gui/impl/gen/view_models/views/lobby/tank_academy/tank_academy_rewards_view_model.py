from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.tank_academy_bonus_model import TankAcademyBonusModel

class State(IntEnum):
    REGULAR = 0
    REWARDSCREENCHAIN = 1
    ENDREWARDSCREENCHAIN = 2
    FIRST = 3
    FINAL = 4


class TankAcademyRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'goToRewardsSelection', b'goToNextTask', b'goToHangarPreview')
    BOX_TOOLTIP_ARG_SHOW_COUNT = b'showCount'

    def __init__(self, properties=4, commands=4):
        super(TankAcademyRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStage(self):
        return self._getNumber(0)

    def setStage(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return State(self._getNumber(1))

    def setState(self, value):
        self._setNumber(1, value.value)
        return

    def getMainRewards(self):
        return self._getArray(2)

    def setMainRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getMainRewardsType():
        return TankAcademyBonusModel

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return TankAcademyBonusModel

    def _initialize(self):
        super(TankAcademyRewardsViewModel, self)._initialize()
        self._addNumberProperty(b'stage', 0)
        self._addNumberProperty(b'state')
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.goToRewardsSelection = self._addCommand(b'goToRewardsSelection')
        self.goToNextTask = self._addCommand(b'goToNextTask')
        self.goToHangarPreview = self._addCommand(b'goToHangarPreview')
        return
