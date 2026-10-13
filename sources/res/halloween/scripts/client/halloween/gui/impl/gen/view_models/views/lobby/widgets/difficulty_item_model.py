from enum import Enum
from frameworks.wulf import ViewModel

class StateEnum(Enum):
    DEFAULT = b'default'
    SELECTED = b'selected'


class DifficultyItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DifficultyItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getIsNew(self):
        return self._getBool(1)

    def setIsNew(self, value):
        self._setBool(1, value)
        return

    def getIsLocked(self):
        return self._getBool(2)

    def setIsLocked(self, value):
        self._setBool(2, value)
        return

    def getState(self):
        return StateEnum(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(DifficultyItemModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'isLocked', False)
        self._addStringProperty(b'state')
        return
