from enum import Enum
from frameworks.wulf import ViewModel

class WidgetState(Enum):
    DISABLED = b'disabled'
    INRACE = b'inRace'
    FINISHED = b'finished'
    NOTFINISHED = b'notFinished'


class FallTanksBattleWidgetModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FallTanksBattleWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getObservable(self):
        return self._getBool(0)

    def setObservable(self, value):
        self._setBool(0, value)
        return

    def getCheckpoint(self):
        return self._getNumber(1)

    def setCheckpoint(self, value):
        self._setNumber(1, value)
        return

    def getPosition(self):
        return self._getNumber(2)

    def setPosition(self, value):
        self._setNumber(2, value)
        return

    def getSpentTime(self):
        return self._getReal(3)

    def setSpentTime(self, value):
        self._setReal(3, value)
        return

    def getState(self):
        return WidgetState(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(FallTanksBattleWidgetModel, self)._initialize()
        self._addBoolProperty(b'observable', False)
        self._addNumberProperty(b'checkpoint', -1)
        self._addNumberProperty(b'position', 0)
        self._addRealProperty(b'spentTime', 0.0)
        self._addStringProperty(b'state', WidgetState.DISABLED.value)
        return
