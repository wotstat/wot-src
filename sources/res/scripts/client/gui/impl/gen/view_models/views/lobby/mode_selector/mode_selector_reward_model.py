from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ModeSelectorRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ModeSelectorRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getResource(1)

    def setName(self, value):
        self._setResource(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getVehicleLevel(self):
        return self._getString(3)

    def setVehicleLevel(self, value):
        self._setString(3, value)
        return

    def getVehicleType(self):
        return self._getString(4)

    def setVehicleType(self, value):
        self._setString(4, value)
        return

    def getIsPremium(self):
        return self._getBool(5)

    def setIsPremium(self, value):
        self._setBool(5, value)
        return

    def getTooltipID(self):
        return self._getString(6)

    def setTooltipID(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(ModeSelectorRewardModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addResourceProperty(b'name', R.invalid())
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'vehicleLevel', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addBoolProperty(b'isPremium', False)
        self._addStringProperty(b'tooltipID', b'')
        return
