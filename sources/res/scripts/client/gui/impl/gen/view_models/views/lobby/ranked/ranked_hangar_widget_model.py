from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.ranked.widget_rank_model import WidgetRankModel

class RankedHangarWidgetModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=15, commands=1):
        super(RankedHangarWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rankLeft(self):
        return self._getViewModel(0)

    @staticmethod
    def getRankLeftType():
        return WidgetRankModel

    @property
    def rankRight(self):
        return self._getViewModel(1)

    @staticmethod
    def getRankRightType():
        return WidgetRankModel

    def getSteps(self):
        return self._getNumber(2)

    def setSteps(self, value):
        self._setNumber(2, value)
        return

    def getStepsTotal(self):
        return self._getNumber(3)

    def setStepsTotal(self, value):
        self._setNumber(3, value)
        return

    def getHasLeftRank(self):
        return self._getBool(4)

    def setHasLeftRank(self, value):
        self._setBool(4, value)
        return

    def getIsFinal(self):
        return self._getBool(5)

    def setIsFinal(self, value):
        self._setBool(5, value)
        return

    def getBonusBattles(self):
        return self._getNumber(6)

    def setBonusBattles(self, value):
        self._setNumber(6, value)
        return

    def getLeagueID(self):
        return self._getNumber(7)

    def setLeagueID(self, value):
        self._setNumber(7, value)
        return

    def getEfficiency(self):
        return self._getReal(8)

    def setEfficiency(self, value):
        self._setReal(8, value)
        return

    def getEfficiencyDiff(self):
        return self._getReal(9)

    def setEfficiencyDiff(self, value):
        self._setReal(9, value)
        return

    def getIsEfficiencyUnavailable(self):
        return self._getBool(10)

    def setIsEfficiencyUnavailable(self, value):
        self._setBool(10, value)
        return

    def getPosition(self):
        return self._getNumber(11)

    def setPosition(self, value):
        self._setNumber(11, value)
        return

    def getIsPositionUnavailable(self):
        return self._getBool(12)

    def setIsPositionUnavailable(self, value):
        self._setBool(12, value)
        return

    def getMaxRank(self):
        return self._getNumber(13)

    def setMaxRank(self, value):
        self._setNumber(13, value)
        return

    def getBattlesTotal(self):
        return self._getNumber(14)

    def setBattlesTotal(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(RankedHangarWidgetModel, self)._initialize()
        self._addViewModelProperty(b'rankLeft', WidgetRankModel())
        self._addViewModelProperty(b'rankRight', WidgetRankModel())
        self._addNumberProperty(b'steps', 0)
        self._addNumberProperty(b'stepsTotal', 0)
        self._addBoolProperty(b'hasLeftRank', False)
        self._addBoolProperty(b'isFinal', False)
        self._addNumberProperty(b'bonusBattles', 0)
        self._addNumberProperty(b'leagueID', -1)
        self._addRealProperty(b'efficiency', 0.0)
        self._addRealProperty(b'efficiencyDiff', 0.0)
        self._addBoolProperty(b'isEfficiencyUnavailable', False)
        self._addNumberProperty(b'position', 0)
        self._addBoolProperty(b'isPositionUnavailable', False)
        self._addNumberProperty(b'maxRank', 0)
        self._addNumberProperty(b'battlesTotal', 0)
        self.onClick = self._addCommand(b'onClick')
        return
