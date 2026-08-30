from __future__ import absolute_import
import operator
from future.utils import viewitems
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION, LOG_DEBUG
from gui.Scaleform.daapi.view.meta.DamageInfoPanelMeta import DamageInfoPanelMeta
from gui.Scaleform.genConsts.DAMAGE_INFO_PANEL_CONSTS import DAMAGE_INFO_PANEL_CONSTS
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control import avatar_getter
from AvatarInputHandler import AvatarInputHandler
from aih_constants import CTRL_MODE_NAME
_DEVICE_NAME_TO_ID = {b'gunHealth': (DAMAGE_INFO_PANEL_CONSTS.GUN), 
   b'turretRotatorHealth': (DAMAGE_INFO_PANEL_CONSTS.TURRET_ROTATOR), 
   b'surveyingDeviceHealth': (DAMAGE_INFO_PANEL_CONSTS.SURVEYING_DEVICE), 
   b'engineHealth': (DAMAGE_INFO_PANEL_CONSTS.ENGINE), 
   b'fuelTankHealth': (DAMAGE_INFO_PANEL_CONSTS.FUEL_TANK), 
   b'radioHealth': (DAMAGE_INFO_PANEL_CONSTS.RADIO), 
   b'ammoBayHealth': (DAMAGE_INFO_PANEL_CONSTS.AMMO_BAY), 
   b'leftTrack0Health': (DAMAGE_INFO_PANEL_CONSTS.LEFT_TRACK), 
   b'rightTrack0Health': (DAMAGE_INFO_PANEL_CONSTS.RIGHT_TRACK), 
   b'commanderHealth': (DAMAGE_INFO_PANEL_CONSTS.COMMANDER), 
   b'gunner1Health': (DAMAGE_INFO_PANEL_CONSTS.FIRST_GUNNER), 
   b'gunner2Health': (DAMAGE_INFO_PANEL_CONSTS.SECOND_GUNNER), 
   b'driverHealth': (DAMAGE_INFO_PANEL_CONSTS.DRIVER), 
   b'radioman1Health': (DAMAGE_INFO_PANEL_CONSTS.FIRST_RADIOMAN), 
   b'radioman2Health': (DAMAGE_INFO_PANEL_CONSTS.SECOND_RADIOMAN), 
   b'loader1Health': (DAMAGE_INFO_PANEL_CONSTS.FIRST_LOADER), 
   b'loader2Health': (DAMAGE_INFO_PANEL_CONSTS.SECOND_LOADER), 
   b'wheel0Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel1Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel2Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel3Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel4Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel5Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel6Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL), 
   b'wheel7Health': (DAMAGE_INFO_PANEL_CONSTS.WHEEL)}
_DEVICE_HIDE_METHODS = {(DAMAGE_INFO_PANEL_CONSTS.GUN): b'as_hideGunS', 
   (DAMAGE_INFO_PANEL_CONSTS.TURRET_ROTATOR): b'as_hideTurretRotatorS', 
   (DAMAGE_INFO_PANEL_CONSTS.SURVEYING_DEVICE): b'as_hideSurveyingDeviceS', 
   (DAMAGE_INFO_PANEL_CONSTS.ENGINE): b'as_hideEngineS', 
   (DAMAGE_INFO_PANEL_CONSTS.FUEL_TANK): b'as_hideFuelTankS', 
   (DAMAGE_INFO_PANEL_CONSTS.RADIO): b'as_hideRadioS', 
   (DAMAGE_INFO_PANEL_CONSTS.AMMO_BAY): b'as_hideAmmoBayS', 
   (DAMAGE_INFO_PANEL_CONSTS.LEFT_TRACK): b'as_hideLeftTrackS', 
   (DAMAGE_INFO_PANEL_CONSTS.RIGHT_TRACK): b'as_hideRightTrackS', 
   (DAMAGE_INFO_PANEL_CONSTS.WHEEL): b'as_hideWheelS', 
   (DAMAGE_INFO_PANEL_CONSTS.COMMANDER): b'as_hideCommanderS', 
   (DAMAGE_INFO_PANEL_CONSTS.FIRST_GUNNER): b'as_hideFirstGunnerS', 
   (DAMAGE_INFO_PANEL_CONSTS.SECOND_GUNNER): b'as_hideSecondGunnerS', 
   (DAMAGE_INFO_PANEL_CONSTS.DRIVER): b'as_hideDriverS', 
   (DAMAGE_INFO_PANEL_CONSTS.FIRST_RADIOMAN): b'as_hideFirstRadiomanS', 
   (DAMAGE_INFO_PANEL_CONSTS.SECOND_RADIOMAN): b'as_hideSecondRadiomanS', 
   (DAMAGE_INFO_PANEL_CONSTS.FIRST_LOADER): b'as_hideFirstLoaderS', 
   (DAMAGE_INFO_PANEL_CONSTS.SECOND_LOADER): b'as_hideSecondLoaderS'}
