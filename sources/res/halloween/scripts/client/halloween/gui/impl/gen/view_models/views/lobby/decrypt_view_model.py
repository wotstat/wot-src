from enum import Enum
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class ArtefactTypes(Enum):
    TEXT = b'text'
    SOUND = b'sound'
    FINAL = b'final'


class DecryptViewModel(ViewModel):
    __slots__ = (b'onAffirmation', b'onMuted', b'onOutroVideo', b'onChangeQuest')

    def __init__(self, properties=11, commands=4):
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

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIsMuted(self):
        return self._getBool(3)

    def setIsMuted(self, value):
        self._setBool(3, value)
        return

    def getIsOutroDisabled(self):
        return self._getBool(4)

    def setIsOutroDisabled(self, value):
        self._setBool(4, value)
        return

    def getIsOutroVisible(self):
        return self._getBool(5)

    def setIsOutroVisible(self, value):
        self._setBool(5, value)
        return

    def getIsTransition(self):
        return self._getBool(6)

    def setIsTransition(self, value):
        self._setBool(6, value)
        return

    def getIsNextArtefactAvailable(self):
        return self._getBool(7)

    def setIsNextArtefactAvailable(self, value):
        self._setBool(7, value)
        return

    def getIsPreviousArtefactAvailable(self):
        return self._getBool(8)

    def setIsPreviousArtefactAvailable(self, value):
        self._setBool(8, value)
        return

    def getRewards(self):
        return self._getArray(9)

    def setRewards(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def getTypes(self):
        return self._getArray(10)

    def setTypes(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getTypesType():
        return unicode

    def _initialize(self):
        super(DecryptViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isMuted', False)
        self._addBoolProperty(b'isOutroDisabled', False)
        self._addBoolProperty(b'isOutroVisible', True)
        self._addBoolProperty(b'isTransition', False)
        self._addBoolProperty(b'isNextArtefactAvailable', False)
        self._addBoolProperty(b'isPreviousArtefactAvailable', False)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'types', Array())
        self.onAffirmation = self._addCommand(b'onAffirmation')
        self.onMuted = self._addCommand(b'onMuted')
        self.onOutroVideo = self._addCommand(b'onOutroVideo')
        self.onChangeQuest = self._addCommand(b'onChangeQuest')
        return
