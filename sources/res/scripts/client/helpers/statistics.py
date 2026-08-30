import BigWorld, ResMgr, Settings, Sound
from constants import ARENA_PERIOD, INVALID_CLIENT_STATS
from account_helpers.settings_core.settings_constants import GRAPHICS, SOUND, SoundPhysicsQuality
from gui.shared.utils.graphics import getGraphicsEngineValue
from gui.shared.utils import monitor_settings
from debug_utils import LOG_DEBUG, LOG_NOTE
from helpers import dependency, isPlayerAvatar
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.helpers.statistics import IStatisticsCollector
from uilogging.helpers import getClientPeripheryID
STATISTICS_VERSION = b'0.0.2'
_OLD_CUSTOM_PRESET_IDX = 6
_NEW_CUSTOM_PRESET_IDX = 5

class _STATISTICS_STATE(object):
    STARTED = 0
    IN_PROGRESS = 1
    STOPPED = 2


class HARDWARE_SCORE_PARAMS(object):
    PARAM_GPU_MEMORY = 0
    PARAM_GPU_SHARED = 1
    PARAM_GPU_SCORE = 2
    PARAM_CPU_SCORE = 3
    PARAM_CPU_CORES = 4
    PARAM_RAM = 5
    PARAM_VIRTUAL_MEMORY = 6
    MAX_PARAMS = 7


class HANGAR_LOADING_STATE(object):
    LOGIN = 0
    CONNECTED = 1
    SHOW_GUI = 2
    QUESTS_SYNC = 3
    USER_SERVER_SETTINGS_SYNC = 4
    START_LOADING_SPACE = 5
    START_LOADING_VEHICLE = 6
    FINISH_LOADING_VEHICLE = 7
    FINISH_LOADING_SPACE = 8
    HANGAR_UI_READY = 9
    TRAINING_UI_READY = 10
    HANGAR_READY = 11
    START_LOADING_TUTORIAL = 12
    FINISH_LOADING_TUTORIAL = 13
    DISCONNECTED = 14
    COUNT = 15


_HANGAR_LOADING_STATES_PREFIX = b'HANGAR LOADING STATE'
_HANGAR_LOADING_STATES = [
 25, 26, 27, 28, 29, 30, 
 31, 32, 33, 
 34, 35, 
 36, 37, 38, 
 39]
_HANGAR_LOADING_STATES_IDS = [HANGAR_LOADING_STATE.FINISH_LOADING_VEHICLE,
 HANGAR_LOADING_STATE.FINISH_LOADING_SPACE,
 HANGAR_LOADING_STATE.FINISH_LOADING_TUTORIAL,
 HANGAR_LOADING_STATE.HANGAR_READY]
_IMPORTANT_GRAPHICS_SETTINGS_SET = {
 40, 
 41, 
 42, 
 43, 
 44, 
 45, 
 46, 
 47, 
 48, 
 49}
_OTHER_GRAPHICS_SETTINGS_SET = {
 50, 
 51, 
 52, 
 53, 
 54, 
 55, 
 56, 
 57, 
 58, 
 59}
_VIDEO_MODE_SIZE_CHANGE_SET = {
 GRAPHICS.WINDOW_SIZE,
 GRAPHICS.RESOLUTION,
 GRAPHICS.BORDERLESS_SIZE}

