import constants, gui
from PlayerEvents import g_playerEvents
from frameworks.wulf import WindowLayer
from gui import SystemMessages
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview_constants import VEHICLE_PREVIEW_ALIASES
from gui.Scaleform.daapi.view.lobby.UiEffectsManager import UiEffectsManager
from gui.Scaleform.daapi.view.meta.LobbyPageMeta import LobbyPageMeta
from gui.Scaleform.framework.entities.View import View, ViewKey, ViewKeyDynamic
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler, ViewLifecycleWatcher
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from gui.shared.events import LoadViewEvent, ViewEventType
from helpers import dependency, i18n, uniprof
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from skeletons.gui.app_loader import IWaitingWidget
from skeletons.gui.game_control import IIGRController, IMapsTrainingController, IArmoryYardController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.gui.impl import IGuiLoader
from uilogging.rename_testing.loggers import RenameTestingUILogger

class _LobbySubViewsLifecycleHandler(IViewLifecycleHandler):
    __WAITING_LBL = b'loadPage'
    __SUB_VIEWS = (
     VIEW_ALIAS.LOBBY_HANGAR,
     VIEW_ALIAS.LOBBY_STORE,
     VIEW_ALIAS.LOBBY_STORAGE,
     VIEW_ALIAS.STORAGE_RESTORE_DEVICES_VIEW,
     VIEW_ALIAS.LOBBY_PROFILE,
     VIEW_ALIAS.LOBBY_BARRACKS,
     PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY,
     PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY,
     VIEW_ALIAS.LOBBY_CUSTOMIZATION,
     VIEW_ALIAS.IMAGE_VIEW,
     VIEW_ALIAS.VEHICLE_PREVIEW,
     VIEW_ALIAS.STYLE_PREVIEW,
     VIEW_ALIAS.VEHICLE_COMPARE,
     VIEW_ALIAS.LOBBY_PERSONAL_MISSIONS,
     PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATIONS,
     PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_AWARD_VIEW_ALIAS,
     PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_VIEW_ALIAS,
     PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS,
     PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATION_AWARDS_SCREEN_ALIAS,
     VIEW_ALIAS.VEHICLE_COMPARE_MAIN_CONFIGURATOR,
     VIEW_ALIAS.LOBBY_RESEARCH,
     VIEW_ALIAS.BATTLE_QUEUE,
     VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE,
     VIEW_ALIAS.EVENT_BATTLE_QUEUE,
     RANKEDBATTLES_ALIASES.RANKED_BATTLES_VIEW_ALIAS)
    __WULF_SUB_VIEWS = (
     R.views.lobby.techtree.VehicleTechTree(),)

    def __init__(self):
        monitoredViews = [ViewKey(alias) for alias in self.__SUB_VIEWS]
        monitoredViews.extend(ViewKeyDynamic(layoutID) for layoutID in self.__WULF_SUB_VIEWS)
        super(_LobbySubViewsLifecycleHandler, self).__init__(monitoredViews)
        self.__loadingSubViews = set()
        self.__isWaitingVisible = False
        return

    def onViewLoading(self, view):
        if view.key not in self.__loadingSubViews:
            self.__loadingSubViews.add(view.key)
            self.__invalidateWaitingStatus()
        return

    def onViewCreated(self, view):
        if view.key in self.__loadingSubViews:
            self.__loadingSubViews.remove(view.key)
            self.__invalidateWaitingStatus()
        return

    def onViewDestroyed(self, view):
        if view.key in self.__loadingSubViews:
            self.__loadingSubViews.remove(view.key)
            self.__invalidateWaitingStatus()
        return

    def __invalidateWaitingStatus(self):
        if self.__loadingSubViews:
            if not self.__isWaitingVisible:
                self.__isWaitingVisible = True
                Waiting.show(self.__WAITING_LBL)
        elif self.__isWaitingVisible:
            self.__isWaitingVisible = False
            Waiting.hide(self.__WAITING_LBL)
        return


