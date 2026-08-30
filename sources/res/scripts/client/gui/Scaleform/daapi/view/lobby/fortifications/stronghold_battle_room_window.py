from constants import PREBATTLE_TYPE
from debug_utils import LOG_DEBUG
from gui import SystemMessages
from gui.clans.clan_helpers import isLeaguesEnabled
from gui.impl import backport
from gui.impl.gen import R
from helpers import time_utils
from gui.Scaleform.daapi.view.meta.FortBattleRoomWindowMeta import FortBattleRoomWindowMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.managers.windows_stored_data import stored_window, DATA_TYPE, TARGET_ID
from gui.prb_control import settings, prbPeripheriesHandlerProperty
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.formatters import messages
from gui.prb_control.entities.base.unit.listener import IStrongholdListener
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import i18n
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import icons, text_styles
from gui.clans import formatters as clans_fmts
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.daapi.view.lobby.fortifications.stronghold_battle_room import StrongholdBattleRoom

@stored_window(DATA_TYPE.UNIQUE_WINDOW, TARGET_ID.CHANNEL_CAROUSEL)
class StrongholdBattleRoomWindow(FortBattleRoomWindowMeta, IStrongholdListener):

    def __init__(self, ctx=None):
        super(StrongholdBattleRoomWindow, self).__init__()
        self.__isOnMatchmakingTimerChangedRegistered = False
        self.currentState = b''
        return

    @prbPeripheriesHandlerProperty
    def prbPeripheriesHandler(self):
        return

    def onWindowMinimize(self):
        g_eventDispatcher.showUnitProgressInCarousel(self.getPrbType())
        self.destroy()
        return

    def getBrowserViewAlias(self, prbType):
        return FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_LIST_VIEW_UI

    def getRoomViewAlias(self, prbType):
        return FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_VIEW_UI

    def getFlashAliases(self):
        return FORTIFICATION_ALIASES.FLASH_ALIASES

    def getPythonAliases(self):
        return FORTIFICATION_ALIASES.PYTHON_ALIASES

    def getPrbType(self):
        return PREBATTLE_TYPE.STRONGHOLD

    def autoSearchCancel(self, value):
        self.currentState = value
        if self.currentState and self.prbEntity.inPlayersMatchingMode():
            self.prbEntity.exitFromPlayersMatchingMode()
            return
        self.prbEntity.exitFromQueue()
        return

    def onUnitPlayerAdded(self, pInfo):
        if not pInfo.isInvite():
            self.__addPlayerNotification(settings.UNIT_NOTIFICATION_KEY.PLAYER_ADDED, pInfo)
        return

    def onUnitPlayerRemoved(self, pInfo):
        if not pInfo.isInvite():
            self.__addPlayerNotification(settings.UNIT_NOTIFICATION_KEY.PLAYER_REMOVED, pInfo)
        return

    def onUnitFlagsChanged(self, flags, timeLeft):
        if flags.isExternalLegionariesMatchingChanged() and not flags.isInExternalLegionariesMatching():
            msgBody = backport.text(R.strings.system_messages.unit.warnings.EXTERNAL_LEGIONARIES_MATCHING_CANCELED())
            SystemMessages.pushMessage(msgBody, type=SystemMessages.SM_TYPE.Warning)
        self.__initState()
        return

    def onUnitErrorReceived(self, errorCode):
        self.as_autoSearchEnableBtnS(True)
        return

    def onUnitAutoSearchFinished(self):
        self.__clearState()
        return

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        if pInfo.isCurrentPlayer():
            self.as_changeAutoSearchBtnsStateS(pPermissions.canStartAutoSearch(), pPermissions.canStopBattleQueue())
        self.prbEntity.strongholdDataChanged()
        return

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        super(StrongholdBattleRoomWindow, self).onUnitPlayerOnlineStatusChanged(pInfo)
        if pInfo.isOffline():
            key = settings.UNIT_NOTIFICATION_KEY.PLAYER_OFFLINE
        else:
            key = settings.UNIT_NOTIFICATION_KEY.PLAYER_ONLINE
        self.__addPlayerNotification(key, pInfo)
        return

    def onUnitRejoin(self):
        self.__clearState()
        return

    def onUnitPlayerBecomeCreator(self, pInfo):
        if pInfo.isCurrentPlayer():
            self._showLeadershipNotification()
        super(StrongholdBattleRoomWindow, self).onUnitPlayerBecomeCreator(pInfo)
        return

    def refresh(self):
        self.prbEntity.requestMaintenanceUpdate()
        return

    def onStrongholdOnReadyStateChanged(self):
        g_eventDispatcher.updateUI()
        return

    def showStrongholdWaiting(self, visible):
        self.as_setWaitingS(visible, b'#waiting:prebattle/change_settings')
        g_eventDispatcher.updateUI()
        return

    def onStrongholdMaintenance(self, showWindow):
        if showWindow:
            text = (b'').join((
             icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ALERTBIGICON, 24, 24, -6, 0),
             text_styles.middleTitle(i18n.makeString(FORTIFICATIONS.MAINWINDOW_MAINTENANCE_HEADER)),
             clans_fmts.getHtmlLineDivider(10),
             text_styles.main(i18n.makeString(FORTIFICATIONS.MAINWINDOW_MAINTENANCE_BODY))))
            self.as_setInfoS(True, text, FORTIFICATIONS.MAINWINDOW_MAINTENANCE_BUTTON)
            self.as_enableWndCloseBtnS(True)
        else:
            self.as_setInfoS(False, b'', b'')
            self.showStrongholdWaiting(True)
        g_eventDispatcher.updateUI()
        return

    def onPlayersMatching(self, isPlayersMatchingInProgress):
        if not isPlayersMatchingInProgress:
            return
        self.__showPlayerSearchState()
        return

    def onStrongholdDataChanged(self, header, isFirstBattle, reserve, reserveOrder):
        self.__initState()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(StrongholdBattleRoomWindow, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, StrongholdBattleRoom):
            viewPy.setProxy(self)
        return

    def _populate(self):
        selectorUtils.setBattleTypeAsKnown(SELECTOR_BATTLE_TYPES.SORTIE)
        self.addListener(events.HideWindowEvent.HIDE_UNIT_WINDOW, self.__handleUnitWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.RenameWindowEvent.RENAME_WINDOW, self.__handleWindowRename, scope=EVENT_BUS_SCOPE.LOBBY)
        super(StrongholdBattleRoomWindow, self)._populate()
        self.prbEntity.initEvents(self)
        g_eventDispatcher.hideUnitProgressInCarousel(self.getPrbType())
        return

    def _dispose(self):
        self.removeListener(events.HideWindowEvent.HIDE_UNIT_WINDOW, self.__handleUnitWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.RenameWindowEvent.RENAME_WINDOW, self.__handleWindowRename, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.StrongholdEvent.STRONGHOLD_ON_TIMER, self._onMatchmakingTimerChanged, scope=EVENT_BUS_SCOPE.STRONGHOLD)
        super(StrongholdBattleRoomWindow, self)._dispose()
        return

    def _onMatchmakingTimerChanged(self, event):
        if self.currentState and self.prbEntity.isInQueue() and self.isPlayerInSlot():
            data = event.ctx
            timerState = data[b'textid']
            if data[b'dtime'] > 0 and timerState == TOOLTIPS.STRONGHOLDS_TIMER_SQUADINQUEUE:
                self.as_changeAutoSearchMainLabelS(i18n.makeString(CYBERSPORT.WINDOW_AUTOSEARCH_SEARCHENEMY_MAINTEXT))
                self.as_changeAutoSearchCountDownSecondsS(data[b'dtime'])
            else:
                self.as_changeAutoSearchTimeDirectionS(1)
                _, unit = self.prbEntity.getUnit()
                startTimer = 0
                if unit:
                    timestamp = unit.getModalTimestamp()
                    if timestamp:
                        startTimer = max(0, int(time_utils.getCurrentTimestamp() - time_utils.makeLocalServerTime(timestamp)))
                        LOG_DEBUG(b'time direction change, timers: ', time_utils.getCurrentTimestamp(), time_utils.makeLocalServerTime(timestamp))
                self.as_changeAutoSearchCountDownSecondsS(startTimer)
                LOG_DEBUG(b'changeAutoSearchCountDownSeconds', startTimer)
                if data[b'isSortie'] or data[b'isFirstBattle']:
                    self.as_changeAutoSearchMainLabelS(i18n.makeString(TOOLTIPS.STRONGHOLDS_TIMER_SEARCHENEMY))
                else:
                    self.as_changeAutoSearchMainLabelS(i18n.makeString(CYBERSPORT.WINDOW_AUTOSEARCH_SEARCHENEMY_MAINTEXT))
        return

    def __registerOnMatchmakingTimerChangedListener(self):
        if not self.__isOnMatchmakingTimerChangedRegistered and self.prbEntity.isStrongholdSettingsValid():
            self.__isOnMatchmakingTimerChangedRegistered = True
            self.addListener(events.StrongholdEvent.STRONGHOLD_ON_TIMER, self._onMatchmakingTimerChanged, scope=EVENT_BUS_SCOPE.STRONGHOLD)
            self.prbEntity.forceTimerEvent()
        return

    def __handleUnitWindowHide(self, _):
        self.destroy()
        return

    def __handleWindowRename(self, event):
        title = event.ctx[b'data']
        self.as_setWindowTitleS(title)
        return

    def __initState(self):
        if self.prbEntity.isInQueue():
            if self.isPlayerInSlot() and not self.prbEntity.canShowMaintenance():
                if isLeaguesEnabled():
                    g_eventDispatcher.showStrongholdsBattleQueue()
                    self.destroy()
                else:
                    self.__changeAutoSearchState()
        elif self.prbEntity.inPlayersMatchingMode():
            self.__showPlayerSearchState()
        else:
            self.__clearState()
        self.__registerOnMatchmakingTimerChangedListener()
        return

    def __clearState(self):
        self.currentState = b''
        self.as_enableWndCloseBtnS(True)
        self.as_hideAutoSearchS()
        return

    def __changeAutoSearchState(self):
        self.currentState = CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE
        self.as_enableWndCloseBtnS(False)
        permissions = self.prbEntity.getPermissions()
        model = {b'state': (self.currentState), 
           b'countDownSeconds': 0, 
           b'contextMessage': b'', 
           b'playersReadiness': [], b'canInvokeAutoSearch': (permissions.canStartAutoSearch()), 
           b'canInvokeBattleQueue': (permissions.canStopBattleQueue()), 
           b'timeDirection': (-1)}
        self.as_changeAutoSearchStateS(model)
        self.as_changeAutoSearchMainLabelS(i18n.makeString(TOOLTIPS.STRONGHOLDS_TIMER_WAITINGFORDATA))
        return

    def __showPlayerSearchState(self):
        pInfo = self.prbEntity.getPlayerInfo()
        if not pInfo.isInSlot:
            return
        self.currentState = CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE
        self.as_enableWndCloseBtnS(False)
        permissions = self.prbEntity.getPermissions()
        model = {b'state': (self.currentState), 
           b'countDownSeconds': (self.prbEntity.getSecondsCountInPlayersMatching()), 
           b'contextMessage': b'', 
           b'playersReadiness': [], b'canInvokeAutoSearch': (permissions.canStartAutoSearch()), 
           b'canInvokeBattleQueue': (permissions.canStopBattleQueue()), 
           b'timeDirection': 1}
        self.as_changeAutoSearchStateS(model)
        self.as_changeAutoSearchMainLabelS(i18n.makeString(TOOLTIPS.STRONGHOLDS_TIMER_LEGIONARIESSEARCH))
        return

    def __addPlayerNotification(self, key, pInfo):
        if self.chat and not pInfo.isCurrentPlayer():
            self.chat.as_addMessageS(messages.getUnitPlayerNotification(key, pInfo))
        return
