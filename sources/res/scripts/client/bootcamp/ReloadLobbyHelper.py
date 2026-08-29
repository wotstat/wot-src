from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from helpers import aop, dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IGameStateTracker

class _PointcutGameSessionControllerFix(aop.Pointcut):

    def __init__(self):
        super(_PointcutGameSessionControllerFix, self).__init__(b'gui.game_control.GameSessionController', b'GameSessionController', b'_stop', aspects=(
         _AspectGameSessionControllerFix,))
        return


class _AspectGameSessionControllerFix(aop.Aspect):

    def atCall(self, cd):
        return cd.changeArgs((
         0, b'doNotifyInStart', False))


class ReloadLobbyHelper(object):
    appLoader = dependency.descriptor(IAppLoader)
    gameState = dependency.descriptor(IGameStateTracker)

    def __init__(self):
        super(ReloadLobbyHelper, self).__init__()
        self.__isReloading = False
        return

    def cancel(self):
        if self.__isReloading:
            g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__onLobbyViewLoaded, EVENT_BUS_SCOPE.DEFAULT)
        self.__isReloading = False
        return

    def reload(self):
        self.__isReloading = True
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__onLobbyViewLoaded, EVENT_BUS_SCOPE.DEFAULT)
        from gui.prb_control.dispatcher import g_prbLoader
        pc = _PointcutGameSessionControllerFix()
        g_prbLoader.onAccountBecomeNonPlayer()
        self.gameState.onAvatarBecomePlayer()
        self.appLoader.switchAccountEntity()
        g_prbLoader.onAccountShowGUI({})
        pc.clear()
        return

    def __onLobbyViewLoaded(self, _):
        self.cancel()
        return
