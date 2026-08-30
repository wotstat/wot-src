import BigWorld
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.shared.utils import getPlayerDatabaseID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IScreenCastController

class ScreenCastController(IScreenCastController, IArenaVehiclesController):
    __slots__ = (b'_isSet', b'_isBattleCtrlInit', b'_dbID')
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(ScreenCastController, self).__init__()
        self._isSet = False
        self._isBattleCtrlInit = False
        self._dbID = 0
        return

    def fini(self):
        if self._isBattleCtrlInit:
            self.sessionProvider.removeArenaCtrl(self)
        return

    def onAvatarBecomePlayer(self):
        if not self._isBattleCtrlInit:
            self.sessionProvider.addArenaCtrl(self)
            self._isBattleCtrlInit = True
            self.__checkDbID()
        return

    def onAccountBecomePlayer(self):
        if self._isBattleCtrlInit:
            self.sessionProvider.removeArenaCtrl(self)
            self._isBattleCtrlInit = False
        return

    def invalidateArenaInfo(self):
        self.__checkDbID()
        return

    def invalidateVehiclesInfo(self, _):
        self.__checkDbID()
        return

    def onLobbyInited(self, event):
        self.__checkDbID()
        return

    def onDisconnected(self):
        self._dbID = 0
        self._isSet = False
        BigWorld.Screener.setUserId(0)
        return

    def __checkDbID(self):
        if self._dbID == 0:
            self._dbID = getPlayerDatabaseID()
            self.__update()
        return

    def __update(self):
        if self._dbID != 0 and not self._isSet:
            BigWorld.Screener.setUserId(self._dbID)
            self._isSet = True
        return
