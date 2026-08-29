from frameworks.wulf import ViewModel

class VehicleSelectorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleSelectorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getRoverType(self):
        return self._getString(0)

    def setRoverType(self, value):
        self._setString(0, value)
        return

    def getRoverName(self):
        return self._getString(1)

    def setRoverName(self, value):
        self._setString(1, value)
        return

    def getShortDescription(self):
        return self._getString(2)

    def setShortDescription(self, value):
        self._setString(2, value)
        return

    def getLongDescription(self):
        return self._getString(3)

    def setLongDescription(self, value):
        self._setString(3, value)
        return

    def getIcon(self):
        return self._getString(4)

    def setIcon(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(VehicleSelectorTooltipModel, self)._initialize()
        self._addStringProperty(b'roverType', b'')
        self._addStringProperty(b'roverName', b'')
        self._addStringProperty(b'shortDescription', b'')
        self._addStringProperty(b'longDescription', b'')
        self._addStringProperty(b'icon', b'')
        return
