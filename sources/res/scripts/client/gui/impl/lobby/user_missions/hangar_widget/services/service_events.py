from __future__ import absolute_import
from PlayerEvents import g_playerEvents
from gui.shared import g_eventBus, events

class ServiceEvents(object):

    def stopListening(self):
        raise NotImplementedError
        return

    def startListening(self):
        raise NotImplementedError
        return

    def startServiceEvents(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__onLobbyInited)
        g_playerEvents.onAccountBecomeNonPlayer += self.__onAccountBecomeNonPlayer
        return

    def stopServiceEvents(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__onLobbyInited)
        g_playerEvents.onAccountBecomeNonPlayer -= self.__onAccountBecomeNonPlayer
        return

    def __onLobbyInited(self, *_):
        self.startListening()
        return

    def __onAccountBecomeNonPlayer(self):
        self.stopListening()
        return
