from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class Rarity(Enum):
    ORDINARY = b'ordinary'
    UNUSUAL = b'unusual'
    RARE = b'rare'
    EPIC = b'epic'
    LEGENDARY = b'legendary'


class FunRandomProgressionStage(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomProgressionStage, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentPoints(self):
        return self._getNumber(0)

    def setCurrentPoints(self, value):
        self._setNumber(0, value)
        return

    def getRequiredPoints(self):
        return self._getNumber(1)

    def setRequiredPoints(self, value):
        self._setNumber(1, value)
        return

    def getMaximumPoints(self):
        return self._getNumber(2)

    def setMaximumPoints(self, value):
        self._setNumber(2, value)
        return

    def getIsCompleted(self):
        return self._getBool(3)

    def setIsCompleted(self, value):
        self._setBool(3, value)
        return

    def getRarity(self):
        return Rarity(self._getString(4))

    def setRarity(self, value):
        self._setString(4, value.value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(FunRandomProgressionStage, self)._initialize()
        self._addNumberProperty(b'currentPoints', -1)
        self._addNumberProperty(b'requiredPoints', -1)
        self._addNumberProperty(b'maximumPoints', -1)
        self._addBoolProperty(b'isCompleted', False)
        self._addStringProperty(b'rarity')
        self._addArrayProperty(b'rewards', Array())
        return
