from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BootcampNationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BootcampNationModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getVehicleIcon(self):
        return self._getResource(3)

    def setVehicleIcon(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(BootcampNationModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'label', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addResourceProperty(b'vehicleIcon', R.invalid())
        return
