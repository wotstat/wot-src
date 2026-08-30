from frameworks.wulf import ViewModel

class DtComponentLayout(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DtComponentLayout, self).__init__(properties=properties, commands=commands)
        return

    def getMarginX(self):
        return self._getReal(0)

    def setMarginX(self, value):
        self._setReal(0, value)
        return

    def getMarginY(self):
        return self._getReal(1)

    def setMarginY(self, value):
        self._setReal(1, value)
        return

    def _initialize(self):
        super(DtComponentLayout, self)._initialize()
        self._addRealProperty(b'marginX', 0.0)
        self._addRealProperty(b'marginY', 0.0)
        return
