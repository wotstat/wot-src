from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class BundleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BundleModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getIsShopBundle(self):
        return self._getBool(2)

    def setIsShopBundle(self, value):
        self._setBool(2, value)
        return

    def getKeysInBundle(self):
        return self._getNumber(3)

    def setKeysInBundle(self, value):
        self._setNumber(3, value)
        return

    def getDescrGroupKey(self):
        return self._getString(4)

    def setDescrGroupKey(self, value):
        self._setString(4, value)
        return

    def getMaximumBundleCount(self):
        return self._getNumber(5)

    def setMaximumBundleCount(self, value):
        self._setNumber(5, value)
        return

    def getBonuses(self):
        return self._getArray(6)

    def setBonuses(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusItemViewModel

    def _initialize(self):
        super(BundleModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceItemModel())
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isShopBundle', False)
        self._addNumberProperty(b'keysInBundle', 0)
        self._addStringProperty(b'descrGroupKey', b'')
        self._addNumberProperty(b'maximumBundleCount', 0)
        self._addArrayProperty(b'bonuses', Array())
        return
