from supply_shared import Supply
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS
from epic_constants import EPIC_BATTLE_TEAM_ID

class EPIC_TIME_WWEVENTS(object):
    EB_RESPAWN_COUNT_DOWN_SOUND_ID = {True: b'timer', False: b'timer_stop'}
    EB_TIME_OVER = b'time_over'


class EPIC_OVERTIME_SOUND_NOTIFICATIONS(object):
    EB_OVERTIME_COUNTDOWN = b'eb_overtime_countdown'
    EB_OVERTIME_COUNTDOWN_STOP = b'eb_overtime_countdown_stop'
    BF_EB_OVERTIME = {True: b'eb_overtime_ATK', 
       False: b'eb_overtime_DEF'}
    BF_EB_OVERTIME_START = b'eb_overtime_start'


class EPIC_METAGAME_WWISE_SOUND_EVENTS(object):
    EB_ACHIEVED_RANK = b'eb_achieved_rank'
    EB_LEVEL_REACHED = b'eb_level_reached'
    EB_PROGRESS_BAR_START = b'gui_progress_bar'
    EB_PROGRESS_BAR_STOP = b'gui_progress_bar_stop'
    EB_LEVEL_REACHED_MAX = b'eb_level_reached_maximum'


class EPIC_SOUND(object):
    EPIC_MSG_SOUNDS_ENABLED = True
    BF_EB_EQUIPMENT_SOUND_LIST = (b'INSPIRE', b'ARTILLERY', b'RECON', b'BOMBER')
    EB_READY_FOR_DEPLOYMENT = b'eb_ready_for_deployment'
    BF_EB_START_BATTLE = {(EPIC_BATTLE_TEAM_ID.TEAM_ATTACKER): b'vo_eb_start_ATK', 
       (EPIC_BATTLE_TEAM_ID.TEAM_DEFENDER): b'vo_eb_start_DEF'}
    BF_EB_GLOBAL_MESSAGE = b'eb_general_message'
    BF_EB_WPN_ZONE_PROTECTION = b'eb_warships_firing'
    BF_EB_BASE_CAPTURE_SIREN_SOUND = b'eb_zone_capture'
    BF_EB_ENTER_CLOSED_ZONE = b'eb_enter_closed_zone'
    BF_EB_ENTER_PROTECTION_ZONE = b'eb_enter_landing_zone'
    BF_EB_AIR_STRIKE_WARNING = b'eb_airstrike_warning_defender'
    BF_EB_LEFT_CLICK_TO_FOLLOW = b'eb_left_click_to_follow'
    BF_EB_SPECTATOR_MODE_FOLLOW_TANK = b'eb_follow_tank'
    BF_EB_LANDING_ZONE_PROTECTION = b'eb_closed_zone_artillery_fire'
    BF_EB_CLOSED_ZONE_ARTILLERY = b'eb_closed_zone_artillery_fire'
    BF_EB_RECOVERY_REQUESTED = b'eb_recovery_requested'
    BF_EB_RECOVERY_SUCCESSFUL = b'eb_recovery_successful'
    BF_EB_RECOVERY_CANCELED = b'eb_recovery_canceled'
    BF_EB_NEW_OBJECTIVE = b'eb_new_battle_objective'
    BF_EB_SPECIFIC_TIME = b'eb_specific_time'
    BF_EB_GENERAL = b'eb_general'
    BF_EB_RANK_UP = {b'show': b'eb_rank_up_show', 
       b'hide': b'eb_rank_up_hide'}
    PROMOTION_RECEIVED = b'eb_promotion'
    BF_EB_RETREAT_SUCCESSFUL = b'eb_retreat_successful'
    BF_EB_ZONE_CONTESTED_ATK = {b'A': b'eb_zone_contested_ATK_A', 
       b'B': b'eb_zone_contested_ATK_B', 
       b'C': b'eb_zone_contested_ATK_C', 
       b'D': b'eb_zone_contested_ATK_D', 
       b'E': b'eb_zone_contested_ATK_E', 
       b'F': b'eb_zone_contested_ATK_F'}
    BF_EB_ZONE_CONTESTED_DEF = {b'A': b'eb_zone_contested_DEF_A', 
       b'B': b'eb_zone_contested_DEF_B', 
       b'C': b'eb_zone_contested_DEF_C', 
       b'D': b'eb_zone_contested_DEF_D', 
       b'E': b'eb_zone_contested_DEF_E', 
       b'F': b'eb_zone_contested_DEF_F'}
    BF_EB_ZONE_CAPTURED_ATK = {True: b'eb_own_zone_captured_ATK', 
       False: b'eb_other_zone_captured_ATK'}
    BF_EB_ZONE_CAPTURED_DEF = {True: b'eb_own_zone_captured_DEF', 
       False: b'eb_other_zone_captured_DEF'}
    BF_EB_AIRSTRIKE_ATK = b'eb_airstrike_ATK'
    BF_EB_AIRSTRIKE_DEF = b'eb_airstrike_DEF'
    BF_EB_AIR_SUPPORT = {(GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE): BF_EB_AIRSTRIKE_ATK, 
       (GAME_MESSAGES_CONSTS.BASE_CAPTURED): BF_EB_AIRSTRIKE_DEF}
    BF_EB_MAIN_OBJECTIVES_REACHED_ATK = {True: b'eb_main_objectives_reached_ATK', 
       False: b'eb_main_objectives_reached_other_ATK'}
    BF_EB_MAIN_OBJECTIVES_REACHED_DEF = {True: b'eb_main_objectives_reached_DEF', 
       False: b'eb_main_objectives_reached_other_DEF'}
    BF_EB_OBJECTIVE_UNDER_ATTACK_ATK = {1: b'eb_objective_under_attack_ATK_1', 
       2: b'eb_objective_under_attack_ATK_2', 
       3: b'eb_objective_under_attack_ATK_3', 
       4: b'eb_objective_under_attack_ATK_4', 
       5: b'eb_objective_under_attack_ATK_5'}
    BF_EB_OBJECTIVE_UNDER_ATTACK_DEF = {1: b'eb_objective_under_attack_DEF_1', 
       2: b'eb_objective_under_attack_DEF_2', 
       3: b'eb_objective_under_attack_DEF_3', 
       4: b'eb_objective_under_attack_DEF_4', 
       5: b'eb_objective_under_attack_DEF_5'}
    BF_EB_MAIN_OBJECTIVES_ONE_DESTROYED = b'eb_objective_destroyed'
    BF_EB_MAIN_OBJECTIVES_ONLY_ONE_LEFT = b'eb_main_objectives_only_one_left'
    BF_EB_MAIN_OBJECTIVES_ALL_DOWN = b'eb_main_objectives_all_down'
    BF_EB_HQ_DESTROYED_ATK_OR_DEF = {(GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED_POSITIVE): b'_ATK', 
       (GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED): b'_DEF'}
    BF_EB_REINFORCEMENTS_ARRIVED = b'eb_reinforcements_arrived'
    BF_EB_REINFORCEMENTS_CEASED = b'eb_reinforcements_ceased'
    BF_EB_TIME_OUT = {True: b'eb_time_out_VICTORY', 
       False: b'eb_time_out_DEFEAT'}
    BF_EB_ALL_ENEMIES_DESTROYED = {True: b'eb_all_enemies_destroyed_VICTORY', 
       False: b'eb_all_enemies_destroyed_DEFEAT'}
    BF_EB_STOP_TICKING = b'time_countdown_stop'
    BF_EB_SUPPLY_UNLOCKED = {(Supply.PILLBOX): b'eb_activation_dot_object', 
       (Supply.FLAMER): b'eb_activation_flamethrower_object', 
       (Supply.MORTAR): b'eb_activation_rszo_object', 
       (Supply.AIRSHIP): b'eb_activation_airship_object'}
    BF_EB_SUPPLY_ACTIVE_POSITIVE = b'eb_zone_airship_object'
    BF_EB_SUPPLY_ACTIVE = b'eb_activity_zone_airship_object'
    BF_EB_VO_MESSAGES = {(GAME_MESSAGES_CONSTS.BASE_CAPTURED): BF_EB_ZONE_CAPTURED_DEF, 
       (GAME_MESSAGES_CONSTS.BASE_CAPTURED_POSITIVE): BF_EB_ZONE_CAPTURED_ATK, 
       (GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED): BF_EB_MAIN_OBJECTIVES_ONE_DESTROYED, 
       (GAME_MESSAGES_CONSTS.OBJECTIVE_DESTROYED_POSITIVE): BF_EB_MAIN_OBJECTIVES_ONE_DESTROYED, 
       (GAME_MESSAGES_CONSTS.HQ_BATTLE_STARTED): BF_EB_MAIN_OBJECTIVES_REACHED_DEF, 
       (GAME_MESSAGES_CONSTS.HQ_BATTLE_STARTED_POSITIVE): BF_EB_MAIN_OBJECTIVES_REACHED_ATK, 
       (GAME_MESSAGES_CONSTS.TIME_REMAINING): BF_EB_SPECIFIC_TIME, 
       (GAME_MESSAGES_CONSTS.TIME_REMAINING_POSITIVE): BF_EB_SPECIFIC_TIME, 
       (GAME_MESSAGES_CONSTS.CAPTURE_BASE): BF_EB_NEW_OBJECTIVE, 
       (GAME_MESSAGES_CONSTS.DEFEND_BASE): BF_EB_NEW_OBJECTIVE, 
       (GAME_MESSAGES_CONSTS.DESTROY_OBJECTIVE): BF_EB_NEW_OBJECTIVE, 
       (GAME_MESSAGES_CONSTS.DEFEND_OBJECTIVE): BF_EB_NEW_OBJECTIVE, 
       (GAME_MESSAGES_CONSTS.OVERTIME): (EPIC_OVERTIME_SOUND_NOTIFICATIONS.BF_EB_OVERTIME), 
       (GAME_MESSAGES_CONSTS.BASE_CONTESTED): BF_EB_ZONE_CONTESTED_DEF, 
       (GAME_MESSAGES_CONSTS.BASE_CONTESTED_POSITIVE): BF_EB_ZONE_CONTESTED_ATK, 
       (GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK): BF_EB_OBJECTIVE_UNDER_ATTACK_DEF, 
       (GAME_MESSAGES_CONSTS.OBJECTIVE_UNDER_ATTACK_POSITIVE): BF_EB_OBJECTIVE_UNDER_ATTACK_ATK, 
       (GAME_MESSAGES_CONSTS.RETREAT_SUCCESSFUL): BF_EB_RETREAT_SUCCESSFUL, 
       (GAME_MESSAGES_CONSTS.GENERAL_RANK_REACHED): BF_EB_GENERAL, 
       (GAME_MESSAGES_CONSTS.RANK_UP): BF_EB_RANK_UP, 
       (GAME_MESSAGES_CONSTS.SUPPLY_UNLOCKED): BF_EB_SUPPLY_UNLOCKED, 
       (GAME_MESSAGES_CONSTS.SUPPLY_ACTIVE_POSITIVE): BF_EB_SUPPLY_ACTIVE_POSITIVE, 
       (GAME_MESSAGES_CONSTS.SUPPLY_ACTIVE): BF_EB_SUPPLY_ACTIVE, 
       (GAME_MESSAGES_CONSTS.PROMOTION_RECEIVED): PROMOTION_RECEIVED}
    EB_UI_REPPAIR_POINT_COMPLETED = b'eb_ui_repair_point'
    EB_UI_REPPAIR_POINT_PROGRESS = b'eb_ui_repair_point_progress'
    EB_UI_REPPAIR_POINT_PROGRESS_STOP = b'eb_ui_repair_point_progress_stop'
    EB_ABILITY_MINEFIELD_BLOCK = b'eb_ability_minefield_block'
    EB_ABILITY_MINEFIELD_APPLY = b'eb_ability_minefield_apply'
    EB_ABILITY_MINEFIELD_HITS_TARGET = b'eb_ability_minefield_hits_target'
    EB_ABILITY_STEALTH_START = b'eb_ability_stealth_start'
    EB_ABILITY_STEALTH_STOP = b'eb_ability_stealth_stop'
    EB_ABILITY_RENOVATION_COMPLETED = b'eb_ability_renovation_completed'
    EQUIPMENT_ACTIVATED = {b'arcade_minefield_epic_battle': b'eb_ability_minefield_zone', 
       b'fl_regenerationKit': b'eb_ability_renovation_apply', 
       b'stealth_radar': b'eb_ability_stealth_apply'}
    EB_VO_RESERVE_UPGRADED = b'vo_eb_reserve_improving'
    EB_VO_RESERVE_UNLOCKED = b'vo_eb_reserve_unlock'
    EB_VO_TANKS_UNLOCKED = b'vo_eb_unlock_tier_9_tanks'
    EB_TANKS_UNLOCKED = b'eb_tanks_9lvl_unlocked'
    EB_UI_ADD_TIME_EMERGENCE = b'eb_ui_add_time_emergence'
    EB_UI_CANNON_DESTRUCTION_EMERGENCE = b'eb_ui_cannon_destruction_emergence'
    EB_UI_CANNON_DESTRUCTION_CROSS = b'eb_ui_cannon_destruction_cross'
    EB_UI_CANNON_DESTRUCTION_DISAPPEARANCE = b'eb_ui_cannon_destruction_disappearance'
    EB_AMBIENT_PROGRESS_PAGE_ENTER = b'eb_ambient_progress_page_enter'
    EB_AMBIENT_PROGRESS_PAGE_EXIT = b'eb_ambient_progress_page_exit'
    EB_SUPPLY_UNLOCKED = b'eb_activity_object'
    EB_UI_SUPPLY_UNLOCKED = b'eb_ui_activity_object'
    EB_AIRSHIP_SPOTTED = b'eb_enemy_sighted_for_team'
    QUESTS_VIEW_ACTIVATION = b'eb_ui_zone_attack_disappearance'
    QUESTS_VIEW_PROGRESSION = b'eb_ui_zone_attack_emergence'
    QUESTS_VIEW_NEW = b'eb_new_task_ready'
    QUESTS_VIEW_COMPLETED = b'eb_task_completed'
    QUESTS_VIEW_NOT_AVAILABLE = b'eb_task_not_available'
    QUESTS_VIEW_AVAILABLE = b'eb_task_available_again'
    EB_CHANGE_RESPAWN_DIRECTION = b'eb_ui_button_battle_press'


class BF_EB_MAIN_OBJECTIVES_SOUND_NOTIFICATIONS(object):
    ONE_DESTROYED = EPIC_SOUND.BF_EB_MAIN_OBJECTIVES_ONE_DESTROYED
    ONLY_ONE_LEFT = EPIC_SOUND.BF_EB_MAIN_OBJECTIVES_ONLY_ONE_LEFT
    ALL_DOWN = EPIC_SOUND.BF_EB_MAIN_OBJECTIVES_ALL_DOWN
