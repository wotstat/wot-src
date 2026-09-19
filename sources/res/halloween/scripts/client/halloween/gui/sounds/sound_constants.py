from __future__ import absolute_import
from halloween.gui.halloween_gui_constants import DifficultyLevel
from gui.impl.lobby.hangar.base.sound_constants import HangarSoundStates
from gui.sounds.filters import States, StatesGroup
from halloween.gui.impl.gen.view_models.views.lobby.story_choice_view_model import StoryChoiceViewModel
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings
from halloween_common.halloween_constants import ARENA_BONUS_TYPE
from halloween.gui.sounds.voiceovers import Voiceover

class SoundLanguage(CONST_CONTAINER):
    RU_VOICEOVER_REALM_CODES = (b'RU', b'ST', b'QA', b'DEV', b'SB')
    VOICEOVER_LOCALIZATION_SWITCH = b'SWITCH_ext_ev_hw_vo'
    VOICEOVER_CN = b'SWITCH_ext_ev_hw_vo_CN'
    VOICEOVER_RU = b'SWITCH_ext_ev_hw_vo_RU'
    VOICEOVER_UA = b'SWITCH_ext_ev_hw_vo_UA'
    VOICEOVER_EN = b'SWITCH_ext_ev_hw_vo_EN'
    LANGUAGE_UA = b'uk'
    LANGUAGE_RU = b'ru'


HW_SOUND_REMAPPING = b'halloween_remapping'
BUNDLE_ENTER = b'ev_hw_hangar_bundle_screen_enter'
BUNDLE_EXIT = b'ev_hw_hangar_bundle_screen_exit'
HW_ENTER_EVENT = b'ev_hw_main_enter'
HW_EXIT_EVENT = b'ev_hw_main_exit'
HW_RESET_HANGAR_MUSIC_EVENT = b'ev_hw_main_reset'
ABOUT_GAME_MODE_ENTER = b'ev_hw_hangar_info_gamemode_enter'
ABOUT_GAME_MODE_EXIT = b'ev_hw_hangar_info_gamemode_exit'
REWARD_PATH_ENTER = b'ev_hw_hangar_reward_path_enter'
REWARD_PATH_EXIT = b'ev_hw_hangar_reward_path_exit'
META_INTRO_ENTER = b'ev_hw_hangar_info_missions_enter'
META_INTRO_EXIT = b'ev_hw_hangar_info_missions_exit'
CONSUMABLES_VIEW_ENTER = b'ev_hw_hangar_consumables_enter'
CONSUMABLES_VIEW_EXIT = b'ev_hw_hangar_consumables_exit'
COMPARISON_VIEW_ENTER = b'ev_hw_hangar_comparison_enter'
COMPARISON_VIEW_EXIT = b'ev_hw_hangar_comparison_exit'
PRE_QUEUE_ENTER = b'ev_hw_hangar_matchmaker_enter'
PRE_QUEUE_EXIT = b'ev_hw_hangar_matchmaker_exit'
HW_PREVIEW_ENTER = b'ev_hw_hangar_tank_preview_enter'
HW_PREVIEW_EXIT = b'ev_hw_hangar_tank_preview_exit'
META_QUANTUM_SCREEN_ENTER = b'ev_hw_meta_quantum{}_enter'
META_QUANTUM_SCREEN_EXIT = b'ev_hw_meta_quantum{}_exit'
META_QUANTUM_VO_ON = b'ev_hw_meta_quantum{}_vo_on'
META_QUANTUM_VO_OFF = b'ev_hw_meta_quantum{}_vo_off'
PBS_ENTER = b'ev_hw_pbs_screen_enter'
PBS_EXIT = b'ev_hw_pbs_screen_exit'
KING_REWARD_WINDOW_ENTER = b'ev_hw_hangar_king_reward_enter'
KING_REWARD_WINDOW_EXIT = b'ev_hw_hangar_king_reward_exit'
STORY_CHOICE_WINDOW_ENTER = b'ev_hw_meta_narrative_choice_enter'
STORY_CHOICE_WINDOW_EXIT = b'ev_hw_meta_narrative_choice_exit'
CREW_SHOWCASE_ENTER = b'ev_hw_hangar_reward_path_crew_members_enter'
CREW_SHOWCASE_EXIT = b'ev_hw_hangar_reward_path_crew_members_exit'
ABILITIES_INCOMPLETE_DIALOG_ENTER = b'ev_hw_hangar_abilities_incomplete_enter'
ABILITIES_INCOMPLETE_DIALOG_EXIT = b'ev_hw_hangar_abilities_incomplete_exit'
BESTIARY_ENTER = b'ev_hw_hangar_bestiary_enter'
BESTIARY_EXIT = b'ev_hw_hangar_bestiary_exit'
ARENA_PHASE_END_WARNING_EVENT_PREFIX = b'ev_hw_gp_music_1min_{phase:02d}'
DIFFICULTY_SCREEN = {(DifficultyLevel.MEDIUM): b'ev_hw_hangar_difficulty_open_hard', 
   (DifficultyLevel.HARD): b'ev_hw_hangar_difficulty_open_nightmare'}

