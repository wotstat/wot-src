from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyTypeModel

class NyCurrencyTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NyCurrencyTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currency(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrencyType():
        return NyCurrencyTypeModel

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)
        return

    def getAllowClick(self):
        return self._getBool(2)

    def setAllowClick(self, value):
        self._setBool(2, value)
        return

    def getIsCurrencyAvailable(self):
        return self._getBool(3)

    def setIsCurrencyAvailable(self, value):
        self._setBool(3, value)
        return

    def getIsProgressionCompleted(self):
        return self._getBool(4)

    def setIsProgressionCompleted(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(NyCurrencyTooltipModel, self)._initialize()
        self._addViewModelProperty(b'currency', NyCurrencyTypeModel())
        self._addNumberProperty(b'amount', 0)
        self._addBoolProperty(b'allowClick', False)
        self._addBoolProperty(b'isCurrencyAvailable', True)
        self._addBoolProperty(b'isProgressionCompleted', True)
        return
