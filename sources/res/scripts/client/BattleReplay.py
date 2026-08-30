import base64, os, datetime, json, copy, typing, cPickle as pickle, logging, zlib
from collections import defaultdict
import Math, BigWorld, ArenaType, Settings, CommandMapping, constants, Keys, Event, AreaDestructibles, BWReplay, TriggersManager
from aih_constants import CTRL_MODE_NAME
from debug_utils import LOG_ERROR, LOG_DEBUG, LOG_WARNING, LOG_CURRENT_EXCEPTION
from gui import GUI_CTRL_MODE_FLAG
from helpers import EffectsList, isPlayerAvatar, isPlayerAccount, getFullClientVersion
from PlayerEvents import g_playerEvents
from ReplayEvents import g_replayEvents
from constants import ARENA_PERIOD, ARENA_BONUS_TYPE, ARENA_GUI_TYPE, INBATTLE_CONFIGS, NULL_ENTITY_ID
from helpers import dependency
from gui.app_loader import settings
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.connection_mgr import IConnectionManager
from skeletons.gameplay import IGameplayLogic, ReplayEventID
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext
from soft_exception import SoftException
from helpers.styles_perf_toolset import g_reportGenerator
_logger = logging.getLogger(__name__)
g_replayCtrl = None
REPLAY_FILE_EXTENSION = b'.mtreplay'
AUTO_RECORD_TEMP_FILENAME = b'temp'
FIXED_REPLAY_FILENAME = b'replay_last_battle'
REPLAY_TIME_MARK_CLIENT_READY = 2147483648L
REPLAY_TIME_MARK_REPLAY_FINISHED = 2147483649L
REPLAY_TIME_MARK_CURRENT_TIME = 2147483650L
FAST_FORWARD_STEP = 20.0
MIN_REPLAY_TIME = 1
_POSTMORTEM_CTRL_MODES = (
 CTRL_MODE_NAME.POSTMORTEM, CTRL_MODE_NAME.DEATH_FREE_CAM, CTRL_MODE_NAME.RESPAWN_DEATH)
_FORWARD_INPUT_CTRL_MODES = (
 CTRL_MODE_NAME.POSTMORTEM, CTRL_MODE_NAME.VIDEO, CTRL_MODE_NAME.CAT,
 CTRL_MODE_NAME.DEATH_FREE_CAM)
_ARENA_GUI_TYPE_TO_MODE_TAG = {(ARENA_GUI_TYPE.COMP7): b'Onslaught', 
   (ARENA_GUI_TYPE.FUN_RANDOM): b'Arcade'}
_IGNORED_SWITCHING_CTRL_MODES = (
 CTRL_MODE_NAME.SNIPER,
 CTRL_MODE_NAME.ARCADE,
 CTRL_MODE_NAME.ARTY,
 CTRL_MODE_NAME.SPG_ONLY_ARTY_MODE,
 CTRL_MODE_NAME.STRATEGIC,
 CTRL_MODE_NAME.DUAL_GUN,
 CTRL_MODE_NAME.MAP_CASE,
 CTRL_MODE_NAME.MAP_CASE_ARCADE,
 CTRL_MODE_NAME.MAP_CASE_EPIC,
 CTRL_MODE_NAME.MAP_CASE_ARCADE_EPIC_MINEFIELD)

class CallbackDataNames(object):
    APPLY_ZOOM = b'applyZoom'
    BC_MARKERS_ONTRIGGERACTIVATED = b'bootcampMarkers_onTriggerActivated'
    BC_MARKERS_ONTRIGGERDEACTIVATED = b'bootcampMarkers_onTriggerDeactivated'
    BC_MARKERS_SHOWMARKER = b'bootcampMarkers_showMarker'
    BC_MARKERS_HIDEMARKER = b'bootcampMarkers_hideMarker'
    HINT_SHOW = b'hint_show'
    HINT_HIDE = b'hint_hide'
    HINT_COMPLETE = b'hint_complete'
    HINT_CLOSE = b'hint_close'
    HINT_ONHIDED = b'hint_onHided'
    BW_CHAT2_REPLAY_ACTION_RECEIVED_CALLBACK = b'bw_chat2.onActionReceived'
    CLIENT_VEHICLE_STATE_GROUP = b'client_vehicle_state_{}'
    DYN_SQUAD_SEND_ACTION_NAME = b'DynSquad.SendInvitationToSquad'
    DYN_SQUAD_ACCEPT_ACTION_NAME = b'DynSquad.AcceptInvitationToSquad'
    DYN_SQUAD_REJECT_ACTION_NAME = b'DynSquad.RejectInvitationToSquad'
    GUN_DAMAGE_SOUND = b'gunDamagedSound'
    ON_TARGET_VEHICLE_CHANGED = b'onTargetVehicleChanged'
    MT_CONFIG_CALLBACK = b'mapsTrainingConfigurationCallback'
    BATTLE_CONTEXT_HINTS_COUNTERS_CALLBACK = b'battleContextHintsCountersCallback'


class SimulatedAoI(object):

    def __init__(self):
        self.__aoiMapping = defaultdict(dict)
        self.__withheld = dict()
        self.__pending = dict()
        self.currentVehicleID = None
        self.currentAvatarID = None
        self.__controlMode = CTRL_MODE_NAME.POSTMORTEM
        return

    def changeVehicle(self, vehicleID):
        if self.currentVehicleID == vehicleID:
            return
        else:
            self.flush(self.__controlMode)
            self.currentVehicleID = vehicleID
            priorAvatarID = self.currentAvatarID
            self.currentAvatarID = None
            if vehicleID:
                vehicleEntity = BigWorld.entities.get(vehicleID)
                if vehicleEntity:
                    self.currentAvatarID = vehicleEntity.avatarID
            if priorAvatarID and priorAvatarID in self.__aoiMapping:
                for entityID, shown in self.__aoiMapping[priorAvatarID].items():
                    if not shown:
                        BWReplay.withholdEntity(entityID, False)
                        self.__withheld[entityID] = False

            currentAoI = None
            if self.currentAvatarID and self.currentAvatarID in self.__aoiMapping:
                currentAoI = self.__aoiMapping[self.currentAvatarID]
            for entityID, isWithheld in self.__withheld.items():
                shouldSee = currentAoI.get(entityID, False) if currentAoI else True
                shouldWithhold = not shouldSee
                if isWithheld != shouldWithhold:
                    BWReplay.withholdEntity(entityID, shouldWithhold)
                    self.__withheld[entityID] = shouldWithhold

            return

    def handleAoIEvent(self, witnessID, entityID, hasEnteredAoI):
        self.__aoiMapping[witnessID][entityID] = hasEnteredAoI
        isWithheld = self.__withheld.setdefault(entityID, False)
        isCurrentAvatar = self.currentAvatarID == witnessID
        if isCurrentAvatar:
            isWithheld = self.__pending.get(entityID, isWithheld)
            shouldWithhold = not hasEnteredAoI
            if isWithheld != shouldWithhold:
                self.__pending[entityID] = shouldWithhold
        return

    def flush(self, controlMode=CTRL_MODE_NAME.POSTMORTEM):
        if controlMode == CTRL_MODE_NAME.VIDEO:
            if self.__controlMode == CTRL_MODE_NAME.VIDEO:
                return
            self.__controlMode = CTRL_MODE_NAME.VIDEO
            for entityID in self.__withheld:
                BWReplay.withholdEntity(entityID, False)

        else:
            for entityID, shouldWithhold in self.__pending.items():
                BWReplay.withholdEntity(entityID, shouldWithhold)
                self.__withheld[entityID] = shouldWithhold

            if self.__controlMode == CTRL_MODE_NAME.VIDEO:
                for entityID, shouldWithhold in self.__withheld.items():
                    if entityID not in self.__pending:
                        BWReplay.withholdEntity(entityID, shouldWithhold)

            self.__pending.clear()
            if self.__controlMode != controlMode:
                self.__controlMode = controlMode
        return

    def reset(self):
        self.__aoiMapping.clear()
        self.__withheld.clear()
        self.__pending.clear()
        self.currentVehicleID = None
        self.currentAvatarID = None
        return


