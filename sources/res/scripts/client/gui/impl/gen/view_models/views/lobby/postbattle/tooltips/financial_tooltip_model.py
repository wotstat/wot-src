from gui.impl.gen.view_models.views.lobby.postbattle.details_group_model import DetailsGroupModel

class FinancialTooltipModel(DetailsGroupModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FinancialTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrencyType(self):
        return self._getString(3)

    def setCurrencyType(self, value):
        self._setString(3, value)
        return

    def getAccountType(self):
        return self._getNumber(4)

    def setAccountType(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(FinancialTooltipModel, self)._initialize()
        self._addStringProperty(b'currencyType', b'')
        self._addNumberProperty(b'accountType', 0)
        return
