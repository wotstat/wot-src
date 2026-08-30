import ScaleformFileLoader, WWISE
from bc_intro_page import BCIntroPage, INTRO_HIGHLIGHT_TYPE
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from bootcamp.BootCampEvents import g_bootcampEvents
from uilogging.deprecated.decorators import loggerTarget, loggerEntry, simpleLog
from uilogging.deprecated.bootcamp.constants import BC_LOG_ACTIONS, BC_LOG_KEYS
from uilogging.deprecated.bootcamp.loggers import BootcampUILogger
from gui.Scaleform import SCALEFORM_SWF_PATH_V3
from sound_gui_manager import CommonSoundSpaceSettings
_DEFAULT_VIDEO_BUFFERING_TIME = 0.0

@loggerTarget(logKey=BC_LOG_KEYS.BC_INTRO_VIDEO, loggerCls=BootcampUILogger)
class BCIntroVideoPage(BCIntroPage, IArenaVehiclesController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _HANGAR_OVERLAY_STATE = b'STATE_video_overlay'
    __SOUND_SETTINGS = CommonSoundSpaceSettings(name=b'hangar_video', entranceStates={_HANGAR_OVERLAY_STATE: ((b'{}_on').format(_HANGAR_OVERLAY_STATE))}, exitStates={_HANGAR_OVERLAY_STATE: ((b'{}_off').format(_HANGAR_OVERLAY_STATE))}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
    _COMMON_SOUND_SPACE = __SOUND_SETTINGS

    def __init__(self, settings):
        super(BCIntroVideoPage, self).__init__(settings)
        self._movieFile = settings.get(b'video', b'')
        self._backgroundVideo = settings.get(b'backgroundVideo', b'')
        self._backgroundVideoBufferTime = settings.get(b'bufferTime', _DEFAULT_VIDEO_BUFFERING_TIME)
        self._backgroundMusicStartEvent = settings.get(b'backgroundMusicStartEvent', b'')
        self._backgroundMusicStopEvent = settings.get(b'backgroundMusicStopEvent', b'')
        self._backgroundMusicPauseEvent = settings.get(b'backgroundMusicPauseEvent', b'')
        self._backgroundMusicResumeEvent = settings.get(b'backgroundMusicResumeEvent', b'')
        self._backgroundMusicToLoopEvent = settings.get(b'backgroundMusicToLoopEvent', b'')
        self._goToBattleEvent = g_bootcampEvents.onBootcampGoNext
        self._delaySpaceLoaded = False
        self._started = False
        return

    def stopVideo(self):
        self._onFinish()
        return

    def updateSpaceLoadProgress(self, progress):
        if not self._videoPlayerVisible:
            self.as_updateProgressS(progress)
        return

    def _getVideoFiles(self):
        return [(b'/').join((SCALEFORM_SWF_PATH_V3, videoName)) for videoName in (self._movieFile, self._backgroundVideo) if videoName]

    def _populate(self):
        videoFiles = self._getVideoFiles()
        if videoFiles:
            ScaleformFileLoader.enableStreaming(videoFiles)
            self._videoPlayerVisible = True
        g_bootcampEvents.onArenaStarted += self._onArenaStarted
        g_bootcampEvents.onBootcampSpaceLoaded += self._onBootcampSpaceLoaded
        self.sessionProvider.addArenaCtrl(self)
        super(BCIntroVideoPage, self)._populate()
        return

    def _dispose(self):
        if self._getVideoFiles():
            ScaleformFileLoader.disableStreaming()
        g_bootcampEvents.onBootcampSpaceLoaded -= self._onBootcampSpaceLoaded
        g_bootcampEvents.onArenaStarted -= self._onArenaStarted
        self.sessionProvider.removeArenaCtrl(self)
        super(BCIntroVideoPage, self)._dispose()
        return

    def _onBootcampSpaceLoaded(self):
        if self._started:
            self._onLoaded()
        else:
            self._delaySpaceLoaded = True
        return

    def _onArenaStarted(self):
        self.destroy()
        return

    @simpleLog(action=BC_LOG_ACTIONS.SKIP_VIDEO)
    def _onFinish(self):
        if self._movieFile and self._backgroundMusicToLoopEvent:
            WWISE.WW_eventGlobal(self._backgroundMusicToLoopEvent)
        g_bootcampEvents.onIntroVideoStop()
        if self._videoPlayerVisible:
            self._showHighlight()
        return

    @loggerEntry
    def _start(self):
        super(BCIntroVideoPage, self)._start()
        self._started = True
        if self._delaySpaceLoaded:
            self._onLoaded()
        return

    def _onLoaded(self):
        self.as_loadedS()
        if not self._videoPlayerVisible:
            self._showHighlight()
        return

    def _showHighlight(self):
        if self._shouldHighlight(INTRO_HIGHLIGHT_TYPE.START_BUTTON):
            self._setHighlighting(INTRO_HIGHLIGHT_TYPE.WELCOME_START_BUTTON if self._videoPlayerVisible else INTRO_HIGHLIGHT_TYPE.START_BUTTON, True)
        if self._isCurrentlyHighlighting(INTRO_HIGHLIGHT_TYPE.ARROWS):
            self._setHighlighting(INTRO_HIGHLIGHT_TYPE.ARROWS, False)
        return

    @simpleLog(action=BC_LOG_ACTIONS.CONTINUE_BUTTON_PRESSED, logOnce=True, restrictions={b'lesson_id': 0}, validate=False)
    def goToBattle(self):
        super(BCIntroVideoPage, self).goToBattle()
        return
