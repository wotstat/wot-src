import WWISE
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class MapsTrainingSound(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'Lobby_music_garage_maps_training'
    GAMEMODE_GROUP = b'STATE_gamemode'
    GAMEMODE_STATE = b'STATE_gamemode_maps_training'
    GAMEMODE_DEFAULT = b'STATE_gamemode_default'
    HANGAR_GROUP = b'STATE_hangar_place'
    HANGAR_STATE = b'STATE_hangar_place_garage'
    ENTER_EVENT = b'mt_mode_enter'
    EXIT_EVENT = b'mt_mode_exit'
    MAP_CHOICE_ENTER = b'mt_map_choice_enter'
    MAP_CHOICE_EXIT = b'mt_map_choice_exit'
    COMPLETE_ITEM = b'mt_anim_scenario_complete'

    @staticmethod
    def onSelectedMap(isSelected):
        if isSelected:
            WWISE.WW_eventGlobal(MapsTrainingSound.MAP_CHOICE_EXIT)
        else:
            WWISE.WW_eventGlobal(MapsTrainingSound.MAP_CHOICE_ENTER)
        return


MAPS_TRAINING_SOUND_SPACE = CommonSoundSpaceSettings(name=MapsTrainingSound.COMMON_SOUND_SPACE, entranceStates={(MapsTrainingSound.HANGAR_GROUP): (MapsTrainingSound.HANGAR_STATE)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=MapsTrainingSound.ENTER_EVENT, exitEvent=MapsTrainingSound.EXIT_EVENT)
