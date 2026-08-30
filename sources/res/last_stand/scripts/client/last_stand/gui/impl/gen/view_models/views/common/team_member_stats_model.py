from frameworks.wulf import ViewModel

class TeamMemberStatsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(TeamMemberStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getKills(self):
        return self._getNumber(0)

    def setKills(self, value):
        self._setNumber(0, value)
        return

    def getPlaceByKills(self):
        return self._getNumber(1)

    def setPlaceByKills(self, value):
        self._setNumber(1, value)
        return

    def getDamage(self):
        return self._getNumber(2)

    def setDamage(self, value):
        self._setNumber(2, value)
        return

    def getPlaceByDamage(self):
        return self._getNumber(3)

    def setPlaceByDamage(self, value):
        self._setNumber(3, value)
        return

    def getAssist(self):
        return self._getNumber(4)

    def setAssist(self, value):
        self._setNumber(4, value)
        return

    def getBlocked(self):
        return self._getNumber(5)

    def setBlocked(self, value):
        self._setNumber(5, value)
        return

    def getSouls(self):
        return self._getNumber(6)

    def setSouls(self, value):
        self._setNumber(6, value)
        return

    def getPlaceByMatter(self):
        return self._getNumber(7)

    def setPlaceByMatter(self, value):
        self._setNumber(7, value)
        return

    def getPlace(self):
        return self._getNumber(8)

    def setPlace(self, value):
        self._setNumber(8, value)
        return

    def getKeys(self):
        return self._getNumber(9)

    def setKeys(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(TeamMemberStatsModel, self)._initialize()
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'placeByKills', 0)
        self._addNumberProperty(b'damage', 0)
        self._addNumberProperty(b'placeByDamage', 0)
        self._addNumberProperty(b'assist', 0)
        self._addNumberProperty(b'blocked', 0)
        self._addNumberProperty(b'souls', 0)
        self._addNumberProperty(b'placeByMatter', 0)
        self._addNumberProperty(b'place', 1)
        self._addNumberProperty(b'keys', 0)
        return
