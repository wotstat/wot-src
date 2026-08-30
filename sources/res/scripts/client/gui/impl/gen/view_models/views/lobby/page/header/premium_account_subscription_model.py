from enum import Enum
from frameworks.wulf import ViewModel

class PremiumTypeEnum(Enum):
    NONE = b'None'
    BASIC = b'Basic'
    PLUS = b'Plus'
    VIP = b'VIP'


class PremiumStateEnum(Enum):
    INACTIVE = b'Inactive'
    ACTIVE = b'Active'
    CANCELLED = b'Cancelled'


class PremiumAccountSubscriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PremiumAccountSubscriptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return PremiumTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getState(self):
        return PremiumStateEnum(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getExpiryTime(self):
        return self._getNumber(2)

    def setExpiryTime(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(PremiumAccountSubscriptionModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addStringProperty(b'state')
        self._addNumberProperty(b'expiryTime', 0)
        return
