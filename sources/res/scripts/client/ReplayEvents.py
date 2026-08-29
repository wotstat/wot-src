import Event

class _ReplayEvents(object):

    @property
    def isPlaying(self):
        return self.__isPlaying

    @property
    def isRecording(self):
        return self.__isRecording

    def __init__(self):
        self.onTimeWarpStart = Event.Event()
        self.onTimeWarpFinish = Event.Event()
        self.onPause = Event.Event()
        self.onMuteSound = Event.Event()
        self.onWatcherNotify = Event.Event()
        self.onReplayTerminated = Event.Event()
        self.__isPlaying = False
        self.__isRecording = False
        return

    def onRecording(self):
        self.__isRecording = True
        return

    def onPlaying(self):
        self.__isPlaying = True
        return


g_replayEvents = _ReplayEvents()
