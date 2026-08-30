from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.tooltips.paragons_tooltip_vehicles_model import ParagonsTooltipVehiclesModel

class FeatureState(IntEnum):
    IS_ACTIVE = 0
    IS_PAUSED = 1
    LIMIT_REACHED = 2
    PARAGONS_NOT_AVAILABLE = 3
    VEHICLES_REQUIRED = 4
    RULES_INCOMLETED = 5
    FIRST_BRANCH_RESET = 6
    DROPPED_BRANCH = 7


class ResetButtonTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(ResetButtonTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getResetBranchesCount(self):
        return self._getNumber(0)

    def setResetBranchesCount(self, value):
        self._setNumber(0, value)
        return

    def getMaxResetBranchesCount(self):
        return self._getNumber(1)

    def setMaxResetBranchesCount(self, value):
        self._setNumber(1, value)
        return

    def getCredits(self):
        return self._getNumber(2)

    def setCredits(self, value):
        self._setNumber(2, value)
        return

    def getParagonsPoints(self):
        return self._getNumber(3)

    def setParagonsPoints(self, value):
        self._setNumber(3, value)
        return

    def getBranchResetPoints(self):
        return self._getNumber(4)

    def setBranchResetPoints(self, value):
        self._setNumber(4, value)
        return

    def getWinPoints(self):
        return self._getNumber(5)

    def setWinPoints(self, value):
        self._setNumber(5, value)
        return

    def getBonusPoints(self):
        return self._getNumber(6)

    def setBonusPoints(self, value):
        self._setNumber(6, value)
        return

    def getState(self):
        return FeatureState(self._getNumber(7))

    def setState(self, value):
        self._setNumber(7, value.value)
        return

    def getVehicleCount(self):
        return self._getNumber(8)

    def setVehicleCount(self, value):
        self._setNumber(8, value)
        return

    def getNecessaryVehicleCount(self):
        return self._getNumber(9)

    def setNecessaryVehicleCount(self, value):
        self._setNumber(9, value)
        return

    def getBattleTypes(self):
        return self._getArray(10)

    def setBattleTypes(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getBattleTypesType():
        return int

    def getVehicles(self):
        return self._getArray(11)

    def setVehicles(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getVehiclesType():
        return ParagonsTooltipVehiclesModel

    def _initialize(self):
        super(ResetButtonTooltipModel, self)._initialize()
        self._addNumberProperty(b'resetBranchesCount', 0)
        self._addNumberProperty(b'maxResetBranchesCount', 0)
        self._addNumberProperty(b'credits', 0)
        self._addNumberProperty(b'paragonsPoints', 0)
        self._addNumberProperty(b'branchResetPoints', 0)
        self._addNumberProperty(b'winPoints', 0)
        self._addNumberProperty(b'bonusPoints', 0)
        self._addNumberProperty(b'state', FeatureState.IS_ACTIVE.value)
        self._addNumberProperty(b'vehicleCount', 0)
        self._addNumberProperty(b'necessaryVehicleCount', 0)
        self._addArrayProperty(b'battleTypes', Array())
        self._addArrayProperty(b'vehicles', Array())
        return
