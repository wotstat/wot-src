from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomHangarWidgetViewModel(ViewModel):
    __slots__ = (b'onShowInfo',)

    def __init__(self, properties=4, commands=1):
        super(FunRandomHangarWidgetViewModel, self).__init__(properties=properties, commands=commands)
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

    def getActiveModeResName(self):
        return self._getString(2)

    def setActiveModeResName(self, value):
        self._setString(2, value)
        return

    def getModifiersDomains(self):
        return self._getArray(3)

    def setModifiersDomains(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getModifiersDomainsType():
        return unicode

    def _initialize(self):
        super(FunRandomHangarWidgetViewModel, self)._initialize()
        self._addViewModelProperty(b'progressionState', FunRandomProgressionState())
        self._addViewModelProperty(b'currentProgressionStage', FunRandomProgressionStage())
        self._addStringProperty(b'activeModeResName', b'undefined')
        self._addArrayProperty(b'modifiersDomains', Array())
        self.onShowInfo = self._addCommand(b'onShowInfo')
        return
