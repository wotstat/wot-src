from frameworks.wulf import ViewModel

class BanShowTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BanShowTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getLongName(self):
        return self._getString(0)

    def setLongName(self, value):
        self._setString(0, value)
        return

    def getVehicleCD(self):
        return self._getNumber(1)

    def setVehicleCD(self, value):
        self._setNumber(1, value)
        return

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)
        return

    def getRoleKey(self):
        return self._getString(3)

    def setRoleKey(self, value):
        self._setString(3, value)
        return

    def getIsPremium(self):
        return self._getBool(4)

    def setIsPremium(self, value):
        self._setBool(4, value)
        return

    def getConfirmedChoice(self):
        return self._getBool(5)

    def setConfirmedChoice(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(BanShowTooltipModel, self)._initialize()
        self._addStringProperty(b'longName', b'')
        self._addNumberProperty(b'vehicleCD', 0)
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'roleKey', b'')
        self._addBoolProperty(b'isPremium', False)
        self._addBoolProperty(b'confirmedChoice', False)
        return
