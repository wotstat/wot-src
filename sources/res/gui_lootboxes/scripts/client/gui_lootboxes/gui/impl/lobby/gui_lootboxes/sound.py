from enum import Enum
import SoundGroups
from gui.sounds.filters import StatesGroup, States
from sound_gui_manager import CommonSoundSpaceSettings

class Sounds(Enum):
    STORAGE_SPACE_NAME = b'loot_box_storage'
    LOOT_BOX_ENTER = b'lootboxes_enter'
    LOOT_BOX_EXIT = b'lootboxes_exit'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_LOOTBOXES = b'STATE_hangar_place_lootboxes'
    STATE_HANGAR_PLACE = b'STATE_hangar_place_garage'
    OVERLAY_SPACE_NAME = b'loot_boxes_overlay'
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'
    INTRO_SPACE_NAME = b'loot_boxes_intro'
    LOOT_BOX_ENTER_FIRST = b'lootboxes_enter_first'
    VIDEO_REWARD_SPACE_NAME = b'lootbox_reward_video'
    CANCEL_SHORT_STATISTIC = b'researches_premium_panel_slide_out'


LOOT_BOXES_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.STORAGE_SPACE_NAME.value, entranceStates={(Sounds.STATE_PLACE.value): (Sounds.STATE_LOOTBOXES.value)}, exitStates={(Sounds.STATE_PLACE.value): (Sounds.STATE_HANGAR_PLACE.value)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=Sounds.LOOT_BOX_EXIT.value)
LOOT_BOXES_OVERLAY_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.OVERLAY_SPACE_NAME.value, entranceStates={(Sounds.OVERLAY_HANGAR_GENERAL.value): (Sounds.OVERLAY_HANGAR_GENERAL_ON.value)}, exitStates={(Sounds.OVERLAY_HANGAR_GENERAL.value): (Sounds.OVERLAY_HANGAR_GENERAL_OFF.value)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
LOOT_BOXES_REWARD_VIDEO_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.VIDEO_REWARD_SPACE_NAME, entranceStates={(StatesGroup.VIDEO_OVERLAY): (States.VIDEO_OVERLAY_ON)}, exitStates={(StatesGroup.VIDEO_OVERLAY): (States.VIDEO_OVERLAY_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')

def playEnterSound(isFirstEnter):
    soundName = Sounds.LOOT_BOX_ENTER_FIRST.value if isFirstEnter else Sounds.LOOT_BOX_ENTER.value
    SoundGroups.g_instance.playSound2D(soundName)
    return
