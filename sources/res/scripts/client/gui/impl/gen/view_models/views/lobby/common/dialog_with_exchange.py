from gui.impl.gen.view_models.common.exchange_panel_model import ExchangePanelModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class DialogWithExchange(FullScreenDialogWindowModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=3):
        super(DialogWithExchange, self).__init__(properties=properties, commands=commands)
        return

    @property
    def exchangePanel(self):
        return self._getViewModel(11)

    @staticmethod
    def getExchangePanelType():
        return ExchangePanelModel

    @property
    def lacksMoney(self):
        return self._getViewModel(12)

    @staticmethod
    def getLacksMoneyType():
        return PriceItemModel

    def getBottomContentType(self):
        return self._getString(13)

    def setBottomContentType(self, value):
        self._setString(13, value)
        return

    def getExchangeState(self):
        return self._getString(14)

    def setExchangeState(self, value):
        self._setString(14, value)
        return

    def _initialize(self):
        super(DialogWithExchange, self)._initialize()
        self._addViewModelProperty(b'exchangePanel', ExchangePanelModel())
        self._addViewModelProperty(b'lacksMoney', PriceItemModel())
        self._addStringProperty(b'bottomContentType', b'')
        self._addStringProperty(b'exchangeState', b'default')
        return
