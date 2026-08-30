from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_rank_model import ModeSelectorRankModel

class ModeSelectorRankedWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(ModeSelectorRankedWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rankLeft(self):
        return self._getViewModel(1)

    @staticmethod
    def getRankLeftType():
        return ModeSelectorRankModel

    @property
    def rankRight(self):
        return self._getViewModel(2)

    @staticmethod
    def getRankRightType():
        return ModeSelectorRankModel

    def getSteps(self):
        return self._getNumber(3)

    def setSteps(self, value):
        self._setNumber(3, value)
        return

    def getStepsTotal(self):
        return self._getNumber(4)

    def setStepsTotal(self, value):
        self._setNumber(4, value)
        return

    def getHasLeftRank(self):
        return self._getBool(5)

    def setHasLeftRank(self, value):
        self._setBool(5, value)
        return

    def getIsFinal(self):
        return self._getBool(6)

    def setIsFinal(self, value):
        self._setBool(6, value)
        return

    def getBonusBattles(self):
        return self._getNumber(7)

    def setBonusBattles(self, value):
        self._setNumber(7, value)
        return

    def getQualBattles(self):
        return self._getNumber(8)

    def setQualBattles(self, value):
        self._setNumber(8, value)
        return

    def getQualTotalBattles(self):
        return self._getNumber(9)

    def setQualTotalBattles(self, value):
        self._setNumber(9, value)
        return

    def getLeagueID(self):
        return self._getNumber(10)

    def setLeagueID(self, value):
        self._setNumber(10, value)
        return

    def getEfficiency(self):
        return self._getReal(11)

    def setEfficiency(self, value):
        self._setReal(11, value)
        return

    def getEfficiencyDiff(self):
        return self._getReal(12)

    def setEfficiencyDiff(self, value):
        self._setReal(12, value)
        return

    def getIsEfficiencyUnavailable(self):
        return self._getBool(13)

    def setIsEfficiencyUnavailable(self, value):
        self._setBool(13, value)
        return

    def getPosition(self):
        return self._getNumber(14)

    def setPosition(self, value):
        self._setNumber(14, value)
        return

    def getIsPositionUnavailable(self):
        return self._getBool(15)

    def setIsPositionUnavailable(self, value):
        self._setBool(15, value)
        return

    def getMaxRank(self):
        return self._getNumber(16)

    def setMaxRank(self, value):
        self._setNumber(16, value)
        return

    def getBattlesTotal(self):
        return self._getNumber(17)

    def setBattlesTotal(self, value):
        self._setNumber(17, value)
        return

    def _initialize(self):
        super(ModeSelectorRankedWidgetModel, self)._initialize()
        self._addViewModelProperty(b'rankLeft', ModeSelectorRankModel())
        self._addViewModelProperty(b'rankRight', ModeSelectorRankModel())
        self._addNumberProperty(b'steps', 0)
        self._addNumberProperty(b'stepsTotal', 0)
        self._addBoolProperty(b'hasLeftRank', False)
        self._addBoolProperty(b'isFinal', False)
        self._addNumberProperty(b'bonusBattles', 0)
        self._addNumberProperty(b'qualBattles', 0)
        self._addNumberProperty(b'qualTotalBattles', 0)
        self._addNumberProperty(b'leagueID', -1)
        self._addRealProperty(b'efficiency', 0.0)
        self._addRealProperty(b'efficiencyDiff', 0.0)
        self._addBoolProperty(b'isEfficiencyUnavailable', False)
        self._addNumberProperty(b'position', 0)
        self._addBoolProperty(b'isPositionUnavailable', False)
        self._addNumberProperty(b'maxRank', 0)
        self._addNumberProperty(b'battlesTotal', 0)
        return
