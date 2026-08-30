from frameworks.wulf import ViewModel
from gui.impl.gen import R

class YearLeaderboardViewModel(ViewModel):
    __slots__ = (b'onLeaderboardBtnClick',)

    def __init__(self, properties=6, commands=1):
        super(YearLeaderboardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPlayerName(self):
        return self._getString(0)

    def setPlayerName(self, value):
        self._setString(0, value)
        return

    def getPlayerClan(self):
        return self._getString(1)

    def setPlayerClan(self, value):
        self._setString(1, value)
        return

    def getPositionsTotal(self):
        return self._getNumber(2)

    def setPositionsTotal(self, value):
        self._setNumber(2, value)
        return

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)
        return

    def getRewardId(self):
        return self._getNumber(4)

    def setRewardId(self, value):
        self._setNumber(4, value)
        return

    def getBgImage(self):
        return self._getResource(5)

    def setBgImage(self, value):
        self._setResource(5, value)
        return

    def _initialize(self):
        super(YearLeaderboardViewModel, self)._initialize()
        self._addStringProperty(b'playerName', b'')
        self._addStringProperty(b'playerClan', b'')
        self._addNumberProperty(b'positionsTotal', 0)
        self._addNumberProperty(b'position', 0)
        self._addNumberProperty(b'rewardId', 0)
        self._addResourceProperty(b'bgImage', R.invalid())
        self.onLeaderboardBtnClick = self._addCommand(b'onLeaderboardBtnClick')
        return
