from enum import Enum
from frameworks.wulf import ViewModel

class BattleStatus(Enum):
    INPROGRESS = b'inProgress'
    COMPLETED = b'completed'


class WidgetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattleStatus(self):
        return BattleStatus(self._getString(0))

    def setBattleStatus(self, value):
        self._setString(0, value.value)
        return

    def getCurrentProgression(self):
        return self._getNumber(1)

    def setCurrentProgression(self, value):
        self._setNumber(1, value)
        return

    def getIsAlertMode(self):
        return self._getBool(2)

    def setIsAlertMode(self, value):
        self._setBool(2, value)
        return

    def getIconPostfix(self):
        return self._getString(3)

    def setIconPostfix(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(WidgetViewModel, self)._initialize()
        self._addStringProperty(b'battleStatus')
        self._addNumberProperty(b'currentProgression', 0)
        self._addBoolProperty(b'isAlertMode', False)
        self._addStringProperty(b'iconPostfix', b'')
        return
