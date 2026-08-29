from frameworks.wulf import ViewModel

class CongratsViewModel(ViewModel):
    __slots__ = ()
    SHINE_ORANGE_ALIAS = b'ShineAnimUI'
    SHINE_BLUE_ALIAS = b'BlueShineAnimUI'
    ADVANCED_SHINE_ORANGE = b'advancedShine'
    ADVANCED_SHINE_BLUE = b'advancedShineBlue'

    def __init__(self, properties=10, commands=0):
        super(CongratsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleIsElite(self):
        return self._getBool(0)

    def setVehicleIsElite(self, value):
        self._setBool(0, value)
        return

    def getShowCongrats(self):
        return self._getBool(1)

    def setShowCongrats(self, value):
        self._setBool(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getVehicleLvl(self):
        return self._getString(3)

    def setVehicleLvl(self, value):
        self._setString(3, value)
        return

    def getVehicleName(self):
        return self._getString(4)

    def setVehicleName(self, value):
        self._setString(4, value)
        return

    def getVehicleImage(self):
        return self._getString(5)

    def setVehicleImage(self, value):
        self._setString(5, value)
        return

    def getCongratsType(self):
        return self._getString(6)

    def setCongratsType(self, value):
        self._setString(6, value)
        return

    def getCongratsSourceId(self):
        return self._getString(7)

    def setCongratsSourceId(self, value):
        self._setString(7, value)
        return

    def getShineSwfAlias(self):
        return self._getString(8)

    def setShineSwfAlias(self, value):
        self._setString(8, value)
        return

    def getAdvancedShineName(self):
        return self._getString(9)

    def setAdvancedShineName(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(CongratsViewModel, self)._initialize()
        self._addBoolProperty(b'vehicleIsElite', False)
        self._addBoolProperty(b'showCongrats', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLvl', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleImage', b'')
        self._addStringProperty(b'congratsType', b'')
        self._addStringProperty(b'congratsSourceId', b'')
        self._addStringProperty(b'shineSwfAlias', b'ShineAnimUI')
        self._addStringProperty(b'advancedShineName', b'advancedShine')
        return
