from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_shell_model import ArmorShellModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_vehicle_module import ArmorVehicleModule

class ArmorAttacker(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ArmorAttacker, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    def getCurrentGun(self):
        return self._getNumber(1)

    def setCurrentGun(self, value):
        self._setNumber(1, value)
        return

    def getCurrentShell(self):
        return self._getNumber(2)

    def setCurrentShell(self, value):
        self._setNumber(2, value)
        return

    def getGuns(self):
        return self._getArray(3)

    def setGuns(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getGunsType():
        return ArmorVehicleModule

    def getShells(self):
        return self._getString(4)

    def setShells(self, value):
        self._setString(4, value)
        return

    def getShellDetails(self):
        return self._getMap(5)

    def setShellDetails(self, value):
        self._setMap(5, value)
        return

    @staticmethod
    def getShellDetailsType():
        return (int, ArmorShellModel)

    def _initialize(self):
        super(ArmorAttacker, self)._initialize()
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addNumberProperty(b'currentGun', 0)
        self._addNumberProperty(b'currentShell', 0)
        self._addArrayProperty(b'guns', Array())
        self._addStringProperty(b'shells', b'')
        self._addMapProperty(b'shellDetails', Map(int, ArmorShellModel))
        return
