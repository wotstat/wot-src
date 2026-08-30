import SoundGroups

class AimSound(object):
    TARGET_UNLOCKED = 0
    TARGET_LOCKED = 1
    TARGET_LOST = 2
    aimSounds = (
     (b'ui_target_unlocked', b'target_unlocked'),
     (b'ui_target_locked', b'target_captured'),
     (b'ui_target_lost', b'target_lost'))

    @staticmethod
    def play(state, playerNotifications=None):
        sounds = AimSound.aimSounds[state]
        SoundGroups.g_instance.playSound2D(sounds[0])
        if playerNotifications is not None:
            playerNotifications.play(sounds[1])
        return
