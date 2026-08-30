from debug_utils import LOG_DEBUG
from gui.sounds.sound_constants import IS_ADVANCED_LOGGING
if IS_ADVANCED_LOGGING:

    def SOUND_DEBUG(msg, *kargs):
        LOG_DEBUG(b'[SOUND]', msg, kargs)
        return


else:

    def SOUND_DEBUG(msg, *kargs):
        return
