from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.reset_vehicle_info_model import ResetVehicleInfoModel

class ResetState(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    FAILED = 2


class ResetBranchViewModel(ViewModel):
    __slots__ = (b'onClose', b'onConfirm', b'onInstallVehicleConfiguration')
    VEHICLE_CONFIGURATION_KEY = b'configuration'
    CURRENT_VALUE_KEY = b'current'
    STOCK_VALUE_KEY = b'stock'

    def __init__(self, properties=9, commands=3):
        super(ResetBranchViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getResetState(self):
        return ResetState(self._getNumber(0))

    def setResetState(self, value):
        self._setNumber(0, value.value)
        return

    def getIsFill(self):
        return self._getBool(1)

    def setIsFill(self, value):
        self._setBool(1, value)
        return

    def getCanEquipStock(self):
        return self._getBool(2)

    def setCanEquipStock(self, value):
        self._setBool(2, value)
        return

    def getResetBranchesCount(self):
        return self._getNumber(3)

    def setResetBranchesCount(self, value):
        self._setNumber(3, value)
        return

    def getMaxResetBranchesCount(self):
        return self._getNumber(4)

    def setMaxResetBranchesCount(self, value):
        self._setNumber(4, value)
        return

    def getResetVehicles(self):
        return self._getArray(5)

    def setResetVehicles(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getResetVehiclesType():
        return ResetVehicleInfoModel

    def getTotalCredits(self):
        return self._getNumber(6)

    def setTotalCredits(self, value):
        self._setNumber(6, value)
        return

    def getCompleteBonusCoins(self):
        return self._getNumber(7)

    def setCompleteBonusCoins(self, value):
        self._setNumber(7, value)
        return

    def getCoinsForBranchReset(self):
        return self._getNumber(8)

    def setCoinsForBranchReset(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(ResetBranchViewModel, self)._initialize()
        self._addNumberProperty(b'resetState', ResetState.INITIAL.value)
        self._addBoolProperty(b'isFill', False)
        self._addBoolProperty(b'canEquipStock', False)
        self._addNumberProperty(b'resetBranchesCount', 0)
        self._addNumberProperty(b'maxResetBranchesCount', 0)
        self._addArrayProperty(b'resetVehicles', Array())
        self._addNumberProperty(b'totalCredits', 0)
        self._addNumberProperty(b'completeBonusCoins', 0)
        self._addNumberProperty(b'coinsForBranchReset', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onInstallVehicleConfiguration = self._addCommand(b'onInstallVehicleConfiguration')
        return
