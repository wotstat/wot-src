from enum import IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_discount_model import RankDiscountModel

class ShopState(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    ERROR = 2


class ShopModel(ViewModel):
    __slots__ = (b'onProductSeen', b'onProductSelect', b'onProductPurchase', b'onProductRestore', b'onGoToHangar', b'onGoToPreview', b'onGoToCustomization', b'onAddToVehicleCompare', b'onMouseOver3dScene', b'onMoveSpace')

    def __init__(self, properties=8, commands=10):
        super(ShopModel, self).__init__(properties=properties, commands=commands)
        return

    def getShopState(self):
        return ShopState(self._getNumber(0))

    def setShopState(self, value):
        self._setNumber(0, value.value)
        return

    def getIsVehiclesCompareEnabled(self):
        return self._getBool(1)

    def setIsVehiclesCompareEnabled(self, value):
        self._setBool(1, value)
        return

    def getVehicleCompareTooltipId(self):
        return self._getString(2)

    def setVehicleCompareTooltipId(self, value):
        self._setString(2, value)
        return

    def getSelectedProductId(self):
        return self._getNumber(3)

    def setSelectedProductId(self, value):
        self._setNumber(3, value)
        return

    def getCurrentRank(self):
        return Rank(self._getNumber(4))

    def setCurrentRank(self, value):
        self._setNumber(4, value.value)
        return

    def getMaxAchievedRank(self):
        return Rank(self._getNumber(5))

    def setMaxAchievedRank(self, value):
        self._setNumber(5, value.value)
        return

    def getRankDiscounts(self):
        return self._getArray(6)

    def setRankDiscounts(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRankDiscountsType():
        return RankDiscountModel

    def getProducts(self):
        return self._getArray(7)

    def setProducts(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getProductsType():
        return BaseProductModel

    def _initialize(self):
        super(ShopModel, self)._initialize()
        self._addNumberProperty(b'shopState')
        self._addBoolProperty(b'isVehiclesCompareEnabled', True)
        self._addStringProperty(b'vehicleCompareTooltipId', b'')
        self._addNumberProperty(b'selectedProductId', 0)
        self._addNumberProperty(b'currentRank')
        self._addNumberProperty(b'maxAchievedRank')
        self._addArrayProperty(b'rankDiscounts', Array())
        self._addArrayProperty(b'products', Array())
        self.onProductSeen = self._addCommand(b'onProductSeen')
        self.onProductSelect = self._addCommand(b'onProductSelect')
        self.onProductPurchase = self._addCommand(b'onProductPurchase')
        self.onProductRestore = self._addCommand(b'onProductRestore')
        self.onGoToHangar = self._addCommand(b'onGoToHangar')
        self.onGoToPreview = self._addCommand(b'onGoToPreview')
        self.onGoToCustomization = self._addCommand(b'onGoToCustomization')
        self.onAddToVehicleCompare = self._addCommand(b'onAddToVehicleCompare')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        return
