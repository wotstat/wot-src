import math, ResMgr
from items import _xml
from items.components import sound_components
from items.writers import shared_writers

def writeWWTripleSoundConfig(soundConfig, section):
    _xml.rewriteString(section, b'wwsound', soundConfig.wwsound, defaultValue=b'')
    _xml.rewriteString(section, b'wwsoundPC', soundConfig.wwsoundPC, defaultValue=b'')
    _xml.rewriteString(section, b'wwsoundNPC', soundConfig.wwsoundNPC, defaultValue=b'')
    return


def writeHullAimingSound(hullAimingSound, section, cache):
    if hullAimingSound is None:
        return _xml.deleteAndCleanup(section, b'hullAiming/audio')
    else:
        changed = False
        audioKey = b'hullAiming/audio/'
        changed |= shared_writers.writeLodDist(hullAimingSound.lodDist, section, audioKey + b'lodDist', cache)
        changed |= _xml.rewriteFloat(section, audioKey + b'angleLimitValue', math.degrees(hullAimingSound.angleLimitValue))
        soundsKey = audioKey + b'sounds/'
        soundsDS = _xml.ListRewriter(section, soundsKey + b'*')
        for sound in hullAimingSound.sounds:
            soundDS = soundsDS.next(preferredPredicate=(lambda ds, snd=sound: ds.name == snd.state), path=soundsKey + sound.state)
            changed |= _xml.rewriteString(soundDS, b'underLimitSounds/wwsoundPC', sound.underLimitSounds.PC)
            changed |= _xml.rewriteString(soundDS, b'underLimitSounds/wwsoundNPC', sound.underLimitSounds.NPC)
            changed |= _xml.rewriteString(soundDS, b'overLimitSounds/wwsoundPC', sound.overLimitSounds.PC)
            changed |= _xml.rewriteString(soundDS, b'overLimitSounds/wwsoundNPC', sound.overLimitSounds.NPC)

        changed |= soundsDS.flush()
        return changed
