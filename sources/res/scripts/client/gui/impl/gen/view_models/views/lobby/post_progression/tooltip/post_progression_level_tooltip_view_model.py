from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel

class ModificationType(Enum):
    NONE = b'none'
    PAIRMODIFICATION = b'pairModification'
    FEATURE = b'feature'


class PostProgressionLevelTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PostProgressionLevelTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def modifier(self):
        return self._getViewModel(0)

    @staticmethod
    def getModifierType():
        return BonusesModel

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getType(self):
        return ModificationType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getNameRes(self):
        return self._getResource(3)

    def setNameRes(self, value):
        self._setResource(3, value)
        return

    def getIsUnlocked(self):
        return self._getBool(4)

    def setIsUnlocked(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(PostProgressionLevelTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'modifier', BonusesModel())
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'type')
        self._addResourceProperty(b'nameRes', R.invalid())
        self._addBoolProperty(b'isUnlocked', False)
        return
