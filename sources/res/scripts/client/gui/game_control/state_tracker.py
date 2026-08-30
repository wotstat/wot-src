from __future__ import absolute_import, print_function
import logging, operator
from gui.shared import g_eventBus, events
from shared_utils import safeForEach
from skeletons.gui.game_control import IGameStateTracker, IGameController
_logger = logging.getLogger(__name__)

class GameStateTracker(IGameStateTracker):

    def __init__(self):
        super(GameStateTracker, self).__init__()
        self._controllers = []
        return

    def init(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)
        return

    def fini(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)
        del self._controllers[:]
        return

    def onAccountShowGUI(self, ctx):
        self.onLobbyStarted(ctx)
        return

    def onConnected(self):
        self._invoke(b'onConnected')
        return

    def onDisconnected(self):
        self._invoke(b'onDisconnected')
        return

    def onAvatarBecomePlayer(self):
        self._invoke(b'onAvatarBecomePlayer')
        return

    def onAccountBecomePlayer(self):
        self._invoke(b'onAccountBecomePlayer')
        return

    def onAccountBecomeNonPlayer(self):
        self._invoke(b'onAccountBecomeNonPlayer')
        return

    def onLobbyStarted(self, ctx):
        self._invoke(b'onLobbyStarted', ctx)
        return

    def onLobbyInited(self, event):
        self._invoke(b'onLobbyInited', event)
        return

    def onServerReplayEntering(self):
        self._invoke(b'onServerReplayEntering')
        return

    def onServerReplayExiting(self):
        self._invoke(b'onServerReplayExiting')
        return

    def addController(self, controller):
        if not isinstance(controller, IGameController):
            _logger.error(b'Controller should implements IGameController')
        self._controllers.append(controller)
        return

    def removeController(self, controller):
        if not isinstance(controller, IGameController):
            _logger.error(b'Controller should implements IGameController')
        self._controllers.remove(controller)
        return

    def _invoke(self, method, *args):
        safeForEach(operator.methodcaller(method, *args), self._controllers)
        return
