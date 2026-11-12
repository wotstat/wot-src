from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel

class NyPetBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NyPetBonusTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentBonus(self):
        return self._getNumber(0)

    def setCurrentBonus(self, value):
        self._setNumber(0, value)
        return

    def getMinBonus(self):
        return self._getNumber(1)

    def setMinBonus(self, value):
        self._setNumber(1, value)
        return

    def getMaxBonus(self):
        return self._getNumber(2)

    def setMaxBonus(self, value):
        self._setNumber(2, value)
        return

    def getWasLeaderboardFinished(self):
        return self._getBool(3)

    def setWasLeaderboardFinished(self, value):
        self._setBool(3, value)
        return

    def getIndicators(self):
        return self._getArray(4)

    def setIndicators(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getIndicatorsType():
        return NyPetIndicatorModel

    def _initialize(self):
        super(NyPetBonusTooltipModel, self)._initialize()
        self._addNumberProperty(b'currentBonus', 0)
        self._addNumberProperty(b'minBonus', 0)
        self._addNumberProperty(b'maxBonus', 0)
        self._addBoolProperty(b'wasLeaderboardFinished', False)
        self._addArrayProperty(b'indicators', Array())
        return
