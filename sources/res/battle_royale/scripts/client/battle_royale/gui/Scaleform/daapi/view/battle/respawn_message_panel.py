from __future__ import absolute_import
import logging, weakref, BigWorld, BattleReplay
from Event import EventsSubscriber
from ReplayEvents import g_replayEvents
from VehicleBRRespawnEffectComponent import VehicleBRRespawnEffectComponent
from battle_royale.gui.Scaleform.daapi.view.battle.respawn_messages_formatters import formatRespawnActivatedMessage, formatRespawnFinishedMessage, formatRespawnNotAvailableMessage, formatAllyInBattleMessage, formatStayInCoverMessage, formatPickUpSphereMessage, formatAllyRespawnedMessage, formatRespawnNotAvailableSoonMessage, formatRespawnActivatedSquadMessage, formatRespawnedMessage
from battle_royale.gui.battle_control.controllers.notification_manager import INotificationManagerListener, MessageType
from battle_royale.gui.battle_control.controllers.spawn_ctrl import ISpawnListener
from constants import ARENA_BONUS_TYPE, ARENA_PERIOD
from gui.Scaleform.daapi.view.meta.BRRespawnMessagePanelMeta import BRRespawnMessagePanelMeta
from gui.battle_control.arena_info import vos_collections
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController, IArenaPeriodController
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from helpers import dependency
from helpers.time_utils import ONE_MINUTE
from items.battle_royale import isSpawnedBot
from skeletons.gui.battle_session import IBattleSessionProvider
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
RESPAWNING_TIMER_DELAY = 1

