import logging, weakref, typing, BigWorld, constants, Keys, Math, BattleReplay, math_utils, GUI, CommandMapping as CM
from PlayerEvents import g_playerEvents
from battleground.simulated_scene import SimulatedScene, ANIMATION_DURATION_BEFORE_SHOT
from constants import ATTACK_REASON, ATTACK_REASONS, ARENA_PERIOD, DEFAULT_GUN_INSTALLATION_INDEX, POSTMORTEM_MODIFIERS
from gui.battle_control.arena_info.interfaces import IBattleFieldController
from gui.shared.events import DeathCamEvent
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from wotdecorators import noexcept
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera
from AvatarInputHandler.DynamicCameras.kill_cam_camera import KillCamera, StartCamDirection, LOOK_AT_KILLER_DURATION
from control_modes import IControlMode, _readCameraTransitionSettings
from aih_constants import CTRL_MODE_NAME
from helpers import dependency, uniprof
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider
from PostmortemDelay import PostmortemDelay
from account_helpers.AccountSettings import AccountSettings, WHEELED_DEATH_DELAY_COUNT
if typing.TYPE_CHECKING:
    from typing import Dict, Any
_PARTICLES_DURATION_AFTER_SHOT = 0.0
_PREPARE_KILLER_VISION_FADE_TIME = 0.8
_SHOW_KILLER_VISION_FADE_TIME = 1.0
_LEAVE_KILLER_VISION_FADE_TIME = 0.8
_SHOW_DEAD_TANK_FADE_TIME = 1.0
_START_VISION_DELAY = 1.0
_KILL_CAM_WAIT_TIME = 2.0
_TIME_BEFORE_FOLLOW_TANK = 2.0
_WHEELED_VEHICLE_POSTMORTEM_DELAY = 3.0
_LOOK_AT_KILLER_DURATION_LEGACY = 2.0
_LOOK_AT_KILLER_SUBSTITUTE_WAIT_TIME = 5
_NO_SKIP_DEATH_CAM_DURATION = 2.0
_PAUSE_BUTTON_COOLDOWN = 0.5
_SKIP_KILL_CAM_BEFORE_AUTORESPAWN_TIME = 15
_RADIUS = 10
_RADIUS_ALPHA = 2
_BLOCKED_KEYS = {
 Keys.KEY_LCONTROL,
 Keys.KEY_RCONTROL,
 Keys.KEY_T,
 Keys.KEY_M,
 Keys.KEY_B,
 Keys.KEY_N,
 Keys.KEY_TAB}
_BLOCKED_ACTIONS = (
 CM.CMD_SHOW_HELP,)
_BLACK_BG_IMG = b'gui/maps/login/blackBg.png'
_logger = logging.getLogger(__name__)

class SimulationAvailability(object):
    AVAILABLE = 0
    NOT_AVAILABLE_MISSING_DATA = 1
    NOT_AVAILABLE_END_OF_BATTLE = 2
    VEHICLES_TOO_CLOSE = 3
    NOT_KILLED_BY_SHOT = 4
    NOT_SUPPORTED_MODE = 5
    NOT_ENOUGH_TIME = 6
    NOT_AVAILABLE = (NOT_AVAILABLE_MISSING_DATA, NOT_AVAILABLE_END_OF_BATTLE, VEHICLES_TOO_CLOSE, NOT_KILLED_BY_SHOT,
     NOT_SUPPORTED_MODE, NOT_ENOUGH_TIME)


