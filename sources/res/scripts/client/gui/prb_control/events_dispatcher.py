import weakref
from collections import namedtuple
from constants import PREBATTLE_TYPE
from debug_utils import LOG_ERROR, LOG_DEBUG
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.locale.CHAT import CHAT
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.app_loader import sf_lobby
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shared.events import ChannelManagementEvent, PreBattleChannelEvent, ChannelCarouselEvent
from helpers import dependency
from messenger.ext import channel_num_gen
from messenger.ext.channel_num_gen import SPECIAL_CLIENT_WINDOWS
from messenger.m_constants import LAZY_CHANNEL
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.game_control import IPlatoonController
TOOLTIP_PRB_DATA = namedtuple(b'TOOLTIP_PRB_DATA', (
 b'tooltipId',
 b'label'))
_CarouselItemCtx = namedtuple(b'_CarouselItemCtx', [
 30, 
 32, 
 33, 
 34, 
 35, 
 36, 
 37, 
 38, 
 39, 
 40])
_defCarouselItemCtx = _CarouselItemCtx(label=None, canClose=False, isNotified=False, icon=None, order=channel_num_gen.getOrder4Prebattle(), criteria=None, layer=WindowLayer.WINDOW, openHandler=None, readyData=None, tooltipData=None)
_LOCKED_SCREENS = (
 PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY,
 PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY)
_EPIC_SCREENS = (
 PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY,
 PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY)

