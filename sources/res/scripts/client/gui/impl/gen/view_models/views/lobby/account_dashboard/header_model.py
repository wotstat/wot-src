from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.page.header.user_info_model import UserInfoModel

class HeaderModel(UserInfoModel):
    __slots__ = (b'onShowBadges', b'onAccountInfoButtonClick')

    def __init__(self, properties=18, commands=2):
        super(HeaderModel, self).__init__(properties=properties, commands=commands)
        return

    def getBadgeID(self):
        return self._getString(11)

    def setBadgeID(self, value):
        self._setString(11, value)
        return

    def getSuffixBadgeID(self):
        return self._getString(12)

    def setSuffixBadgeID(self, value):
        self._setString(12, value)
        return

    def getClanDescription(self):
        return self._getString(13)

    def setClanDescription(self, value):
        self._setString(13, value)
        return

    def getClanIcon(self):
        return self._getString(14)

    def setClanIcon(self, value):
        self._setString(14, value)
        return

    def getIsTeamKiller(self):
        return self._getBool(15)

    def setIsTeamKiller(self, value):
        self._setBool(15, value)
        return

    def getIsEmailPending(self):
        return self._getBool(16)

    def setIsEmailPending(self, value):
        self._setBool(16, value)
        return

    def getEmailButtonLabel(self):
        return self._getResource(17)

    def setEmailButtonLabel(self, value):
        self._setResource(17, value)
        return

    def _initialize(self):
        super(HeaderModel, self)._initialize()
        self._addStringProperty(b'badgeID', b'')
        self._addStringProperty(b'suffixBadgeID', b'')
        self._addStringProperty(b'clanDescription', b'')
        self._addStringProperty(b'clanIcon', b'')
        self._addBoolProperty(b'isTeamKiller', False)
        self._addBoolProperty(b'isEmailPending', False)
        self._addResourceProperty(b'emailButtonLabel', R.invalid())
        self.onShowBadges = self._addCommand(b'onShowBadges')
        self.onAccountInfoButtonClick = self._addCommand(b'onAccountInfoButtonClick')
        return
