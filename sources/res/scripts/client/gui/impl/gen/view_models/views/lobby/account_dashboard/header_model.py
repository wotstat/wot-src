from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class AccountInfoStateEnum(Enum):
    RENAMEAVAILABLE = b'renameAvailable'
    RENAMEDISABLED = b'renameDisabled'
    RENAMEINPROGRESS = b'renameInProgress'
    EMAILPENDING = b'emailPending'
    COMPLETED = b'completed'


class HeaderModel(ViewModel):
    __slots__ = (b'onShowBadges', b'onAccountInfoButtonClick')

    def __init__(self, properties=11, commands=2):
        super(HeaderModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserName(self):
        return self._getString(0)

    def setUserName(self, value):
        self._setString(0, value)
        return

    def getBadgeID(self):
        return self._getString(1)

    def setBadgeID(self, value):
        self._setString(1, value)
        return

    def getSuffixBadgeID(self):
        return self._getString(2)

    def setSuffixBadgeID(self, value):
        self._setString(2, value)
        return

    def getIsInClan(self):
        return self._getBool(3)

    def setIsInClan(self, value):
        self._setBool(3, value)
        return

    def getClanAbbrev(self):
        return self._getString(4)

    def setClanAbbrev(self, value):
        self._setString(4, value)
        return

    def getRoleInClan(self):
        return self._getString(5)

    def setRoleInClan(self, value):
        self._setString(5, value)
        return

    def getClanDescription(self):
        return self._getString(6)

    def setClanDescription(self, value):
        self._setString(6, value)
        return

    def getClanIcon(self):
        return self._getString(7)

    def setClanIcon(self, value):
        self._setString(7, value)
        return

    def getIsTeamKiller(self):
        return self._getBool(8)

    def setIsTeamKiller(self, value):
        self._setBool(8, value)
        return

    def getAccountInfoState(self):
        return AccountInfoStateEnum(self._getString(9))

    def setAccountInfoState(self, value):
        self._setString(9, value.value)
        return

    def getEmailButtonLabel(self):
        return self._getResource(10)

    def setEmailButtonLabel(self, value):
        self._setResource(10, value)
        return

    def _initialize(self):
        super(HeaderModel, self)._initialize()
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'badgeID', b'')
        self._addStringProperty(b'suffixBadgeID', b'')
        self._addBoolProperty(b'isInClan', False)
        self._addStringProperty(b'clanAbbrev', b'')
        self._addStringProperty(b'roleInClan', b'')
        self._addStringProperty(b'clanDescription', b'')
        self._addStringProperty(b'clanIcon', b'')
        self._addBoolProperty(b'isTeamKiller', False)
        self._addStringProperty(b'accountInfoState')
        self._addResourceProperty(b'emailButtonLabel', R.invalid())
        self.onShowBadges = self._addCommand(b'onShowBadges')
        self.onAccountInfoButtonClick = self._addCommand(b'onAccountInfoButtonClick')
        return
