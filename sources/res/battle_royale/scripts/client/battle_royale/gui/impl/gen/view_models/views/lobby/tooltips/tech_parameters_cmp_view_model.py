from frameworks.wulf import ViewModel

class TechParametersCmpViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TechParametersCmpViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDifficulty(self):
        return self._getNumber(0)

    def setDifficulty(self, value):
        self._setNumber(0, value)
        return

    def getSpotting(self):
        return self._getNumber(1)

    def setSpotting(self, value):
        self._setNumber(1, value)
        return

    def getMobility(self):
        return self._getNumber(2)

    def setMobility(self, value):
        self._setNumber(2, value)
        return

    def getSurvivability(self):
        return self._getNumber(3)

    def setSurvivability(self, value):
        self._setNumber(3, value)
        return

    def getDamage(self):
        return self._getNumber(4)

    def setDamage(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(TechParametersCmpViewModel, self)._initialize()
        self._addNumberProperty(b'difficulty', 0)
        self._addNumberProperty(b'spotting', 0)
        self._addNumberProperty(b'mobility', 0)
        self._addNumberProperty(b'survivability', 0)
        self._addNumberProperty(b'damage', 0)
        return