class DifficultyWindowState(CONST_CONTAINER):
    GROUP = b'STATE_hangar_filtered'
    OPEN = b'STATE_hangar_filtered_on'
    CLOSE = b'STATE_hangar_filtered_off'


class KingRewardState(CONST_CONTAINER):
    GROUP = b'STATE_overlay_hangar_general'
    GENERAL_ON = b'STATE_overlay_hangar_general_on'
    GENERAL_OFF = b'STATE_overlay_hangar_general_off'


class PersonalDeathZoneAbilityBossState(CONST_CONTAINER):
    GROUP = b'STATE_ev_gp_deathzone_aoe'
    ENTER = b'STATE_ev_gp_deathzone_aoe_enter'
    EXIT = b'STATE_ev_gp_deathzone_aoe_exit'


BOTS_SPAWN = {b'germany:G64_Panther_II_Hall_minion': b'ev_hw_gp_hunters_spawn', 
   b'usa:A100_T49_HW_BOT': b'ev_hw_gp_bot_lost_spawn', 
   b'germany:G25_PzII_Luchs_HELL_HALL': None, 
   b'germany:G25_PzII_Luchs_HELL': None, 
   b'germany:G00_Bomber_Hell': b'ev_hw_gp_bot_bomber_spawn', 
   b'germany:G00_K_bomber__HW_21_AI': None, 
   b'france:F110_Lynx_6x6_HW_BOT': None, 
   b'germany:G146_E100_Hell_Boss': None, 
   b'usa:A66_M103_Boss_HW23': None, 
   b'ussr:R205_Rozanov_Boss_HW23': None}
DEFAULT_BOT_SPAWN = None
BOTS_ENGINE = {b'usa:A100_T49_HW_BOT': b'ev_hw_gp_bot_lost_engine', 
   b'uk:GB100_Manticore_HW_BOT': b'ev_hw_gp_bot_scavenger_engine', 
   b'germany:G00_Spider_Boss_HW26_bot': b'ev_hw_gp_bot_hexapod_engine'}
