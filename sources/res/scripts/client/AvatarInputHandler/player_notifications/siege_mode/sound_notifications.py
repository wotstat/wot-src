import BigWorld
from components_base.component import Component
import SoundGroups
from constants import VEHICLE_SIEGE_STATE
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE, DEVICE_STATE_DESTROYED
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class SiegeStates(object):
    STARTED = 0
    PAUSED = 1
    STOPPED = 2


def playTriggerSound(soundStateChange):
    if soundStateChange and soundStateChange.trigger:
        SoundGroups.g_instance.playSound2D(soundStateChange.trigger)
    return


def playUnavailableSound(soundStateChange):
    if soundStateChange and soundStateChange.unavailable:
        SoundGroups.g_instance.playSound2D(soundStateChange.unavailable)
    return


class SoundNotifications(object):
    START_TO_SIEGE_MODE = b'start_to_siege_mode_PC'
    START_TO_BASE_MODE = b'start_to_base_mode_PC'
    MOVEMENT_LIMITED_ON = b'strv_siege_mode_movement_limited_on'
    MOVEMENT_LIMITED_OFF = b'strv_siege_mode_movement_limited_off'
    TRANSITION_TIMER = b'siege_mode_transition_timer'
    UI_TURBINE_MODE_ON_STOP = b'ui_turbine_polish_siege_mode_on_stop'
    UI_TURBINE_MODE_OFF_STOP = b'ui_turbine_polish_siege_mode_off_stop'
    UI_TURBINE_MODE_ON = b'ui_turbine_polish_siege_mode_on'
    UI_TURBINE_MODE_OFF = b'ui_turbine_polish_siege_mode_off'
    TWIN_GUN_SWITCH_START = b'gun_rld_dgp_switch_start'
    TWIN_GUN_SWITCH_STOP = b'gun_rld_dgp_switch_stop'


class SiegeModeNotificationsBase(Component):
    _MODE_TYPE = b''

    def __init__(self, vehicleID):
        self.__vehicleID = vehicleID
        return

    @property
    def vehicleID(self):
        return self.__vehicleID

    def start(self):
        return

    def stop(self):
        return

    @classmethod
    def getModeType(cls):
        return cls._MODE_TYPE


class TurboshaftModeSoundNotifications(SiegeModeNotificationsBase):
    _MODE_TYPE = b'turboshaft'

    def __init__(self, vehicleID):
        super(TurboshaftModeSoundNotifications, self).__init__(vehicleID)
        self.__sounds = {(VEHICLE_SIEGE_STATE.SWITCHING_ON): (SoundGroups.g_instance.getSound2D(SoundNotifications.UI_TURBINE_MODE_ON)), 
           (VEHICLE_SIEGE_STATE.SWITCHING_OFF): (SoundGroups.g_instance.getSound2D(SoundNotifications.UI_TURBINE_MODE_OFF)), 
           (VEHICLE_SIEGE_STATE.ENABLED): (SoundGroups.g_instance.getSound2D(SoundNotifications.UI_TURBINE_MODE_ON_STOP)), 
           (VEHICLE_SIEGE_STATE.DISABLED): (SoundGroups.g_instance.getSound2D(SoundNotifications.UI_TURBINE_MODE_OFF_STOP))}
        self.__lastState = None
        self.__engineWasDestroyed = False
        return

    def onSiegeStateChanged(self, vehicleID, newState, _):
        if newState not in self.__sounds or vehicleID != self.vehicleID:
            return
        vehicle = avatar_getter.getPlayerVehicle()
        if vehicle is None or not vehicle.isAlive():
            return
        isEngineDestroyed = BigWorld.player().deviceStates.get(b'engine') == b'destroyed'
        if isEngineDestroyed != self.__engineWasDestroyed:
            if isEngineDestroyed:
                SoundGroups.g_instance.playSound2D(SoundNotifications.MOVEMENT_LIMITED_ON)
            else:
                SoundGroups.g_instance.playSound2D(SoundNotifications.MOVEMENT_LIMITED_OFF)
            self.__engineWasDestroyed = isEngineDestroyed
        if self.__lastState == newState:
            return
        else:
            isValidTransition = self.__lastState is not None and (self.__lastState + 1) % (VEHICLE_SIEGE_STATE.SWITCHING_OFF + 1) == newState
            if self.__lastState:
                self.__sounds[self.__lastState].stop()
            if isValidTransition:
                self.__sounds[newState].play()
            self.__lastState = newState
            return

    def destroy(self):
        if self.__lastState:
            self.__sounds[self.__lastState].stop()
        if self.__engineWasDestroyed:
            SoundGroups.g_instance.playSound2D(SoundNotifications.MOVEMENT_LIMITED_OFF)
        return


