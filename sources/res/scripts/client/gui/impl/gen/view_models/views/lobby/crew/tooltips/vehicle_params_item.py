from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ValueStyleEnum(Enum):
    GREENBRIGHT = b'greenBright'
    RED = b'red'
    WHITEORANGE = b'whiteOrange'
    YELLOW = b'yellow'
    WHITESPANISH = b'whiteSpanish'


class VehicleParamsItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleParamsItem, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getAsteriskIcon(self):
        return self._getResource(4)

    def setAsteriskIcon(self, value):
        self._setResource(4, value)
        return

    def _initialize(self):
        super(VehicleParamsItem, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'value', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isEnabled', True)
        self._addResourceProperty(b'asteriskIcon', R.invalid())
        return
