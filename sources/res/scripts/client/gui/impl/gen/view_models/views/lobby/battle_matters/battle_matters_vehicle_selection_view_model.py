from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel

class BattleMattersVehicleSelectionViewModel(ViewModel):
    __slots__ = (b'onGoBack', b'onShowVehicle', b'onCompareVehicle', b'onResetFilter')
    ARG_VEHICLE_ID = b'vehCD'

    def __init__(self, properties=4, commands=4):
        super(BattleMattersVehicleSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)
        return

    def getTotalVehiclesCount(self):
        return self._getNumber(1)

    def setTotalVehiclesCount(self, value):
        self._setNumber(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def getVehicles(self):
        return self._getArray(3)

    def setVehicles(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getVehiclesType():
        return BattleMattersVehicleModel

    def _initialize(self):
        super(BattleMattersVehicleSelectionViewModel, self)._initialize()
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'totalVehiclesCount', 0)
        self._addNumberProperty(b'level', 0)
        self._addArrayProperty(b'vehicles', Array())
        self.onGoBack = self._addCommand(b'onGoBack')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onCompareVehicle = self._addCommand(b'onCompareVehicle')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        return
