from enum import Enum
from frameworks.wulf import ViewModel

class MapStateEnum(Enum):
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE = b'active'
    MAPS_BLACKLIST_SLOT_STATE_CHANGE = b'change'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED = b'disabled'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED_BY_KILL_SWITCH = b'disabledByKillSwitch'
    MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = b'cooldown'
    MAPS_BLACKLIST_SLOT_STATE_SELECTED = b'selected'
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = b'activeNoHover'


class SlotTypeEnum(Enum):
    DEFAULT = b'defaultSlots'
    PREMIUM = b'premiumSlots'
    SUBSCRB = b'subscrbSlots'
    REWARDS = b'rewardsSlots'


class MapsBlacklistSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(MapsBlacklistSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return SlotTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getState(self):
        return MapStateEnum(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getMapId(self):
        return self._getString(2)

    def setMapId(self, value):
        self._setString(2, value)
        return

    def getSeasonId(self):
        return self._getNumber(3)

    def setSeasonId(self, value):
        self._setNumber(3, value)
        return

    def getCooldownTime(self):
        return self._getNumber(4)

    def setCooldownTime(self, value):
        self._setNumber(4, value)
        return

    def getExpirationTime(self):
        return self._getNumber(5)

    def setExpirationTime(self, value):
        self._setNumber(5, value)
        return

    def getFiltered(self):
        return self._getBool(6)

    def setFiltered(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(MapsBlacklistSlotModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addStringProperty(b'state')
        self._addStringProperty(b'mapId', b'')
        self._addNumberProperty(b'seasonId', 0)
        self._addNumberProperty(b'cooldownTime', 0)
        self._addNumberProperty(b'expirationTime', 0)
        self._addBoolProperty(b'filtered', True)
        return