class LobbyView(LobbyPageMeta, IWaitingWidget):

    class COMPONENTS(object):
        HEADER = b'lobbyHeader'

    itemsCache = dependency.descriptor(IItemsCache)
    igrCtrl = dependency.descriptor(IIGRController)
    lobbyContext = dependency.descriptor(ILobbyContext)
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)
    armoryYardController = dependency.descriptor(IArmoryYardController)
    gui = dependency.descriptor(IGuiLoader)

    def __init__(self, ctx=None):
        super(LobbyView, self).__init__(ctx)
        self.__currIgrType = constants.IGR_TYPE.NONE
        self.__viewLifecycleWatcher = ViewLifecycleWatcher()
        self._entityEnqueueCancelCallback = None
        self._UiEffectsManager = UiEffectsManager()
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    def showWaiting(self, message, _=False):
        self.as_showWaitingS(backport.text(message))
        return

    def hideWaiting(self):
        self.as_hideWaitingS()
        return

    def moveSpace(self, dx, dy, dz):
        self.fireEvent(CameraRelatedEvents(CameraRelatedEvents.LOBBY_VIEW_MOUSE_MOVE, ctx={b'dx': dx, b'dy': dy, b'dz': dz}))
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_SPACE_MOVED, ctx={b'dx': dx, b'dy': dy, b'dz': dz}))
        return

    def notifyCursorOver3dScene(self, isOver3dScene):
        if self.mapsTrainingController.isMapsTrainingPrbActive:
            container = self.app.containerManager.getContainer(WindowLayer.SUB_VIEW)
            view = container.getView()
            if view and view.alias not in VEHICLE_PREVIEW_ALIASES:
                return
        if self.armoryYardController.isSceneLoaded() and not isOver3dScene:
            return
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={b'isOver3dScene': isOver3dScene}))
        return

    def notifyCursorDragging(self, isDragging):
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_DRAGGING, ctx={b'isDragging': isDragging}))
        return

    @uniprof.regionDecorator(label=b'account.show_gui', scope=b'enter')
    def _populate(self):
        View._populate(self)
        self.__currIgrType = self.igrCtrl.getRoomType()
        g_prbLoader.setEnabled(True)
        self.addListener(events.LobbySimpleEvent.SHOW_HELPLAYOUT, self.__showHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.LobbySimpleEvent.CLOSE_HELPLAYOUT, self.__closeHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_LOBBY_SUB_CONTAINER_ITEMS, self.__hideSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.REVEAL_LOBBY_SUB_CONTAINER_ITEMS, self.__revealSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.LobbyInterfaceEvent.TOGGLE_VISIBILITY, self.__onToggleVisibility, scope=EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onEntityCheckOutEnqueued += self._onEntityCheckoutEnqueued
        g_playerEvents.onAccountBecomeNonPlayer += self._onAccountBecomeNonPlayer
        viewLifecycleHandler = _LobbySubViewsLifecycleHandler()
        self.__viewLifecycleWatcher.start(self.app.containerManager, [viewLifecycleHandler])
        self.igrCtrl.onIgrTypeChanged += self.__onIgrTypeChanged
        battlesCount = self.itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount()
        epicBattlesCount = self.itemsCache.items.getAccountDossier().getEpicBattleStats().getBattlesCount()
        self.lobbyContext.updateBattlesCount(battlesCount, epicBattlesCount)
        self.fireEvent(events.GUICommonEvent(events.GUICommonEvent.LOBBY_VIEW_LOADED))
        RenameTestingUILogger().logHangarEnter()
        self.bwProto.voipController.invalidateMicrophoneMute()
        self._UiEffectsManager.populate(app=self.app)
        return

    def _invalidate(self, *args, **kwargs):
        g_prbLoader.setEnabled(True)
        super(LobbyView, self)._invalidate(*args, **kwargs)
        return

    @uniprof.regionDecorator(label=b'account.show_gui', scope=b'exit')
    def _dispose(self):
        self.igrCtrl.onIgrTypeChanged -= self.__onIgrTypeChanged
        self.__viewLifecycleWatcher.stop()
        g_playerEvents.onEntityCheckOutEnqueued -= self._onEntityCheckoutEnqueued
        g_playerEvents.onAccountBecomeNonPlayer -= self._onAccountBecomeNonPlayer
        if self._entityEnqueueCancelCallback:
            self._entityEnqueueCancelCallback = None
            g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self._onEntityCheckoutCanceled, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.LobbySimpleEvent.SHOW_HELPLAYOUT, self.__showHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.LobbySimpleEvent.CLOSE_HELPLAYOUT, self.__closeHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_LOBBY_SUB_CONTAINER_ITEMS, self.__hideSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.REVEAL_LOBBY_SUB_CONTAINER_ITEMS, self.__revealSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self._UiEffectsManager.dispose()
        self.removeListener(events.LobbyInterfaceEvent.TOGGLE_VISIBILITY, self.__onToggleVisibility, scope=EVENT_BUS_SCOPE.LOBBY)
        View._dispose(self)
        return

    def _onEntityCheckoutEnqueued(self, cancelCallback):
        g_eventBus.addListener(ViewEventType.LOAD_VIEW, self._onEntityCheckoutCanceled, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.handleEvent(LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_QUEUE_DIALOG_SHOW)), EVENT_BUS_SCOPE.LOBBY)
        self._entityEnqueueCancelCallback = cancelCallback
        return

    def _onEntityCheckoutCanceled(self, event):
        if event.alias == VIEW_ALIAS.BOOTCAMP_QUEUE_DIALOG_CANCEL:
            g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self._onEntityCheckoutCanceled, EVENT_BUS_SCOPE.LOBBY)
            if self._entityEnqueueCancelCallback:
                self._entityEnqueueCancelCallback()
            self._entityEnqueueCancelCallback = None
        return

    def _onAccountBecomeNonPlayer(self):
        self._entityEnqueueCancelCallback = None
        g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self._onEntityCheckoutCanceled, EVENT_BUS_SCOPE.LOBBY)
        return

    def __showHelpLayout(self, _):
        self.as_showHelpLayoutS()
        return

    def __closeHelpLayout(self, _):
        self.as_closeHelpLayoutS()
        return

    def __handleScreenShotMade(self, event):
        if b'path' not in event.ctx:
            return
        SystemMessages.pushMessage(i18n.makeString(b'#menu:screenshot/save') % {b'path': (event.ctx[b'path'])}, SystemMessages.SM_TYPE.Information)
        return

    def __hideSubContainerItems(self, _):
        self.as_setSubContainerItemsVisibilityS(False)
        return

    def __revealSubContainerItems(self, _):
        self.as_setSubContainerItemsVisibilityS(True)
        return

    def __onIgrTypeChanged(self, roomType, xpFactor):
        icon = gui.makeHtmlString(b'html_templates:igr/iconSmall', b'premium')
        if roomType == constants.IGR_TYPE.PREMIUM:
            SystemMessages.pushMessage(i18n.makeString(SYSTEM_MESSAGES.IGR_CUSTOMIZATION_BEGIN, igrIcon=icon), type=SystemMessages.SM_TYPE.Information)
        elif roomType in [constants.IGR_TYPE.BASE, constants.IGR_TYPE.NONE] and self.__currIgrType == constants.IGR_TYPE.PREMIUM:
            SystemMessages.pushMessage(i18n.makeString(SYSTEM_MESSAGES.IGR_CUSTOMIZATION_END, igrIcon=icon), type=SystemMessages.SM_TYPE.Information)
        self.__currIgrType = roomType
        return

    def __onToggleVisibility(self, event):
        headerIsVisible = event.ctx.get(b'headerIsVisible', True)
        messengerBarVisible = event.ctx.get(b'messengerBarVisible', True)
        ignoreTopOffset = event.ctx.get(b'ignoreTopOffset', False)
        self.as_setInterfaceVisibleS({b'headerIsVisible': headerIsVisible, 
           b'messengerBarVisible': messengerBarVisible, 
           b'ignoreTopOffset': ignoreTopOffset})
        return
