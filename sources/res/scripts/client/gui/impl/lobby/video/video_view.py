import logging, Windowing, BigWorld
from PlayerEvents import g_playerEvents
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.video.video_view_model import VideoViewModel
from gui.impl.lobby.video.video_sound_manager import DummySoundManager
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.Scaleform.Waiting import Waiting
from gui.sounds.filters import switchVideoOverlaySoundFilter
from helpers import getClientLanguage, dependency
from shared_utils import CONST_CONTAINER
from skeletons.gui.app_loader import IAppLoader
_logger = logging.getLogger(__name__)

class _SubtitlesLanguages(CONST_CONTAINER):
    CS = 1
    DE = 2
    EN = 3
    ES = 4
    FR = 5
    ITA = 6
    JA = 7
    KO = 8
    LATAM = 9
    PL = 10
    ptBR = 11
    ZHSG = 12
    TH = 13
    TR = 14
    ZHTW = 15


_SUBTITLE_TO_LOCALES_MAP = {(_SubtitlesLanguages.CS): {
                            b'cs'}, 
   (_SubtitlesLanguages.DE): {
                            b'de'}, 
   (_SubtitlesLanguages.EN): {
                            18, 
                            19, 20, 21, 22, 23, 
                            24, 25, 26, 27, 28, 
                            29, 30, 31, 32, 33, 
                            34, 35}, 
   (_SubtitlesLanguages.ES): {
                            b'es'}, 
   (_SubtitlesLanguages.FR): {
                            b'fr'}, 
   (_SubtitlesLanguages.ITA): {
                             b'it'}, 
   (_SubtitlesLanguages.JA): {
                            b'ja'}, 
   (_SubtitlesLanguages.KO): {
                            b'ko'}, 
   (_SubtitlesLanguages.LATAM): {
                               b'es_ar'}, 
   (_SubtitlesLanguages.PL): {
                            b'pl'}, 
   (_SubtitlesLanguages.ptBR): {
                              b'pt_br'}, 
   (_SubtitlesLanguages.TH): {
                            b'th'}, 
   (_SubtitlesLanguages.TR): {
                            b'tr'}, 
   (_SubtitlesLanguages.ZHTW): {
                              b'zh_tw'}, 
   (_SubtitlesLanguages.ZHSG): {
                              b'zh_sg', b'zh_cn'}}
_LOCALE_TO_SUBTITLE_MAP = {loc: subID for loc in _SUBTITLE_TO_LOCALES_MAP.iteritems()}
_LAYERS = [
 WindowLayer.OVERLAY, WindowLayer.CURSOR, WindowLayer.WAITING, WindowLayer.SERVICE_LAYOUT]

class VideoView(ViewImpl):
    __slots__ = (b'__onVideoStartedHandle', b'__onVideoStoppedHandle', b'__onVideoClosedHandle', b'__isAutoClose', b'__soundControl', b'__previouslyVisibleLayers', b'__app', b'__videoSource', b'__isUiVisible')
    __appFactory = dependency.descriptor(IAppLoader)

    def __init__(self, viewId, *args, **kwargs):
        settings = ViewSettings(viewId or R.views.lobby.video_view.GfVideoView())
        settings.model = VideoViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(VideoView, self).__init__(settings)
        self.__onVideoStartedHandle = kwargs.get(b'onVideoStarted')
        self.__onVideoStoppedHandle = kwargs.get(b'onVideoStopped')
        self.__onVideoClosedHandle = kwargs.get(b'onVideoClosed')
        self.__isAutoClose = kwargs.get(b'isAutoClose')
        self.__isUiVisible = kwargs.get(b'isUiVisible')
        self.__soundControl = kwargs.get(b'soundControl') or DummySoundManager()
        self.__previouslyVisibleLayers = []
        self.__app = self.__appFactory.getApp()
        self.__videoSource = kwargs.get(b'videoSource')
        return

    @property
    def viewModel(self):
        return super(VideoView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(VideoView, self)._onLoading(*args, **kwargs)
        if self.__videoSource is None:
            _logger.error(b'__videoSource is not specified!')
        else:
            self.viewModel.setVideoSource(self.__videoSource)
            self.viewModel.setIsUIVisible(bool(self.__isUiVisible))
            language = getClientLanguage()
            self.viewModel.setSubtitleTrack(_LOCALE_TO_SUBTITLE_MAP.get(language, 0))
            self.viewModel.setIsWindowAccessible(Windowing.isWindowAccessible())
            g_playerEvents.onAccountBecomeNonPlayer += self.__removeClosedHandle
            Windowing.addWindowAccessibilitynHandler(self.__onWindowAccessibilityChanged)
            switchVideoOverlaySoundFilter(on=True)
        return

    def _onLoaded(self, *args, **kwargs):
        Waiting.suspend(id(self))
        return

    def _initialize(self, *args, **kwargs):
        super(VideoView, self)._initialize(*args, **kwargs)
        self.__hideBack()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onCloseBtnClick, self.__onCloseWindow),
         (
          self.viewModel.onVideoStarted, self.__onVideoStarted),
         (
          self.viewModel.onVideoStopped, self.__onVideoStopped),
         (
          self.viewModel.onLoadError, self.__onLoadError))

    def _finalize(self):
        Waiting.resume(id(self))
        self.__showBack()
        g_playerEvents.onAccountBecomeNonPlayer -= self.__removeClosedHandle
        Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        if self.__onVideoClosedHandle is not None:
            self.__onVideoClosedHandle()
            self.__onVideoClosedHandle = None
        self.__soundControl.stop()
        self.__soundControl = DummySoundManager()
        self.__app = None
        self.__previouslyVisibleLayers = None
        switchVideoOverlaySoundFilter(on=False)
        return

    def __onCloseWindow(self, _=None):
        self.destroyWindow()
        return

    def __removeClosedHandle(self):
        self.__onVideoClosedHandle = None
        return

    def __onVideoStarted(self, _=None):
        if self.__onVideoStartedHandle is not None:
            self.__onVideoStartedHandle()
            self.__onVideoStartedHandle = None
        self.__soundControl.start()
        if not self.viewModel.getIsWindowAccessible():
            self.__soundControl.pause()
        return

    def __onVideoStopped(self, _=None):
        if self.__onVideoStoppedHandle is not None:
            self.__onVideoStoppedHandle()
            self.__onVideoStoppedHandle = None
        self.__soundControl.stop()
        if self.__isAutoClose:
            self.destroyWindow()
        return

    def __onLoadError(self, _=None):
        self.__onVideoStopped()
        return

    def __onWindowAccessibilityChanged(self, isWindowAccessible):
        if isWindowAccessible:
            self.__soundControl.unpause()
        else:
            self.__soundControl.pause()
        self.viewModel.setIsWindowAccessible(isWindowAccessible)
        return

    def __hideBack(self):
        BigWorld.worldDrawEnabled(False)
        if self.__app is not None:
            containerManager = self.__app.containerManager
            self.__previouslyVisibleLayers = containerManager.getVisibleLayers()
            containerManager.setVisibleLayers(_LAYERS)
        return

    def __showBack(self):
        BigWorld.worldDrawEnabled(True)
        if self.__app is not None:
            self.__app.containerManager.setVisibleLayers(self.__previouslyVisibleLayers)
        return


class VideoViewWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, viewId=None, *args, **kwargs):
        super(VideoViewWindow, self).__init__(content=VideoView(viewId=viewId, *args, **kwargs), wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.OVERLAY, decorator=None)
        return
