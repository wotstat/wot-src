from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.menu_item_model import MenuItemModel

class MainMenuModel(ViewModel):
    __slots__ = (b'onNavigate',)
    MODE_SELECTOR = b'modeSelector'
    SHOP = b'shop'
    STORAGE = b'storage'
    MISSIONS = b'missions'
    PERSONAL_MISSIONS = b'personalMissions'
    ACHIEVEMENTS = b'achievements'
    TECHTREE = b'techtree'
    TOURNAMENT = b'tournament'
    BARRACKS = b'barracks'
    CLANS = b'clans'
    REPLAYS = b'replays'

    def __init__(self, properties=5, commands=1):
        super(MainMenuModel, self).__init__(properties=properties, commands=commands)
        return

    def getMenuItems(self):
        return self._getArray(0)

    def setMenuItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMenuItemsType():
        return MenuItemModel

    def getModeName(self):
        return self._getString(1)

    def setModeName(self, value):
        self._setString(1, value)
        return

    def getModeId(self):
        return self._getString(2)

    def setModeId(self, value):
        self._setString(2, value)
        return

    def getHasTechTreeEvents(self):
        return self._getBool(3)

    def setHasTechTreeEvents(self, value):
        self._setBool(3, value)
        return

    def getClanEmblem(self):
        return self._getString(4)

    def setClanEmblem(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(MainMenuModel, self)._initialize()
        self._addArrayProperty(b'menuItems', Array())
        self._addStringProperty(b'modeName', b'')
        self._addStringProperty(b'modeId', b'')
        self._addBoolProperty(b'hasTechTreeEvents', False)
        self._addStringProperty(b'clanEmblem', b'')
        self.onNavigate = self._addCommand(b'onNavigate')
        return
