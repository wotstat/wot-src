from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_bundle_model import ArmoryYardBundleModel

class ArmoryYardBundlesViewModel(ViewModel):
    __slots__ = (b'onBuyBundle', b'onBuyTokens', b'onClose')

    def __init__(self, properties=7, commands=3):
        super(ArmoryYardBundlesViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tokenPriceGold(self):
        return self._getViewModel(0)

    @staticmethod
    def getTokenPriceGoldType():
        return PriceModel

    @property
    def tokenPriceCrystal(self):
        return self._getViewModel(1)

    @staticmethod
    def getTokenPriceCrystalType():
        return PriceModel

    def getIsBlurEnabled(self):
        return self._getBool(2)

    def setIsBlurEnabled(self, value):
        self._setBool(2, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(3)

    def setCurrentLevel(self, value):
        self._setNumber(3, value)
        return

    def getBundles(self):
        return self._getArray(4)

    def setBundles(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getBundlesType():
        return ArmoryYardBundleModel

    def getCurrentTime(self):
        return self._getNumber(5)

    def setCurrentTime(self, value):
        self._setNumber(5, value)
        return

    def getEndTime(self):
        return self._getNumber(6)

    def setEndTime(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(ArmoryYardBundlesViewModel, self)._initialize()
        self._addViewModelProperty(b'tokenPriceGold', PriceModel())
        self._addViewModelProperty(b'tokenPriceCrystal', PriceModel())
        self._addBoolProperty(b'isBlurEnabled', False)
        self._addNumberProperty(b'currentLevel', 0)
        self._addArrayProperty(b'bundles', Array())
        self._addNumberProperty(b'currentTime', 0)
        self._addNumberProperty(b'endTime', 0)
        self.onBuyBundle = self._addCommand(b'onBuyBundle')
        self.onBuyTokens = self._addCommand(b'onBuyTokens')
        self.onClose = self._addCommand(b'onClose')
        return
