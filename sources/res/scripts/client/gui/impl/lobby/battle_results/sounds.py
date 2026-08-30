from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class RandomBattleResultsSounds(CONST_CONTAINER):
    BATTLE_RESULTS_SPACE_NAME = b'postbattle_view'
    GAMEPLACE_STATE = b'STATE_gameplace'
    GAMEPLACE_BATTLE_RESULTS_STATE = b'STATE_gameplace_result'
    GAMEPLACE_HANGAR_STATE = b'STATE_gameplace_hangar'
    OVERLAY_HANGAR_FILTERED = b'STATE_hangar_filtered'
    OVERLAY_HANGAR_FILTERED_ON = b'STATE_hangar_filtered_on'
    OVERLAY_HANGAR_FILTERED_OFF = b'STATE_hangar_filtered_off'


RANDOM_BATTLE_RESULTS_SOUND_SPACE = CommonSoundSpaceSettings(name=RandomBattleResultsSounds.BATTLE_RESULTS_SPACE_NAME, entranceStates={(RandomBattleResultsSounds.GAMEPLACE_STATE): (RandomBattleResultsSounds.GAMEPLACE_BATTLE_RESULTS_STATE), 
   (RandomBattleResultsSounds.OVERLAY_HANGAR_FILTERED): (RandomBattleResultsSounds.OVERLAY_HANGAR_FILTERED_ON)}, exitStates={(RandomBattleResultsSounds.GAMEPLACE_STATE): (RandomBattleResultsSounds.GAMEPLACE_HANGAR_STATE), 
   (RandomBattleResultsSounds.OVERLAY_HANGAR_FILTERED): (RandomBattleResultsSounds.OVERLAY_HANGAR_FILTERED_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
