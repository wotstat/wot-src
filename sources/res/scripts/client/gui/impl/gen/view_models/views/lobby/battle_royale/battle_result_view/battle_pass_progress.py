from enum import Enum
from frameworks.wulf import ViewModel

class ChapterStates(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'
    COMPLETED = b'completed'


class BattlePassProgress(ViewModel):
    __slots__ = (b'onSubmitClick',)
    BP_STATE_NORMAL = b'normal'
    BP_STATE_BOUGHT = b'bought'
    BP_STATE_DISABLED = b'disabled'
    PROGRESSION_IN_PROGRESS = b'progressionInProgress'
    PROGRESSION_COMPLETED = b'progressionCompleted'

    def __init__(self, properties=14, commands=1):
        super(BattlePassProgress, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentLevel(self):
        return self._getNumber(0)

    def setCurrentLevel(self, value):
        self._setNumber(0, value)
        return

    def getMaxPoints(self):
        return self._getNumber(1)

    def setMaxPoints(self, value):
        self._setNumber(1, value)
        return

    def getEarnedPoints(self):
        return self._getNumber(2)

    def setEarnedPoints(self, value):
        self._setNumber(2, value)
        return

    def getCurrentLevelPoints(self):
        return self._getNumber(3)

    def setCurrentLevelPoints(self, value):
        self._setNumber(3, value)
        return

    def getProgressionState(self):
        return self._getString(4)

    def setProgressionState(self, value):
        self._setString(4, value)
        return

    def getBattlePassState(self):
        return self._getString(5)

    def setBattlePassState(self, value):
        self._setString(5, value)
        return

    def getChapterID(self):
        return self._getNumber(6)

    def setChapterID(self, value):
        self._setNumber(6, value)
        return

    def getHasExtra(self):
        return self._getBool(7)

    def setHasExtra(self, value):
        self._setBool(7, value)
        return

    def getHasResource(self):
        return self._getBool(8)

    def setHasResource(self, value):
        self._setBool(8, value)
        return

    def getChapterState(self):
        return ChapterStates(self._getString(9))

    def setChapterState(self, value):
        self._setString(9, value.value)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(10)

    def setIsBattlePassPurchased(self, value):
        self._setBool(10, value)
        return

    def getFreePoints(self):
        return self._getNumber(11)

    def setFreePoints(self, value):
        self._setNumber(11, value)
        return

    def getIsSingleChapter(self):
        return self._getBool(12)

    def setIsSingleChapter(self, value):
        self._setBool(12, value)
        return

    def getIsBpPointsShopEntryPointActive(self):
        return self._getBool(13)

    def setIsBpPointsShopEntryPointActive(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(BattlePassProgress, self)._initialize()
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'maxPoints', 0)
        self._addNumberProperty(b'earnedPoints', 0)
        self._addNumberProperty(b'currentLevelPoints', 0)
        self._addStringProperty(b'progressionState', b'')
        self._addStringProperty(b'battlePassState', b'')
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'hasExtra', False)
        self._addBoolProperty(b'hasResource', False)
        self._addStringProperty(b'chapterState')
        self._addBoolProperty(b'isBattlePassPurchased', False)
        self._addNumberProperty(b'freePoints', 0)
        self._addBoolProperty(b'isSingleChapter', False)
        self._addBoolProperty(b'isBpPointsShopEntryPointActive', False)
        self.onSubmitClick = self._addCommand(b'onSubmitClick')
        return
