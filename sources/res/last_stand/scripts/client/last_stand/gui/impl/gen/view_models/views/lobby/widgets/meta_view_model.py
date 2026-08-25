from enum import Enum
from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class ArtefactStates(Enum):
    NONE = b'none'
    INPROGRESS = b'inProgress'
    RECEIVE = b'receive'
    OPEN = b'open'


class MetaViewModel(ViewModel):
    __slots__ = (b'onSkip', b'onDecrypt', b'onView', b'onSlideToNext')

    def __init__(self, properties=11, commands=4):
        super(MetaViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonus(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusType():
        return BonusItemViewModel

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getIndex(self):
        return self._getNumber(2)

    def setIndex(self, value):
        self._setNumber(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getSkipPrice(self):
        return self._getNumber(5)

    def setSkipPrice(self, value):
        self._setNumber(5, value)
        return

    def getDecodePrice(self):
        return self._getNumber(6)

    def setDecodePrice(self, value):
        self._setNumber(6, value)
        return

    def getKeys(self):
        return self._getNumber(7)

    def setKeys(self, value):
        self._setNumber(7, value)
        return

    def getState(self):
        return ArtefactStates(self._getString(8))

    def setState(self, value):
        self._setString(8, value.value)
        return

    def getTypes(self):
        return self._getArray(9)

    def setTypes(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getTypesType():
        return unicode

    def getHasProminentReward(self):
        return self._getBool(10)

    def setHasProminentReward(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(MetaViewModel, self)._initialize()
        self._addViewModelProperty(b'bonus', BonusItemViewModel())
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'skipPrice', 0)
        self._addNumberProperty(b'decodePrice', 0)
        self._addNumberProperty(b'keys', 0)
        self._addStringProperty(b'state')
        self._addArrayProperty(b'types', Array())
        self._addBoolProperty(b'hasProminentReward', False)
        self.onSkip = self._addCommand(b'onSkip')
        self.onDecrypt = self._addCommand(b'onDecrypt')
        self.onView = self._addCommand(b'onView')
        self.onSlideToNext = self._addCommand(b'onSlideToNext')
        return
