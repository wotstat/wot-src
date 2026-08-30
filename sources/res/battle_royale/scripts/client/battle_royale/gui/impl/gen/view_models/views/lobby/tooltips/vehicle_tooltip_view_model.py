from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.rent_price_model import RentPriceModel

class VehicleTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(VehicleTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rentPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getRentPriceType():
        return RentPriceModel

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)
        return

    def getVehicleNation(self):
        return self._getString(2)

    def setVehicleNation(self, value):
        self._setString(2, value)
        return

    def getRentState(self):
        return self._getString(3)

    def setRentState(self, value):
        self._setString(3, value)
        return

    def getStatusLevel(self):
        return self._getString(4)

    def setStatusLevel(self, value):
        self._setString(4, value)
        return

    def getStatusText(self):
        return self._getString(5)

    def setStatusText(self, value):
        self._setString(5, value)
        return

    def getRentTimeLeft(self):
        return self._getString(6)

    def setRentTimeLeft(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(VehicleTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'rentPrice', RentPriceModel())
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleNation', b'')
        self._addStringProperty(b'rentState', b'')
        self._addStringProperty(b'statusLevel', b'')
        self._addStringProperty(b'statusText', b'')
        self._addStringProperty(b'rentTimeLeft', b'')
        return
