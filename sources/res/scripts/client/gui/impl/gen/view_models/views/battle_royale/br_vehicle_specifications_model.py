from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BrVehicleSpecificationsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BrVehicleSpecificationsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSpecName(self):
        return self._getResource(0)

    def setSpecName(self, value):
        self._setResource(0, value)
        return

    def getIconSource(self):
        return self._getResource(1)

    def setIconSource(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(BrVehicleSpecificationsModel, self)._initialize()
        self._addResourceProperty(b'specName', R.invalid())
        self._addResourceProperty(b'iconSource', R.invalid())
        return
