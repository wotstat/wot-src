from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class AdditionalRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AdditionalRewardsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getHeaderText(self):
        return self._getResource(0)

    def setHeaderText(self, value):
        self._setResource(0, value)
        return

    def getHeaderCount(self):
        return self._getNumber(1)

    def setHeaderCount(self, value):
        self._setNumber(1, value)
        return

    def getDescription(self):
        return self._getResource(2)

    def setDescription(self, value):
        self._setResource(2, value)
        return

    def getDescriptionCount(self):
        return self._getNumber(3)

    def setDescriptionCount(self, value):
        self._setNumber(3, value)
        return

    def getBonus(self):
        return self._getArray(4)

    def setBonus(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getBonusType():
        return BonusModel

    def _initialize(self):
        super(AdditionalRewardsTooltipModel, self)._initialize()
        self._addResourceProperty(b'headerText', R.invalid())
        self._addNumberProperty(b'headerCount', 0)
        self._addResourceProperty(b'description', R.invalid())
        self._addNumberProperty(b'descriptionCount', 0)
        self._addArrayProperty(b'bonus', Array())
        return
