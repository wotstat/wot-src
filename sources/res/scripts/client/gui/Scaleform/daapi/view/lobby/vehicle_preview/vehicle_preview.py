import itertools
from copy import deepcopy
import BigWorld, SoundGroups
from CurrentVehicle import g_currentPreviewVehicle, g_currentVehicle
from HeroTank import HeroTank
from account_helpers import AccountSettings
from account_helpers.AccountSettings import PREVIEW_INFO_PANEL_IDX
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS
from constants import QUEUE_TYPE
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventProgressionUrl
from gui.Scaleform.daapi.view.lobby.LobbySelectableView import LobbySelectableView
from gui.Scaleform.daapi.view.lobby.store.browser.sound_constants import SHOP_PREVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip
from gui.Scaleform.daapi.view.lobby.vehicle_preview.hero_tank_preview_constants import getHeroTankPreviewParams
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info.crew_tab import getUniqueMembers
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import OFFER_CHANGED_EVENT, addBuiltInEquipment, getActiveOffer
from gui.Scaleform.daapi.view.lobby.vehicle_preview.sound_constants import RESEARCH_PREVIEW_SOUND_SPACE, VEHICLE_PREVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.VehiclePreviewMeta import VehiclePreviewMeta
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates, CameraRelatedEvents
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.buy_vehicle_view import BuyVehicleWindow
from gui.prb_control.dispatcher import g_prbLoader
from gui.resource_well.resource_well_helpers import isResourceWellRewardVehicle
from gui.shared import EVENT_BUS_SCOPE, event_bus_handlers, event_dispatcher, events, g_eventBus
from gui.shared.event_dispatcher import showShop, showVehPostProgressionView, getTechTreeLoadEvent
from gui.shared.events import LobbySimpleEvent
from gui.shared.formatters import getRoleTextWithIcon, text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.money import MONEY_UNDEFINED
from gui.shared.tutorial_helper import getTutorialGlobalStorage
from gui.techtree.go_back_helper import WulfPreviewAlias
from helpers import dependency
from helpers.i18n import makeString as _ms
from preview_selectable_logic import PreviewSelectableLogic
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IHeroTankController, IVehicleComparisonBasket, IPersonalMissionsController
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from tutorial.control.context import GLOBAL_FLAG
from uilogging.shop.loggers import getPreviewUILoggers
from uilogging.shop.logging_constants import ShopCloseItemStates
from web.web_client_api.common import ItemPackEntry, ItemPackType, ItemPackTypeGroup
_BACK_BTN_LABELS = {(VIEW_ALIAS.LOBBY_HANGAR): b'hangar', 
   (VIEW_ALIAS.LOBBY_STORE): b'shop', 
   (VIEW_ALIAS.LOBBY_STORAGE): b'storage', 
   (VIEW_ALIAS.LOBBY_RESEARCH): b'researchTree', 
   (WulfPreviewAlias.WULF_TECHTREE): b'researchTree', 
   (VIEW_ALIAS.VEHICLE_COMPARE): b'vehicleCompare', 
   (VIEW_ALIAS.REFERRAL_PROGRAM_WINDOW): b'referralProgram', 
   (VIEW_ALIAS.EPIC_BATTLE_PAGE): b'frontline', 
   (VIEW_ALIAS.RANKED_BATTLE_PAGE): b'ranked', 
   (VIEW_ALIAS.ADVENT_CALENDAR): b'adventCalendar', 
   (VIEW_ALIAS.VEH_POST_PROGRESSION): b'vehPostProgression', 
   (PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_AWARDS_VIEW_ALIAS): b'personalAwards', 
   (VIEW_ALIAS.RENTAL_VEHICLE_PREVIEW): None, 
   (VIEW_ALIAS.CONFIGURABLE_VEHICLE_PREVIEW): None, 
   (VIEW_ALIAS.RESOURCE_WELL_VEHICLE_PREVIEW): b'resourceWell', 
   (VIEW_ALIAS.SHOP_SALES_VEHICLE_PREVIEW): b'eventProgression', 
   (VIEW_ALIAS.STAT_TRACK_VEHICLE_PREVIEW): None, 
   (VIEW_ALIAS.STRONGHOLD_PROGRESSION): None}
