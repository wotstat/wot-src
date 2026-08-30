from functools import partial
import BigWorld
from adisp import adisp_process
from constants import PremiumConfigs
from debug_utils import LOG_ERROR
from frameworks.wulf import ViewStatus
from gui import DialogsInterface, makeHtmlString
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_maintenance import EventBoardsMaintenance
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import checkEventExist
from gui.Scaleform.daapi.view.meta.CurrentVehicleMissionsViewMeta import CurrentVehicleMissionsViewMeta
from gui.Scaleform.daapi.view.meta.MissionsEventBoardsViewMeta import MissionsEventBoardsViewMeta
from gui.Scaleform.daapi.view.meta.MissionsGroupedViewMeta import MissionsGroupedViewMeta
from gui.Scaleform.daapi.view.meta.MissionsMarathonViewMeta import MissionsMarathonViewMeta
from gui.Scaleform.daapi.view.meta.TemporaryMissionsViewMeta import TemporaryMissionsViewMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.event_boards.settings import expandGroup, isGroupMinimized
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.summer_sale.summer_sale_main_view import SummerSaleMainView
from gui.server_events import caches, settings
from gui.server_events.events_dispatcher import hideMissionDetails, showMissionsCategories, showMissionsTemporary
from gui.server_events.events_helpers import isCosmicQuest, isDailyQuest, isDebutBoxesQuest, isMarathon, isPremium
from gui.shared import actions, events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showDebutBoxesInfoPage, showTankPremiumAboutPage, showSummerSaleInfoPage, showShop
from gui.shared.formatters import icons, text_styles
from helpers import dependency
from helpers.events_handler import EventsHandler
from helpers.i18n import makeString as _ms
from shared_utils import nextTick
from skeletons.gui.game_control import IBrowserController, IDebutBoxesController, IMarathonEventsController, IReloginController, ISummerSaleController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from th_async import th_async, th_await
from uilogging.marathon.loggers import MarathonLogger, MarathonEvents

