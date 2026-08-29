from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BlueprintPrice(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(BlueprintPrice, self).__init__(properties=properties, commands=commands)
        return

    def getIconBig(self):
        return self._getResource(0)

    def setIconBig(self, value):
        self._setResource(0, value)
        return

    def getNationName(self):
        return self._getString(1)

    def setNationName(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getNumber(2)

    def setValue(self, value):
        self._setNumber(2, value)
        return

    def getHasDelimeter(self):
        return self._getBool(3)

    def setHasDelimeter(self, value):
        self._setBool(3, value)
        return

    def getItemCD(self):
        return self._getNumber(4)

    def setItemCD(self, value):
        self._setNumber(4, value)
        return

    def getTooltipId(self):
        return self._getString(5)

    def setTooltipId(self, value):
        self._setString(5, value)
        return

    def getType(self):
        return self._getString(6)

    def setType(self, value):
        self._setString(6, value)
        return

    def getIcon(self):
        return self._getResource(7)

    def setIcon(self, value):
        self._setResource(7, value)
        return

    def getNotEnough(self):
        return self._getBool(8)

    def setNotEnough(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(BlueprintPrice, self)._initialize()
        self._addResourceProperty(b'iconBig', R.invalid())
        self._addStringProperty(b'nationName', b'')
        self._addNumberProperty(b'value', 0)
        self._addBoolProperty(b'hasDelimeter', False)
        self._addNumberProperty(b'itemCD', 0)
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'type', b'custom')
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'notEnough', False)
        return
