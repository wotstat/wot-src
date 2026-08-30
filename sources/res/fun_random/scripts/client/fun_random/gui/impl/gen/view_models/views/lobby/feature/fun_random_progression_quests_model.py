from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_infinite_progression_condition import FunRandomInfiniteProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomProgressionQuestsModel(ViewModel):
    __slots__ = (b'onMissionClick', b'onMarkAsViewed')

    def __init__(self, properties=4, commands=2):
        super(FunRandomProgressionQuestsModel, self).__init__(properties=properties, commands=commands)
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

    def getAssetsPointer(self):
        return self._getString(3)

    def setAssetsPointer(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(FunRandomProgressionQuestsModel, self)._initialize()
        self._addViewModelProperty(b'state', FunRandomProgressionState())
        self._addViewModelProperty(b'condition', FunRandomProgressionCondition())
        self._addViewModelProperty(b'infiniteCondition', FunRandomInfiniteProgressionCondition())
        self._addStringProperty(b'assetsPointer', b'undefined')
        self.onMissionClick = self._addCommand(b'onMissionClick')
        self.onMarkAsViewed = self._addCommand(b'onMarkAsViewed')
        return
