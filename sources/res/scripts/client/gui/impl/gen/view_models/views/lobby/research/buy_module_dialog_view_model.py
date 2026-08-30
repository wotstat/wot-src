from enum import Enum
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class MountDisabledReason(Enum):
    INVALID = b'invalid'
    NONE = b'none'
    NEEDGUN = b'need gun'
    NOTFORVEHICLETYPE = b'not for this vehicle type'
    NOTFORCURRENTVEHICLE = b'not for current vehicle'
    NEEDTURRET = b'need turret'


class ModuleType(Enum):
    FUELTANK = b'vehicleFuelTank'
    CHASSIS = b'vehicleChassis'
    WHEELEDCHASSIS = b'vehicleWheeledChassis'
    ENGINE = b'vehicleEngine'
    RADIO = b'vehicleRadio'
    TURRET = b'vehicleTurret'
    GUN = b'vehicleGun'


class BuyModuleDialogViewModel(FullScreenDialogWindowModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=3):
        super(BuyModuleDialogViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getModuleType(self):
        return ModuleType(self._getString(11))

    def setModuleType(self, value):
        self._setString(11, value.value)
        return

    def getModulePrice(self):
        return self._getNumber(12)

    def setModulePrice(self, value):
        self._setNumber(12, value)
        return

    def getPreviousModuleName(self):
        return self._getString(13)

    def setPreviousModuleName(self, value):
        self._setString(13, value)
        return

    def getPreviousModulePrice(self):
        return self._getNumber(14)

    def setPreviousModulePrice(self, value):
        self._setNumber(14, value)
        return

    def getAutoSellEnabled(self):
        return self._getBool(15)

    def setAutoSellEnabled(self, value):
        self._setBool(15, value)
        return

    def getMountDisabledReason(self):
        return MountDisabledReason(self._getString(16))

    def setMountDisabledReason(self, value):
        self._setString(16, value.value)
        return

    def _initialize(self):
        super(BuyModuleDialogViewModel, self)._initialize()
        self._addStringProperty(b'moduleType')
        self._addNumberProperty(b'modulePrice', 0)
        self._addStringProperty(b'previousModuleName', b'')
        self._addNumberProperty(b'previousModulePrice', 0)
        self._addBoolProperty(b'autoSellEnabled', False)
        self._addStringProperty(b'mountDisabledReason')
        return
