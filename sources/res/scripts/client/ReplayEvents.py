from __future__ import absolute_import
import Event

class _ReplayEvents(object):

    @property
    def isPlaying(self):
        return self.__isPlaying

    @property
    def isRecording(self):
        return self.__isRecording

    @property
    def isTimeWarp(self):
        return self.__isTimeWarp

    @property
    def isLastWarpRewind(self):
        return self.__isLastWarpRewind

    def __init__(self):
        self.onTimeWarpStart = Event.Event()
        self.onTimeWarpFinish = Event.Event()
        self.onPause = Event.Event()
        self.onMuteSound = Event.Event()
        self.onPlaybackSpeedChanged = Event.Event()
        self.onWatcherNotify = Event.Event()
        self.onReplayTerminated = Event.Event()
        self.__isPlaying = False
        self.__isRecording = False
        self.__isTimeWarp = False
        self.__isLastWarpRewind = False
        return

    def onRecording(self):
        self.__isRecording = True
        return

    def onPlaying(self):
        self.__isPlaying = True
        return

    def callOnTimeWarpStart(self, isRewind):
        self.__isTimeWarp = True
        self.__isLastWarpRewind = isRewind
        self.onTimeWarpStart()
        return

    def callOnTimeWarpFinish(self):
        self.onTimeWarpFinish()
        self.__isTimeWarp = False
        return


g_replayEvents = _ReplayEvents()
