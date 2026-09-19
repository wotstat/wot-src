from enum import Enum
from frameworks.wulf import ViewModel

class VehicleTypes(Enum):
    NONE = b'none'
    LIGHTTANK = b'lightTank'
    MEDIUMTANK = b'mediumTank'
    HEAVYTANK = b'heavyTank'
    SPG = b'SPG'
    AT_SPG = b'AT-SPG'


class VehicleStates(Enum):
    DEFAULT = b'default'
    LOCKED = b'locked'
    INBATTLE = b'inBattle'
    INPLATOON = b'inPlatoon'
    INQUEUE = b'inQueue'


class CarouselTooltips(Enum):
    HALLOWEENCAROUSELVEHICLE = b'halloweenCarouselVehicle'
    HALLOWEENVEHICLEFEATURETOOLTIP = b'halloweenVehicleFeatureTooltip'
    DAILYQUEST = b'dailyQuest'


class HangarCarouselVehicleViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(HangarCarouselVehicleViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)
        return

    def getInvID(self):
        return self._getNumber(1)

    def setInvID(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIconName(self):
        return self._getString(3)

    def setIconName(self, value):
        self._setString(3, value)
        return

    def getHasDaily(self):
        return self._getBool(4)

    def setHasDaily(self, value):
        self._setBool(4, value)
        return

    def getVehicleType(self):
        return VehicleTypes(self._getString(5))

    def setVehicleType(self, value):
        self._setString(5, value.value)
        return

    def getVehicleState(self):
        return VehicleStates(self._getString(6))

    def setVehicleState(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(HangarCarouselVehicleViewModel, self)._initialize()
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'invID', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'iconName', b'')
        self._addBoolProperty(b'hasDaily', False)
        self._addStringProperty(b'vehicleType')
        self._addStringProperty(b'vehicleState')
        return
