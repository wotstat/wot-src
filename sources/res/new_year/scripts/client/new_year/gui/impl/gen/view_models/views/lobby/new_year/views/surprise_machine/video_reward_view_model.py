from frameworks.wulf import ViewModel

class VideoRewardViewModel(ViewModel):
    __slots__ = (b'closeRewardVehicle', b'showVehicle')

    def __init__(self, properties=5, commands=2):
        super(VideoRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(1)

    def setVehicleLvl(self, value):
        self._setNumber(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getIsElite(self):
        return self._getBool(3)

    def setIsElite(self, value):
        self._setBool(3, value)
        return

    def getIsMainViewVisible(self):
        return self._getBool(4)

    def setIsMainViewVisible(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(VideoRewardViewModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addStringProperty(b'vehicleType', b'')
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isMainViewVisible', True)
        self.closeRewardVehicle = self._addCommand(b'closeRewardVehicle')
        self.showVehicle = self._addCommand(b'showVehicle')
        return
