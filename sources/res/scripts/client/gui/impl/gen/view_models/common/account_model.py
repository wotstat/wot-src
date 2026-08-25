from frameworks.wulf import ViewModel

class AccountModel(ViewModel):
    __slots__ = ()
    IGR_TYPE_NONE = 0
    IGR_TYPE_BASE = 1
    IGR_TYPE_PREMIUM = 2

    def __init__(self, properties=10, commands=0):
        super(AccountModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserName(self):
        return self._getString(0)

    def setUserName(self, value):
        self._setString(0, value)
        return

    def getFakeUserName(self):
        return self._getString(1)

    def setFakeUserName(self, value):
        self._setString(1, value)
        return

    def getAnonymizer(self):
        return self._getBool(2)

    def setAnonymizer(self, value):
        self._setBool(2, value)
        return

    def getClanAbbrev(self):
        return self._getString(3)

    def setClanAbbrev(self, value):
        self._setString(3, value)
        return

    def getIgrType(self):
        return self._getNumber(4)

    def setIgrType(self, value):
        self._setNumber(4, value)
        return

    def getIsTeamKiller(self):
        return self._getBool(5)

    def setIsTeamKiller(self, value):
        self._setBool(5, value)
        return

    def getIsKilled(self):
        return self._getBool(6)

    def setIsKilled(self, value):
        self._setBool(6, value)
        return

    def getDatabaseID(self):
        return self._getNumber(7)

    def setDatabaseID(self, value):
        self._setNumber(7, value)
        return

    def getBadge(self):
        return self._getString(8)

    def setBadge(self, value):
        self._setString(8, value)
        return

    def getSuffixBadge(self):
        return self._getString(9)

    def setSuffixBadge(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(AccountModel, self)._initialize()
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'fakeUserName', b'')
        self._addBoolProperty(b'anonymizer', False)
        self._addStringProperty(b'clanAbbrev', b'')
        self._addNumberProperty(b'igrType', 0)
        self._addBoolProperty(b'isTeamKiller', False)
        self._addBoolProperty(b'isKilled', False)
        self._addNumberProperty(b'databaseID', 0)
        self._addStringProperty(b'badge', b'')
        self._addStringProperty(b'suffixBadge', b'')
        return