class KillModeBase(IControlMode, CallbackDelayer):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, dataSection, avatarInputHandler):
        super(KillModeBase, self).__init__()
        CallbackDelayer.__init__(self)
        self._modeEnteredTime = -1
        self._victimVehicleID = None
        self._killerVehicleID = None
        self._rawSimulationData = None
        self._trajectoryPoints = [None, None]
        self._postmortemKwargs = None
        self._skipBattleTimeLeft = dataSection.readFloat(b'skipBattleTimeLeft')
        self._cameraTransitionDurations = _readCameraTransitionSettings(dataSection[b'camera'])
        self._aih = weakref.proxy(avatarInputHandler)
        self._cam = KillCamera(dataSection[b'camera'], dataSection.readVector2(b'defaultOffset'))
        self.__killCamState = DeathCamEvent.State.NONE
        return

    @property
    def camera(self):
        return self._cam

    @property
    def curVehicleID(self):
        return self._victimVehicleID

    @property
    def killCamCtrl(self):
        return self.guiSessionProvider.shared.killCamCtrl

    @property
    def killCamState(self):
        return self.__killCamState

    @property
    def _killerIsSpotted(self):
        return self._rawSimulationData and self._rawSimulationData.get(b'attacker', {}).get(b'spotted')

    def create(self):
        self._cam.create(onChangeControlMode=None, postmortemMode=True, smartPointCalculator=True)
        return

    def destroy(self):
        self.disable(smoothFade=False)
        self._cam.destroy()
        self._cam = None
        self._aih = None
        self.clearCallbacks()
        return

    def enable(self, **kwargs):
        _logger.info(b'[%s] %s is Enabled', self.__class__.__name__, self.__class__.__name__)
        self._modeEnteredTime = BigWorld.time()
        avatar = BigWorld.player()
        if avatar is None:
            _logger.error(b'Avatar is None, cannot enter %s.', self.__class__.__name__)
            return
        else:
            self._changeKillCamModeState(DeathCamEvent.State.NONE)
            self._victimVehicleID = avatar.playerVehicleID
            self._postmortemKwargs = kwargs
            self._postmortemKwargs[b'newVehicleID'] = BigWorld.player().playerVehicleID
            vehicleMProv = avatar.consistentMatrices.attachedVehicleMatrix
            camAngles = None
            pivotSettings = None
            previousCam = None
            isInArcadeZoomState = False
            if b'previousCam' in kwargs:
                previousCam = kwargs[b'previousCam']
                camAngles = getattr(previousCam, b'angles', None)
                if isinstance(previousCam, ArcadeCamera):
                    pivotSettings = previousCam.aimingSystem.getPivotSettings()
                    isInArcadeZoomState = previousCam.isInArcadeZoomState()
            if previousCam is None or not isInArcadeZoomState or pivotSettings is None:
                pivotSettings = PostmortemDelay.KILLER_VEHICLE_CAMERA_PIVOT_SETTINGS
            self._cam.enable(vehicleMProv=vehicleMProv, preferredPos=camAngles, initialPivotSettings=pivotSettings)
            killerVehicleID = self._aih.getKillerVehicleID()
            deathReason = self._aih.getDeathReason()
            if killerVehicleID is None and deathReason is None:
                self._aih.onReceivedKillerID += self.__onReceiveKillerID
            else:
                self.__onReceiveKillerID(killerVehicleID)
            return

    def disable(self, smoothFade=True):
        _logger.info(b'[%s] disable()', self.__class__.__name__)
        self._modeEnteredTime = -1
        self._postmortemKwargs = None
        self._cam.disable()
        self.clearCallbacks()
        self._aih.onReceivedKillerID -= self.__onReceiveKillerID
        return

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if key in _BLOCKED_KEYS or CM.g_instance.isFiredList(_BLOCKED_ACTIONS, key):
            return True
        if BattleReplay.g_replayCtrl.isPlaying or not self._canSkipKillCamera():
            return False
        if CM.g_instance.isFired(CM.CMD_CM_POSTMORTEM_SELF_VEHICLE, key) and isDown and self._canSwitchToFreecam():
            self._switchToCtrlMode(CTRL_MODE_NAME.DEATH_FREE_CAM)
            return True
        if key in (Keys.KEY_LEFTMOUSE, Keys.KEY_RIGHTMOUSE) and not isDown:
            self._switchToCtrlMode(CTRL_MODE_NAME.POSTMORTEM, immediateSwitchToAllyVehicle=self._canSwitchToAllyVehicle())
            return True
        return False

    def _leaveMode(self):
        raise NotImplementedError(b'Implement in inheriting classes!')
        return

    def _handleModeExecution(self):
        raise NotImplementedError(b'Implement in inheriting classes!')
        return

    def _changeKillCamModeState(self, newState):
        self.__killCamState = newState
        _logger.info(b'%s: Kill Cam State changed to: %s', self.__class__.__name__, self.__killCamState)
        if self.killCamCtrl:
            self.killCamCtrl.changeKillCamModeState(self.__killCamState)
        return

    def _canShowKillerVisionInPeriod(self):
        periodCtrl = self.guiSessionProvider.shared.arenaPeriod
        if not periodCtrl:
            return False
        if BattleReplay.g_replayCtrl.isPlaying:
            return True
        isBattlePeriod = periodCtrl.getPeriod() == ARENA_PERIOD.BATTLE
        isTimeLeft = periodCtrl.getEndTime() - BigWorld.serverTime() > self._skipBattleTimeLeft
        return isBattlePeriod and isTimeLeft

    def _areBothTeamsAlive(self):
        avatar = BigWorld.player()
        battleFieldCtrl = self.guiSessionProvider.dynamic.battleField
        if not avatar or not battleFieldCtrl:
            return False
        if BattleReplay.g_replayCtrl.isPlaying:
            return True
        allies, enemies = battleFieldCtrl.getAliveVehicles()
        if not allies and not avatar.isPostmortemModificationActive(CTRL_MODE_NAME.KILL_CAM, POSTMORTEM_MODIFIERS.ENABLED_IF_NO_ALLY):
            _logger.debug(b'Skip KillerVision because no allies are left alive and battle will end')
            return False
        if not enemies:
            _logger.debug(b'Skip KillerVision because no enemies are left alive and battle will end')
            return False
        return True

    def _checkSimulationAvailability(self):
        avatar = BigWorld.player()
        vehicle = avatar.vehicle
        if vehicle is None:
            vehicle = BigWorld.entity(avatar.playerVehicleID)
        if not self._canShowKillerVisionInPeriod():
            _logger.info(b'The battle ends soon - shorten Look At Killer rotation or skip Killer Vision')
            return (
             SimulationAvailability.NOT_AVAILABLE_END_OF_BATTLE, None)
        else:
            if b'killCamData' not in vehicle.dynamicComponents:
                _logger.info(b"Player doesn't have killCamData available")
                return (
                 SimulationAvailability.NOT_AVAILABLE_MISSING_DATA, None)
            if not self._isKillByShot():
                _logger.info(b"Player wasn't killed by shot")
                return (
                 SimulationAvailability.NOT_KILLED_BY_SHOT, None)
            simulationData = self.__getRawSimulationData(vehicle)
            if not self._validateRawSimulationData(simulationData):
                _logger.info(b'Skip KillerVision because no simulation data are available')
                return (
                 SimulationAvailability.NOT_AVAILABLE_MISSING_DATA, None)
            return (SimulationAvailability.AVAILABLE, simulationData)

    def _validateRawSimulationData(self, rawSimulationData):
        if rawSimulationData is None:
            return False
        else:
            attackerData = rawSimulationData.get(b'attacker', None)
            trajectoryData = rawSimulationData.get(b'trajectoryData', None)
            if not attackerData or not trajectoryData:
                _logger.error(b'_validateRawSimulationData(): Missing attackerData %s, or trajectoryData %s', attackerData, trajectoryData)
                return False
            return True

    def _canSkipKillCamera(self):
        if BigWorld.time() - self._modeEnteredTime < _NO_SKIP_DEATH_CAM_DURATION:
            return False
        return True

    def _canSwitchToFreecam(self):
        if not self._canSkipKillCamera():
            return False
        respawnCtrl = self.guiSessionProvider.dynamic.respawn
        needToRespawn = respawnCtrl and respawnCtrl.playerLives > 0
        if needToRespawn:
            return False
        return BigWorld.player().isPostmortemFeatureEnabled(CTRL_MODE_NAME.DEATH_FREE_CAM)

    def _canSwitchToAllyVehicle(self):
        return True

    def _switchToCtrlMode(self, targetMode, **kwargs):
        if targetMode != CTRL_MODE_NAME.DEATH_FREE_CAM:
            self.selectPlayer(None)
        newVehicleID = BigWorld.player().playerVehicleID if targetMode in (CTRL_MODE_NAME.POSTMORTEM,
         CTRL_MODE_NAME.DEATH_FREE_CAM) else None
        BigWorld.player().inputHandler.onControlModeChanged(targetMode, prevModeName=CTRL_MODE_NAME.KILL_CAM, camMatrix=Math.Matrix(BigWorld.camera().matrix), curVehicleID=self._victimVehicleID, newVehicleID=newVehicleID, transitionDuration=self._cameraTransitionDurations[targetMode], **kwargs)
        return

    def _isKillByShot(self):
        deathReasonID = BigWorld.player().inputHandler.getDeathReason()
        return deathReasonID is not None and ATTACK_REASONS[deathReasonID] in (
         ATTACK_REASON.SHOT, ATTACK_REASON.FIRE)

    def _isFirstTenDeathsWheeledTank(self, vehicleID):
        vehicle = BigWorld.entities.get(vehicleID)
        if vehicle is None or not vehicle.isWheeledTech:
            return False
        wheeledDeathCountLeft = AccountSettings.getSettings(WHEELED_DEATH_DELAY_COUNT)
        if wheeledDeathCountLeft == 0:
            return False
        else:
            return True

    def _tryDecrementWheeledDeathCounter(self, vehicleID):
        if self._isFirstTenDeathsWheeledTank(vehicleID):
            wheeledDeathCountLeft = AccountSettings.getSettings(WHEELED_DEATH_DELAY_COUNT)
            AccountSettings.setSettings(WHEELED_DEATH_DELAY_COUNT, max(wheeledDeathCountLeft - 1, 0))
        return

    def __getRawSimulationData(self, vehicle):
        if not vehicle:
            _logger.error(b"__getRawSimulationData: Unable to get player's vehicle")
            return None
        else:
            rawSimulationData = vehicle.killCamData.getSimulationData()
            return rawSimulationData

    def __onReceiveKillerID(self, vehicleID):
        self._killerVehicleID = vehicleID
        playerVehicle = BigWorld.entities.get(self._victimVehicleID)
        isDefinedPostmortemView = playerVehicle and playerVehicle.isPostmortemViewPointDefined
        if isDefinedPostmortemView:
            _logger.info(b'[%s] Leave %s (in base class): we have a predefined postmortem view - leave mode', self.__class__.__name__, self.__class__.__name__)
            self._leaveMode()
        else:
            self._handleModeExecution()
        return


