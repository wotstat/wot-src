from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class DeconstructItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(DeconstructItemModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    @property
    def bonuses(self):
        return self._getViewModel(1)

    @staticmethod
    def getBonusesType():
        return BonusesModel

    def getDeviceID(self):
        return self._getNumber(2)

    def setDeviceID(self, value):
        self._setNumber(2, value)
        return

    def getDeviceName(self):
        return self._getString(3)

    def setDeviceName(self, value):
        self._setString(3, value)
        return

    def getDeviceImage(self):
        return self._getResource(4)

    def setDeviceImage(self, value):
        self._setResource(4, value)
        return

    def getDeviceLevel(self):
        return self._getNumber(5)

    def setDeviceLevel(self, value):
        self._setNumber(5, value)
        return

    def getEffect(self):
        return self._getResource(6)

    def setEffect(self, value):
        self._setResource(6, value)
        return

    def getEquipCoinsForDeconstruction(self):
        return self._getNumber(7)

    def setEquipCoinsForDeconstruction(self, value):
        self._setNumber(7, value)
        return

    def getStorageCount(self):
        return self._getNumber(8)

    def setStorageCount(self, value):
        self._setNumber(8, value)
        return

    def getSelectedCount(self):
        return self._getNumber(9)

    def setSelectedCount(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(DeconstructItemModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'bonuses', BonusesModel())
        self._addNumberProperty(b'deviceID', 0)
        self._addStringProperty(b'deviceName', b'')
        self._addResourceProperty(b'deviceImage', R.invalid())
        self._addNumberProperty(b'deviceLevel', 1)
        self._addResourceProperty(b'effect', 1)
        self._addNumberProperty(b'equipCoinsForDeconstruction', 0)
        self._addNumberProperty(b'storageCount', 0)
        self._addNumberProperty(b'selectedCount', 0)
        return
