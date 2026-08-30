from __future__ import absolute_import
import logging, typing, constants, gui
from frameworks.wulf import WindowLayer
from gui import SystemMessages
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VEHICLE_PREVIEW_ALIASES
from gui.Scaleform.daapi.view.meta.LobbyPageMeta import LobbyPageMeta
from gui.Scaleform.framework.entities.View import View, ViewKey, ViewKeyDynamic
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler, ViewLifecycleWatcher
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared.system_factory import registerLifecycleHandledSubViews, collectLifecycleHandledSubViews, collectViewsForMonitoring, collectDynamicViewsForMonitoring
from helpers import dependency, i18n, uniprof
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from skeletons.gui.app_loader import IWaitingWidget
from skeletons.gui.game_control import IIGRController, IMapsTrainingController, IWalletController, IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.impl.pub.view_component import ViewComponent
_logger = logging.getLogger(__name__)
registerLifecycleHandledSubViews([
 VIEW_ALIAS.LOBBY_HANGAR,
 VIEW_ALIAS.LEGACY_LOBBY_HANGAR,
 VIEW_ALIAS.LOBBY_STORE,
 VIEW_ALIAS.LOBBY_STORAGE,
 VIEW_ALIAS.LOBBY_PROFILE,
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
 PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS,
 PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATION_AWARDS_SCREEN_ALIAS,
 VIEW_ALIAS.VEHICLE_COMPARE_MAIN_CONFIGURATOR,
 VIEW_ALIAS.LOBBY_TECHTREE,
 VIEW_ALIAS.BATTLE_QUEUE,
 VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_VIEW_ALIAS,
 VIEW_ALIAS.VEHICLE_HUB,
 VIEW_ALIAS.POST_BATTLE_RESULTS,
 VIEW_ALIAS.USER_MISSIONS_HUB_CONTAINER])

class _LobbySubViewsLifecycleHandler(IViewLifecycleHandler):
    __WAITING_LBL = b'loadPage'
    __DYNAMIC_VIEWS = (
     R.views.lobby.dog_tags.AnimatedDogTagsView(),)

    def __init__(self):
        super(_LobbySubViewsLifecycleHandler, self).__init__([ViewKey(alias) for alias in collectLifecycleHandledSubViews() + collectViewsForMonitoring()] + [ViewKeyDynamic(alias) for alias in list(self.__DYNAMIC_VIEWS) + collectDynamicViewsForMonitoring()])
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


class LobbyPanelInjector(InjectComponentAdaptor, IGlobalListener):

    def __init__(self):
        super(LobbyPanelInjector, self).__init__()
        self._viewType = self._getViewType()
        return

    def onPrbEntitySwitched(self):
        self._viewType = self._getViewType()
        if self._injectView is None or type(self._injectView) is self._viewType:
            return
        self._destroyInjected()
        self._createInjectView()
        return

    def destroy(self):
        self.stopGlobalListening()
        super(LobbyPanelInjector, self).destroy()
        return

    def _populate(self):
        super(LobbyPanelInjector, self)._populate()
        self.startGlobalListening()
        return

    def _makeInjectView(self):
        return self._viewType()

    def _getViewType(self):
        raise NotImplementedError
        return


class LobbyHeaderInject(LobbyPanelInjector):
    _hangarGuiCtrl = dependency.descriptor(IHangarGuiController)

    def _getViewType(self):
        controlsHelper = self._hangarGuiCtrl.currentGuiProvider.getLobbyHeaderHelper()
        if controlsHelper is not None:
            return controlsHelper.getHeaderType()
        else:
            return


class LobbyFooterInject(LobbyPanelInjector):
    _hangarGuiCtrl = dependency.descriptor(IHangarGuiController)

    def _getViewType(self):
        controlsHelper = self._hangarGuiCtrl.currentGuiProvider.getLobbyHeaderHelper()
        if controlsHelper is not None:
            return controlsHelper.getFooterType()
        else:
            return