_TABS_DATA = (
 {b'id': (VEHPREVIEW_CONSTANTS.BROWSE_LINKAGE), 
    b'label': (VEHICLE_PREVIEW.INFOPANEL_TAB_BROWSE_NAME), 
    b'linkage': (VEHPREVIEW_CONSTANTS.BROWSE_LINKAGE)},
 {b'id': (VEHPREVIEW_CONSTANTS.MODULES_LINKAGE), 
    b'label': (VEHICLE_PREVIEW.INFOPANEL_TAB_MODULES_NAME), 
    b'linkage': (VEHPREVIEW_CONSTANTS.MODULES_LINKAGE)},
 {b'id': (VEHPREVIEW_CONSTANTS.CREW_LINKAGE), 
    b'label': (VEHICLE_PREVIEW.INFOPANEL_TAB_CREWINFO_NAME), 
    b'linkage': (VEHPREVIEW_CONSTANTS.CREW_LINKAGE)})
_SHOW_BACK_BTN = True
_SHOW_CLOSE_BTN = True

def _isCollectibleVehicleWithModules():
    return g_currentPreviewVehicle.isCollectible() and g_currentPreviewVehicle.hasModulesToSelect()


def _updateCollectorHintParameters():
    tutorialStorage = getTutorialGlobalStorage()
    if tutorialStorage is None:
        return
    else:
        isActiveModulesTab = AccountSettings.getSettings(PREVIEW_INFO_PANEL_IDX) == _getModulesTabIdx()
        hintValue = False if isActiveModulesTab else _isCollectibleVehicleWithModules()
        tutorialStorage.setValue(GLOBAL_FLAG.COLLECTIBLE_VEHICLE_PREVIEW_ENABLED, hintValue)
        return


def _updatePostProgressionParameters():
    tutorialStorage = getTutorialGlobalStorage()
    if tutorialStorage is None:
        return
    else:
        tutorialStorage.setValue(GLOBAL_FLAG.VEH_POST_PROGRESSION_ENABLED, g_currentPreviewVehicle.isPostProgressionExists())
        return


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def _isPostProgressionBulletVisible(settingsCore=None):
    return g_currentPreviewVehicle.isPostProgressionExists() and not settingsCore.serverSettings.getUIStorage().get(UI_STORAGE_KEYS.VEH_PREVIEW_POST_PROGRESSION_BULLET_SHOWN)


def _getModulesTabIdx():
    return [tab[b'id'] for tab in _TABS_DATA].index(VEHPREVIEW_CONSTANTS.MODULES_LINKAGE)


