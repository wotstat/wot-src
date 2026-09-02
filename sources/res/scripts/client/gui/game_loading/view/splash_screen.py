import logging, typing, BigWorld, ScaleformFileLoader, Settings, version_utils, game_loading_bindings, gui
from collections import namedtuple
from SoundGroups import MASTER_VOLUME_DEFAULT
from gui.Scaleform import SCALEFORM_SWF_PATH_V3
from gui.Scaleform.daapi.view.external_components import ExternalFlashComponent
from gui.Scaleform.daapi.view.external_components import ExternalFlashSettings
from gui.Scaleform.daapi.view.meta.SplashScreenMeta import SplashScreenMeta
from gui.Scaleform.genConsts.SPLASHSCREENCONSTANTS import SPLASHSCREENCONSTANTS
from gui.doc_loaders.GuiDirReader import GuiDirReader
from helpers import uniprof, clientVersionGetter
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
_logger = logging.getLogger(__name__)
_VideoSettings = namedtuple(b'_VideoSettings', [b'canBeSkipped'])
VIDEO_FADE_OUT_TIME = 250
DEFAULT_VIDEO_BUFFERING_TIME = 2.0
ALWAYS_SHOW_SPLASH_SCREEN = b'development/alwaysShowIntroVideo'

def getCompulsoryVideoSettings(path):
    for settings in gui.GUI_SETTINGS.compulsoryIntroVideos:
        if settings[b'path'] == path:
            return _VideoSettings(settings.get(b'canBeSkipped', False))

    return


def versionChanged(userPrefs):
    if userPrefs.readBool(ALWAYS_SHOW_SPLASH_SCREEN):
        return True
    mainVersion = version_utils.getClientMainVersion(clientVersionGetter)
    lastVideoVersion = userPrefs.readString(Settings.INTRO_VIDEO_VERSION, b'')
    return lastVideoVersion != mainVersion


def mustShowSplashScreen(userPrefs):
    if not gui.GUI_SETTINGS.guiEnabled:
        return False
    if userPrefs.readInt(Settings.KEY_SHOW_STARTUP_MOVIE, 1) == 1:
        if gui.GUI_SETTINGS.compulsoryIntroVideos:
            return True
        return versionChanged(userPrefs)
    return userPrefs.readBool(ALWAYS_SHOW_SPLASH_SCREEN, False)


class SplashScreen(ExternalFlashComponent, SplashScreenMeta):
    __slots__ = (b'_movieFiles', b'_writeSetting', b'_bufferTime', b'_soundValue', b'_canSkip', b'_width', b'_height', b'_currentMovie', b'_videoStarted')

    def __init__(self, preferences):
        super(SplashScreen, self).__init__(ExternalFlashSettings(b'splashScreen', b'splashScreenApp.swf', b'root.main', SPLASHSCREENCONSTANTS.ON_SPLASH_SCREEN_LOADED_CALLBACK))
        self.createExternalComponent()
        self._userPrefs = preferences
        self._movieFiles = GuiDirReader.getAvailableIntroVideoFiles()
        self._writeSetting = False
        self._bufferTime = self._userPrefs.readFloat(Settings.VIDEO_BUFFERING_TIME, DEFAULT_VIDEO_BUFFERING_TIME)
        self._soundValue = self._getVideoVolume()
        self._videoStarted = False
        self._canSkip = True
        self._currentMovie = None
        self._width = 0
        self._height = 0
        return

    @uniprof.regionDecorator(label=b'offline.splash_screen', scope=b'enter')
    def onLoad(self):
        self.active(True)
        return

    @uniprof.regionDecorator(label=b'offline.splash_screen', scope=b'exit')
    def onDelete(self):
        self.close()
        return

    def onComplete(self):
        _logger.debug(b'Startup Video completed!')
        self._nextMovie()
        return

    def onError(self):
        _logger.debug(b'Startup Video error!')
        self._nextMovie()
        return

    def fadeOutComplete(self):
        game_loading_bindings.closeSplashScreen()
        return

    def setStageSize(self, width, height):
        if self._isDAAPIInited():
            return self.as_setSizeS(width, height)
        self._width = width
        self._height = height
        return

    def turnDAAPIon(self, setScript, movieClip):
        super(SplashScreen, self).turnDAAPIon(setScript, movieClip)
        self.as_setSizeS(self._width, self._height)
        return

    def tryToSkip(self):
        if self._canSkip:
            self._nextMovie()
        return

    def applicationVisibilityChanged(self):
        if self._videoStarted and not BigWorld.isWindowVisible():
            self._soundValue = 0.0
        else:
            self._soundValue = self._getVideoVolume()
        self._sendDataToFlash()
        return

    def _populate(self):
        super(SplashScreen, self)._populate()
        if self._movieFiles:
            files = [(b'/').join((SCALEFORM_SWF_PATH_V3, v)) for v in self._movieFiles]
            ScaleformFileLoader.enableStreaming(files)
            self._nextMovie()
        else:
            self._allVideosComplete()
        return

    def _destroy(self):
        ScaleformFileLoader.disableStreaming()
        self._userPrefs = None
        super(SplashScreen, self)._destroy()
        return

    def _nextMovie(self):
        if not self._movieFiles:
            self._allVideosComplete()
            return
        self._currentMovie = self._movieFiles.pop(0)
        settings = getCompulsoryVideoSettings(self._currentMovie)
        if settings:
            self._sendDataToFlash()
            self._canSkip = settings.canBeSkipped
        else:
            self._canSkip = True
            if versionChanged(self._userPrefs):
                self._sendDataToFlash()
                self._writeSetting = True
            else:
                _logger.debug(b'Startup Video skipped: %s', self._currentMovie)
                self._nextMovie()
        return

    def _sendDataToFlash(self):
        if not self._currentMovie:
            return
        _logger.debug(b'Startup Video: path = %s, sound volume = %d%%', self._currentMovie, self._soundValue * 100)
        self.as_playVideoS({b'source': (self._currentMovie), 
           b'bufferTime': (self._bufferTime), 
           b'volume': (self._soundValue)})
        self._videoStarted = True
        return

    def _allVideosComplete(self):
        if self._writeSetting:
            self._userPrefs.writeString(Settings.INTRO_VIDEO_VERSION, version_utils.getClientMainVersion(clientVersionGetter))
        self.as_fadeOutS(VIDEO_FADE_OUT_TIME)
        return

    def _getVideoVolume(self):
        ds = self._userPrefs[Settings.KEY_SOUND_PREFERENCES]
        if not ds:
            return MASTER_VOLUME_DEFAULT / 2
        return ds.readFloat(b'masterVolume', MASTER_VOLUME_DEFAULT) / 2


def createSplashScreen(preferences):
    if mustShowSplashScreen(preferences):
        return SplashScreen(preferences)
    else:
        return
