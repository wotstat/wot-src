from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.common.player_online_status_model import PlayerOnlineStatusModel

class UserItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(UserItem, self).__init__(properties=properties, commands=commands)
        return

    @property
    def playerOnlineStatus(self):
        return self._getViewModel(0)

    @staticmethod
    def getPlayerOnlineStatusType():
        return PlayerOnlineStatusModel

    def getUserID(self):
        return self._getNumber(1)

    def setUserID(self, value):
        self._setNumber(1, value)
        return

    def getUserNickName(self):
        return self._getString(2)

    def setUserNickName(self, value):
        self._setString(2, value)
        return

    def getClanTag(self):
        return self._getString(3)

    def setClanTag(self, value):
        self._setString(3, value)
        return

    def getIsWaitResponse(self):
        return self._getBool(4)

    def setIsWaitResponse(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(UserItem, self)._initialize()
        self._addViewModelProperty(b'playerOnlineStatus', PlayerOnlineStatusModel())
        self._addNumberProperty(b'userID', 0)
        self._addStringProperty(b'userNickName', b'')
        self._addStringProperty(b'clanTag', b'')
        self._addBoolProperty(b'isWaitResponse', False)
        return
