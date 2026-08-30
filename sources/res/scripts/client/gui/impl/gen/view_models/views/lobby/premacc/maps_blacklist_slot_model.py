from enum import Enum
from frameworks.wulf import ViewModel

class MapStateEnum(Enum):
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE = b'active'
    MAPS_BLACKLIST_SLOT_STATE_CHANGE = b'change'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED = b'disabled'
    MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = b'cooldown'
    MAPS_BLACKLIST_SLOT_STATE_SELECTED = b'selected'
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = b'active_no_hover'


class SlotTypeEnum(Enum):
    NONE = b'none'
    PREMIUM = b'premium'
    WOTPLUS = b'wotplus'


class MapsBlacklistSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MapsBlacklistSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return MapStateEnum(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)
        return

    def getSeasonId(self):
        return self._getNumber(2)

    def setSeasonId(self, value):
        self._setNumber(2, value)
        return

    def getCooldownTime(self):
        return self._getNumber(3)

    def setCooldownTime(self, value):
        self._setNumber(3, value)
        return

    def getFiltered(self):
        return self._getBool(4)

    def setFiltered(self, value):
        self._setBool(4, value)
        return

    def getSlotType(self):
        return SlotTypeEnum(self._getString(5))

    def setSlotType(self, value):
        self._setString(5, value.value)
        return

    def _initialize(self):
        super(MapsBlacklistSlotModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'mapId', b'')
        self._addNumberProperty(b'seasonId', 0)
        self._addNumberProperty(b'cooldownTime', 0)
        self._addBoolProperty(b'filtered', True)
        self._addStringProperty(b'slotType', SlotTypeEnum.NONE.value)
        return