class VehiclePreview(LobbySelectableView, VehiclePreviewMeta):
    __background_alpha__ = 0.0
    __metaclass__ = event_bus_handlers.EventBusListener
    _itemsCache = dependency.descriptor(IItemsCache)
    __eventsCache = dependency.descriptor(IEventsCache)
    __comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    __heroTanksControl = dependency.descriptor(IHeroTankController)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __guiLoader = dependency.descriptor(IGuiLoader)
    __personalMissionsController = dependency.descriptor(IPersonalMissionsController)

    def __init__(self, ctx=None):
        self.__ctx = ctx
        self._backAlias = ctx.get(b'previewAlias', VIEW_ALIAS.LOBBY_HANGAR)
        self._itemsPack = ctx.get(b'itemsPack')
        if self._backAlias == VIEW_ALIAS.LOBBY_STORE or self._itemsPack is not None:
            self._COMMON_SOUND_SPACE = SHOP_PREVIEW_SOUND_SPACE
        elif self._backAlias in (WulfPreviewAlias.WULF_TECHTREE, VIEW_ALIAS.LOBBY_RESEARCH):
            self._COMMON_SOUND_SPACE = RESEARCH_PREVIEW_SOUND_SPACE
        elif self._backAlias in (VIEW_ALIAS.RANKED_BATTLE_PAGE, VIEW_ALIAS.VEH_POST_PROGRESSION):
            self._COMMON_SOUND_SPACE = VEHICLE_PREVIEW_SOUND_SPACE
        else:
            self._COMMON_SOUND_SPACE = ctx.get(b'soundSpace', self._COMMON_SOUND_SPACE)
        super(VehiclePreview, self).__init__(ctx)
        self.__currentOffer = None
        self._vehicleCD = ctx[b'itemCD']
        self.__vehicleStrCD = ctx.get(b'vehicleStrCD')
        self._previousBackAlias = ctx.get(b'previousBackAlias')
        self._previewBackCb = ctx.get(b'previewBackCb')
        self._backBtnLabel = ctx.get(b'backBtnLabel')
        self.__isHeroTank = ctx.get(b'isHeroTank', False)
        self.__customizationCD = (ctx.get(b'vehParams') or {}).get(b'styleCD')
        self.__offers = ctx.get(b'offers')
        self._price = ctx.get(b'price', MONEY_UNDEFINED)
        self._oldPrice = ctx.get(b'oldPrice', MONEY_UNDEFINED)
        self._title = ctx.get(b'title')
        self._description = ctx.get(b'description')
        self.__endTime = ctx.get(b'endTime')
        self.__buyParams = ctx.get(b'buyParams')
        self.__topPanelData = ctx.get(b'topPanelData') or {}
        self.__style = ctx.get(b'style')
        self.__subscriptions = ctx.get(b'subscriptions') or ()
        self.__bottomPanelTextData = ctx.get(b'bottomPanelTextData')
        self.__showCloseBtn = ctx.get(b'showCloseBtn', _SHOW_CLOSE_BTN)
        self.__unmodifiedItemsPack = deepcopy(self._itemsPack)
        addBuiltInEquipment(self._itemsPack, self._itemsCache, self._vehicleCD)
        notInteractive = (
         VIEW_ALIAS.LOBBY_STORE, VIEW_ALIAS.RANKED_BATTLE_PAGE, VIEW_ALIAS.VEH_POST_PROGRESSION,
         VIEW_ALIAS.RESOURCE_WELL_VEHICLE_PREVIEW, VIEW_ALIAS.RESOURCE_WELL_HERO_VEHICLE_PREVIEW)
        self._heroInteractive = not (self._itemsPack or self.__offers or ctx.get(b'offerID', 0) or self.__topPanelData or self._backAlias in notInteractive)
        self.__haveCustomCrew = any(item.type == ItemPackType.CREW_CUSTOM for item in self._itemsPack) if self._itemsPack else False
        self.__hangarVehicleCD = ctx.get(b'hangarVehicleCD')
        self.__previewAppearance = ctx.get(b'previewAppearance')
        if self.__previewAppearance:
            self.__vehAppearanceChanged = True
            g_currentPreviewVehicle.resetAppearance(self.__previewAppearance)
        else:
            self.__vehAppearanceChanged = False
        self.__keepVehicleSelectionEnabled = False
        self._needToResetAppearance = True
        if not self.__isHeroTank:
            self.__hangarSpace.removeVehicle()
        g_currentPreviewVehicle.selectHeroTank(self.__isHeroTank)
        self.__uiMetricsLogger, self.__uiFlowLogger = getPreviewUILoggers(bool(self._itemsPack), str(self._vehicleCD), self.__buyParams)
        return

    def setTopPanel(self):
        self.as_setTopPanelS(self.__topPanelData.get(b'linkage', b''))
        return

    def setBottomPanel(self):
        self.as_setBottomPanelS(VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_LINKAGE)
        return

    def _populate(self):
        self.addListener(CameraRelatedEvents.VEHICLE_LOADING, self.__onVehicleLoading, EVENT_BUS_SCOPE.DEFAULT)
        self.setTopPanel()
        self.setBottomPanel()
        if g_currentPreviewVehicle.intCD == self._vehicleCD:
            self.__fullUpdate()
        if self.__hangarVehicleCD and self.__isHeroTank and self.__vehAppearanceChanged:
            g_currentPreviewVehicle.resetAppearance()
            g_currentPreviewVehicle.selectVehicle(self.__hangarVehicleCD, style=self.__style)
            g_currentPreviewVehicle.resetAppearance(self.__previewAppearance)
        elif g_currentPreviewVehicle.intCD == self._vehicleCD:
            g_currentPreviewVehicle.selectNoVehicle()
        g_currentPreviewVehicle.selectVehicle(self._vehicleCD, self.__vehicleStrCD, style=self.__style)
        super(VehiclePreview, self)._populate()
        g_currentPreviewVehicle.onChanged += self.__onVehicleChanged
        g_currentPreviewVehicle.onVehicleInventoryChanged += self._onInventoryChanged
        self.__comparisonBasket.onChange += self.__onCompareBasketChanged
        self.__comparisonBasket.onSwitchChange += self.__updateHeaderData
        self.__hangarSpace.onSpaceCreate += self.__onHangarCreateOrRefresh
        self.__hangarSpace.onSpaceRefresh += self.closeView
        self.__hangarSpace.setVehicleSelectable(True)
        if not g_currentPreviewVehicle.isPresent():
            event_dispatcher.showHangar()
        if not self._heroInteractive:
            self.__heroTanksControl.setInteractive(False)
        if self._backAlias == VIEW_ALIAS.LOBBY_STORE:
            self.__uiFlowLogger.logOpenPreview()
            self.__uiMetricsLogger.onViewOpen()
        self.addListener(CameraRelatedEvents.CAMERA_ENTITY_UPDATED, self.handleSelectedEntityUpdated)
        self.addListener(LobbySimpleEvent.ENTITY_TOOLTIP_SHOW, self.__onEntityTooltipShow)
        self.addListener(LobbySimpleEvent.ENTITY_TOOLTIP_HIDE, self.__onEntityTooltipHide)
        specialData = getHeroTankPreviewParams() if self.__isHeroTank else None
        if specialData is not None and specialData.enterEvent:
            SoundGroups.g_instance.playSound2D(specialData.enterEvent)
        g_eventBus.addListener(OFFER_CHANGED_EVENT, self.__onOfferChanged)
        _updateCollectorHintParameters()
        _updatePostProgressionParameters()
        for event, callback in self.__subscriptions:
            event += callback

        self.as_setDataS(self._getData())
        return

    def _dispose(self):
        specialData = getHeroTankPreviewParams() if self.__isHeroTank else None
        if specialData is not None and specialData.exitEvent:
            SoundGroups.g_instance.playSound2D(specialData.exitEvent)
        self.removeListener(CameraRelatedEvents.VEHICLE_LOADING, self.__onVehicleLoading, EVENT_BUS_SCOPE.DEFAULT)
        self.removeListener(LobbySimpleEvent.ENTITY_TOOLTIP_SHOW, self.__onEntityTooltipShow)
        self.removeListener(LobbySimpleEvent.ENTITY_TOOLTIP_HIDE, self.__onEntityTooltipHide)
        g_clientUpdateManager.removeObjectCallbacks(self)
        g_currentPreviewVehicle.onChanged -= self.__onVehicleChanged
        g_currentPreviewVehicle.onVehicleInventoryChanged -= self._onInventoryChanged
        self.__comparisonBasket.onChange -= self.__onCompareBasketChanged
        self.__comparisonBasket.onSwitchChange -= self.__updateHeaderData
        self.__hangarSpace.onSpaceCreate -= self.__onHangarCreateOrRefresh
        self.__hangarSpace.onSpaceRefresh -= self.closeView
        self.__hangarSpace.setVehicleSelectable(self.__keepVehicleSelectionEnabled)
        self.removeListener(CameraRelatedEvents.CAMERA_ENTITY_UPDATED, self.handleSelectedEntityUpdated)
        isMapsTrainingViewOpened = self.__guiLoader.windowsManager.getViewByLayoutID(R.views.lobby.maps_training.MapsTrainingPage()) is not None
        if self._needToResetAppearance and not isMapsTrainingViewOpened:
            g_currentPreviewVehicle.selectNoVehicle()
            g_currentPreviewVehicle.resetAppearance()
        g_currentPreviewVehicle.selectHeroTank(False)
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN), scope=EVENT_BUS_SCOPE.LOBBY)
        if self._backAlias == VIEW_ALIAS.VEHICLE_PREVIEW:
            g_currentVehicle.refreshModel()
        self._previewBackCb = None
        self.__unmodifiedItemsPack = None
        super(VehiclePreview, self)._dispose()
        if not self._heroInteractive:
            self.__heroTanksControl.setInteractive(True)
        if self.__vehAppearanceChanged and not isMapsTrainingViewOpened:
            g_currentPreviewVehicle.resetAppearance()
        g_eventBus.removeListener(OFFER_CHANGED_EVENT, self.__onOfferChanged)
        for event, callback in self.__subscriptions:
            event -= callback

        return

    def __onEntityTooltipShow(self, event):
        itemId = event.ctx.get(b'selectionId', b'')
        self.as_show3DSceneTooltipS(TOOLTIPS_CONSTANTS.ENVIRONMENT, [itemId])
        return

    def __onEntityTooltipHide(self, _):
        self.as_hide3DSceneTooltipS()
        return

    def closeView(self):
        if self._backAlias == VIEW_ALIAS.LOBBY_STORE:
            self.__uiMetricsLogger.onViewClosed(ShopCloseItemStates.CLOSE_BUTTON.value)
        event_dispatcher.showHangar()
        return

    def onBackClick(self):
        if self._backAlias == VIEW_ALIAS.LOBBY_STORE:
            self.__uiMetricsLogger.onViewClosed(ShopCloseItemStates.BACK_BUTTON.value)
        self._processBackClick()
        return

    def onOpenInfoTab(self, index):
        AccountSettings.setSettings(PREVIEW_INFO_PANEL_IDX, index)
        _updatePostProgressionParameters()
        return

    def onGoToPostProgressionClick(self):
        self._resetPostProgressionBullet()
        if self._backAlias == VIEW_ALIAS.VEH_POST_PROGRESSION and callable(self._previewBackCb):
            self._previewBackCb()
        else:
            showVehPostProgressionView(self._vehicleCD, exitEvent=self._getExitEvent())
        return

    def onCompareClick(self):
        self.__comparisonBasket.addVehicle(self._vehicleCD, initParameters={b'strCD': (g_currentPreviewVehicle.item.descriptor.makeCompactDescr())})
        return

    def handleSelectedEntityUpdated(self, event):
        ctx = event.ctx
        entity = BigWorld.entities.get(ctx[b'entityId'], None)
        if ctx[b'state'] == CameraMovementStates.MOVING_TO_OBJECT:
            if isinstance(entity, HeroTank):
                descriptor = entity.typeDescriptor
                if descriptor:
                    self._needToResetAppearance = False
                    vehicleCD = descriptor.type.compactDescr
                    if isResourceWellRewardVehicle(vehicleCD=vehicleCD):
                        event_dispatcher.showResourceWellHeroPreview(vehicleCD=vehicleCD, previewAlias=VIEW_ALIAS.VEHICLE_PREVIEW, previousBackAlias=self._backAlias, backCallback=self._previewBackCb)
                    else:
                        event_dispatcher.showHeroTankPreview(vehicleCD, previewAlias=VIEW_ALIAS.VEHICLE_PREVIEW, previousBackAlias=self._backAlias, previewBackCb=self._previewBackCb, backBtnLabel=self._backBtnLabel)
            elif entity.id == self.__hangarSpace.space.vehicleEntityId:
                self._processBackClick({b'entity': entity})
        return

    def _highlight3DEntityAndShowTT(self, entity):
        itemId = entity.selectionId
        if itemId:
            self.as_show3DSceneTooltipS(TOOLTIPS_CONSTANTS.ENVIRONMENT, [itemId])
        return

    def _fade3DEntityAndHideTT(self, entity):
        self.as_hide3DSceneTooltipS()
        return

    def _createSelectableLogic(self):
        return PreviewSelectableLogic()

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == VEHPREVIEW_CONSTANTS.TOP_PANEL_TABS_PY_ALIAS:
            viewPy.setData(**self.__topPanelData)
            viewPy.setParentCtx(**self.__ctx)
        elif alias == VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_PY_ALIAS:
            viewPy.setIsHeroTank(self.__isHeroTank)
            viewPy.setBackAlias(self._backAlias)
            viewPy.setBackCallback(self._previewBackCb)
            if self._itemsPack:
                viewPy.setPackItems(self._itemsPack, self._price, self._oldPrice)
                viewPy.setPanelTextData(self._title)
                viewPy.setTimerData(self.__endTime)
                viewPy.setBuyParams(self.__buyParams)
                viewPy.setBundlePreviewMetricsLogger(self.__uiMetricsLogger)
            elif self.__offers:
                viewPy.setOffers(self.__offers, self._title)
            elif self.__bottomPanelTextData:
                viewPy.setPanelTextData(**self.__bottomPanelTextData)
        elif alias == VEHPREVIEW_CONSTANTS.CREW_LINKAGE:
            pmVehicleCDs = self.__eventsCache.getPersonalMissions().getAllPMVehiclesCDs()
            pmVehicleCDs.extend([vehicle.intCD for vehicle in self.__personalMissionsController.getVehiclesForChampionQuestPM3()])
            if self._itemsPack:
                crewItems = tuple(item for item in self._itemsPack if item.type in ItemPackTypeGroup.CREW)
                vehicleItems = tuple(item for item in self._itemsPack if item.type in ItemPackTypeGroup.VEHICLE)
                if crewItems and not vehicleItems:
                    groupID = crewItems[0].groupID
                    vehicleItems = (ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=groupID),)
                viewPy.setVehicleCrews(vehicleItems, crewItems)
            elif self.__offers:
                offer = getActiveOffer(self.__offers)
                viewPy.setVehicleCrews((
                 ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=offer.crew.groupID),), (
                 offer.crew,))
            if self.__isHeroTank:
                crewData = self.__heroTanksControl.getCurrentTankCrew()
                if crewData and crewData.get(b'tankmen'):
                    viewPy.setVehicleCrews((
                     ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=1),), (
                     ItemPackEntry(type=ItemPackType.CREW_CUSTOM, groupID=1, extra=crewData),))
                else:
                    viewPy.setVehicleCrews((ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=1),), ())
            elif g_currentPreviewVehicle.item.intCD in pmVehicleCDs:
                viewPy.setVehicleCrews((ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=1),), [
                 ItemPackEntry(id=1, type=ItemPackType.CREW_100, count=1, groupID=1)])
            else:
                viewPy.setVehicleCrews((ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=1),), ())
        elif alias == VEHPREVIEW_CONSTANTS.BROWSE_LINKAGE:
            viewPy.setHeroTank(self.__isHeroTank)
            if self.__offers:
                offer = self.__currentOffer if self.__currentOffer is not None else getActiveOffer(self.__offers)
                viewPy.setActiveOffer(offer)
        elif alias == VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_WOT_PLUS_LINKAGE:
            viewPy.setOffers(self.__offers)
        return

    def _getData(self):
        vehicle = g_currentPreviewVehicle.item
        vehicleLevel = makeHtmlString(b'html_templates:lobby/vehicle_preview', b'vehicleNameRegular', {b'name': (backport.text(R.strings.menu.header.level.num(vehicle.level)()))})
        vehicleNameStyle = b'vehicleNamePremium' if vehicle.isPremium else b'vehicleNameRegular'
        vehicleName = makeHtmlString(b'html_templates:lobby/vehicle_preview', vehicleNameStyle, {b'name': (vehicle.descriptor.type.shortUserString)})
        compareBtnEnabled, compareBtnTooltip = resolveStateTooltip(self.__comparisonBasket, vehicle, VEH_COMPARE.STORE_COMPAREVEHICLEBTN_TOOLTIPS_ADDTOCOMPARE, VEH_COMPARE.STORE_COMPAREVEHICLEBTN_TOOLTIPS_DISABLED)
        result = {b'closeBtnLabel': (VEHICLE_PREVIEW.HEADER_CLOSEBTN_LABEL), 
           b'backBtnLabel': (VEHICLE_PREVIEW.HEADER_BACKBTN_LABEL), 
           b'backBtnDescrLabel': (self._getBackBtnLabel()), 
           b'showCloseBtn': (self.__showCloseBtn), 
           b'showBackButton': _SHOW_BACK_BTN, 
           b'showPostProgressionBtn': (vehicle.isPostProgressionExists), 
           b'vehicleName': vehicleName, 
           b'vehicleLevel': vehicleLevel, 
           b'vehicleType': (vehicle.type), 
           b'isVehicleElite': (vehicle.isElite), 
           b'nationFlagIcon': (RES_ICONS.getNationFlag(vehicle.nationName)), 
           b'compareBtnTooltip': compareBtnTooltip, 
           b'showCompareBtn': compareBtnEnabled, 
           b'listDesc': (self.__getInfoPanelListDescription(vehicle)), 
           b'isMultinational': (vehicle.hasNationGroup), 
           b'roleText': (getRoleTextWithIcon(vehicle.role, vehicle.roleLabel)), 
           b'roleId': (vehicle.role), 
           b'vehicleCD': (vehicle.intCD)}
        return result

    def _getExitEvent(self):
        hangarVehicleCD = None
        hangarVehicle = self.__hangarSpace.getVehicleEntity()
        currentVehicle = g_currentVehicle.item
        hangarVehicleDescr = hangarVehicle.typeDescriptor
        if self.__isHeroTank and currentVehicle is not None and hangarVehicleDescr is not None and hangarVehicleDescr.type.compactDescr != currentVehicle.compactDescr:
            hangarVehicleCD = hangarVehicleDescr.type.compactDescr
        return events.LoadViewEvent(SFViewLoadParams(self.alias), ctx={b'itemCD': (self._vehicleCD), 
           b'previewAlias': (self._backAlias), 
           b'previousBackAlias': (self._previousBackAlias), 
           b'vehicleStrCD': (self.__vehicleStrCD), 
           b'previewBackCb': (self._previewBackCb), 
           b'bottomPanelTextData': (self.__bottomPanelTextData), 
           b'itemsPack': (self.__unmodifiedItemsPack), 
           b'offers': (self.__offers), 
           b'price': (self._price), 
           b'oldPrice': (self._oldPrice), 
           b'title': (self._title), 
           b'description': (self._description), 
           b'endTime': (self.__endTime), 
           b'buyParams': (self.__buyParams), 
           b'vehParams': ({b'styleCD': (self.__customizationCD)} if self.__customizationCD is not None else {}), 
           b'isHeroTank': (self.__isHeroTank), 
           b'hangarVehicleCD': hangarVehicleCD, 
           b'topPanelData': (self.__topPanelData), 
           b'style': (self.__ctx.get(b'style')), 
           b'backBtnLabel': (self._backBtnLabel), 
           b'previewAppearance': (self.__previewAppearance)})

    def __onVehicleLoading(self, ctxEvent):
        if self.__customizationCD is not None and not ctxEvent.ctx.get(b'started'):
            customizationItem = self._itemsCache.items.getItemByCD(self.__customizationCD)
            if customizationItem is None:
                return
            if customizationItem.itemTypeID == GUI_ITEM_TYPE.STYLE:
                g_currentPreviewVehicle.previewStyle(customizationItem)
            elif customizationItem.itemTypeID == GUI_ITEM_TYPE.CAMOUFLAGE:
                g_currentPreviewVehicle.previewCamouflage(customizationItem)
        return

    def __fullUpdate(self):
        self.__updateHeaderData()
        self.__updateTabsData()
        self.__updateModuleBullet()
        return

    def __updateTabsData(self):
        selectedTabInd = AccountSettings.getSettings(PREVIEW_INFO_PANEL_IDX)
        if self.__haveCustomCrew or self.__offers:
            tab_ids = [tab[b'id'] for tab in _TABS_DATA]
            if VEHPREVIEW_CONSTANTS.CREW_LINKAGE in tab_ids:
                selectedTabInd = tab_ids.index(VEHPREVIEW_CONSTANTS.CREW_LINKAGE)
        for idx, tab in enumerate(_TABS_DATA):
            tab[b'selected'] = selectedTabInd == idx

        self.as_setTabsDataS(_TABS_DATA)
        return

    def __onVehicleChanged(self, *args):
        if g_currentPreviewVehicle.isPresent():
            self._vehicleCD = g_currentPreviewVehicle.item.intCD
            self.__updateCrewTabLabel()
            self.__fullUpdate()
        return

    def __updateCrewTabLabel(self):
        crewCount = len(g_currentPreviewVehicle.item.crew)
        crewCount += len(getUniqueMembers(g_currentPreviewVehicle.item))
        for tab in _TABS_DATA:
            if tab[b'linkage'] == VEHPREVIEW_CONSTANTS.CREW_LINKAGE:
                tab[b'label'] = _ms(VEHICLE_PREVIEW.INFOPANEL_TAB_CREWINFO_NAME, crewCount=crewCount)

        return

    def __onCompareBasketChanged(self, changedData):
        if changedData.isFullChanged:
            self.__updateHeaderData()
        return

    def __updateHeaderData(self):
        self.as_setDataS(self._getData())
        return

    @staticmethod
    def __getInfoPanelListDescription(vehicle):
        descriptions = (
         text_styles.main(VEHICLE_PREVIEW.INFOPANEL_TAB_LISTDESC_CREW),
         text_styles.main(VEHICLE_PREVIEW.INFOPANEL_TAB_LISTDESC_CREWSKILLS),
         text_styles.main(VEHICLE_PREVIEW.INFOPANEL_TAB_LISTDESC_CREWEQUIPS),
         text_styles.main(VEHICLE_PREVIEW.INFOPANEL_TAB_LISTDESC_CREWSKILLSEQUIPS))
        hasSkillBonuses = any(tMan.skills for _, tMan in vehicle.crew)
        hasEquipBonuses = any(itertools.chain(vehicle.optDevices.installed, vehicle.battleAbilities.installed, vehicle.battleBoosters.installed, (rCons and rCons.getKpi() for rCons in vehicle.consumables.installed), (
         vehicle.hasOutfit(vehicle.getAnyOutfitSeason()),)))
        return descriptions[hasEquipBonuses << 1 | hasSkillBonuses]

    def _getBackBtnLabel(self):
        if self._backBtnLabel:
            return self._backBtnLabel
        else:
            if self._backAlias and self._backAlias in _BACK_BTN_LABELS:
                backBtnLabel = _BACK_BTN_LABELS[self._backAlias]
                if not backBtnLabel:
                    return None
                return VEHICLE_PREVIEW.getBackBtnLabel(_BACK_BTN_LABELS[self._backAlias])
            return VEHICLE_PREVIEW.HEADER_BACKBTN_DESCRLABEL_HANGAR

    def _getPrbEntityType(self):
        prbDispatcher = g_prbLoader.getDispatcher()
        if not prbDispatcher:
            return QUEUE_TYPE.UNKNOWN
        else:
            entity = prbDispatcher.getEntity()
            if entity is not None:
                return entity.getQueueType()
            return QUEUE_TYPE.UNKNOWN

    def __onHangarCreateOrRefresh(self):
        if self._getPrbEntityType() in (QUEUE_TYPE.BATTLE_ROYALE, QUEUE_TYPE.BATTLE_ROYALE_TOURNAMENT):
            self.closeView()
            return
        self.__keepVehicleSelectionEnabled = True
        self.__handleWindowClose()
        return

    @event_bus_handlers.eventBusHandler(events.HideWindowEvent.HIDE_VEHICLE_PREVIEW, EVENT_BUS_SCOPE.LOBBY)
    def __handleWindowClose(self, event=None):
        if event is not None:
            if event.ctx.get(b'back', True):
                self.onBackClick()
            elif event.ctx.get(b'close', False):
                self.closeView()
        self.destroy()
        return

    def _processBackClick(self, ctx=None):
        if self._previewBackCb:
            self._previewBackCb()
        elif self._backAlias == VIEW_ALIAS.LOBBY_RESEARCH and g_currentPreviewVehicle.isPresent():
            event_dispatcher.showResearchView(self._vehicleCD, exitEvent=getTechTreeLoadEvent(g_currentPreviewVehicle.item.nationName))
        elif self._backAlias == VIEW_ALIAS.VEHICLE_PREVIEW:
            entity = ctx.get(b'entity', None) if ctx else None
            if entity:
                compactDescr = entity.typeDescriptor.type.compactDescr
                if self._itemsCache.items.inventory.getItemData(compactDescr) is not None:
                    event_dispatcher.showHangar()
                else:
                    event_dispatcher.showVehiclePreview(compactDescr, previewAlias=self._previousBackAlias)
            else:
                event_dispatcher.showHangar()
        elif self._backAlias == VIEW_ALIAS.LOBBY_STORE:
            showShop()
        elif self._backAlias == WulfPreviewAlias.WULF_TECHTREE:
            event_dispatcher.showVehicleTechTreeView()
        elif self._backAlias == VIEW_ALIAS.STRONGHOLD_PROGRESSION:
            event_dispatcher.showStrongholds(getStrongholdEventProgressionUrl())
        else:
            event = g_entitiesFactories.makeLoadEvent(SFViewLoadParams(self._backAlias), {b'isBackEvent': True})
            self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _onInventoryChanged(self, *_):
        if not BuyVehicleWindow.getInstances():
            g_currentPreviewVehicle.selectNoVehicle()
            event_dispatcher.showHangar()
        return

    def __onOfferChanged(self, event):
        self.__currentOffer = event.ctx.get(b'offer')
        return

    def __updateModuleBullet(self):
        self.as_setBulletVisibilityS(_getModulesTabIdx(), _isPostProgressionBulletVisible())
        return

    def _resetPostProgressionBullet(self):
        if _isPostProgressionBulletVisible(settingsCore=self.__settingsCore):
            self.__settingsCore.serverSettings.saveInUIStorage({(UI_STORAGE_KEYS.VEH_PREVIEW_POST_PROGRESSION_BULLET_SHOWN): True})
            self.__updateModuleBullet()
        return
