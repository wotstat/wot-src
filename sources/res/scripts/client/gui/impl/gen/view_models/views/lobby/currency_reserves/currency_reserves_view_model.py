from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserve_model import CurrencyReserveModel

class CurrencyReservesViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(CurrencyReservesViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def creditReserve(self):
        return self._getViewModel(0)

    @staticmethod
    def getCreditReserveType():
        return CurrencyReserveModel

    @property
    def goldReserve(self):
        return self._getViewModel(1)

    @staticmethod
    def getGoldReserveType():
        return CurrencyReserveModel

    def getTimeToOpen(self):
        return self._getNumber(2)

    def setTimeToOpen(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(CurrencyReservesViewModel, self)._initialize()
        self._addViewModelProperty(b'creditReserve', CurrencyReserveModel())
        self._addViewModelProperty(b'goldReserve', CurrencyReserveModel())
        self._addNumberProperty(b'timeToOpen', 0)
        self.onClose = self._addCommand(b'onClose')
        return
