from __future__ import absolute_import
from last_stand.gui.ls_gui_constants import DifficultyLevel
from gui.impl.lobby.hangar.base.sound_constants import HangarSoundStates
from gui.sounds.filters import States, StatesGroup
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings
from last_stand_common.last_stand_constants import ARENA_BONUS_TYPE
from last_stand.gui.sounds.voiceovers import Voiceover

class SoundLanguage(CONST_CONTAINER):
    RU_VOICEOVER_REALM_CODES = (b'RU', b'ST', b'QA', b'DEV', b'SB')
    VOICEOVER_LOCALIZATION_SWITCH = b'SWITCH_ext_ev_hw_vo'
    VOICEOVER_CN = b'SWITCH_ext_ev_hw_vo_CN'
    VOICEOVER_RU = b'SWITCH_ext_ev_hw_vo_RU'
    VOICEOVER_UA = b'SWITCH_ext_ev_hw_vo_UA'
    VOICEOVER_EN = b'SWITCH_ext_ev_hw_vo_EN'
    LANGUAGE_UA = b'uk'
    LANGUAGE_RU = b'ru'


LS_ENTER_EVENT = b'ev_last_stand_main_enter'
LS_EXIT_EVENT = b'ev_last_stand_main_exit'
LS_SOUND_REMAPPING = b'last_stand_remapping'
ABOUT_GAME_MODE_ENTER = b'ev_last_stand_about_event_enter'
ABOUT_GAME_MODE_EXIT = b'ev_last_stand_about_event_exit'
REWARD_PATH_ENTER = b'ev_last_stand_reward_path_enter'
REWARD_PATH_EXIT = b'ev_last_stand_reward_path_exit'
META_INTRO_ENTER = b'ev_last_stand_info_objectives_enter'
META_INTRO_EXIT = b'ev_last_stand_info_objectives_exit'
CONSUMABLES_VIEW_ENTER = b'ev_last_stand_consumables_enter'
CONSUMABLES_VIEW_EXIT = b'ev_last_stand_consumables_exit'
PRE_QUEUE_ENTER = b'ev_last_stand_matchmaker_enter'
PRE_QUEUE_EXIT = b'ev_last_stand_matchmaker_exit'
LS_PREVIEW_ENTER = b'ev_hw_hangar_tank_preview_enter'
LS_PREVIEW_EXIT = b'ev_hw_hangar_tank_preview_exit'
META_STORY_POINT_OPEN_SOUND = b'ev_last_stand_quantum{}_enter'
META_STORY_POINT_CLOSE_SOUND = b'ev_last_stand_quantum{}_exit'
META_VOICEOVER_UNMUTE = b'ev_last_stand_quantum_sound_on'
META_VOICEOVER_MUTE = b'ev_last_stand_quantum_sound_off'
META_VOICEOVER_BUTTON_CLICK_UNMUTE = b'ev_last_stand_quantum_button_sound_on'
META_VOICEOVER_BUTTON_CLICK_MUTE = b'ev_last_stand_quantum_button_sound_off'
PBS_ENTER = b'ev_last_stand_pbs_screen_enter'
PBS_EXIT = b'ev_last_stand_pbs_screen_exit'
BUNDLE_VIEW_ENTER = b'ev_last_stand_exchange_screen_enter'
BUNDLE_VIEW_EXIT = b'ev_last_stand_exchange_screen_exit'
REWARD_WINDOW_ENTER = b'ev_last_stand_reward_screen_enter'
REWARD_WINDOW_EXIT = b'ev_last_stand_reward_screen_exit'
DIFFICULTY_SCREEN = {(DifficultyLevel.MEDIUM): b'ev_last_stand_chapter_unlocked_02', 
   (DifficultyLevel.HARD): b'ev_last_stand_chapter_unlocked_03'}

class DifficultyWindowState(CONST_CONTAINER):
    GROUP = b'STATE_hangar_filtered'
    OPEN = b'STATE_hangar_filtered_on'
    CLOSE = b'STATE_hangar_filtered_off'


class RewardState(CONST_CONTAINER):
    GROUP = b'STATE_overlay_hangar_general'
    GENERAL_ON = b'STATE_overlay_hangar_general_on'
    GENERAL_OFF = b'STATE_overlay_hangar_general_off'


class PersonalDeathZoneAbilityBossState(CONST_CONTAINER):
    GROUP = b'STATE_ev_gp_deathzone_aoe'
    ENTER = b'STATE_ev_gp_deathzone_aoe_enter'
    EXIT = b'STATE_ev_gp_deathzone_aoe_exit'


