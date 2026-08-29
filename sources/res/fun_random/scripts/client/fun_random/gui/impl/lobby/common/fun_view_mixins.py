from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import HeaderMenuVisibilityState
from gui.shared import events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE

class LobbyHeaderVisibility(object):
    __slots__ = ()

    @classmethod
    def suspendLobbyHeader(cls, state=HeaderMenuVisibilityState.NOTHING):
        cls._toggleLobbyHeaderVisibility(state)
        return

    @classmethod
    def resumeLobbyHeader(cls, state=HeaderMenuVisibilityState.ALL):
        cls._toggleLobbyHeaderVisibility(state)
        return

    @classmethod
    def _toggleLobbyHeaderVisibility(cls, state):
        event = events.LobbyHeaderMenuEvent(events.LobbyHeaderMenuEvent.TOGGLE_VISIBILITY, ctx={b'state': state})
        g_eventBus.handleEvent(event, EVENT_BUS_SCOPE.LOBBY)
        return
