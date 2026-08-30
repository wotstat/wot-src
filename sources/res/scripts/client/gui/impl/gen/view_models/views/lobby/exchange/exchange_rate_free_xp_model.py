from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_base_model import ExchangeRateBaseModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_vehicles_selection_model import ExchangeRateVehiclesSelectionModel

class ExchangeRateFreeXpModel(ExchangeRateBaseModel):
    __slots__ = (b'onVehiclesSelected',)

    def __init__(self, properties=10, commands=5):
        super(ExchangeRateFreeXpModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehiclesSelection(self):
        return self._getArray(9)

    def setVehiclesSelection(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getVehiclesSelectionType():
        return ExchangeRateVehiclesSelectionModel

    def _initialize(self):
        super(ExchangeRateFreeXpModel, self)._initialize()
        self._addArrayProperty(b'vehiclesSelection', Array())
        self.onVehiclesSelected = self._addCommand(b'onVehiclesSelected')
        return
