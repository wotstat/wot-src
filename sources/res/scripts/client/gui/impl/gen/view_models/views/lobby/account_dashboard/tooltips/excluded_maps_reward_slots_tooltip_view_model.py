from enum import Enum
from frameworks.wulf import ViewModel

class MapStateEnum(Enum):
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE = b'active'
    MAPS_BLACKLIST_SLOT_STATE_CHANGE = b'change'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED = b'disabled'
    MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = b'cooldown'
    MAPS_BLACKLIST_SLOT_STATE_SELECTED = b'selected'
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = b'activeNoHover'


class ExcludedMapsRewardSlotsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ExcludedMapsRewardSlotsTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return MapStateEnum(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getCooldownTime(self):
        return self._getNumber(1)

    def setCooldownTime(self, value):
        self._setNumber(1, value)
        return

    def getExpirationTime(self):
        return self._getNumber(2)

    def setExpirationTime(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(ExcludedMapsRewardSlotsTooltipViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'cooldownTime', 0)
        self._addNumberProperty(b'expirationTime', 0)
        return
