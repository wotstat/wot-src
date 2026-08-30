import typing
from frameworks_common.state_machine.transitions import TransitionType
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.lobby.personal_reserves.reserves_activation_view import ReservesActivationView
from gui.lobby_state_machine.states import GuiImplViewLobbyState, LobbyStateDescription, SubScopeTopLayerState
from gui.impl.gen import R

def registerStates(machine):
    machine.addState(PersonalReservesState())
    return


def registerTransitions(machine):
    return


@SubScopeTopLayerState.parentOf
class PersonalReservesState(GuiImplViewLobbyState):
    STATE_ID = b'personal_reserves'
    VIEW_KEY = ViewKey(R.views.lobby.personal_reserves.ReservesActivationView())

    def __init__(self):
        super(PersonalReservesState, self).__init__(ReservesActivationView, ScopeTemplates.LOBBY_SUB_SCOPE)
        return

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self, transitionType=TransitionType.EXTERNAL)
        return

    def getNavigationDescription(self):
        from gui.shared.event_dispatcher import showPersonalReservesInfomationScreen
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.personal_reserves()), infos=(
         LobbyStateDescription.Info(type=LobbyStateDescription.Info.Type.INFO, onMoreInfoRequested=showPersonalReservesInfomationScreen),))
