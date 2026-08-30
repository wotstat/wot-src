from enum import Enum
from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class ArtefactTypes(Enum):
    TEXT = b'text'
    SOUND = b'sound'
    FINAL = b'final'


class DecryptViewModel(ViewModel):
    __slots__ = (b'onAffirmation', b'onMuted')

    def __init__(self, properties=8, commands=2):
        super(DecryptViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIndex(self):
        return self._getNumber(1)

    def setIndex(self, value):
        self._setNumber(1, value)
        return

    def getSelectedDifficulty(self):
        return self._getNumber(2)

    def setSelectedDifficulty(self, value):
        self._setNumber(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getIsMuted(self):
        return self._getBool(4)

    def setIsMuted(self, value):
        self._setBool(4, value)
        return

    def getIsTransition(self):
        return self._getBool(5)

    def setIsTransition(self, value):
        self._setBool(5, value)
        return

    def getRewards(self):
        return self._getArray(6)

    def setRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def getTypes(self):
        return self._getArray(7)

    def setTypes(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getTypesType():
        return unicode

    def _initialize(self):
        super(DecryptViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addNumberProperty(b'selectedDifficulty', 0)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isMuted', False)
        self._addBoolProperty(b'isTransition', False)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'types', Array())
        self.onAffirmation = self._addCommand(b'onAffirmation')
        self.onMuted = self._addCommand(b'onMuted')
        return
