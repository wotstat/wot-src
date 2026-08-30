from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BadgeTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BadgeTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getImage(self):
        return self._getResource(1)

    def setImage(self, value):
        self._setResource(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getPlayerName(self):
        return self._getString(3)

    def setPlayerName(self, value):
        self._setString(3, value)
        return

    def getVehicleIcon(self):
        return self._getString(4)

    def setVehicleIcon(self, value):
        self._setString(4, value)
        return

    def getVehicleLevel(self):
        return self._getString(5)

    def setVehicleLevel(self, value):
        self._setString(5, value)
        return

    def getSmallBadgeIcon(self):
        return self._getResource(6)

    def setSmallBadgeIcon(self, value):
        self._setResource(6, value)
        return

    def _initialize(self):
        super(BadgeTooltipViewModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addResourceProperty(b'image', R.invalid())
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'playerName', b'')
        self._addStringProperty(b'vehicleIcon', b'')
        self._addStringProperty(b'vehicleLevel', b'')
        self._addResourceProperty(b'smallBadgeIcon', R.invalid())
        return
