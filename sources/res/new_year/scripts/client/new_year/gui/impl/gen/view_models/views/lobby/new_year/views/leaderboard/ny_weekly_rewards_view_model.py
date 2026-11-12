from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_stage_model import NyStageModel

class NyWeeklyRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onInfoClick', b'onPreviewClick', b'onTabSelected')

    def __init__(self, properties=5, commands=4):
        super(NyWeeklyRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentStage(self):
        return self._getNumber(0)

    def setCurrentStage(self, value):
        self._setNumber(0, value)
        return

    def getFinalStageComplete(self):
        return self._getBool(1)

    def setFinalStageComplete(self, value):
        self._setBool(1, value)
        return

    def getIsRecalc(self):
        return self._getBool(2)

    def setIsRecalc(self, value):
        self._setBool(2, value)
        return

    def getStages(self):
        return self._getArray(3)

    def setStages(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getStagesType():
        return NyStageModel

    def getIsFromMainView(self):
        return self._getBool(4)

    def setIsFromMainView(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(NyWeeklyRewardsViewModel, self)._initialize()
        self._addNumberProperty(b'currentStage', 0)
        self._addBoolProperty(b'finalStageComplete', False)
        self._addBoolProperty(b'isRecalc', False)
        self._addArrayProperty(b'stages', Array())
        self._addBoolProperty(b'isFromMainView', True)
        self.onClose = self._addCommand(b'onClose')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        self.onPreviewClick = self._addCommand(b'onPreviewClick')
        self.onTabSelected = self._addCommand(b'onTabSelected')
        return