_DEVICE_UPDATE_METHODS = {(DAMAGE_INFO_PANEL_CONSTS.GUN): b'as_updateGunS', 
   (DAMAGE_INFO_PANEL_CONSTS.TURRET_ROTATOR): b'as_updateTurretRotatorS', 
   (DAMAGE_INFO_PANEL_CONSTS.SURVEYING_DEVICE): b'as_updateSurveyingDeviceS', 
   (DAMAGE_INFO_PANEL_CONSTS.ENGINE): b'as_updateEngineS', 
   (DAMAGE_INFO_PANEL_CONSTS.FUEL_TANK): b'as_updateFuelTankS', 
   (DAMAGE_INFO_PANEL_CONSTS.RADIO): b'as_updateRadioS', 
   (DAMAGE_INFO_PANEL_CONSTS.AMMO_BAY): b'as_updateAmmoBayS', 
   (DAMAGE_INFO_PANEL_CONSTS.LEFT_TRACK): b'as_updateLeftTrackS', 
   (DAMAGE_INFO_PANEL_CONSTS.RIGHT_TRACK): b'as_updateRightTrackS', 
   (DAMAGE_INFO_PANEL_CONSTS.WHEEL): b'as_updateWheelS', 
   (DAMAGE_INFO_PANEL_CONSTS.COMMANDER): b'as_updateCommanderS', 
   (DAMAGE_INFO_PANEL_CONSTS.FIRST_GUNNER): b'as_updateFirstGunnerS', 
   (DAMAGE_INFO_PANEL_CONSTS.SECOND_GUNNER): b'as_updateSecondGunnerS', 
   (DAMAGE_INFO_PANEL_CONSTS.DRIVER): b'as_updateDriverS', 
   (DAMAGE_INFO_PANEL_CONSTS.FIRST_RADIOMAN): b'as_updateFirstRadiomanS', 
   (DAMAGE_INFO_PANEL_CONSTS.SECOND_RADIOMAN): b'as_updateSecondRadiomanS', 
   (DAMAGE_INFO_PANEL_CONSTS.FIRST_LOADER): b'as_updateFirstLoaderS', 
   (DAMAGE_INFO_PANEL_CONSTS.SECOND_LOADER): b'as_updateSecondLoaderS'}

def _deviceDataConverter(deviceName, state):
    if deviceName not in _DEVICE_NAME_TO_ID:
        LOG_ERROR(b'Device ID is not found', deviceName)
        return None
    else:
        if state == b'destroyed':
            stateID = DAMAGE_INFO_PANEL_CONSTS.DESTROYED
        else:
            stateID = DAMAGE_INFO_PANEL_CONSTS.DAMAGED
        return (_DEVICE_NAME_TO_ID[deviceName], stateID)


def _defaultIterator(fetcher):
    for deviceName, state in fetcher.getDamagedDevices():
        value = _deviceDataConverter(deviceName, state)
        if value is not None:
            yield value

    return


def _yohIterator(fetcher):
    damagedDevices = dict(fetcher.getDamagedDevices())
    for mainTrack, protectingTrack in ((b'leftTrack0Health', b'leftTrack1Health'),
     (b'rightTrack0Health', b'rightTrack1Health')):
        isMainDestroyed = damagedDevices.get(mainTrack) == b'destroyed'
        isProtectingDestroyed = damagedDevices.get(protectingTrack) == b'destroyed'
        damagedDevices.pop(protectingTrack, None)
        if isMainDestroyed or isProtectingDestroyed:
            damagedDevices[mainTrack] = b'destroyed' if isMainDestroyed else b'damaged'
        else:
            damagedDevices.pop(mainTrack, None)

    for deviceName, state in viewitems(damagedDevices):
        value = _deviceDataConverter(deviceName, state)
        if value is not None:
            yield value

    return


def _getDevicesIterator(fetcher, isYoh):
    iterator = _yohIterator if isYoh else _defaultIterator
    for value in iterator(fetcher):
        yield value

    return


def _getDevicesSnapshot(fetcher, isYoh):
    snap = set()
    for deviceID, stateID in _getDevicesIterator(fetcher, isYoh):
        snap.add((deviceID, stateID))

    return snap


