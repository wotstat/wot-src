from enum import IntEnum
from frameworks.wulf import ViewModel

class ChapterStatus(IntEnum):
    ACTIVE = 0
    PAUSED = 1
    COMPLETED = 2
    NOTSTARTED = 3


class ChapterSimpleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ChapterSimpleModel, self).__init__(properties=properties, commands=commands)
        return

    def getChapterID(self):
        return self._getNumber(0)

    def setChapterID(self, value):
        self._setNumber(0, value)
        return

    def getChapterStatus(self):
        return ChapterStatus(self._getNumber(1))

    def setChapterStatus(self, value):
        self._setNumber(1, value.value)
        return

    def getIsRegular(self):
        return self._getBool(2)

    def setIsRegular(self, value):
        self._setBool(2, value)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(3)

    def setIsBattlePassPurchased(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ChapterSimpleModel, self)._initialize()
        self._addNumberProperty(b'chapterID', 0)
        self._addNumberProperty(b'chapterStatus')
        self._addBoolProperty(b'isRegular', False)
        self._addBoolProperty(b'isBattlePassPurchased', False)
        return
