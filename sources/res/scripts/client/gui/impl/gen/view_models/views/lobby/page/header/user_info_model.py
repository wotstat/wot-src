from enum import IntEnum
from frameworks.wulf import ViewModel

class SteamEmailStatusEnum(IntEnum):
    UNDEFINED = 0
    ADD_NEEDED = 1
    ADDED = 2
    CONFIRMATION_SENT = 3
    CONFIRMED = 4
    PROCESSING = 5


class UserInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(UserInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserName(self):
        return self._getString(0)

    def setUserName(self, value):
        self._setString(0, value)
        return

    def getBadgeID(self):
        return self._getNumber(1)

    def setBadgeID(self, value):
        self._setNumber(1, value)
        return

    def getIsInClan(self):
        return self._getBool(2)

    def setIsInClan(self, value):
        self._setBool(2, value)
        return

    def getClanAbbrev(self):
        return self._getString(3)

    def setClanAbbrev(self, value):
        self._setString(3, value)
        return

    def getSuffixBadgeID(self):
        return self._getNumber(4)

    def setSuffixBadgeID(self, value):
        self._setNumber(4, value)
        return

    def getRoleInClan(self):
        return self._getString(5)

    def setRoleInClan(self, value):
        self._setString(5, value)
        return

    def getEmail(self):
        return self._getString(6)

    def setEmail(self, value):
        self._setString(6, value)
        return

    def getAnonymized(self):
        return self._getBool(7)

    def setAnonymized(self, value):
        self._setBool(7, value)
        return

    def getSteamEmailStatus(self):
        return SteamEmailStatusEnum(self._getNumber(8))

    def setSteamEmailStatus(self, value):
        self._setNumber(8, value.value)
        return

    def getHasSteamAccount(self):
        return self._getBool(9)

    def setHasSteamAccount(self, value):
        self._setBool(9, value)
        return

    def getTeamKiller(self):
        return self._getBool(10)

    def setTeamKiller(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(UserInfoModel, self)._initialize()
        self._addStringProperty(b'userName', b'')
        self._addNumberProperty(b'badgeID', 0)
        self._addBoolProperty(b'isInClan', False)
        self._addStringProperty(b'clanAbbrev', b'')
        self._addNumberProperty(b'suffixBadgeID', 0)
        self._addStringProperty(b'roleInClan', b'')
        self._addStringProperty(b'email', b'')
        self._addBoolProperty(b'anonymized', False)
        self._addNumberProperty(b'steamEmailStatus')
        self._addBoolProperty(b'hasSteamAccount', False)
        self._addBoolProperty(b'teamKiller', False)
        return