class TwinGunModeSoundNotifications(SiegeModeNotificationsBase):
    _MODE_TYPE = b'twinGun'
    __DEVICE = b'gun'
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, vehicleID):
        super(TwinGunModeSoundNotifications, self).__init__(vehicleID)
        self.__vehicleStateUpdatedHandlers = {(VEHICLE_VIEW_STATE.DEVICES): (self.__updateDeviceState), 
           (VEHICLE_VIEW_STATE.REPAIRING): (self.__updateRepairingDevice)}
        self.__siegeTransitionState = SiegeStates.STOPPED
        self.__startSound = SoundGroups.g_instance.getSound2D(SoundNotifications.TWIN_GUN_SWITCH_START)
        return

    def destroy(self):
        self.__clear()
        self.__startSound = None
        return

    def start(self):
        vehicleCtrl = self.__sessionProvider.shared.vehicleState
        if vehicleCtrl is not None:
            vehicleCtrl.onVehicleStateUpdated += self.__onVehicleStateUpdated
        return

    def stop(self):
        vehicleCtrl = self.__sessionProvider.shared.vehicleState
        if vehicleCtrl is not None:
            vehicleCtrl.onVehicleStateUpdated -= self.__onVehicleStateUpdated
        self.__clear()
        return

    def onSiegeStateChanged(self, vehicleID, newState, _):
        if vehicleID != self.vehicleID:
            return
        if BigWorld.player().deviceStates.get(self.__DEVICE) == DEVICE_STATE_DESTROYED:
            return
        isSwitching = newState in VEHICLE_SIEGE_STATE.SWITCHING
        isSwitchingStarted = self.__isSwitchingStarted()
        if isSwitchingStarted == isSwitching:
            return
        if not isSwitchingStarted and isSwitching:
            self.__startSound.play()
            self.__siegeTransitionState = SiegeStates.STARTED
        else:
            self.__stopSound()
            SoundGroups.g_instance.playSound2D(SoundNotifications.TWIN_GUN_SWITCH_STOP)
            self.__siegeTransitionState = SiegeStates.STOPPED
        return

    def __clear(self):
        if self.__isSwitchingStarted():
            self.__stopSound()
        self.__siegeTransitionState = SiegeStates.STOPPED
        self.__vehicleStateUpdatedHandlers = {}
        return

    def __isSwitchingStarted(self):
        return self.__siegeTransitionState == SiegeStates.STARTED

    def __isValidDevice(self, device):
        return device == self.__DEVICE

    def __onVehicleStateUpdated(self, state, value):
        if state in self.__vehicleStateUpdatedHandlers and self.__isValidDevice(value[0]):
            handler = self.__vehicleStateUpdatedHandlers[state]
            handler(value)
        return

    def __playGunDestroyedSound(self):
        vehicle = avatar_getter.getPlayerVehicle()
        if vehicle is not None:
            siegeModeParams = vehicle.typeDescriptor.type.siegeModeParams
            soundStateChange = siegeModeParams[b'soundStateChange'] if siegeModeParams else None
            playUnavailableSound(soundStateChange)
        return

    def __stopSound(self):
        if self.__startSound.isPlaying:
            self.__startSound.stop()
        return

    def __updateDeviceState(self, value):
        _, deviceState, __ = value
        if deviceState == DEVICE_STATE_DESTROYED and self.__isSwitchingStarted():
            self.__playGunDestroyedSound()
            self.__stopSound()
            SoundGroups.g_instance.playSound2D(SoundNotifications.TWIN_GUN_SWITCH_STOP)
            self.__siegeTransitionState = SiegeStates.PAUSED
        return

    def __updateRepairingDevice(self, value):
        if self.__siegeTransitionState == SiegeStates.PAUSED:
            _, progress, _, __ = value
            if progress == 0:
                self.__playGunDestroyedSound()
        return


