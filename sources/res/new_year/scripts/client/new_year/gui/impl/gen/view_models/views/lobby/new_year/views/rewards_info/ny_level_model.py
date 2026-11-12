from frameworks.wulf import ViewModel

class NyLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyLevelModel, self).__init__(properties=properties, commands=commands)
        return

    def getNumber(self):
        return self._getNumber(0)

    def setNumber(self, value):
        self._setNumber(0, value)
        return

    def getMaxPoints(self):
        return self._getNumber(1)

    def setMaxPoints(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(NyLevelModel, self)._initialize()
        self._addNumberProperty(b'number', 1)
        self._addNumberProperty(b'maxPoints', 0)
        return
