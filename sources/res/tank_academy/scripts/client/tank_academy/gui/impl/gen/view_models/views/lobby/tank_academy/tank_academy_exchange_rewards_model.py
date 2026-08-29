from frameworks.wulf import ViewModel

class TankAcademyExchangeRewardsModel(ViewModel):
    __slots__ = (b'onConfirm', b'onClose')

    def __init__(self, properties=3, commands=2):
        super(TankAcademyExchangeRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def getVehicleUserName(self):
        return self._getString(1)

    def setVehicleUserName(self, value):
        self._setString(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(TankAcademyExchangeRewardsModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleUserName', b'')
        self._addNumberProperty(b'level', 0)
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onClose = self._addCommand(b'onClose')
        return
