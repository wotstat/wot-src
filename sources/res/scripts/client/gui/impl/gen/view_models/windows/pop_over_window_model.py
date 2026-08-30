from gui.impl.gen.view_models.windows.window_model import WindowModel

class PopOverWindowModel(WindowModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(PopOverWindowModel, self).__init__(properties=properties, commands=commands)
        return

    def getBoundX(self):
        return self._getNumber(3)

    def setBoundX(self, value):
        self._setNumber(3, value)
        return

    def getBoundY(self):
        return self._getNumber(4)

    def setBoundY(self, value):
        self._setNumber(4, value)
        return

    def getBoundWidth(self):
        return self._getNumber(5)

    def setBoundWidth(self, value):
        self._setNumber(5, value)
        return

    def getBoundHeight(self):
        return self._getNumber(6)

    def setBoundHeight(self, value):
        self._setNumber(6, value)
        return

    def getDirectionType(self):
        return self._getNumber(7)

    def setDirectionType(self, value):
        self._setNumber(7, value)
        return

    def getIsCloseBtnVisible(self):
        return self._getBool(8)

    def setIsCloseBtnVisible(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(PopOverWindowModel, self)._initialize()
        self._addNumberProperty(b'boundX', 0)
        self._addNumberProperty(b'boundY', 0)
        self._addNumberProperty(b'boundWidth', 0)
        self._addNumberProperty(b'boundHeight', 0)
        self._addNumberProperty(b'directionType', 0)
        self._addBoolProperty(b'isCloseBtnVisible', True)
        return