class EventDispatcher(object):
    gameSession = dependency.descriptor(IGameSessionController)
    __appLoader = dependency.descriptor(IAppLoader)
    platoonCtrl = dependency.descriptor(IPlatoonController)

    def __init__(self):
        super(EventDispatcher, self).__init__()
        self.__loadingEvent = None
        return

    @sf_lobby
    def app(self):
        return

    def init(self, dispatcher):
        self.__setPrebattleDispatcher(dispatcher)
        app = self.app
        if app and app.containerManager:
            app.containerManager.onViewAddedToContainer += self.__onViewAddedToContainer
            app.loaderManager.onViewLoadCanceled += self.__onViewLoadCanceled
            app.loaderManager.onViewLoadError += self.__onViewLoadError
        g_eventBus.addListener(events.TrainingEvent.RETURN_TO_TRAINING_ROOM, self.__returnToTrainingRoom, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(events.TrainingEvent.SHOW_TRAINING_LIST, self.__showTrainingList, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(events.TrainingEvent.SHOW_EPIC_TRAINING_LIST, self.__showEpicTrainingList, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def fini(self):
        self.__setPrebattleDispatcher(None)
        self.__loadingEvent = None
        app = self.app
        if app and app.containerManager:
            app.containerManager.onViewAddedToContainer -= self.__onViewAddedToContainer
            app.loaderManager.onViewLoadCanceled -= self.__onViewLoadCanceled
            app.loaderManager.onViewLoadError -= self.__onViewLoadError
        g_eventBus.removeListener(events.TrainingEvent.RETURN_TO_TRAINING_ROOM, self.__returnToTrainingRoom, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(events.TrainingEvent.SHOW_TRAINING_LIST, self.__showTrainingList, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(events.TrainingEvent.SHOW_EPIC_TRAINING_LIST, self.__showEpicTrainingList, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def dispatchSwitchResult(self, result):
        self.__fireEvent(events.PrebattleEvent(events.PrebattleEvent.SWITCHED if result else events.PrebattleEvent.NOT_SWITCHED))
        return

    def isTrainingLoaded(self):
        return self.__getLoadedEvent() in _LOCKED_SCREENS or self.__loadingEvent in _LOCKED_SCREENS

    def isEpicTrainingLoaded(self):
        return self.__getLoadedEvent() in _EPIC_SCREENS or self.__loadingEvent in _EPIC_SCREENS

    def updateUI(self, loadedAlias=None):
        self.__fireEvent(events.FightButtonEvent(events.FightButtonEvent.FIGHT_BUTTON_UPDATE))
        self.__invalidatePrbEntity(loadedAlias)
        return

    def loadHangar(self):
        self.__fireLoadEvent(VIEW_ALIAS.LOBBY_HANGAR)
        return

    def loadBattleQueue(self):
        self.__fireLoadEvent(VIEW_ALIAS.BATTLE_QUEUE)
        return

    def loadTrainingList(self):
        self.addTrainingToCarousel()
        self.__showTrainingList()
        return

    def loadTrainingRoom(self):
        self.addTrainingToCarousel(False)
        self.__showTrainingRoom()
        return

    def loadEpicTrainingList(self):
        self.addEpicTrainingToCarousel()
        self.__showEpicTrainingList()
        return

    def loadEpicTrainingRoom(self):
        self.addEpicTrainingToCarousel(False)
        self.__showEpicTrainingRoom()
        return

    def loadBattleSessionWindow(self, prbType):
        self.addSpecBattleToCarousel(prbType)
        self.showBattleSessionWindow()
        return

    def loadBattleSessionList(self):
        self.__fireShowEvent(PREBATTLE_ALIASES.BATTLE_SESSION_LIST_WINDOW_PY)
        return

    def loadUnit(self, prbType):
        self.__addUnitToCarousel(prbType)
        self.showUnitWindow(prbType)
        return

    def loadStrongholds(self):
        self.__addStrongholdsToCarousel()
        self.showStrongholdsWindow()
        return

    def loadTournaments(self):
        return

    def loadSquad(self, prbType, ctx=None, isTeamReady=False):
        self.__addSquadToCarousel(prbType, isTeamReady)
        self.__showSquadWindow(prbType, ctx and ctx.get(b'showInvitesWindow', False), toggleUI=False)
        return

    def loadRanked(self):
        self.__fireShowEvent(RANKEDBATTLES_ALIASES.RANKED_BATTLES_INTRO_ALIAS)
        return

    def loadRankedUnreachable(self):
        self.__fireShowEvent(RANKEDBATTLES_ALIASES.RANKED_BATTLES_UNREACHABLE_VIEW_ALIAS)
        return

    def loadBootcampQueue(self):
        self.__fireEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_QUEUE_DIALOG_SHOW)))
        return

    def unloadBootcampQueue(self):
        self.__fireEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_QUEUE_DIALOG_CLOSE)))
        return

    def removeTrainingFromCarousel(self, isList=True, closeWindow=True):
        clientType = SPECIAL_CLIENT_WINDOWS.TRAINING_LIST if isList else SPECIAL_CLIENT_WINDOWS.TRAINING_ROOM
        clientID = channel_num_gen.getClientID4SpecialWindow(clientType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'removeTrainingToCarousel')
            return
        self.__handleRemoveRequest(clientID, closeWindow=closeWindow)
        return

    def removeEpicTrainingFromCarousel(self, isList=True, closeWindow=True):
        clientType = SPECIAL_CLIENT_WINDOWS.EPIC_TRAINING_LIST if isList else SPECIAL_CLIENT_WINDOWS.EPIC_TRAINING_ROOM
        clientID = channel_num_gen.getClientID4SpecialWindow(clientType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'removeEpicTrainingFromCarousel')
            return
        self.__handleRemoveRequest(clientID, closeWindow=closeWindow)
        return

    def addTrainingToCarousel(self, isList=True):
        self.removeTrainingFromCarousel(not isList, closeWindow=False)
        if isList:
            clientType = SPECIAL_CLIENT_WINDOWS.TRAINING_LIST
            alias = PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY
            handler = lambda : self.__fireEvent(events.TrainingEvent(events.TrainingEvent.SHOW_TRAINING_LIST))
        else:
            clientType = SPECIAL_CLIENT_WINDOWS.TRAINING_ROOM
            alias = PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY
            handler = lambda : self.__fireEvent(events.TrainingEvent(events.TrainingEvent.RETURN_TO_TRAINING_ROOM))
        clientID = channel_num_gen.getClientID4SpecialWindow(clientType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'addTrainingToCarousel')
            return
        currCarouselItemCtx = _defCarouselItemCtx._replace(label=MENU.HEADERBUTTONS_BATTLE_TYPES_TRAINING, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): alias}, layer=WindowLayer.SUB_VIEW, openHandler=handler)
        self.__handleAddPreBattleRequest(clientID, currCarouselItemCtx._asdict())
        return

    def addEpicTrainingToCarousel(self, isList=True):
        self.removeEpicTrainingFromCarousel(not isList, closeWindow=False)
        if isList:
            clientType = SPECIAL_CLIENT_WINDOWS.EPIC_TRAINING_LIST
            alias = PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY
            handler = lambda : self.__fireEvent(events.TrainingEvent(events.TrainingEvent.SHOW_EPIC_TRAINING_LIST))
        else:
            clientType = SPECIAL_CLIENT_WINDOWS.EPIC_TRAINING_ROOM
            alias = PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY
            handler = lambda : self.__fireEvent(events.TrainingEvent(events.TrainingEvent.RETURN_TO_TRAINING_ROOM))
        clientID = channel_num_gen.getClientID4SpecialWindow(clientType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'addEpicTrainingToCarousel')
            return
        label = (b'{} - {}').format(backport.text(R.strings.menu.headerButtons.battle.types.epicTraining()), backport.text(R.strings.menu.headerButtons.battle.types.epicTraining.descr()))
        currCarouselItemCtx = _defCarouselItemCtx._replace(label=label, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): alias}, layer=WindowLayer.SUB_VIEW, openHandler=handler)
        self.__handleAddPreBattleRequest(clientID, currCarouselItemCtx._asdict())
        return

    def addSpecBattleToCarousel(self, prbType):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'addSpecBattleToCarousel')
            return
        if prbType is PREBATTLE_TYPE.CLAN:
            label = CHAT.CHANNELS_CLAN
        elif prbType is PREBATTLE_TYPE.TOURNAMENT:
            label = CHAT.CHANNELS_TOURNAMENT
        else:
            LOG_ERROR(b'Prebattle type is not valid', prbType)
            return
        currCarouselItemCtx = _defCarouselItemCtx._replace(label=label, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (PREBATTLE_ALIASES.BATTLE_SESSION_ROOM_WINDOW_PY)}, openHandler=self.showBattleSessionWindow)
        self.__handleAddPreBattleRequest(clientID, currCarouselItemCtx._asdict())
        return

    def addSpecBattlesToCarousel(self):
        clientID = channel_num_gen.getClientID4LazyChannel(LAZY_CHANNEL.SPECIAL_BATTLES)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'addSpecBattlesToCarousel')
            return
        currCarouselItemCtx = _defCarouselItemCtx._replace(label=LAZY_CHANNEL.SPECIAL_BATTLES, order=channel_num_gen.getOrder4LazyChannel(LAZY_CHANNEL.SPECIAL_BATTLES), isNotified=False, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (PREBATTLE_ALIASES.BATTLE_SESSION_LIST_WINDOW_PY)}, openHandler=self.loadBattleSessionList)
        self.__fireEvent(ChannelManagementEvent(clientID, PreBattleChannelEvent.REQUEST_TO_ADD, currCarouselItemCtx._asdict()))
        return

    def restoreBattleSessionList(self):
        viewContainer = self.app.containerManager
        window = viewContainer.getView(WindowLayer.WINDOW, {(POP_UP_CRITERIA.VIEW_ALIAS): (PREBATTLE_ALIASES.BATTLE_SESSION_LIST_WINDOW_PY)})
        if window is None:
            clientID = channel_num_gen.getClientID4LazyChannel(LAZY_CHANNEL.SPECIAL_BATTLES)
            if not clientID:
                LOG_ERROR(b'Client ID not found', b'restoreBattleSessionList')
                return
            self.__fireEvent(events.ChannelManagementEvent(clientID, ChannelCarouselEvent.OPEN_BUTTON_CLICK, {b'clientID': clientID}))
        return

    def removeSpecBattleFromCarousel(self, prbType, closeWindow=True):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'_removeSpecBattleFromCarousel')
            return
        self.__handleRemoveRequest(clientID, closeWindow=closeWindow)
        return

    def removeSpecBattlesFromCarousel(self):
        clientID = channel_num_gen.getClientID4LazyChannel(LAZY_CHANNEL.SPECIAL_BATTLES)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'removeSpecBattlesFromCarousel')
            return
        self.__fireEvent(ChannelManagementEvent(clientID, PreBattleChannelEvent.REQUEST_TO_REMOVE))
        return

    def hideSpecialBattleWindow(self):
        self.__fireHideEvent(events.HideWindowEvent.HIDE_SPECIAL_BATTLE_WINDOW)
        return

    def notifySpecialBattleWindow(self):
        clientID = channel_num_gen.getClientID4LazyChannel(LAZY_CHANNEL.SPECIAL_BATTLES)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'notifySpecialBattleWindow')
            return
        self.__fireEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_CHANGE, {b'key': b'isNotified', 
           b'value': True, 
           b'isShowByReq': True, 
           b'showIfClosed': True}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def showUnitWindow(self, prbType):
        if prbType in PREBATTLE_TYPE.SQUAD_PREBATTLES:
            self.__showSquadWindow(prbType, toggleUI=False)
        else:
            self.__fireShowEvent(CYBER_SPORT_ALIASES.CYBER_SPORT_WINDOW_PY)
        return

    def showStrongholdsWindow(self):
        from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
        self.__fireShowEvent(FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_WINDOW_ALIAS)
        return

    def showTournamentWindow(self):
        return

    def showStrongholdsBattleQueue(self):
        self.removeUnitFromCarousel(PREBATTLE_TYPE.STRONGHOLD)
        self.__fireShowEvent(VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE)
        return

    def showTournamentQueue(self):
        return

    def strongholdsOnTimer(self, data):
        self.__fireEvent(events.StrongholdEvent(events.StrongholdEvent.STRONGHOLD_ON_TIMER, ctx=data), scope=EVENT_BUS_SCOPE.STRONGHOLD)
        return

    def showSwitchPeripheryWindow(self, ctx, isModal=True):
        if isModal:
            alias = VIEW_ALIAS.SWITCH_PERIPHERY_WINDOW_MODAL
        else:
            alias = VIEW_ALIAS.SWITCH_PERIPHERY_WINDOW
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(alias), ctx=ctx), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def removeUnitFromCarousel(self, prbType, closeWindow=True):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'removeUnitFromCarousel', prbType)
            return
        self.__handleRemoveRequest(clientID, closeWindow=closeWindow)
        return

    def setUnitProgressInCarousel(self, prbType, isInProgress):
        if prbType in PREBATTLE_TYPE.SQUAD_PREBATTLES:
            LOG_DEBUG(b'No unit progress for squad.')
            return
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'setUnitProgressInCarousel', prbType)
            return
        self.__fireEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_CHANGE, {b'key': b'isInProgress', 
           b'value': isInProgress, 
           b'isShowByReq': isInProgress, 
           b'showIfClosed': True}))
        return

    def showUnitProgressInCarousel(self, prbType):
        self._showUnitProgress(prbType, True)
        return

    def hideUnitProgressInCarousel(self, prbType):
        self._showUnitProgress(prbType, False)
        return

    def fireAutoInviteReceived(self, invite):
        self.__fireEvent(events.AutoInviteEvent(invite, events.AutoInviteEvent.INVITE_RECEIVED))
        return

    def showParentControlNotification(self):
        from gui import DialogsInterface
        DialogsInterface.showDialog(self.gameSession.getParentControlNotificationMeta(), (lambda *args: None))
        return

    def showBattleSessionWindow(self):
        self.__fireShowEvent(PREBATTLE_ALIASES.BATTLE_SESSION_ROOM_WINDOW_PY)
        return

    def setSquadTeamReadyInCarousel(self, prbType, isTeamReady):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'setSquadTeamReadyInCarousel', prbType)
            return
        g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_CHANGE, {b'key': b'tooltipData', 
           b'value': (self.__getTooltipPrbData(CHAT.CHANNELS_SQUADREADY_TOOLTIP if isTeamReady else CHAT.CHANNELS_SQUADNOTREADY_TOOLTIP)), 
           b'isShowByReq': False, 
           b'showIfClosed': True}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def needToLoadHangar(self, ctx, modeFlags, aliasToLoad):
        if ctx is not None:
            switchMask = FUNCTIONAL_FLAG.TRAINING | FUNCTIONAL_FLAG.EPIC_TRAINING
            canSwitch = (ctx.getFlags() | modeFlags) & switchMask == switchMask
            if canSwitch:
                return False
        res = False
        inView = None
        if self.__appLoader is not None and self.__appLoader.getApp() is not None and self.__appLoader.getApp().containerManager is not None:
            inView = self.__appLoader.getApp().containerManager.getView(WindowLayer.SUB_VIEW)
        if inView is not None:
            if inView.alias in aliasToLoad:
                res = True
        return res

    def _showUnitProgress(self, prbType, show):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'_showUnitStatus', prbType)
            return
        self.__fireEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_SHOW, {b'show': show}))
        return

    def __showSquadWindow(self, prbType, showInvitesWindow=False, toggleUI=False):
        self.platoonCtrl.evaluateVisibility(toggleUI=toggleUI)
        return

    def __showTrainingRoom(self):
        self.__fireLoadEvent(PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY)
        return

    def __returnToTrainingRoom(self, event=None):
        self.__prbDispatcher.doAction()
        return

    def __showEpicTrainingRoom(self):
        self.__fireLoadEvent(PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY)
        return

    def __fireEvent(self, event, scope=EVENT_BUS_SCOPE.LOBBY):
        g_eventBus.handleEvent(event, scope)
        return

    def __fireHideEvent(self, event):
        self.__fireEvent(events.HideWindowEvent(event))
        return

    def __fireShowEvent(self, eventName, arg=None):
        if arg is None:
            self.__fireEvent(events.LoadViewEvent(SFViewLoadParams(eventName)))
        else:
            self.__fireEvent(events.LoadViewEvent(SFViewLoadParams(eventName), ctx=arg))
        return

    def __fireLoadEvent(self, eventName, arg=None):
        if self.__getLoadedEvent() == eventName:
            LOG_DEBUG(b'View already is loaded', eventName)
            return
        else:
            if self.__loadingEvent:
                LOG_DEBUG(b'View is still loading. It is ignored', self.__loadingEvent, eventName)
            else:
                self.__loadingEvent = eventName
                if arg is None:
                    self.__fireEvent(events.LoadViewEvent(SFViewLoadParams(eventName)))
                else:
                    self.__fireEvent(events.LoadViewEvent(SFViewLoadParams(eventName), ctx=arg))
            return

    def __handleRemoveRequest(self, clientID, closeWindow=True):
        self.__fireEvent(ChannelManagementEvent(clientID, PreBattleChannelEvent.REQUEST_TO_REMOVE_PRE_BATTLE_CHANNEL, ctx={b'closeWindow': closeWindow}))
        return

    def __handleAddPreBattleRequest(self, clientID, carouselItemCtx):
        self.__fireEvent(ChannelManagementEvent(clientID, PreBattleChannelEvent.REQUEST_TO_ADD_PRE_BATTLE_CHANNEL, carouselItemCtx))
        return

    def __closeBattleSessionWindow(self):
        self.__fireHideEvent(events.HideWindowEvent.HIDE_BATTLE_SESSION_WINDOW)
        return

    def __closeUnitWindow(self):
        self.__fireHideEvent(events.HideWindowEvent.HIDE_UNIT_WINDOW)
        return

    def __setPrebattleDispatcher(self, prbDispatcher):
        if prbDispatcher is not None:
            self.__prbDispatcher = weakref.proxy(prbDispatcher)
        else:
            self.__prbDispatcher = None
        return

    def __showTrainingList(self, event=None):
        self.__fireLoadEvent(PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY)
        return

    def __showEpicTrainingList(self, event=None):
        self.__fireLoadEvent(PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY)
        return

    def __getReadyPrbData(self, isReady):
        return {b'isReady': isReady}

    def __getTooltipPrbData(self, tooltipId, label=b''):
        return TOOLTIP_PRB_DATA(tooltipId=tooltipId, label=label)._asdict()

    def __invalidatePrbEntity(self, loadedAlias):
        if loadedAlias == VIEW_ALIAS.LOBBY_HANGAR and self.__prbDispatcher is not None:
            entity = self.__prbDispatcher.getEntity()
            if entity:
                entity.invalidate()
        return

    def __onViewLoadError(self, view, *args, **kwargs):
        if view.alias == self.__loadingEvent:
            self.__loadingEvent = None
        return

    def __onViewLoadCanceled(self, view, *args, **kwargs):
        if view.alias == self.__loadingEvent:
            self.__loadingEvent = None
        return

    def __onViewAddedToContainer(self, _, pyEntity):
        settings = pyEntity.settings
        if settings is None or settings.event == self.__loadingEvent:
            self.__loadingEvent = None
        if pyEntity.layer == WindowLayer.SUB_VIEW:
            self.updateUI(pyEntity.alias)
        return

    def __getLoadedEvent(self):
        app = self.app
        if app and app.containerManager:
            container = app.containerManager.getContainer(WindowLayer.SUB_VIEW)
            if container:
                view = container.getView()
                if view and view.settings is not None:
                    return view.settings.event
        return

    def __addUnitToCarousel(self, prbType):
        from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
        self.__addUnitToCarouselCommon(prbType, CYBERSPORT.WINDOW_TITLE, CYBER_SPORT_ALIASES.CYBER_SPORT_WINDOW_PY, (lambda : self.showUnitWindow(prbType)))
        return

    def __addStrongholdsToCarousel(self):
        from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
        from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
        self.__addUnitToCarouselCommon(PREBATTLE_TYPE.STRONGHOLD, FORTIFICATIONS.SORTIE_INTROVIEW_TITLE, FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_WINDOW_ALIAS, self.showStrongholdsWindow)
        return

    def __addTournamentToCarousel(self):
        return

    def __addUnitToCarouselCommon(self, prbType, label, viewAlias, openHandler):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'addUnitToCarousel', clientID)
            return
        criteria = {(POP_UP_CRITERIA.VIEW_ALIAS): viewAlias}
        currCarouselItemCtx = _defCarouselItemCtx._replace(label=label, criteria=criteria, layer=WindowLayer.WINDOW, openHandler=openHandler)
        self.__handleAddPreBattleRequest(clientID, currCarouselItemCtx._asdict())
        return

    def __addSquadToCarousel(self, prbType, isTeamReady=False):
        clientID = channel_num_gen.getClientID4Prebattle(prbType)
        if not clientID:
            LOG_ERROR(b'Client ID not found', b'addSquadToCarousel')
            return
        currCarouselItemCtx = _defCarouselItemCtx._replace(label=CHAT.CHANNELS_SQUAD, icon=RES_ICONS.MAPS_ICONS_MESSENGER_SQUAD_ICON, criteria={}, openHandler=(lambda : self.__showSquadWindow(prbType, toggleUI=True)), tooltipData=self.__getTooltipPrbData(CHAT.CHANNELS_SQUADREADY_TOOLTIP if isTeamReady else CHAT.CHANNELS_SQUADNOTREADY_TOOLTIP))
        self.__handleAddPreBattleRequest(clientID, currCarouselItemCtx._asdict())
        return


g_eventDispatcher = EventDispatcher()
