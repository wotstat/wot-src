import WWISE
from gui.sounds.sound_systems import wwise_system, no_system
__all__ = (b'getCurrentSoundSystem',)

def getCurrentSoundSystem():
    if WWISE.enabled:
        return wwise_system.WWISESoundSystem()
    return no_system.NoSoundSystem()