class KillCamMode(KillModeBase):

    def __init__(self, dataSection, avatarInputHandler):
        super(KillCamMode, self).__init__(dataSection, avatarInputHandler)
        self.__isLeaveKillCamWhenPrepared = False
        self.__bFadeScreenActive = False
        self.__lastTimePauseToggled = 0.0
        self.__vehicleRespawnTriggered = False
        self.__isAutoRespawnScheduled = False
        self.__simulatedVictimID = None
        self.__simulatedKillerID = None
        self.__unspottedOrigin = None
        self.__simulatedScene = SimulatedScene(dataSection[b'deathCamPostProcessEffects'])
        self.__skipKillCamDistance = dataSection.readFloat(b'skipKillCamVehiclesDistance')
        self._skipBattleTimeLeft = dataSection.readFloat(b'skipBattleTimeLeft')
        self._skipNotEnoughTimeForDC = dataSection.readFloat(b'skipNotEnoughTimeForDC')
        return

    @property
    def __isRicochet(self):
        return self._rawSimulationData[b'projectile'][b'ricochetCount'] > 0

    def create(self):
        super(KillCamMode, self).create()
        ctrl = self.guiSessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched += self.__onSwitchToPostmortem
        self.__simulatedScene.create()
        return

    def destroy(self):
        super(KillCamMode, self).destroy()
        ctrl = self.guiSessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched -= self.__onSwitchToPostmortem
        self.__simulatedScene.destroy()
        self.__simulatedScene = None
        return

    def enable(self, **kwargs):
        uniprof.enterToRegion(b'avatar.control_mode.kill_cam')
        respawnCtrl = self.guiSessionProvider.dynamic.respawn
        if respawnCtrl is not None:
            respawnCtrl.onRespawnInfoUpdated += self.__onRespawnInfoUpdate
        BigWorld.wg_setTreeHidingRadius(_RADIUS, _RADIUS_ALPHA)
        g_playerEvents.onArenaPeriodChange += self.__onArenaPeriodChanged
        if self.killCamCtrl:
            self.killCamCtrl.onRespawnRequested += self.__onVehicleRespawn
        self.__simulatedScene.onAllVehiclesLoaded += self.__onAllVehiclesLoaded
        self.__simulatedScene.onSimulatedSceneHasEnded += self.__simulatedSceneEnded
        self._changeKillCamModeState(DeathCamEvent.State.INACTIVE)
        if not self._aih.appLoader.getApp().hasGuiControlModeConsumers(VIEW_ALIAS.INGAME_MENU):
            self._aih.setForcedGuiControlMode(False)
        super(KillCamMode, self).enable(**kwargs)
        return

    def disable(self, smoothFade=True):
        super(KillCamMode, self).disable(smoothFade)
        self.__isLeaveKillCamWhenPrepared = False
        self._rawSimulationData = None
        self.__vehicleRespawnTriggered = False
        self.__isAutoRespawnScheduled = False
        self.__simulatedScene.onAnimationsCompleted -= self.__onVehicleAnimationFinished
        self.__simulatedScene.disableScene()
        BigWorld.wg_setHideEdges(False)
        respawnCtrl = self.guiSessionProvider.dynamic.respawn
        if respawnCtrl is not None:
            respawnCtrl.onRespawnInfoUpdated -= self.__onRespawnInfoUpdate
        if self.__bFadeScreenActive:
            self.__fadeScreen(False, _LEAVE_KILLER_VISION_FADE_TIME if smoothFade else 0.0)
        g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChanged
        if self.killCamCtrl:
            self.killCamCtrl.onRespawnRequested -= self.__onVehicleRespawn
        self.__simulatedScene.onAllVehiclesLoaded -= self.__onAllVehiclesLoaded
        self.__simulatedScene.onSimulatedSceneHasEnded -= self.__simulatedSceneEnded
        if self.killCamState not in (DeathCamEvent.State.NONE, DeathCamEvent.State.FINISHED):
            self._changeKillCamModeState(DeathCamEvent.State.FINISHED)
        uniprof.exitFromRegion(b'avatar.control_mode.kill_cam')
        return

    def handleKeyEvent(self, isDown, key, mods, event=None):
        handledInBase = super(KillCamMode, self).handleKeyEvent(isDown, key, mods, event)
        if handledInBase:
            return True
        if key == Keys.KEY_ESCAPE and isDown:
            replayCtrl = BattleReplay.g_replayCtrl
            if replayCtrl.isPaused:
                replayCtrl.resetPlaybackSpeedIdx()
            if self.killCamState in DeathCamEvent.SIMULATION_INCL_FADES:
                self.__fadeAndLeaveKillCam(isInterrupted=True)
                return True
            self.__isLeaveKillCamWhenPrepared = True
        if BattleReplay.g_replayCtrl.isPlaying:
            return self.handleReplayKeyEvent(isDown, key)
        if key == Keys.KEY_SPACE and isDown:
            if self.killCamState in DeathCamEvent.SIMULATION_EXCL_FADES:
                self.togglePauseKillCam()
                return True
        return False

    def handleReplayKeyEvent(self, isDown, key):
        replayCtrl = BattleReplay.g_replayCtrl
        isReplayPaused = replayCtrl.isPlaying and replayCtrl.isPaused
        if key == Keys.KEY_SPACE and isDown:
            if self.killCamState not in DeathCamEvent.SIMULATION_EXCL_FADES:
                if isReplayPaused:
                    replayCtrl.resetPlaybackSpeedIdx()
                else:
                    replayCtrl.setPlaybackSpeedIdx(0)
            elif self.killCamState in DeathCamEvent.SIMULATION_EXCL_FADES:
                self.togglePauseKillCam()
            return True
        if key == Keys.KEY_RIGHTARROW and not isDown:
            if self.killCamState in DeathCamEvent.SIMULATION_EXCL_FADES:
                self.__fadeAndLeaveKillCam(isInterrupted=True)
                if isReplayPaused:
                    replayCtrl.resetPlaybackSpeedIdx()
                return True
        return False

    def handleMouseEvent(self, dx, dy, dz):
        self._cam.update(dx, dy, math_utils.clamp(-1, 1, dz))
        GUI.mcursor().position = Math.Vector2(0, 0)
        return True

    def isSelfVehicle(self):
        return False

    def togglePauseKillCam(self):
        if self.killCamState == DeathCamEvent.State.ENDING:
            return
        replayCtrl = BattleReplay.g_replayCtrl
        isPauseCooldownActive = BigWorld.time() - self.__lastTimePauseToggled < _PAUSE_BUTTON_COOLDOWN
        isReplayPaused = replayCtrl.isPlaying and replayCtrl.isPaused
        if not isReplayPaused and isPauseCooldownActive:
            return
        self.__lastTimePauseToggled = BigWorld.time()
        if self.killCamState == DeathCamEvent.State.RESUME or self.killCamState == DeathCamEvent.State.ACTIVE:
            self._changeKillCamModeState(DeathCamEvent.State.PAUSE)
            if replayCtrl.isPlaying:
                replayCtrl.setPlaybackSpeedIdx(0)
            self.__pauseResumeChanged(True)
        elif self.killCamState == DeathCamEvent.State.PAUSE:
            self._changeKillCamModeState(DeathCamEvent.State.RESUME)
            if replayCtrl.isPlaying:
                replayCtrl.resetPlaybackSpeedIdx(allowResetToZero=True)
            self.__pauseResumeChanged(False)
        else:
            _logger.error(b"KillCamMode: Pausing kill cam during phase when it's not allowed")
        return

    def _handleModeExecution(self):
        _logger.info(b'[KillCamCtrlMode] _handleModeExecution()')
        waitTime = 0.0
        if not BigWorld.player().isPostmortemFeatureEnabled(CTRL_MODE_NAME.LOOK_AT_KILLER):
            self._tryDecrementWheeledDeathCounter(self._victimVehicleID)
            waitTime = _KILL_CAM_WAIT_TIME + _LOOK_AT_KILLER_SUBSTITUTE_WAIT_TIME - _PREPARE_KILLER_VISION_FADE_TIME
        self.delayCallback(waitTime, self.__initializeSimulationData)
        return

    @noexcept
    def _leaveMode(self):
        _logger.info(b'[KillCamCtrlMode] _leaveMode()')
        if self.killCamCtrl:
            self.killCamCtrl.simulationSceneActive(False)
        self.clearCallbacks()
        self.__simulatedScene.onAnimationsCompleted -= self.__onVehicleAnimationFinished
        self.__simulatedScene.disableScene()
        self._cam.disable()
        return

    def _canSkipKillCamera(self):
        if not BigWorld.player().isPostmortemFeatureEnabled(CTRL_MODE_NAME.LOOK_AT_KILLER):
            if not super(KillCamMode, self)._canSkipKillCamera():
                return False
        if self.killCamState in DeathCamEvent.SIMULATION_EXCL_FADES or self.killCamState == DeathCamEvent.State.ENDING:
            return False
        if self.__bFadeScreenActive:
            return False
        return True

    def _switchToCtrlMode(self, targetMode, **kwargs):
        if self.killCamState == DeathCamEvent.State.PREPARING:
            return
        super(KillCamMode, self)._switchToCtrlMode(targetMode, **kwargs)
        return

    def _checkSimulationAvailability(self):
        avatar = BigWorld.player()
        vehicle = avatar.vehicle
        if vehicle is None:
            vehicle = BigWorld.entity(avatar.playerVehicleID)
        if not self._areBothTeamsAlive():
            return (
             SimulationAvailability.NOT_AVAILABLE_END_OF_BATTLE, None)
        else:
            availability, simulationData = super(KillCamMode, self)._checkSimulationAvailability()
            if availability is not SimulationAvailability.AVAILABLE:
                return (availability, None)
            if avatar.arenaExtraData.get(b'isRandomEventsAllowed', False):
                postmortemSettings = avatar.arenaExtraData.get(b'postmortemSettings', {})
                killcamConfig = postmortemSettings.get(b'config', {}).get(b'killcam', {})
                isAllowedForRandomEvents = killcamConfig.get(b'isAllowedForRandomEvents', False)
                if not isAllowedForRandomEvents:
                    _logger.info(b'Skip DeathCam scene because Random Events are not supported')
                    return (
                     SimulationAvailability.NOT_SUPPORTED_MODE, None)
            if not self.killCamCtrl:
                _logger.warning(b"DeathCam is enabled but can't find killCamCtrl")
                return (
                 SimulationAvailability.NOT_SUPPORTED_MODE, None)
            if b'VehicleRespawnComponent' in vehicle.dynamicComponents:
                delay = vehicle.dynamicComponents.get(b'VehicleRespawnComponent').delay
                if 0 < delay < self._skipNotEnoughTimeForDC:
                    _logger.info(b'Not enough time to show DeathCam before respawn!')
                    return (
                     SimulationAvailability.NOT_ENOUGH_TIME, None)
            battleFieldCtrl = self.guiSessionProvider.dynamic.battleField
            if not battleFieldCtrl:
                _logger.error(b'Error, battle field controller not available')
                return (
                 SimulationAvailability.NOT_AVAILABLE_MISSING_DATA, None)
            if not self.__isDistanceFarEnough(simulationData):
                _logger.info(b'Skip KillerVision because vehicles are too close to each other')
                return (
                 SimulationAvailability.VEHICLES_TOO_CLOSE, None)
            return (SimulationAvailability.AVAILABLE, simulationData)

    def _validateRawSimulationData(self, rawSimulationData):
        if not super(KillCamMode, self)._validateRawSimulationData(rawSimulationData):
            return False
        else:
            playerData = rawSimulationData.get(b'player', None)
            projectileData = rawSimulationData.get(b'projectile', None)
            unspottedOrigin = rawSimulationData.get(b'unspottedOrigin', None)
            if not playerData or not projectileData:
                _logger.error(b'_validateRawSimulationData():Missing playerData %s, projectileData %s, or unspottedOrigin %s', playerData, projectileData, unspottedOrigin)
                return False
            return True

    def __onSwitchToPostmortem(self, noRespawnPossible, respawnAvailable):
        _logger.info(b'[KillCamCtrlMode]: __onSwitchToPostmortem: saving kill snapshot')
        self.__simulatedScene.saveKillSnapshot()
        return

    def __initializeSimulationData(self):
        simulationAvailability, self._rawSimulationData = self._checkSimulationAvailability()
        if simulationAvailability != SimulationAvailability.AVAILABLE:
            self.__skipKillCam(simulationAvailability)
            return
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isControllingCamera:
            BattleReplay.g_replayCtrl.stopCameraControl()
        self._trajectoryPoints = self._rawSimulationData[b'trajectoryData']
        self.__unspottedOrigin = self._rawSimulationData[b'unspottedOrigin']
        projectile = self._rawSimulationData[b'projectile']
        shotID = projectile.get(b'shotID', 0)
        self.__simulatedScene.setPendingShotID(shotID)
        self._postmortemKwargs[b'bPostmortemDelay'] = False
        self.__fadeAndPrepareKillCamData()
        return

    def __skipKillCam(self, simulationAvailability):
        _logger.info(b'[KillCamCtrlMode] __skipKillCam()')
        suicide = self._killerVehicleID == self._victimVehicleID
        isKillerSpotted = BigWorld.entity(self._killerVehicleID) is not None
        if not suicide and isKillerSpotted:
            self._postmortemKwargs[b'keepCameraSettings'] = True
        if suicide or simulationAvailability == SimulationAvailability.NOT_AVAILABLE_END_OF_BATTLE:
            self._postmortemKwargs[b'bPostmortemDelay'] = False
        self._leaveMode()
        return

    def __fadeAndPrepareKillCamData(self):
        uniprof.exitFromRegion(b'avatar.control_mode.kill_cam.initialCamera')
        if self.__isLeaveKillCamWhenPrepared or not self._canShowKillerVisionInPeriod() or not self._areBothTeamsAlive():
            _logger.info(b'[KillCamCtrlMode] __fadeAndPrepareKillCamData: Battle ended while preparing')
            self._leaveMode()
            return
        self._changeKillCamModeState(DeathCamEvent.State.PREPARING)
        BigWorld.wg_setHideEdges(True)
        self.__fadeScreen(True, _PREPARE_KILLER_VISION_FADE_TIME)
        self.delayCallback(_PREPARE_KILLER_VISION_FADE_TIME, self.__prepareAnimationsAndCam)
        return

    def __prepareAnimationsAndCam(self):
        self.__simulatedScene.onAnimationsCompleted += self.__onVehicleAnimationFinished
        self.__simulatedScene.enableScene(self._rawSimulationData, self._trajectoryPoints, self._killerIsSpotted)
        self.__simulatedKillerID = self.__simulatedScene.simulatedKillerID
        self.__simulatedVictimID = self.__simulatedScene.simulatedVictimID
        self._cam.trajectoryPoints = self._trajectoryPoints
        self._cam.playerHuskID = self.__simulatedVictimID
        self._changeKillCamModeState(DeathCamEvent.State.STARTING)
        return

    def __onAllVehiclesLoaded(self):
        self.delayCallback(_START_VISION_DELAY, self.__startKillCamSimulation)
        return

    def __startKillCamSimulation(self):
        if self.__isLeaveKillCamWhenPrepared:
            self._leaveMode()
            return
        self.killCamCtrl.simulationSceneActive(True)
        self.__simulatedScene.updateVehicleEntities()
        self.__fadeScreen(False, _SHOW_KILLER_VISION_FADE_TIME)
        projectileData = self._rawSimulationData[b'projectile']
        self._cam.projectileTriNorm = self._rawSimulationData[b'projectile'][b'triNormal']
        self._cam.hasProjectilePierced = self._rawSimulationData[b'projectile'][b'hasProjectilePierced']
        self._cam.hasNonPiercedDamage = self._rawSimulationData[b'projectile'][b'hasNonPiercedDamage']
        self._cam.isSPG = self._rawSimulationData[b'attacker'][b'vehicleType'] == b'SPG'
        impactType = self._rawSimulationData[b'projectile'][b'impactType']
        if impactType == constants.IMPACT_TYPES.LEGACY_HE:
            self.delayCallback(_SHOW_KILLER_VISION_FADE_TIME, self.__enableEdgeDrawing)
        if self._killerIsSpotted:
            self.__simulatedScene.startAnimations(projectileData[b'shotID'])
        self.__notifyKillCamCtrl()
        uniprof.enterToRegion(b'avatar.control_mode.kill_cam.vision')
        if self._killerIsSpotted:
            self._cam.startKillerVision(self.__simulatedKillerID, self.__simulatedVictimID, self.__isRicochet, projectileData, self.__fadeAndLeaveKillCam)
        else:
            self._cam.startPlayerVision(projectileData, self.__fadeAndLeaveKillCam)
            self.__displayKillCamAnimationEffects()
        self._changeKillCamModeState(DeathCamEvent.State.ACTIVE)
        return

    def __notifyKillCamCtrl(self):
        phase1Duration, phase2Duration, phase3Duration, totalSceneDuration = self._cam.calculatePhaseDurations(self._killerIsSpotted)
        phaseDurations = (
         phase1Duration, phase2Duration, phase3Duration)
        projectileData = self._rawSimulationData[b'projectile']
        playerRelativeArmor = self._rawSimulationData[b'player'][b'relativeArmor']
        hasSpottedData = self._rawSimulationData[b'attacker'][b'hasSpottedData']
        playerIsSpotted = self._rawSimulationData[b'player'][b'victimIsNotSpotted']
        causeOfDeath = self._rawSimulationData[b'player'][b'causeOfDeath']
        simulatedKiller = BigWorld.entity(self.__simulatedKillerID) if self.__simulatedKillerID else None
        if simulatedKiller:
            gunInstallationIndex = projectileData.get(b'gunInstallationIndex', DEFAULT_GUN_INSTALLATION_INDEX)
            gunIndex = projectileData.get(b'gunIndex', 0)
            simulatedKillerGunInfo = (
             simulatedKiller.gunOriginMatrix(gunInstallationIndex, gunIndex),
             simulatedKiller.gunFireMatrix(gunInstallationIndex, gunIndex))
        else:
            simulatedKillerGunInfo = None
        mechanicsInfo = {b'player': (self._rawSimulationData.get(b'player', {}).get(b'mechanicsInfo')), 
           b'attacker': (self._rawSimulationData.get(b'attacker', {}).get(b'mechanicsInfo'))}
        self.killCamCtrl.killCamModeActive(self.__unspottedOrigin, simulatedKillerGunInfo, projectileData, phaseDurations, hasSpottedData, simulatedKiller is not None, playerRelativeArmor, playerIsSpotted, totalSceneDuration - _START_VISION_DELAY, causeOfDeath, mechanicsInfo)
        return

    def __fadeScreen(self, bFade=True, duration=1.0):
        if self.__bFadeScreenActive == bFade:
            return
        self.__bFadeScreenActive = bFade
        if BigWorld.WGRenderSettings().getPosteffectsSettings() == 4:
            self.__startBlackScreen(bFade, duration)
        else:
            self.__startScreenFade(bFade, duration)
        return

    def __startScreenFade(self, isFadeToBlack, duration):
        if isFadeToBlack:
            BigWorld.WGRenderSettings().setFadeParams(Math.Vector4(0, 0, 0, 1.0), duration)
        else:
            BigWorld.WGRenderSettings().setFadeParams(Math.Vector4(0, 0, 0, 0.0), duration)
        return

    def __startBlackScreen(self, isFadeToBlack, duration):
        if self.killCamState == DeathCamEvent.State.PREPARING:
            self.delayCallback(duration, self.__setBlackScreen, isFadeToBlack)
            return
        self.__setBlackScreen(isFadeToBlack)
        return

    def __setBlackScreen(self, isFadeToBlack):
        if isFadeToBlack:
            BigWorld.wg_enableGUIBackground(True, False)
            BigWorld.wg_setGUIBackground(_BLACK_BG_IMG)
        else:
            BigWorld.wg_enableGUIBackground(False, False)
        return

    def __enableEdgeDrawing(self):
        BigWorld.wg_setHideEdges(False)
        return

    def __fadeAndLeaveKillCam(self, isInterrupted=False):
        uniprof.exitFromRegion(b'avatar.control_mode.kill_cam.vision')
        if self.killCamState == DeathCamEvent.State.ENDING or self.killCamState == DeathCamEvent.State.FINISHED:
            return
        if isInterrupted and self.killCamCtrl:
            self.killCamCtrl.killCamInterrupted()
        self.__simulatedScene.hideEdgeEffects()
        self.__fadeScreen(True, _LEAVE_KILLER_VISION_FADE_TIME)
        self.delayCallback(_LEAVE_KILLER_VISION_FADE_TIME, self._leaveMode)
        self._changeKillCamModeState(DeathCamEvent.State.ENDING)
        return

    def __simulatedSceneEnded(self):
        if self._postmortemKwargs is None:
            return
        else:
            self.__enableEdgeDrawing()
            self._rawSimulationData = None
            if self.killCamState not in DeathCamEvent.BEFORE_SIMULATION:
                self.__fadeScreen(False, _SHOW_DEAD_TANK_FADE_TIME)
            self._changeKillCamModeState(DeathCamEvent.State.FINISHED)
            if self.__vehicleRespawnTriggered:
                ownVehicle = BigWorld.entities.get(BigWorld.player().playerVehicleID, None)
                vehRespComponent = ownVehicle and ownVehicle.dynamicComponents.get(b'VehicleRespawnComponent')
                if vehRespComponent:
                    vehRespComponent.waitForRespawnReadiness()
                else:
                    _logger.error(b'[KillCamMode] VehicleRespawnComponent not found!')
                return
            targetMode = BigWorld.player().getNextControlMode()
            if self._postmortemKwargs.get(b'keepCameraSettings', False):
                self._postmortemKwargs[b'pivotSettings'] = self.camera.getPivotSettings()
                self._postmortemKwargs[b'distanceFromFocus'] = self.camera.aimingSystem.distanceFromFocus
            self._aih.onControlModeChanged(targetMode, **self._postmortemKwargs)
            self._cam.resetCamera()
            return

    def __displayKillCamAnimationEffects(self):
        isSpotted = self._killerIsSpotted
        self.__simulatedScene.displayEffects(self.__simulatedVictimID)
        self.killCamCtrl.killCamModeEffectsPlaced(isSpotted)
        if _PARTICLES_DURATION_AFTER_SHOT <= 0.0:
            return
        BigWorld.wg_setWorldTimeScale(1.0 / ANIMATION_DURATION_BEFORE_SHOT)
        self.delayCallback(_PARTICLES_DURATION_AFTER_SHOT, self.__stopParticlesAfterShot)
        return

    def __stopParticlesAfterShot(self):
        self.__simulatedScene.updateParticlesTimeScale()
        return

    def __pauseResumeChanged(self, pause):
        self.__simulatedScene.pauseOrResumeAnimations(pause)
        self._cam.userInterruption(pause)
        return

    def __onVehicleAnimationFinished(self):
        self.__simulatedScene.onAnimationsCompleted -= self.__onVehicleAnimationFinished
        self.__simulatedScene.updateParticlesTimeScale()
        self.__displayKillCamAnimationEffects()
        return

    def __onArenaPeriodChanged(self, period, *args):
        if period != ARENA_PERIOD.AFTERBATTLE or BattleReplay.g_replayCtrl.isPlaying:
            return
        if self.killCamState in DeathCamEvent.SIMULATION_EXCL_FADES:
            self.__fadeAndLeaveKillCam()
        elif self.killCamState == DeathCamEvent.State.PREPARING:
            self.__isLeaveKillCamWhenPrepared = True
        else:
            self._leaveMode()
        return

    def __onRespawnInfoUpdate(self, respawnInfo):
        if respawnInfo is not None and not self.__isAutoRespawnScheduled:
            self.__isAutoRespawnScheduled = True
            killCamSceneUntilNow = int(BigWorld.time() - self._modeEnteredTime)
            autoRespawnTimeLeft = int(respawnInfo.autoRespawnTime - BigWorld.serverTime())
            forcedExitTime = autoRespawnTimeLeft - _SKIP_KILL_CAM_BEFORE_AUTORESPAWN_TIME - killCamSceneUntilNow
            self.delayCallback(forcedExitTime, self.__forceExitKillCamScene)
        return

    def __onVehicleRespawn(self):
        self.__vehicleRespawnTriggered = True
        self.__forceExitKillCamScene()
        return

    def __forceExitKillCamScene(self):
        self.__fadeAndLeaveKillCam()
        return

    def __isDistanceFarEnough(self, simulationData):
        if not simulationData[b'attacker'][b'spotted']:
            return True
        attackerPosition = simulationData[b'attacker'][b'position']
        victimPosition = simulationData[b'player'][b'position']
        return (victimPosition - attackerPosition).length > self.__skipKillCamDistance


