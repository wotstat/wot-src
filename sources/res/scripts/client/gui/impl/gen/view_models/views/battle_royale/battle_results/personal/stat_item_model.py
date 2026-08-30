from frameworks.wulf import ViewModel
from gui.impl.gen import R

class StatItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(StatItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getWreathImage(self):
        return self._getResource(1)

    def setWreathImage(self, value):
        self._setResource(1, value)
        return

    def getCurrentValue(self):
        return self._getNumber(2)

    def setCurrentValue(self, value):
        self._setNumber(2, value)
        return

    def getMaxValue(self):
        return self._getNumber(3)

    def setMaxValue(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(StatItemModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addResourceProperty(b'wreathImage', R.invalid())
        self._addNumberProperty(b'currentValue', -1)
        self._addNumberProperty(b'maxValue', -1)
        return
