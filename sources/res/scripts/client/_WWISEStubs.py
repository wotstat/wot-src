from __future__ import absolute_import
import typing, Math

class Sound:

    def __init__(self, *args, **kwargs):
        raise TypeError(b'WWISE.Sound is abstract and cannot be directly instanced.')
        return


class SoundParameter:

    def __init__(self, *args, **kwargs):
        raise TypeError(b'WWISE.SoundParameter is abstract and cannot be directly instanced.')
        return


class EventCategory:

    def __init__(self, name):
        self.muted = False
        self.paused = False
        self.volume = 0.0
        self.pitch = 0.0
        return

    def stopAllEvents(self):
        return


class EventGroup:

    def __init__(self, name):
        self.memoryUsed = 0
        self.isPlaying = False
        self.isLoaded = False
        return

    def loadEventData(self, arg=False):
        return

    def freeEventData(self, arg=False):
        return


class EventProject:

    def __init__(self, *args, **kwargs):
        self.memoryUsed = 0
        return

    def stopAllEvents(self, arg=False):
        return

    def release(self):
        return


class EventReverb:

    def __init__(self, name):
        self.active = False
        self.position = Math.Vector3(0, 0, 0)
        self.minDistance = 0.0
        self.maxDistance = 0.0
        return


class MusicSystem:

    def __init__(self):
        self.memoryUsed = 0
        self.muted = False
        self.paused = False
        self.volume = 0.0
        return

    def promptCue(self, name):
        return

    def setParameterValue(self, name, value):
        return

    def getParameterValue(self, name):
        return 0.0

    def setCallback(self, fn):
        return

    def reset(self, type, cb):
        return

    def loadSoundData(self, blocking):
        return


def getMusicSystem():
    return MusicSystem()


def getSound(*args, **kwargs):
    return


def playSound(*args, **kwargs):
    return


def getSoundBanks(*args, **kwargs):
    return []


def loadSoundBankIntoMemory(*args, **kwargs):
    return


def unloadSoundBankFromMemory(*args, **kwargs):
    return


def setDefaultSoundProject(*args, **kwargs):
    return


def loadEventProject(*args, **kwargs):
    return


def reloadEventProject(*args, **kwargs):
    return


def unloadEventProject(*args, **kwargs):
    return


def loadSoundGroup(*args, **kwargs):
    return


def unloadSoundGroup(*args, **kwargs):
    return


def setMasterVolume(*args, **kwargs):
    return


def getFxSoundDuration(*args, **kwargs):
    return 0.0


def registerEventReverb(*args, **kwargs):
    return


def getEventReverb(*args, **kwargs):
    return


def LSloadEventsDB(*args, **kwargs):
    return


def WG_loadCommon(*args, **kwargs):
    return


def WW_setRTCPGlobal(name, value, **kwargs):
    return


def WW_setRTPCBus(*args, **kwargs):
    return


def setLanguage(*args, **kwargs):
    return


def WG_loadBanks(*args, **kwargs):
    return


def WG_loadLogin(*args, **kwargs):
    return


def WG_isMSR(*args, **kwargs):
    return False


def WW_setVolumeThreshold(*args, **kwargs):
    return


def WW_setSoundSystem(*args, **kwargs):
    return
