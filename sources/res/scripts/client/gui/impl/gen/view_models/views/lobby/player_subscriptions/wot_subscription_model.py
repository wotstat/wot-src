from enum import Enum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionModel

class WotSubscriptionStateEnum(Enum):
    INACTIVE = b'Inactive'
    ACTIVE = b'Active'
    CANCELLED = b'Cancelled'
    ERROR = b'Error'
    TRIAL = b'Trial'


class WotSubscriptionModel(SubscriptionModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(WotSubscriptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getWotSubscriptionState(self):
        return WotSubscriptionStateEnum(self._getString(8))

    def setWotSubscriptionState(self, value):
        self._setString(8, value.value)
        return

    def _initialize(self):
        super(WotSubscriptionModel, self)._initialize()
        self._addStringProperty(b'wotSubscriptionState')
        return