class BattleReplay(object):
    isPlaying = property((lambda self: self.__replayCtrl.isPlaying()))
    isServerSideReplay = property((lambda self: self.__replayCtrl.isServerSideReplay))
    isRecording = property((lambda self: self.__replayCtrl.isRecording))
    isClientReady = property((lambda self: self.__replayCtrl.isClientReady))
    isControllingCamera = property((lambda self: self.__replayCtrl.isControllingCamera))
    isOffline = property((lambda self: self.__replayCtrl.isOfflinePlaybackMode))
    isTimeWarpInProgress = property((lambda self: self.__replayCtrl.isTimeWarpInProgress))
    isServerAim = property((lambda self: self.__replayCtrl.isServerAim))
    playerVehicleID = property((lambda self: self.__replayCtrl.playerVehicleID))
    isLoading = property((lambda self: self.__replayCtrl.getAutoStartFileName() is not None and self.__replayCtrl.getAutoStartFileName() != b''))
    isPaused = property((lambda self: self.__replayCtrl.playbackSpeed == 0))
    fps = property((lambda self: self.__replayCtrl.fps))
    ping = property((lambda self: self.__replayCtrl.ping))
    compressed = property((lambda self: self.__replayCtrl.isFileCompressed()))
    isLaggingNow = property((lambda self: self.__replayCtrl.isLaggingNow))
    playbackSpeed = property((lambda self: self.__replayCtrl.playbackSpeed))
    scriptModalWindowsEnabled = property((lambda self: self.__replayCtrl.scriptModalWindowsEnabled))
    currentTime = property((lambda self: self.__replayCtrl.getTimeMark(REPLAY_TIME_MARK_CURRENT_TIME)))
    warpTime = property((lambda self: self.__warpTime))
    rewind = property((lambda self: self.__rewind))
    isAutoRecordingEnabled = property((lambda self: self.__isAutoRecordingEnabled))
    arenaInfo = property((lambda self: self.__getArenaInfo()))

    def resetUpdateGunOnTimeWarp(self):
        self.__updateGunOnTimeWarp = False
        return

    isUpdateGunOnTimeWarp = property((lambda self: self.__updateGunOnTimeWarp))
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    gameplay = dependency.descriptor(IGameplayLogic)
    settingsCore = dependency.descriptor(ISettingsCore)
    lobbyContext = dependency.descriptor(ILobbyContext)
    connectionMgr = dependency.descriptor(IConnectionManager)
    appLoader = dependency.descriptor(IAppLoader)

    def __init__(self):
        userPrefs = Settings.g_instance.userPrefs
        if not userPrefs.has_key(Settings.KEY_REPLAY_PREFERENCES):
            userPrefs.write(Settings.KEY_REPLAY_PREFERENCES, b'')
        self.__settings = userPrefs[Settings.KEY_REPLAY_PREFERENCES]
        self.__fileName = None
        self.__replayCtrl = BigWorld.ReplayManager()
        self.__replayCtrl.replayFinishedCallback = self.onReplayFinished
        self.__replayCtrl.replayTerminatedCallback = self.onReplayTerminated
        self.__replayCtrl.replayMetaDataCallback = self.onReplayMetaData
        self.__replayCtrl.controlModeChangedCallback = self.onControlModeChanged
        self.__replayCtrl.ammoButtonPressedCallback = self.__onAmmoButtonPressed
        self.__replayCtrl.playerVehicleIDChangedCallback = self.onPlayerVehicleIDChanged
        self.__replayCtrl.clientVersionDiffersCallback = self.onClientVersionDiffers
        self.__replayCtrl.battleChatMessageCallback = self.onBattleChatMessage
        self.__replayCtrl.lockTargetCallback = self.onLockTarget
        self.__replayCtrl.equipmentIdCallback = self.onSetEquipmentId
        self.__replayCtrl.warpFinishedCallback = self.__onTimeWarpFinished
        self.__replayCtrl.sniperModeCallback = self.onSniperModeChanged
        self.__replayCtrl.entityAoIChangedCallback = self.onEntityAoIChangedCallback
        self.__replayCtrl.postTickCallback = self.onPostTickCallback
        self.__replayCtrl.serverAimCallback = self.setUseServerAim
        self.__isAutoRecordingEnabled = False
        self.__quitAfterStop = False
        self.__isPlayingPlayList = False
        self.__playList = []
        self.__isFinished = False
        self.__isMenuShowed = False
        self.__updateGunOnTimeWarp = False
        self.__lastObservedVehicleID = NULL_ENTITY_ID
        self.__aoi = SimulatedAoI()
        self.__isVehicleChanging = False
        self.__playerDatabaseID = 0
        self.__serverSettings = dict()
        if isPlayerAccount():
            self.__playerDatabaseID = BigWorld.player().databaseID
        self.__playbackSpeedModifiers = (0.0, 0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)
        self.__playbackSpeedModifiersStr = (b'0', b'1/16', b'1/8', b'1/4', b'1/2', b'1', b'2', b'4', b'8', b'16')
        self.__playbackSpeedIdx = self.__playbackSpeedModifiers.index(1.0)
        self.__savedPlaybackSpeedIdx = self.__playbackSpeedIdx
        self.__gunWasLockedBeforePause = False
        self.__wasVideoBeforeRewind = False
        self.__videoCameraMatrix = Math.Matrix()
        self.__replayDir = b'./replays'
        self.__replayCtrl.clientVersion = BigWorld.getProductVersion()
        self.__enableTimeWarp = False
        self.__isChatPlaybackEnabled = True
        self.__warpTime = -1.0
        self.__equipmentId = None
        self.__rewind = False
        self.replayTimeout = 0
        self.__arenaPeriod = -1
        self.__arenaPeriodLength = -1
        self.__handleInput = True
        self.__previousPeriod = -1
        self.__replayStartTime = 0
        self.__replayEndTime = 0
        self.__actualReplayStartTime = 0
        self.__actualReplayEndTime = 0
        self.enableAutoRecordingBattles(True)
        self.onCommandReceived = Event.Event()
        self.onAmmoSettingChanged = Event.Event()
        self.onServerAimChanged = Event.Event()
        self.onStopped = Event.Event()
        self.onPlay = Event.Event()
        if hasattr(self.__replayCtrl, b'setupStreamExcludeFilter'):
            import streamIDs
            self.__replayCtrl.setupStreamExcludeFilter(streamIDs.STREAM_ID_CHAT_MIN, streamIDs.STREAM_ID_CHAT_MAX)
        if hasattr(self.__replayCtrl, b'setupAvatarMethodExcludeFilter'):
            self.__replayCtrl.setupAvatarMethodExcludeFilter(b'messenger_onActionByServer_chat2')
        if constants.IS_DEVELOPMENT:
            try:
                import development.replay_override
            except Exception:
                pass

        return

    def enableHandleInput(self):
        self.__handleInput = True
        return

    def disableHandleInput(self):
        self.__handleInput = False
        return

    def subscribe(self):
        g_playerEvents.onBattleResultsReceived += self.__onBattleResultsReceived
        g_playerEvents.onAccountBecomePlayer += self.__onAccountBecomePlayer
        g_playerEvents.onArenaPeriodChange += self.__onArenaPeriodChange
        g_playerEvents.onBootcampAccountMigrationComplete += self.__onBootcampAccountMigrationComplete
        g_playerEvents.onAvatarObserverVehicleChanged += self.__onAvatarObserverVehicleChanged
        self.settingsCore.onSettingsChanged += self.__onSettingsChanging
        return

    def unsubscribe(self):
        g_playerEvents.onBattleResultsReceived -= self.__onBattleResultsReceived
        g_playerEvents.onAccountBecomePlayer -= self.__onAccountBecomePlayer
        g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChange
        g_playerEvents.onBootcampAccountMigrationComplete -= self.__onBootcampAccountMigrationComplete
        g_playerEvents.onAvatarObserverVehicleChanged -= self.__onAvatarObserverVehicleChanged
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanging
        return

    def destroy(self):
        self.stop(isDestroyed=True)
        self.onCommandReceived.clear()
        self.onCommandReceived = None
        self.onAmmoSettingChanged.clear()
        self.onAmmoSettingChanged = None
        self.onServerAimChanged.clear()
        self.onServerAimChanged = None
        self.enableAutoRecordingBattles(False)
        self.__replayCtrl.replayTerminatedCallback = None
        self.__replayCtrl.replayFinishedCallback = None
        self.__replayCtrl.replayMetaDataCallback = None
        self.__replayCtrl.controlModeChangedCallback = None
        self.__replayCtrl.clientVersionDiffersCallback = None
        self.__replayCtrl.playerVehicleIDChangedCallback = None
        self.__replayCtrl.battleChatMessageCallback = None
        self.__replayCtrl.ammoButtonPressedCallback = None
        self.__replayCtrl.lockTargetCallback = None
        self.__replayCtrl.equipmentIdCallback = None
        self.__replayCtrl.warpFinishedCallback = None
        self.__replayCtrl.serverAimCallback = None
        self.__replayCtrl = None
        self.__settings = None
        self.__videoCameraMatrix = None
        self.__warpTime = -1.0
        self.__arenaPeriod = -1
        self.__arenaPeriodLength = -1
        return

    def record(self, fileName=None):
        if self.isPlaying:
            return False
        else:
            if self.isRecording:
                if not self.stop():
                    LOG_ERROR(b'Failed to start recording new replay - cannot stop previous record')
                    return False
            useAutoFilename = False
            if fileName is None:
                useAutoFilename = True
            try:
                if not os.path.isdir(self.__replayDir):
                    os.makedirs(self.__replayDir)
            except Exception:
                LOG_ERROR(b'Failed to create directory for replay files')
                return False

            success = False
            for i in xrange(100):
                try:
                    if useAutoFilename:
                        fileName = os.path.join(self.__replayDir, AUTO_RECORD_TEMP_FILENAME + (b'' if i == 0 else str(i)) + REPLAY_FILE_EXTENSION)
                    f = open(fileName, b'wb')
                    f.close()
                    os.remove(fileName)
                    success = True
                    break
                except Exception:
                    if useAutoFilename:
                        continue
                    else:
                        break

            if not success:
                LOG_ERROR(b'Failed to create replay file, replays folder may be write-protected')
                return False
            g_replayEvents.onRecording()
            if self.__replayCtrl.startRecording(fileName):
                self.__fileName = fileName
                return True
            return False

    def play(self, fileName=None):
        if self.isRecording:
            self.stop()
        g_reportGenerator.startCollectingData()
        from SafeUnpickler import SafeUnpickler
        pickle._originalPickleLoads = pickle.loads
        pickle.loads = SafeUnpickler.loads
        if fileName is not None and fileName.rfind(b'.mtreplaylist') != -1:
            self.__playList = []
            self.__isPlayingPlayList = True
            try:
                f = open(fileName)
                s = f.read()
                f.close()
                self.__playList = s.replace(b'\r\n', b'\n').replace(b'\r', b'\n').split(b'\n')
                fileName = None
            except Exception:
                pass

        if fileName is None:
            if not self.__playList:
                return False
            fileName = self.__playList[0]
            self.__playList.pop(0)
            self.__quitAfterStop = not self.__playList
        self.__fileName = fileName
        if self.__replayCtrl.startPlayback(fileName):
            self.__playbackSpeedIdx = self.__playbackSpeedModifiers.index(1.0)
            self.__savedPlaybackSpeedIdx = self.__playbackSpeedIdx
            self.__replayStartTime = self.__replayCtrl.getReplayStartTime()
            self.__replayEndTime = self.__replayCtrl.getReplayEndTime()
            self.recalculateReplayTimes()
            g_replayEvents.onPlaying()
            self.onPlay(fileName, True)
            return True
        else:
            self.__fileName = None
            self.onPlay(fileName, False)
            return False

    def stop(self, rewindToTime=None, delete=False, isDestroyed=False):
        if not self.isPlaying and not self.isRecording:
            return False
        else:
            self.onStopped()
            g_reportGenerator.stopCollectingData()
            g_reportGenerator.generateReport()
            wasPlaying = self.isPlaying
            wasServerReplay = self.isServerSideReplay
            isOffline = self.__replayCtrl.isOfflinePlaybackMode
            self.__aoi.reset()
            self.__lastObservedVehicleID = NULL_ENTITY_ID
            self.__replayCtrl.stop(delete)
            self.__fileName = None
            self.__isVehicleChanging = False
            if wasPlaying:
                if isPlayerAvatar():
                    BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnterWorld
                    BigWorld.player().onObserverVehicleChanged -= self.__onObserverVehicleChanged
                if not isOffline and not isDestroyed:
                    self.connectionMgr.onDisconnected += self.__goToNextReplay
                if wasServerReplay:
                    BigWorld.clearAllSpaces()
                else:
                    BigWorld.clearEntitiesAndSpaces()
                    BigWorld.disconnect()
                g_replayEvents.onReplayTerminated.clear()
                if self.__quitAfterStop:
                    BigWorld.quit()
                elif isOffline and not isDestroyed:
                    self.__goToNextReplay()
            return True

    def onReplayTerminated(self, reason):
        _logger.info(b'BattleReplay.onReplayTerminated: reason=%r', reason)
        g_replayEvents.onMuteSound(False)
        g_replayEvents.onReplayTerminated(reason)
        self.__isFinished = False
        originalPickleLoads = getattr(pickle, b'_originalPickleLoads', None)
        if originalPickleLoads is not None:
            pickle.loads = originalPickleLoads
            pickle._originalPickleLoads = None
        return

    def onReplayMetaData(self, metaData):
        if b'serverSettings' in metaData:
            self.__serverSettings = pickle.loads(zlib.decompress(base64.b64decode(metaData[b'serverSettings'])))
        return

    def onEntityAoIChangedCallback(self, witnessID, entityID, hasEnteredAoI):
        _logger.debug(b'BattleReplay: onEntityAoIChangedCallback: witnessID=%s, entityID=%s, hasEnteredAoI=%s', witnessID, entityID, hasEnteredAoI)
        self.__aoi.handleAoIEvent(witnessID, entityID, hasEnteredAoI)
        return

    def getAutoStartFileName(self):
        return self.__replayCtrl.getAutoStartFileName()

    def autoStartBattleReplay(self):
        fileName = self.getAutoStartFileName()
        if fileName:
            self.__quitAfterStop = True
            if not self.play(fileName):
                BigWorld.quit()
            else:
                return True
        return False

    def getSpaceID(self):
        return BigWorld.player().spaceID

    def handleKeyEvent(self, isDown, key, mods, isRepeat, event):
        if not self.isPlaying:
            return False
        if self.isTimeWarpInProgress:
            return True
        if not self.__handleInput:
            return False
        if key == Keys.KEY_F1:
            if not isRepeat and not isDown:
                self.__showInfoMessages()
            return True
        if not self.isClientReady:
            return False
        cmdMap = CommandMapping.g_instance
        player = BigWorld.player()
        if not isPlayerAvatar():
            return False
        isCursorVisible = player.isForcedGuiControlMode()
        if key == Keys.KEY_ESCAPE:
            if isDown and not isCursorVisible:
                self.__isMenuShowed = True
                return False
        if not isCursorVisible:
            self.__isMenuShowed = False
        if self.__isMenuShowed or isCursorVisible:
            return False
        currReplayTime = self.__replayCtrl.getTimeMark(REPLAY_TIME_MARK_CURRENT_TIME)
        finishReplayTime = self.__replayCtrl.getTimeMark(REPLAY_TIME_MARK_REPLAY_FINISHED)
        if currReplayTime > finishReplayTime:
            currReplayTime = finishReplayTime
        fastForwardStep = FAST_FORWARD_STEP * (2.0 if mods == 2 else 1.0)
        if key == Keys.KEY_F11 and isDown:
            if self.isPlaying:
                self.__replayCtrl.onPutScreenshotMark()
                return True
        if (key == Keys.KEY_LEFTMOUSE or cmdMap.isFired(CommandMapping.CMD_CM_SHOOT, key)) and isDown:
            if not isCursorVisible:
                if self.isServerSideReplay:
                    if self.__arenaPeriod == ARENA_PERIOD.BATTLE:
                        player.switchObserverFPV()
                    return True
                if self.isControllingCamera:
                    self.appLoader.detachCursor(settings.APP_NAME_SPACE.SF_BATTLE)
                    controlMode = self.getControlMode()
                    if controlMode in _POSTMORTEM_CTRL_MODES:
                        self.onControlModeChanged(controlMode)
                    else:
                        self.onControlModeChanged(b'arcade')
                    self.__replayCtrl.isControllingCamera = False
                    self.__showInfoMessage(b'replayFreeCameraActivated')
                elif not self.__isAllowedSavedCamera():
                    return False
                self.__replayCtrl.isControllingCamera = True
                self.onControlModeChanged()
                self.__showInfoMessage(b'replaySavedCameraActivated')
                return True
        if cmdMap.isFired(CommandMapping.CMD_CM_ALTERNATE_MODE, key) and isDown:
            if self.isControllingCamera:
                return True
        if key == Keys.KEY_SPACE and isDown and not self.__isFinished:
            self.togglePause()
            return True
        if key == Keys.KEY_DOWNARROW and isDown and not self.__isFinished:
            self.changeSpeed(-1)
            return True
        if key == Keys.KEY_UPARROW and isDown and not self.__isFinished:
            self.changeSpeed(1)
            return True
        if key == Keys.KEY_RIGHTARROW and isDown and not self.__isFinished:
            self.__timeWarp(currReplayTime + fastForwardStep)
            return True
        if key == Keys.KEY_LEFTARROW:
            self.__aoi.reset()
            self.__timeWarp(currReplayTime - fastForwardStep)
            return True
        if key == Keys.KEY_HOME and isDown:
            self.__aoi.reset()
            self.__timeWarp(0.0)
            return True
        if key == Keys.KEY_END and isDown and not self.__isFinished:
            self.__timeWarp(finishReplayTime)
            return True
        if key == Keys.KEY_C and isDown:
            self.__isChatPlaybackEnabled = not self.__isChatPlaybackEnabled
        suppressCommand = cmdMap.isFiredList(xrange(CommandMapping.CMD_AMMO_CHOICE_1, CommandMapping.CMD_AMMO_CHOICE_0 + 1), key) and isDown
        if not suppressCommand and cmdMap.isFiredList((
         CommandMapping.CMD_CM_LOCK_TARGET,
         CommandMapping.CMD_CM_LOCK_TARGET_OFF,
         CommandMapping.CMD_CM_POSTMORTEM_NEXT_VEHICLE,
         CommandMapping.CMD_CM_POSTMORTEM_SELF_VEHICLE,
         CommandMapping.CMD_RADIAL_MENU_SHOW,
         CommandMapping.CMD_RELOAD_PARTIAL_CLIP), key) and isDown and not isCursorVisible:
            suppressCommand = True
        elif cmdMap.isFiredList((
         CommandMapping.CMD_STOP_UNTIL_FIRE,
         CommandMapping.CMD_INCREMENT_CRUISE_MODE,
         CommandMapping.CMD_DECREMENT_CRUISE_MODE,
         CommandMapping.CMD_MOVE_FORWARD,
         CommandMapping.CMD_MOVE_FORWARD_SPEC,
         CommandMapping.CMD_MOVE_BACKWARD,
         CommandMapping.CMD_ROTATE_LEFT,
         CommandMapping.CMD_ROTATE_RIGHT,
         CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION), key):
            suppressCommand = True
        if suppressCommand:
            playerControlModeName = player.inputHandler.ctrlModeName
            isForwardInputToCtrlMode = playerControlModeName in _FORWARD_INPUT_CTRL_MODES
            if isForwardInputToCtrlMode:
                player.inputHandler.ctrl.handleKeyEvent(isDown, key, mods, event)
            return True
        return False

    def changeSpeed(self, step):
        newId = self.__playbackSpeedIdx + step
        maxId = len(self.__playbackSpeedModifiers) - 1
        clampedId = min(max(newId, 0), maxId)
        if clampedId != self.__playbackSpeedIdx:
            self.setPlaybackSpeedIdx(clampedId)
        return

    def togglePause(self):
        if self.__playbackSpeedIdx > 0:
            self.setPlaybackSpeedIdx(0)
        else:
            self.setPlaybackSpeedIdx(self.__savedPlaybackSpeedIdx if self.__savedPlaybackSpeedIdx != 0 else self.__playbackSpeedModifiers.index(1.0))
        return

    def handleMouseEvent(self, dx, dy, dz):
        if not (self.isPlaying and self.isClientReady):
            return False
        if self.isTimeWarpInProgress:
            return True
        if not isPlayerAvatar():
            return False
        if self.isControllingCamera:
            if dz != 0:
                return True
        return False

    def setGunRotatorTargetPoint(self, value):
        self.__replayCtrl.gunRotatorTargetPoint = value
        return

    def getGunRotatorTargetPoint(self):
        return self.__replayCtrl.gunRotatorTargetPoint

    def setConsumablesPosition(self, pos, direction=Math.Vector3(1, 1, 1)):
        self.__replayCtrl.gunMarkerPosition = pos
        self.__replayCtrl.gunMarkerDirection = direction
        return

    def setGunMarkerParams(self, diameter, dualAccDiameter, pos, direction):
        controlMode = self.getControlMode()
        if controlMode != b'mapcase':
            self.__replayCtrl.gunMarkerDiameter = diameter
            self.__replayCtrl.dualAccDiameter = dualAccDiameter
            self.__replayCtrl.gunMarkerDirection = direction
            self.__replayCtrl.gunMarkerPosition = pos
        return

    def getGunMarkerParams(self, defaultPos, defaultDir):
        diameter = self.__replayCtrl.gunMarkerDiameter
        dualAccDiameter = self.__replayCtrl.dualAccDiameter
        direction = self.__replayCtrl.gunMarkerDirection
        pos = self.__replayCtrl.gunMarkerPosition
        if direction == Math.Vector3(0, 0, 0):
            pos = defaultPos
            direction = defaultDir
        return (
         diameter, dualAccDiameter, pos, direction)

    def getGunMarkerPos(self):
        return self.__replayCtrl.gunMarkerPosition

    def getEquipmentId(self):
        return self.__equipmentId

    def useSyncroniusResourceLoading(self, use):
        self.__replayCtrl.useSyncroniusResourceLoading = use
        return

    def setArcadeGunMarkerSize(self, size):
        self.__replayCtrl.setArcadeGunMarkerSize(size)
        return

    def getArcadeGunMarkerSize(self):
        return self.__replayCtrl.getArcadeGunMarkerSize()

    def setDualAccMarkerSize(self, size):
        self.__replayCtrl.setDualAccMarkerSize(size)
        return

    def getDualAccMarkerSize(self):
        return self.__replayCtrl.getDualAccMarkerSize()

    def setSPGGunMarkerParams(self, dispersionAngle, size):
        self.__replayCtrl.setSPGGunMarkerParams((dispersionAngle, size))
        return

    def getSPGGunMarkerParams(self):
        return self.__replayCtrl.getSPGGunMarkerParams()

    def setAimClipPosition(self, position):
        self.__replayCtrl.setAimClipPosition(position)
        return

    def getAimClipPosition(self):
        return self.__replayCtrl.getAimClipPosition()

    def setTurretYaw(self, value):
        self.__replayCtrl.turretYaw = value
        return

    def getTurretYaw(self):
        return self.__replayCtrl.getTurretYawByTime(self.currentTime)

    def setGunPitch(self, value):
        self.__replayCtrl.gunPitch = value
        return

    def getGunPitch(self):
        return self.__replayCtrl.gunPitch

    def setGunReloadTime(self, startTime, duration):
        self.__replayCtrl.setGunReloadTime(startTime, duration)
        return

    def resetArenaPeriod(self):
        if not self.isRecording:
            LOG_ERROR(b'Replay is not recorded on resetArenaPeriod')
        self.__replayCtrl.resetArenaPeriod()
        return

    def setArenaPeriod(self, period, length):
        if not self.isRecording:
            LOG_ERROR(b'Replay is not recorded on setArenaPeriod')
        self.__replayCtrl.arenaPeriod = period
        self.__replayCtrl.arenaLength = length
        return

    def getArenaPeriod(self):
        if not self.isPlaying:
            raise SoftException(b'Replay is not playing')
        return self.__replayCtrl.arenaPeriod

    def getArenaLength(self):
        if not self.isPlaying:
            raise SoftException(b'Replay is not playing')
        return self.__replayCtrl.arenaLength

    def setPlayerVehicleID(self, vehicleID):
        if vehicleID == 0 and isPlayerAvatar():
            vehicleID = BigWorld.player().playerVehicleID
        self.__replayCtrl.playerVehicleID = vehicleID
        return

    def setPlaybackSpeedIdx(self, value):
        if self.isTimeWarpInProgress:
            return
        else:
            self.__savedPlaybackSpeedIdx = self.__playbackSpeedIdx
            self.__playbackSpeedIdx = value
            newSpeed = self.__playbackSpeedModifiers[self.__playbackSpeedIdx]
            self.__enableInGameEffects(0.0 < newSpeed < 8.0)
            g_replayEvents.onMuteSound(newSpeed == 0.0)
            player = BigWorld.player()
            if newSpeed != self.__replayCtrl.playbackSpeed:
                if newSpeed == 0:
                    if player.gunRotator is not None:
                        self.__gunWasLockedBeforePause = player.gunRotator._VehicleGunRotator__isLocked
                        player.gunRotator.lock(True)
                    self.__showInfoMessage(b'replayPaused')
                    isPaused = True
                elif player.gunRotator is not None:
                    player.gunRotator.lock(self.__gunWasLockedBeforePause)
                newSpeedStr = self.__playbackSpeedModifiersStr[self.__playbackSpeedIdx]
                self.__showInfoMessage(b'replaySpeedChange', {b'speed': newSpeedStr})
                isPaused = False
                self.__replayCtrl.playbackSpeed = newSpeed
                g_replayEvents.onPause(isPaused)
            return

    def getPlaybackSpeedIdx(self):
        ret = self.__playbackSpeedModifiers.index(self.__replayCtrl.playbackSpeed)
        if ret == -1:
            return self.__playbackSpeedModifiers.index(1.0)
        return ret

    def setControlMode(self, value):
        self.__replayCtrl.controlMode = value
        return

    def getControlMode(self):
        return self.__replayCtrl.controlMode

    def onClientReady(self):
        player = BigWorld.player()
        if not (self.isPlaying or self.isRecording):
            return
        self.__replayCtrl.playerVehicleID = player.playerVehicleID
        self.__replayCtrl.onClientReady()
        if self.isPlaying:
            if not BigWorld.IS_CONSUMER_CLIENT_BUILD:
                self.__logSVNInfo()
            AreaDestructibles.g_destructiblesManager.onAfterReplayTimeWarp()
            if isPlayerAvatar():
                player.onVehicleEnterWorld += self.__onVehicleEnterWorld
                player.onObserverVehicleChanged += self.__onObserverVehicleChanged
                if isServerSideReplay():
                    otherVehicles = [x for x in BigWorld.entities.valuesOfType(b'Vehicle') if x.id != player.playerVehicleID]
                    self.bindToVehicleForServerSideReplay(player.playerVehicleID)
                    player.updateVehicleHealth(player.playerVehicleID, 0, 0, 1, 0)
                    if otherVehicles:
                        if self.__lastObservedVehicleID not in BigWorld.entities.keys():
                            self.bindToVehicleForServerSideReplay(otherVehicles[-1].id)
                        else:
                            self.bindToVehicleForServerSideReplay(self.__lastObservedVehicleID)
            if not self.isServerSideReplay:
                self.appLoader.attachCursor(settings.APP_NAME_SPACE.SF_BATTLE, flags=GUI_CTRL_MODE_FLAG.CURSOR_ATTACHED)
        if self.isRecording:
            player = BigWorld.player()
            arena = player.arena
            arenaName = arena.arenaType.geometry
            i = arenaName.find(b'/')
            if i != -1:
                arenaName = arenaName[i + 1:]
            now = datetime.datetime.now()
            now = b'%02d.%02d.%04d %02d:%02d:%02d' % (now.day, now.month, now.year, now.hour, now.minute, now.second)
            vehicleName = BigWorld.entities[player.playerVehicleID].typeDescriptor.name
            vehicleName = vehicleName.replace(b':', b'-')
            vehicles = self.__getArenaVehiclesInfo()
            gameplayID = player.arenaTypeID >> 16
            clientVersionFromXml = getFullClientVersion()
            clientVersionFromExe = BigWorld.getProductVersion()
            arenaInfo = {b'dateTime': now, 
               b'playerName': (player.name), 
               b'playerID': (self.__playerDatabaseID), 
               b'playerVehicle': vehicleName, 
               b'mapName': arenaName, 
               b'arenaUniqueID': (arena.arenaUniqueID), 
               b'mapDisplayName': (arena.arenaType.name), 
               b'gameplayID': (ArenaType.getGameplayName(gameplayID) or gameplayID), 
               b'vehicles': vehicles, 
               b'battleType': (arena.bonusType), 
               b'clientVersionFromExe': clientVersionFromExe, 
               b'clientVersionFromXml': clientVersionFromXml, 
               b'serverName': (self.connectionMgr.serverUserName), 
               b'regionCode': (constants.AUTH_REALM), 
               b'serverSettings': (self.__serverSettings), 
               b'hasMods': (self.__replayCtrl.hasMods)}
            if not BigWorld.IS_CONSUMER_CLIENT_BUILD:
                arenaInfo[b'branchURL'], arenaInfo[b'lastChangedRevision'] = self.__getBranchAndRevision()
            if BigWorld.player().arena.guiType == constants.ARENA_GUI_TYPE.BOOTCAMP:
                from bootcamp.Bootcamp import g_bootcamp
                arenaInfo[b'lessonId'] = g_bootcamp.getLessonNum()
                arenaInfo[b'bootcampCtx'] = g_bootcamp.serializeContext()
            self.__replayCtrl.recMapName = arenaName
            self.__replayCtrl.recPlayerVehicleName = vehicleName
            self.__replayCtrl.recBattleModeTag = _ARENA_GUI_TYPE_TO_MODE_TAG.get(arena.guiType, b'')
            self.__replayCtrl.setArenaInfoStr(json.dumps(_JSON_Encode(arenaInfo)))
        else:
            self.__showInfoMessages()
            if self.replayTimeout > 0:
                LOG_DEBUG(b'replayTimeout set for %.2f' % float(self.replayTimeout))
                BigWorld.callback(float(self.replayTimeout), BigWorld.quit)
        return

    def bindToVehicleForServerSideReplay(self, vehicleID):
        LOG_DEBUG(b'Avatar.bindToVehicleForServerSideReplay: vehicleID=%s' % vehicleID)
        player = BigWorld.player()
        player.isObserverFPV, isObserverFPV = False, player.isObserverFPV
        if player.isObserverFPV != isObserverFPV:
            player.set_isObserverFPV(isObserverFPV)
        BWReplay.withholdEntity(vehicleID, False)
        BWReplay.injectNonVolatileUpdate(player.id, vehicleID, player.position, (
         player.yaw, player.pitch, player.roll))
        player.onSwitchViewpoint(vehicleID, Math.Vector3(0, 0, 0))
        return

    @property
    def isNormalSpeed(self):
        return self.playbackSpeed == 1.0

    def __getBranchAndRevision(self):
        from vcs import svn
        svnInstance = svn()
        if not svnInstance.enabled():
            return (b'undefined', b'undefined')
        else:
            info = svnInstance.getInfo()
            if info is None:
                return (b'undefined', b'undefined')
            rootPath = info.workingCopyRootAbsPath
            info = svnInstance.getInfo(rootPath)
            if info is None:
                return (b'undefined', b'undefined')
            return (
             info.branchURL, info.lastChangedRevision)

    def __logSVNInfo(self):
        if self.isServerSideReplay:
            return
        else:
            currentBranch, currentRevision = self.__getBranchAndRevision()
            replayBranch = self.arenaInfo.get(b'branchURL')
            if replayBranch is None:
                replayBranch = b'undefined'
            replayRevision = self.arenaInfo.get(b'lastChangedRevision')
            if replayRevision is None:
                replayRevision = b'undefined'
            _logger.info(b'Current branch: ' + currentBranch)
            _logger.info(b'Current revision: ' + str(currentRevision))
            _logger.info(b'Replay branch: ' + replayBranch)
            _logger.info(b'Replay revision: ' + str(replayRevision))
            return

    def __showInfoMessages(self):
        self.__showInfoMessage(b'replayControlsHelp1')
        self.__showInfoMessage(b'replayControlsHelp2')
        self.__showInfoMessage(b'replayControlsHelp3')
        return

    def __getArenaVehiclesInfo(self):
        vehicles = {}
        for k, v in BigWorld.player().arena.vehicles.iteritems():
            vehicle = copy.copy(v)
            vehicle[b'vehicleType'] = v[b'vehicleType'].name if v[b'vehicleType'] is not None else b''
            del vehicle[b'accountDBID']
            del vehicle[b'prebattleID']
            del vehicle[b'clanDBID']
            del vehicle[b'isPrebattleCreator']
            del vehicle[b'isAvatarReady']
            del vehicle[b'outfitCD']
            vehicles[k] = vehicle

        return vehicles

    def loadServerSettings(self):
        if self.isPlaying:
            try:
                if not self.isServerSideReplay:
                    self.__serverSettings = self.arenaInfo.get(b'serverSettings')
                else:
                    self.__serverSettings = pickle.loads(zlib.decompress(self.__serverSettings))
            except Exception:
                LOG_WARNING(b'There is problem while unpacking server settings from replay')
                if constants.IS_DEVELOPMENT:
                    LOG_CURRENT_EXCEPTION()

            self.lobbyContext.setServerSettings(self.__serverSettings)
        return

    def disableTimeWarp(self):
        self.__enableTimeWarp = False
        return

    def enableTimeWarp(self):
        if self.isPlaying:
            self.__enableTimeWarp = True
        return

    def onBattleLoadingFinished(self):
        self.enableTimeWarp()
        if self.isPlaying:
            self.__replayCtrl.onBattleLoadingFinished()
        return

    def onReplayFinished(self):
        replayTimes = self.__replayCtrl.getReplayTimes() - 1
        if replayTimes > 0:
            self.__replayCtrl.setReplayTimes(replayTimes)
            self.timeWarp(self.__actualReplayStartTime)
            return
        self.__replayCtrl.processFinish()
        if not self.scriptModalWindowsEnabled:
            self.stop()
            return
        if self.__isPlayingPlayList:
            self.stop()
            BigWorld.callback(1.0, self.play)
            return
        self.__isMenuShowed = False
        self.gameplay.postStateEvent(ReplayEventID.REPLAY_FINISHED)
        self.__isFinished = True
        self.setPlaybackSpeedIdx(0)
        return

    def onControlModeChanged(self, forceControlMode=None):
        player = BigWorld.player()
        if not self.isPlaying or not isPlayerAvatar():
            return
        entity = BigWorld.entities.get(self.playerVehicleID)
        if (entity is None or not entity.isStarted) and forceControlMode is None:
            controlMode = self.getControlMode()
            if controlMode == CTRL_MODE_NAME.SNIPER:
                return
        if not self.isControllingCamera and forceControlMode is None:
            return
        else:
            controlMode = self.getControlMode() if forceControlMode is None else forceControlMode
            if forceControlMode is None and not self.isControllingCamera and controlMode in _IGNORED_SWITCHING_CTRL_MODES:
                return
            if self.__equipmentId is None and controlMode == CTRL_MODE_NAME.MAP_CASE_ARCADE:
                return
            preferredPos = self.getGunRotatorTargetPoint()
            if controlMode == CTRL_MODE_NAME.MAP_CASE:
                _, _, preferredPos, _ = self.getGunMarkerParams(preferredPos, Math.Vector3(0.0, 0.0, 1.0))
            player.inputHandler.onControlModeChanged(controlMode, camMatrix=BigWorld.camera().matrix, preferredPos=preferredPos, saveZoom=False, saveDist=False, equipmentID=self.__equipmentId, curVehicleID=self.__replayCtrl.playerVehicleID)
            return

    def onPlayerVehicleIDChanged(self):
        player = BigWorld.player()
        if self.isPlaying and hasattr(player, b'positionControl'):
            player.inputHandler.ctrl.selectPlayer(self.__replayCtrl.playerVehicleID)
        return

    def __onAvatarObserverVehicleChanged(self, vehID):
        if self.isServerSideReplay:
            self.__isVehicleChanging = True
            if vehID != BigWorld.player().playerVehicleID:
                self.__lastObservedVehicleID = vehID
            self.__aoi.changeVehicle(vehID)
        self.__isVehicleChanging = False
        return

    def isVehicleChanging(self):
        return self.__isVehicleChanging

    def isAllyToObservedVehicle(self, vehID):
        observedVehicleID = self.__aoi.currentVehicleID
        if not observedVehicleID:
            return False
        arenaVehicles = BigWorld.player().arena.vehicles
        currTeam = arenaVehicles[observedVehicleID][b'team']
        vehTeam = arenaVehicles[vehID][b'team']
        return currTeam == vehTeam

    def onPostTickCallback(self):
        self.__aoi.flush(self.getControlMode())
        currentTime = self.currentTime
        if currentTime < self.__actualReplayStartTime:
            self.timeWarp(self.__actualReplayStartTime)
        elif currentTime > self.__actualReplayEndTime:
            self.onReplayFinished()
        return

    def setAmmoSetting(self, idx):
        if not isPlayerAvatar():
            return
        if self.isRecording:
            self.__replayCtrl.onAmmoButtonPressed(idx)
        return

    def __onAmmoButtonPressed(self, idx):
        self.onAmmoSettingChanged(idx)
        return

    def onSniperModeChanged(self, enable):
        if self.isPlaying:
            if enable:
                TriggersManager.g_manager.activateTrigger(TriggersManager.TRIGGER_TYPE.SNIPER_MODE)
            else:
                TriggersManager.g_manager.deactivateTrigger(TriggersManager.TRIGGER_TYPE.SNIPER_MODE)
        elif self.isRecording:
            self.__replayCtrl.onSniperMode(enable)
        return

    def onLockTarget(self, lock, playVoiceNotifications):
        if not isPlayerAvatar():
            return
        if self.isPlaying:
            BigWorld.player().onLockTarget(lock, playVoiceNotifications)
        elif self.isRecording:
            self.__replayCtrl.onLockTarget(lock, playVoiceNotifications)
        return

    def onBattleChatMessage(self, messageText, isCurrentPlayer):
        from messenger import MessengerEntry
        if self.isRecording:
            self.__replayCtrl.onBattleChatMessage(messageText, isCurrentPlayer)
        elif self.isPlaying and not self.isTimeWarpInProgress:
            if self.__isChatPlaybackEnabled:
                MessengerEntry.g_instance.gui.addClientMessage(messageText, isCurrentPlayer)
        return

    def setFpsPingLag(self, fps, ping, isLaggingNow):
        self.__replayCtrl.fps = fps
        self.__replayCtrl.ping = ping
        self.__replayCtrl.isLaggingNow = isLaggingNow
        return

    def onClientVersionDiffers(self):
        if not self.scriptModalWindowsEnabled:
            self.acceptVersionDiffering()
            return
        self.gameplay.postStateEvent(ReplayEventID.REPLAY_VERSION_CONFIRMATION)
        return

    def acceptVersionDiffering(self):
        self.__replayCtrl.confirmDlgAccepted()
        return

    def registerReplayFileExtension(self):
        self.__replayCtrl.registerReplayFileExtension()
        return

    def enableAutoRecordingBattles(self, enable, delete=False):
        if self.__isAutoRecordingEnabled == enable:
            return
        else:
            self.__isAutoRecordingEnabled = enable
            if enable:
                if enable == 1:
                    self.setResultingFileName(FIXED_REPLAY_FILENAME, True)
                elif enable == 2:
                    self.setResultingFileName(None)
                g_playerEvents.onAccountBecomePlayer += self.__startAutoRecord
                self.__startAutoRecord()
            else:
                g_playerEvents.onAccountBecomePlayer -= self.__startAutoRecord
                if self.isRecording:
                    self.stop(delete=delete)
            return

    def setResultingFileName(self, fileName, overwriteExisting=False):
        self.__replayCtrl.setResultingFileName(fileName or b'', overwriteExisting)
        return

    def timeWarp(self, time):
        self.__timeWarp(time)
        return

    def __showInfoMessage(self, msg, args=None):
        if not self.isTimeWarpInProgress:
            g_replayEvents.onWatcherNotify(msg, args)
        return

    def __startAutoRecord(self):
        if not self.__isAutoRecordingEnabled:
            return
        if self.isPlaying:
            return
        if self.isRecording or not isPlayerAccount():
            return
        self.record()
        return

    def __goToNextReplay(self):
        self.gameplay.postStateEvent(ReplayEventID.REPLAY_NEXT)
        self.connectionMgr.onDisconnected -= self.__goToNextReplay
        return

    def setArenaStatisticsStr(self, arenaUniqueStr):
        self.__replayCtrl.setArenaStatisticsStr(arenaUniqueStr)
        return

    def __onBattleResultsReceived(self, isPlayerVehicle, results):
        if isPlayerVehicle:
            modifiedResults = copy.deepcopy(results)
            allPlayersVehicles = modifiedResults.get(b'vehicles', None)
            if allPlayersVehicles is not None:
                for playerVehicles in allPlayersVehicles.itervalues():
                    for vehicle in playerVehicles:
                        if vehicle is not None:
                            vehicle[b'damageEventList'] = None

            personals = modifiedResults.get(b'personal', None)
            if personals is not None:
                for personal in personals.itervalues():
                    for field in (b'damageEventList', b'xpReplay', b'creditsReplay', b'tmenXPReplay', b'flXPReplay', b'goldReplay', b'crystalReplay', b'eventCoinReplay', b'bpcoinReplay', b'freeXPReplay', b'avatarDamageEventList', b'equipCoinReplay', b'battlePassPointsReplay', b'paragonCoinsReplay'):
                        personal[field] = None

                    for currency in personal.get(b'currencies', {}).itervalues():
                        currency[b'replay'] = None

            common = modifiedResults.get(b'common', None)
            if common is not None:
                common[b'accountCompDescr'] = None
            modifiedResults = (modifiedResults, self.__getArenaVehiclesInfo(),
             BigWorld.player().arena.statistics)
            try:
                self.__replayCtrl.setArenaStatisticsStr(json.dumps(_JSON_Encode(modifiedResults)))
            except Exception:
                LOG_ERROR(b'__onBattleResultsReceived::setArenaStatisticsStr _JSON_Encode error!')

        return

    def __onAccountBecomePlayer(self):
        self.enableAutoRecordingBattles(True)
        if not isPlayerAccount():
            return
        else:
            player = BigWorld.player()
            serverSettings = player.serverSettings
            for cfgName in INBATTLE_CONFIGS:
                self.__serverSettings[cfgName] = serverSettings[cfgName]

            if player.databaseID is None:
                BigWorld.callback(0.1, self.__onAccountBecomePlayer)
            else:
                self.__playerDatabaseID = player.databaseID
            return

    def __onSettingsChanging(self, *_):
        if not self.isPlaying:
            return
        newSpeed = self.__playbackSpeedModifiers[self.__playbackSpeedIdx]
        newQuiet = newSpeed == 0 or newSpeed > 4.0
        g_replayEvents.onMuteSound(newQuiet)
        return

    def __timeWarp(self, time):
        if not self.isPlaying or not self.__enableTimeWarp:
            return
        g_replayEvents.onTimeWarpStart()
        if self.__isFinished:
            self.setPlaybackSpeedIdx(self.__savedPlaybackSpeedIdx)
        self.__isFinished = False
        self.__warpTime = time
        self.__rewind = time < self.__replayCtrl.getTimeMark(REPLAY_TIME_MARK_CURRENT_TIME)
        AreaDestructibles.g_destructiblesManager.onBeforeReplayTimeWarp(self.__rewind)
        self.__updateGunOnTimeWarp = True
        EffectsList.EffectsListPlayer.clear()
        if self.__rewind:
            self.appLoader.detachCursor(settings.APP_NAME_SPACE.SF_BATTLE)
            playerControlModeName = BigWorld.player().inputHandler.ctrlModeName
            self.__wasVideoBeforeRewind = playerControlModeName == CTRL_MODE_NAME.VIDEO
            self.__videoCameraMatrix.set(BigWorld.camera().matrix)
            BigWorld.PyGroundEffectManager().stopAll()
            BigWorld.clearDecals()
        g_replayEvents.onMuteSound(True)
        self.__enableInGameEffects(False)
        if self.__rewind:
            self.gameplay.postStateEvent(ReplayEventID.REPLAY_REWIND)
        if not self.__replayCtrl.beginTimeWarp(time):
            self.__cleanupAfterTimeWarp()
            return
        self.__rewind = False
        return

    def __enableInGameEffects(self, enable):
        AreaDestructibles.g_destructiblesManager.forceNoAnimation = not enable
        return

    def getSetting(self, key, default=None):
        if self.__settings.has_key(key):
            return pickle.loads(base64.b64decode(self.__settings.readString(key)))
        return default

    def setSetting(self, key, value):
        self.__settings.write(key, base64.b64encode(pickle.dumps(value)))
        diff = {key: value}
        self.settingsCore.onSettingsChanged(diff)
        return

    def isFinished(self):
        if self.isPlaying or g_replayCtrl.isTimeWarpInProgress:
            return self.__isFinished
        return False

    def isFinishedNoPlayCheck(self):
        return self.__isFinished

    def isNeedToPlay(self, entity_id):
        return self.__replayCtrl.isEffectNeedToPlay(entity_id)

    def setUseServerAim(self, server_aim):
        if self.isPlaying:
            self.onServerAimChanged(server_aim)
        elif self.isRecording:
            self.__replayCtrl.onServerAim(server_aim)
        return

    def printAIMType(self):
        if self.isServerAim:
            print b'SERVER_AIM_ACTIVE'
        else:
            print b'CLIENT_AIM_ACTIVE'
        return

    def setEquipmentID(self, value):
        self.__replayCtrl.onSetEquipmentID(value)
        return

    def onSetEquipmentId(self, equipmentId):
        inputHandler = BigWorld.player().inputHandler
        if equipmentId != -1:
            self.__equipmentId = equipmentId
            inputHandler.showClientGunMarkers(False)
            if self.getControlMode() == CTRL_MODE_NAME.MAP_CASE and inputHandler.ctrl.equipmentID != equipmentId:
                inputHandler.ctrl.activateEquipment(equipmentId)
        else:
            inputHandler.showClientGunMarkers(True)
            self.__equipmentId = None
        return

    def __onVehicleEnterWorld(self, vehicle):
        if vehicle.id == self.playerVehicleID:
            if self.__replayCtrl.isControllingCamera:
                self.onControlModeChanged(self.getControlMode())
        return

    def __onObserverVehicleChanged(self):
        if self.__replayCtrl.isControllingCamera and not self.__isAllowedSavedCamera():
            self.__replayCtrl.isControllingCamera = False
        return

    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        if self.isRecording:
            if self.__arenaPeriod == period and period == ARENA_PERIOD.BATTLE and self.__previousPeriod != period:
                self.__perviousPeriod = period
                self.resetArenaPeriod()
        self.__arenaPeriod = period
        self.__arenaPeriodLength = periodLength
        self.__replayCtrl.arenaPeriod = period
        self.__replayCtrl.arenaLength = periodLength
        if period == ARENA_PERIOD.BATTLE:
            self.recalculateReplayTimes()
        return

    def recalculateReplayTimes(self):
        replayStartTime = self.__replayStartTime
        replayEndTime = self.__replayEndTime
        if self.__replayCtrl.isUsingReverseTimeFormat() and self.__arenaPeriodLength > 0:
            if replayStartTime != 0:
                replayStartTime = self.__arenaPeriodLength - replayStartTime
            if replayEndTime != float(b'inf'):
                replayEndTime = self.__arenaPeriodLength - replayEndTime
        totalReplayTime = self.__replayCtrl.getTimeMark(REPLAY_TIME_MARK_REPLAY_FINISHED)
        replayStartTime = min(replayStartTime, replayEndTime - MIN_REPLAY_TIME, totalReplayTime - MIN_REPLAY_TIME)
        replayStartTime = max(replayStartTime, 0)
        self.__actualReplayStartTime = replayStartTime
        self.__actualReplayEndTime = replayEndTime
        return

    def __onBootcampAccountMigrationComplete(self):
        if self.isRecording:
            self.stop(delete=True)
        return

    def setDataCallback(self, name, callback):
        eventHandler = self.__replayCtrl.getCallbackHandler(name)
        if eventHandler is None:
            eventHandler = Event.Event()
            self.__replayCtrl.setDataCallback(name, eventHandler)
        eventHandler += callback
        return

    def serializeCallbackData(self, cbkName, data):
        self.__replayCtrl.serializeCallbackData(cbkName, data)
        return

    def delDataCallback(self, name, callback):
        eventHandler = self.__replayCtrl.getCallbackHandler(name)
        if eventHandler is not None:
            eventHandler -= callback
        return

    def __onTimeWarpFinished(self):
        self.__cleanupAfterTimeWarp()
        return

    def __cleanupAfterTimeWarp(self):
        self.__warpTime = -1.0
        self.__enableInGameEffects(0.0 < self.__playbackSpeedModifiers[self.__playbackSpeedIdx] < 8.0)
        mute = not 0.0 < self.__playbackSpeedModifiers[self.__playbackSpeedIdx] < 8.0
        g_replayEvents.onMuteSound(mute)
        if self.__wasVideoBeforeRewind:
            BigWorld.player().inputHandler.onControlModeChanged(b'video', prevModeName=b'arcade', camMatrix=self.__videoCameraMatrix)
            self.__wasVideoBeforeRewind = False
        g_replayEvents.onTimeWarpFinish()
        return

    def onRespawnMode(self, enabled):
        self.__replayCtrl.onRespawnMode(enabled)
        return

    def __isAllowedSavedCamera(self):
        if BigWorld.player().isObserver():
            return BigWorld.player().arenaBonusType not in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE
        return True

    def __getArenaInfo(self):
        arenaInfoStr = self.__replayCtrl.getArenaInfoStr()
        if arenaInfoStr:
            return json.loads(arenaInfoStr)
        else:
            return


def _JSON_Encode(obj):
    if isinstance(obj, dict):
        newDict = {}
        for key, value in obj.iteritems():
            if isinstance(key, tuple):
                newDict[str(key)] = _JSON_Encode(value)
            else:
                newDict[key] = _JSON_Encode(value)

        return newDict
    if isinstance(obj, (list, tuple, set, frozenset)):
        newList = []
        for value in obj:
            newList.append(_JSON_Encode(value))

        return newList
    return obj


def isPlaying():
    if g_replayCtrl is not None:
        return g_replayCtrl.isPlaying or g_replayCtrl.isTimeWarpInProgress
    else:
        return False


def isServerSideReplay():
    if g_replayCtrl is not None:
        return g_replayCtrl.isServerSideReplay
    else:
        return False


def isLoading():
    return g_replayCtrl is not None and g_replayCtrl.isLoading


def isFinished():
    return g_replayCtrl is not None and g_replayCtrl.isFinishedNoPlayCheck()


def getSpaceID():
    if g_replayCtrl is not None:
        return g_replayCtrl.getSpaceID()
    else:
        return BigWorld.player().spaceID
