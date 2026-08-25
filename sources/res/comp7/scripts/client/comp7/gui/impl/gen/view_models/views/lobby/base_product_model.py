from enum import Enum, IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.product_price_model import ProductPriceModel

class ProductTypes(IntEnum):
    BASE = 0
    VEHICLE = 1
    STYLE3D = 2
    REWARD = 3


class ProductState(Enum):
    LOCKED = b'locked'
    READYTORESTORE = b'readyToRestore'
    READYTOPURCHASE = b'readyToPurchase'
    PURCHASED = b'purchased'
    INPROGRESS = b'inProgress'


class BaseProductModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(BaseProductModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return ProductPriceModel

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getType(self):
        return ProductTypes(self._getNumber(2))

    def setType(self, value):
        self._setNumber(2, value.value)
        return

    def getRank(self):
        return Rank(self._getNumber(3))

    def setRank(self, value):
        self._setNumber(3, value.value)
        return

    def getLimitedQuantity(self):
        return self._getNumber(4)

    def setLimitedQuantity(self, value):
        self._setNumber(4, value)
        return

    def getState(self):
        return ProductState(self._getString(5))

    def setState(self, value):
        self._setString(5, value.value)
        return

    def getIsNew(self):
        return self._getBool(6)

    def setIsNew(self, value):
        self._setBool(6, value)
        return

    def getDescription(self):
        return self._getString(7)

    def setDescription(self, value):
        self._setString(7, value)
        return

    def getTooltipId(self):
        return self._getString(8)

    def setTooltipId(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(BaseProductModel, self)._initialize()
        self._addViewModelProperty(b'price', ProductPriceModel())
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'type')
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'limitedQuantity', 0)
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isNew', False)
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'tooltipId', b'')
        return
