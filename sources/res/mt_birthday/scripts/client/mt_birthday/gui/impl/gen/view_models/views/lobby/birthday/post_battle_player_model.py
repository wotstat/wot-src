from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class PostBattlePlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(PostBattlePlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    @property
    def userInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getUserInfoType():
        return UserNameModel

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)
        return

    def getIsLoading(self):
        return self._getBool(3)

    def setIsLoading(self, value):
        self._setBool(3, value)
        return

    def getIsBanned(self):
        return self._getBool(4)

    def setIsBanned(self, value):
        self._setBool(4, value)
        return

    def getIsPlayerInBlacklist(self):
        return self._getBool(5)

    def setIsPlayerInBlacklist(self, value):
        self._setBool(5, value)
        return

    def getIsBot(self):
        return self._getBool(6)

    def setIsBot(self, value):
        self._setBool(6, value)
        return

    def getTotalDamage(self):
        return self._getNumber(7)

    def setTotalDamage(self, value):
        self._setNumber(7, value)
        return

    def getKills(self):
        return self._getNumber(8)

    def setKills(self, value):
        self._setNumber(8, value)
        return

    def getXp(self):
        return self._getNumber(9)

    def setXp(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(PostBattlePlayerModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'userInfo', UserNameModel())
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isLoading', False)
        self._addBoolProperty(b'isBanned', False)
        self._addBoolProperty(b'isPlayerInBlacklist', False)
        self._addBoolProperty(b'isBot', False)
        self._addNumberProperty(b'totalDamage', 0)
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'xp', 0)
        return
