from frameworks.wulf import ViewModel

class PlayerInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PlayerInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getPlayerName(self):
        return self._getString(0)

    def setPlayerName(self, value):
        self._setString(0, value)
        return

    def getPlayerClanTag(self):
        return self._getString(1)

    def setPlayerClanTag(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(PlayerInfoModel, self)._initialize()
        self._addStringProperty(b'playerName', b'')
        self._addStringProperty(b'playerClanTag', b'')
        return
