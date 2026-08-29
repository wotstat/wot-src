from enum import Enum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class SimpleFunProgressionStatus(Enum):
    DISABLED = b'disabled'
    ACTIVE = b'active'
    RESETTABLE = b'resettable'


class ModeSelectorFunRandomWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ModeSelectorFunRandomWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return SimpleFunProgressionStatus(self._getString(1))

    def setStatus(self, value):
        self._setString(1, value.value)
        return

    def getCurrentStage(self):
        return self._getNumber(2)

    def setCurrentStage(self, value):
        self._setNumber(2, value)
        return

    def getResetTimer(self):
        return self._getNumber(3)

    def setResetTimer(self, value):
        self._setNumber(3, value)
        return

    def getStageCurrentPoints(self):
        return self._getNumber(4)

    def setStageCurrentPoints(self, value):
        self._setNumber(4, value)
        return

    def getStageMaximumPoints(self):
        return self._getNumber(5)

    def setStageMaximumPoints(self, value):
        self._setNumber(5, value)
        return

    def getConditionText(self):
        return self._getString(6)

    def setConditionText(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(ModeSelectorFunRandomWidgetModel, self)._initialize()
        self._addStringProperty(b'status')
        self._addNumberProperty(b'currentStage', -1)
        self._addNumberProperty(b'resetTimer', -1)
        self._addNumberProperty(b'stageCurrentPoints', -1)
        self._addNumberProperty(b'stageMaximumPoints', -1)
        self._addStringProperty(b'conditionText', b'')
        return
