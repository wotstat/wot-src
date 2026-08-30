from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.br_vehicle_specifications_model import BrVehicleSpecificationsModel

class TechParametersCmpViewModel(ViewModel):
    __slots__ = (b'onModulesBtnClick', b'onResized')

    def __init__(self, properties=2, commands=2):
        super(TechParametersCmpViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleGoodSpec(self):
        return self._getArray(0)

    def setVehicleGoodSpec(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getVehicleGoodSpecType():
        return BrVehicleSpecificationsModel

    def getVehicleBadSpec(self):
        return self._getArray(1)

    def setVehicleBadSpec(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getVehicleBadSpecType():
        return BrVehicleSpecificationsModel

    def _initialize(self):
        super(TechParametersCmpViewModel, self)._initialize()
        self._addArrayProperty(b'vehicleGoodSpec', Array())
        self._addArrayProperty(b'vehicleBadSpec', Array())
        self.onModulesBtnClick = self._addCommand(b'onModulesBtnClick')
        self.onResized = self._addCommand(b'onResized')
        return
