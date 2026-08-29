import math, typing, ResMgr
from constants import IS_DEVELOPMENT
from debug_utils import LOG_DEBUG
from items import _xml
from items.components import component_constants
from items.components import sound_components
from items.readers import shared_readers
from soft_exception import SoftException

def readWWTripleSoundConfig(section):
    if IS_DEVELOPMENT:
        for name in (b'sound', b'soundPC', b'soundNPC'):
            if section.has_key(name):
                raise SoftException((b'Section "[hull|engine]/{}" is no longer supported').format(name))

    return sound_components.WWTripleSoundConfig(intern(section.readString(b'wwsound', component_constants.EMPTY_STRING)), intern(section.readString(b'wwsoundPC', component_constants.EMPTY_STRING)), intern(section.readString(b'wwsoundNPC', component_constants.EMPTY_STRING)))


def readHullAimingSound(xmlCtx, section, cache):
    if section[b'hullAiming'] is None:
        return
    else:
        try:
            lodDist = shared_readers.readLodDist(xmlCtx, section, b'hullAiming/audio/lodDist', cache)
            angleLimit = math.radians(_xml.readFloat(xmlCtx, section, b'hullAiming/audio/angleLimitValue', component_constants.ZERO_FLOAT))
            sounds = []
            for actionName, actionSection in _xml.getChildren(xmlCtx, section, b'hullAiming/audio/sounds'):
                ctx = (
                 xmlCtx, b'hullAiming/audio/sounds')
                underLimitSounds = sound_components.SoundPair(PC=intern(_xml.readNonEmptyString(ctx, actionSection, b'underLimitSounds/wwsoundPC')), NPC=intern(_xml.readNonEmptyString(ctx, actionSection, b'underLimitSounds/wwsoundNPC')))
                overLimitSounds = sound_components.SoundPair(PC=intern(_xml.readNonEmptyString(ctx, actionSection, b'overLimitSounds/wwsoundPC')), NPC=intern(_xml.readNonEmptyString(ctx, actionSection, b'overLimitSounds/wwsoundNPC')))
                sound = sound_components.StatedSounds(state=actionName, underLimitSounds=underLimitSounds, overLimitSounds=overLimitSounds)
                sounds.append(sound)

            hullAimingSound = sound_components.HullAimingSound(lodDist=lodDist, angleLimitValue=_xml.cachedFloat(angleLimit), sounds=sounds)
            return hullAimingSound
        except:
            LOG_DEBUG(b'Incorrect hullAiming/audio section')
            return

        return


def readSoundSiegeModeStateChange(xmlCtx, section):
    pcOn = _xml.readStringOrEmpty(xmlCtx, section, b'soundStateChange/on')
    pcOff = _xml.readStringOrEmpty(xmlCtx, section, b'soundStateChange/off')
    npcOn = _xml.readStringOrEmpty(xmlCtx, section, b'soundStateChange/npcOn')
    npcOff = _xml.readStringOrEmpty(xmlCtx, section, b'soundStateChange/npcOff')
    return sound_components.SoundSiegeModeStateChange(on=pcOn, off=pcOff, npcOn=npcOn, npcOff=npcOff, isEngine=_xml.readBool(xmlCtx, section, b'soundStateChange/isEngine', False))
