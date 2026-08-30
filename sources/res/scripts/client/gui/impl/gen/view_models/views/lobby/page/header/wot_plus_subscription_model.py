from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_bonus_model import WotPlusSubscriptionBonusModel

class WotPlusTypeEnum(Enum):
    NONE = b'None'
    CORE = b'Core'
    PRO = b'Pro'


class WotPlusStateEnum(Enum):
    INACTIVE = b'Inactive'
    ACTIVE = b'Active'
    CANCELLED = b'Cancelled'


class WotPlusPeriodicityEnum(IntEnum):
    P6MONTHS = 6
    P12MONTHS = 12


class WotPlusSubscriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(WotPlusSubscriptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWotPlusEnabled(self):
        return self._getBool(0)

    def setIsWotPlusEnabled(self, value):
        self._setBool(0, value)
        return

    def getType(self):
        return WotPlusTypeEnum(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getState(self):
        return WotPlusStateEnum(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def getPeriodicity(self):
        return WotPlusPeriodicityEnum(self._getNumber(3))

    def setPeriodicity(self, value):
        self._setNumber(3, value.value)
        return

    def getExpiryTime(self):
        return self._getNumber(4)

    def setExpiryTime(self, value):
        self._setNumber(4, value)
        return

    def getBenefits(self):
        return self._getArray(5)

    def setBenefits(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getBenefitsType():
        return WotPlusSubscriptionBonusModel

    def getProBenefits(self):
        return self._getArray(6)

    def setProBenefits(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getProBenefitsType():
        return WotPlusSubscriptionBonusModel

    def _initialize(self):
        super(WotPlusSubscriptionModel, self)._initialize()
        self._addBoolProperty(b'isWotPlusEnabled', True)
        self._addStringProperty(b'type')
        self._addStringProperty(b'state')
        self._addNumberProperty(b'periodicity')
        self._addNumberProperty(b'expiryTime', 0)
        self._addArrayProperty(b'benefits', Array())
        self._addArrayProperty(b'proBenefits', Array())
        return
