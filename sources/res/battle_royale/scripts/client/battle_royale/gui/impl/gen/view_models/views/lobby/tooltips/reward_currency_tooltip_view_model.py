from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.daily_bonus_model import DailyBonusModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel

class RewardCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RewardCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eventInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getEventInfoType():
        return BattleRoyaleEventModel

    @property
    def dailyBonus(self):
        return self._getViewModel(1)

    @staticmethod
    def getDailyBonusType():
        return DailyBonusModel

    def getCurrencyType(self):
        return self._getString(2)

    def setCurrencyType(self, value):
        self._setString(2, value)
        return

    def getHasPremiumBonus(self):
        return self._getBool(3)

    def setHasPremiumBonus(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(RewardCurrencyTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'eventInfo', BattleRoyaleEventModel())
        self._addViewModelProperty(b'dailyBonus', DailyBonusModel())
        self._addStringProperty(b'currencyType', b'')
        self._addBoolProperty(b'hasPremiumBonus', False)
        return