class LookAtKillerMode(KillModeBase):

    def _handleModeExecution(self):
        _logger.info(b'[LookAtKillerMode] _handleModeExecution()')
        self.delayCallback(_KILL_CAM_WAIT_TIME, self.__handleLookAtKillerFlow)
        return

    def _leaveMode(self):
        _logger.info(b'[LookAtKillerMode] _leaveMode()')
        targetMode = BigWorld.player().getNextControlMode()
        self._postmortemKwargs[b'previousCam'] = self._cam
        self._aih.onControlModeChanged(targetMode, **self._postmortemKwargs)
        self._cam.resetCamera()
        return

    def __handleLookAtKillerFlow(self):
        availability, self._rawSimulationData = self._checkSimulationAvailability()
        if availability == SimulationAvailability.AVAILABLE:
            self._trajectoryPoints = self._rawSimulationData.get(b'trajectoryData')
        self.__startCameraRotation(availability)
        return

    def __startCameraRotation(self, simAvailability):
        isBattleEnding = simAvailability == SimulationAvailability.NOT_AVAILABLE_END_OF_BATTLE
        haveEnoughTime = not isBattleEnding and self._areBothTeamsAlive()
        if haveEnoughTime:
            waitTime = LOOK_AT_KILLER_DURATION - _PREPARE_KILLER_VISION_FADE_TIME
        else:
            waitTime = _TIME_BEFORE_FOLLOW_TANK
        isFirstTenDeathWheeledTank = self._isFirstTenDeathsWheeledTank(self._victimVehicleID)
        if isFirstTenDeathWheeledTank and simAvailability != SimulationAvailability.AVAILABLE:
            self._tryDecrementWheeledDeathCounter(self._victimVehicleID)
            waitTime = _WHEELED_VEHICLE_POSTMORTEM_DELAY
        suicide = self._killerVehicleID == self._victimVehicleID
        if not suicide:
            if (simAvailability == SimulationAvailability.NOT_KILLED_BY_SHOT or simAvailability == SimulationAvailability.NOT_AVAILABLE_MISSING_DATA) and not isFirstTenDeathWheeledTank:
                waitTime = _LOOK_AT_KILLER_DURATION_LEGACY
            self.__handleCameraRotation(enemySpottedInsideAOI=BigWorld.entity(self._killerVehicleID) is not None, killerIsSpotted=self._killerIsSpotted)
        if suicide or not haveEnoughTime:
            self._postmortemKwargs[b'bPostmortemDelay'] = False
        self.delayCallback(waitTime, self._leaveMode)
        return

    def __handleCameraRotation(self, enemySpottedInsideAOI=False, killerIsSpotted=False):
        _logger.info(b'[LookAtKillerMode] __handleCameraRotation()')
        if enemySpottedInsideAOI:
            self._cam.setCameraToLookTowards(sourceVehicleID=self._victimVehicleID, targetVehicleID=self._killerVehicleID, mode=StartCamDirection.TOWARDS_TARGET, isInstant=False)
        elif killerIsSpotted:
            self._cam.setCameraToLookTowards(sourceVehicleID=self._victimVehicleID, targetVehicleID=None, firstPoint=self._trajectoryPoints[0], lastPoint=self._trajectoryPoints[-1], isInstant=False)
        else:
            self._cam.setCameraToLookTowards(sourceVehicleID=self._victimVehicleID, targetVehicleID=None, firstPoint=self._trajectoryPoints[0], lastPoint=self._trajectoryPoints[-1], isInstant=False, originatesFromVehicle=False)
        return
