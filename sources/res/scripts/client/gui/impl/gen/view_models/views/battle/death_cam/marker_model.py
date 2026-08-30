from frameworks.wulf import ViewModel

class MarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MarkerModel, self).__init__(properties=properties, commands=commands)
        return

    def getPosx(self):
        return self._getReal(0)

    def setPosx(self, value):
        self._setReal(0, value)
        return

    def getPosy(self):
        return self._getReal(1)

    def setPosy(self, value):
        self._setReal(1, value)
        return

    def getNdcLimitX(self):
        return self._getReal(2)

    def setNdcLimitX(self, value):
        self._setReal(2, value)
        return

    def getNdcLimitY(self):
        return self._getReal(3)

    def setNdcLimitY(self, value):
        self._setReal(3, value)
        return

    def getIsVisible(self):
        return self._getBool(4)

    def setIsVisible(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(MarkerModel, self)._initialize()
        self._addRealProperty(b'posx', 0.0)
        self._addRealProperty(b'posy', 0.0)
        self._addRealProperty(b'ndcLimitX', 2.0)
        self._addRealProperty(b'ndcLimitY', 2.0)
        self._addBoolProperty(b'isVisible', False)
        return
