from __future__ import absolute_import
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import LobbyState, LobbyStateDescription, LobbyStateFlags, SubScopeSubLayerState, ViewLobbyState

def registerStates(machine):
    machine.addState(VehiclePreviewState())
    machine.addState(HeroTankPreviewState())
    machine.addState(RentalVehiclePreviewState())
    machine.addState(TradeInVehiclePreviewState())
    machine.addState(MarathonVehiclePreviewState())
    machine.addState(OfferGiftVehiclePreviewState())
    machine.addState(StyleProgressionPreviewState())
    machine.addState(StyleBuyingPreviewState())
    machine.addState(ShowcaseStyleBuyingPreviewState())
    machine.addState(VehiclePreviewStateWithTopPanel())
    return


def registerTransitions(machine):
    addTransition = machine.addNavigationTransitionFromParent
    addTransition(machine.getStateByCls(VehiclePreviewState))
    addTransition(machine.getStateByCls(HeroTankPreviewState))
    addTransition(machine.getStateByCls(RentalVehiclePreviewState))
    addTransition(machine.getStateByCls(TradeInVehiclePreviewState))
    addTransition(machine.getStateByCls(MarathonVehiclePreviewState))
    addTransition(machine.getStateByCls(OfferGiftVehiclePreviewState))
    addTransition(machine.getStateByCls(StyleProgressionPreviewState))
    addTransition(machine.getStateByCls(StyleBuyingPreviewState))
    addTransition(machine.getStateByCls(ShowcaseStyleBuyingPreviewState))
    addTransition(machine.getStateByCls(VehiclePreviewStateWithTopPanel))
    return


class _VehiclePreviewStateProto(ViewLobbyState):

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_VehiclePreviewStateProto, self).__init__(flags=flags)
        self.__cachedParams = {}
        return

    def registerTransitions(self):
        from gui.Scaleform.daapi.view.lobby.veh_post_progression.states import VehiclePostProgressionState
        from gui.Scaleform.daapi.view.lobby.vehicle_compare.states import VehicleCompareState
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        machine = self.getMachine()
        self.addNavigationTransition(machine.getStateByCls(VehiclePostProgressionState), record=True)
        self.addNavigationTransition(machine.getStateByCls(VehicleCompareState), record=True)
        self.addNavigationTransition(machine.getStateByCls(ShopState), record=True)
        return

    def serializeParams(self):
        return self.__cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.vehicle_preview()))

    def _prepareCamera(self):
        from ClientSelectableCameraObject import ClientSelectableCameraObject
        ClientSelectableCameraObject.switchCamera()
        return

    def _onEntered(self, event):
        super(_VehiclePreviewStateProto, self)._onEntered(event)
        self.__cachedParams = event.params
        self._prepareCamera()
        return

    def _onExited(self):
        super(_VehiclePreviewStateProto, self)._onExited()
        self.__cachedParams = {}
        return

    def _getViewLoadCtx(self, event):
        return {b'ctx': {b'itemCD': (event.params[b'itemCD']), 
                    b'previewAlias': (event.params.get(b'previewAlias', None)), 
                    b'vehicleStrCD': (event.params.get(b'vehicleStrCD', None)), 
                    b'itemsPack': (event.params.get(b'itemsPack', None)), 
                    b'offers': (event.params.get(b'offers', None)), 
                    b'price': (event.params.get(b'price', None)), 
                    b'oldPrice': (event.params.get(b'oldPrice', None)), 
                    b'title': (event.params.get(b'title', None)), 
                    b'description': (event.params.get(b'description', None)), 
                    b'endTime': (event.params.get(b'endTime', None)), 
                    b'buyParams': (event.params.get(b'buyParams', None)), 
                    b'obtainingMethod': (event.params.get(b'obtainingMethod', None)), 
                    b'vehParams': (event.params.get(b'vehParams', None)), 
                    b'style': (event.params.get(b'style', None)), 
                    b'resetAppearance': (event.params.get(b'resetAppearance', False)), 
                    b'topPanelData': (event.params.get(b'topPanelData', None))}}


@SubScopeSubLayerState.parentOf
class VehiclePreviewStateWithTopPanel(LobbyState):
    STATE_ID = b'vehiclePreviewWithTopPanel'

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(ConfigurableVehiclePreviewState(LobbyStateFlags.INITIAL))
        lsm.addState(StylePreviewState())
        return

    def registerTransitions(self):
        for state in self.getChildrenStates():
            self.getParent().addNavigationTransition(state)
            self.addNavigationTransition(state)

        return


@SubScopeSubLayerState.parentOf
class VehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.VEHICLE_PREVIEW)


@SubScopeSubLayerState.parentOf
class HeroTankPreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.HERO_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.HERO_VEHICLE_PREVIEW)

    def _prepareCamera(self):
        from ClientSelectableCameraObject import ClientSelectableCameraObject
        ClientSelectableCameraObject.switchCamera(cameraName=b'HeroTank')
        return

    def _getViewLoadCtx(self, event):
        params = super(HeroTankPreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'previewAppearance': (event.params.get(b'previewAppearance', None)), 
           b'isHeroTank': (event.params.get(b'isHeroTank', True)), 
           b'previousBackAlias': (event.params.get(b'previousBackAlias', None)), 
           b'hangarVehicleCD': (event.params.get(b'hangarVehicleCD', None)), 
           b'backOutfit': (event.params.get(b'backOutfit', None))})
        return params


