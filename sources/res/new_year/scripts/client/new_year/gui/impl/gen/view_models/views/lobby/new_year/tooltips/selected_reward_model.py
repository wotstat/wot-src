from enum import Enum
from frameworks.wulf import ViewModel

class SelectedRewardName(Enum):
    VEHICLE_FOR_GIFT = b'vehicleForGift'
    VEHICLE_DISCOUNT = b'vehicleDiscount'
    BLUEPRINTS = b'blueprints'


class SelectedRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SelectedRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(1)

    def setVehicleLvl(self, value):
        self._setNumber(1, value)
        return

    def getUserName(self):
        return self._getString(2)

    def setUserName(self, value):
        self._setString(2, value)
        return

    def getCreditDiscount(self):
        return self._getNumber(3)

    def setCreditDiscount(self, value):
        self._setNumber(3, value)
        return

    def getNation(self):
        return self._getString(4)

    def setNation(self, value):
        self._setString(4, value)
        return

    def getCount(self):
        return self._getNumber(5)

    def setCount(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(SelectedRewardModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addStringProperty(b'userName', b'')
        self._addNumberProperty(b'creditDiscount', 0)
        self._addStringProperty(b'nation', b'')
        self._addNumberProperty(b'count', 0)
        return
