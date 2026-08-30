from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class PriceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PriceModel, self).__init__(properties=properties, commands=commands)
        return

    def getPriceID(self):
        return self._getString(0)

    def setPriceID(self, value):
        self._setString(0, value)
        return

    def getPrice(self):
        return self._getArray(1)

    def setPrice(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getDefPrice(self):
        return self._getArray(2)

    def setDefPrice(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getDefPriceType():
        return PriceItemModel

    def getDiscount(self):
        return self._getArray(3)

    def setDiscount(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getDiscountType():
        return PriceItemModel

    def _initialize(self):
        super(PriceModel, self)._initialize()
        self._addStringProperty(b'priceID', b'')
        self._addArrayProperty(b'price', Array())
        self._addArrayProperty(b'defPrice', Array())
        self._addArrayProperty(b'discount', Array())
        return
