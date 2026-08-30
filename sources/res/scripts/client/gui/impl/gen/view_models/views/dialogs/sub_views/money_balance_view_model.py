from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel

class MoneyBalanceViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(MoneyBalanceViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def goldTooltip(self):
        return self._getViewModel(0)

    @staticmethod
    def getGoldTooltipType():
        return DialogTemplateGenericTooltipViewModel

    @property
    def creditsTooltip(self):
        return self._getViewModel(1)

    @staticmethod
    def getCreditsTooltipType():
        return DialogTemplateGenericTooltipViewModel

    @property
    def crystalsTooltip(self):
        return self._getViewModel(2)

    @staticmethod
    def getCrystalsTooltipType():
        return DialogTemplateGenericTooltipViewModel

    @property
    def freeExpTooltip(self):
        return self._getViewModel(3)

    @staticmethod
    def getFreeExpTooltipType():
        return DialogTemplateGenericTooltipViewModel

    @property
    def equipCoinTooltip(self):
        return self._getViewModel(4)

    @staticmethod
    def getEquipCoinTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getGold(self):
        return self._getNumber(5)

    def setGold(self, value):
        self._setNumber(5, value)
        return

    def getCredits(self):
        return self._getNumber(6)

    def setCredits(self, value):
        self._setNumber(6, value)
        return

    def getCrystals(self):
        return self._getNumber(7)

    def setCrystals(self, value):
        self._setNumber(7, value)
        return

    def getFreeExp(self):
        return self._getNumber(8)

    def setFreeExp(self, value):
        self._setNumber(8, value)
        return

    def getEquipCoin(self):
        return self._getNumber(9)

    def setEquipCoin(self, value):
        self._setNumber(9, value)
        return

    def getIsWGMAvailable(self):
        return self._getBool(10)

    def setIsWGMAvailable(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(MoneyBalanceViewModel, self)._initialize()
        self._addViewModelProperty(b'goldTooltip', DialogTemplateGenericTooltipViewModel())
        self._addViewModelProperty(b'creditsTooltip', DialogTemplateGenericTooltipViewModel())
        self._addViewModelProperty(b'crystalsTooltip', DialogTemplateGenericTooltipViewModel())
        self._addViewModelProperty(b'freeExpTooltip', DialogTemplateGenericTooltipViewModel())
        self._addViewModelProperty(b'equipCoinTooltip', DialogTemplateGenericTooltipViewModel())
        self._addNumberProperty(b'gold', -1)
        self._addNumberProperty(b'credits', -1)
        self._addNumberProperty(b'crystals', -1)
        self._addNumberProperty(b'freeExp', -1)
        self._addNumberProperty(b'equipCoin', -1)
        self._addBoolProperty(b'isWGMAvailable', False)
        return
