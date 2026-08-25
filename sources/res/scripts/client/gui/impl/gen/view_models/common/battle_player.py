from enum import Enum
from gui.impl.gen import R
from gui.impl.gen.view_models.common.commendationStateModel import CommendationStateModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class VehicleTypeEnum(Enum):
    ATSPG = b'atSpg'
    HEAVYTANK = b'heavyTank'
    LIGHTTANK = b'lightTank'
    MEDIUMTANK = b'mediumTank'
    SPG = b'spg'
    UNDEFINED = b'undefined'


class BattlePlayer(UserNameModel):
    __slots__ = ()

    def __init__(self, properties=37, commands=0):
        super(BattlePlayer, self).__init__(properties=properties, commands=commands)
        return

    @property
    def prestigeEmblemModel(self):
        return self._getViewModel(10)

    @staticmethod
    def getPrestigeEmblemModelType():
        return PrestigeEmblemModel

    @property
    def commendationStateModel(self):
        return self._getViewModel(11)

    @staticmethod
    def getCommendationStateModelType():
        return CommendationStateModel

    def getIsCurrentPlayer(self):
        return self._getBool(12)

    def setIsCurrentPlayer(self, value):
        self._setBool(12, value)
        return

    def getVehicleId(self):
        return self._getNumber(13)

    def setVehicleId(self, value):
        self._setNumber(13, value)
        return

    def getAvatarSessionID(self):
        return self._getString(14)

    def setAvatarSessionID(self, value):
        self._setString(14, value)
        return

    def getPlatoon(self):
        return self._getNumber(15)

    def setPlatoon(self, value):
        self._setNumber(15, value)
        return

    def getIsMyPlatoon(self):
        return self._getBool(16)

    def setIsMyPlatoon(self, value):
        self._setBool(16, value)
        return

    def getIsInviteSent(self):
        return self._getBool(17)

    def setIsInviteSent(self, value):
        self._setBool(17, value)
        return

    def getIsInviteReceived(self):
        return self._getBool(18)

    def setIsInviteReceived(self, value):
        self._setBool(18, value)
        return

    def getIsPlatoonInvitationDisabled(self):
        return self._getBool(19)

    def setIsPlatoonInvitationDisabled(self, value):
        self._setBool(19, value)
        return

    def getKills(self):
        return self._getNumber(20)

    def setKills(self, value):
        self._setNumber(20, value)
        return

    def getVehicleName(self):
        return self._getString(21)

    def setVehicleName(self, value):
        self._setString(21, value)
        return

    def getIsChatMuted(self):
        return self._getBool(22)

    def setIsChatMuted(self, value):
        self._setBool(22, value)
        return

    def getIsVoiceMuted(self):
        return self._getBool(23)

    def setIsVoiceMuted(self, value):
        self._setBool(23, value)
        return

    def getIsVoiceActive(self):
        return self._getBool(24)

    def setIsVoiceActive(self, value):
        self._setBool(24, value)
        return

    def getVehicleContourUrl(self):
        return self._getString(25)

    def setVehicleContourUrl(self, value):
        self._setString(25, value)
        return

    def getVehicleType(self):
        return VehicleTypeEnum(self._getString(26))

    def setVehicleType(self, value):
        self._setString(26, value.value)
        return

    def getVehicleLevel(self):
        return self._getNumber(27)

    def setVehicleLevel(self, value):
        self._setNumber(27, value)
        return

    def getIsKiller(self):
        return self._getBool(28)

    def setIsKiller(self, value):
        self._setBool(28, value)
        return

    def getIsReported(self):
        return self._getBool(29)

    def setIsReported(self, value):
        self._setBool(29, value)
        return

    def getIsLoaded(self):
        return self._getBool(30)

    def setIsLoaded(self, value):
        self._setBool(30, value)
        return

    def getAnonymizerTooltip(self):
        return self._getString(31)

    def setAnonymizerTooltip(self, value):
        self._setString(31, value)
        return

    def getLiveTagTooltipTitle(self):
        return self._getResource(32)

    def setLiveTagTooltipTitle(self, value):
        self._setResource(32, value)
        return

    def getLiveTagTooltipBody(self):
        return self._getResource(33)

    def setLiveTagTooltipBody(self, value):
        self._setResource(33, value)
        return

    def getLiveTagDamage(self):
        return self._getBool(34)

    def setLiveTagDamage(self, value):
        self._setBool(34, value)
        return

    def getLiveTagAssist(self):
        return self._getBool(35)

    def setLiveTagAssist(self, value):
        self._setBool(35, value)
        return

    def getLiveTagBlock(self):
        return self._getBool(36)

    def setLiveTagBlock(self, value):
        self._setBool(36, value)
        return

    def _initialize(self):
        super(BattlePlayer, self)._initialize()
        self._addViewModelProperty(b'prestigeEmblemModel', PrestigeEmblemModel())
        self._addViewModelProperty(b'commendationStateModel', CommendationStateModel())
        self._addBoolProperty(b'isCurrentPlayer', False)
        self._addNumberProperty(b'vehicleId', 0)
        self._addStringProperty(b'avatarSessionID', b'')
        self._addNumberProperty(b'platoon', 0)
        self._addBoolProperty(b'isMyPlatoon', False)
        self._addBoolProperty(b'isInviteSent', False)
        self._addBoolProperty(b'isInviteReceived', False)
        self._addBoolProperty(b'isPlatoonInvitationDisabled', False)
        self._addNumberProperty(b'kills', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addBoolProperty(b'isChatMuted', False)
        self._addBoolProperty(b'isVoiceMuted', False)
        self._addBoolProperty(b'isVoiceActive', False)
        self._addStringProperty(b'vehicleContourUrl', b'')
        self._addStringProperty(b'vehicleType', VehicleTypeEnum.UNDEFINED.value)
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addBoolProperty(b'isKiller', False)
        self._addBoolProperty(b'isReported', False)
        self._addBoolProperty(b'isLoaded', False)
        self._addStringProperty(b'anonymizerTooltip', b'')
        self._addResourceProperty(b'liveTagTooltipTitle', R.invalid())
        self._addResourceProperty(b'liveTagTooltipBody', R.invalid())
        self._addBoolProperty(b'liveTagDamage', False)
        self._addBoolProperty(b'liveTagAssist', False)
        self._addBoolProperty(b'liveTagBlock', False)
        return