class RespawnMessagePanel(BRRespawnMessagePanelMeta, ISpawnListener, IArenaPeriodController, IArenaVehiclesController, INotificationManagerListener):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    TIME_TO_SHOW = 5
    RESPAWN_DELAY_BEFORE_SHOW = 1
    RESPAWN_COMPLETED_DELAY_BEFORE_SHOW = 2

    def __init__(self):
        super(RespawnMessagePanel, self).__init__()
        self.__vehicleIDs = []
        self.__lives = -1
        self.notificationManager = None
        self.__respawnTimestampSent = False
        self.__timeoutCallbackID = None
        self._message = None
        self.__es = EventsSubscriber()
        return

    def addNotificationManager(self, notificationManager):
        self.notificationManager = weakref.ref(notificationManager)
        self.notificationManager().addRespawnPanel(self)
        return

    def getCtrlScope(self):
        return _SCOPE.PERIOD | _SCOPE.VEHICLES

    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        periodCtrl = self.sessionProvider.shared.arenaPeriod
        if periodCtrl is not None and periodCtrl.getPeriod() < ARENA_PERIOD.BATTLE:
            return
        else:
            if vInfoVO.vehicleID in self.__vehicleIDs:
                _logger.debug(b'invalidateVehicleStatus %s, %s', vInfoVO.vehicleID, vInfoVO.isAlive())
                vehicle = BigWorld.player().getVehicleAttached()
                if vehicle.isAlive() and not vInfoVO.isAlive() and self.__lives == 0:
                    _logger.debug(b'formatPickUpSphereMessage')
                    message = formatPickUpSphereMessage(self.TIME_TO_SHOW, self.RESPAWN_DELAY_BEFORE_SHOW)
                    self.__addMessage(message)
            return

    def updateRespawnTime(self, timeLeft):
        bonusType = self.sessionProvider.arenaVisitor.getArenaBonusType()
        isSquadMode = bonusType in ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD_RANGE
        if timeLeft > 0.0:
            if isSquadMode:
                _logger.debug(b'formatRespawnActivatedSquadMessage %s', timeLeft)
                message = formatRespawnActivatedSquadMessage(timeLeft, self.RESPAWN_DELAY_BEFORE_SHOW)
                self.__addMessage(message)
            else:
                _logger.debug(b'formatRespawnActivatedMessage %s', timeLeft)
                message = formatRespawnActivatedMessage(timeLeft, self.RESPAWN_DELAY_BEFORE_SHOW)
                self.__addMessage(message)
        return

    def updateTeammateRespawnTime(self, timeLeft):
        if timeLeft > 0.0:
            _logger.debug(b'formatStayInCoverMessage %s', timeLeft)
            message = formatStayInCoverMessage(timeLeft, RESPAWNING_TIMER_DELAY)
            self.__addMessage(message)
        return

    def updateBlockToResurrectTime(self, blockTime):
        if blockTime > 0.0:
            _logger.debug(b'formatAllyInBattleMessage %s', blockTime)
            message = formatAllyInBattleMessage(blockTime, self.RESPAWN_DELAY_BEFORE_SHOW)
            self.__addMessage(message)
        return

    def updateLives(self, livesLeft, _):
        self.__lives = livesLeft if livesLeft is not None else 0
        return

    def __onRespawnTimeFinished(self):
        _logger.debug(b'formatRespawnNotAvailableMessage')
        message = formatRespawnNotAvailableMessage(self.TIME_TO_SHOW)
        self.__addMessage(message)
        return

    def sendMessageTime(self, seconds):
        if not self._message:
            raise SoftException(b'No message on the panel, cant set message time')
        self.as_setMessageTimeS(seconds)
        return

    def sendMessage(self, message):
        if self._message:
            raise SoftException(b'Message already on the panel')
        self._message = message
        self.as_addMessageS(message)
        return

    def hideMessage(self):
        if not self._message:
            raise SoftException(b'No message on the panel')
        self._message = None
        self.as_hideMessageS()
        return

    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        timesGoneFromStart = self.__getTimeGoneFromStart(endTime, length)
        self.__onPeriodChange(period, timesGoneFromStart)
        return

    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        timesGoneFromStart = self.__getTimeGoneFromStart(endTime, length)
        self.__onPeriodChange(period, timesGoneFromStart)
        return

    def componentChanged(self):
        self.notificationManager().clearQueue()
        return

    def _populate(self):
        super(RespawnMessagePanel, self)._populate()
        self.sessionProvider.addArenaCtrl(self)
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            self.__es.subscribeToEvent(ctrl.onRespawnBaseMoving, self.__onRespawnBaseMoving)
            self.__es.subscribeToEvent(ctrl.onVehicleStateUpdated, self.__onVehicleStateUpdated)
        if self.sessionProvider.arenaVisitor.bonus.isSquadSupported():
            self.__initSquadPlayers()
            self.__es.subscribeToEvent(VehicleBRRespawnEffectComponent.onRespawned, self.__onVehicleRespawned)
        deathScreenCtrl = self.sessionProvider.dynamic.deathScreen
        if deathScreenCtrl:
            self.__es.subscribeToEvent(deathScreenCtrl.onShowDeathScreen, self.__onShowDeathScreen)
            self.__es.subscribeToEvent(deathScreenCtrl.onWinnerScreen, self.__onShowDeathScreen)
        self.__es.subscribeToEvent(BigWorld.player().onObserverVehicleChanged, self.__onObserverVehicleChanged)
        battleRoyaleComponent = self.sessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent
        self.__es.subscribeToEvent(battleRoyaleComponent.onBattleRoyaleDefeatedTeamsUpdate, self.__onTeamDeath)
        self.__es.subscribeToEvent(battleRoyaleComponent.onRespawnTimeFinished, self.__onRespawnTimeFinished)
        if BattleReplay.g_replayCtrl.isPlaying:
            self.__es.subscribeToEvent(g_replayEvents.onTimeWarpStart, self.__onReplayTimeWarpStart)
        return

    def _dispose(self):
        self.notificationManager = None
        if self.__timeoutCallbackID:
            BigWorld.cancelCallback(self.__timeoutCallbackID)
            self.__timeoutCallbackID = None
        self.sessionProvider.removeArenaCtrl(self)
        self.__es.unsubscribeFromAllEvents()
        super(RespawnMessagePanel, self)._dispose()
        return

    def __onVehicleRespawned(self, vehicleID):
        if vehicleID in self.__vehicleIDs:
            _logger.debug(b'formatAllyRespawnedMessage')
            message = formatAllyRespawnedMessage(self.TIME_TO_SHOW, self.RESPAWN_DELAY_BEFORE_SHOW)
            self.__addMessage(message)
        return

    @staticmethod
    def __getTimeGoneFromStart(endTime, length):
        startTime = endTime - length
        return BigWorld.serverTime() - startTime

    def __onPeriodChange(self, period, timesGoneFromStart):
        if period == ARENA_PERIOD.BATTLE and not self.__respawnTimestampSent:
            arenaInfo = BigWorld.player().arena.arenaInfo
            respawnPeriod = arenaInfo.arenaInfoBRComponent.respawnPeriod if arenaInfo else 0
            secondsLeft = max(respawnPeriod - timesGoneFromStart, 0)
            self.__respawnTimestampSent = True
            timeToNotification = max(secondsLeft - ONE_MINUTE, 0)
            if timeToNotification:
                self.__timeoutCallbackID = BigWorld.callback(timeToNotification, self.__showNotAvailableSoonNotification)
        return

    def __onRespawnBaseMoving(self, *_):
        message = formatRespawnFinishedMessage(self.TIME_TO_SHOW, self.RESPAWN_COMPLETED_DELAY_BEFORE_SHOW)
        self.__addMessage(message)
        return

    def __onVehicleStateUpdated(self, stateID, _):
        if stateID == VEHICLE_VIEW_STATE.DEATH_INFO:
            message = formatRespawnedMessage(0)
            message.msgType = MessageType.vehicleDeadMsg
            message.showBefore = -1
            self.notificationManager().addRespawnMessage(message)
        return

    def __initSquadPlayers(self):
        self.__vehicleIDs = []
        arenaDP = self.sessionProvider.getArenaDP()
        collection = vos_collections.AllyItemsCollection().ids(arenaDP)
        for vId in collection:
            vInfoVO = arenaDP.getVehicleInfo(vId)
            playerVehId = BigWorld.player().observedVehicleID or arenaDP.getPlayerVehicleID()
            if not vInfoVO.isObserver() and playerVehId != vId and not isSpawnedBot(vInfoVO.vehicleType.tags):
                self.__vehicleIDs.append(vId)

        return

    def __showNotAvailableSoonNotification(self):
        self.__timeoutCallbackID = None
        message = formatRespawnNotAvailableSoonMessage(self.TIME_TO_SHOW)
        self.__addMessage(message)
        return

    def __addMessage(self, message):
        if self.notificationManager():
            if message.msgType in (MessageType.respActivatedMsg, MessageType.allyInBattleMsg,
             MessageType.stayInCoverMsg):
                message.showBefore = BigWorld.serverTime() + message.time
            else:
                message.showBefore = BigWorld.serverTime() + ONE_MINUTE
            self.notificationManager().addRespawnMessage(message)
        return

    def __onShowDeathScreen(self):
        self.notificationManager().clearQueue()
        return

    def __onReplayTimeWarpStart(self):
        self.notificationManager().clearQueue()
        return

    def __onObserverVehicleChanged(self, *_):
        self.__initSquadPlayers()
        return

    def __checkTeamInDeffeatedTeams(self):
        observedVehicleID = BigWorld.player().getObservedVehicleID()
        observedVehicleTeam = self.sessionProvider.getArenaDP().getVehicleInfo(observedVehicleID).team
        defeatedTeams = set(self.sessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent.defeatedTeams)
        return observedVehicleTeam in defeatedTeams

    def __onTeamDeath(self, *_):
        if not self.__checkTeamInDeffeatedTeams:
            return
        self.notificationManager().clearQueue()
        return
