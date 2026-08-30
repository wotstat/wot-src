from frameworks.wulf import ViewModel

class BattleRoyaleRespawnAbilityModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleRoyaleRespawnAbilityModel, self).__init__(properties=properties, commands=commands)
        return

    def getSoloRespawnPeriod(self):
        return self._getNumber(0)

    def setSoloRespawnPeriod(self, value):
        self._setNumber(0, value)
        return

    def getPlatoonRespawnPeriod(self):
        return self._getNumber(1)

    def setPlatoonRespawnPeriod(self, value):
        self._setNumber(1, value)
        return

    def getPlatoonTimeToResurrect(self):
        return self._getNumber(2)

    def setPlatoonTimeToResurrect(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BattleRoyaleRespawnAbilityModel, self)._initialize()
        self._addNumberProperty(b'soloRespawnPeriod', 0)
        self._addNumberProperty(b'platoonRespawnPeriod', 0)
        self._addNumberProperty(b'platoonTimeToResurrect', 0)
        return
