from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class BundleType(Enum):
    SMALL = b'small'
    MEDIUM = b'medium'
    LARGE = b'large'


class ArmoryYardBuyBundleViewModel(ViewModel):
    __slots__ = (b'onBuyBundle', b'onBack', b'onClose')
    MAX_VISIBLE_REWARDS = 10

    def __init__(self, properties=9, commands=3):
        super(ArmoryYardBuyBundleViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getBundleId(self):
        return self._getString(1)

    def setBundleId(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return BundleType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getStartLevel(self):
        return self._getNumber(3)

    def setStartLevel(self, value):
        self._setNumber(3, value)
        return

    def getEndLevel(self):
        return self._getNumber(4)

    def setEndLevel(self, value):
        self._setNumber(4, value)
        return

    def getLevelCount(self):
        return self._getNumber(5)

    def setLevelCount(self, value):
        self._setNumber(5, value)
        return

    def getRewards(self):
        return self._getArray(6)

    def setRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getIsWalletAvailable(self):
        return self._getBool(7)

    def setIsWalletAvailable(self, value):
        self._setBool(7, value)
        return

    def getIsBlurEnabled(self):
        return self._getBool(8)

    def setIsBlurEnabled(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(ArmoryYardBuyBundleViewModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addStringProperty(b'bundleId', b'')
        self._addStringProperty(b'type')
        self._addNumberProperty(b'startLevel', 0)
        self._addNumberProperty(b'endLevel', 0)
        self._addNumberProperty(b'levelCount', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addBoolProperty(b'isBlurEnabled', False)
        self.onBuyBundle = self._addCommand(b'onBuyBundle')
        self.onBack = self._addCommand(b'onBack')
        self.onClose = self._addCommand(b'onClose')
        return
