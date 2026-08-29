from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NationChangeSupplyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NationChangeSupplyModel, self).__init__(properties=properties, commands=commands)
        return

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(NationChangeSupplyModel, self)._initialize()
        self._addResourceProperty(b'image', R.invalid())
        self._addNumberProperty(b'intCD', 0)
        return
