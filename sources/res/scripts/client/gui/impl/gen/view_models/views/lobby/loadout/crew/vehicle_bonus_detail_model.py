from frameworks.wulf import ViewModel

class VehicleBonusDetailModel(ViewModel):
    __slots__ = ()
    COMMANDER = b'commander'
    BROTHERHOOD = b'brotherhood'

    def __init__(self, properties=3, commands=0):
        super(VehicleBonusDetailModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getBonus(self):
        return self._getReal(2)

    def setBonus(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(VehicleBonusDetailModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'type', b'')
        self._addRealProperty(b'bonus', 0.0)
        return
