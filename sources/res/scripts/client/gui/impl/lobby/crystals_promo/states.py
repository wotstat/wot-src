import typing
from frameworks_common.state_machine.transitions import TransitionType
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.lobby_state_machine.states import GuiImplViewLobbyState, TopScopeTopLayerState, LobbyStateDescription
from gui.impl.gen import R
from gui.impl.lobby.crystals_promo.crystals_promo_view import CrystalsPromoView

def registerStates(machine):
    machine.addState(CrystalsPromoState())
    return


def registerTransitions(machine):
    return


@TopScopeTopLayerState.parentOf
class CrystalsPromoState(GuiImplViewLobbyState):
    STATE_ID = b'crystalsPromo'
    VIEW_KEY = ViewKey(R.views.lobby.crystalsPromo.CrystalsPromoView())

    def __init__(self):
        super(CrystalsPromoState, self).__init__(CrystalsPromoView, ScopeTemplates.LOBBY_TOP_SUB_SCOPE)
        return

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        self.addNavigationTransition(lsm.getStateByCls(ShopState), transitionType=TransitionType.EXTERNAL)
        return

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.crystals_promo()))