BOTS_EXPLOSION = {b'germany:G00_Bomber_Hell': b'ev_hw_gp_bot_bomber_explosion', 
   b'germany:G00_K_bomber__HW_21_AI': b'ev_hw_gp_bot_alpha_bomber_explosion', 
   b'usa:A100_T49_HW_BOT': b'ev_hw_gp_bot_lost_explosion', 
   b'germany:G114_Rheinmetall_Skorpian_HW_BOT': b'ev_hw_gp_bot_alpha_explosion', 
   b'germany:G99_RhB_Waffentrager_HW_BOT': b'ev_hw_gp_bot_alpha_explosion', 
   b'germany:G97_Waffentrager_IV_HW_BOT': b'ev_hw_gp_bot_alpha_explosion', 
   b'germany:G54_E-50_Hall_minion': b'ev_hw_gp_bot_alpha_explosion', 
   b'uk:GB81_FV4004_HW_BOT': b'ev_hw_gp_bot_alpha_explosion', 
   b'uk:GB83_FV4005_HELL': b'ev_hw_gp_bot_alpha_explosion', 
   b'germany:G73_E50_Ausf_M_Hall_minion': b'ev_hw_gp_bot_alpha_explosion', 
   b'germany:G25_PzII_Luchs_HELL': b'ev_hw_gp_bot_rabbit_explosion', 
   b'germany:G25_PzII_Luchs_HELL_HALL': b'ev_hw_gp_bot_rabbit_explosion', 
   b'france:F110_Lynx_6x6_HW_BOT': b'ev_hw_gp_bot_trapper_explosion', 
   b'ussr:R171_IS_3_II_HW_BOT': b'ev_hw_gp_bot_charger_explosion', 
   b'uk:GB125_Saladin_HW_BOT': b'ev_hw_gp_bot_detonator_explosion', 
   b'germany:G113_SP_I_C_HW_BOT': b'ev_hw_gp_bot_hive_explosion', 
   b'germany:G171_E77_HW_BOT': b'ev_hw_gp_bot_monarch_explosion', 
   b'uk:GB100_Manticore_HW_BOT': b'ev_hw_gp_bot_scavenger_explosion', 
   b'germany:G00_Spider_Boss_HW26_bot': b'ev_hw_gp_bot_hexapod_explosion'}

class VehicleSoulsContainerSounds(CONST_CONTAINER):

    class Player(CONST_CONTAINER):
        ON = b'ev_hw_gp_mini_collector_on'
        OFF = b'ev_hw_gp_mini_collector_off'

    class Ally(CONST_CONTAINER):
        ON = b'ev_hw_gp_mini_collector_on_npc'
        OFF = b'ev_hw_gp_mini_collector_off_npc'


class SoulsCollectorSounds(CONST_CONTAINER):
    RTPC = b'RTPC_ext_hw_gp_collector_capacity'
    LOOP = b'ev_hw_gp_phase_collector'
    COLLECT = b'ev_hw_gp_collecting_mirium_progress'
    FULL = b'ev_hw_gp_collecting_mirium_done'


BATTLE_START = b'ev_hw_gp_start'
BATTLE_FINISH = b'ev_hw_gp_stop'
PHASE_CHANGED = b'ev_hw_gp_phase_teleportation'

class DeathZoneSounds(CONST_CONTAINER):
    ENTER = b'ev_hw_gp_red_death_zone_enter'
    LEAVE = b'ev_hw_gp_red_death_zone_exit'
    DAMAGE = b'ev_hw_gp_red_death_zone_damage'


class PersonalDeathZoneSounds(CONST_CONTAINER):
    ACTIVATION = b'ev_hw_gp_deathzone_aoe_activation'
    DEACTIVATION = b'ev_hw_gp_deathzone_aoe_deactivation'


class PostMortemSounds(CONST_CONTAINER):
    ON = b'ev_hw_gp_postmortem_on'
    OFF = b'ev_hw_gp_postmortem_off'


class VehicleDetectorSounds(CONST_CONTAINER):
    RTPC = b'RTPC_ext_hw_gp_immortal_detector'
    DETECTOR_ON = b'ev_hw_gp_immortal_detector_on'
    DETECTOR_OFF = b'ev_hw_gp_immortal_detector_off'


class AwardCongratsWindowSounds(CONST_CONTAINER):
    ON_ENTER = {(StoryChoiceViewModel.OPTION_1): b'ev_hw_meta_narrative_choice_left_reward', 
       (StoryChoiceViewModel.OPTION_2): b'ev_hw_meta_narrative_choice_right_reward'}


ACTIVE_PHASE_RTPC = b'RTPC_ext_hw_gp_phase'

