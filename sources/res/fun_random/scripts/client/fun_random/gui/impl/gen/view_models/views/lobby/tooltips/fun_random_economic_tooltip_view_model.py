from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.financial_details_model import FinancialDetailsModel

class CurrencyType(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTALS = b'crystal'
    XP = b'xp'
    FREE_XP = b'freeXP'
    TANKMEN_XP = b'tankmenXP'


class FunRandomEconomicTooltipViewModel(FinancialDetailsModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomEconomicTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyType(self):
        return CurrencyType(self._getString(4))

    def setCurrencyType(self, value):
        self._setString(4, value.value)
        return

    def getPremiumAdvertising(self):
        return self._getString(5)

    def setPremiumAdvertising(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(FunRandomEconomicTooltipViewModel, self)._initialize()
        self._addStringProperty(b'currencyType')
        self._addStringProperty(b'premiumAdvertising', b'')
        return
