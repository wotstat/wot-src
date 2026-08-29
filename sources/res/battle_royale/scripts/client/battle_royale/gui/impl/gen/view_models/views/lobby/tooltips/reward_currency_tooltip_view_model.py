from frameworks.wulf import ViewModel

class RewardCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RewardCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyType(self):
        return self._getString(0)

    def setCurrencyType(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(RewardCurrencyTooltipViewModel, self)._initialize()
        self._addStringProperty(b'currencyType', b'')
        return
