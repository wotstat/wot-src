from enum import Enum
from frameworks.wulf import ViewModel

class SlotStateEnum(Enum):
    EMPTY = b'empty'
    SELECTED = b'selected'
    DISABLED = b'disabled'
    DISABLEDBYKILLSWITCH = b'disabledByKillSwitch'


class SlotTypeEnum(Enum):
    DEFAULT = b'defaultSlots'
    PREMIUM = b'premiumSlots'
    SUBSCRB = b'subscrbSlots'
    REWARDS = b'rewardsSlots'


class MapModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MapModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return SlotTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)
        return

    def getSlotState(self):
        return SlotStateEnum(self._getString(2))

    def setSlotState(self, value):
        self._setString(2, value.value)
        return

    def getCooldownEndTimeInSecs(self):
        return self._getNumber(3)

    def setCooldownEndTimeInSecs(self, value):
        self._setNumber(3, value)
        return

    def getExpirationTime(self):
        return self._getNumber(4)

    def setExpirationTime(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(MapModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addStringProperty(b'mapId', b'')
        self._addStringProperty(b'slotState')
        self._addNumberProperty(b'cooldownEndTimeInSecs', 0)
        self._addNumberProperty(b'expirationTime', 0)
        return
