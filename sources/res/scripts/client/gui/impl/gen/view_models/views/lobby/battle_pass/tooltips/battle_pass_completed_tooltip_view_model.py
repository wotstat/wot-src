from enum import Enum
from frameworks.wulf import ViewModel

class ChapterType(Enum):
    COMMON = b'common'
    EXTRA = b'extra'
    HOLIDAY = b'holiday'


class BattlePassCompletedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BattlePassCompletedTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(0)

    def setIsBattlePassPurchased(self, value):
        self._setBool(0, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(1)

    def setNotChosenRewardCount(self, value):
        self._setNumber(1, value)
        return

    def getIsAvailableTankmen(self):
        return self._getBool(2)

    def setIsAvailableTankmen(self, value):
        self._setBool(2, value)
        return

    def getChapterType(self):
        return ChapterType(self._getString(3))

    def setChapterType(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(BattlePassCompletedTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isBattlePassPurchased', False)
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addBoolProperty(b'isAvailableTankmen', False)
        self._addStringProperty(b'chapterType')
        return
