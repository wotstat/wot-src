from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class Sounds(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'techtree'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_TECHTREE = b'STATE_hangar_place_research'
    AMBIENT = b'researches_ambience'
    MUSIC = b'researches_music'
    RESET = b'researches_music_reset'


TECHTREE_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.COMMON_SOUND_SPACE, entranceStates={(Sounds.STATE_PLACE): (Sounds.STATE_PLACE_TECHTREE)}, exitStates={}, persistentSounds=(
 Sounds.MUSIC, Sounds.AMBIENT), stoppableSounds=(), priorities=(), autoStart=True, exitEvent=Sounds.RESET)