class DamageInfoPanel(DamageInfoPanelMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(DamageInfoPanel, self).__init__()
        self.__isShown = False
        self.__vehicleID = 0
        self.__devicesSnap = set()
        self.__isInFire = False
        self.__isTrackWithinTrack = False
        return

    def _populate(self):
        super(DamageInfoPanel, self)._populate()
        feedback = self.sessionProvider.shared.feedback
        if feedback is not None:
            feedback.onVehicleFeedbackReceived += self.__onVehicleFeedbackReceived
        vehicleState = self.sessionProvider.shared.vehicleState
        if vehicleState is not None:
            vehicleState.onPostMortemSwitched += self.__onPostMortemSwitched
            vehicleState.onVehicleControlling += self.__onVehicleControlling
        handler = avatar_getter.getInputHandler()
        if handler is not None:
            if isinstance(handler, AvatarInputHandler):
                handler.onCameraChanged += self.__onCameraChanged
        return

    def _dispose(self):
        vehicleState = self.sessionProvider.shared.vehicleState
        if vehicleState is not None:
            vehicleState.onPostMortemSwitched -= self.__onPostMortemSwitched
            vehicleState.onVehicleControlling -= self.__onVehicleControlling
        feedback = self.sessionProvider.shared.feedback
        if feedback is not None:
            feedback.onVehicleFeedbackReceived -= self.__onVehicleFeedbackReceived
        handler = avatar_getter.getInputHandler()
        if handler is not None:
            if isinstance(handler, AvatarInputHandler):
                handler.onCameraChanged -= self.__onCameraChanged
        self.__devicesSnap.clear()
        self.__isInFire = False
        super(DamageInfoPanel, self)._dispose()
        return

    def __show(self, vehicleID, fetcher):
        vehicleType = self.sessionProvider.arenaVisitor.vehicles.getVehicleInfo(vehicleID).get(b'vehicleType')
        if vehicleType is not None:
            self.__isTrackWithinTrack = vehicleType.isTrackWithinTrack
        if not self.__isShown:
            self.__setDevicesStates(fetcher)
        else:
            self.__updateDevicesStates(vehicleID, fetcher)
        self.__vehicleID = vehicleID
        return

    def __hide(self):
        if not self.__isShown:
            return
        LOG_DEBUG(b'Hides all states of device')
        self.as_hideS()
        self.__vehicleID = 0
        self.__devicesSnap.clear()
        self.__isShown = False
        self.__isTrackWithinTrack = False
        return

    def __setDevicesStates(self, fetcher):
        self.__isShown = True
        items = []
        for deviceID, stateID in _getDevicesIterator(fetcher, self.__isTrackWithinTrack):
            items.append((deviceID, stateID))
            self.__devicesSnap.add((deviceID, stateID))

        self.__isInFire = fetcher.isInFire()
        if self.__isInFire:
            fireID = DAMAGE_INFO_PANEL_CONSTS.SHOW_FIRE
        else:
            fireID = DAMAGE_INFO_PANEL_CONSTS.HIDE_FIRE
        LOG_DEBUG(b'Shows states of devices', items, self.__isInFire)
        self.as_showS(items, fireID)
        return

    def __updateDevicesStates(self, vehicleID, fetcher):
        newDevicesSnap = _getDevicesSnapshot(fetcher, self.__isTrackWithinTrack)
        toHide = self.__devicesSnap.difference(newDevicesSnap)
        toUpdate = dict(newDevicesSnap.difference(self.__devicesSnap))
        for deviceID, _ in toHide:
            if deviceID in toUpdate:
                continue
            if deviceID in _DEVICE_HIDE_METHODS:
                method = _DEVICE_HIDE_METHODS[deviceID]
                LOG_DEBUG(b'Hides state of device', method)
                try:
                    operator.methodcaller(method)(self)
                except (AttributeError, TypeError):
                    LOG_CURRENT_EXCEPTION()

            else:
                LOG_ERROR(b'Method to hide device is not found', deviceID)

        isHit = self.__vehicleID != vehicleID
        for deviceID, stateID in viewitems(toUpdate):
            if deviceID in _DEVICE_UPDATE_METHODS:
                method = _DEVICE_UPDATE_METHODS[deviceID]
                LOG_DEBUG(b'Updates state of device', method, stateID, isHit)
                try:
                    operator.methodcaller(method, stateID, isHit)(self)
                except (AttributeError, TypeError):
                    LOG_CURRENT_EXCEPTION()

            else:
                LOG_ERROR(b'Method to update device is not found', deviceID)

        self.__devicesSnap = newDevicesSnap
        isInFire = fetcher.isInFire()
        if isInFire != self.__isInFire:
            self.__isInFire = isInFire
            if self.__isInFire:
                self.as_showFireS(True)
            else:
                self.as_hideFireS()
        return

    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        if eventID == _EVENT_ID.SHOW_VEHICLE_DAMAGES_DEVICES:
            self.__show(vehicleID, value)
        elif eventID == _EVENT_ID.HIDE_VEHICLE_DAMAGES_DEVICES:
            self.__hide()
        return

    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        self.__hide()
        return

    def __onVehicleControlling(self, vehicle):
        self.__hide()
        return

    def __onCameraChanged(self, mode, vehicleID=0):
        if mode in {CTRL_MODE_NAME.RESPAWN_DEATH, CTRL_MODE_NAME.POSTMORTEM}:
            self.__hide()
        return
