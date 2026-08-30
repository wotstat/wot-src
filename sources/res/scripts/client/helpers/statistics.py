import BigWorld, ResMgr, Settings
from constants import ARENA_PERIOD, INVALID_CLIENT_STATS
from account_helpers.settings_core.settings_constants import GRAPHICS
from debug_utils import LOG_DEBUG, LOG_NOTE
from helpers import dependency, isPlayerAvatar
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IBootcampController
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.helpers.statistics import IStatisticsCollector
from ExtensionsManager import g_extensionsManager
STATISTICS_VERSION = b'0.0.2'

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
    GAMEFACE_UI_LOADING_SCREEN_DESTROYED = 10
    TRAINING_UI_READY = 11
    HANGAR_READY = 12
    START_LOADING_TUTORIAL = 13
    FINISH_LOADING_TUTORIAL = 14
    DISCONNECTED = 15
    COUNT = 16


_HANGAR_LOADING_STATES_PREFIX = b'HANGAR LOADING STATE'
_HANGAR_LOADING_STATES = [
 21, 22, 23, 24, 25, 26, 
 27, 28, 29, 
 30, 31, 32, 
 33, 34, 
 35, 36]
_HANGAR_LOADING_STATES_IDS = [HANGAR_LOADING_STATE.FINISH_LOADING_VEHICLE,
 HANGAR_LOADING_STATE.FINISH_LOADING_SPACE,
 HANGAR_LOADING_STATE.FINISH_LOADING_TUTORIAL,
 HANGAR_LOADING_STATE.HANGAR_READY]
_IMPORTANT_GRAPHICS_SETTINGS_SET = {
 37, 
 38, 
 39, 
 40, 
 41, 
 42, 
 43, 
 44, 
 45, 
 46}
_OTHER_GRAPHICS_SETTINGS_SET = {
 47, 
 48, 
 49, 
 50, 
 51, 
 52, 
 53, 
 54, 
 55, 
 56}
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
    bootcampController = dependency.descriptor(IBootcampController)

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
        return

    def needCollectSessionData(self, value):
        self.__needCollectSessionData = value
        return

    def getSessionData(self):
        stat = BigWorld.getClientStatistics()
        if stat:
            return self.__getSessionData(stat)
        else:
            return

    def getStatistics(self, andStop=True):
        result = {b'system': None, b'session': None}
        stat = BigWorld.getClientStatistics()
        BigWorld.clearCrashedState()
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

    def noteLastArenaData(self, arenaTypeID, arenaUniqueID, arenaTeam):
        self.__lastArenaTypeID = arenaTypeID
        self.__lastArenaUniqueID = arenaUniqueID
        self.__lastArenaTeam = arenaTeam
        if not self.__hangarWasLoadedOnce and not self.bootcampController.isInBootcamp() and not self.__isInStoryMode():
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

    def __getSessionData(self, stat):
        stat[b'graphicsPreset'] = self.settingsCore.getSetting(GRAPHICS.PRESETS)
        windowMode = BigWorld.getWindowMode()
        windowModeLUT = {(BigWorld.WindowModeWindowed): 0, 
           (BigWorld.WindowModeExclusiveFullscreen): 1, 
           (BigWorld.WindowModeBorderless): 2}
        stat[b'windowMode'] = windowModeLUT.get(windowMode, 0)
        from gui.shared.utils import monitor_settings
        monitorSettings = monitor_settings.g_monitorSettings
        resolutionContainer = monitorSettings.currentWindowSize
        if windowMode == BigWorld.WindowModeExclusiveFullscreen:
            resolutionContainer = monitorSettings.currentVideoMode
        elif windowMode == BigWorld.WindowModeBorderless:
            resolutionContainer = monitorSettings.currentBorderlessSize
        stat[b'screenResWidth'] = resolutionContainer.width
        stat[b'screenResHeight'] = resolutionContainer.height
        stat[b'drrScale'] = int(round(BigWorld.getDRRScale() * 100))
        stat[b'dynamicDRR'] = BigWorld.isDRRAutoscalingEnabled()
        stat[b'invalidStats'] |= self.__invalidStats
        stat[b'soundQuality'] = Settings.g_instance.userPrefs[Settings.KEY_SOUND_PREFERENCES].readInt(b'LQ_render', 0)
        stat[b'hangarLoadingTime'] = self.__hangarLoadingTime
        stat[b'lastArenaUniqueID'] = self.__lastArenaUniqueID
        stat[b'lastArenaTypeID'] = self.__lastArenaTypeID
        stat[b'lastArenaTeam'] = self.__lastArenaTeam
        return stat

    def __getSystemData(self, statisticsDict):
        return {b'isLaptop': (statisticsDict[b'isLaptop']), 
           b'cpuVendor': (statisticsDict[b'cpuVendor']), 
           b'cpuCores': (statisticsDict[b'cpuCores']), 
           b'cpuFreq': (statisticsDict[b'cpuFreq']), 
           b'gpuVendor': (statisticsDict[b'gpuVendor']), 
           b'gpuMemory': (statisticsDict[b'gpuMemory']), 
           b'os': (statisticsDict[b'os']), 
           b'graphicsEngine': (self.settingsCore.getSetting(GRAPHICS.RENDER_PIPELINE)), 
           b'cpuScore': (BigWorld.getAutoDetectGraphicsSettingsScore(HARDWARE_SCORE_PARAMS.PARAM_CPU_SCORE)), 
           b'gpuScore': (BigWorld.getAutoDetectGraphicsSettingsScore(HARDWARE_SCORE_PARAMS.PARAM_GPU_SCORE)), 
           b'osBit': (statisticsDict[b'osBit']), 
           b'hasMods': (statisticsDict[b'hasMods']), 
           b'reason32bit': (statisticsDict[b'reason32bit']), 
           b'cpuFamily': (statisticsDict[b'cpuFamily']), 
           b'gpuFamily': (statisticsDict[b'gpuFamily']), 
           b'crashed': (statisticsDict[b'crashed']), 
           b'prevHasMods': (statisticsDict[b'prevHasMods']), 
           b'prevCrashAddr': (statisticsDict[b'prevCrashAddr']), 
           b'prevClientVersion': (statisticsDict[b'prevClientVersion']), 
           b'contentType': (ResMgr.activeContentType()), 
           b'gpuDriverVersion': (statisticsDict[b'gpuDriverVersion']), 
           b'graphicsAPIID': (statisticsDict[b'graphicsAPIID']), 
           b'multiGPU': 0, 
           b'cpuName': (statisticsDict[b'cpuName']), 
           b'hangarFirstLoadingTime': (self.__hangarLoadingTime), 
           b'clientBit': (statisticsDict[b'clientBit']), 
           b'ramTotal': (statisticsDict[b'ramTotal']), 
           b'virtTotal': (statisticsDict[b'virtTotal']), 
           b'pageFileTotal': (statisticsDict[b'pageFileTotal']), 
           b'systemHddName': (statisticsDict[b'systemHddName']), 
           b'gameHddName': (statisticsDict[b'gameHddName'])}

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

    @staticmethod
    def __isInStoryMode():
        if not g_extensionsManager.isExtensionEnabled(b'story_mode'):
            return False
        from story_mode.skeletons.story_mode_controller import IStoryModeController
        storyModeCtrl = dependency.instance(IStoryModeController)
        return storyModeCtrl.isEnabled() and storyModeCtrl.isOnboarding
