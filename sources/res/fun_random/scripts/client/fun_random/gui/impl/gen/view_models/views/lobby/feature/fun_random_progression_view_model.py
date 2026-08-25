from frameworks.wulf import Array, ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_infinite_progression_condition import FunRandomInfiniteProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onShowInfo', b'onOpenTierList')

    def __init__(self, properties=8, commands=3):
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

    @property
    def infiniteCondition(self):
        return self._getViewModel(2)

    @staticmethod
    def getInfiniteConditionType():
        return FunRandomInfiniteProgressionCondition

    @property
    def infiniteStage(self):
        return self._getViewModel(3)

    @staticmethod
    def getInfiniteStageType():
        return FunRandomProgressionStage

    def getStages(self):
        return self._getArray(4)

    def setStages(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getStagesType():
        return FunRandomProgressionStage

    def getAssetsPointer(self):
        return self._getString(5)

    def setAssetsPointer(self, value):
        self._setString(5, value)
        return

    def getIsFirstOpen(self):
        return self._getBool(6)

    def setIsFirstOpen(self, value):
        self._setBool(6, value)
        return

    def getModeViewSettings(self):
        return self._getString(7)

    def setModeViewSettings(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(FunRandomProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'state', FunRandomProgressionState())
        self._addViewModelProperty(b'condition', FunRandomProgressionCondition())
        self._addViewModelProperty(b'infiniteCondition', FunRandomInfiniteProgressionCondition())
        self._addViewModelProperty(b'infiniteStage', FunRandomProgressionStage())
        self._addArrayProperty(b'stages', Array())
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addBoolProperty(b'isFirstOpen', False)
        self._addStringProperty(b'modeViewSettings', b'{}')
        self.onClose = self._addCommand(b'onClose')
        self.onShowInfo = self._addCommand(b'onShowInfo')
        self.onOpenTierList = self._addCommand(b'onOpenTierList')
        return
