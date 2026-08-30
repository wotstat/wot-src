from __future__ import absolute_import
import typing
from frameworks.state_machine import StateFlags
from frameworks.state_machine.transitions import TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.storage_view import StorageView
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS
from gui.lobby_state_machine.states import SubScopeSubLayerState, LobbyStateDescription, ViewLobbyState
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader

def registerStates(machine):
    machine.addState(StorageState())
    machine.addState(OfferGiftsState())
    return


def registerTransitions(machine):
    storage = machine.getStateByCls(StorageState)
    machine.addNavigationTransitionFromParent(storage)
    return


@SubScopeSubLayerState.parentOf
class StorageState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.LOBBY_STORAGE
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOBBY_STORAGE)
    __appLoader = dependency.descriptor(IAppLoader)

    def registerTransitions(self):
        from gui.impl.lobby.vehicle_hub import OverviewState
        from gui.impl.lobby.blueprints.states import BlueprintState
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import StylePreviewState
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import StyleProgressionPreviewState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(BlueprintState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(OverviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(StyleProgressionPreviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(StylePreviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(OfferGiftsState), record=True)
        return

    def _getViewLoadCtx(self, event):
        return {b'ctx': {b'defaultSection': (event.params.get(b'defaultSection', STORAGE_CONSTANTS.FOR_SELL)), 
                    b'defaultTab': (event.params.get(b'defaultTab', None))}}

    def serializeParams(self):
        storageView = self.__appLoader.getApp().containerManager.getViewByKey(self.getViewKey())
        section, tab = storageView.findActiveSectionAndTabId()
        return {b'defaultSection': section, 
           b'defaultTab': tab}

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.depot()))


@SubScopeSubLayerState.parentOf
class OfferGiftsState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.OFFER_GIFT_VIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.OFFER_GIFT_VIEW)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(OfferGiftsState, self).__init__(flags=flags)
        self.__cachedParams = {}
        return

    def registerTransitions(self):
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import OfferGiftVehiclePreviewState
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)
        self.addNavigationTransition(self, transitionType=TransitionType.EXTERNAL)
        self.addNavigationTransition(lsm.getStateByCls(OfferGiftVehiclePreviewState), record=True)
        return

    def serializeParams(self):
        return self.__cachedParams

    @classmethod
    def goTo(cls, offerID=None, overrideSuccessCallback=None, overrideOnBackCallback=None):
        super(OfferGiftsState, cls).goTo(offerID=offerID, overrideSuccessCallback=overrideSuccessCallback, overrideOnBackCallback=overrideOnBackCallback)
        return

    def _onEntered(self, event):
        super(OfferGiftsState, self)._onEntered(event)
        self.__cachedParams = event.params
        return

    def _onExited(self):
        super(OfferGiftsState, self)._onExited()
        self.__cachedParams = {}
        return

    def _getViewLoadCtx(self, event):
        return {b'offerID': (event.params.get(b'offerID', None)), 
           b'overrideSuccessCallback': (event.params.get(b'overrideSuccessCallback', None)), 
           b'overrideOnBackCallback': (event.params.get(b'overrideOnBackCallback', None))}
