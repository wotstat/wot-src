import logging
from functools import wraps
import typing, BigWorld
from adisp import isAsync
from frameworks.wulf import Window, View, WindowSettings, ViewSettings, WindowFlags, WindowStatus
from gui.impl.gen import R
from gui.impl.gen.view_models.views.fading_cover_view_model import FadingCoverViewModel
from gui.impl.gen_utils import DynAccessor
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.impl import IGuiLoader
from th_async import th_async, th_await, await_callback, AsyncSemaphore, BrokenPromiseError
if typing.TYPE_CHECKING:
    from typing import Callable, Optional, Union
_logger = logging.getLogger(__name__)
FADE_IN_DURATION = 0.15
FADE_OUT_DURATION = 0.4
BRING_TO_FRONT_FRAMES_COUNT = 2

class ICover(object):
    __slots__ = ()

    def fadeOut(self, onComplete):
        raise NotImplementedError
        return

    def fadeIn(self, onComplete):
        raise NotImplementedError
        return


class DefaultFadingCover(View, ICover):
    __slots__ = (b'_onComplete',)

    def __init__(self, background=None, fadeInDuration=FADE_IN_DURATION, fadeOutDuration=FADE_OUT_DURATION):
        model = FadingCoverViewModel()
        settings = ViewSettings(layoutID=R.views.common.FadingCoverView(), model=model)
        super(DefaultFadingCover, self).__init__(settings)
        self._onComplete = None
        model.setFadeInDuration(fadeInDuration)
        model.setFadeOutDuration(fadeOutDuration)
        if background:
            bgRes = background() if isinstance(background, DynAccessor) else background
            model.setBackground(bgRes)
        return

    @property
    def viewModel(self):
        return super(DefaultFadingCover, self).getViewModel()

    def fadeOut(self, onComplete):
        if self.viewModel.getIsVisible():
            onComplete()
        else:
            self._onComplete = onComplete
            self.viewModel.setIsVisible(True)
        return

    def fadeIn(self, onComplete):
        if not self.viewModel.getIsVisible():
            onComplete()
        else:
            self._onComplete = onComplete
            self.viewModel.setIsVisible(False)
        return

    def _onLoading(self, *args, **kwargs):
        super(DefaultFadingCover, self)._onLoading(*args, **kwargs)
        self.viewModel.onFadingInComplete += self._fadingCompleteHandler
        self.viewModel.onFadingOutComplete += self._fadingCompleteHandler
        return

    def _finalize(self):
        self.viewModel.onFadingInComplete -= self._fadingCompleteHandler
        self.viewModel.onFadingOutComplete -= self._fadingCompleteHandler
        self._onComplete = None
        super(DefaultFadingCover, self)._finalize()
        return

    def _fadingCompleteHandler(self):
        if callable(self._onComplete):
            cb = self._onComplete
            self._onComplete = None
            cb()
        return


class FadingCoverWindow(Window):
    __slots__ = ()

    def __init__(self, content, layer):
        settings = WindowSettings()
        settings.flags = WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN
        settings.layer = layer
        settings.content = content
        super(FadingCoverWindow, self).__init__(settings)
        return

    @property
    def _cover(self):
        return super(FadingCoverWindow, self).content

    def fadeOut(self, callback):
        self.load()
        self._cover.fadeOut(callback)
        return

    def fadeIn(self, callback):
        self._cover.fadeIn(callback)
        return


class FadeManager(object):
    __slots__ = (b'_layer', b'_coverFactory', b'_currentWindow', b'_isDestroyed', b'_semaphore')
    _gui = dependency.descriptor(IGuiLoader)
    _appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, layer, coverFactory=None):
        super(FadeManager, self).__init__()
        self._layer = layer
        self._coverFactory = coverFactory
        self._currentWindow = None
        self._isDestroyed = False
        self._semaphore = AsyncSemaphore()
        return

    def __enter__(self):
        return self

    def __exit__(self, exceptionType, exceptionValue, exceptionTraceBack):
        self.destroy()
        return

    def destroy(self):
        self._gui.windowsManager.onWindowStatusChanged -= self._windowStatusChanged
        if self._currentWindow:
            self._currentWindow.destroy()
            self._currentWindow = None
        self._coverFactory = None
        self._isDestroyed = True
        self._semaphore.destroy()
        return

    @property
    def isAnimating(self):
        return self._currentWindow is not None

    @th_async
    def show(self):
        yield self._transit(self._doShow)
        return

    @th_async
    def hide(self):
        yield self._transit(self._doHide)
        return

    def hideImmediately(self):
        self._gui.windowsManager.onWindowStatusChanged -= self._windowStatusChanged
        if self._currentWindow:
            self._currentWindow.destroy()
            self._currentWindow = None
        return

    @th_async
    def _doShow(self):
        if self._isDestroyed:
            return
        container = self._appLoader.getApp().containerManager.getContainer(self._layer)
        if not container:
            return
        if self._currentWindow:
            return
        cover = self._coverFactory() if self._coverFactory else DefaultFadingCover()
        self._currentWindow = FadingCoverWindow(content=cover, layer=self._layer)
        self._gui.windowsManager.onWindowStatusChanged += self._windowStatusChanged
        yield await_callback(self._currentWindow.fadeOut)()
        return

    @th_async
    def _doHide(self):
        if self._isDestroyed:
            return
        container = self._appLoader.getApp().containerManager.getContainer(self._layer)
        if not container or not self._currentWindow:
            return
        yield await_callback(self._currentWindow.fadeIn)()
        self.hideImmediately()
        return

    @th_async
    def _transit(self, transition):
        yield self._semaphore.acquire()
        try:
            try:
                yield transition()
            except BrokenPromiseError:
                _logger.debug(b'%s, got BrokenPromiseError during the fade-in/fade-out animation.', transition)

        finally:
            self._semaphore.release()

        return

    def _windowStatusChanged(self, uniqueID, newStatus):
        if not self.isAnimating:
            return
        if newStatus == WindowStatus.LOADING:
            window = self._gui.windowsManager.getWindow(uniqueID)
            if window == self._currentWindow or window.layer != self._currentWindow.layer:
                return
            BigWorld.callback(0.0, (lambda : self._bringToFront(BRING_TO_FRONT_FRAMES_COUNT)))
        return

    def _bringToFront(self, framesLeft):
        if self._currentWindow:
            self._currentWindow.tryFocus()
            framesLeft -= 1
            if framesLeft > 0:
                BigWorld.callback(0.0, (lambda : self._bringToFront(framesLeft)))
        return


class useFade(object):

    def __init__(self, layer, coverFactory, *args, **kwargs):
        super(useFade, self).__init__()
        self._layer = layer
        self._coverFactory = coverFactory
        self._args = args
        self._kwargs = kwargs
        return

    def __call__(self, func):

        @wraps(func)
        @th_async
        def wrapper(*args, **kwargs):
            with FadeManager(self._layer, self._createCover) as fadeManager:
                yield th_await(fadeManager.show())
                result = func(*args, **kwargs)
                if isAsync(func):
                    yield await_callback(result)(*args, **kwargs)
                yield th_await(fadeManager.hide())
            return

        return wrapper

    def _createCover(self):
        return self._coverFactory(*self._args, **self._kwargs)


class useDefaultFade(useFade):

    def __init__(self, layer, background=None, fadeInDuration=FADE_IN_DURATION, fadeOutDuration=FADE_OUT_DURATION):
        super(useDefaultFade, self).__init__(layer, DefaultFadingCover, background=background, fadeInDuration=fadeInDuration, fadeOutDuration=fadeOutDuration)
        return
