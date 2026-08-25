from __future__ import absolute_import
from adisp import adisp_process, adisp_async
from gui.game_control.links import URLMacros
from helpers import dependency
from skeletons.gui.game_control import IGameWindowController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache

class GameWindowController(IGameWindowController):
    eventsCache = dependency.descriptor(IEventsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.__urlMacros = URLMacros()
        self.__isLobbyInited = False
        super(GameWindowController, self).__init__()
        return

    def fini(self):
        self.__urlMacros.clear()
        self.__urlMacros = None
        self.hideWindow()
        super(GameWindowController, self).fini()
        return

    def onLobbyInited(self, event):
        self.__isLobbyInited = True
        self._addListeners()
        return

    def onAvatarBecomePlayer(self):
        self._removeListeners()
        if self.__isLobbyInited:
            self.hideWindow()
        self.__isLobbyInited = False
        super(GameWindowController, self).onAvatarBecomePlayer()
        return

    def onDisconnected(self):
        self.__isLobbyInited = False
        self._removeListeners()
        self.hideWindow()
        super(GameWindowController, self).onDisconnected()
        return

    def hideWindow(self):
        raise NotImplementedError
        return

    def showWindow(self, url=None, invokedFrom=None):
        self.hideWindow()
        self._showWindow(url, invokedFrom)
        return

    @adisp_async
    @adisp_process
    def getUrl(self, callback=lambda *args: None):
        url = yield self.__urlMacros.parse(self._getUrl())
        callback(url)
        return

    def _addListeners(self):
        self.eventsCache.onSyncCompleted += self._onSyncCompleted
        return

    def _removeListeners(self):
        self.eventsCache.onSyncCompleted -= self._onSyncCompleted
        return

    def _onSyncCompleted(self, *_):
        return

    @adisp_process
    def _showWindow(self, url, invokedFrom=None):
        if url is None:
            url = yield self.getUrl()
            if not url:
                return
        self._openWindow(url, invokedFrom)
        return

    def _openWindow(self, url, invokedFrom=None):
        raise NotImplementedError
        return
