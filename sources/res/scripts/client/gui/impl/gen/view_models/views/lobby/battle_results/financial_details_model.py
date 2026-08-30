from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.currency_group_model import CurrencyGroupModel

class FinancialDetailsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FinancialDetailsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def earned(self):
        return self._getViewModel(0)

    @staticmethod
    def getEarnedType():
        return CurrencyGroupModel

    @property
    def expenses(self):
        return self._getViewModel(1)

    @staticmethod
    def getExpensesType():
        return CurrencyGroupModel

    @property
    def total(self):
        return self._getViewModel(2)

    @staticmethod
    def getTotalType():
        return CurrencyGroupModel

    @property
    def additional(self):
        return self._getViewModel(3)

    @staticmethod
    def getAdditionalType():
        return CurrencyGroupModel

    def _initialize(self):
        super(FinancialDetailsModel, self)._initialize()
        self._addViewModelProperty(b'earned', CurrencyGroupModel())
        self._addViewModelProperty(b'expenses', CurrencyGroupModel())
        self._addViewModelProperty(b'total', CurrencyGroupModel())
        self._addViewModelProperty(b'additional', CurrencyGroupModel())
        return
