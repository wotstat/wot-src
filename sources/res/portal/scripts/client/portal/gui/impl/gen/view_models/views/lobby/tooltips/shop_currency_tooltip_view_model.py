from frameworks.wulf import ViewModel

class ShopCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ShopCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsPortalCoinTooltip(self):
        return self._getBool(0)

    def setIsPortalCoinTooltip(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(ShopCurrencyTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isPortalCoinTooltip', False)
        return
