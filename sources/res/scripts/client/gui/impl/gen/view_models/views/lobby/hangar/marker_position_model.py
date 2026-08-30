from frameworks.wulf import ViewModel

class MarkerPositionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MarkerPositionModel, self).__init__(properties=properties, commands=commands)
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

    def getScale(self):
        return self._getReal(4)

    def setScale(self, value):
        self._setReal(4, value)
        return

    def getIsVisible(self):
        return self._getBool(5)

    def setIsVisible(self, value):
        self._setBool(5, value)
        return

    def getAngle(self):
        return self._getReal(6)

    def setAngle(self, value):
        self._setReal(6, value)
        return

    def getDistance(self):
        return self._getNumber(7)

    def setDistance(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(MarkerPositionModel, self)._initialize()
        self._addRealProperty(b'posx', 0.0)
        self._addRealProperty(b'posy', 0.0)
        self._addRealProperty(b'ndcLimitX', 1.15)
        self._addRealProperty(b'ndcLimitY', 1.15)
        self._addRealProperty(b'scale', 0.0)
        self._addBoolProperty(b'isVisible', False)
        self._addRealProperty(b'angle', 0.0)
        self._addNumberProperty(b'distance', 0)
        return
