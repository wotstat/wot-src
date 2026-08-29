from enum import Enum
from frameworks.wulf import ViewModel

class TabType(Enum):
    PROGRESS = b'progress'
    REWARDS = b'rewards'
    INFO = b'info'
    SUPPLY = b'supply'


class FrontlineContainerTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FrontlineContainerTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return TabType(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getIsHighlighted(self):
        return self._getBool(2)

    def setIsHighlighted(self, value):
        self._setBool(2, value)
        return

    def getResId(self):
        return self._getNumber(3)

    def setResId(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(FrontlineContainerTabModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'type')
        self._addBoolProperty(b'isHighlighted', False)
        self._addNumberProperty(b'resId', 0)
        return