class ActivePhaseState(CONST_CONTAINER):
    GROUP = b'STATE_ev_hw_gp_phase'
    PHASE_1 = b'STATE_ev_hw_gp_phase_01'
    PHASE_2 = b'STATE_ev_hw_gp_phase_02'
    PHASE_3 = b'STATE_ev_hw_gp_phase_03'
    PHASE_4 = b'STATE_ev_hw_gp_phase_04'
    DEFAULT = PHASE_1
    _STATE_PATTERN = b'PHASE_{}'

    @classmethod
    def getStateByPhase(cls, phaseID):
        return getattr(cls, cls._STATE_PATTERN.format(phaseID), cls.DEFAULT)


SOULS_COLLECTOR_OBJ_NAME = b'hwSoulsCollector'
VEHICLE_OBJ_NAME_PATTERN = b'hwVehicleSound_{}'
LOOT_OBJ_NAME_PATTERN = b'hwLootSound_{}'

class Difficulty(CONST_CONTAINER):
    EASY = b'normal'
    MEDIUM = b'hard'
    HARD = b'nightmare'
    DEFAULT = EASY
    _DIFFICULTY_BY_ARENA_BONUS_TYPE = {(ARENA_BONUS_TYPE.HALLOWEEN): EASY, 
       (ARENA_BONUS_TYPE.HALLOWEEN_MEDIUM): MEDIUM, 
       (ARENA_BONUS_TYPE.HALLOWEEN_HARD): HARD}

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
    GROUP = b'STATE_ev_hw_difficulty'
    VALUE = DifficultyFormatter(b'STATE_ev_hw_difficulty_{dif}')


class BossBattleMusic(CONST_CONTAINER):
    BOSS_FIGHT_START = b'ev_hw_music_bf_normal_start'
    FIRST_DAMAGE_2_LIVES_LEFT = b'ev_hw_music_bf_normal_1_2'
    FIRST_DAMAGE_1_LIVES_LEFT = b'ev_hw_music_bf_normal_2_2'
    PHASE_1_FINISH = b'ev_hw_music_bf_normal_2_1'
    BOSS_KILLED = b'ev_hw_music_bf_normal_win'
    LOSE_2_LIVES_LEFT_BEFORE_1_SHOT = b'ev_hw_music_bf_normal_lose_1_1'
    LOSE_2_LIVES_LEFT_AFTER_1_SHOT = b'ev_hw_music_bf_normal_lose_1_2'
    LOSE_1_LIVES_LEFT_BEFORE_1_SHOT = b'ev_hw_music_bf_normal_lose_2_1'
    LOSE_1_LIVES_LEFT_AFTER_1_SHOT = b'ev_hw_music_bf_normal_lose_2_2'

    @classmethod
    def getFirstDamageEventByBossLives(cls, livesLeft):
        return getattr(cls, (b'FIRST_DAMAGE_{}_LIVES_LEFT').format(livesLeft), cls.FIRST_DAMAGE_2_LIVES_LEFT)

    @classmethod
    def getLoseEvent(cls, isFirstShotPerformed, livesLeft):
        state = b'AFTER' if isFirstShotPerformed else b'BEFORE'
        return getattr(cls, (b'LOSE_{}_LIVES_LEFT_{}_1_SHOT').format(livesLeft, state), cls.LOSE_2_LIVES_LEFT_BEFORE_1_SHOT)


class HexapodBossBattleMusic(CONST_CONTAINER):
    BOSS_HP_RTPC = b'RTPC_ext_hw_gp_boss_hp'


class AnomaliesSounds(CONST_CONTAINER):

    class Battle(CONST_CONTAINER):
        ITEM_HOVER = b'ev_hw_gp_ui_anomalies_highlight'
        UPGRADE_PANEL_APPEAR = b'ev_hw_gp_ui_anomalies_appear'
        ENTER = b'ev_hw_gp_ui_anomalies_enter'
        LEAVE = b'ev_hw_gp_ui_anomalies_exit'

    class Hangar(CONST_CONTAINER):
        ENTER = b'ev_hw_hangar_anomalies_enter'
        LEAVE = b'ev_hw_hangar_anomalies_exit'


