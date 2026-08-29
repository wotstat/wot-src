from frameworks.wulf import ViewModel

class BattleSessionModel(ViewModel):
    __slots__ = (b'onTournamentsClicked', b'onGlobalMapClicked', b'onClanClicked', b'onCloseClicked')

    def __init__(self, properties=4, commands=4):
        super(BattleSessionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsInClan(self):
        return self._getBool(0)

    def setIsInClan(self, value):
        self._setBool(0, value)
        return

    def getClanName(self):
        return self._getString(1)

    def setClanName(self, value):
        self._setString(1, value)
        return

    def getClanIcon(self):
        return self._getString(2)

    def setClanIcon(self, value):
        self._setString(2, value)
        return

    def getIsTournamentLinkIGB(self):
        return self._getBool(3)

    def setIsTournamentLinkIGB(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(BattleSessionModel, self)._initialize()
        self._addBoolProperty(b'isInClan', False)
        self._addStringProperty(b'clanName', b'')
        self._addStringProperty(b'clanIcon', b'')
        self._addBoolProperty(b'isTournamentLinkIGB', False)
        self.onTournamentsClicked = self._addCommand(b'onTournamentsClicked')
        self.onGlobalMapClicked = self._addCommand(b'onGlobalMapClicked')
        self.onClanClicked = self._addCommand(b'onClanClicked')
        self.onCloseClicked = self._addCommand(b'onCloseClicked')
        return
