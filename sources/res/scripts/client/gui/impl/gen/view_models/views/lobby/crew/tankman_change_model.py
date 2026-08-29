from gui.impl.gen import R
from frameworks.wulf import ViewModel

class TankmanChangeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(TankmanChangeModel, self).__init__(properties=properties, commands=commands)
        return

    def getNationName(self):
        return self._getString(0)

    def setNationName(self, value):
        self._setString(0, value)
        return

    def getNationID(self):
        return self._getString(1)

    def setNationID(self, value):
        self._setString(1, value)
        return

    def getNameID(self):
        return self._getString(2)

    def setNameID(self, value):
        self._setString(2, value)
        return

    def getNameText(self):
        return self._getString(3)

    def setNameText(self, value):
        self._setString(3, value)
        return

    def getSurnameID(self):
        return self._getString(4)

    def setSurnameID(self, value):
        self._setString(4, value)
        return

    def getSurnameText(self):
        return self._getString(5)

    def setSurnameText(self, value):
        self._setString(5, value)
        return

    def getIcon(self):
        return self._getResource(6)

    def setIcon(self, value):
        self._setResource(6, value)
        return

    def getIsFemale(self):
        return self._getBool(7)

    def setIsFemale(self, value):
        self._setBool(7, value)
        return

    def getVehType(self):
        return self._getString(8)

    def setVehType(self, value):
        self._setString(8, value)
        return

    def getVehicleID(self):
        return self._getString(9)

    def setVehicleID(self, value):
        self._setString(9, value)
        return

    def getVehicleName(self):
        return self._getString(10)

    def setVehicleName(self, value):
        self._setString(10, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(11)

    def setVehicleLevel(self, value):
        self._setNumber(11, value)
        return

    def getSpecialty(self):
        return self._getString(12)

    def setSpecialty(self, value):
        self._setString(12, value)
        return

    def getVehicleIcon(self):
        return self._getResource(13)

    def setVehicleIcon(self, value):
        self._setResource(13, value)
        return

    def getIsEliteVehicle(self):
        return self._getBool(14)

    def setIsEliteVehicle(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(TankmanChangeModel, self)._initialize()
        self._addStringProperty(b'nationName', b'')
        self._addStringProperty(b'nationID', b'')
        self._addStringProperty(b'nameID', b'')
        self._addStringProperty(b'nameText', b'')
        self._addStringProperty(b'surnameID', b'')
        self._addStringProperty(b'surnameText', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isFemale', False)
        self._addStringProperty(b'vehType', b'')
        self._addStringProperty(b'vehicleID', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addStringProperty(b'specialty', b'')
        self._addResourceProperty(b'vehicleIcon', R.invalid())
        self._addBoolProperty(b'isEliteVehicle', False)
        return
