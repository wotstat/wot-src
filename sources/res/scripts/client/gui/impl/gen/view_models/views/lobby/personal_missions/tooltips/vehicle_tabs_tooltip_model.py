from frameworks.wulf import ViewModel

class VehicleTabsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleTabsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMinVehicleLevel(self):
        return self._getNumber(0)

    def setMinVehicleLevel(self, value):
        self._setNumber(0, value)
        return

    def getMaxVehicleLevel(self):
        return self._getNumber(1)

    def setMaxVehicleLevel(self, value):
        self._setNumber(1, value)
        return

    def getBranchName(self):
        return self._getString(2)

    def setBranchName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(VehicleTabsTooltipModel, self)._initialize()
        self._addNumberProperty(b'minVehicleLevel', 0)
        self._addNumberProperty(b'maxVehicleLevel', 0)
        self._addStringProperty(b'branchName', b'')
        return
