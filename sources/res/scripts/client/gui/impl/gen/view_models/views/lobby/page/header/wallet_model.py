from frameworks.wulf import Map, ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.currency_model import CurrencyModel

class WalletModel(ViewModel):
    __slots__ = (b'onCurrencyAction',)

    def __init__(self, properties=1, commands=1):
        super(WalletModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencies(self):
        return self._getMap(0)

    def setCurrencies(self, value):
        self._setMap(0, value)
        return

    @staticmethod
    def getCurrenciesType():
        return (unicode, CurrencyModel)

    def _initialize(self):
        super(WalletModel, self)._initialize()
        self._addMapProperty(b'currencies', Map(unicode, CurrencyModel))
        self.onCurrencyAction = self._addCommand(b'onCurrencyAction')
        return
