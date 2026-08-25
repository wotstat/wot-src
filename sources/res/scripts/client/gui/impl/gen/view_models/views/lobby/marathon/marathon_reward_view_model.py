from frameworks.wulf import ViewModel

class MarathonRewardViewModel(ViewModel):
    __slots__ = (b'onGoToVehicleBtnClick', b'onViewRewardsBtnClick', b'onCloseBtnClick', b'onVideoStarted', b'onVideoStopped')

    def __init__(self, properties=6, commands=5):
        super(MarathonRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsGoToVehicleBtnEnabled(self):
        return self._getBool(0)

    def setIsGoToVehicleBtnEnabled(self, value):
        self._setBool(0, value)
        return

    def getVideoSource(self):
        return self._getString(1)

    def setVideoSource(self, value):
        self._setString(1, value)
        return

    def getVehicleIsElite(self):
        return self._getBool(2)

    def setVehicleIsElite(self, value):
        self._setBool(2, value)
        return

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)
        return

    def getVehicleLvl(self):
        return self._getString(4)

    def setVehicleLvl(self, value):
        self._setString(4, value)
        return

    def getVehicleName(self):
        return self._getString(5)

    def setVehicleName(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(MarathonRewardViewModel, self)._initialize()
        self._addBoolProperty(b'isGoToVehicleBtnEnabled', True)
        self._addStringProperty(b'videoSource', b'')
        self._addBoolProperty(b'vehicleIsElite', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLvl', b'')
        self._addStringProperty(b'vehicleName', b'')
        self.onGoToVehicleBtnClick = self._addCommand(b'onGoToVehicleBtnClick')
        self.onViewRewardsBtnClick = self._addCommand(b'onViewRewardsBtnClick')
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        self.onVideoStopped = self._addCommand(b'onVideoStopped')
        return
