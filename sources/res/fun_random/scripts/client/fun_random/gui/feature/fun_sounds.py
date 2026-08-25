from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class FunSounds(CONST_CONTAINER):
    HANGAR_PLACE_STATE = b'STATE_hangar_place'
    HANGAR_PLACE_TASKS = b'STATE_hangar_place_fep'
    OVERLAY_HANGAR_STATE = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_STATE_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_STATE_OFF = b'STATE_overlay_hangar_general_off'
    PROGRESSION_SPACE_NAME = b'fun_progression_view'
    PROGRESSION_ENTER_EVENT = b'ev_fep_meta_enter'
    PROGRESSION_EXIT_EVENT = b'ev_fep_meta_exit'
    REWARDS_SPACE_NAME = b'fun_rewards_view'
    REWARDS_SCREEN_GENERAL = b'gui_reward_screen_general'
    TIER_LIST_SPACE_NAME = b'fun_tier_list'
    TIER_LIST_ENTER = b'ev_fep_infopage_enter'
    TIER_LIST_EXIT = b'ev_fep_infopage_exit'
    BATTLE_RESULTS_SPACE_NAME = b'fun_postbattle_view'
    GAMEPLACE_STATE = b'STATE_gameplace'
    GAMEPLACE_BATTLE_RESULTS_STATE = b'STATE_gameplace_result'
    GAMEPLACE_HANGAR_STATE = b'STATE_gameplace_hangar'
    BATTLE_RESULTS_ENTER_EVENT = b'gui_hangar_neutral_screen'


FUN_PROGRESSION_SOUND_SPACE = CommonSoundSpaceSettings(name=FunSounds.PROGRESSION_SPACE_NAME, entranceStates={(FunSounds.HANGAR_PLACE_STATE): (FunSounds.HANGAR_PLACE_TASKS)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=FunSounds.PROGRESSION_ENTER_EVENT, exitEvent=FunSounds.PROGRESSION_EXIT_EVENT)
FUN_REWARD_SCREEN_SOUND_SPACE = CommonSoundSpaceSettings(name=FunSounds.REWARDS_SPACE_NAME, entranceStates={(FunSounds.OVERLAY_HANGAR_STATE): (FunSounds.OVERLAY_HANGAR_STATE_ON)}, exitStates={(FunSounds.OVERLAY_HANGAR_STATE): (FunSounds.OVERLAY_HANGAR_STATE_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=FunSounds.REWARDS_SCREEN_GENERAL, exitEvent=b'')
FUN_TIER_LIST_SOUND_SPACE = CommonSoundSpaceSettings(name=FunSounds.TIER_LIST_SPACE_NAME, entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=FunSounds.TIER_LIST_ENTER, exitEvent=FunSounds.TIER_LIST_EXIT)
FUN_BATTLE_RESULTS_SOUND_SPACE = CommonSoundSpaceSettings(name=FunSounds.BATTLE_RESULTS_SPACE_NAME, entranceStates={(FunSounds.GAMEPLACE_STATE): (FunSounds.GAMEPLACE_BATTLE_RESULTS_STATE)}, exitStates={(FunSounds.GAMEPLACE_STATE): (FunSounds.GAMEPLACE_HANGAR_STATE)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=FunSounds.BATTLE_RESULTS_ENTER_EVENT, exitEvent=b'')
