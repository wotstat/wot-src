import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event

class IVoiceoverManager(IGameController):
    if typing.TYPE_CHECKING:
        onSubtitleShow = None
        onSubtitleHide = None
        onStarted = None
        onStopped = None

    @property
    def currentSubtitle(self):
        raise NotImplementedError
        return

    @property
    def currentCtx(self):
        raise NotImplementedError
        return

    @property
    def isPlaying(self):
        raise NotImplementedError
        return

    def stopVoiceover(self):
        raise NotImplementedError
        return

    def playVoiceover(self, voiceoverId, ctx=None):
        raise NotImplementedError
        return
