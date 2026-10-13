import WWISE, SoundGroups
from gui.SystemMessages import pushMessage, SM_TYPE
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
MIN_SOUND_SYSTEM_MIXER_VALUE = 10
RECOMMENDED_SOUND_SYSTEM_MIXER_VALUE = 100

class SystemMixerVolumeCtrl(object):
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self):
        self.__appMixerVolume = 100
        self.__invAppMixerVolume = True
        return

    def init(self):
        self.connectionMgr.onConnected += self.__onConnected
        return

    def fini(self):
        self.connectionMgr.onConnected -= self.__onConnected
        return

    def isSystemMixerVolumeDisabled(self):
        if self.__invAppMixerVolume:
            self.__appMixerVolume = round(WWISE.WW_getAppMixerVolume() * 100)
            self.__invAppMixerVolume = False
        return self.__appMixerVolume <= MIN_SOUND_SYSTEM_MIXER_VALUE

    def fixSystemMixerVolume(self):
        WWISE.WW_setAppMixerVolume(RECOMMENDED_SOUND_SYSTEM_MIXER_VALUE)
        self.__invAppMixerVolume = True
        return

    def markNeedInvAppMixerVolume(self):
        self.__invAppMixerVolume = True
        return

    def __onConnected(self):
        self.__invAppMixerVolume = True
        self.__checkSoundSystemOffStatus()
        return

    def __checkSoundSystemOffStatus(self):
        if self.isSystemMixerVolumeDisabled() and SoundGroups.g_instance.getMasterVolume() > 0:
            pushMessage(b'', SM_TYPE.SystemMixerVolumeDisabled, None, None)
        return