class BattleEquipmentPanelSounds(CONST_CONTAINER):
    ACTIVATE = b'ev_hw_gp_ui_ability_button'
    READY = b'ev_hw_gp_ui_ability_button_ready'
    NOT_READY = b'ev_hw_gp_ui_ability_button_not_ready'


class BattleBuffsPanelSounds(CONST_CONTAINER):
    ACTIVATE = b'ev_hw_gp_random_buff_hud_on'
    DEACTIVATE = b'ev_hw_gp_random_buff_hud_off'
    SHOW_ICON = b'ev_hw_gp_random_buff_icon'


class PhaseStartSounds(CONST_CONTAINER):
    PHASE_1_STARTED = b'ev_hw_gp_phase_01_stinger'
    PHASE_2_STARTED = b'ev_hw_gp_phase_02_stinger'
    PHASE_3_STARTED = b'ev_hw_gp_phase_03_stinger'
    PHASE_4_STARTED = b'ev_hw_gp_phase_04_stinger'
    _PHASE_STARTED_PATTERN = b'PHASE_{}_STARTED'
    DEFAULT = PHASE_1_STARTED

    @classmethod
    def getPhaseStartedEvent(cls, phaseID):
        return getattr(cls, cls._PHASE_STARTED_PATTERN.format(phaseID), cls.DEFAULT)


class PhaseModifierSounds(CONST_CONTAINER):
    START = {b'chronostorm': b'ev_hw_gp_ui_phase_chronostorm', 
       b'corrosion': b'ev_hw_gp_ui_phase_corrosion', 
       b'execution': b'ev_hw_gp_ui_phase_execution', 
       b'miriumization': b'ev_hw_gp_ui_phase_miriumization'}


class BossBattleSound(CONST_CONTAINER):
    PLAYER_ENTERED_AURA = b'ev_hw_gp_boss_aura_player_in'
    PLAYER_LEAVED_AURA = b'ev_hw_gp_boss_aura_player_out'
    AURA_ACTIVATION = b'ev_hw_gp_boss_aura'
    BOSS_TELEPORTATION = b'ev_hw_gp_bf_boss_teleportation'
    BOSS_HIT_MARKER = b'ev_hw_gp_boss_hit_marker'
    BOSS_HIT_MARKER_INVULNERABILITY = b'ev_hw_gp_boss_hit_marker_invulnerability'

    @classmethod
    def getAuraIntersectionEvent(cls, entered):
        action = b'ENTERED' if entered else b'LEAVED'
        return getattr(cls, (b'PLAYER_{}_AURA').format(action))


class HexapodBossBattleSound(CONST_CONTAINER):
    HEXAPOD_FIRE = b'ev_hw_gp_bot_hexapod_fire'


class PhaseStartedVoiceover(CONST_CONTAINER):
    PHASE_1 = Voiceover(b'ev_hw_gp_vo_phase1_intro', b'ev_hw_gp_vo_phase1_exposition_intro')
    PHASE_2 = Voiceover(b'ev_hw_gp_vo_phase2_intro')
    PHASE_3 = Voiceover(b'ev_hw_gp_vo_phase3_intro')
    PHASE_4 = Voiceover(b'ev_hw_gp_vo_bossfight_intro', b'ev_hw_gp_vo_bossfight_exposition_intro')

    @classmethod
    def get(cls, phaseIndex):
        return getattr(cls, (b'PHASE_{}').format(phaseIndex), None)


