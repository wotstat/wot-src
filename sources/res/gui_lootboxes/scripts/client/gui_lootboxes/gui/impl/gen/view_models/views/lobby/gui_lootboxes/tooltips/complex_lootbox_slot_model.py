from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class ComplexLootboxSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ComplexLootboxSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)
        return

    def getProbability(self):
        return self._getReal(1)

    def setProbability(self, value):
        self._setReal(1, value)
        return

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(ComplexLootboxSlotModel, self)._initialize()
        self._addStringProperty(b'description', b'')
        self._addRealProperty(b'probability', 0.0)
        self._addArrayProperty(b'bonuses', Array())
        return
