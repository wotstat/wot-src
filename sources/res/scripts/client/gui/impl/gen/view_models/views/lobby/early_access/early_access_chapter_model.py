from enum import Enum
from frameworks.wulf import ViewModel

class ChapterState(Enum):
    DISABLED = b'disabled'
    ACTIVE = b'active'
    COMPLETED = b'completed'


class EarlyAccessChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(EarlyAccessChapterModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getState(self):
        return ChapterState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getCompletedQuestsAll(self):
        return self._getNumber(2)

    def setCompletedQuestsAll(self, value):
        self._setNumber(2, value)
        return

    def getCompletedQuestsNew(self):
        return self._getNumber(3)

    def setCompletedQuestsNew(self, value):
        self._setNumber(3, value)
        return

    def getTotalQuests(self):
        return self._getNumber(4)

    def setTotalQuests(self, value):
        self._setNumber(4, value)
        return

    def getShowTokens(self):
        return self._getBool(5)

    def setShowTokens(self, value):
        self._setBool(5, value)
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

    def _initialize(self):
        super(EarlyAccessChapterModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'state')
        self._addNumberProperty(b'completedQuestsAll', 0)
        self._addNumberProperty(b'completedQuestsNew', 0)
        self._addNumberProperty(b'totalQuests', 0)
        self._addBoolProperty(b'showTokens', False)
        self._addNumberProperty(b'receivedTokens', 0)
        self._addNumberProperty(b'totalTokens', 0)
        return
