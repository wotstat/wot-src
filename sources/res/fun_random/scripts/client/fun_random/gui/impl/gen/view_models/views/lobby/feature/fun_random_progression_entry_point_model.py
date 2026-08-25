from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomProgressionEntryPointModel(ViewModel):
    __slots__ = (b'onShowInfo',)

    def __init__(self, properties=2, commands=1):
        super(FunRandomProgressionEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progressionState(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionStateType():
        return FunRandomProgressionState

    @property
    def currentProgressionStage(self):
        return self._getViewModel(1)

    @staticmethod
    def getCurrentProgressionStageType():
        return FunRandomProgressionStage

    def _initialize(self):
        super(FunRandomProgressionEntryPointModel, self)._initialize()
        self._addViewModelProperty(b'progressionState', FunRandomProgressionState())
        self._addViewModelProperty(b'currentProgressionStage', FunRandomProgressionStage())
        self.onShowInfo = self._addCommand(b'onShowInfo')
        return
