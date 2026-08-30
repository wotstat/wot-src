import logging
from constants import IS_LOOT_BOXES_ENABLED
from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl import backport
from gui.impl.gen import R
from gui.periodic_battles.models import PrimeTimeStatus
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency
from skeletons.gui.game_control import IWhiteTigerController, ILootBoxesController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.system_messages import ISystemMessages
from skeletons.gui.wt_event import IWTEventNotifications
from client_constants import EVENT_STATES
from white_tiger.gui.gui_constants import SCH_CLIENT_MSG_TYPE
_logger = logging.getLogger(__name__)

class WTEventNotifications(IWTEventNotifications):
    _STR_RES = R.strings.white_tiger.notifications
    __gameEventCtrl = dependency.descriptor(IWhiteTigerController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __systemMessages = dependency.descriptor(ISystemMessages)
    __lootBoxesCtrl = dependency.descriptor(ILootBoxesController)

    def __init__(self):
        super(WTEventNotifications, self).__init__()
        self.__curStatus = PrimeTimeStatus.NOT_SET
        self.__isEnabled = False
        return

    def init(self):
        return

    def fini(self):
        return

    def onLobbyInited(self, event):
        g_clientUpdateManager.addCallbacks({b'tokens': (self.__onTokensUpdate)})
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self.__gameEventCtrl.onPrimeTimeStatusUpdated += self.__onPrimeTimeStatusUpdate
        self.__gameEventCtrl.onUpdated += self.__onEventUpdated
        status, _, _ = self.__gameEventCtrl.getPrimeTimeStatus()
        if self.__curStatus != PrimeTimeStatus.NOT_SET:
            self.__onPrimeTimeStatusUpdate(status)
        else:
            self.__curStatus = status
        self.__isEnabled = self.__gameEventCtrl.isEnabled()
        return

    def onAccountBecomeNonPlayer(self):
        self.__clear()
        return

    def onDisconnected(self):
        self.__clear()
        return

    def __clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self.__gameEventCtrl.onPrimeTimeStatusUpdated -= self.__onPrimeTimeStatusUpdate
        self.__gameEventCtrl.onUpdated -= self.__onEventUpdated
        return

    def __onTokensUpdate(self, diff):
        for token in self.__gameEventCtrl.getBossTokenIDList():
            if token in diff:
                ticketTokenStr = token.split(b':')[1]
                SystemMessages.pushMessage(text=backport.text(self._STR_RES.dyn(ticketTokenStr).received.body(), ticketsCount=str(self.__gameEventCtrl.getBossTokenCount(token))), messageData={b'header': (backport.text(self._STR_RES.dyn(ticketTokenStr).received.header()))}, type=SystemMessages.SM_TYPE.WarningHeader, priority=NotificationPriorityLevel.HIGH)

        return

    def __onServerSettingsChange(self, diff):
        if not self.__gameEventCtrl.isAvailable():
            return
        if IS_LOOT_BOXES_ENABLED in diff:
            if self.__lootBoxesCtrl.isEnabled():
                self.__systemMessages.proto.serviceChannel.pushClientMessage({b'text': (backport.text(self._STR_RES.lootboxes.switchOn.body()))}, SCH_CLIENT_MSG_TYPE.WT_SWITCH_ON_LOOTBOXES_NOTIFICATIONS)
            else:
                SystemMessages.pushMessage(text=backport.text(self._STR_RES.lootboxes.switchOff.body()), type=SystemMessages.SM_TYPE.WarningHeader, priority=NotificationPriorityLevel.HIGH, messageData={b'header': (backport.text(self._STR_RES.lootboxes.header()))})
        return

    def __onEventUpdated(self):
        if self.__isEnabled == self.__gameEventCtrl.isEnabled():
            return
        self.__isEnabled = self.__gameEventCtrl.isEnabled()
        eventState = EVENT_STATES.START if self.__isEnabled else EVENT_STATES.FINISH
        self.__systemMessages.proto.serviceChannel.pushClientMessage({b'state': eventState}, SCH_CLIENT_MSG_TYPE.WT_EVENT_STATE)
        return

    def __onPrimeTimeStatusUpdate(self, status):
        if self.__curStatus == status:
            return
        if status == PrimeTimeStatus.FROZEN:
            SystemMessages.pushMessage(text=backport.text(self._STR_RES.switchOff.body()), messageData={b'header': (backport.text(self._STR_RES.switchOff.header()))}, type=SystemMessages.SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.HIGH)
        elif self.__curStatus == PrimeTimeStatus.FROZEN:
            SystemMessages.pushMessage(text=backport.text(self._STR_RES.switchOn.body()), messageData={b'header': (backport.text(self._STR_RES.switchOn.header()))}, type=SystemMessages.SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.HIGH)
        elif status == PrimeTimeStatus.AVAILABLE:
            if not self.__isFirstPrimeTime():
                SystemMessages.pushMessage(text=backport.text(self._STR_RES.primeTime.available.body()), messageData={b'header': (backport.text(self._STR_RES.primeTime.available.header()))}, type=SystemMessages.SM_TYPE.WarningHeader)
        elif status == PrimeTimeStatus.NOT_AVAILABLE:
            SystemMessages.pushMessage(text=backport.text(self._STR_RES.primeTime.notAvailable.body()), messageData={b'header': (backport.text(self._STR_RES.primeTime.notAvailable.header()))}, type=SystemMessages.SM_TYPE.WarningHeader)
        self.__curStatus = status
        return

    def __isFirstPrimeTime(self):
        if not self.__gameEventCtrl.getSeasonPassed():
            curSeason = self.__gameEventCtrl.getCurrentSeason()
            if curSeason is not None and curSeason.getPassedCyclesNumber() == 0 and not self.__gameEventCtrl.hasPrimeTimesPassedForCurrentCycle():
                return True
        return False