class SiegeModeSoundNotifications(SiegeModeNotificationsBase):
    _MODE_TYPE = b'siege'

    def __init__(self, vehicleID):
        super(SiegeModeSoundNotifications, self).__init__(vehicleID)
        self.__sounds = {(SoundNotifications.START_TO_SIEGE_MODE): (SoundGroups.g_instance.getSound2D(SoundNotifications.START_TO_SIEGE_MODE)), 
           (SoundNotifications.START_TO_BASE_MODE): (SoundGroups.g_instance.getSound2D(SoundNotifications.START_TO_BASE_MODE))}
        self.__engineWasDestroyed = False
        self.__siegeCallback = None
        return

    def stop(self):
        self.__clear()
        return

    def destroy(self):
        self.__clear()
        self.__sounds = None
        return

    def onSiegeStateChanged(self, vehicleID, newState, timeToNextMode):
        if self.__sounds is None or self.vehicleID != vehicleID:
            return
        goToSiegeMode = newState == VEHICLE_SIEGE_STATE.SWITCHING_ON
        goToBaseMode = newState == VEHICLE_SIEGE_STATE.SWITCHING_OFF
        siegeModeEnabled = newState == VEHICLE_SIEGE_STATE.ENABLED
        siegeModeDisabled = newState == VEHICLE_SIEGE_STATE.DISABLED
        isValidState = goToSiegeMode or goToBaseMode or siegeModeEnabled or siegeModeDisabled
        if not isValidState:
            return
        else:
            eventId = SoundNotifications.START_TO_SIEGE_MODE
            if goToBaseMode or siegeModeDisabled:
                eventId = SoundNotifications.START_TO_BASE_MODE
            isEngineDestroyed = BigWorld.player().deviceStates.get(b'engine') == b'destroyed'
            if isEngineDestroyed != self.__engineWasDestroyed:
                if isEngineDestroyed:
                    SoundGroups.g_instance.playSound2D(SoundNotifications.MOVEMENT_LIMITED_ON)
                else:
                    SoundGroups.g_instance.playSound2D(SoundNotifications.MOVEMENT_LIMITED_OFF)
                self.__engineWasDestroyed = isEngineDestroyed
            if goToSiegeMode:
                if self.__siegeCallback is not None:
                    BigWorld.cancelCallback(self.__siegeCallback)
                    self.__siegeCallback = None
                if not isEngineDestroyed:
                    deltaTime = timeToNextMode - 1.0 if timeToNextMode > 1.0 else 0.0
                    self.__siegeCallback = BigWorld.callback(deltaTime, self.__onSiegeTimer)
            shouldStopSound = siegeModeEnabled or siegeModeDisabled or isEngineDestroyed
            sound = self.__sounds[eventId]
            if sound is None:
                return
            if shouldStopSound:
                sound.stop()
            elif not sound.isPlaying:
                sound.play()
            return

    def __onSiegeTimer(self):
        SoundGroups.g_instance.playSound2D(SoundNotifications.TRANSITION_TIMER)
        self.__siegeCallback = None
        return

    def __clear(self):
        if self.__sounds is not None:
            for sound in self.__sounds.itervalues():
                if sound is not None:
                    sound.stop()

        if self.__engineWasDestroyed:
            SoundGroups.g_instance.playSound2D(SoundNotifications.MOVEMENT_LIMITED_OFF)
        if self.__siegeCallback is not None:
            BigWorld.cancelCallback(self.__siegeCallback)
        return


class PillboxSiegeSoundNotifications(SiegeModeSoundNotifications):
    _PILLBOX_COMPONENT_NAME = b'pillboxSiegeComponent'

    def onSiegeStateChanged(self, vehicleID, newState, timeToNextMode):
        if newState in VEHICLE_SIEGE_STATE.SWITCHING:
            vehicle = BigWorld.entities.get(vehicleID)
            if vehicle is not None:
                pillboxSiege = vehicle.dynamicComponents.get(self._PILLBOX_COMPONENT_NAME)
                if pillboxSiege is not None:
                    status = pillboxSiege.publicStatus
                    if status.state == VEHICLE_SIEGE_STATE.PILLBOX_ENABLED or status.nextState == VEHICLE_SIEGE_STATE.PILLBOX_ENABLED:
                        super(PillboxSiegeSoundNotifications, self).onSiegeStateChanged(vehicleID, VEHICLE_SIEGE_STATE.PILLBOX_ENABLED, timeToNextMode)
        super(PillboxSiegeSoundNotifications, self).onSiegeStateChanged(vehicleID, newState, timeToNextMode)
        return
