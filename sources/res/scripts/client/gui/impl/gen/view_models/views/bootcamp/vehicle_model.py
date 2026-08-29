from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VehicleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(VehicleModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'name', b'')
        return
