from enum import Enum
from frameworks.wulf import ViewModel

class SubscriptionCardState(Enum):
    AVAILABLE = b'available'
    ACTIVE = b'active'
    DISABLE = b'disable'


class SubscriptionCardModel(ViewModel):
    __slots__ = (b'onCardClick', b'onInfoButtonClik')

    def __init__(self, properties=2, commands=2):
        super(SubscriptionCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return SubscriptionCardState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getNextCharge(self):
        return self._getString(1)

    def setNextCharge(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(SubscriptionCardModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'nextCharge', b'')
        self.onCardClick = self._addCommand(b'onCardClick')
        self.onInfoButtonClik = self._addCommand(b'onInfoButtonClik')
        return
