from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import ModePerformanceModel

class CardState(IntEnum):
    NOT_STARTED = 0
    ACTIVE = 1
    DISABLED = 2
    FINISHED = 3


class FunRandomSubSelectorCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(FunRandomSubSelectorCardModel, self).__init__(properties=properties, commands=commands)
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

    def getSubModeId(self):
        return self._getNumber(2)

    def setSubModeId(self, value):
        self._setNumber(2, value)
        return

    def getConditions(self):
        return self._getString(3)

    def setConditions(self, value):
        self._setString(3, value)
        return

    def getState(self):
        return CardState(self._getNumber(4))

    def setState(self, value):
        self._setNumber(4, value.value)
        return

    def getIsSelected(self):
        return self._getBool(5)

    def setIsSelected(self, value):
        self._setBool(5, value)
        return

    def getTimeLeft(self):
        return self._getString(6)

    def setTimeLeft(self, value):
        self._setString(6, value)
        return

    def getTimeToStart(self):
        return self._getNumber(7)

    def setTimeToStart(self, value):
        self._setNumber(7, value)
        return

    def getModifiersDomains(self):
        return self._getArray(8)

    def setModifiersDomains(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getModifiersDomainsType():
        return unicode

    def _initialize(self):
        super(FunRandomSubSelectorCardModel, self)._initialize()
        self._addViewModelProperty(b'performance', ModePerformanceModel())
        self._addStringProperty(b'assetsPointer', b'')
        self._addNumberProperty(b'subModeId', 0)
        self._addStringProperty(b'conditions', b'')
        self._addNumberProperty(b'state')
        self._addBoolProperty(b'isSelected', False)
        self._addStringProperty(b'timeLeft', b'')
        self._addNumberProperty(b'timeToStart', -1)
        self._addArrayProperty(b'modifiersDomains', Array())
        return
