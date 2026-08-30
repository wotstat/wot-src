import logging, BigWorld
from constants import ARENA_PERIOD
from gui.battle_control.view_components import ViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.arena_info.interfaces import IRadarController
from gui.battle_control import avatar_getter
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from Event import EventsSubscriber
_logger = logging.getLogger(__name__)

class RadarResponseCode(object):
    SUCCESS, FAILURE, WRONG_ARENA_PERIOD, COOLDOWN, DESTROYED_VEHICLE = range(1, 6)


class IRadarListener(object):

    def startTimeOut(self, timeLeft, duration):
        return

    def timeOutDone(self):
        return

    def radarIsReady(self, isReady):
        return

    def radarActivated(self, radarRadius):
        return

    def radarActivationFailed(self, code):
        return

    def radarInfoReceived(self, radarInfo):
        return

    def reset(self):
        return


class IReplayRadarListener(IRadarListener):

    def setCoolDownTimeSnapshot(self, time):
        return


class RadarController(ViewComponentsController, IRadarController, EventsSubscriber):
    __slots__ = (b'__dynamicViews', b'__callbackID', b'__radarReadinessTime')
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    __INITIAL_VALUE = 0.0

    def __init__(self):
        super(RadarController, self).__init__()
        self.__dynamicViews = []
        self.__callbackID = None
        self.__radarReadinessTime = self.__INITIAL_VALUE
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.RADAR_CTRL

    def startControl(self, *args):
        avatar = BigWorld.player()
        arena = avatar.arena
        if arena is not None:
            self.subscribeToEvent(arena.onRadarInfoReceived, self.__onRadarInfoReceived)
        playerVehicle = avatar.vehicle
        if playerVehicle is not None:
            self.updateRadarReadinessTime(playerVehicle.radar.radarReadinessTime)
        else:
            self.subscribeToEvent(avatar.onVehicleEnterWorld, self.__onVehicleEnterWorld)
        self.subscribeToEvent(self.__guiSessionProvider.onUpdateObservedVehicleData, self.__onUpdateObservedVehicleData)
        return

    def stopControl(self):
        self.__cancelCallback()
        self.unsubscribeFromAllEvents()
        self.clearViewComponents()
        return

    def activateRadar(self):
        avatar = BigWorld.player()
        responseCode = self.__canActivate(avatar)
        if responseCode == RadarResponseCode.SUCCESS:
            avatar.vehicle.cell.radar.activateRadar()
        else:
            allListeners = self._iterAllListeners()
            for listener in allListeners:
                listener.radarActivationFailed(responseCode)

        return

    def updateRadarReadinessTime(self, radarReadinessTime):
        activatedUpdateRequired = False
        if self.__radarReadinessTime != self.__INITIAL_VALUE:
            activatedUpdateRequired = True
        self.__radarReadinessTime = radarReadinessTime
        actualTime = self._calcActualTime()
        if actualTime > 0:
            if activatedUpdateRequired:
                self.__notifyRadarActivated()
            self._notifyTimeOutStarted(actualTime)
            self._launchReloadCallback(actualTime)
        else:
            for listener in self._iterAllListeners():
                listener.reset()

            if BigWorld.player().isObserver():
                self.__clearRadarData()
        return

    def updateRadarReadiness(self, isReady):
        allListeners = self._iterAllListeners()
        for listener in allListeners:
            listener.radarIsReady(isReady)

        return

    def setViewComponents(self, *components):
        self._viewComponents = list(components)
        return

    def clearViewComponents(self):
        super(RadarController, self).clearViewComponents()
        self.__dynamicViews = []
        return

    def addRuntimeView(self, view):
        if view in self.__dynamicViews:
            _logger.warning(b'View already added - %s', view)
        else:
            self.__dynamicViews.append(view)
        return

    def removeRuntimeView(self, view):
        if view in self.__dynamicViews:
            self.__dynamicViews.remove(view)
        return

    @staticmethod
    def _getRadarCooldownTotalTime():
        avatar = BigWorld.player()
        if avatar.vehicle:
            return avatar.vehicle.typeDescriptor.radio.radarCooldown
        return 0

    def _iterAllListeners(self):
        for view in self._viewComponents:
            yield view

        for view in self.__dynamicViews:
            yield view

        return

    def _launchReloadCallback(self, actualTime):
        self.__cancelCallback()
        if self.__guiSessionProvider.shared.arenaPeriod.getPeriod() == ARENA_PERIOD.BATTLE:
            self.__callbackID = BigWorld.callback(actualTime, self._notifyRadarReloaded)
        return

    def _calcActualTime(self):
        return self.__radarReadinessTime - BigWorld.serverTime()

    def _notifyTimeOutStarted(self, actualTime):
        duration = max(self._getRadarCooldownTotalTime(), actualTime)
        for listener in self._iterAllListeners():
            listener.startTimeOut(actualTime, duration)

        return

    def _notifyRadarReloaded(self):
        self.__callbackID = None
        for listener in self._iterAllListeners():
            listener.timeOutDone()

        return

    def __notifyRadarActivated(self):
        for listener in self._iterAllListeners():
            listener.radarActivated(self.__getRadarRadius())

        return

    def __canActivate(self, avatar):
        if avatar is not None:
            ctrl = self.__guiSessionProvider.shared.arenaPeriod
            if ctrl.getPeriod() != ARENA_PERIOD.BATTLE:
                return RadarResponseCode.WRONG_ARENA_PERIOD
            vehicle = avatar.vehicle
            if not vehicle or avatar.vehicle.health <= 0:
                return RadarResponseCode.DESTROYED_VEHICLE
            ctrl = self.__guiSessionProvider.shared.vehicleState
            if avatar.isObserver() or ctrl.isInPostmortem:
                return RadarResponseCode.DESTROYED_VEHICLE
            if avatar.vehicle.radar.radarReadinessTime >= BigWorld.serverTime():
                return RadarResponseCode.COOLDOWN
            return RadarResponseCode.SUCCESS
        else:
            return RadarResponseCode.FAILURE

    @staticmethod
    def __getRadarRadius():
        avatar = BigWorld.player()
        if avatar.vehicle:
            return avatar.vehicle.typeDescriptor.radio.radarRadius
        return 0

    def __onRadarInfoReceived(self, radarInfo):
        if len(radarInfo) != 3:
            _logger.warning(b'Incorrect radar data in BigWorld.player().arena.onRadarInfoReceived')
            return
        for listener in self._iterAllListeners():
            listener.radarInfoReceived(radarInfo)

        return

    def __onVehicleEnterWorld(self, vehicle):
        if vehicle.id == avatar_getter.getPlayerVehicleID():
            BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnterWorld
            self.updateRadarReadinessTime(vehicle.radar.radarReadinessTime)
        return

    def __cancelCallback(self):
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        return

    def __clearRadarData(self):
        for listener in self._iterAllListeners():
            listener.startTimeOut(0.0, 0.0)

        return

    def __onUpdateObservedVehicleData(self, vID, extraData):
        vehicle = BigWorld.entities.get(vID)
        if vehicle and vehicle.isAlive():
            vehicle.radar.refreshRadar()
        else:
            self.__cancelCallback()
        return


