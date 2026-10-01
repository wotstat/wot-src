import SoundGroups
from debug_utils import LOG_ERROR
from gui.battle_control import avatar_getter

def playVoiceover(eventName):
    soundNotifications = avatar_getter.getSoundNotifications()
    if soundNotifications:
        soundNotifications.play(eventName)
    else:
        LOG_ERROR((b'[PortalBattle]: could not play voiceover event {}').format(eventName))
    return


def play2DSound(name):
    SoundGroups.g_instance.playSound2D(name)
    return


def play3DSound(name, point):
    SoundGroups.g_instance.playSoundPos(name, point)
    return
