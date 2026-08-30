from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class ShopOnOpenState(Enum):
    AVAILABLE = b'available'
    NOT_AVAILABLE = b'notAvailable'
    DISABLED = b'disabled'


class SeniorityRewardAwardViewModel(ViewModel):
    __slots__ = (b'onOpenBtnClick', b'onShopBtnClick')

    def __init__(self, properties=5, commands=2):
        super(SeniorityRewardAwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def getMaxCategory(self):
        return self._getString(1)

    def setMaxCategory(self, value):
        self._setString(1, value)
        return

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getSpecialCurrencyCount(self):
        return self._getNumber(3)

    def setSpecialCurrencyCount(self, value):
        self._setNumber(3, value)
        return

    def getShopOnOpenState(self):
        return ShopOnOpenState(self._getString(4))

    def setShopOnOpenState(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(SeniorityRewardAwardViewModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        self._addStringProperty(b'maxCategory', b'')
        self._addArrayProperty(b'bonuses', Array())
        self._addNumberProperty(b'specialCurrencyCount', -1)
        self._addStringProperty(b'shopOnOpenState', ShopOnOpenState.NOT_AVAILABLE.value)
        self.onOpenBtnClick = self._addCommand(b'onOpenBtnClick')
        self.onShopBtnClick = self._addCommand(b'onShopBtnClick')
        return
