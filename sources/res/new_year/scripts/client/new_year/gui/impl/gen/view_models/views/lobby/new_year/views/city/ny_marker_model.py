from frameworks.wulf import ViewModel

class NyMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NyMarkerModel, self).__init__(properties=properties, commands=commands)
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

    def getScale(self):
        return self._getReal(2)

    def setScale(self, value):
        self._setReal(2, value)
        return

    def getAngle(self):
        return self._getReal(3)

    def setAngle(self, value):
        self._setReal(3, value)
        return

    def getIsVisible(self):
        return self._getBool(4)

    def setIsVisible(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(NyMarkerModel, self)._initialize()
        self._addRealProperty(b'posx', 0.0)
        self._addRealProperty(b'posy', 0.0)
        self._addRealProperty(b'scale', 0.0)
        self._addRealProperty(b'angle', 0.0)
        self._addBoolProperty(b'isVisible', True)
        return