class _GroupedMissionsView(MissionsGroupedViewMeta):

    def clickActionBtn(self, actionID):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_STORE), ctx={b'tabId': (STORE_CONSTANTS.STORE_ACTIONS)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def expand(self, gID, value):
        settings.expandGroup(gID, value)
        if self._questsDP is not None:
            for blockData in self._questsDP.collection:
                if blockData.get(b'blockId') == gID:
                    blockData[b'isCollapsed'] = settings.isGroupMinimized(gID)

        return


class MissionsGroupedView(_GroupedMissionsView):
    __debutBoxesController = dependency.descriptor(IDebutBoxesController)

    def dummyClicked(self, eventType):
        if eventType == b'OpenCategoriesEvent':
            showMissionsCategories()
        else:
            super(MissionsGroupedView, self).dummyClicked(eventType)
        return

    def _populate(self):
        self.__debutBoxesController.onStateChanged += self._onEventsUpdate
        super(MissionsGroupedView, self)._populate()
        return

    def _dispose(self):
        self.__debutBoxesController.onStateChanged -= self._onEventsUpdate
        super(MissionsGroupedView, self)._dispose()
        return

    @staticmethod
    def _getBackground():
        return RES_ICONS.MAPS_ICONS_MISSIONS_BACKGROUNDS_MARATHONS

    @staticmethod
    def _getDummy():
        return {b'iconSource': (RES_ICONS.MAPS_ICONS_LIBRARY_ALERTBIGICON), 
           b'htmlText': (text_styles.main(_ms(QUESTS.MISSIONS_NOTASKSMARATHON_DUMMY_TEXT))), 
           b'alignCenter': False, 
           b'btnVisible': True, 
           b'btnLabel': b'', 
           b'btnTooltip': b'', 
           b'btnEvent': b'OpenCategoriesEvent', 
           b'btnLinkage': (BUTTON_LINKAGES.BUTTON_LINK)}

    def _getViewQuestFilter(self):
        return (lambda q: isMarathon(q.getGroupID()) or isDebutBoxesQuest(q.getID(), debutBoxesController=self.__debutBoxesController))

    def onClickInfoBtn(self, eventType):
        if eventType == QUESTS_ALIASES.DEBUT_BOXES_EVENT:
            showDebutBoxesInfoPage(self.__debutBoxesController.getInfoPageUrl())
        return


class MissionsMarathonView(MissionsMarathonViewMeta):
    _browserCtrl = dependency.descriptor(IBrowserController)
    _marathonsCtrl = dependency.descriptor(IMarathonEventsController)
    eventsCache = dependency.descriptor(IEventsCache)
    __slots__ = (b'__marathonLogger',)

    def __init__(self):
        super(MissionsMarathonView, self).__init__()
        self.__browserID = None
        self._marathonEvent = self._marathonsCtrl.getMarathon(caches.getNavInfo().getMarathonPrefix()) or self._marathonsCtrl.getPrimaryMarathon()
        self._width = 0
        self._height = 0
        self._builder = None
        self.__loadBrowserCallbackID = None
        self.__browserView = None
        self.__marathonLogger = MarathonLogger()
        return

    def closeView(self):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_HANGAR)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def getSuitableEvents(self):
        return []

    @adisp_process
    def reload(self):
        browser = self._browserCtrl.getBrowser(self.__browserID)
        if browser is not None and self._marathonEvent and self.__browserView:
            url = yield self._marathonEvent.getUrl()
            if url:
                self.__browserView.showLoading(True)
                browser.navigate(url)
                self.__marathonLogger.logEnter(MarathonEvents.OPEN_PAGE)
        else:
            yield lambda callback: callback(True)
        return

    def setActive(self, value):
        self.reload()
        return

    def setBuilder(self, builder, filterData, eventID):
        self._builder = builder
        self._onEventsUpdate()
        return

    def setMarathon(self, prefix):
        self._marathonEvent = self._marathonsCtrl.getMarathon(prefix)
        return

    def viewSize(self, width, height):
        self._width = width
        self._height = height
        return

    def markVisited(self):
        return

    @adisp_process
    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == VIEW_ALIAS.BROWSER and self._marathonEvent:
            if self.__browserID is None:
                url = yield self._marathonEvent.getUrl()
                browserID = yield self._browserCtrl.load(url=url, useBrowserWindow=False, browserID=self.__browserID, browserSize=(
                 self._width, self._height))
                self.__browserID = browserID
                viewPy.init(browserID, self._marathonEvent.createMarathonWebHandlers(), alias=alias)
                self.__browserView = viewPy
                self.__browserView.showContentUnderLoading = False
                self.__updateBrowserProperties()
            else:
                LOG_ERROR(b'Attampt to initialize browser 2nd time!')
        return

    @th_async
    def _onEventsUpdate(self, *args):
        yield th_await(self.eventsCache.prefetcher.demand())
        if self._builder:
            self.__updateEvents()
        return

    def _populate(self):
        super(MissionsMarathonView, self)._populate()
        self._marathonEvent.showRewardVideo()
        Waiting.hide(b'loadPage')
        self.__loadBrowserCallbackID = BigWorld.callback(0.01, self.__loadBrowser)
        g_eventBus.addListener(events.MissionsEvent.ON_TAB_CHANGED, self.__updateBrowserProperties, EVENT_BUS_SCOPE.LOBBY)
        self.__marathonLogger.logEnter(MarathonEvents.OPEN_PAGE)
        return

    def _dispose(self):
        g_eventBus.removeListener(events.MissionsEvent.ON_TAB_CHANGED, self.__updateBrowserProperties, EVENT_BUS_SCOPE.LOBBY)
        self.__cancelLoadBrowserCallback()
        self.__browserView = None
        super(MissionsMarathonView, self)._dispose()
        return

    def __cancelLoadBrowserCallback(self):
        if self.__loadBrowserCallbackID is not None:
            BigWorld.cancelCallback(self.__loadBrowserCallbackID)
            self.__loadBrowserCallbackID = None
        return

    def __loadBrowser(self):
        self.__loadBrowserCallbackID = None
        self.as_loadBrowserS()
        return

    def __updateEvents(self):
        self._builder.invalidateBlocks()
        return

    def __updateBrowserProperties(self, *args):
        self.__viewActive = caches.getNavInfo().getMissionsTab() == QUESTS_ALIASES.MISSIONS_MARATHON_VIEW_PY_ALIAS
        browser = self._browserCtrl.getBrowser(self.__browserID)
        if browser:
            if self.__viewActive:
                browser.skipEscape = not self._marathonEvent.isNeedHandlingEscape
                browser.useSpecialKeys = False
            else:
                browser.skipEscape = False
                browser.useSpecialKeys = True
        return


