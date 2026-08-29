from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class BattleTypesTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleTypesTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleLevelFrom(self):
        return self._getNumber(0)

    def setVehicleLevelFrom(self, value):
        self._setNumber(0, value)
        return

    def getVehicleLevelTo(self):
        return self._getNumber(1)

    def setVehicleLevelTo(self, value):
        self._setNumber(1, value)
        return

    def getAvailableBattleTypes(self):
        return self._getArray(2)

    def setAvailableBattleTypes(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getAvailableBattleTypesType():
        return int

    def _initialize(self):
        super(BattleTypesTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'vehicleLevelFrom', 1)
        self._addNumberProperty(b'vehicleLevelTo', 1)
        self._addArrayProperty(b'availableBattleTypes', Array())
        return
