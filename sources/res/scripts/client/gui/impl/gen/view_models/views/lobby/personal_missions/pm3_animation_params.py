from frameworks.wulf import ViewModel

class Pm3AnimationParams(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(Pm3AnimationParams, self).__init__(properties=properties, commands=commands)
        return

    def getStart(self):
        return self._getNumber(0)

    def setStart(self, value):
        self._setNumber(0, value)
        return

    def getEnd(self):
        return self._getNumber(1)

    def setEnd(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(Pm3AnimationParams, self)._initialize()
        self._addNumberProperty(b'start', 0)
        self._addNumberProperty(b'end', 0)
        return
