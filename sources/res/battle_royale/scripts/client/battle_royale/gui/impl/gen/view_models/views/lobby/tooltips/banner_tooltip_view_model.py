from enum import Enum
from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel

class PerformanceRisk(Enum):
    LOW = b'low'
    MEDIUM = b'medium'
    HIGH = b'high'


class BannerTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BannerTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eventInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getEventInfoType():
        return BattleRoyaleEventModel

    def getTime(self):
        return self._getNumber(1)

    def setTime(self, value):
        self._setNumber(1, value)
        return

    def getModeState(self):
        return self._getString(2)

    def setModeState(self, value):
        self._setString(2, value)
        return

    def getPerformanceRisk(self):
        return PerformanceRisk(self._getString(3))

    def setPerformanceRisk(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(BannerTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'eventInfo', BattleRoyaleEventModel())
        self._addNumberProperty(b'time', 0)
        self._addStringProperty(b'modeState', b'')
        self._addStringProperty(b'performanceRisk', PerformanceRisk.HIGH.value)
        return
