from frameworks.wulf import ViewModel

class BossStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BossStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getClan(self):
        return self._getString(1)

    def setClan(self, value):
        self._setString(1, value)
        return

    def getKills(self):
        return self._getNumber(2)

    def setKills(self, value):
        self._setNumber(2, value)
        return

    def getCurrentHP(self):
        return self._getNumber(3)

    def setCurrentHP(self, value):
        self._setNumber(3, value)
        return

    def getMaxHP(self):
        return self._getNumber(4)

    def setMaxHP(self, value):
        self._setNumber(4, value)
        return

    def getIsAnonymized(self):
        return self._getBool(5)

    def setIsAnonymized(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(BossStatusModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'clan', b'')
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'currentHP', 0)
        self._addNumberProperty(b'maxHP', 0)
        self._addBoolProperty(b'isAnonymized', False)
        return
