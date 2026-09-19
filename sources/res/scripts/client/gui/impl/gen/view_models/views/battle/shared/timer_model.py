from frameworks.wulf import ViewModel

class TimerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TimerModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartTimestamp(self):
        return self._getNumber(0)

    def setStartTimestamp(self, value):
        self._setNumber(0, value)
        return

    def getElapsed(self):
        return self._getReal(1)

    def setElapsed(self, value):
        self._setReal(1, value)
        return

    def getDuration(self):
        return self._getReal(2)

    def setDuration(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(TimerModel, self)._initialize()
        self._addNumberProperty(b'startTimestamp', 0)
        self._addRealProperty(b'elapsed', 0.0)
        self._addRealProperty(b'duration', 0.0)
        return