BOTS_SPAWN = {b'germany:G00_Bomber_LS_BOT': b'ev_gp_bot_bomber_spawn', 
   b'germany:G00_Obelisk_01_LS_bot': b'ev_gp_bot_obelisk_spawn_3D', 
   b'germany:G00_Obelisk_02_LS_bot': b'ev_gp_bot_obelisk_spawn_3D', 
   b'germany:G00_Obelisk_03_LS_bot': b'ev_gp_bot_obelisk_spawn_3D'}
BOTS_ENGINE = {b'usa:A100_T49_LS_BOT': b'ev_gp_bot_lost_engine', 
   b'germany:G00_Obelisk_01_LS_bot': b'ev_gp_bot_obelisk_engine', 
   b'germany:G00_Obelisk_02_LS_bot': b'ev_gp_bot_obelisk_engine', 
   b'germany:G00_Obelisk_03_LS_bot': b'ev_gp_bot_obelisk_engine', 
   b'uk:GB99_Turtle_Mk1_EASY_LS_BOT': b'ev_gp_bot_bastion_engine', 
   b'uk:GB99_Turtle_Mk1_MEDIUM_LS_BOT': b'ev_gp_bot_bastion_engine', 
   b'uk:GB99_Turtle_Mk1_HARD_LS_BOT': b'ev_gp_bot_bastion_engine'}
BOTS_EXPLOSION = {b'germany:G00_Bomber_LS_BOT': b'ev_gp_bot_bomber_explosion', 
   b'germany:G00_Alpha_Bomber_LS_BOT': b'ev_gp_bot_alpha_bomber_explosion', 
   b'usa:A100_T49_LS_BOT': b'ev_gp_bot_lost_explosion', 
   b'germany:G114_Rheinmetall_Skorpian_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'germany:G99_RhB_Waffentrager_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'germany:G97_Waffentrager_IV_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'germany:G54_E-50_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'uk:GB81_FV4004_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'uk:GB83_FV4005_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'germany:G73_E50_Ausf_M_LS_BOT': b'ev_gp_bot_alpha_explosion', 
   b'uk:GB125_Saladin_LS_BOT': b'ev_gp_bot_detonator_explosion', 
   b'germany:G25_PzII_Luchs_Alpha_LS_BOT': b'ev_gp_bot_rabbit_explosion', 
   b'france:F110_Lynx_6x6_LS_BOT': b'ev_gp_bot_trapper_explosion', 
   b'ussr:R171_IS_3_II_LS_BOT': b'ev_gp_bot_charger_explosion', 
   b'czech:Cz34_Vz_71_Tesak_LS_BOT': b'ev_gp_bot_ripper_explosion', 
   b'germany:G00_K_bomber_Boss_LS25_bot': b'ev_gp_bot_boss_bomber_explosion', 
   b'germany:G187_Taschenratte_LS_BOT': b'ev_gp_bot_boss_zero_explosion', 
   b'germany:G00_Obelisk_01_LS_bot': b'ev_gp_bot_obelisk_explosion', 
   b'germany:G00_Obelisk_02_LS_bot': b'ev_gp_bot_obelisk_explosion', 
   b'germany:G00_Obelisk_03_LS_bot': b'ev_gp_bot_obelisk_explosion', 
   b'uk:GB99_Turtle_Mk1_EASY_LS_BOT': b'ev_gp_bot_bastion_explosion', 
   b'uk:GB99_Turtle_Mk1_MEDIUM_LS_BOT': b'ev_gp_bot_bastion_explosion', 
   b'uk:GB99_Turtle_Mk1_HARD_LS_BOT': b'ev_gp_bot_bastion_explosion'}
BATTLE_START = b'ev_last_stand_gameplay_start'
BATTLE_FINISH = b'ev_last_stand_gameplay_stop'
CONVOY_PROGRESS_RTPC = b'RTPC_ext_ls_boss_bomber'

class DeathZoneSounds(CONST_CONTAINER):
    ENTER = b'ev_gp_red_death_zone_enter'
    LEAVE = b'ev_gp_red_death_zone_exit'
    DAMAGE = b'ev_gp_red_death_zone_damage'


class PersonalDeathZoneSounds(CONST_CONTAINER):
    ACTIVATION = b'ev_gp_deathzone_aoe_activation'
    DEACTIVATION = b'ev_gp_deathzone_aoe_deactivation'


class PostMortemSounds(CONST_CONTAINER):
    ON = b'ev_last_stand_postmortem_on'
    OFF = b'ev_last_stand_postmortem_off'


VEHICLE_OBJ_NAME_PATTERN = b'lsVehicleSound_{}'

