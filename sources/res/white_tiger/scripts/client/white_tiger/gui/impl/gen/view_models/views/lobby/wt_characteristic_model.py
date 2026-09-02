from gui.impl.gen import R
from frameworks.wulf import ViewModel

class WtCharacteristicModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(WtCharacteristicModel, self).__init__(properties=properties, commands=commands)
        return

    def getParameter(self):
        return self._getString(0)

    def setParameter(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(WtCharacteristicModel, self)._initialize()
        self._addStringProperty(b'parameter', b'')
        self._addResourceProperty(b'icon', R.invalid())
        return
