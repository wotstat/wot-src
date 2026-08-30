from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel
from gui.impl.gen.view_models.views.lobby.offers.gift_model import GiftModel

class OfferModel(ViewModel):
    __slots__ = (b'onBack', b'onLearnMore')

    def __init__(self, properties=13, commands=2):
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

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getLearnMore(self):
        return self._getString(4)

    def setLearnMore(self, value):
        self._setString(4, value)
        return

    def getTokens(self):
        return self._getNumber(5)

    def setTokens(self, value):
        self._setNumber(5, value)
        return

    def getTokensIcon(self):
        return self._getString(6)

    def setTokensIcon(self, value):
        self._setString(6, value)
        return

    def getClicksCount(self):
        return self._getNumber(7)

    def setClicksCount(self, value):
        self._setNumber(7, value)
        return

    def getSignImageLarge(self):
        return self._getString(8)

    def setSignImageLarge(self, value):
        self._setString(8, value)
        return

    def getSignImageSmall(self):
        return self._getString(9)

    def setSignImageSmall(self, value):
        self._setString(9, value)
        return

    def getExpiration(self):
        return self._getNumber(10)

    def setExpiration(self, value):
        self._setNumber(10, value)
        return

    def getBackground(self):
        return self._getString(11)

    def setBackground(self, value):
        self._setString(11, value)
        return

    def getShowPrice(self):
        return self._getBool(12)

    def setShowPrice(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(OfferModel, self)._initialize()
        self._addViewModelProperty(b'gifts', ListModel())
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'learnMore', b'')
        self._addNumberProperty(b'tokens', 0)
        self._addStringProperty(b'tokensIcon', b'')
        self._addNumberProperty(b'clicksCount', 0)
        self._addStringProperty(b'signImageLarge', b'')
        self._addStringProperty(b'signImageSmall', b'')
        self._addNumberProperty(b'expiration', 0)
        self._addStringProperty(b'background', b'')
        self._addBoolProperty(b'showPrice', False)
        self.onBack = self._addCommand(b'onBack')
        self.onLearnMore = self._addCommand(b'onLearnMore')
        return
