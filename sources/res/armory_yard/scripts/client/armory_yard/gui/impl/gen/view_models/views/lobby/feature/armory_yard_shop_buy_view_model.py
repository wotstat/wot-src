from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_shop_item import ArmoryYardShopItem

class ArmoryYardShopBuyViewModel(ViewModel):
    __slots__ = (b'onBuyProduct', b'onBack', b'onClose', b'onShowVehiclePreview', b'onShowStylePreview')
    MAX_VISIBLE_REWARDS = 4

    def __init__(self, properties=8, commands=5):
        super(ArmoryYardShopBuyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def item(self):
        return self._getViewModel(0)

    @staticmethod
    def getItemType():
        return ArmoryYardShopItem

    def getIsWalletAvailable(self):
        return self._getBool(1)

    def setIsWalletAvailable(self, value):
        self._setBool(1, value)
        return

    def getGoldConversion(self):
        return self._getNumber(2)

    def setGoldConversion(self, value):
        self._setNumber(2, value)
        return

    def getCrystalConversion(self):
        return self._getNumber(3)

    def setCrystalConversion(self, value):
        self._setNumber(3, value)
        return

    def getCurrencyAmount(self):
        return self._getNumber(4)

    def setCurrencyAmount(self, value):
        self._setNumber(4, value)
        return

    def getGoldAmount(self):
        return self._getNumber(5)

    def setGoldAmount(self, value):
        self._setNumber(5, value)
        return

    def getCrystalAmount(self):
        return self._getNumber(6)

    def setCrystalAmount(self, value):
        self._setNumber(6, value)
        return

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(ArmoryYardShopBuyViewModel, self)._initialize()
        self._addViewModelProperty(b'item', ArmoryYardShopItem())
        self._addBoolProperty(b'isWalletAvailable', False)
        self._addNumberProperty(b'goldConversion', 0)
        self._addNumberProperty(b'crystalConversion', 0)
        self._addNumberProperty(b'currencyAmount', 0)
        self._addNumberProperty(b'goldAmount', 0)
        self._addNumberProperty(b'crystalAmount', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onBuyProduct = self._addCommand(b'onBuyProduct')
        self.onBack = self._addCommand(b'onBack')
        self.onClose = self._addCommand(b'onClose')
        self.onShowVehiclePreview = self._addCommand(b'onShowVehiclePreview')
        self.onShowStylePreview = self._addCommand(b'onShowStylePreview')
        return
