from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ArmoryYardVideoRewardViewModel(VehicleInfoModel):
    __slots__ = (b'onClose', b'onError', b'onShowVehicle', b'onVideoStarted')

    def __init__(self, properties=12, commands=4):
        super(ArmoryYardVideoRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWindowAccessible(self):
        return self._getBool(10)

    def setIsWindowAccessible(self, value):
        self._setBool(10, value)
        return

    def getVideoName(self):
        return self._getString(11)

    def setVideoName(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(ArmoryYardVideoRewardViewModel, self)._initialize()
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addStringProperty(b'videoName', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onError = self._addCommand(b'onError')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        return
