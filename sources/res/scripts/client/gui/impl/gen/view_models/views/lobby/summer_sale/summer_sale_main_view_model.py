from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.summer_sale.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.summer_sale.product_model import ProductModel
from gui.impl.gen.view_models.views.lobby.summer_sale.rewards_category_model import RewardsCategoryModel
from gui.impl.gen.view_models.views.lobby.summer_sale.stepper_view_model import StepperViewModel
from gui.impl.gen.view_models.views.lobby.summer_sale.time_range_model import TimeRangeModel

class SummerSaleMainViewModel(ViewModel):
    __slots__ = (b'onStepperCountChange', b'onBuyCoinsClick', b'onBuyProductClick', b'onInfoClick', b'onPreviewVehicle', b'onOpenShop', b'onOpenQuests', b'onClose')

    def __init__(self, properties=10, commands=8):
        super(SummerSaleMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eventTimeRange(self):
        return self._getViewModel(0)

    @staticmethod
    def getEventTimeRangeType():
        return TimeRangeModel

    @property
    def stepper(self):
        return self._getViewModel(1)

    @staticmethod
    def getStepperType():
        return StepperViewModel

    @property
    def summerSaleSetsTotalPrice(self):
        return self._getViewModel(2)

    @staticmethod
    def getSummerSaleSetsTotalPriceType():
        return PriceModel

    def getSummerSaleSetProductCode(self):
        return self._getString(3)

    def setSummerSaleSetProductCode(self, value):
        self._setString(3, value)
        return

    def getBumblebeeCoinsBalance(self):
        return self._getNumber(4)

    def setBumblebeeCoinsBalance(self, value):
        self._setNumber(4, value)
        return

    def getHoneyCoinsBalance(self):
        return self._getNumber(5)

    def setHoneyCoinsBalance(self, value):
        self._setNumber(5, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(6)

    def setProgressionLevel(self, value):
        self._setNumber(6, value)
        return

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardsCategoryModel

    def getProducts(self):
        return self._getArray(8)

    def setProducts(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getProductsType():
        return ProductModel

    def getIsAnyRandomVehicleObtained(self):
        return self._getBool(9)

    def setIsAnyRandomVehicleObtained(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(SummerSaleMainViewModel, self)._initialize()
        self._addViewModelProperty(b'eventTimeRange', TimeRangeModel())
        self._addViewModelProperty(b'stepper', StepperViewModel())
        self._addViewModelProperty(b'summerSaleSetsTotalPrice', PriceModel())
        self._addStringProperty(b'summerSaleSetProductCode', b'')
        self._addNumberProperty(b'bumblebeeCoinsBalance', 0)
        self._addNumberProperty(b'honeyCoinsBalance', 0)
        self._addNumberProperty(b'progressionLevel', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'products', Array())
        self._addBoolProperty(b'isAnyRandomVehicleObtained', False)
        self.onStepperCountChange = self._addCommand(b'onStepperCountChange')
        self.onBuyCoinsClick = self._addCommand(b'onBuyCoinsClick')
        self.onBuyProductClick = self._addCommand(b'onBuyProductClick')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        self.onPreviewVehicle = self._addCommand(b'onPreviewVehicle')
        self.onOpenShop = self._addCommand(b'onOpenShop')
        self.onOpenQuests = self._addCommand(b'onOpenQuests')
        self.onClose = self._addCommand(b'onClose')
        return