class StatisticsCollector(IStatisticsCollector):
    update = property((lambda self: self.__updateFunc))
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)
    connectionMgr = dependency.descriptor(IConnectionManager)
    hangarSpace = dependency.descriptor(IHangarSpace)
    gameSession = dependency.descriptor(IGameSessionController)

    def __init__(self):
        self.__state = _STATISTICS_STATE.STOPPED
        self.__hangarLoaded = False
        self.__invalidStats = 0
        self.__dynEvents = []
        self.reset()
        self.__needCollectSystemData = False
        self.__needCollectSessionData = False
        self.__hangarWasLoadedOnce = False
        self.__sendFullStat = False
        self.__loadingStates = [
         0.0] * HANGAR_LOADING_STATE.COUNT
        self.__loadingInitialState = HANGAR_LOADING_STATE.LOGIN
        self.__hangarLoadingTime = 0.0
        self.__lastArenaUniqueID = 0
        self.__lastArenaTypeID = 0
        self.__lastArenaTeam = 0
        self.__randomEvents = []
        self.__blArenaPeriod = 0
        return

    def init(self):
        self.connectionMgr.onDisconnected += self.__onClientDisconnected
        self.hangarSpace.onSpaceCreate += self.__onHangarSpaceLoaded
        return

    def fini(self):
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self.connectionMgr.onDisconnected -= self.__onClientDisconnected
        self.hangarSpace.onSpaceCreate -= self.__onHangarSpaceLoaded
        self.__updateFunc = None
        return

    def start(self):
        self.stop()
        self.reset()
        self.__state = _STATISTICS_STATE.STARTED
        return

    def stop(self):
        if self.__state != _STATISTICS_STATE.STOPPED:
            self.__state = _STATISTICS_STATE.STOPPED
            BigWorld.enableBattleStatisticCollector(False)
            self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
            ctrl = self.sessionProvider.shared.drrScale
            if ctrl is not None:
                ctrl.onDRRChanged -= self.__onDRRChanged
        return

    def reset(self):
        self.__invalidStats = 0
        self.__updateFunc = self.__updateIdle
        return

    def needCollectSystemData(self, value):
        self.__needCollectSystemData = value
        self.__sendFullStat = self.__sendFullStat and value
        return

    def needCollectSessionData(self, value):
        self.__needCollectSessionData = value
        return

    def getSessionData(self):
        stat = BigWorld.wg_getClientStatistics()
        if stat:
            return self.__getSessionData(stat)
        else:
            return

    def getStatistics(self, andStop=True):
        result = {b'system': None, b'session': None}
        stat = BigWorld.wg_getClientStatistics()
        if not stat:
            return result
        else:
            if self.__sendFullStat:
                self.__sendFullStat = False
                self.__needCollectSystemData = False
                self.__needCollectSessionData = False
                result[b'system'] = self.__getSystemData(stat)
                result[b'session'] = self.__getSessionData(stat)
            if self.__needCollectSystemData:
                self.__needCollectSystemData = False
                result[b'system'] = self.__getSystemData(stat)
            if self.__needCollectSessionData:
                self.__needCollectSessionData = False
                result[b'session'] = self.__getSessionData(stat)
            if andStop is True:
                self.stop()
            return result

    def noteLastArenaData(self, arenaTypeID, arenaUniqueID, arenaTeam, randomEvents, blArenaPeriod):
        self.__lastArenaTypeID = arenaTypeID
        self.__lastArenaUniqueID = arenaUniqueID
        self.__lastArenaTeam = arenaTeam
        self.__randomEvents = randomEvents
        self.__blArenaPeriod = blArenaPeriod
        if not self.__hangarWasLoadedOnce:
            self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_STRAIGHT_INTO_BATTLE
            self.__sendFullStat = True
        return

    def noteHangarLoadingState(self, state, initialState=False, showSummaryNow=False):
        if state < 0 or state > HANGAR_LOADING_STATE.COUNT:
            LOG_DEBUG((b'Unknown hangar loading state: {0}').format(state))
            return
        if initialState:
            self.__loadingStates = [
             0] * HANGAR_LOADING_STATE.COUNT
            self.__loadingInitialState = state
        if self.__loadingStates[state] != 0.0:
            return
        exactTime = BigWorld.timeExact()
        stateName = (b'{0}: {1}').format(_HANGAR_LOADING_STATES_PREFIX, _HANGAR_LOADING_STATES[state])
        LOG_NOTE((b'{0} - {1}').format(stateName, exactTime))
        self.__loadingStates[state] = exactTime
        BigWorld.addUPLMessage(stateName)
        if showSummaryNow:
            reportHeader = _HANGAR_LOADING_STATES_PREFIX + b': SUMMARY'
            if self.__loadingStates[HANGAR_LOADING_STATE.FINISH_LOADING_TUTORIAL] != 0.0:
                reportHeader += b' (With Tutorial stage) '
            self.__hangarLoadingTime = self.__loadingStates[state] - self.__loadingStates[self.__loadingInitialState]
            LOG_NOTE(reportHeader + b' TOTAL = ' + str(self.__hangarLoadingTime))
            BigWorld.hangarLoaded(self.__hangarLoadingTime)
        return

    def __getSessionData(self, statisticsDict):
        lastArenaTypeID = self.__lastArenaTypeID
        windowMode = BigWorld.getWindowMode()
        windowModeLUT = {(BigWorld.WindowModeWindowed): 0, 
           (BigWorld.WindowModeExclusiveFullscreen): 1, 
           (BigWorld.WindowModeBorderless): 2}
        monitorSettings = monitor_settings.g_monitorSettings
        resolutionContainer = monitorSettings.screenResolution
        recommendedSoundPresetString = Sound.getRecommendedPreset()
        soundPrefs = Settings.g_instance.userPrefs[Settings.KEY_SOUND_PREFERENCES]
        selectedSoundPresetString = soundPrefs.readString(SOUND.PHYSICS_QUALITY, recommendedSoundPresetString)
        recommendedSoundPreset = SoundPhysicsQuality.ORDER.index(recommendedSoundPresetString) & 255
        selectedSoundPreset = SoundPhysicsQuality.ORDER.index(selectedSoundPresetString) & 255
        data = {b'started_at': (int(self.gameSession.sessionStartedAt)), 
           b'map': (lastArenaTypeID & 65535), 
           b'mode': (lastArenaTypeID >> 16), 
           b'spawn': (self.__lastArenaTeam), 
           b'fps_min': (statisticsDict[b'fpsMin']), 
           b'fps_max': (statisticsDict[b'fpsMax']), 
           b'fps_avg': (statisticsDict[b'fpsAvg']), 
           b'fps_0_5': (statisticsDict[b'fps_0_5']), 
           b'fps_6_10': (statisticsDict[b'fps_6_10']), 
           b'fps_11_15': (statisticsDict[b'fps_11_15']), 
           b'fps_16_20': (statisticsDict[b'fps_16_20']), 
           b'fps_21_25': (statisticsDict[b'fps_21_25']), 
           b'fps_26_30': (statisticsDict[b'fps_26_30']), 
           b'fps_31_35': (statisticsDict[b'fps_31_35']), 
           b'fps_36_40': (statisticsDict[b'fps_36_40']), 
           b'fps_gt_40': (statisticsDict[b'fps_gt_40']), 
           b'fps_41_45': (statisticsDict[b'fps_41_45']), 
           b'fps_46_50': (statisticsDict[b'fps_46_50']), 
           b'fps_51_55': (statisticsDict[b'fps_51_55']), 
           b'fps_56_60': (statisticsDict[b'fps_56_60']), 
           b'fps_61_70': (statisticsDict[b'fps_61_70']), 
           b'fps_71_80': (statisticsDict[b'fps_71_80']), 
           b'fps_81_90': (statisticsDict[b'fps_81_90']), 
           b'fps_91_100': (statisticsDict[b'fps_91_100']), 
           b'fps_101_120': (statisticsDict[b'fps_101_120']), 
           b'fps_121_140': (statisticsDict[b'fps_121_140']), 
           b'fps_141_160': (statisticsDict[b'fps_141_160']), 
           b'fps_161_180': (statisticsDict[b'fps_161_180']), 
           b'fps_gt_180': (statisticsDict[b'fps_gt_180']), 
           b'fps_deviation': (statisticsDict[b'fpsDeviation']), 
           b'ping': (statisticsDict[b'ping']), 
           b'lag': (statisticsDict[b'lag']), 
           b'graphics_preset': (self.__getPresetIdx()), 
           b'screen_res_width': (resolutionContainer.width), 
           b'screen_res_height': (resolutionContainer.height), 
           b'window_mode': (windowModeLUT.get(windowMode, 0)), 
           b'drr_scale': (int(round(BigWorld.getDRRScale() * 100))), 
           b'game_session_duration': (statisticsDict[b'gameSessionDuration']), 
           b'arena_id': (self.__lastArenaUniqueID), 
           b'periphery_id': (getClientPeripheryID()), 
           b'camera_pos_x': (statisticsDict[b'cameraPos'][0]), 
           b'camera_pos_y': (statisticsDict[b'cameraPos'][1]), 
           b'camera_pos_z': (statisticsDict[b'cameraPos'][2]), 
           b'camera_dir_x': (statisticsDict[b'cameraDir'][0]), 
           b'camera_dir_y': (statisticsDict[b'cameraDir'][1]), 
           b'camera_dir_z': (statisticsDict[b'cameraDir'][2]), 
           b'invalid_stats': (self.__invalidStats), 
           b'graphics_settings': (statisticsDict[b'graphicsSettings']), 
           b'active_time': (statisticsDict[b'activeTime']), 
           b'loading_time': (statisticsDict[b'loadingTime']), 
           b'dynamic_drr': (BigWorld.isDRRAutoscalingEnabled()), 
           b'sound_quality': (recommendedSoundPreset << 8 | selectedSoundPreset), 
           b'hangar_loading_time': (self.__hangarLoadingTime), 
           b'ram_available': (statisticsDict[b'ramAvailable']), 
           b'ram_peak': (statisticsDict[b'ramPeak']), 
           b'virt_available': (statisticsDict[b'virtAvailable']), 
           b'virt_peak': (statisticsDict[b'virtPeak']), 
           b'page_file_available': (statisticsDict[b'pageFileAvailable']), 
           b'page_file_peak': (statisticsDict[b'pageFilePeak']), 
           b'memory_critical': (statisticsDict[b'memoryCritical']), 
           b'vertical_sync': (statisticsDict[b'vertical_sync']), 
           b'gpu_utilization_low_fps': (statisticsDict[b'gpu_utilization_low_fps']), 
           b'cpu_utilization_low_fps': (statisticsDict[b'cpu_utilization_low_fps']), 
           b'gpu_utilization': (statisticsDict[b'gpu_utilization']), 
           b'cpu_utilization': (statisticsDict[b'cpu_utilization']), 
           b'random_events': (len(self.__randomEvents)), 
           b'bl_arena_period': (self.__blArenaPeriod)}
        BigWorld.wg_reportSessionData(data)
        return data

    def __getSystemData(self, statisticsDict):
        data = {b'started_at': (int(self.gameSession.sessionStartedAt)), 
           b'server_name': (self.connectionMgr.serverUserName), 
           b'is_laptop': (statisticsDict[b'isLaptop']), 
           b'cpu_vendor': (statisticsDict[b'cpuVendor']), 
           b'cpu_cores': (statisticsDict[b'cpuCores']), 
           b'cpu_freq': (statisticsDict[b'cpuFreq']), 
           b'gpu_vendor': (statisticsDict[b'gpuVendor']), 
           b'gpumemory': (statisticsDict[b'gpuMemory']), 
           b'os': (statisticsDict[b'os']), 
           b'graphics_engine': (getGraphicsEngineValue()), 
           b'cpu_score': (BigWorld.getAutoDetectGraphicsSettingsScore(HARDWARE_SCORE_PARAMS.PARAM_CPU_SCORE)), 
           b'gpu_score': (BigWorld.getAutoDetectGraphicsSettingsScore(HARDWARE_SCORE_PARAMS.PARAM_GPU_SCORE)), 
           b'os_bit': (statisticsDict[b'osBit']), 
           b'has_mods': (statisticsDict[b'hasMods']), 
           b'reason_32bit': (statisticsDict[b'reason32bit']), 
           b'cpu_family': (statisticsDict[b'cpuFamily']), 
           b'gpu_family': (statisticsDict[b'gpuFamily']), 
           b'crashed': (statisticsDict[b'crashed']), 
           b'content_type': (ResMgr.activeContentType()), 
           b'gpu_driver_version': (statisticsDict[b'gpuDriverVersion']), 
           b'graphics_api_id': (statisticsDict[b'graphicsAPIID']), 
           b'multi_gpu': (statisticsDict[b'multiGPU']), 
           b'CPU_name': (statisticsDict[b'cpuName']), 
           b'hangar_first_loading_time': (self.__hangarLoadingTime), 
           b'client_bit': (statisticsDict[b'clientBit']), 
           b'ram_total': (statisticsDict[b'ramTotal']), 
           b'virt_total': (statisticsDict[b'virtTotal']), 
           b'page_file_total': (statisticsDict[b'pageFileTotal']), 
           b'system_hdd_name': (statisticsDict[b'systemHddName']), 
           b'game_hdd_name': (statisticsDict[b'gameHddName']), 
           b'cat_hw_id': (statisticsDict[b'cat_hw_id'])}
        BigWorld.wg_reportSystemData(data)
        return data

    def __onSettingsChanged(self, diff):
        keys = set(diff.keys())
        if _VIDEO_MODE_SIZE_CHANGE_SET & keys:
            self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_RESOLUTION_CHANGED
        if GRAPHICS.VIDEO_MODE in keys:
            self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_WM_CHANGED
        if GRAPHICS.DYNAMIC_RENDERER in keys:
            self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_DRR_SCALE_CHANGED
        if _IMPORTANT_GRAPHICS_SETTINGS_SET & keys:
            self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_GS_MAJOR_CHANGED
        if _OTHER_GRAPHICS_SETTINGS_SET & keys:
            self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_GS_MINOR_CHANGED
        return

    def __onHangarSpaceLoaded(self):
        self.__hangarLoaded = True
        self.__hangarWasLoadedOnce = True
        return

    def __onClientDisconnected(self):
        self.__hangarLoaded = False
        return

    def __onDRRChanged(self):
        self.__invalidStats |= INVALID_CLIENT_STATS.CLIENT_DRR_SCALE_CHANGED
        return

    def __updateIdle(self):
        if isPlayerAvatar() and BigWorld.player().arena.period > ARENA_PERIOD.IDLE:
            self.__updateFunc = self.__updatePrebattle
            self.__updateFunc()
        return

    def __updatePrebattle(self):
        if isPlayerAvatar() and BigWorld.player().arena.period == ARENA_PERIOD.BATTLE and self.__state == _STATISTICS_STATE.STARTED:
            BigWorld.enableBattleStatisticCollector(True)
            self.settingsCore.onSettingsChanged += self.__onSettingsChanged
            ctrl = self.sessionProvider.shared.drrScale
            if ctrl is not None:
                ctrl.onDRRChanged += self.__onDRRChanged
            self.__state = _STATISTICS_STATE.IN_PROGRESS
            self.__updateFunc = self.__updateBattle
            self.__updateFunc()
        return

    def __updateBattle(self):
        return

    def __getPresetIdx(self):
        presetIdx = self.settingsCore.getSetting(GRAPHICS.PRESETS)
        if presetIdx == _NEW_CUSTOM_PRESET_IDX:
            presetIdx = _OLD_CUSTOM_PRESET_IDX
        return presetIdx
