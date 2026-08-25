from enum import Enum, IntEnum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionModel

class WotSubscriptionStateEnum(Enum):
    INACTIVE = b'Inactive'
    ACTIVE = b'Active'
    CANCELLED = b'Cancelled'


class WotTierEnum(Enum):
    NONE = b'None'
    CORE = b'Core'
    PRO = b'Pro'


class WotPlusPeriodicityEnum(IntEnum):
    P6MONTHS = 6
    P12MONTHS = 12


class WotSubscriptionModel(SubscriptionModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(WotSubscriptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getWotSubscriptionState(self):
        return WotSubscriptionStateEnum(self._getString(8))

    def setWotSubscriptionState(self, value):
        self._setString(8, value.value)
        return

    def getWotTier(self):
        return WotTierEnum(self._getString(9))

    def setWotTier(self, value):
        self._setString(9, value.value)
        return

    def getSubscriptionPeriodicity(self):
        return WotPlusPeriodicityEnum(self._getNumber(10))

    def setSubscriptionPeriodicity(self, value):
        self._setNumber(10, value.value)
        return

    def getIsButtonHighlighted(self):
        return self._getBool(11)

    def setIsButtonHighlighted(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(WotSubscriptionModel, self)._initialize()
        self._addStringProperty(b'wotSubscriptionState')
        self._addStringProperty(b'wotTier')
        self._addNumberProperty(b'subscriptionPeriodicity')
        self._addBoolProperty(b'isButtonHighlighted', False)
        return