@VehiclePreviewStateWithTopPanel.parentOf
class ConfigurableVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.CONFIGURABLE_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.CONFIGURABLE_VEHICLE_PREVIEW)

    def _getViewLoadCtx(self, event):
        params = super(ConfigurableVehiclePreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'hiddenBlocks': (event.params.get(b'hiddenBlocks', None)), 
           b'heroInteractive': (event.params.get(b'heroInteractive', True)), 
           b'subscriptions': (event.params.get(b'subscriptions', ()))})
        return params


@SubScopeSubLayerState.parentOf
class RentalVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.RENTAL_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.RENTAL_VEHICLE_PREVIEW)


@SubScopeSubLayerState.parentOf
class TradeInVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.TRADE_IN_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.TRADE_IN_VEHICLE_PREVIEW)


@SubScopeSubLayerState.parentOf
class MarathonVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.MARATHON_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.MARATHON_VEHICLE_PREVIEW)

    def _getViewLoadCtx(self, event):
        params = super(MarathonVehiclePreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'marathonPrefix': (event.params.get(b'marathonPrefix', b'')), 
           b'previewAppearance': (event.params.get(b'previewAppearance', None)), 
           b'backToHangar': (event.params.get(b'backToHangar', False))})
        return params


@SubScopeSubLayerState.parentOf
class OfferGiftVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.OFFER_GIFT_VEHICLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.OFFER_GIFT_VEHICLE_PREVIEW)

    def _getViewLoadCtx(self, event):
        params = super(OfferGiftVehiclePreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'offerID': (event.params.get(b'offerID', None)), 
           b'giftID': (event.params.get(b'giftID', None)), 
           b'confirmCallback': (event.params.get(b'confirmCallback', None)), 
           b'customCallbacks': (event.params.get(b'customCallbacks', {}))})
        return params


class _StylePreviewStateProto(ViewLobbyState):

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_StylePreviewStateProto, self).__init__(flags=flags)
        self.__cachedParams = {}
        return

    def registerTransitions(self):
        from gui.Scaleform.daapi.view.lobby.veh_post_progression.states import VehiclePostProgressionState
        from gui.Scaleform.daapi.view.lobby.vehicle_compare.states import VehicleCompareState
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        machine = self.getMachine()
        self.addNavigationTransition(machine.getStateByCls(VehiclePostProgressionState), record=True)
        self.addNavigationTransition(machine.getStateByCls(VehicleCompareState), record=True)
        self.addNavigationTransition(machine.getStateByCls(ShopState), record=True)
        return

    def serializeParams(self):
        return self.__cachedParams

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.style_preview()))

    def _prepareCamera(self):
        from ClientSelectableCameraObject import ClientSelectableCameraObject
        ClientSelectableCameraObject.switchCamera()
        return

    def _onEntered(self, event):
        super(_StylePreviewStateProto, self)._onEntered(event)
        self.__cachedParams = event.params
        self._prepareCamera()
        return

    def _onExited(self):
        super(_StylePreviewStateProto, self)._onExited()
        self.__cachedParams = {}
        return

    def _getViewLoadCtx(self, event):
        return {b'ctx': {b'itemCD': (event.params[b'itemCD']), 
                    b'style': (event.params.get(b'style', None)), 
                    b'resetAppearance': (event.params.get(b'resetAppearance', False)), 
                    b'styleDescr': (event.params.get(b'styleDescr', b'')), 
                    b'backPreviewAlias': (event.params.get(b'backPreviewAlias', None)), 
                    b'topPanelData': (event.params.get(b'topPanelData', None)), 
                    b'outfit': (event.params.get(b'outfit', None)), 
                    b'isHeroTank': (event.params.get(b'isHeroTank', False)), 
                    b'itemsPack': (event.params.get(b'itemsPack', None))}}


@VehiclePreviewStateWithTopPanel.parentOf
class StylePreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.STYLE_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.STYLE_PREVIEW)


@SubScopeSubLayerState.parentOf
class StyleProgressionPreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.STYLE_PROGRESSION_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.STYLE_PROGRESSION_PREVIEW)

    def _getViewLoadCtx(self, event):
        params = super(StyleProgressionPreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'styleLevel': (event.params.get(b'styleLevel', None)), 
           b'chapterId': (event.params.get(b'chapterId', None))})
        return params


@SubScopeSubLayerState.parentOf
class StyleBuyingPreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.STYLE_BUYING_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.STYLE_BUYING_PREVIEW)

    def _getViewLoadCtx(self, event):
        params = super(StyleBuyingPreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'styleLevel': (event.params.get(b'styleLevel', None)), 
           b'price': (event.params.get(b'price', None)), 
           b'buyParams': (event.params.get(b'buyParams', None))})
        return params


@SubScopeSubLayerState.parentOf
class ShowcaseStyleBuyingPreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.SHOWCASE_STYLE_BUYING_PREVIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.SHOWCASE_STYLE_BUYING_PREVIEW)

    def _getViewLoadCtx(self, event):
        params = super(ShowcaseStyleBuyingPreviewState, self)._getViewLoadCtx(event)
        params[b'ctx'].update({b'price': (event.params.get(b'price', None)), 
           b'originalPrice': (event.params.get(b'originalPrice', None)), 
           b'buyParams': (event.params.get(b'buyParams', None)), 
           b'obtainingMethod': (event.params.get(b'obtainingMethod', None)), 
           b'endTime': (event.params.get(b'endTime', None)), 
           b'discountPercent': (event.params.get(b'discountPercent', None))})
        return params
