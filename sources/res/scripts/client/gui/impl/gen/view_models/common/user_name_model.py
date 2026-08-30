from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.badge_model import BadgeModel

class UserNameModel(ViewModel):
    __slots__ = ()
    IGR_TYPE_NONE = 0
    IGR_TYPE_BASE = 1
    IGR_TYPE_PREMIUM = 2

    def __init__(self, properties=10, commands=0):
        super(UserNameModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def badge(self):
        return self._getViewModel(0)

    @staticmethod
    def getBadgeType():
        return BadgeModel

    @property
    def suffixBadge(self):
        return self._getViewModel(1)

    @staticmethod
    def getSuffixBadgeType():
        return BadgeModel

    def getUserName(self):
        return self._getString(2)

    def setUserName(self, value):
        self._setString(2, value)
        return

    def getHiddenUserName(self):
        return self._getString(3)

    def setHiddenUserName(self, value):
        self._setString(3, value)
        return

    def getClanAbbrev(self):
        return self._getString(4)

    def setClanAbbrev(self, value):
        self._setString(4, value)
        return

    def getIsFakeNameVisible(self):
        return self._getBool(5)

    def setIsFakeNameVisible(self, value):
        self._setBool(5, value)
        return

    def getIgrType(self):
        return self._getNumber(6)

    def setIgrType(self, value):
        self._setNumber(6, value)
        return

    def getIsTeamKiller(self):
        return self._getBool(7)

    def setIsTeamKiller(self, value):
        self._setBool(7, value)
        return

    def getIsKilled(self):
        return self._getBool(8)

    def setIsKilled(self, value):
        self._setBool(8, value)
        return

    def getDatabaseID(self):
        return self._getNumber(9)

    def setDatabaseID(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(UserNameModel, self)._initialize()
        self._addViewModelProperty(b'badge', BadgeModel())
        self._addViewModelProperty(b'suffixBadge', BadgeModel())
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'hiddenUserName', b'')
        self._addStringProperty(b'clanAbbrev', b'')
        self._addBoolProperty(b'isFakeNameVisible', True)
        self._addNumberProperty(b'igrType', 0)
        self._addBoolProperty(b'isTeamKiller', False)
        self._addBoolProperty(b'isKilled', False)
        self._addNumberProperty(b'databaseID', 0)
        return
