from frameworks.wulf import ViewModel

class RankedSeasonEfficiencyModel(ViewModel):
    __slots__ = ()
    PERIOD_PAST = 0
    PERIOD_CURRENT = 1
    PERIOD_FUTURE = 2
    EFFICIENCY_DEFAULT = 0
    EFFICIENCY_BEST = 1
    EFFICIENCY_OUT_OF_LEAGUE = 2
    WAITING_AWARDS = 3

    def __init__(self, properties=3, commands=0):
        super(RankedSeasonEfficiencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getReal(0)

    def setValue(self, value):
        self._setReal(0, value)
        return

    def getPeriodState(self):
        return self._getNumber(1)

    def setPeriodState(self, value):
        self._setNumber(1, value)
        return

    def getEfficiencyState(self):
        return self._getNumber(2)

    def setEfficiencyState(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RankedSeasonEfficiencyModel, self)._initialize()
        self._addRealProperty(b'value', 0.0)
        self._addNumberProperty(b'periodState', 0)
        self._addNumberProperty(b'efficiencyState', 0)
        return
