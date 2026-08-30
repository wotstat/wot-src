from enum import Enum
from frameworks.wulf import ViewModel

class AchievementType(Enum):
    REPEATABLE = b'repeatable'
    CLASS = b'class'
    CUSTOM = b'custom'
    SERIES = b'series'
    SINGLE = b'single'
    RARE = b'rare'


class CounterType(Enum):
    NONE = b'none'
    SIMPLE = b'simple'
    SERIES = b'series'
    STAGES = b'stages'


class AchievementModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(AchievementModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getResourceName(self):
        return self._getString(1)

    def setResourceName(self, value):
        self._setString(1, value)
        return

    def getBlock(self):
        return self._getString(2)

    def setBlock(self, value):
        self._setString(2, value)
        return

    def getType(self):
        return AchievementType(self._getString(3))

    def setType(self, value):
        self._setString(3, value.value)
        return

    def getCounterType(self):
        return CounterType(self._getString(4))

    def setCounterType(self, value):
        self._setString(4, value.value)
        return

    def getValue(self):
        return self._getNumber(5)

    def setValue(self, value):
        self._setNumber(5, value)
        return

    def getRareIconId(self):
        return self._getString(6)

    def setRareIconId(self, value):
        self._setString(6, value)
        return

    def getRareBigIconId(self):
        return self._getString(7)

    def setRareBigIconId(self, value):
        self._setString(7, value)
        return

    def getIsNew(self):
        return self._getBool(8)

    def setIsNew(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(AchievementModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'resourceName', b'')
        self._addStringProperty(b'block', b'')
        self._addStringProperty(b'type')
        self._addStringProperty(b'counterType')
        self._addNumberProperty(b'value', 0)
        self._addStringProperty(b'rareIconId', b'')
        self._addStringProperty(b'rareBigIconId', b'')
        self._addBoolProperty(b'isNew', False)
        return
