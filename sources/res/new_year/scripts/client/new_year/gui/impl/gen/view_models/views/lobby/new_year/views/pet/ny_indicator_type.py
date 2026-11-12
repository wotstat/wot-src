from enum import Enum
from frameworks.wulf import ViewModel

class IndicatorType(Enum):
    FOOD = b'food'
    FUN = b'fun'
    ACTIVITY = b'activity'


class NyIndicatorType(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyIndicatorType, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return IndicatorType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(NyIndicatorType, self)._initialize()
        self._addStringProperty(b'type')
        return
