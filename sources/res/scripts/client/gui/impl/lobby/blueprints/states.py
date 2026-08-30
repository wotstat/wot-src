import typing
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.lobby_state_machine.states import GuiImplViewLobbyState, SubScopeSubLayerState, LobbyStateDescription
from gui.impl.gen import R

def registerStates(machine):
    machine.addState(BlueprintState())
    return


def registerTransitions(machine):
    blueprint = machine.getStateByCls(BlueprintState)
    machine.addNavigationTransitionFromParent(blueprint)
    return


@SubScopeSubLayerState.parentOf
class BlueprintState(GuiImplViewLobbyState):
    STATE_ID = b'blueprint'
    VIEW_KEY = ViewKey(R.views.lobby.blueprints.blueprint_screen.blueprint_screen.BlueprintScreen())

    def __init__(self):
        from gui.impl.lobby.blueprints.blueprint_screen import BlueprintScreen
        super(BlueprintState, self).__init__(BlueprintScreen, ScopeTemplates.LOBBY_SUB_SCOPE)
        self._cachedParams = None
        return

    def _getViewLoadCtx(self, event):
        return {b'ctx': {b'vehicleCD': (event.params[b'vehicleCD'])}}

    def _onEntered(self, event):
        self._cachedParams = event.params
        super(BlueprintState, self)._onEntered(event)
        return

    def serializeParams(self):
        return self._cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.blueprints()))
