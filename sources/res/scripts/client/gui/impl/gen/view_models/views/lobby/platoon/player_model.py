from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.platoon.common_player_data_model import CommonPlayerDataModel
from gui.impl.gen.view_models.views.lobby.platoon.sound_model import SoundModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
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

    @property
    def prestigeEmblem(self):
        return self._getViewModel(3)

    @staticmethod
    def getPrestigeEmblemType():
        return PrestigeEmblemModel

    def getIsCurrentUser(self):
        return self._getBool(4)

    def setIsCurrentUser(self, value):
        self._setBool(4, value)
        return

    def getIsCommander(self):
        return self._getBool(5)

    def setIsCommander(self, value):
        self._setBool(5, value)
        return

    def getIsReady(self):
        return self._getBool(6)

    def setIsReady(self, value):
        self._setBool(6, value)
        return

    def getIsPrem(self):
        return self._getBool(7)

    def setIsPrem(self, value):
        self._setBool(7, value)
        return

    def getAccID(self):
        return self._getString(8)

    def setAccID(self, value):
        self._setString(8, value)
        return

    def getIsIgnored(self):
        return self._getBool(9)

    def setIsIgnored(self, value):
        self._setBool(9, value)
        return

    def getIsPrestigeAvailable(self):
        return self._getBool(10)

    def setIsPrestigeAvailable(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'commonData', CommonPlayerDataModel())
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addViewModelProperty(b'voice', SoundModel())
        self._addViewModelProperty(b'prestigeEmblem', PrestigeEmblemModel())
        self._addBoolProperty(b'isCurrentUser', False)
        self._addBoolProperty(b'isCommander', False)
        self._addBoolProperty(b'isReady', False)
        self._addBoolProperty(b'isPrem', False)
        self._addStringProperty(b'accID', b'')
        self._addBoolProperty(b'isIgnored', False)
        self._addBoolProperty(b'isPrestigeAvailable', False)
        return
