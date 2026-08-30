from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel
from gui.impl.gen.view_models.views.lobby.summer_sale.price_model import PriceModel

class SummerSaleTokensBonusModel(TokenBonusModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(SummerSaleTokensBonusModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(11)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getProductCode(self):
        return self._getString(12)

    def setProductCode(self, value):
        self._setString(12, value)
        return

    def getInInventory(self):
        return self._getBool(13)

    def setInInventory(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(SummerSaleTokensBonusModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addStringProperty(b'productCode', b'')
        self._addBoolProperty(b'inInventory', False)
        return
