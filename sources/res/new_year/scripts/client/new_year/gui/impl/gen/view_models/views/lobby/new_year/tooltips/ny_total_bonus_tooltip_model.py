from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_multiplier_value import NyMultiplierValue

class NyTotalBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NyTotalBonusTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getPrevBonus(self):
        return self._getReal(0)

    def setPrevBonus(self, value):
        self._setReal(0, value)
        return

    def getCurrentBonus(self):
        return self._getReal(1)

    def setCurrentBonus(self, value):
        self._setReal(1, value)
        return

    def getMaxBonus(self):
        return self._getReal(2)

    def setMaxBonus(self, value):
        self._setReal(2, value)
        return

    def getMultipliersTable(self):
        return self._getArray(3)

    def setMultipliersTable(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getMultipliersTableType():
        return NyMultiplierValue

    def _initialize(self):
        super(NyTotalBonusTooltipModel, self)._initialize()
        self._addRealProperty(b'prevBonus', 0.0)
        self._addRealProperty(b'currentBonus', 0.0)
        self._addRealProperty(b'maxBonus', 25)
        self._addArrayProperty(b'multipliersTable', Array())
        return
