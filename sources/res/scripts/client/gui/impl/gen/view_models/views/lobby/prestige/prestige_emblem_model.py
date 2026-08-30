from enum import Enum
from frameworks.wulf import ViewModel

class PrestigeLevelGrade(Enum):
    IRON = b'iron'
    BRONZE = b'bronze'
    SILVER = b'silver'
    GOLD = b'gold'
    ENAMEL = b'enamel'
    MAXIMUM = b'prestige'
    UNDEFINED = b'undefined'


class PrestigeEmblemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PrestigeEmblemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return PrestigeLevelGrade(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getGrade(self):
        return self._getNumber(2)

    def setGrade(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(PrestigeEmblemModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'grade', -1)
        return
