from frameworks.wulf import ViewModel

class CoordinateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CoordinateModel, self).__init__(properties=properties, commands=commands)
        return

    def getX(self):
        return self._getNumber(0)

    def setX(self, value):
        self._setNumber(0, value)
        return

    def getY(self):
        return self._getNumber(1)

    def setY(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(CoordinateModel, self)._initialize()
        self._addNumberProperty(b'x', 0)
        self._addNumberProperty(b'y', 0)
        return
