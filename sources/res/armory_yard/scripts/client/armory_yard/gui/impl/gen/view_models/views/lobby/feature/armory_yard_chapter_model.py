from enum import Enum, IntEnum
from frameworks.wulf import ViewModel

class ChapterState(Enum):
    DISABLED = b'disabled'
    ACTIVE = b'active'
    COMPLETED = b'completed'


class ChapterTokenState(IntEnum):
    HIDDEN = 0
    TOKENS = 1
    COINS = 2
    LOCK = 3


class ArmoryYardChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(ArmoryYardChapterModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return ChapterState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getCompletedQuestsNew(self):
        return self._getNumber(2)

    def setCompletedQuestsNew(self, value):
        self._setNumber(2, value)
        return

    def getCompletedQuestsAll(self):
        return self._getNumber(3)

    def setCompletedQuestsAll(self, value):
        self._setNumber(3, value)
        return

    def getTotalQuests(self):
        return self._getNumber(4)

    def setTotalQuests(self, value):
        self._setNumber(4, value)
        return

    def getTokenState(self):
        return ChapterTokenState(self._getNumber(5))

    def setTokenState(self, value):
        self._setNumber(5, value.value)
        return

    def getReceivedTokens(self):
        return self._getNumber(6)

    def setReceivedTokens(self, value):
        self._setNumber(6, value)
        return

    def getTotalTokens(self):
        return self._getNumber(7)

    def setTotalTokens(self, value):
        self._setNumber(7, value)
        return

    def getIsPostProgression(self):
        return self._getBool(8)

    def setIsPostProgression(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(ArmoryYardChapterModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'state')
        self._addNumberProperty(b'completedQuestsNew', 0)
        self._addNumberProperty(b'completedQuestsAll', 0)
        self._addNumberProperty(b'totalQuests', 0)
        self._addNumberProperty(b'tokenState')
        self._addNumberProperty(b'receivedTokens', 0)
        self._addNumberProperty(b'totalTokens', 0)
        self._addBoolProperty(b'isPostProgression', False)
        return
