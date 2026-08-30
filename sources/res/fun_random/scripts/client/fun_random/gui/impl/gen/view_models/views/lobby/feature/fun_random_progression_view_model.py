from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onShowInfo', b'onViewSwitch')

    def __init__(self, properties=5, commands=3):
        super(FunRandomProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def state(self):
        return self._getViewModel(0)

    @staticmethod
    def getStateType():
        return FunRandomProgressionState

    @property
    def condition(self):
        return self._getViewModel(1)

    @staticmethod
    def getConditionType():
        return FunRandomProgressionCondition

    def getStages(self):
        return self._getArray(2)

    def setStages(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getStagesType():
        return FunRandomProgressionStage

    def getAssetsPointer(self):
        return self._getString(3)

    def setAssetsPointer(self, value):
        self._setString(3, value)
        return

    def getIsNavigationButtonVisible(self):
        return self._getBool(4)

    def setIsNavigationButtonVisible(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(FunRandomProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'state', FunRandomProgressionState())
        self._addViewModelProperty(b'condition', FunRandomProgressionCondition())
        self._addArrayProperty(b'stages', Array())
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addBoolProperty(b'isNavigationButtonVisible', False)
        self.onClose = self._addCommand(b'onClose')
        self.onShowInfo = self._addCommand(b'onShowInfo')
        self.onViewSwitch = self._addCommand(b'onViewSwitch')
        return
