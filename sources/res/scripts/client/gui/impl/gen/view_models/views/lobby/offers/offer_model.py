from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel
from gui.impl.gen.view_models.views.lobby.offers.gift_model import GiftModel

class OfferModel(ViewModel):
    __slots__ = (b'onBack',)

    def __init__(self, properties=8, commands=1):
        super(OfferModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def gifts(self):
        return self._getViewModel(0)

    @staticmethod
    def getGiftsType():
        return GiftModel

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getTokens(self):
        return self._getNumber(3)

    def setTokens(self, value):
        self._setNumber(3, value)
        return

    def getClicksCount(self):
        return self._getNumber(4)

    def setClicksCount(self, value):
        self._setNumber(4, value)
        return

    def getExpiration(self):
        return self._getNumber(5)

    def setExpiration(self, value):
        self._setNumber(5, value)
        return

    def getBackground(self):
        return self._getString(6)

    def setBackground(self, value):
        self._setString(6, value)
        return

    def getKey(self):
        return self._getNumber(7)

    def setKey(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(OfferModel, self)._initialize()
        self._addViewModelProperty(b'gifts', ListModel())
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'tokens', 0)
        self._addNumberProperty(b'clicksCount', 0)
        self._addNumberProperty(b'expiration', 0)
        self._addStringProperty(b'background', b'')
        self._addNumberProperty(b'key', 0)
        self.onBack = self._addCommand(b'onBack')
        return
