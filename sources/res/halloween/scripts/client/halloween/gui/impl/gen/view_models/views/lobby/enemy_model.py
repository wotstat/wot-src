from frameworks.wulf import ViewModel

class EnemyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(EnemyModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getResourceKey(self):
        return self._getString(2)

    def setResourceKey(self, value):
        self._setString(2, value)
        return

    def getRole(self):
        return self._getString(3)

    def setRole(self, value):
        self._setString(3, value)
        return

    def getAbility(self):
        return self._getString(4)

    def setAbility(self, value):
        self._setString(4, value)
        return

    def getUnlockedByMission(self):
        return self._getNumber(5)

    def setUnlockedByMission(self, value):
        self._setNumber(5, value)
        return

    def getHasShopStyle(self):
        return self._getBool(6)

    def setHasShopStyle(self, value):
        self._setBool(6, value)
        return

    def getIsNew(self):
        return self._getBool(7)

    def setIsNew(self, value):
        self._setBool(7, value)
        return

    def getIsLocked(self):
        return self._getBool(8)

    def setIsLocked(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(EnemyModel, self)._initialize()
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'resourceKey', b'')
        self._addStringProperty(b'role', b'')
        self._addStringProperty(b'ability', b'')
        self._addNumberProperty(b'unlockedByMission', 0)
        self._addBoolProperty(b'hasShopStyle', False)
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'isLocked', False)
        return
