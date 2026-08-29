from enum import Enum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class BattleRoyaleProgressionStatus(Enum):
    DISABLED = b'disabled'
    ACTIVE = b'active'


class ModeSelectorBattleRoyaleWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ModeSelectorBattleRoyaleWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return BattleRoyaleProgressionStatus(self._getString(1))

    def setStatus(self, value):
        self._setString(1, value.value)
        return

    def getCurrentStage(self):
        return self._getNumber(2)

    def setCurrentStage(self, value):
        self._setNumber(2, value)
        return

    def getStageCurrentPoints(self):
        return self._getNumber(3)

    def setStageCurrentPoints(self, value):
        self._setNumber(3, value)
        return

    def getStageMaximumPoints(self):
        return self._getNumber(4)

    def setStageMaximumPoints(self, value):
        self._setNumber(4, value)
        return

    def getIconPostfix(self):
        return self._getString(5)

    def setIconPostfix(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(ModeSelectorBattleRoyaleWidgetModel, self)._initialize()
        self._addStringProperty(b'status')
        self._addNumberProperty(b'currentStage', -1)
        self._addNumberProperty(b'stageCurrentPoints', -1)
        self._addNumberProperty(b'stageMaximumPoints', -1)
        self._addStringProperty(b'iconPostfix', b'')
        return
