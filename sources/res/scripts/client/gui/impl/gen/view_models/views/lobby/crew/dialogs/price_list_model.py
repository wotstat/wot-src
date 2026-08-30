from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel

class PriceListModel(ViewModel):
    __slots__ = (b'onCardClick', b'onPriceSelect')

    def __init__(self, properties=1, commands=2):
        super(PriceListModel, self).__init__(properties=properties, commands=commands)
        return

    def getCardsList(self):
        return self._getArray(0)

    def setCardsList(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCardsListType():
        return PriceCardModel

    def _initialize(self):
        super(PriceListModel, self)._initialize()
        self._addArrayProperty(b'cardsList', Array())
        self.onCardClick = self._addCommand(b'onCardClick')
        self.onPriceSelect = self._addCommand(b'onPriceSelect')
        return