class RadarReplayController(RadarController):
    __slots__ = (b'__updateCbId', b'__currentTime', b'__ticksSinceLastUpdate')
    _CB_UPDATE_TIMEOUT = 0.1
    _CB_UPDATE_TICK_DELAY = 3

    def __init__(self):
        super(RadarReplayController, self).__init__()
        self.__updateCbId = None
        self.__currentTime = None
        self.__ticksSinceLastUpdate = self._CB_UPDATE_TICK_DELAY
        return

    def stopControl(self):
        self.__cancelUpdateCB()
        super(RadarReplayController, self).stopControl()
        return

    def _notifyTimeOutStarted(self, _):
        self.__cancelUpdateCB()
        actialTime = self._calcActualTime()
        if actialTime > 0.0:
            if self.__ticksSinceLastUpdate == self._CB_UPDATE_TICK_DELAY:
                super(RadarReplayController, self)._notifyTimeOutStarted(actialTime)
                self.__ticksSinceLastUpdate = 0
            else:
                self.__ticksSinceLastUpdate += 1
            self._notifyCoolDowntTime()
            self.__updateCbId = BigWorld.callback(self._CB_UPDATE_TIMEOUT, self.__updateTimeOut)
        elif self.__currentTime >= 0.0:
            self._notifyRadarReloaded()
            self._notifyCoolDowntTime()
            self.__ticksSinceLastUpdate = 0
        self.__currentTime = actialTime
        return

    def _launchReloadCallback(self, actualTime):
        return

    def __cancelUpdateCB(self):
        if self.__updateCbId:
            BigWorld.cancelCallback(self.__updateCbId)
            self.__updateCbId = None
        return

    def __updateTimeOut(self):
        self.__updateCbId = None
        self._notifyTimeOutStarted(None)
        return

    def _notifyCoolDowntTime(self):
        for listener in self._iterAllListeners():
            if isinstance(listener, IReplayRadarListener):
                listener.setCoolDownTimeSnapshot(self._calcActualTime())

        return
