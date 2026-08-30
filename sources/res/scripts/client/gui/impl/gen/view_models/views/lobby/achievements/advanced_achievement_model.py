from enum import Enum
from frameworks.wulf import ViewModel

class AdvancedAchievementType(Enum):
    SINGLE = b'single'
    CUMULATIVE = b'cumulative'
    STAGED = b'staged'
    SUBCATEGORY = b'subcategory'
    CATEGORY = b'Category'


class AdvancedAchievementIconPosition(Enum):
    TOP = b'top'
    CENTER = b'center'
    BOTTOM = b'bottom'


class AdvancedAchievementIconSizeMap(Enum):
    DEFAULT = b''
    PERSONALMISSIONS = b'personal_missions'


class AdvancedAchievementModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(AdvancedAchievementModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return AdvancedAchievementType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getKey(self):
        return self._getString(1)

    def setKey(self, value):
        self._setString(1, value)
        return

    def getCategory(self):
        return self._getString(2)

    def setCategory(self, value):
        self._setString(2, value)
        return

    def getId(self):
        return self._getNumber(3)

    def setId(self, value):
        self._setNumber(3, value)
        return

    def getBackground(self):
        return self._getString(4)

    def setBackground(self, value):
        self._setString(4, value)
        return

    def getTheme(self):
        return self._getString(5)

    def setTheme(self, value):
        self._setString(5, value)
        return

    def getIconPosition(self):
        return AdvancedAchievementIconPosition(self._getString(6))

    def setIconPosition(self, value):
        self._setString(6, value.value)
        return

    def getIconSizeMap(self):
        return AdvancedAchievementIconSizeMap(self._getString(7))

    def setIconSizeMap(self, value):
        self._setString(7, value.value)
        return

    def getCurrentValue(self):
        return self._getNumber(8)

    def setCurrentValue(self, value):
        self._setNumber(8, value)
        return

    def getMaxValue(self):
        return self._getNumber(9)

    def setMaxValue(self, value):
        self._setNumber(9, value)
        return

    def getAchievementScore(self):
        return self._getNumber(10)

    def setAchievementScore(self, value):
        self._setNumber(10, value)
        return

    def getStage(self):
        return self._getNumber(11)

    def setStage(self, value):
        self._setNumber(11, value)
        return

    def getIsTrophy(self):
        return self._getBool(12)

    def setIsTrophy(self, value):
        self._setBool(12, value)
        return

    def getReceivedDate(self):
        return self._getString(13)

    def setReceivedDate(self, value):
        self._setString(13, value)
        return

    def getReceivedShortDate(self):
        return self._getString(14)

    def setReceivedShortDate(self, value):
        self._setString(14, value)
        return

    def _initialize(self):
        super(AdvancedAchievementModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addStringProperty(b'key', b'')
        self._addStringProperty(b'category', b'')
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'background', b'')
        self._addStringProperty(b'theme', b'')
        self._addStringProperty(b'iconPosition')
        self._addStringProperty(b'iconSizeMap')
        self._addNumberProperty(b'currentValue', 0)
        self._addNumberProperty(b'maxValue', 0)
        self._addNumberProperty(b'achievementScore', 0)
        self._addNumberProperty(b'stage', 0)
        self._addBoolProperty(b'isTrophy', False)
        self._addStringProperty(b'receivedDate', b'')
        self._addStringProperty(b'receivedShortDate', b'')
        return
