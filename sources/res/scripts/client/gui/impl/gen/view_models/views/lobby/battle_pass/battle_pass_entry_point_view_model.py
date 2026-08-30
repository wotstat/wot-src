from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class AnimationState(Enum):
    NORMAL = b'normal'
    NEW_LEVEL = b'newLevel'
    BUY_BATTLE_PASS = b'buyBattlePass'
    NOT_TAKEN_REWARDS = b'notTakenRewards'
    PROGRESSION_COMPLETED = b'progressionCompleted'
    NEW_CHAPTER = b'newChapter'
    CHANGE_PROGRESS = b'changeProgress'
    CHAPTER_NOT_CHOSEN = b'chapterNotChosen'


class BPState(Enum):
    DISABLED = b'disabled'
    SEASON_WAITING = b'seasonWaiting'
    NORMAL = b'normal'
    ATTENTION = b'attention'


class ChapterType(Enum):
    DEFAULT = b'default'
    MARATHON = b'marathon'
    RESOURCE = b'resource'


class BattlePassEntryPointViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=22, commands=1):
        super(BattlePassEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getChapterType(self):
        return ChapterType(self._getString(0))

    def setChapterType(self, value):
        self._setString(0, value.value)
        return

    def getAvailableChapterTypes(self):
        return self._getArray(1)

    def setAvailableChapterTypes(self, value):
        self._setArray(1, value)
        return

    def getIsResourceAvailable(self):
        return self._getBool(2)

    def setIsResourceAvailable(self, value):
        self._setBool(2, value)
        return

    def getPrevLevel(self):
        return self._getNumber(3)

    def setPrevLevel(self, value):
        self._setNumber(3, value)
        return

    def getLevel(self):
        return self._getNumber(4)

    def setLevel(self, value):
        self._setNumber(4, value)
        return

    def getPrevProgression(self):
        return self._getReal(5)

    def setPrevProgression(self, value):
        self._setReal(5, value)
        return

    def getProgression(self):
        return self._getReal(6)

    def setProgression(self, value):
        self._setReal(6, value)
        return

    def getBattlePassState(self):
        return BPState(self._getString(7))

    def setBattlePassState(self, value):
        self._setString(7, value.value)
        return

    def getIsSmall(self):
        return self._getBool(8)

    def setIsSmall(self, value):
        self._setBool(8, value)
        return

    def getTooltipID(self):
        return self._getNumber(9)

    def setTooltipID(self, value):
        self._setNumber(9, value)
        return

    def getIsFirstShow(self):
        return self._getBool(10)

    def setIsFirstShow(self, value):
        self._setBool(10, value)
        return

    def getAnimState(self):
        return AnimationState(self._getString(11))

    def setAnimState(self, value):
        self._setString(11, value.value)
        return

    def getAnimStateKey(self):
        return self._getNumber(12)

    def setAnimStateKey(self, value):
        self._setNumber(12, value)
        return

    def getIsProgressionCompleted(self):
        return self._getBool(13)

    def setIsProgressionCompleted(self, value):
        self._setBool(13, value)
        return

    def getHasBattlePass(self):
        return self._getBool(14)

    def setHasBattlePass(self, value):
        self._setBool(14, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(15)

    def setNotChosenRewardCount(self, value):
        self._setNumber(15, value)
        return

    def getPreviousChapterID(self):
        return self._getNumber(16)

    def setPreviousChapterID(self, value):
        self._setNumber(16, value)
        return

    def getChapterID(self):
        return self._getNumber(17)

    def setChapterID(self, value):
        self._setNumber(17, value)
        return

    def getBattleType(self):
        return self._getString(18)

    def setBattleType(self, value):
        self._setString(18, value)
        return

    def getIsChapterChosen(self):
        return self._getBool(19)

    def setIsChapterChosen(self, value):
        self._setBool(19, value)
        return

    def getFreePoints(self):
        return self._getNumber(20)

    def setFreePoints(self, value):
        self._setNumber(20, value)
        return

    def getShowHint(self):
        return self._getBool(21)

    def setShowHint(self, value):
        self._setBool(21, value)
        return

    def _initialize(self):
        super(BattlePassEntryPointViewModel, self)._initialize()
        self._addStringProperty(b'chapterType')
        self._addArrayProperty(b'availableChapterTypes', Array())
        self._addBoolProperty(b'isResourceAvailable', False)
        self._addNumberProperty(b'prevLevel', 0)
        self._addNumberProperty(b'level', 0)
        self._addRealProperty(b'prevProgression', 0.0)
        self._addRealProperty(b'progression', -1)
        self._addStringProperty(b'battlePassState')
        self._addBoolProperty(b'isSmall', False)
        self._addNumberProperty(b'tooltipID', 0)
        self._addBoolProperty(b'isFirstShow', False)
        self._addStringProperty(b'animState')
        self._addNumberProperty(b'animStateKey', 0)
        self._addBoolProperty(b'isProgressionCompleted', False)
        self._addBoolProperty(b'hasBattlePass', False)
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addNumberProperty(b'previousChapterID', 0)
        self._addNumberProperty(b'chapterID', 0)
        self._addStringProperty(b'battleType', b'')
        self._addBoolProperty(b'isChapterChosen', False)
        self._addNumberProperty(b'freePoints', 0)
        self._addBoolProperty(b'showHint', False)
        self.onClick = self._addCommand(b'onClick')
        return
