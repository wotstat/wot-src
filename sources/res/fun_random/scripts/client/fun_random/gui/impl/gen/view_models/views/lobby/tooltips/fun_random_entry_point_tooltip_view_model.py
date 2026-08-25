from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import ModePerformanceModel

class FunRandomEntryPointTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomEntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def performance(self):
        return self._getViewModel(0)

    @staticmethod
    def getPerformanceType():
        return ModePerformanceModel

    def getAssetsPointer(self):
        return self._getString(1)

    def setAssetsPointer(self, value):
        self._setString(1, value)
        return

    def getModeState(self):
        return self._getString(2)

    def setModeState(self, value):
        self._setString(2, value)
        return

    def getStartTime(self):
        return self._getNumber(3)

    def setStartTime(self, value):
        self._setNumber(3, value)
        return

    def getLeftTime(self):
        return self._getNumber(4)

    def setLeftTime(self, value):
        self._setNumber(4, value)
        return

    def getEndTime(self):
        return self._getNumber(5)

    def setEndTime(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(FunRandomEntryPointTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'performance', ModePerformanceModel())
        self._addStringProperty(b'assetsPointer', b'undefined')
        self._addStringProperty(b'modeState', b'')
        self._addNumberProperty(b'startTime', 0)
        self._addNumberProperty(b'leftTime', 0)
        self._addNumberProperty(b'endTime', 0)
        return
