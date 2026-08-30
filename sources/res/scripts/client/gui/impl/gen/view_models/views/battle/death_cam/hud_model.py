from frameworks.wulf import ViewModel

class HudModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(HudModel, self).__init__(properties=properties, commands=commands)
        return

    def getBarsVisible(self):
        return self._getBool(0)

    def setBarsVisible(self, value):
        self._setBool(0, value)
        return

    def getIsFinalPhase(self):
        return self._getBool(1)

    def setIsFinalPhase(self, value):
        self._setBool(1, value)
        return

    def getRemainingTime(self):
        return self._getReal(2)

    def setRemainingTime(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(HudModel, self)._initialize()
        self._addBoolProperty(b'barsVisible', False)
        self._addBoolProperty(b'isFinalPhase', False)
        self._addRealProperty(b'remainingTime', 0.0)
        return