class MissionsEventBoardsView(MissionsEventBoardsViewMeta):

    def __init__(self):
        super(MissionsEventBoardsView, self).__init__()
        self.__eventsData = None
        self.__tableView = None
        self.__maintenance = None
        return

    @checkEventExist
    def orderClick(self, eventID):
        ctx = {b'eventID': eventID, b'title': (_ms(EVENT_BOARDS.ORDERS_TITLE)), 
           b'url': (self.__eventsData.getEvent(eventID).getManual())}
        self.__openDetailsContainer(EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_BROWSER_VIEW, ctx)
        return

    @checkEventExist
    def techniqueClick(self, eventID):
        ctx = {b'eventID': eventID}
        self.__openDetailsContainer(EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_VEHICLES_VIEW, ctx)
        return

    @checkEventExist
    def awardClick(self, eventID):
        ctx = {b'eventID': eventID}
        self.__openDetailsContainer(EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_AWARDS_LINKAGE, ctx)
        return

    @adisp_process
    def serverClick(self, eventID, serverID):

        def doJoin():
            from gui.Scaleform.framework import g_entitiesFactories
            g_eventBus.handleEvent(g_entitiesFactories.makeLoadEvent(SFViewLoadParams(b'missions')), scope=EVENT_BUS_SCOPE.LOBBY)
            return

        reloginCtrl = dependency.instance(IReloginController)
        success = yield DialogsInterface.showI18nConfirmDialog(b'changePeriphery')
        if success:
            reloginCtrl.doRelogin(int(serverID), extraChainSteps=(
             actions.OnLobbyInitedAction(onInited=doJoin),))
        return

    @checkEventExist
    @adisp_process
    def registrationClick(self, eventID):
        self.as_setWaitingVisibleS(True)
        yield self.eventsController.joinEvent(eventID)
        self.as_setWaitingVisibleS(False)
        self._onEventsUpdate()
        return

    @checkEventExist
    @adisp_process
    def participateClick(self, eventID):
        eventData = self.__eventsData.getEvent(eventID)
        started = eventData.isStarted()
        self.as_setWaitingVisibleS(True)
        dialog = b'leaveEvent' if started else b'leaveStartedEvent'
        success = yield DialogsInterface.showI18nConfirmDialog(dialog, ctx={b'warning': (makeHtmlString(b'html_templates:lobby/dialogs', b'leaveEventWarning', {b'message': (backport.text(R.strings.dialogs.leaveEvent.message.warning()))}))})
        if success:
            yield self.eventsController.leaveEvent(eventID)
            yield self._onEventsUpdateAsync()
        self.as_setWaitingVisibleS(False)
        return

    @checkEventExist
    def expand(self, gID, value):
        event = self.__eventsData.getEvent(gID)
        expandGroup(event, value)
        if self._questsDP is not None:
            for blockData in self._questsDP.collection:
                if blockData.get(b'blockId') == gID:
                    blockData[b'isCollapsed'] = isGroupMinimized(event)

        return

    def onRefresh(self):
        self._onEventsUpdate()
        return

    def _populate(self):
        super(MissionsEventBoardsView, self)._populate()
        self.__eventsData = self.eventsController.getEventsSettingsData()
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        return

    def _dispose(self):
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        if self.__maintenance:
            self.__maintenance.onRefresh -= self.onRefresh
        super(MissionsEventBoardsView, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(MissionsEventBoardsView, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, EventBoardsMaintenance):
            self.__maintenance = viewPy
            viewPy.onRefresh += self.onRefresh
        return

    def _invalidate(self, *args, **kwargs):
        super(MissionsEventBoardsView, self)._invalidate(*args, **kwargs)
        if self.__tableView is not None:
            self.__tableView.destroy()
        return

    @staticmethod
    def _getBackground():
        return RES_ICONS.MAPS_ICONS_MISSIONS_BACKGROUNDS_MARATHONS

    def _setMaintenance(self, visible):
        headerText = icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ALERTICON) + _ms(EVENT_BOARDS.MAINTENANCE_TITLE)
        bodyText = _ms(EVENT_BOARDS.MAINTENANCE_BODY)
        buttonText = _ms(EVENT_BOARDS.MAINTENANCE_UPDATE)
        self.as_setMaintenanceS(visible, headerText, bodyText, buttonText)
        return

    @checkEventExist
    def __onFilterApply(self, eventID, leaderboardsID):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_EVENT_BOARDS_TABLE), ctx={b'eventID': eventID, b'leaderboardID': (int(leaderboardsID))}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __onViewLoaded(self, view, *args, **kwargs):
        if view.alias in (EVENTBOARDS_ALIASES.RESULT_FILTER_POPOVER_ALIAS,
         EVENTBOARDS_ALIASES.RESULT_FILTER_POPOVER_VEHICLES_ALIAS):
            if view.caller == b'missions':
                eventID = view.eventID
                eventData = self.__eventsData.getEvent(eventID)
                if eventData is not None:
                    view.setData(eventData, partial(self.__onFilterApply, eventID))
                else:
                    view.destroy()
                    self._setMaintenance(True)
        elif view.alias == VIEW_ALIAS.LOBBY_EVENT_BOARDS_TABLE:
            self.__tableView = view
            view.onDisposed += self.__tableViewDisposed
        return

    @adisp_process
    def __tableViewDisposed(self, view):
        self.as_setPlayFadeInTweenEnabledS(False)
        view.onDisposed -= self.__tableViewDisposed
        self.__tableView = None
        hideMissionDetails()
        yield self._onEventsUpdateAsync()
        self.as_scrollToItemS(b'blockId', view.getEventID())
        return

    def __openDetailsContainer(self, viewAlias, ctx=None):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(viewAlias), ctx=ctx), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class MissionsCategoriesView(_GroupedMissionsView):
    _lobbyContext = dependency.descriptor(ILobbyContext)
    __summerSaleController = dependency.descriptor(ISummerSaleController)
    __showDQInMissionsTab = False

    @classmethod
    def setShowDQInMissionsTab(cls, value):
        cls.__showDQInMissionsTab = value
        return

    @staticmethod
    def getViewQuestFilter():
        return (lambda q: not (isMarathon(q.getGroupID()) or isPremium(q.getGroupID()) or isDailyQuest(q.getID()) or isDebutBoxesQuest(q.getID()) or isCosmicQuest(q.getID())))

    @staticmethod
    def getViewQuestFilterIncludingDailyQuests():
        viewQuestFilter = MissionsCategoriesView.getViewQuestFilter()
        return (lambda q: viewQuestFilter(q) or isPremium(q.getGroupID()) or isDailyQuest(q.getID()))

    def onClickButtonDetails(self):
        showTankPremiumAboutPage()
        return

    def onClickInfoBtn(self, eventType):
        if eventType == QUESTS_ALIASES.SUMMER_SALE_EVENT:
            showSummerSaleInfoPage()
        return

    def onClickOpenShopBtn(self, eventType):
        if eventType == QUESTS_ALIASES.SUMMER_SALE_EVENT:
            showShop(self.__summerSaleController.getShopPageUrl())
        return

    def onClickOpenEventBtn(self, eventType):
        if eventType == QUESTS_ALIASES.SUMMER_SALE_EVENT:
            showMissionsTemporary()
        return

    def _populate(self):
        super(MissionsCategoriesView, self)._populate()
        self._lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        return

    def _dispose(self):
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        super(MissionsCategoriesView, self)._dispose()
        return

    @staticmethod
    def _getBackground():
        return RES_ICONS.MAPS_ICONS_MISSIONS_BACKGROUNDS_CATEGORIES

    def _getViewQuestFilter(self):
        return self.getViewQuestFilter()

    def __onServerSettingsChange(self, diff):
        if PremiumConfigs.PREM_QUESTS not in diff:
            return
        diffConfig = diff.get(PremiumConfigs.PREM_QUESTS)
        if b'enabled' in diffConfig:
            self._onEventsUpdate()
        return


