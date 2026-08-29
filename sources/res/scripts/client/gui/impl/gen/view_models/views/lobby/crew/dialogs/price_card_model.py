from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel

class CardType(Enum):
    DEFAULT = b'default'
    RESET = b'reset'
    RETRAIN = b'retrain'
    RECRUIT = b'recruit'


class CardState(Enum):
    DEFAULT = b''
    DISABLED = b'disabled'
    SELECTED = b'selected'


class PriceCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(PriceCardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return CurrencyViewModel

    @property
    def tooltip(self):
        return self._getViewModel(1)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getId(self):
        return self._getString(2)

    def setId(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getTitle(self):
        return self._getString(4)

    def setTitle(self, value):
        self._setString(4, value)
        return

    def getCardState(self):
        return CardState(self._getString(5))

    def setCardState(self, value):
        self._setString(5, value.value)
        return

    def getCardType(self):
        return CardType(self._getString(6))

    def setCardType(self, value):
        self._setString(6, value.value)
        return

    def getDescription(self):
        return self._getString(7)

    def setDescription(self, value):
        self._setString(7, value)
        return

    def getKwargs(self):
        return self._getString(8)

    def setKwargs(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(PriceCardModel, self)._initialize()
        self._addViewModelProperty(b'price', CurrencyViewModel())
        self._addViewModelProperty(b'tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'cardState')
        self._addStringProperty(b'cardType')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'kwargs', b'')
        return
