from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BlueprintValuePrice(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BlueprintValuePrice, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getNotEnough(self):
        return self._getBool(3)

    def setNotEnough(self, value):
        self._setBool(3, value)
        return

    def getHasDelimeter(self):
        return self._getBool(4)

    def setHasDelimeter(self, value):
        self._setBool(4, value)
        return

    def getItemCD(self):
        return self._getNumber(5)

    def setItemCD(self, value):
        self._setNumber(5, value)
        return

    def getTooltipId(self):
        return self._getString(6)

    def setTooltipId(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(BlueprintValuePrice, self)._initialize()
        self._addStringProperty(b'value', b'0')
        self._addStringProperty(b'type', b'custom')
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'notEnough', False)
        self._addBoolProperty(b'hasDelimeter', False)
        self._addNumberProperty(b'itemCD', 0)
        self._addStringProperty(b'tooltipId', b'')
        return
