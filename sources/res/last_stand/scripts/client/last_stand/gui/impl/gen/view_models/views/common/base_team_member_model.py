from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from last_stand.gui.impl.gen.view_models.views.common.team_member_stats_model import TeamMemberStatsModel
from last_stand.gui.impl.gen.view_models.views.common.vehicle_model import VehicleModel

class TeamMemberBanType(Enum):
    NOTBANNED = b'notBanned'
    WARNED = b'warned'
    BANNED = b'banned'


class BaseTeamMemberModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(BaseTeamMemberModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserNameModel

    @property
    def vehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    @property
    def stats(self):
        return self._getViewModel(2)

    @staticmethod
    def getStatsType():
        return TeamMemberStatsModel

    def getId(self):
        return self._getNumber(3)

    def setId(self, value):
        self._setNumber(3, value)
        return

    def getPlayerId(self):
        return self._getNumber(4)

    def setPlayerId(self, value):
        self._setNumber(4, value)
        return

    def getIsOwnSquad(self):
        return self._getBool(5)

    def setIsOwnSquad(self, value):
        self._setBool(5, value)
        return

    def getIsAlive(self):
        return self._getBool(6)

    def setIsAlive(self, value):
        self._setBool(6, value)
        return

    def getIsReady(self):
        return self._getBool(7)

    def setIsReady(self, value):
        self._setBool(7, value)
        return

    def getIsCurrentPlayer(self):
        return self._getBool(8)

    def setIsCurrentPlayer(self, value):
        self._setBool(8, value)
        return

    def getSquadNum(self):
        return self._getNumber(9)

    def setSquadNum(self, value):
        self._setNumber(9, value)
        return

    def getBanType(self):
        return TeamMemberBanType(self._getString(10))

    def setBanType(self, value):
        self._setString(10, value.value)
        return

    def _initialize(self):
        super(BaseTeamMemberModel, self)._initialize()
        self._addViewModelProperty(b'user', UserNameModel())
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addViewModelProperty(b'stats', TeamMemberStatsModel())
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'playerId', 0)
        self._addBoolProperty(b'isOwnSquad', False)
        self._addBoolProperty(b'isAlive', True)
        self._addBoolProperty(b'isReady', True)
        self._addBoolProperty(b'isCurrentPlayer', False)
        self._addNumberProperty(b'squadNum', 0)
        self._addStringProperty(b'banType')
        return
