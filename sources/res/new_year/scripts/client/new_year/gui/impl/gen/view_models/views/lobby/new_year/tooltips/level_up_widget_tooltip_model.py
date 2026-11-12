from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyTypeModel

class LevelUpWidgetTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(LevelUpWidgetTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currency(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrencyType():
        return NyCurrencyTypeModel

    def getCustomizationZone(self):
        return self._getString(1)

    def setCustomizationZone(self, value):
        self._setString(1, value)
        return

    def getPointsCount(self):
        return self._getNumber(2)

    def setPointsCount(self, value):
        self._setNumber(2, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(3)

    def setCurrentLevel(self, value):
        self._setNumber(3, value)
        return

    def getToysCount(self):
        return self._getNumber(4)

    def setToysCount(self, value):
        self._setNumber(4, value)
        return

    def getCurrencyCount(self):
        return self._getNumber(5)

    def setCurrencyCount(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(LevelUpWidgetTooltipModel, self)._initialize()
        self._addViewModelProperty(b'currency', NyCurrencyTypeModel())
        self._addStringProperty(b'customizationZone', b'')
        self._addNumberProperty(b'pointsCount', 0)
        self._addNumberProperty(b'currentLevel', 1)
        self._addNumberProperty(b'toysCount', 0)
        self._addNumberProperty(b'currencyCount', 0)
        return
