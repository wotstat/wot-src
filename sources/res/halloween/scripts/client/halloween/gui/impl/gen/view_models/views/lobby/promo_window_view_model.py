from frameworks.wulf import ViewModel

class PromoWindowViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=7, commands=1):
        super(PromoWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleUserName(self):
        return self._getString(0)

    def setVehicleUserName(self, value):
        self._setString(0, value)
        return

    def getVehicleLevel(self):
        return self._getString(1)

    def setVehicleLevel(self, value):
        self._setString(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getVehicleIsPremium(self):
        return self._getBool(3)

    def setVehicleIsPremium(self, value):
        self._setBool(3, value)
        return

    def getStartDate(self):
        return self._getNumber(4)

    def setStartDate(self, value):
        self._setNumber(4, value)
        return

    def getEndDate(self):
        return self._getNumber(5)

    def setEndDate(self, value):
        self._setNumber(5, value)
        return

    def getRegularArtefactsLength(self):
        return self._getNumber(6)

    def setRegularArtefactsLength(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(PromoWindowViewModel, self)._initialize()
        self._addStringProperty(b'vehicleUserName', b'')
        self._addStringProperty(b'vehicleLevel', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addBoolProperty(b'vehicleIsPremium', False)
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'regularArtefactsLength', 0)
        self.onClose = self._addCommand(b'onClose')
        return
