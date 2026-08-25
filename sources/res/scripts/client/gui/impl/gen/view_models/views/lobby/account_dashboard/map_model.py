from enum import Enum
from frameworks.wulf import ViewModel

class SlotStateEnum(Enum):
    EMPTY = b'empty'
    SELECTED = b'selected'
    DISABLED = b'disabled'


class SlotTypeEnum(Enum):
    NONE = b'none'
    PREMIUM = b'premium'
    WOTPLUS = b'wotplus'


class MapModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MapModel, self).__init__(properties=properties, commands=commands)
        return

    def getCooldownEndTimeInSecs(self):
        return self._getNumber(0)

    def setCooldownEndTimeInSecs(self, value):
        self._setNumber(0, value)
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

    def getSlotType(self):
        return SlotTypeEnum(self._getString(3))

    def setSlotType(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(MapModel, self)._initialize()
        self._addNumberProperty(b'cooldownEndTimeInSecs', 0)
        self._addStringProperty(b'mapId', b'')
        self._addStringProperty(b'slotState')
        self._addStringProperty(b'slotType', SlotTypeEnum.NONE.value)
        return
