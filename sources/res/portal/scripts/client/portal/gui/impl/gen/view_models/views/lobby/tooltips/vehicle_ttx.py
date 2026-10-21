from frameworks.wulf import ViewModel

class VehicleTtx(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleTtx, self).__init__(properties=properties, commands=commands)
        return

    def getDamage(self):
        return self._getNumber(0)

    def setDamage(self, value):
        self._setNumber(0, value)
        return

    def getMobility(self):
        return self._getNumber(1)

    def setMobility(self, value):
        self._setNumber(1, value)
        return

    def getArmor(self):
        return self._getNumber(2)

    def setArmor(self, value):
        self._setNumber(2, value)
        return

    def getReload(self):
        return self._getNumber(3)

    def setReload(self, value):
        self._setNumber(3, value)
        return

    def getHp(self):
        return self._getNumber(4)

    def setHp(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(VehicleTtx, self)._initialize()
        self._addNumberProperty(b'damage', 0)
        self._addNumberProperty(b'mobility', 0)
        self._addNumberProperty(b'armor', 0)
        self._addNumberProperty(b'reload', 0)
        self._addNumberProperty(b'hp', 0)
        return
