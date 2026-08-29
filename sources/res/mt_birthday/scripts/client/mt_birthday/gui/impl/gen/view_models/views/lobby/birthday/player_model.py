from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.common.player_online_status_model import PlayerOnlineStatusModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(PlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def playerOnlineStatus(self):
        return self._getViewModel(0)

    @staticmethod
    def getPlayerOnlineStatusType():
        return PlayerOnlineStatusModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getClanAbbrev(self):
        return self._getString(2)

    def setClanAbbrev(self, value):
        self._setString(2, value)
        return

    def getSpaID(self):
        return self._getNumber(3)

    def setSpaID(self, value):
        self._setNumber(3, value)
        return

    def getLocked(self):
        return self._getBool(4)

    def setLocked(self, value):
        self._setBool(4, value)
        return

    def getIsNameLoading(self):
        return self._getBool(5)

    def setIsNameLoading(self, value):
        self._setBool(5, value)
        return

    def getIsWaitResponse(self):
        return self._getBool(6)

    def setIsWaitResponse(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'playerOnlineStatus', PlayerOnlineStatusModel())
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'clanAbbrev', b'')
        self._addNumberProperty(b'spaID', 0)
        self._addBoolProperty(b'locked', False)
        self._addBoolProperty(b'isNameLoading', True)
        self._addBoolProperty(b'isWaitResponse', False)
        return