class TemporaryMissionsTabView(InjectComponentAdaptor, TemporaryMissionsViewMeta, EventsHandler):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __VIEW = {(R.views.lobby.summer_sale.SummerSaleMainView()): SummerSaleMainView}

    @nextTick
    def updateState(self, *args, **kwargs):
        layoutID = kwargs.get(b'layoutID', R.invalid())
        if layoutID == R.invalid():
            layoutID = self.__getDefaultLayoutID()
        self._destroyInjected()
        self._createInjectView(layoutID)
        return

    def markVisited(self):
        return

    def _populate(self):
        super(TemporaryMissionsTabView, self)._populate()
        self._subscribe()
        return

    def _dispose(self):
        self._unsubscribe()
        super(TemporaryMissionsTabView, self)._dispose()
        return

    def _addInjectContentListeners(self):
        self._injectView.onStatusChanged += self.__onViewStatusChanged
        return

    def _removeInjectContentListeners(self):
        self._injectView.onStatusChanged -= self.__onViewStatusChanged
        return

    def _makeInjectView(self, layoutID=R.invalid()):
        if layoutID == R.invalid():
            layoutID = self.__getDefaultLayoutID()
        return self.__VIEW[layoutID](layoutID)

    def __getDefaultLayoutID(self):
        return R.views.lobby.summer_sale.SummerSaleMainView()

    def __onViewStatusChanged(self, state):
        if state == ViewStatus.LOADED:
            self.as_showViewS()
        self.as_setWaitingVisibleS(state not in (ViewStatus.LOADED, ViewStatus.DESTROYED))
        return


class CurrentVehicleMissionsView(CurrentVehicleMissionsViewMeta):

    def setBuilder(self, builder, filters, eventId):
        super(CurrentVehicleMissionsView, self).setBuilder(builder, filters, eventId)
        self._builder.onBlocksDataChanged += self.__onBlocksDataChanged
        return

    @staticmethod
    def _getBackground():
        return RES_ICONS.MAPS_ICONS_MISSIONS_BACKGROUNDS_CURRENTVEHICLE

    def _dispose(self):
        self._builder.onBlocksDataChanged -= self.__onBlocksDataChanged
        super(CurrentVehicleMissionsView, self)._dispose()
        return

    def __onBlocksDataChanged(self):
        self._builder.invalidateBlocks()
        self._filterMissions()
        self._onDataChangedNotify()
        return
