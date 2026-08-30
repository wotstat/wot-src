from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.player_model import PlayerModel
from gui.impl.gen.view_models.views.lobby.platoon.slot_label_element_model import SlotLabelElementModel

class PrebattleType(Enum):
    SQUAD = b'squad'
    EVENT = b'event'
    COMP7 = b'comp7'
    BATTLEROYAL = b'battle_royal'
    EPIC = b'epic'
    MAPBOX = b'mapbox'


class ErrorType(IntEnum):
    NONE = 0
    MODEOFFLINE = 1


class SlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(SlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def player(self):
        return self._getViewModel(0)

    @staticmethod
    def getPlayerType():
        return PlayerModel

    def getPrebattleType(self):
        return PrebattleType(self._getString(1))

    def setPrebattleType(self, value):
        self._setString(1, value.value)
        return

    def getSlotId(self):
        return self._getNumber(2)

    def setSlotId(self, value):
        self._setNumber(2, value)
        return

    def getIsSearching(self):
        return self._getBool(3)

    def setIsSearching(self, value):
        self._setBool(3, value)
        return

    def getSearchStartTime(self):
        return self._getNumber(4)

    def setSearchStartTime(self, value):
        self._setNumber(4, value)
        return

    def getIsEmpty(self):
        return self._getBool(5)

    def setIsEmpty(self, value):
        self._setBool(5, value)
        return

    def getIsDisabled(self):
        return self._getBool(6)

    def setIsDisabled(self, value):
        self._setBool(6, value)
        return

    def getIsInBattle(self):
        return self._getBool(7)

    def setIsInBattle(self, value):
        self._setBool(7, value)
        return

    def getInfoText(self):
        return self._getString(8)

    def setInfoText(self, value):
        self._setString(8, value)
        return

    def getEstimatedTime(self):
        return self._getString(9)

    def setEstimatedTime(self, value):
        self._setString(9, value)
        return

    def getErrorType(self):
        return ErrorType(self._getNumber(10))

    def setErrorType(self, value):
        self._setNumber(10, value.value)
        return

    def getSlotLabelElements(self):
        return self._getArray(11)

    def setSlotLabelElements(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getSlotLabelElementsType():
        return SlotLabelElementModel

    def _initialize(self):
        super(SlotModel, self)._initialize()
        self._addViewModelProperty(b'player', PlayerModel())
        self._addStringProperty(b'prebattleType')
        self._addNumberProperty(b'slotId', 0)
        self._addBoolProperty(b'isSearching', False)
        self._addNumberProperty(b'searchStartTime', 0)
        self._addBoolProperty(b'isEmpty', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isInBattle', False)
        self._addStringProperty(b'infoText', b'')
        self._addStringProperty(b'estimatedTime', b'')
        self._addNumberProperty(b'errorType')
        self._addArrayProperty(b'slotLabelElements', Array())
        return
