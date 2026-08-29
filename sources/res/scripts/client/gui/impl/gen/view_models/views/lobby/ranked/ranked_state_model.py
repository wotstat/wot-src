from frameworks.wulf import ViewModel

class RankedStateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RankedStateModel, self).__init__(properties=properties, commands=commands)
        return

    def getDivision(self):
        return self._getNumber(0)

    def setDivision(self, value):
        self._setNumber(0, value)
        return

    def getRank(self):
        return self._getNumber(1)

    def setRank(self, value):
        self._setNumber(1, value)
        return

    def getStep(self):
        return self._getNumber(2)

    def setStep(self, value):
        self._setNumber(2, value)
        return

    def getDivisionStart(self):
        return self._getNumber(3)

    def setDivisionStart(self, value):
        self._setNumber(3, value)
        return

    def getDivisionFinish(self):
        return self._getNumber(4)

    def setDivisionFinish(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(RankedStateModel, self)._initialize()
        self._addNumberProperty(b'division', 0)
        self._addNumberProperty(b'rank', 0)
        self._addNumberProperty(b'step', 0)
        self._addNumberProperty(b'divisionStart', 0)
        self._addNumberProperty(b'divisionFinish', 0)
        return
