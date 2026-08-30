import SoundGroups
from armory_yard.gui.Scaleform.daapi.view.lobby.hangar.sound_constants import SOUNDS

def setSoundDroneMode(isPostProgression):
    if isPostProgression:
        SoundGroups.g_instance.setSwitch(SOUNDS.SOUND_DRONE_SWITCH_GROUP, SOUNDS.SOUND_DRONE_02)
    else:
        SoundGroups.g_instance.setSwitch(SOUNDS.SOUND_DRONE_SWITCH_GROUP, SOUNDS.SOUND_DRONE_01)
    return


class ArmorySoundManager(object):
    __slots__ = (b'__isFirstEntrance', b'__isEnabled')

    def __init__(self):
        self.__isFirstEntrance = True
        self.__isEnabled = False
        return

    def clear(self):
        self.__isFirstEntrance = True
        self.__isEnabled = False
        return

    def onSoundModeChanged(self, isArmorySoundMode):
        if isArmorySoundMode == self.__isEnabled:
            return
        if isArmorySoundMode:
            if self.__isFirstEntrance:
                self.__isFirstEntrance = False
                SoundGroups.g_instance.playSound2D(SOUNDS.FIRST_ENTER)
            else:
                SoundGroups.g_instance.playSound2D(SOUNDS.ENTER)
        else:
            SoundGroups.g_instance.playSound2D(SOUNDS.EXIT)
        self.__isEnabled = isArmorySoundMode
        return
