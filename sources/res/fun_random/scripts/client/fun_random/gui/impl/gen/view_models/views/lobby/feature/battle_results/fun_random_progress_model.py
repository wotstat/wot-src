from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class FunRandomProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(FunRandomProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasProgress(self):
        return self._getBool(0)

    def setHasProgress(self, value):
        self._setBool(0, value)
        return

    def getAssetsPointer(self):
        return self._getString(1)

    def setAssetsPointer(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getIsInUnlimitedProgression(self):
        return self._getBool(3)

    def setIsInUnlimitedProgression(self, value):
        self._setBool(3, value)
        return

    def getPreviousStage(self):
        return self._getNumber(4)

    def setPreviousStage(self, value):
        self._setNumber(4, value)
        return

    def getCurrentStage(self):
        return self._getNumber(5)

    def setCurrentStage(self, value):
        self._setNumber(5, value)
        return

    def getMaximumStage(self):
        return self._getNumber(6)

    def setMaximumStage(self, value):
        self._setNumber(6, value)
        return

    def getPreviousPoints(self):
        return self._getNumber(7)

    def setPreviousPoints(self, value):
        self._setNumber(7, value)
        return

    def getEarnedPoints(self):
        return self._getNumber(8)

    def setEarnedPoints(self, value):
        self._setNumber(8, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(9)

    def setCurrentPoints(self, value):
        self._setNumber(9, value)
        return

    def getMaximumPoints(self):
        return self._getNumber(10)

    def setMaximumPoints(self, value):
        self._setNumber(10, value)
        return

    def getRewards(self):
        return self._getArray(11)

    def setRewards(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getStageRequiredCounters(self):
        return self._getArray(12)

    def setStageRequiredCounters(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getStageRequiredCountersType():
        return int

    def _initialize(self):
        super(FunRandomProgressModel, self)._initialize()
        self._addBoolProperty(b'hasProgress', False)
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'isInUnlimitedProgression', False)
        self._addNumberProperty(b'previousStage', -1)
        self._addNumberProperty(b'currentStage', -1)
        self._addNumberProperty(b'maximumStage', -1)
        self._addNumberProperty(b'previousPoints', -1)
        self._addNumberProperty(b'earnedPoints', -1)
        self._addNumberProperty(b'currentPoints', -1)
        self._addNumberProperty(b'maximumPoints', -1)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'stageRequiredCounters', Array())
        return
