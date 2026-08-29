from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class BundleType(Enum):
    SMALL = b'small'
    MEDIUM = b'medium'
    LARGE = b'large'


class ArmoryYardBundleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ArmoryYardBundleModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getIndex(self):
        return self._getString(1)

    def setIndex(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return BundleType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getLevelCount(self):
        return self._getNumber(3)

    def setLevelCount(self, value):
        self._setNumber(3, value)
        return

    def getDiscountPercent(self):
        return self._getNumber(4)

    def setDiscountPercent(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ArmoryYardBundleModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addStringProperty(b'index', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'levelCount', 0)
        self._addNumberProperty(b'discountPercent', 0)
        return
