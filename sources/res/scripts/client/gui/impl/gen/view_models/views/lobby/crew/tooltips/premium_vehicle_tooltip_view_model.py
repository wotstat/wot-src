from frameworks.wulf import ViewModel

class PremiumVehicleTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PremiumVehicleTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehTypeName(self):
        return self._getString(0)

    def setVehTypeName(self, value):
        self._setString(0, value)
        return

    def getNationName(self):
        return self._getString(1)

    def setNationName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(PremiumVehicleTooltipViewModel, self)._initialize()
        self._addStringProperty(b'vehTypeName', b'')
        self._addStringProperty(b'nationName', b'')
        return
