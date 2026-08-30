from frameworks.wulf import ViewModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(PlayerModel, self).__init__(properties=properties, commands=commands)
        return

    def getSpaID(self):
        return self._getNumber(0)

    def setSpaID(self, value):
        self._setNumber(0, value)
        return

    def getUserName(self):
        return self._getString(1)

    def setUserName(self, value):
        self._setString(1, value)
        return

    def getClanTag(self):
        return self._getString(2)

    def setClanTag(self, value):
        self._setString(2, value)
        return

    def getClanTagColor(self):
        return self._getString(3)

    def setClanTagColor(self, value):
        self._setString(3, value)
        return

    def getBadgeID(self):
        return self._getString(4)

    def setBadgeID(self, value):
        self._setString(4, value)
        return

    def getSuffixBadgeID(self):
        return self._getString(5)

    def setSuffixBadgeID(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addNumberProperty(b'spaID', 0)
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'clanTag', b'')
        self._addStringProperty(b'clanTagColor', b'')
        self._addStringProperty(b'badgeID', b'')
        self._addStringProperty(b'suffixBadgeID', b'')
        return
