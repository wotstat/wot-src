from frameworks.wulf import ViewModel

class AtmosphereAnimationModel(ViewModel):
    __slots__ = (b'onAnimationEnd',)

    def __init__(self, properties=3, commands=1):
        super(AtmosphereAnimationModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlotId(self):
        return self._getNumber(0)

    def setSlotId(self, value):
        self._setNumber(0, value)
        return

    def getPoints(self):
        return self._getNumber(1)

    def setPoints(self, value):
        self._setNumber(1, value)
        return

    def getIsReady(self):
        return self._getBool(2)

    def setIsReady(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(AtmosphereAnimationModel, self)._initialize()
        self._addNumberProperty(b'slotId', 0)
        self._addNumberProperty(b'points', 0)
        self._addBoolProperty(b'isReady', False)
        self.onAnimationEnd = self._addCommand(b'onAnimationEnd')
        return
