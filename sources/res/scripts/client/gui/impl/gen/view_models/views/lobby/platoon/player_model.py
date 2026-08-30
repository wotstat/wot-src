from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.platoon.common_player_data_model import CommonPlayerDataModel
from gui.impl.gen.view_models.views.lobby.platoon.sound_model import SoundModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(PlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def commonData(self):
        return self._getViewModel(0)

    @staticmethod
    def getCommonDataType():
        return CommonPlayerDataModel

    @property
    def vehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    @property
    def voice(self):
        return self._getViewModel(2)

    @staticmethod
    def getVoiceType():
        return SoundModel

    def getIsCurrentUser(self):
        return self._getBool(3)

    def setIsCurrentUser(self, value):
        self._setBool(3, value)
        return

    def getIsCommander(self):
        return self._getBool(4)

    def setIsCommander(self, value):
        self._setBool(4, value)
        return

    def getIsReady(self):
        return self._getBool(5)

    def setIsReady(self, value):
        self._setBool(5, value)
        return

    def getIsPrem(self):
        return self._getBool(6)

    def setIsPrem(self, value):
        self._setBool(6, value)
        return

    def getAccID(self):
        return self._getString(7)

    def setAccID(self, value):
        self._setString(7, value)
        return

    def getIsIgnored(self):
        return self._getBool(8)

    def setIsIgnored(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'commonData', CommonPlayerDataModel())
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addViewModelProperty(b'voice', SoundModel())
        self._addBoolProperty(b'isCurrentUser', False)
        self._addBoolProperty(b'isCommander', False)
        self._addBoolProperty(b'isReady', False)
        self._addBoolProperty(b'isPrem', False)
        self._addStringProperty(b'accID', b'')
        self._addBoolProperty(b'isIgnored', False)
        return
