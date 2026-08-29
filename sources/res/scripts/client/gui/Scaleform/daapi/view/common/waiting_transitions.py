import logging, SCALEFORM
from gui.Scaleform.daapi.view.external_components import ExternalFlashComponent
from gui.Scaleform.daapi.view.external_components import ExternalFlashSettings
from gui.Scaleform.daapi.view.meta.WaitingTransitionMeta import WaitingTransitionMeta
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.app_loader import IWaitingWidget
_logger = logging.getLogger(__name__)
_DEFAULT_MOVIE_BACKGROUND_ALPHA = 0.6

class TransitionMode(object):
    DISABLED = 0
    ENABLED = 1
    TRIGGER = 2
    SHOW_BACKGROUND = 4
    PERMANENT_MESSAGE = 8


class WaitingTransition(ExternalFlashComponent, WaitingTransitionMeta, IWaitingWidget):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(WaitingTransition, self).__init__(ExternalFlashSettings(b'transition', b'waitingTransitionsApp.swf', b'root.main', ROOT_SWF_CONSTANTS.WAITING_TRANSITION_CALLBACK))
        self.__textID = R.invalid()
        self.__mode = TransitionMode.DISABLED
        self.createExternalComponent()
        self.isEnabled = False
        self.movie.scaleMode = SCALEFORM.eMovieScaleMode.NO_SCALE
        self.movie.backgroundAlpha = _DEFAULT_MOVIE_BACKGROUND_ALPHA
        return

    def isInTransitionMode(self):
        return self.__mode != TransitionMode.DISABLED

    def setTransitionMode(self, mode):
        self.__mode = mode
        if self.__mode == TransitionMode.DISABLED:
            self.__textID = R.invalid()
        if self._isDAAPIInited():
            self.__setupBackground()
        return

    def showWaiting(self, messageID, _=False):
        self.active(True)
        if self.__mode & TransitionMode.PERMANENT_MESSAGE > 0 and self.__textID:
            return
        self.__textID = messageID
        if self._isDAAPIInited():
            self.as_setTransitionTextS(backport.text(self.__textID))
        return

    def hideWaiting(self):
        if self.__mode & TransitionMode.TRIGGER > 0:
            self.__mode = TransitionMode.DISABLED
            self.__textID = R.invalid()
        self.active(False)
        self.movie.backgroundAlpha = _DEFAULT_MOVIE_BACKGROUND_ALPHA
        return

    def afterCreate(self):
        super(WaitingTransition, self).afterCreate()
        self.addListener(GameEvent.CHANGE_APP_RESOLUTION, self.__onAppResolutionChanged, scope=EVENT_BUS_SCOPE.GLOBAL)
        if self.__textID:
            self.as_setTransitionTextS(backport.text(self.__textID))
        self.__setupBackground()
        return

    def beforeDelete(self):
        self.removeListener(GameEvent.CHANGE_APP_RESOLUTION, self.__onAppResolutionChanged, scope=EVENT_BUS_SCOPE.GLOBAL)
        super(WaitingTransition, self).beforeDelete()
        return

    def __setupBackground(self):
        if self.__mode & TransitionMode.SHOW_BACKGROUND > 0:
            self.movie.backgroundAlpha = 0.0
            self.as_showBGS()
        else:
            self.movie.backgroundAlpha = _DEFAULT_MOVIE_BACKGROUND_ALPHA
            self.as_hideBGS()
        return

    def __onAppResolutionChanged(self, event):
        ctx = event.ctx
        if b'width' not in ctx:
            _logger.error(b'Application width is not found: %r', ctx)
            return
        if b'height' not in ctx:
            _logger.error(b'Application height is not found: %r', ctx)
            return
        if b'scale' not in ctx:
            _logger.error(b'Application scale is not found: %r', ctx)
            return
        self.as_updateStageS(ctx[b'width'], ctx[b'height'], ctx[b'scale'])
        return
