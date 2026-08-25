from enum import IntEnum
from frameworks.wulf import Array
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import ModePerformanceModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_model import ModeSelectorCardModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_reward_model import ModeSelectorRewardModel

class BattlePassState(IntEnum):
    NONE = 0
    STATIC = 1
    NEW = 2


class ModeSelectorNormalCardModel(ModeSelectorCardModel):
    __slots__ = ()

    def __init__(self, properties=22, commands=0):
        super(ModeSelectorNormalCardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def widget(self):
        return self._getViewModel(10)

    @staticmethod
    def getWidgetType():
        return ModeSelectorBaseWidgetModel

    @property
    def performance(self):
        return self._getViewModel(11)

    @staticmethod
    def getPerformanceType():
        return ModePerformanceModel

    def getName(self):
        return self._getString(12)

    def setName(self, value):
        self._setString(12, value)
        return

    def getEventName(self):
        return self._getString(13)

    def setEventName(self, value):
        self._setString(13, value)
        return

    def getStatusNotActive(self):
        return self._getString(14)

    def setStatusNotActive(self, value):
        self._setString(14, value)
        return

    def getStatusActive(self):
        return self._getString(15)

    def setStatusActive(self, value):
        self._setString(15, value)
        return

    def getDescription(self):
        return self._getString(16)

    def setDescription(self, value):
        self._setString(16, value)
        return

    def getConditions(self):
        return self._getString(17)

    def setConditions(self, value):
        self._setString(17, value)
        return

    def getTimeLeft(self):
        return self._getString(18)

    def setTimeLeft(self, value):
        self._setString(18, value)
        return

    def getRewardList(self):
        return self._getArray(19)

    def setRewardList(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getRewardListType():
        return ModeSelectorRewardModel

    def getBattlePassState(self):
        return BattlePassState(self._getNumber(20))

    def setBattlePassState(self, value):
        self._setNumber(20, value.value)
        return

    def getExternalPath(self):
        return self._getResource(21)

    def setExternalPath(self, value):
        self._setResource(21, value)
        return

    def _initialize(self):
        super(ModeSelectorNormalCardModel, self)._initialize()
        self._addViewModelProperty(b'widget', ModeSelectorBaseWidgetModel())
        self._addViewModelProperty(b'performance', ModePerformanceModel())
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'eventName', b'')
        self._addStringProperty(b'statusNotActive', b'')
        self._addStringProperty(b'statusActive', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'conditions', b'')
        self._addStringProperty(b'timeLeft', b'')
        self._addArrayProperty(b'rewardList', Array())
        self._addNumberProperty(b'battlePassState')
        self._addResourceProperty(b'externalPath', R.invalid())
        return
