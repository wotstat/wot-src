from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class FortRushProgressionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(FortRushProgressionTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAvailable(self):
        return self._getBool(0)

    def setIsAvailable(self, value):
        self._setBool(0, value)
        return

    def getNewMissionsDateTime(self):
        return self._getNumber(1)

    def setNewMissionsDateTime(self, value):
        self._setNumber(1, value)
        return

    def getIsProgressionCompleted(self):
        return self._getBool(2)

    def setIsProgressionCompleted(self, value):
        self._setBool(2, value)
        return

    def getCurrentProgressionPoints(self):
        return self._getNumber(3)

    def setCurrentProgressionPoints(self, value):
        self._setNumber(3, value)
        return

    def getTotalProgressionPoints(self):
        return self._getNumber(4)

    def setTotalProgressionPoints(self, value):
        self._setNumber(4, value)
        return

    def getCurrentProgressionStage(self):
        return self._getNumber(5)

    def setCurrentProgressionStage(self, value):
        self._setNumber(5, value)
        return

    def getRewards(self):
        return self._getArray(6)

    def setRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(FortRushProgressionTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isAvailable', False)
        self._addNumberProperty(b'newMissionsDateTime', 0)
        self._addBoolProperty(b'isProgressionCompleted', False)
        self._addNumberProperty(b'currentProgressionPoints', 0)
        self._addNumberProperty(b'totalProgressionPoints', 0)
        self._addNumberProperty(b'currentProgressionStage', 0)
        self._addArrayProperty(b'rewards', Array())
        return