class Difficulty(CONST_CONTAINER):
    EASY = b'01'
    MEDIUM = b'02'
    HARD = b'03'
    DEFAULT = EASY
    _DIFFICULTY_BY_ARENA_BONUS_TYPE = {(ARENA_BONUS_TYPE.LAST_STAND): EASY, 
       (ARENA_BONUS_TYPE.LAST_STAND_MEDIUM): MEDIUM, 
       (ARENA_BONUS_TYPE.LAST_STAND_HARD): HARD}

    @classmethod
    def getDifficultyByArenaBonusType(cls, arenaBonusType):
        return cls._DIFFICULTY_BY_ARENA_BONUS_TYPE.get(arenaBonusType, cls.DEFAULT)


class DifficultyFormatter(object):

    def __init__(self, str_):
        self._str = str_
        return

    def __call__(self, arenaBonusType):
        return self._str.format(dif=Difficulty.getDifficultyByArenaBonusType(arenaBonusType))


class DifficultyState(CONST_CONTAINER):
    GROUP = b'STATE_ev_last_stand_chapter'
    VALUE = DifficultyFormatter(b'STATE_ev_last_stand_chapter_{dif}')


class BattleEquipmentPanelSounds(CONST_CONTAINER):
    ACTIVATE = b'ev_last_stand_gp_ui_ability_button'
    READY = b'ev_last_stand_gp_ui_ability_button_ready'
    NOT_READY = b'ev_last_stand_gp_ui_ability_button_not_ready'


class LootSounds(CONST_CONTAINER):

    class Player(CONST_CONTAINER):
        PICKUP_SUCCEED = {b'LS_lootSoulsSmall': b'ev_last_stand_collect_pc_player', 
           b'LS_lootSoulsMedium': b'ev_last_stand_collect_pc_player', 
           b'LS_lootSoulsBig': b'ev_last_stand_collect_pc_player', 
           b'LS_lootShells': b'ev_halloween_2020_gameplay_collect_buff'}

    class Ally(CONST_CONTAINER):
        PICKUP_SUCCEED = b'ev_last_stand_collect_all_players'


HANGAR_SOUND_SETTINGS = CommonSoundSpaceSettings(name=b'lsHangar', entranceStates={(HangarSoundStates.PLACE.value): (HangarSoundStates.PLACE_GARAGE.value), (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')

class LastStandVO(CONST_CONTAINER):
    PLAYER_DEAD = b'ev_last_stand_vo_player_dead'
    ALLY_4_TANKS_LEFT = Voiceover(b'ev_last_stand_vo_4_tanks_left', aliveOnly=True)
    ALLY_3_TANKS_LEFT = Voiceover(b'ev_last_stand_vo_3_tanks_left', aliveOnly=True)
    ALLY_2_TANKS_LEFT = Voiceover(b'ev_last_stand_vo_2_tanks_left', aliveOnly=True)
    ALLY_1_TANKS_LEFT = Voiceover(b'ev_last_stand_vo_player_last', aliveOnly=True)
    BATTLE_STARTED = Voiceover(b'ev_last_stand_vo_start', aliveOnly=True)
    WAVE_2_STARTED = b'ev_last_stand_vo_bots_spawn_02'
    WAVE_3_STARTED = b'ev_last_stand_vo_bots_spawn_03'
    WAVE_4_STARTED = b'ev_last_stand_vo_bots_spawn_04'
    WAVE_5_STARTED = b'ev_last_stand_vo_final_bots_spawn'
    WAVE_FINISHED = Voiceover(b'ev_last_stand_vo_destroyed_all_bots', aliveOnly=True)
    ONE_MINUTE_LEFT = b'ev_last_stand_vo_1min'
    WIN = b'ev_last_stand_vo_win'
    LOSE = b'ev_last_stand_vo_defeat'

    @classmethod
    def getWaveStartedVO(cls, phase):
        return getattr(cls, (b'WAVE_{}_STARTED').format(phase), None)

    @classmethod
    def getAllyTanksLeftVO(cls, alliesAliveCount):
        return getattr(cls, (b'ALLY_{}_TANKS_LEFT').format(alliesAliveCount), None)


class BattleMusic(CONST_CONTAINER):
    WAVE_STARTED = b'ev_last_stand_music_battle'
    BOTS_DESTROYED = b'ev_last_stand_music_exploration'
    WIN = b'ev_last_stand_music_end'


class ObeliskBattleSound(CONST_CONTAINER):
    HIT_2D = b'ev_gp_bot_obelisk_weak_zone_hit_2d'
    HIT_3D = b'ev_gp_bot_obelisk_weak_zone_hit_3d'