class VO(CONST_CONTAINER):
    BOSS_APPEARING = {b'germany:G146_E100_Hell_Boss': b'ev_hw_gp_vo_phase_boss_detection', 
       b'usa:A66_M103_Boss_HW23': b'ev_hw_gp_vo_phase_boss_detection', 
       b'ussr:R205_Rozanov_Boss_HW23': b'ev_hw_gp_vo_phase_boss_detection'}
    LOSE_BEFORE_BOSS_BATTLE = b'ev_hw_vo_phase_lose'
    FIRST_SHOT_AT_BOSS_BEFORE_BOSS_BATTLE = Voiceover(b'ev_hw_gp_vo_phase_boss_shooting', aliveOnly=True)
    BOSSFIGHT_PHASE_2 = Voiceover(b'ev_hw_gp_vo_bossfight_phase2', aliveOnly=True)
    BOSSFIGHT_PHASE_3 = Voiceover(b'ev_hw_gp_vo_bossfight_phase3', aliveOnly=True)
    LOSE_BOSS_FIGHT = b'ev_hw_vo_bossfight_lose'
    PHASE_ONE_MINUTE_LEFT = Voiceover(b'ev_hw_gp_vo_phase_one_minute_timer', aliveOnly=True)
    COLLECTOR_HALF_FILLED = Voiceover(b'ev_hw_gp_vo_phase_collector_half', aliveOnly=True)
    COLLECTOR_FULL_FILLED = Voiceover(b'ev_hw_gp_vo_phase_collector_full', aliveOnly=True)
    SHOT_AT_INVULNERABLE_BOSS = Voiceover(b'ev_hw_gp_vo_bf_boss_shooting', aliveOnly=True)
    PLAYER_DEAD_COMMON = b'ev_hw_gp_vo_player_dead'
    PLAYER_DEAD_BOSSFIGHT = b'ev_hw_gp_vo_player_bossfight_dead'
    ALLY_4_TANKS_LEFT = Voiceover(b'ev_hw_gp_vo_4_tanks_left', aliveOnly=True)
    ALLY_3_TANKS_LEFT = Voiceover(b'ev_hw_gp_vo_3_tanks_left', aliveOnly=True)
    ALLY_2_TANKS_LEFT = Voiceover(b'ev_hw_gp_vo_2_tanks_left', aliveOnly=True)
    ALLY_1_TANKS_LEFT = Voiceover(b'ev_hw_gp_vo_player_last', aliveOnly=True)
    BOTS_SPAWN_BY_ROLE = {b'charger': (Voiceover(b'ev_hw_gp_vo_charger_spawn', aliveOnly=True))}

    @classmethod
    def getAllyTanksLeftVO(cls, alliesAliveCount):
        return getattr(cls, (b'ALLY_{}_TANKS_LEFT').format(alliesAliveCount), None)

    SUBTITLES_ENABLED_SETTING = False


class VOObjects(CONST_CONTAINER):
    WIN = Voiceover(b'ev_hw_vo_bossfight_win', b'ev_hw_vo_bossfight_exposition_win', False)


class LootSounds(CONST_CONTAINER):

    class States(CONST_CONTAINER):
        DEFAULT = {b'HW_lootAnomaly': b'ev_hw_gp_battle_loot_idle'}
        CAPTURED = {b'HW_lootAnomaly': b'ev_hw_gp_battle_loot_capture'}

    class Player(CONST_CONTAINER):
        PICKUP_STARTED = {b'HW_lootAnomaly': b'ev_hw_gp_ui_battle_loot_capture_start'}
        PICKUP_CANCELED = {b'HW_lootAnomaly': b'ev_hw_gp_ui_battle_loot_capture_stop'}
        PICKUP_SUCCEED = {b'HW_lootSoulsSmall': b'ev_hw_gp_collect_mirium_pc', 
           b'HW_lootSoulsMedium': b'ev_hw_gp_collect_mirium_pc', 
           b'HW_lootSoulsBig': b'ev_hw_gp_collect_mirium_pc', 
           b'HW_lootShells': b'ev_hw_gp_collect_xtra_wpn_pc', 
           b'HW_lootAnomaly': b'ev_hw_gp_ui_battle_loot_capture_finish'}

    class Ally(CONST_CONTAINER):
        PICKUP_SUCCEED = b'ev_hw_gp_collect_mirium_npc'


HANGAR_SOUND_SETTINGS = CommonSoundSpaceSettings(name=b'hwHangar', entranceStates={(HangarSoundStates.PLACE.value): (HangarSoundStates.PLACE_GARAGE.value), (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