class LobbyView(LobbyPageMeta, IWaitingWidget, IGlobalListener):
    itemsCache = dependency.descriptor(IItemsCache)
    igrCtrl = dependency.descriptor(IIGRController)
    lobbyContext = dependency.descriptor(ILobbyContext)
    wallet = dependency.descriptor(IWalletController)
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)

    def __init__(self, ctx=None):
        super(LobbyView, self).__init__(ctx)
        self.__currIgrType = constants.IGR_TYPE.NONE
        self.__viewLifecycleWatcher = ViewLifecycleWatcher()
        self.__oldStyleViewMode = False
        return

    def create(self):
        super(LobbyView, self).create()
        accAttrs = self.itemsCache.items.stats.attributes
        battle_selector_items.create()
        battle_selector_items.getItems().validateAccountAttrs(accAttrs)
        self.startGlobalListening()
        g_prbLoader.setEnabled(True)
        self.fireEvent(events.GUICommonEvent(events.GUICommonEvent.LOBBY_VIEW_LOADED))
        Waiting.hide(b'enter')
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    def showWaiting(self, messageID, softStart=False, showBg=True):
        self.as_showWaitingS(backport.text(messageID))
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
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={b'isOver3dScene': isOver3dScene}))
        return

    def notifyCursorDragging(self, isDragging):
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_DRAGGING, ctx={b'isDragging': isDragging}))
        return

    def setRequiresOldStyle(self, value):
        if self.__oldStyleViewMode == value:
            return
        self.__oldStyleViewMode = value
        self._updateRequiresOldStyle(VIEW_ALIAS.LOBBY_HEADER_OVERLAPPING)
        self._updateRequiresOldStyle(VIEW_ALIAS.LOBBY_FOOTER_OVERLAPPING)
        return

    def _updateRequiresOldStyle(self, alias):
        component = self.getComponent(alias)
        if component is not None:
            component.getInjectView().setOldStyleViewFlag(self.__oldStyleViewMode)
        return

    @uniprof.regionDecorator(label=b'account.show_gui', scope=b'enter')
    def _populate(self):
        self.fireEvent(events.GUICommonEvent(events.GUICommonEvent.LOBBY_VIEW_LOADING))
        super(LobbyView, self)._populate()
        self.__currIgrType = self.igrCtrl.getRoomType()
        self.addListener(events.LobbySimpleEvent.SHOW_HELPLAYOUT, self.__showHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.LobbySimpleEvent.CLOSE_HELPLAYOUT, self.__closeHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_LOBBY_SUB_CONTAINER_ITEMS, self.__hideSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.REVEAL_LOBBY_SUB_CONTAINER_ITEMS, self.__revealSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        viewLifecycleHandler = _LobbySubViewsLifecycleHandler()
        self.__viewLifecycleWatcher.start(self.app.containerManager, [viewLifecycleHandler])
        self.igrCtrl.onIgrTypeChanged += self.__onIgrTypeChanged
        self.wallet.onWalletStatusChanged += self.__onWalletChanged
        battlesCount = self.itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount()
        epicBattlesCount = self.itemsCache.items.getAccountDossier().getEpicBattleStats().getBattlesCount()
        self.lobbyContext.updateBattlesCount(battlesCount, epicBattlesCount)
        self.as_setWalletStatusS(self.wallet.componentsStatuses)
        self.bwProto.voipController.invalidateMicrophoneMute()
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(LobbyView, self)._onRegisterFlashComponent(viewPy, alias)
        if alias in (VIEW_ALIAS.LOBBY_HEADER_OVERLAPPING, VIEW_ALIAS.LOBBY_FOOTER_OVERLAPPING):
            self._updateRequiresOldStyle(alias)
        return

    @uniprof.regionDecorator(label=b'account.show_gui', scope=b'exit')
    def _dispose(self):
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self.igrCtrl.onIgrTypeChanged -= self.__onIgrTypeChanged
        self.wallet.onWalletStatusChanged -= self.__onWalletChanged
        self.__viewLifecycleWatcher.stop()
        self.removeListener(events.LobbySimpleEvent.SHOW_HELPLAYOUT, self.__showHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.LobbySimpleEvent.CLOSE_HELPLAYOUT, self.__closeHelpLayout, EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_LOBBY_SUB_CONTAINER_ITEMS, self.__hideSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.REVEAL_LOBBY_SUB_CONTAINER_ITEMS, self.__revealSubContainerItems, EVENT_BUS_SCOPE.GLOBAL)
        self.stopGlobalListening()
        battle_selector_items.clear()
        super(LobbyView, self)._dispose()
        return

    def onPrbEntitySwitched(self):
        self.__updateBattleSelector()
        return

    def __onServerSettingsChange(self, _):
        self.__updateBattleSelector()
        return

    def __updateBattleSelector(self):
        state = g_prbLoader.getDispatcher().getFunctionalState()
        battle_selector_items.getItems().update(state)
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

    def __onWalletChanged(self, status):
        self.as_setWalletStatusS(status)
        return
