from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class Sounds(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'techtree'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_TECHTREE = b'STATE_hangar_place_research'
    AMBIENT = b'researches_ambience'
    MUSIC = b'researches_music'
    RESET = b'researches_music_reset'
    BLUEPRINT_VIEW_ON_SOUND_ID = b'gui_blueprint_view_switch_on'
    BLUEPRINT_VIEW_OFF_SOUND_ID = b'gui_blueprint_view_switch_off'
    BLUEPRINT_VIEW_PLUS_SOUND_ID = b'gui_blueprint_view_switch_on_plus'
    TOP_OF_THE_TREE_ANIMATION_ON_SOUND_ID = b'researches_top_of_the_tree_start'
    TOP_OF_THE_TREE_ANIMATION_OFF_SOUND_ID = b'researches_top_of_the_tree_stop'
    TOP_OF_THE_TREE_ANIMATION_STOP_ANIMATION = b'researches_top_of_the_tree_stop_animation'


TECHTREE_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.COMMON_SOUND_SPACE, entranceStates={(Sounds.STATE_PLACE): (Sounds.STATE_PLACE_TECHTREE)}, exitStates={}, persistentSounds=(
 Sounds.MUSIC, Sounds.AMBIENT), stoppableSounds=(), priorities=(), autoStart=True, exitEvent=Sounds.RESET)
