from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.deconstruct_item_model import DeconstructItemModel

class DeconstructionDeviceViewModel(ViewModel):
    __slots__ = (b'onOkClick', b'onCloseClick', b'onModuleAdd', b'onModuleReduce')

    def __init__(self, properties=8, commands=4):
        super(DeconstructionDeviceViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentVehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentVehicleInfoType():
        return VehicleInfoModel

    def getEquipCoinsOnAccount(self):
        return self._getNumber(1)

    def setEquipCoinsOnAccount(self, value):
        self._setNumber(1, value)
        return

    def getEquipCoinsForDeconstruction(self):
        return self._getNumber(2)

    def setEquipCoinsForDeconstruction(self, value):
        self._setNumber(2, value)
        return

    def getEquipCoinsNeededForUpgrade(self):
        return self._getNumber(3)

    def setEquipCoinsNeededForUpgrade(self, value):
        self._setNumber(3, value)
        return

    def getDeviceForUpgradeName(self):
        return self._getString(4)

    def setDeviceForUpgradeName(self, value):
        self._setString(4, value)
        return

    def getIsOptDeviceRestored(self):
        return self._getBool(5)

    def setIsOptDeviceRestored(self, value):
        self._setBool(5, value)
        return

    def getModulesInStorage(self):
        return self._getArray(6)

    def setModulesInStorage(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getModulesInStorageType():
        return DeconstructItemModel

    def getModulesOnVehicles(self):
        return self._getArray(7)

    def setModulesOnVehicles(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getModulesOnVehiclesType():
        return DeconstructItemModel

    def _initialize(self):
        super(DeconstructionDeviceViewModel, self)._initialize()
        self._addViewModelProperty(b'currentVehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'equipCoinsOnAccount', 0)
        self._addNumberProperty(b'equipCoinsForDeconstruction', 0)
        self._addNumberProperty(b'equipCoinsNeededForUpgrade', 0)
        self._addStringProperty(b'deviceForUpgradeName', b'')
        self._addBoolProperty(b'isOptDeviceRestored', False)
        self._addArrayProperty(b'modulesInStorage', Array())
        self._addArrayProperty(b'modulesOnVehicles', Array())
        self.onOkClick = self._addCommand(b'onOkClick')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onModuleAdd = self._addCommand(b'onModuleAdd')
        self.onModuleReduce = self._addCommand(b'onModuleReduce')
        return
