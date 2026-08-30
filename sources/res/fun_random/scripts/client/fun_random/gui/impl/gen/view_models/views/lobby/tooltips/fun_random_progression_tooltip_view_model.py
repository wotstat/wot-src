from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomProgressionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FunRandomProgressionTooltipViewModel, self).__init__(properties=properties, commands=commands)
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

    @property
    def currentStage(self):
        return self._getViewModel(2)

    @staticmethod
    def getCurrentStageType():
        return FunRandomProgressionStage

    def getAssetsPointer(self):
        return self._getString(3)

    def setAssetsPointer(self, value):
        self._setString(3, value)
        return

    def getIsMultipleSubModes(self):
        return self._getBool(4)

    def setIsMultipleSubModes(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(FunRandomProgressionTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'state', FunRandomProgressionState())
        self._addViewModelProperty(b'condition', FunRandomProgressionCondition())
        self._addViewModelProperty(b'currentStage', FunRandomProgressionStage())
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addBoolProperty(b'isMultipleSubModes', True)
        return
