from gui.sounds.sound_constants import SoundSystems, SPEAKERS_CONFIG

class SoundSystemAbstract(object):

    def getID(self):
        raise NotImplementedError
        return

    def init(self):
        return

    def fini(self):
        return

    def isMSR(self):
        return False

    def enableDynamicPreset(self):
        return

    def disableDynamicPreset(self):
        return

    def setSoundSystem(self, value):
        return

    def setBassBoost(self, isEnabled):
        return

    def getSystemSpeakersPresetID(self):
        return SPEAKERS_CONFIG.AUTO_DETECTION

    def getUserSpeakersPresetID(self):
        return SPEAKERS_CONFIG.AUTO_DETECTION

    def setUserSpeakersPresetID(self, presetID):
        return

    def sendGlobalEvent(self, eventName, **params):
        return

    def onEnvStart(self, environment):
        return

    def onEnvStop(self, environment):
        return

    def __repr__(self):
        return b'SoundSystem(%s)' % SoundSystems.getUserName(self.getID())
