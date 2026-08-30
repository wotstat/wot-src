from frameworks.wulf import ViewModel

class StatsEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(StatsEfficiencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getDamageDealt(self):
        return self._getNumber(0)

    def setDamageDealt(self, value):
        self._setNumber(0, value)
        return

    def getKills(self):
        return self._getNumber(1)

    def setKills(self, value):
        self._setNumber(1, value)
        return

    def getEarnedXp(self):
        return self._getNumber(2)

    def setEarnedXp(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(StatsEfficiencyModel, self)._initialize()
        self._addNumberProperty(b'damageDealt', 0)
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'earnedXp', 0)
        return
