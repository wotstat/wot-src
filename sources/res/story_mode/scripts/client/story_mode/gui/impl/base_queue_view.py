import BigWorld
from PlayerEvents import g_playerEvents
from helpers import dependency
from gui.impl.pub import ViewImpl
from shared_utils import safeCancelCallback
from story_mode.skeletons.story_mode_controller import IStoryModeController

class BaseWaitQueueView(ViewImpl):
    __slots__ = (b'_timerCallback',)
    storyModeCtrl = dependency.descriptor(IStoryModeController)

    def __init__(self, *args, **kwargs):
        super(BaseWaitQueueView, self).__init__(*args, **kwargs)
        self._timerCallback = None
        return

    def startWaitQueue(self):
        if self._timerCallback is None:
            self._timerCallback = BigWorld.callback(self.storyModeCtrl.settings.waitTimeQueue, self._onWaitQueueTimeout)
        return

    def _onLoading(self, *args, **kwargs):
        super(BaseWaitQueueView, self)._onLoading(*args, **kwargs)
        g_playerEvents.onArenaCreated += self._onArenaCreated
        return

    def _finalize(self):
        self._stopTimer()
        g_playerEvents.onArenaCreated -= self._onArenaCreated
        super(BaseWaitQueueView, self)._finalize()
        return

    def _onArenaCreated(self):
        self._stopTimer()
        return

    def _stopTimer(self):
        if self._timerCallback is not None:
            safeCancelCallback(self._timerCallback)
            self._timerCallback = None
        return

    def _onWaitQueueTimeout(self):
        self._timerCallback = None
        return
