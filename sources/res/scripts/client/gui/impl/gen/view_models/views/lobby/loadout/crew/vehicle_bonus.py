from frameworks.wulf import ViewModel

class VehicleBonus(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleBonus, self).__init__(properties=properties, commands=commands)
        return

    def getEquipment(self):
        return self._getReal(0)

    def setEquipment(self, value):
        self._setReal(0, value)
        return

    def getBrotherhood(self):
        return self._getReal(1)

    def setBrotherhood(self, value):
        self._setReal(1, value)
        return

    def getOptDevices(self):
        return self._getReal(2)

    def setOptDevices(self, value):
        self._setReal(2, value)
        return

    def getCommander(self):
        return self._getReal(3)

    def setCommander(self, value):
        self._setReal(3, value)
        return

    def getBattleBooster(self):
        return self._getReal(4)

    def setBattleBooster(self, value):
        self._setReal(4, value)
        return

    def _initialize(self):
        super(VehicleBonus, self)._initialize()
        self._addRealProperty(b'equipment', 0.0)
        self._addRealProperty(b'brotherhood', 0.0)
        self._addRealProperty(b'optDevices', 0.0)
        self._addRealProperty(b'commander', 0.0)
        self._addRealProperty(b'battleBooster', 0.0)
        return
