from frameworks.wulf import ViewModel

class RectModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RectModel, self).__init__(properties=properties, commands=commands)
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

    def getWidth(self):
        return self._getNumber(2)

    def setWidth(self, value):
        self._setNumber(2, value)
        return

    def getHeight(self):
        return self._getNumber(3)

    def setHeight(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(RectModel, self)._initialize()
        self._addNumberProperty(b'x', 0)
        self._addNumberProperty(b'y', 0)
        self._addNumberProperty(b'width', 0)
        self._addNumberProperty(b'height', 0)
        return
