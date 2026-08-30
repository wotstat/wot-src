from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.menu_item_model import MenuItemModel

class BattleSessionModel(ViewModel):
    __slots__ = (b'onTournamentsClicked', b'onGlobalMapClicked', b'onClanClicked', b'onCloseClicked', b'onNavigate')

    def __init__(self, properties=7, commands=5):
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

    def getMenuItems(self):
        return self._getArray(4)

    def setMenuItems(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getMenuItemsType():
        return MenuItemModel

    def getModeName(self):
        return self._getString(5)

    def setModeName(self, value):
        self._setString(5, value)
        return

    def getModeId(self):
        return self._getString(6)

    def setModeId(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(BattleSessionModel, self)._initialize()
        self._addBoolProperty(b'isInClan', False)
        self._addStringProperty(b'clanName', b'')
        self._addStringProperty(b'clanIcon', b'')
        self._addBoolProperty(b'isTournamentLinkIGB', False)
        self._addArrayProperty(b'menuItems', Array())
        self._addStringProperty(b'modeName', b'')
        self._addStringProperty(b'modeId', b'')
        self.onTournamentsClicked = self._addCommand(b'onTournamentsClicked')
        self.onGlobalMapClicked = self._addCommand(b'onGlobalMapClicked')
        self.onClanClicked = self._addCommand(b'onClanClicked')
        self.onCloseClicked = self._addCommand(b'onCloseClicked')
        self.onNavigate = self._addCommand(b'onNavigate')
        return
