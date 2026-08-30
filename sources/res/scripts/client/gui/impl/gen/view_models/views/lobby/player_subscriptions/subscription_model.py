from enum import Enum
from frameworks.wulf import ViewModel

class SubscriptionTypeEnum(Enum):
    WOTSUBSCRIPTION = b'WotSubscription'
    EXTERNALSUBSCRIPTION = b'ExternalSubscription'


class SubscriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(SubscriptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getSubscriptionType(self):
        return SubscriptionTypeEnum(self._getString(3))

    def setSubscriptionType(self, value):
        self._setString(3, value.value)
        return

    def getImageUriSmall(self):
        return self._getString(4)

    def setImageUriSmall(self, value):
        self._setString(4, value)
        return

    def getImageUriMedium(self):
        return self._getString(5)

    def setImageUriMedium(self, value):
        self._setString(5, value)
        return

    def getImageUriLarge(self):
        return self._getString(6)

    def setImageUriLarge(self, value):
        self._setString(6, value)
        return

    def getRefreshTime(self):
        return self._getNumber(7)

    def setRefreshTime(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(SubscriptionModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'subscriptionType')
        self._addStringProperty(b'imageUriSmall', b'')
        self._addStringProperty(b'imageUriMedium', b'')
        self._addStringProperty(b'imageUriLarge', b'')
        self._addNumberProperty(b'refreshTime', 0)
        return
