from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ArmorValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ArmorValueModel, self).__init__(properties=properties, commands=commands)
        return

    def getColor(self):
        return self._getString(0)

    def setColor(self, value):
        self._setString(0, value)
        return

    def getLeftValue(self):
        return self._getString(1)

    def setLeftValue(self, value):
        self._setString(1, value)
        return

    def getRightValue(self):
        return self._getString(2)

    def setRightValue(self, value):
        self._setString(2, value)
        return

    def getOverlay(self):
        return self._getResource(3)

    def setOverlay(self, value):
        self._setResource(3, value)
        return

    def getIsActive(self):
        return self._getBool(4)

    def setIsActive(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(ArmorValueModel, self)._initialize()
        self._addStringProperty(b'color', b'')
        self._addStringProperty(b'leftValue', b'')
        self._addStringProperty(b'rightValue', b'')
        self._addResourceProperty(b'overlay', R.invalid())
        self._addBoolProperty(b'isActive', True)
        return
