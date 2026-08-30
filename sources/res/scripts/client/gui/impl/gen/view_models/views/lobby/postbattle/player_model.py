from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from gui.impl.gen.view_models.views.lobby.postbattle.player_details_model import PlayerDetailsModel

class PlayerModel(ViewModel):
    __slots__ = ()
    PLAYER_DAMAGE_DEALT = b'damageDealt'
    PLAYER_KILLS = b'kills'
    PLAYER_EARNED_XP = b'earnedXp'
    PLAYER_IDX = b'idx'
    PLAYER_SQUAD_IDX = b'squadIdx'

    def __init__(self, properties=16, commands=0):
        super(PlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def details(self):
        return self._getViewModel(0)

    @staticmethod
    def getDetailsType():
        return PlayerDetailsModel

    @property
    def user(self):
        return self._getViewModel(1)

    @staticmethod
    def getUserType():
        return UserNameModel

    def getEarnedXp(self):
        return self._getNumber(2)

    def setEarnedXp(self, value):
        self._setNumber(2, value)
        return

    def getVehicleName(self):
        return self._getString(3)

    def setVehicleName(self, value):
        self._setString(3, value)
        return

    def getLocalizedVehicleName(self):
        return self._getString(4)

    def setLocalizedVehicleName(self, value):
        self._setString(4, value)
        return

    def getKills(self):
        return self._getNumber(5)

    def setKills(self, value):
        self._setNumber(5, value)
        return

    def getDamageDealt(self):
        return self._getNumber(6)

    def setDamageDealt(self, value):
        self._setNumber(6, value)
        return

    def getVehicleType(self):
        return self._getString(7)

    def setVehicleType(self, value):
        self._setString(7, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(8)

    def setVehicleLevel(self, value):
        self._setNumber(8, value)
        return

    def getSquadIdx(self):
        return self._getNumber(9)

    def setSquadIdx(self, value):
        self._setNumber(9, value)
        return

    def getIsPersonal(self):
        return self._getBool(10)

    def setIsPersonal(self, value):
        self._setBool(10, value)
        return

    def getTeam(self):
        return self._getNumber(11)

    def setTeam(self, value):
        self._setNumber(11, value)
        return

    def getIsSameSquad(self):
        return self._getBool(12)

    def setIsSameSquad(self, value):
        self._setBool(12, value)
        return

    def getIdx(self):
        return self._getNumber(13)

    def setIdx(self, value):
        self._setNumber(13, value)
        return

    def getVehicleCD(self):
        return self._getNumber(14)

    def setVehicleCD(self, value):
        self._setNumber(14, value)
        return

    def getDbID(self):
        return self._getNumber(15)

    def setDbID(self, value):
        self._setNumber(15, value)
        return

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'details', PlayerDetailsModel())
        self._addViewModelProperty(b'user', UserNameModel())
        self._addNumberProperty(b'earnedXp', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'localizedVehicleName', b'')
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'damageDealt', 0)
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addNumberProperty(b'squadIdx', 0)
        self._addBoolProperty(b'isPersonal', False)
        self._addNumberProperty(b'team', 0)
        self._addBoolProperty(b'isSameSquad', False)
        self._addNumberProperty(b'idx', 0)
        self._addNumberProperty(b'vehicleCD', 0)
        self._addNumberProperty(b'dbID', 0)
        return
