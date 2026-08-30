from enum import Enum
from frameworks.wulf import ViewModel

class HighlightType(Enum):
    NONE = b'none'
    INCREASE = b'increase'
    DECREASE = b'decrease'
    SITUATIONAL = b'situational'


class VehicleParamBaseViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleParamBaseViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getTooltipID(self):
        return self._getString(2)

    def setTooltipID(self, value):
        self._setString(2, value)
        return

    def getValue(self):
        return self._getString(3)

    def setValue(self, value):
        self._setString(3, value)
        return

    def getHighlightType(self):
        return HighlightType(self._getString(4))

    def setHighlightType(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(VehicleParamBaseViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isEnabled', False)
        self._addStringProperty(b'tooltipID', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'highlightType')
        return
