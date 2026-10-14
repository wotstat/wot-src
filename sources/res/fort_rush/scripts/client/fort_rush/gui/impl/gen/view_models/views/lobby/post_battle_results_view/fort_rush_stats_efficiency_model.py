from frameworks.wulf import ViewModel

class FortRushStatsEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FortRushStatsEfficiencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getFortRushScore(self):
        return self._getNumber(0)

    def setFortRushScore(self, value):
        self._setNumber(0, value)
        return

    def getDamageDealt(self):
        return self._getNumber(1)

    def setDamageDealt(self, value):
        self._setNumber(1, value)
        return

    def getKills(self):
        return self._getNumber(2)

    def setKills(self, value):
        self._setNumber(2, value)
        return

    def getRespawns(self):
        return self._getNumber(3)

    def setRespawns(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(FortRushStatsEfficiencyModel, self)._initialize()
        self._addNumberProperty(b'fortRushScore', 0)
        self._addNumberProperty(b'damageDealt', 0)
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'respawns', 0)
        return
