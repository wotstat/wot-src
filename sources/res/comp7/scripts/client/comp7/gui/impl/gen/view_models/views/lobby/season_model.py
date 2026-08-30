from enum import IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from frameworks.wulf import ViewModel

class SeasonState(IntEnum):
    NOTSTARTED = 0
    JUSTSTARTED = 1
    ACTIVE = 2
    ENDSOON = 3
    END = 4
    DISABLED = 5


class SeasonModel(ViewModel):
    __slots__ = (b'pollServerTime',)

    def __init__(self, properties=6, commands=1):
        super(SeasonModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return SeasonName(self._getString(0))

    def setName(self, value):
        self._setString(0, value.value)
        return

    def getStartTimestamp(self):
        return self._getNumber(1)

    def setStartTimestamp(self, value):
        self._setNumber(1, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(3)

    def setServerTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getState(self):
        return SeasonState(self._getNumber(4))

    def setState(self, value):
        self._setNumber(4, value.value)
        return

    def getHasTentativeDates(self):
        return self._getBool(5)

    def setHasTentativeDates(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(SeasonModel, self)._initialize()
        self._addStringProperty(b'name')
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self._addNumberProperty(b'state')
        self._addBoolProperty(b'hasTentativeDates', False)
        self.pollServerTime = self._addCommand(b'pollServerTime')
        return
