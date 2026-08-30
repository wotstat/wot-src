import weakref
from collections import namedtuple
from account_helpers.settings_core import settings_constants, longToInt32
from account_helpers.settings_core.migrations import migrateToVersion
from account_helpers.settings_core.settings_constants import VERSION, GuiSettingsBehavior, OnceOnlyHints, SPGAim, CONTOUR, NewYearStorageKeys, WTLootBoxesViewedKeys
from adisp import adisp_process, adisp_async
from debug_utils import LOG_ERROR, LOG_DEBUG
from gui.battle_pass.battle_pass_helpers import updateBattlePassSettings
from gui.limited_ui.lui_rules_storage import LuiRules
from gui.server_events.pm_constants import PM_TUTOR_FIELDS
from helpers import dependency
from shared_utils import CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCache
GUI_START_BEHAVIOR = b'guiStartBehavior'

class SETTINGS_SECTIONS(CONST_CONTAINER):
    GAME = b'GAME'
    GAME_EXTENDED = b'GAME_EXTENDED'
    GAME_EXTENDED_2 = b'GAME_EXTENDED_2'
    GAMEPLAY = b'GAMEPLAY'
    GRAPHICS = b'GRAPHICS'
    SOUND = b'SOUND'
    CONTROLS = b'CONTROLS'
    AIM_1 = b'AIM_1'
    AIM_2 = b'AIM_2'
    AIM_3 = b'AIM_3'
    AIM_4 = b'AIM_4'
    MARKERS_1 = b'MARKERS_1'
    MARKERS_2 = b'MARKERS_2'
    CAROUSEL_FILTER_1 = b'CAROUSEL_FILTER_1'
    CAROUSEL_FILTER_2 = b'CAROUSEL_FILTER_2'
    RANKED_CAROUSEL_FILTER_1 = b'RANKED_CAROUSEL_FILTER_1'
    RANKED_CAROUSEL_FILTER_2 = b'RANKED_CAROUSEL_FILTER_2'
    ROYALE_CAROUSEL_FILTER_1 = b'ROYALE_CAROUSEL_FILTER_1'
    ROYALE_CAROUSEL_FILTER_2 = b'ROYALE_CAROUSEL_FILTER_2'
    EPICBATTLE_CAROUSEL_FILTER_1 = b'EPICBATTLE_CAROUSEL_FILTER_1'
    EPICBATTLE_CAROUSEL_FILTER_2 = b'EPICBATTLE_CAROUSEL_FILTER_2'
    BATTLEPASS_CAROUSEL_FILTER_1 = b'BATTLEPASS_CAROUSEL_FILTER_1'
    MAPBOX_CAROUSEL_FILTER_1 = b'MAPBOX_CAROUSEL_FILTER_1'
    MAPBOX_CAROUSEL_FILTER_2 = b'MAPBOX_CAROUSEL_FILTER_2'
    FUN_RANDOM_CAROUSEL_FILTER_1 = b'FUN_RANDOM_CAROUSEL_FILTER_1'
    FUN_RANDOM_CAROUSEL_FILTER_2 = b'FUN_RANDOM_CAROUSEL_FILTER_2'
    COMP7_CAROUSEL_FILTER_1 = b'COMP7_CAROUSEL_FILTER_1'
    COMP7_CAROUSEL_FILTER_2 = b'COMP7_CAROUSEL_FILTER_2'
    VERSUS_AI_CAROUSEL_FILTER_1 = b'VERSUS_AI_CAROUSEL_FILTER_1'
    VERSUS_AI_CAROUSEL_FILTER_2 = b'VERSUS_AI_CAROUSEL_FILTER_2'
    GUI_START_BEHAVIOR = b'GUI_START_BEHAVIOR'
    EULA_VERSION = b'EULA_VERSION'
    MARKS_ON_GUN = b'MARKS_ON_GUN'
    CONTACTS = b'CONTACTS'
    FALLOUT = b'FALLOUT'
    ONCE_ONLY_HINTS = b'ONCE_ONLY_HINTS'
    ONCE_ONLY_HINTS_2 = b'ONCE_ONLY_HINTS_2'
    ONCE_ONLY_HINTS_3 = b'ONCE_ONLY_HINTS_3'
    FEEDBACK = b'FEEDBACK'
    DAMAGE_INDICATOR = b'FEEDBACK_DAMAGE_INDICATOR'
    DAMAGE_LOG = b'FEEDBACK_DAMAGE_LOG'
    BATTLE_EVENTS = b'FEEDBACK_BATTLE_EVENTS'
    BATTLE_BORDER_MAP = b'FEEDBACK_BORDER_MAP'
    SIXTH_SENSE = b'FEEDBACK_SIXTH_SENSE'
    QUESTS_PROGRESS = b'QUESTS_PROGRESS'
    UI_STORAGE = b'UI_STORAGE'
    UI_STORAGE_2 = b'UI_STORAGE_2'
    BATTLE_MATTERS_QUESTS = b'BATTLE_MATTERS_QUESTS'
    SESSION_STATS = b'SESSION_STATS'
    BATTLE_PASS_STORAGE = b'BATTLE_PASS_STORAGE'
    BATTLE_COMM = b'BATTLE_COMM'
    DOG_TAGS = b'DOG_TAGS'
    UNIT_FILTER = b'UNIT_FILTER'
    BATTLE_HUD = b'BATTLE_HUD'
    SPG_AIM = b'SPG_AIM'
    CONTOUR = b'CONTOUR'
    LIMITED_UI_1 = b'LIMITED_UI_1'
    LIMITED_UI_2 = b'LIMITED_UI_2'
    ARMORY_YARD = b'ARMORY_YARD'
    NEW_YEAR = b'NEW_YEAR'
    BATTLE_CONTEXT_HINTS = b'BATTLE_CONTEXT_HINTS'
    BATTLE_CONTEXT_HINTS_2 = b'BATTLE_CONTEXT_HINTS_2'
    BATTLE_CONTEXT_HINTS_3 = b'BATTLE_CONTEXT_HINTS_3'
    BATTLE_CONTEXT_HINTS_GROUP = (BATTLE_CONTEXT_HINTS, BATTLE_CONTEXT_HINTS_2, BATTLE_CONTEXT_HINTS_3)
    ONCE_ONLY_HINTS_GROUP = (ONCE_ONLY_HINTS, ONCE_ONLY_HINTS_2, ONCE_ONLY_HINTS_3)
    LIMITED_UI_GROUP = (LIMITED_UI_1, LIMITED_UI_2)
    LOOT_BOX_VIEWED = b'LOOT_BOX_VIEWED'


class UI_STORAGE_KEYS(CONST_CONTAINER):
    AUTO_RELOAD_HIGHLIGHTS_COUNTER = b'auto_reload_highlights_count'
    AUTO_RELOAD_MARK_IS_SHOWN = b'auto_reload_mark_shown'
    DISABLE_ANIMATED_TOOLTIP = b'disable_animated_tooltip'
    FIELD_POST_HINT_IS_SHOWN = b'field_post_hint'
    REFERRAL_BUTTON_CIRCLES_SHOWN = b'referral_button_circles_shown'
    DUAL_GUN_HIGHLIGHTS_COUNTER = b'dual_gun_highlights_count'
    DUAL_GUN_MARK_IS_SHOWN = b'dual_gun_mark_shown'
    DISABLE_EDITABLE_STYLE_REWRITE_WARNING = b'disable_editable_style_rewrite_warning'
    OPTIONAL_DEVICE_SETUP_INTRO_SHOWN = b'optional_device_setup_intro_shown'
    TURBOSHAFT_HIGHLIGHTS_COUNTER = b'turboshaft_highlights_count'
    ROCKET_ACCELERATION_HIGHLIGHTS_COUNTER = b'rocket_acceleration_highlights_count'
    TURBOSHAFT_MARK_IS_SHOWN = b'turboshaft_mark_shown'
    ROCKET_ACCELERATION_MARK_IS_SHOWN = b'rocket_acceleration_mark_shown'
    EPIC_BATTLE_ABILITIES_INTRO_SHOWN = b'epic_battle_abilities_intro_shown'
    POST_PROGRESSION_INTRO_SHOWN = b'post_progression_intro_shown'
    VEH_PREVIEW_POST_PROGRESSION_BULLET_SHOWN = b'veh_preview_post_progression_bullet_shown'
    ACHIEVEMENT_EDIT_VIEW_VISITED = b'achievement_edit_view_visited'
    DUAL_ACCURACY_HIGHLIGHTS_COUNTER = b'dual_accuracy_highlights_count'
    DUAL_ACCURACY_MARK_IS_SHOWN = b'dual_accuracy_mark_shown'
    GUI_LOOTBOXES_ENTRY_POINT = b'gui_lootboxes_entry_point'
    FLAMETHROWER_HIGHLIGHTS_COUNTER = b'flamethrower_highlights_count'
    FLAMETHROWER_MARK_IS_SHOWN = b'flamethrower_mark_shown'
    THERMAL_VISION_HIGHLIGHTS_COUNTER = b'thermal_vision_highlights_count'
    THERMAL_VISION_MARK_IS_SHOWN = b'thermal_vision_mark_shown'
    AUTO_RELOAD_DUAL_GUN_HIGHLIGHTS_COUNTER = b'auto_reload_dual_gun_highlights_counter'
    AUTO_RELOAD_DUAL_GUN_MARK_IS_SHOWN = b'auto_reload_dual_gun_mark_is_shown'
    CLIP_DUAL_GUN_HIGHLIGHTS_COUNTER = b'clip_dual_gun_highlights_counter'
    CLIP_DUAL_GUN_MARK_IS_SHOWN = b'clip_dual_gun_mark_is_shown'
    DUAL_GUN_DUAL_ACCURACY_HIGHLIGHTS_COUNTER = b'dual_gun_dual_accuracy_highlights_count'
    TANK_ACADEMY_WELCOME_SCREEN_SHOWN = b'tank_academy_welcome_screen_shown'


class BATTLE_MATTERS_KEYS(CONST_CONTAINER):
    QUESTS_SHOWN = b'shown'
    QUEST_PROGRESS = b'questProgress'


class ARMORY_YARD_KEYS(CONST_CONTAINER):
    BUILD_PROGRESS = b'buildProgress'
    CURRENT_SEASON = b'currentSeason'


class BATTLE_CONTEXT_HINTS(CONST_CONTAINER):
    PLAYER_VEHICLE_OBSERVED = b'PlayerVehicleObserved'
    KILLED_WHILE_OBSERVED = b'KilledWhileObserved'
    IN_SAFETY_WHILE_NOT_OBSERVED = b'InSafetyWhileNotObserved'
    ENGINE_DAMAGE_REPAIR_KIT = b'EngineDamageRepairKit'
    AMMUNITION_DAMAGE_REPAIR_KIT = b'AmmunitionDamageRepairKit'
    FUELTANK_DAMAGE_REPAIR_KIT = b'FueltankDamageRepairKit'
    GUN_ROTATOR_DAMAGE_REPAIR_KIT = b'GunRotatorDamageRepairKit'
    GUN_DAMAGE_REPAIR_KIT = b'GunDamageRepairKit'
    AMMUNITION_CRIT = b'AmmunitionCrit'
    FUELTANK_CRIT = b'FueltankCrit'
    GUN_ROTATOR_DESTROY_REPAIR_KIT = b'GunRotatorDestroyRepairKit'
    ENGINE_DESTROY_REPAIR_KIT = b'EngineDestroyRepairKit'
    GUN_DESTROY_REPAIR_KIT = b'GunDestroyRepairKit'
    TRACK_DESTROY_REPAIR_KIT = b'TrackDestroyRepairKit'
    MODULE_DAMAGE = b'ModuleDamage'
    COMMANDER_DAMAGE_MED_KIT = b'CommanderDamageMedKit'
    DRIVER_DAMAGE_MED_KIT = b'DriverDamageMedKit'
    GUNNER_DAMAGE_MED_KIT = b'GunnerDamageMedKit'
    LOADER_DAMAGE_MED_KIT = b'LoaderDamageMedKit'
    RADIOMAN_DAMAGE_MED_KIT = b'RadiomanDamageMedKit'
    AMMO_TYPE_AVAILABLE = b'AmmoTypeAvailable'
    AMMO_TYPE_SWITCH = b'AmmoTypeSwitch'


class ServerSettingsManager(object):
    settingsCache = dependency.descriptor(ISettingsCache)
    GAME = settings_constants.GAME
    GRAPHICS = settings_constants.GRAPHICS
    SOUND = settings_constants.SOUND
    CONTROLS = settings_constants.CONTROLS
    Section = namedtuple(b'Section', [b'masks', b'offsets'])
    Offset = namedtuple(b'Offset', [b'offset', b'mask'])
    CONTACTS = settings_constants.CONTACTS
    DAMAGE_INDICATOR = settings_constants.DAMAGE_INDICATOR
    DAMAGE_LOG = settings_constants.DAMAGE_LOG
    BATTLE_EVENTS = settings_constants.BATTLE_EVENTS
    BATTLE_BORDER_MAP = settings_constants.BATTLE_BORDER_MAP
    QUESTS_PROGRESS = settings_constants.QUESTS_PROGRESS
    SIXTH_SENSE = settings_constants.SIXTH_SENSE
    SESSION_STATS = settings_constants.SESSION_STATS
    BATTLE_COMM = settings_constants.BattleCommStorageKeys
    BATTLE_PASS = settings_constants.BattlePassStorageKeys
    SCORE_PANEL = settings_constants.ScorePanelStorageKeys
    SECTIONS = {(SETTINGS_SECTIONS.GAME): (Section(masks={(GAME.ENABLE_OL_FILTER): 0, 
                                  (GAME.ENABLE_SPAM_FILTER): 1, 
                                  (GAME.INVITES_FROM_FRIENDS): 2, 
                                  (GAME.STORE_RECEIVER_IN_BATTLE): 3, 
                                  (GAME.PLAYERS_PANELS_SHOW_LEVELS): 4, 
                                  (GAME.SHOW_DAMAGE_ICON): 5, 
                                  (GAME.DYNAMIC_CAMERA): 6, 
                                  (GAME.ENABLE_POSTMORTEM_DELAY): 7, 
                                  (GAME.ENABLE_SERVER_AIM): 8, 
                                  (GAME.SHOW_VEHICLES_COUNTER): 9, 
                                  (GAME.SHOW_VECTOR_ON_MAP): 10, 
                                  (GAME.SHOW_SECTOR_ON_MAP): 11, 
                                  (GAME.RECEIVE_FRIENDSHIP_REQUEST): 12, 
                                  (GAME.SNIPER_MODE_STABILIZATION): 13, 
                                  (GAME.DISABLE_BATTLE_CHAT): 28}, offsets={(GAME.REPLAY_ENABLED): (Offset(14, 3 << 14)), 
                                  (GAME.DATE_TIME_MESSAGE_INDEX): (Offset(16, 983040)), 
                                  (GAME.MINIMAP_ALPHA): (Offset(20, 267386880)), 
                                  (GAME.SHOW_VEH_MODELS_ON_MAP): (Offset(29, 3 << 29))})), 
       (SETTINGS_SECTIONS.GAME_EXTENDED): (Section(masks={(GAME.PRE_COMMANDER_CAM): 0, 
                                           (GAME.CHAT_CONTACTS_LIST_ONLY): 1, 
                                           (GAME.RECEIVE_INVITES_IN_BATTLE): 2, 
                                           (GAME.RECEIVE_CLAN_INVITES_NOTIFICATIONS): 3, 
                                           (GAME.MINIMAP_VIEW_RANGE): 6, 
                                           (GAME.MINIMAP_MAX_VIEW_RANGE): 7, 
                                           (GAME.MINIMAP_DRAW_RANGE): 8, 
                                           (GAME.INCREASED_ZOOM): 9, 
                                           (GAME.SNIPER_MODE_BY_SHIFT): 10, 
                                           (GAME.COMMANDER_CAM): 11, 
                                           (GAME.CAROUSEL_TYPE): 12, 
                                           (GAME.DOUBLE_CAROUSEL_TYPE): 13, 
                                           (GAME.VEHICLE_CAROUSEL_STATS): 14, 
                                           (GAME.MINIMAP_ALPHA_ENABLED): 15, 
                                           (GAME.HANGAR_CAM_PARALLAX_ENABLED): 16, 
                                           (GAME.ENABLE_SPEEDOMETER): 23, 
                                           (GAME.DISPLAY_PLATOON_MEMBERS): 24, 
                                           (GAME.MINIMAP_MIN_SPOTTING_RANGE): 25, 
                                           (GAME.ENABLE_REPAIR_TIMER): 26, 
                                           (GAME.ENABLE_BATTLE_NOTIFIER): 29, 
                                           (GAME.HULLLOCK_ENABLED): 30}, offsets={(GAME.BATTLE_LOADING_INFO): (Offset(4, 3 << 4)), 
                                           (GAME.BATTLE_LOADING_RANKED_INFO): (Offset(21, 3 << 21)), 
                                           (GAME.HANGAR_CAM_PERIOD): (Offset(18, 7 << 18)), 
                                           (GAME.SNIPER_ZOOM): (Offset(27, 3 << 27))})), 
       (SETTINGS_SECTIONS.GAME_EXTENDED_2): (Section(masks={(GAME.SHOW_ARTY_HIT_ON_MAP): 0, 
                                             (GAME.GAMEPLAY_ONLY_10_MODE): 1, 
                                             (GAME.SCROLL_SMOOTHING): 4, 
                                             (GAME.GAMEPLAY_DEV_MAPS): 5, 
                                             (GAME.SHOW_THERMAL_VISION_SECTOR_ON_MAP): 6, 
                                             (GAME.ENABLE_THERMAL_VISION_EFFECT): 7, 
                                             (GAME.ENABLE_THERMAL_VISION_SECTOR_EFFECT): 8, 
                                             (GAME.HANGAR_CREW_WIDGET): 9, 
                                             (GAME.ENABLE_BATTLE_CONTEXT_HINTS): 10}, offsets={(GAME.CUSTOMIZATION_DISPLAY_TYPE): (Offset(2, 3 << 2))})), 
       (SETTINGS_SECTIONS.GAMEPLAY): (Section(masks={}, offsets={(GAME.GAMEPLAY_MASK): (Offset(0, 65535))})), 
       (SETTINGS_SECTIONS.GRAPHICS): (Section(masks={(GAME.LENS_EFFECT): 1}, offsets={})), 
       (SETTINGS_SECTIONS.SOUND): (Section(masks={}, offsets={(SOUND.ALT_VOICES): (Offset(0, 255))})), 
       (SETTINGS_SECTIONS.CONTROLS): (Section(masks={(CONTROLS.MOUSE_HORZ_INVERSION): 0, 
                                      (CONTROLS.MOUSE_VERT_INVERSION): 1, 
                                      (CONTROLS.BACK_DRAFT_INVERSION): 2}, offsets={})), 
       (SETTINGS_SECTIONS.AIM_1): (Section(masks={}, offsets={b'net': (Offset(0, 255)), 
                                   b'netType': (Offset(8, 65280)), 
                                   b'centralTag': (Offset(16, 16711680)), 
                                   b'centralTagType': (Offset(24, 4278190080L))})), 
       (SETTINGS_SECTIONS.AIM_2): (Section(masks={}, offsets={b'reloader': (Offset(0, 255)), 
                                   b'condition': (Offset(8, 65280)), 
                                   b'mixing': (Offset(16, 16711680)), 
                                   b'mixingType': (Offset(24, 4278190080L))})), 
       (SETTINGS_SECTIONS.AIM_3): (Section(masks={}, offsets={b'cassette': (Offset(0, 255)), 
                                   b'gunTag': (Offset(8, 65280)), 
                                   b'gunTagType': (Offset(16, 16711680)), 
                                   b'reloaderTimer': (Offset(24, 4278190080L))})), 
       (SETTINGS_SECTIONS.AIM_4): (Section(masks={}, offsets={b'zoomIndicator': (Offset(0, 255))})), 
       (SETTINGS_SECTIONS.SPG_AIM): (Section(masks={(SPGAim.SHOTS_RESULT_INDICATOR): 0, 
                                     (SPGAim.SPG_SCALE_WIDGET): 1, 
                                     (SPGAim.SPG_STRATEGIC_CAM_MODE): 2, 
                                     (SPGAim.AUTO_CHANGE_AIM_MODE): 3}, offsets={(SPGAim.AIM_ENTRANCE_MODE): (Offset(4, 3 << 4))})), 
       (SETTINGS_SECTIONS.CONTOUR): (Section(masks={(CONTOUR.ENHANCED_CONTOUR): 0}, offsets={(CONTOUR.CONTOUR_PENETRABLE_ZONE): (Offset(1, 3 << 1)), 
                                     (CONTOUR.CONTOUR_IMPENETRABLE_ZONE): (Offset(3, 3 << 3))})), 
       (SETTINGS_SECTIONS.MARKERS_1): (Section(masks={b'markerBaseIcon': 0, 
                                       b'markerBaseLevel': 1, 
                                       b'markerBaseHpIndicator': 2, 
                                       b'markerBaseDamage': 3, 
                                       b'markerBaseVehicleName': 4, 
                                       b'markerBasePlayerName': 5, 
                                       b'markerBaseAimMarker2D': 6, 
                                       b'markerAltIcon': 16, 
                                       b'markerAltLevel': 17, 
                                       b'markerAltHpIndicator': 18, 
                                       b'markerAltDamage': 19, 
                                       b'markerAltVehicleName': 20, 
                                       b'markerAltPlayerName': 21, 
                                       b'markerAltAimMarker2D': 22}, offsets={b'markerBaseHp': (Offset(8, 65280)), 
                                       b'markerAltHp': (Offset(24, 4278190080L))})), 
       (SETTINGS_SECTIONS.MARKERS_2): (Section(masks={b'markerBaseVehicleDist': 0, 
                                       b'markerAltVehicleDist': 1}, offsets={})), 
       (SETTINGS_SECTIONS.CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                               b'germany': 1, 
                                               b'usa': 2, 
                                               b'china': 3, 
                                               b'france': 4, 
                                               b'uk': 5, 
                                               b'japan': 6, 
                                               b'czech': 7, 
                                               b'sweden': 8, 
                                               b'poland': 9, 
                                               b'italy': 10, 
                                               b'intunion': 11, 
                                               b'lightTank': 15, 
                                               b'mediumTank': 16, 
                                               b'heavyTank': 17, 
                                               b'SPG': 18, 
                                               b'AT-SPG': 19, 
                                               b'level_1': 20, 
                                               b'level_2': 21, 
                                               b'level_3': 22, 
                                               b'level_4': 23, 
                                               b'level_5': 24, 
                                               b'level_6': 25, 
                                               b'level_7': 26, 
                                               b'level_8': 27, 
                                               b'level_9': 28, 
                                               b'level_10': 29, 
                                               b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                               b'elite': 1, 
                                               b'rented': 2, 
                                               b'igr': 3, 
                                               b'favorite': 5, 
                                               b'bonus': 6, 
                                               b'event': 7, 
                                               b'crystals': 8, 
                                               b'role_HT_assault': 11, 
                                               b'role_HT_break': 12, 
                                               b'role_HT_support': 13, 
                                               b'role_HT_universal': 14, 
                                               b'role_MT_universal': 15, 
                                               b'role_MT_sniper': 16, 
                                               b'role_MT_assault': 17, 
                                               b'role_MT_support': 18, 
                                               b'role_ATSPG_assault': 19, 
                                               b'role_ATSPG_universal': 20, 
                                               b'role_ATSPG_sniper': 21, 
                                               b'role_ATSPG_support': 22, 
                                               b'role_LT_universal': 23, 
                                               b'role_LT_wheeled': 24, 
                                               b'role_SPG': 25, 
                                               b'debut_boxes': 26, 
                                               b'role_SPG_flame': 27, 
                                               b'role_SPG_assault': 28, 
                                               b'early_access': 29, 
                                               b'paragons': 30}, offsets={})), 
       (SETTINGS_SECTIONS.RANKED_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                      b'germany': 1, 
                                                      b'usa': 2, 
                                                      b'china': 3, 
                                                      b'france': 4, 
                                                      b'uk': 5, 
                                                      b'japan': 6, 
                                                      b'czech': 7, 
                                                      b'sweden': 8, 
                                                      b'poland': 9, 
                                                      b'italy': 10, 
                                                      b'intunion': 11, 
                                                      b'lightTank': 15, 
                                                      b'mediumTank': 16, 
                                                      b'heavyTank': 17, 
                                                      b'SPG': 18, 
                                                      b'AT-SPG': 19, 
                                                      b'level_1': 20, 
                                                      b'level_2': 21, 
                                                      b'level_3': 22, 
                                                      b'level_4': 23, 
                                                      b'level_5': 24, 
                                                      b'level_6': 25, 
                                                      b'level_7': 26, 
                                                      b'level_8': 27, 
                                                      b'level_9': 28, 
                                                      b'level_10': 29, 
                                                      b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.RANKED_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                      b'elite': 1, 
                                                      b'rented': 2, 
                                                      b'igr': 3, 
                                                      b'gameMode': 4, 
                                                      b'favorite': 5, 
                                                      b'bonus': 6, 
                                                      b'event': 7, 
                                                      b'crystals': 8, 
                                                      b'ranked': 9, 
                                                      b'role_HT_assault': 11, 
                                                      b'role_HT_break': 12, 
                                                      b'role_HT_support': 13, 
                                                      b'role_HT_universal': 14, 
                                                      b'role_MT_universal': 15, 
                                                      b'role_MT_sniper': 16, 
                                                      b'role_MT_assault': 17, 
                                                      b'role_MT_support': 18, 
                                                      b'role_ATSPG_assault': 19, 
                                                      b'role_ATSPG_universal': 20, 
                                                      b'role_ATSPG_sniper': 21, 
                                                      b'role_ATSPG_support': 22, 
                                                      b'role_LT_universal': 23, 
                                                      b'role_LT_wheeled': 24, 
                                                      b'role_SPG': 25, 
                                                      b'debut_boxes': 26, 
                                                      b'role_SPG_flame': 27, 
                                                      b'role_SPG_assault': 28, 
                                                      b'paragons': 29}, offsets={})), 
       (SETTINGS_SECTIONS.EPICBATTLE_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                          b'germany': 1, 
                                                          b'usa': 2, 
                                                          b'china': 3, 
                                                          b'france': 4, 
                                                          b'uk': 5, 
                                                          b'japan': 6, 
                                                          b'czech': 7, 
                                                          b'sweden': 8, 
                                                          b'poland': 9, 
                                                          b'italy': 10, 
                                                          b'intunion': 11, 
                                                          b'lightTank': 15, 
                                                          b'mediumTank': 16, 
                                                          b'heavyTank': 17, 
                                                          b'SPG': 18, 
                                                          b'AT-SPG': 19, 
                                                          b'level_1': 20, 
                                                          b'level_2': 21, 
                                                          b'level_3': 22, 
                                                          b'level_4': 23, 
                                                          b'level_5': 24, 
                                                          b'level_6': 25, 
                                                          b'level_7': 26, 
                                                          b'level_8': 27, 
                                                          b'level_9': 28, 
                                                          b'level_10': 29, 
                                                          b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.EPICBATTLE_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                          b'elite': 1, 
                                                          b'rented': 2, 
                                                          b'igr': 3, 
                                                          b'gameMode': 4, 
                                                          b'favorite': 5, 
                                                          b'bonus': 6, 
                                                          b'event': 7, 
                                                          b'crystals': 8, 
                                                          b'role_HT_assault': 11, 
                                                          b'role_HT_break': 12, 
                                                          b'role_HT_support': 13, 
                                                          b'role_HT_universal': 14, 
                                                          b'role_MT_universal': 15, 
                                                          b'role_MT_sniper': 16, 
                                                          b'role_MT_assault': 17, 
                                                          b'role_MT_support': 18, 
                                                          b'role_ATSPG_assault': 19, 
                                                          b'role_ATSPG_universal': 20, 
                                                          b'role_ATSPG_sniper': 21, 
                                                          b'role_ATSPG_support': 22, 
                                                          b'role_LT_universal': 23, 
                                                          b'role_LT_wheeled': 24, 
                                                          b'role_SPG': 25, 
                                                          b'role_SPG_flame': 26, 
                                                          b'role_SPG_assault': 27, 
                                                          b'paragons': 28}, offsets={})), 
       (SETTINGS_SECTIONS.BATTLEPASS_CAROUSEL_FILTER_1): (Section(masks={b'isCommonProgression': 0}, offsets={})), 
       (SETTINGS_SECTIONS.COMP7_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                     b'germany': 1, 
                                                     b'usa': 2, 
                                                     b'china': 3, 
                                                     b'france': 4, 
                                                     b'uk': 5, 
                                                     b'japan': 6, 
                                                     b'czech': 7, 
                                                     b'sweden': 8, 
                                                     b'poland': 9, 
                                                     b'italy': 10, 
                                                     b'intunion': 11, 
                                                     b'lightTank': 15, 
                                                     b'mediumTank': 16, 
                                                     b'heavyTank': 17, 
                                                     b'SPG': 18, 
                                                     b'AT-SPG': 19, 
                                                     b'level_1': 20, 
                                                     b'level_2': 21, 
                                                     b'level_3': 22, 
                                                     b'level_4': 23, 
                                                     b'level_5': 24, 
                                                     b'level_6': 25, 
                                                     b'level_7': 26, 
                                                     b'level_8': 27, 
                                                     b'level_9': 28, 
                                                     b'level_10': 29, 
                                                     b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.COMP7_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                     b'elite': 1, 
                                                     b'rented': 2, 
                                                     b'igr': 3, 
                                                     b'gameMode': 4, 
                                                     b'favorite': 5, 
                                                     b'bonus': 6, 
                                                     b'event': 7, 
                                                     b'crystals': 8, 
                                                     b'comp7': 9, 
                                                     b'role_HT_assault': 11, 
                                                     b'role_HT_break': 12, 
                                                     b'role_HT_support': 13, 
                                                     b'role_HT_universal': 14, 
                                                     b'role_MT_universal': 15, 
                                                     b'role_MT_sniper': 16, 
                                                     b'role_MT_assault': 17, 
                                                     b'role_MT_support': 18, 
                                                     b'role_ATSPG_assault': 19, 
                                                     b'role_ATSPG_universal': 20, 
                                                     b'role_ATSPG_sniper': 21, 
                                                     b'role_ATSPG_support': 22, 
                                                     b'role_LT_universal': 23, 
                                                     b'role_LT_wheeled': 24, 
                                                     b'role_SPG': 25, 
                                                     b'debut_boxes': 26, 
                                                     b'role_SPG_flame': 27, 
                                                     b'role_SPG_assault': 28, 
                                                     b'paragons': 29}, offsets={})), 
       (SETTINGS_SECTIONS.GUI_START_BEHAVIOR): (Section(masks={(GuiSettingsBehavior.FREE_XP_INFO_DIALOG_SHOWED): 0, 
                                                (GuiSettingsBehavior.RANKED_WELCOME_VIEW_SHOWED): 1, 
                                                (GuiSettingsBehavior.RANKED_WELCOME_VIEW_STARTED): 2, 
                                                (GuiSettingsBehavior.EPIC_RANDOM_CHECKBOX_CLICKED): 3, 
                                                (GuiSettingsBehavior.CREW_22_WELCOME_SHOWN): 24, 
                                                (GuiSettingsBehavior.DISPLAY_PLATOON_MEMBER_CLICKED): 25, 
                                                (GuiSettingsBehavior.VEH_POST_PROGRESSION_UNLOCK_MSG_NEED_SHOW): 26, 
                                                (GuiSettingsBehavior.BIRTHDAY_CALENDAR_INTRO_SHOWED): 27, 
                                                (GuiSettingsBehavior.RESOURCE_WELL_INTRO_SHOWN): 28, 
                                                (GuiSettingsBehavior.COMP7_WHATS_NEW_SHOWN): 29, 
                                                (GuiSettingsBehavior.COMP7_INTRO_SHOWN): 30, 
                                                (GuiSettingsBehavior.WINBACK_INTRO_SHOWED): 31}, offsets={(GuiSettingsBehavior.COMP7_VERSION_FLAG): (Offset(20, 15 << 20))})), 
       (SETTINGS_SECTIONS.EULA_VERSION): (Section(masks={}, offsets={b'version': (Offset(0, 4294967295L))})), 
       (SETTINGS_SECTIONS.MARKS_ON_GUN): (Section(masks={}, offsets={(GAME.SHOW_MARKS_ON_GUN): (Offset(0, 4294967295L))})), 
       (SETTINGS_SECTIONS.CONTACTS): (Section(masks={(CONTACTS.SHOW_OFFLINE_USERS): 0, 
                                      (CONTACTS.SHOW_OTHERS_CATEGORY): 1}, offsets={(CONTACTS.ANTISPAM_MESSAGES_COUNTER): (Offset(2, 7 << 2))})), 
       (SETTINGS_SECTIONS.FALLOUT): (Section(masks={b'isEnabled': 3, 
                                     b'isAutomatch': 4, 
                                     b'hasVehicleLvl8': 5, 
                                     b'hasVehicleLvl10': 6}, offsets={b'falloutBattleType': (Offset(8, 65280))})), 
       (SETTINGS_SECTIONS.ONCE_ONLY_HINTS): (Section(masks={(OnceOnlyHints.FALLOUT_QUESTS_TAB): 0, 
                                             (OnceOnlyHints.C11N_PROGRESSION_VIEW_HINT): 1, 
                                             (OnceOnlyHints.SHOP_TRADE_IN_HINT): 2, 
                                             (OnceOnlyHints.VEH_COMPARE_CONFIG_HINT): 3, 
                                             (OnceOnlyHints.HOLD_SHEET_HINT): 4, 
                                             (OnceOnlyHints.HAVE_NEW_BADGE_HINT): 5, 
                                             (OnceOnlyHints.EPIC_RESERVES_SLOT_HINT): 6, 
                                             (OnceOnlyHints.SHOW_ABILITIES_BUTTON_HINT): 7, 
                                             (OnceOnlyHints.PAUSE_HINT): 8, 
                                             (OnceOnlyHints.HAVE_NEW_SUFFIX_BADGE_HINT): 9, 
                                             (OnceOnlyHints.BADGE_PAGE_NEW_SUFFIX_BADGE_HINT): 10, 
                                             (OnceOnlyHints.C11N_AUTOPROLONGATION_HINT): 11, 
                                             (OnceOnlyHints.BLUEPRINTS_SWITCHBUTTON_HINT): 12, 
                                             (OnceOnlyHints.BLUEPRINTS_RESEARCH_BUTTON_HINT): 13, 
                                             (OnceOnlyHints.BLUEPRINTS_TECHTREE_CONVERT_BUTTON_HINT): 14, 
                                             (OnceOnlyHints.BLUEPRINTS_RESEARCH_CONVERT_BUTTON_HINT): 15, 
                                             (OnceOnlyHints.BLUEPRINT_SCREEN_CONVERT_FRAGMENT_HINT): 16, 
                                             (OnceOnlyHints.ACCOUNT_BUTTON_HINT): 17, 
                                             (OnceOnlyHints.SESSION_STATS_OPEN_BTN_HINT): 18, 
                                             (OnceOnlyHints.BATTLE_SESSION_UP_BUTTON_TOURNAMENT_HINT): 19, 
                                             (OnceOnlyHints.CREW_OPERATION_BTN_HINT): 20, 
                                             (OnceOnlyHints.SOUND_BUTTONEX_HINT): 21, 
                                             (OnceOnlyHints.SESSION_STATS_SETTINGS_BTN_HINT): 22, 
                                             (OnceOnlyHints.VEHICLE_PREVIEW_MODULES_BUTTON_HINT): 23, 
                                             (OnceOnlyHints.C11N_EDITABLE_STYLES_HINT): 24, 
                                             (OnceOnlyHints.C11N_PROGRESSION_REQUIRED_STYLES_HINT): 25, 
                                             (OnceOnlyHints.C11N_EDITABLE_STYLE_SLOT_HINT): 26, 
                                             (OnceOnlyHints.C11N_EDITABLE_STYLE_SLOT_BUTTON_HINT): 27, 
                                             (OnceOnlyHints.C11N_PROGRESSION_REQUIRED_STYLE_SLOT_HINT): 28, 
                                             (OnceOnlyHints.C11N_PROGRESSION_REQUIRED_STYLE_SLOT_BUTTON_HINT): 29}, offsets={})), 
       (SETTINGS_SECTIONS.ONCE_ONLY_HINTS_2): (Section(masks={(OnceOnlyHints.AMMUNITION_PANEL_HINT): 0, 
                                               (OnceOnlyHints.MODERNIZED_SETUP_TAB_HINT): 1, 
                                               (OnceOnlyHints.OPT_DEV_DRAG_AND_DROP_HINT): 2, 
                                               (OnceOnlyHints.DOGTAG_HANGAR_HINT): 3, 
                                               (OnceOnlyHints.DOGTAG_PROFILE_HINT): 4, 
                                               (OnceOnlyHints.PLATOON_BTN_HINT): 5, 
                                               (OnceOnlyHints.MODE_SELECTOR_WIDGETS_BTN_HINT): 6, 
                                               (OnceOnlyHints.HANGAR_MANUAL_HINT): 7, 
                                               (OnceOnlyHints.MAPS_TRAINING_NEWBIE_HINT): 8, 
                                               (OnceOnlyHints.AMUNNITION_PANEL_EPIC_BATTLE_ABILITIES_HINT): 9, 
                                               (OnceOnlyHints.VEHICLE_PREVIEW_POST_PROGRESSION_BUTTON_HINT): 10, 
                                               (OnceOnlyHints.VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT): 11, 
                                               (OnceOnlyHints.HERO_VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT): 12, 
                                               (OnceOnlyHints.SWITCH_EQUIPMENT_AUXILIARY_LOADOUT_HINT): 13, 
                                               (OnceOnlyHints.SWITCH_EQUIPMENT_ESSENTIALS_LOADOUT_HINT): 14, 
                                               (OnceOnlyHints.COMPARE_MODIFICATIONS_PANEL_HINT): 15, 
                                               (OnceOnlyHints.COMPARE_SPECIALIZATION_BUTTON_HINT): 16, 
                                               (OnceOnlyHints.TRADE_IN_VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT): 17, 
                                               (OnceOnlyHints.PERSONAL_TRADE_IN_VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT): 18, 
                                               (OnceOnlyHints.RESEARCH_POST_PROGRESSION_ENTRY_POINT_HINT): 19, 
                                               (OnceOnlyHints.WOTPLUS_HANGAR_HINT): 20, 
                                               (OnceOnlyHints.WOTPLUS_PROFILE_HINT): 21, 
                                               (OnceOnlyHints.HANGAR_HAVE_NEW_BADGE_HINT): 22, 
                                               (OnceOnlyHints.HANGAR_HAVE_NEW_SUFFIX_BADGE_HINT): 23, 
                                               (OnceOnlyHints.APPLY_ABILITIES_TO_TYPE_CHECKBOX_HINT): 24, 
                                               (OnceOnlyHints.BATTLE_MATTERS_FIGHT_BUTTON_HINT): 25, 
                                               (OnceOnlyHints.BATTLE_MATTERS_ENTRY_POINT_BUTTON_HINT): 26, 
                                               (OnceOnlyHints.PERSONAL_RESERVES_HANGAR_HINT): 27, 
                                               (OnceOnlyHints.PERSONAL_RESERVES_ACTIVATION_HINT): 28, 
                                               (OnceOnlyHints.AMMUNITION_FILTER_HINT): 29, 
                                               (OnceOnlyHints.SUMMARY_CUSTOMIZATION_BUTTON_HINT): 30}, offsets={})), 
       (SETTINGS_SECTIONS.ONCE_ONLY_HINTS_3): (Section(masks={(OnceOnlyHints.BATTLE_SELECTOR_BAR_AI_HINT): 2, 
                                               (OnceOnlyHints.LOOT_PROBABILITY_HINT): 3, 
                                               (OnceOnlyHints.PERSONAL_MISSIONS_OPERATION_HINT): 4, 
                                               (OnceOnlyHints.PM_NEW_CAMPAIGN_HINT): 5, 
                                               (OnceOnlyHints.PARAGONS_FIRST_RESET_HINT): 6, 
                                               (OnceOnlyHints.PARAGONS_ENTRY_POINT_HINT): 7, 
                                               (OnceOnlyHints.PARAGONS_RESEARCH_BUTTON_HINT): 8, 
                                               (OnceOnlyHints.BIRTHDAY_POSTBATTLE_TEAM_STATS_TAB_HINT): 9, 
                                               (OnceOnlyHints.ADD_ECONOMIC_DIRECTIVES_HINT): 10, 
                                               (OnceOnlyHints.EPIC_SUPPLY_INFO_HINT): 11, 
                                               (OnceOnlyHints.COMP7_SKILL_HINT): 12, 
                                               (OnceOnlyHints.TANK_ACADEMY_FIGHT_BUTTON_HINT): 13, 
                                               (OnceOnlyHints.TANK_ACADEMY_ENTRY_POINT_HINT): 14}, offsets={})), 
       (SETTINGS_SECTIONS.DAMAGE_INDICATOR): (Section(masks={(DAMAGE_INDICATOR.TYPE): 0, 
                                              (DAMAGE_INDICATOR.PRESET_CRITS): 1, 
                                              (DAMAGE_INDICATOR.DAMAGE_VALUE): 2, 
                                              (DAMAGE_INDICATOR.VEHICLE_INFO): 3, 
                                              (DAMAGE_INDICATOR.ANIMATION): 4, 
                                              (DAMAGE_INDICATOR.DYNAMIC_INDICATOR): 5, 
                                              (DAMAGE_INDICATOR.PRESET_ALLIES): 6}, offsets={})), 
       (SETTINGS_SECTIONS.DAMAGE_LOG): (Section(masks={(DAMAGE_LOG.TOTAL_DAMAGE): 0, 
                                        (DAMAGE_LOG.BLOCKED_DAMAGE): 1, 
                                        (DAMAGE_LOG.ASSIST_DAMAGE): 2, 
                                        (DAMAGE_LOG.ASSIST_STUN): 3}, offsets={(DAMAGE_LOG.SHOW_DETAILS): (Offset(4, 3 << 4)), 
                                        (DAMAGE_LOG.SHOW_EVENT_TYPES): (Offset(6, 3 << 6)), 
                                        (DAMAGE_LOG.EVENT_POSITIONS): (Offset(8, 3 << 8))})), 
       (SETTINGS_SECTIONS.BATTLE_EVENTS): (Section(masks={(BATTLE_EVENTS.SHOW_IN_BATTLE): 0, 
                                           (BATTLE_EVENTS.ENEMY_HP_DAMAGE): 1, 
                                           (BATTLE_EVENTS.ENEMY_BURNING): 2, 
                                           (BATTLE_EVENTS.ENEMY_RAM_ATTACK): 3, 
                                           (BATTLE_EVENTS.BLOCKED_DAMAGE): 4, 
                                           (BATTLE_EVENTS.ENEMY_DETECTION_DAMAGE): 5, 
                                           (BATTLE_EVENTS.ENEMY_TRACK_DAMAGE): 6, 
                                           (BATTLE_EVENTS.ENEMY_DETECTION): 7, 
                                           (BATTLE_EVENTS.ENEMY_KILL): 8, 
                                           (BATTLE_EVENTS.BASE_CAPTURE_DROP): 9, 
                                           (BATTLE_EVENTS.BASE_CAPTURE): 10, 
                                           (BATTLE_EVENTS.ENEMY_CRITICAL_HIT): 11, 
                                           (BATTLE_EVENTS.EVENT_NAME): 12, 
                                           (BATTLE_EVENTS.VEHICLE_INFO): 13, 
                                           (BATTLE_EVENTS.ENEMY_WORLD_COLLISION): 14, 
                                           (BATTLE_EVENTS.RECEIVED_DAMAGE): 15, 
                                           (BATTLE_EVENTS.RECEIVED_CRITS): 16, 
                                           (BATTLE_EVENTS.ENEMY_ASSIST_STUN): 17, 
                                           (BATTLE_EVENTS.ENEMIES_STUN): 18, 
                                           (BATTLE_EVENTS.HEALTH_ADDED): 20}, offsets={})), 
       (SETTINGS_SECTIONS.BATTLE_BORDER_MAP): (Section(masks={}, offsets={(BATTLE_BORDER_MAP.MODE_SHOW_BORDER): (Offset(0, 3)), 
                                               (BATTLE_BORDER_MAP.TYPE_BORDER): (Offset(2, 3 << 2))})), 
       (SETTINGS_SECTIONS.SIXTH_SENSE): (Section(masks={}, offsets={(SIXTH_SENSE.INDICATOR_SIZE): (Offset(0, 3)), 
                                         (SIXTH_SENSE.INDICATOR_ALPHA): (Offset(3, 1016))})), 
       (SETTINGS_SECTIONS.UI_STORAGE): (Section(masks={(PM_TUTOR_FIELDS.GREETING_SCREEN_SHOWN): 0, 
                                        (PM_TUTOR_FIELDS.FIRST_ENTRY_AWARDS_SHOWN): 1, 
                                        (PM_TUTOR_FIELDS.ONE_FAL_SHOWN): 7, 
                                        (PM_TUTOR_FIELDS.MULTIPLE_FAL_SHOWN): 8, 
                                        (UI_STORAGE_KEYS.AUTO_RELOAD_MARK_IS_SHOWN): 9, 
                                        (UI_STORAGE_KEYS.DISABLE_ANIMATED_TOOLTIP): 13, 
                                        (UI_STORAGE_KEYS.FIELD_POST_HINT_IS_SHOWN): 14, 
                                        (PM_TUTOR_FIELDS.PM2_ONE_FAL_SHOWN): 15, 
                                        (PM_TUTOR_FIELDS.PM2_MULTIPLE_FAL_SHOWN): 16, 
                                        (UI_STORAGE_KEYS.REFERRAL_BUTTON_CIRCLES_SHOWN): 17, 
                                        (UI_STORAGE_KEYS.DUAL_GUN_MARK_IS_SHOWN): 18, 
                                        (UI_STORAGE_KEYS.DISABLE_EDITABLE_STYLE_REWRITE_WARNING): 22, 
                                        (UI_STORAGE_KEYS.TURBOSHAFT_MARK_IS_SHOWN): 26, 
                                        (UI_STORAGE_KEYS.OPTIONAL_DEVICE_SETUP_INTRO_SHOWN): 27, 
                                        (UI_STORAGE_KEYS.EPIC_BATTLE_ABILITIES_INTRO_SHOWN): 28, 
                                        (UI_STORAGE_KEYS.POST_PROGRESSION_INTRO_SHOWN): 29, 
                                        (UI_STORAGE_KEYS.VEH_PREVIEW_POST_PROGRESSION_BULLET_SHOWN): 30}, offsets={(PM_TUTOR_FIELDS.INITIAL_FAL_COUNT): (Offset(2, 124)), 
                                        (UI_STORAGE_KEYS.AUTO_RELOAD_HIGHLIGHTS_COUNTER): (Offset(10, 7168)), 
                                        (UI_STORAGE_KEYS.DUAL_GUN_HIGHLIGHTS_COUNTER): (Offset(19, 3670016)), 
                                        (UI_STORAGE_KEYS.TURBOSHAFT_HIGHLIGHTS_COUNTER): (Offset(23, 58720256))})), 
       (SETTINGS_SECTIONS.UI_STORAGE_2): (Section(masks={(UI_STORAGE_KEYS.ROCKET_ACCELERATION_MARK_IS_SHOWN): 0, 
                                          (UI_STORAGE_KEYS.ACHIEVEMENT_EDIT_VIEW_VISITED): 4, 
                                          (UI_STORAGE_KEYS.GUI_LOOTBOXES_ENTRY_POINT): 5, 
                                          (UI_STORAGE_KEYS.DUAL_ACCURACY_MARK_IS_SHOWN): 9, 
                                          (UI_STORAGE_KEYS.FLAMETHROWER_MARK_IS_SHOWN): 13, 
                                          (UI_STORAGE_KEYS.THERMAL_VISION_MARK_IS_SHOWN): 17, 
                                          (UI_STORAGE_KEYS.AUTO_RELOAD_DUAL_GUN_MARK_IS_SHOWN): 21, 
                                          (UI_STORAGE_KEYS.CLIP_DUAL_GUN_MARK_IS_SHOWN): 25, 
                                          (UI_STORAGE_KEYS.TANK_ACADEMY_WELCOME_SCREEN_SHOWN): 29}, offsets={(UI_STORAGE_KEYS.ROCKET_ACCELERATION_HIGHLIGHTS_COUNTER): (Offset(1, 14)), 
                                          (UI_STORAGE_KEYS.DUAL_ACCURACY_HIGHLIGHTS_COUNTER): (Offset(6, 448)), 
                                          (UI_STORAGE_KEYS.FLAMETHROWER_HIGHLIGHTS_COUNTER): (Offset(10, 7168)), 
                                          (UI_STORAGE_KEYS.THERMAL_VISION_HIGHLIGHTS_COUNTER): (Offset(14, 114688)), 
                                          (UI_STORAGE_KEYS.AUTO_RELOAD_DUAL_GUN_HIGHLIGHTS_COUNTER): (Offset(18, 1835008)), 
                                          (UI_STORAGE_KEYS.CLIP_DUAL_GUN_HIGHLIGHTS_COUNTER): (Offset(22, 29360128)), 
                                          (UI_STORAGE_KEYS.DUAL_GUN_DUAL_ACCURACY_HIGHLIGHTS_COUNTER): (Offset(26, 469762048))})), 
       (SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS): (Section(masks={}, offsets={(BATTLE_MATTERS_KEYS.QUESTS_SHOWN): (Offset(0, 255)), 
                                                   (BATTLE_MATTERS_KEYS.QUEST_PROGRESS): (Offset(8, 4294967040L))})), 
       (SETTINGS_SECTIONS.QUESTS_PROGRESS): (Section(masks={}, offsets={(QUESTS_PROGRESS.VIEW_TYPE): (Offset(0, 3)), 
                                             (QUESTS_PROGRESS.DISPLAY_TYPE): (Offset(2, 3 << 2))})), 
       (SETTINGS_SECTIONS.SESSION_STATS): (Section(masks={(SESSION_STATS.IS_NOT_NEEDED_RESET_STATS_EVERY_DAY): 0, 
                                           (SESSION_STATS.IS_NEEDED_SAVE_CURRENT_TAB): 1, 
                                           (SESSION_STATS.CURRENT_TAB): 2, 
                                           (SESSION_STATS.ECONOMIC_BLOCK_VIEW): 3, 
                                           (SESSION_STATS.SHOW_WTR): 4, 
                                           (SESSION_STATS.SHOW_RATIO_DAMAGE): 5, 
                                           (SESSION_STATS.SHOW_RATIO_KILL): 6, 
                                           (SESSION_STATS.SHOW_WINS): 7, 
                                           (SESSION_STATS.SHOW_AVERAGE_DAMAGE): 8, 
                                           (SESSION_STATS.SHOW_HELP_DAMAGE): 9, 
                                           (SESSION_STATS.SHOW_BLOCKED_DAMAGE): 10, 
                                           (SESSION_STATS.SHOW_AVERAGE_XP): 11, 
                                           (SESSION_STATS.SHOW_WIN_RATE): 12, 
                                           (SESSION_STATS.SHOW_AVERAGE_VEHICLE_LEVEL): 13, 
                                           (SESSION_STATS.SHOW_AVERAGE_FRAGS): 14, 
                                           (SESSION_STATS.SHOW_SURVIVED_RATE): 15, 
                                           (SESSION_STATS.SHOW_SPOTTED): 16, 
                                           (SESSION_STATS.ONLY_ONCE_HINT_SHOWN_FIELD): 17}, offsets={})), 
       (SETTINGS_SECTIONS.BATTLE_PASS_STORAGE): (Section(masks={(BATTLE_PASS.INTRO_SHOWN): 16, 
                                                 (BATTLE_PASS.EXTRA_CHAPTER_FIRST_ENTER): 17, 
                                                 (BATTLE_PASS.EXTRA_CHAPTER_VIDEO_SHOWN): 18, 
                                                 (BATTLE_PASS.EXTRA_CHAPTER_INTRO_SHOWN): 19, 
                                                 (BATTLE_PASS.INTRO_VIDEO_SHOWN): 20}, offsets={(BATTLE_PASS.BUY_ANIMATION_WAS_SHOWN): (Offset(10, 31 << 10)), 
                                                 (BATTLE_PASS.FLAGS_VERSION): (Offset(21, 63 << 21))})), 
       (SETTINGS_SECTIONS.BATTLE_COMM): (Section(masks={(BATTLE_COMM.ENABLE_BATTLE_COMMUNICATION): 0, 
                                         (BATTLE_COMM.SHOW_COM_IN_PLAYER_LIST): 1, 
                                         (BATTLE_COMM.SHOW_STICKY_MARKERS): 2, 
                                         (BATTLE_COMM.SHOW_CALLOUT_MESSAGES): 3, 
                                         (BATTLE_COMM.SHOW_BASE_MARKERS): 4, 
                                         (BATTLE_COMM.SHOW_LOCATION_MARKERS): 5}, offsets={})), 
       (SETTINGS_SECTIONS.DOG_TAGS): (Section(masks={(GAME.SHOW_VICTIMS_DOGTAG): 0, 
                                      (GAME.SHOW_DOGTAG_TO_KILLER): 1}, offsets={})), 
       (SETTINGS_SECTIONS.BATTLE_HUD): (Section(masks={(SCORE_PANEL.SHOW_HP_VALUES): 0, 
                                        (SCORE_PANEL.SHOW_HP_DIFFERENCE): 1, 
                                        (SCORE_PANEL.ENABLE_TIER_GROUPING): 2, 
                                        (SCORE_PANEL.SHOW_HP_BAR): 3}, offsets={(GAME.SHOW_VEHICLE_HP_IN_PLAYERS_PANEL): (Offset(4, 3 << 4)), 
                                        (GAME.SHOW_VEHICLE_HP_IN_MINIMAP): (Offset(6, 3 << 6))})), 
       (SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                      b'germany': 1, 
                                                      b'usa': 2, 
                                                      b'china': 3, 
                                                      b'france': 4, 
                                                      b'uk': 5, 
                                                      b'japan': 6, 
                                                      b'czech': 7, 
                                                      b'sweden': 8, 
                                                      b'poland': 9, 
                                                      b'italy': 10, 
                                                      b'intunion': 11, 
                                                      b'lightTank': 15, 
                                                      b'mediumTank': 16, 
                                                      b'heavyTank': 17, 
                                                      b'SPG': 18, 
                                                      b'AT-SPG': 19, 
                                                      b'level_1': 20, 
                                                      b'level_2': 21, 
                                                      b'level_3': 22, 
                                                      b'level_4': 23, 
                                                      b'level_5': 24, 
                                                      b'level_6': 25, 
                                                      b'level_7': 26, 
                                                      b'level_8': 27, 
                                                      b'level_9': 28, 
                                                      b'level_10': 29, 
                                                      b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                      b'elite': 1, 
                                                      b'rented': 2, 
                                                      b'igr': 3, 
                                                      b'gameMode': 4, 
                                                      b'favorite': 5, 
                                                      b'bonus': 6, 
                                                      b'event': 7, 
                                                      b'crystals': 8, 
                                                      b'battleRoyale': 9}, offsets={})), 
       (SETTINGS_SECTIONS.MAPBOX_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                      b'germany': 1, 
                                                      b'usa': 2, 
                                                      b'china': 3, 
                                                      b'france': 4, 
                                                      b'uk': 5, 
                                                      b'japan': 6, 
                                                      b'czech': 7, 
                                                      b'sweden': 8, 
                                                      b'poland': 9, 
                                                      b'italy': 10, 
                                                      b'intunion': 11, 
                                                      b'lightTank': 15, 
                                                      b'mediumTank': 16, 
                                                      b'heavyTank': 17, 
                                                      b'SPG': 18, 
                                                      b'AT-SPG': 19, 
                                                      b'level_1': 20, 
                                                      b'level_2': 21, 
                                                      b'level_3': 22, 
                                                      b'level_4': 23, 
                                                      b'level_5': 24, 
                                                      b'level_6': 25, 
                                                      b'level_7': 26, 
                                                      b'level_8': 27, 
                                                      b'level_9': 28, 
                                                      b'level_10': 29, 
                                                      b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.MAPBOX_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                      b'elite': 1, 
                                                      b'rented': 2, 
                                                      b'igr': 3, 
                                                      b'gameMode': 4, 
                                                      b'favorite': 5, 
                                                      b'bonus': 6, 
                                                      b'event': 7, 
                                                      b'crystals': 8, 
                                                      b'role_HT_assault': 11, 
                                                      b'role_HT_break': 12, 
                                                      b'role_HT_support': 13, 
                                                      b'role_HT_universal': 14, 
                                                      b'role_MT_universal': 15, 
                                                      b'role_MT_sniper': 16, 
                                                      b'role_MT_assault': 17, 
                                                      b'role_MT_support': 18, 
                                                      b'role_ATSPG_assault': 19, 
                                                      b'role_ATSPG_universal': 20, 
                                                      b'role_ATSPG_sniper': 21, 
                                                      b'role_ATSPG_support': 22, 
                                                      b'role_LT_universal': 23, 
                                                      b'role_LT_wheeled': 24, 
                                                      b'role_SPG': 25, 
                                                      b'role_SPG_flame': 26, 
                                                      b'role_SPG_assault': 27}, offsets={})), 
       (SETTINGS_SECTIONS.UNIT_FILTER): (Section(masks={}, offsets={(GAME.UNIT_FILTER): (Offset(0, 4095))})), 
       (SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                          b'germany': 1, 
                                                          b'usa': 2, 
                                                          b'china': 3, 
                                                          b'france': 4, 
                                                          b'uk': 5, 
                                                          b'japan': 6, 
                                                          b'czech': 7, 
                                                          b'sweden': 8, 
                                                          b'poland': 9, 
                                                          b'italy': 10, 
                                                          b'intunion': 11, 
                                                          b'lightTank': 15, 
                                                          b'mediumTank': 16, 
                                                          b'heavyTank': 17, 
                                                          b'SPG': 18, 
                                                          b'AT-SPG': 19, 
                                                          b'level_1': 20, 
                                                          b'level_2': 21, 
                                                          b'level_3': 22, 
                                                          b'level_4': 23, 
                                                          b'level_5': 24, 
                                                          b'level_6': 25, 
                                                          b'level_7': 26, 
                                                          b'level_8': 27, 
                                                          b'level_9': 28, 
                                                          b'level_10': 29, 
                                                          b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                          b'elite': 1, 
                                                          b'rented': 2, 
                                                          b'igr': 3, 
                                                          b'gameMode': 4, 
                                                          b'favorite': 5, 
                                                          b'bonus': 6, 
                                                          b'event': 7, 
                                                          b'crystals': 8, 
                                                          b'funRandom': 9, 
                                                          b'role_HT_assault': 11, 
                                                          b'role_HT_break': 12, 
                                                          b'role_HT_support': 13, 
                                                          b'role_HT_universal': 14, 
                                                          b'role_MT_universal': 15, 
                                                          b'role_MT_sniper': 16, 
                                                          b'role_MT_assault': 17, 
                                                          b'role_MT_support': 18, 
                                                          b'role_ATSPG_assault': 19, 
                                                          b'role_ATSPG_universal': 20, 
                                                          b'role_ATSPG_sniper': 21, 
                                                          b'role_ATSPG_support': 22, 
                                                          b'role_LT_universal': 23, 
                                                          b'role_LT_wheeled': 24, 
                                                          b'role_SPG': 25, 
                                                          b'role_SPG_flame': 26, 
                                                          b'role_SPG_assault': 27, 
                                                          b'paragons': 29}, offsets={})), 
       (SETTINGS_SECTIONS.LIMITED_UI_1): (Section(masks={(LuiRules.LOBBY_HEADER_COUNTERS_STORE): 0, 
                                          (LuiRules.LOBBY_HEADER_COUNTERS_PROFILE): 1, 
                                          (LuiRules.PROFILE_HOF): 2, 
                                          (LuiRules.PROFILE_TECHNIQUE_PAGE): 3, 
                                          (LuiRules.SESSION_STATS): 4, 
                                          (LuiRules.BLUEPRINTS_BUTTON): 5, 
                                          (LuiRules.LOBBY_HEADER_COUNTERS_MISSIONS): 6, 
                                          (LuiRules.MISSIONS_MARATHON_VIEW): 7, 
                                          (LuiRules.LOBBY_HEADER_COUNTERS_PM_OPERATIONS): 8, 
                                          (LuiRules.AP_ZONE_HINT): 9, 
                                          (LuiRules.AP_BATTLE_ABILITIES_HINT): 10, 
                                          (LuiRules.C7N_BUBBLE): 11, 
                                          (LuiRules.TECH_TREE_EVENTS): 12, 
                                          (LuiRules.DOG_TAG_HINT): 13, 
                                          (LuiRules.MODE_SELECTOR_WIDGET_BTN_HINT): 14, 
                                          (LuiRules.PR_HANGAR_HINT): 15, 
                                          (LuiRules.MODERNIZE_SETUP_HINT): 16, 
                                          (LuiRules.OFFER_BANNER_WINDOW): 17, 
                                          (LuiRules.COMP7_ENTRY_POINT): 18, 
                                          (LuiRules.BP_ENTRY): 19, 
                                          (LuiRules.PROGRESSIVE_ITEMS_REWARD): 20, 
                                          (LuiRules.DAILY_MISSIONS): 21, 
                                          (LuiRules.CRAFT_MACHINE_ENTRY_POINT): 22, 
                                          (LuiRules.MAPBOX_ENTRY_POINT): 23, 
                                          (LuiRules.EPIC_BATTLES_ENTRY_POINT): 24, 
                                          (LuiRules.BATTLE_MISSIONS): 25, 
                                          (LuiRules.BLACK_MARKET_ENTRY_POINT): 26, 
                                          (LuiRules.HERO_TANK): 27, 
                                          (LuiRules.BM_FLAG): 28, 
                                          (LuiRules.PERSONAL_MISSIONS): 29, 
                                          (LuiRules.SYS_MSG_COLLECTION_START_BP): 30, 
                                          (LuiRules.LOBBY_HEADER_COUNTERS_STORAGE): 31}, offsets={})), 
       (SETTINGS_SECTIONS.LIMITED_UI_2): (Section(masks={(LuiRules.PR_HANGAR_BUTTON): 0, 
                                          (LuiRules.STRONGHOLD_ENTRY_POINT): 1, 
                                          (LuiRules.BR_ENTRY_POINT): 2, 
                                          (LuiRules.FUN_RANDOM_ENTRY_POINT): 3, 
                                          (LuiRules.FUN_RANDOM_NOTIFICATIONS): 4, 
                                          (LuiRules.SYS_MSG_COLLECTIONS_UPDATED_ENTRY): 5, 
                                          (LuiRules.GUI_LOOTBOXES_ENTRY_POINT): 6, 
                                          (LuiRules.ARMORY_YARD_ENTRY_POINT): 7, 
                                          (LuiRules.RESOURCE_WELL): 8, 
                                          (LuiRules.GUI_COSMIC_ENTRY_POINT): 9, 
                                          (LuiRules.SHOP_SALES_ENTRY_POINT): 10, 
                                          (LuiRules.UNIVERSAL_FLAG_ENTRY_POINT): 11, 
                                          (LuiRules.SUBSCRIPTION_STATE): 12, 
                                          (LuiRules.EARLY_ACCESS_ENTRY_POINT): 13, 
                                          (LuiRules.NEW_CAMPAIGN_HINT): 14, 
                                          (LuiRules.PARAGONS_ENTRY_POINT): 15, 
                                          (LuiRules.PARAGONS_TREE_BRANCHES): 16, 
                                          (LuiRules.PARAGONS_NOTIFICATION): 17, 
                                          (LuiRules.TEASER): 18, 
                                          (LuiRules.COMMON_CHAT): 19, 
                                          (LuiRules.CHANNELS): 20, 
                                          (LuiRules.PERSONAL_MISSIONS_CONTENT): 21, 
                                          (LuiRules.TOURNAMENTS_CONTENT): 22, 
                                          (LuiRules.VERSUS_AI_CONTENT): 23, 
                                          (LuiRules.STRONGHOLD_CONTENT): 24, 
                                          (LuiRules.PARAGONS_BUTTONS): 25, 
                                          (LuiRules.RANKED_CONTENT): 26, 
                                          (LuiRules.COMP7_CONTENT): 27, 
                                          (LuiRules.SPEC_BATTLE_CONTENT): 28, 
                                          (LuiRules.ARCADE_CONTENT): 29, 
                                          (LuiRules.FIELD_TRIALS_CONTENT): 30, 
                                          (LuiRules.FRONTLINE_CONTENT): 31}, offsets={})), 
       (SETTINGS_SECTIONS.ARMORY_YARD): (Section(masks={}, offsets={(ARMORY_YARD_KEYS.BUILD_PROGRESS): (Offset(0, 255)), 
                                         (ARMORY_YARD_KEYS.CURRENT_SEASON): (Offset(8, 4294967040L))})), 
       (SETTINGS_SECTIONS.NEW_YEAR): (Section(masks={(NewYearStorageKeys.HAS_TOYS_HINT_SHOWN): 0, 
                                      (NewYearStorageKeys.NY_FIRST_ENTRANCE): 1, 
                                      (NewYearStorageKeys.NY_WELCOME_NOTIFICATION): 2, 
                                      (NewYearStorageKeys.NY_PET_TOYS_REMOVED): 3, 
                                      (NewYearStorageKeys.NY_FIRST_QUEST_VIDEO_VISITED): 4, 
                                      (NewYearStorageKeys.DECORATIONS_POPOVER_VIEWED): 9, 
                                      (NewYearStorageKeys.DECORATIONS_POPOVER_BROKEN): 10}, offsets={(NewYearStorageKeys.NY_FIRST_QUEST_ENTRANCE): (Offset(11, 63 << 11))})), 
       (SETTINGS_SECTIONS.VERSUS_AI_CAROUSEL_FILTER_1): (Section(masks={b'ussr': 0, 
                                                         b'germany': 1, 
                                                         b'usa': 2, 
                                                         b'china': 3, 
                                                         b'france': 4, 
                                                         b'uk': 5, 
                                                         b'japan': 6, 
                                                         b'czech': 7, 
                                                         b'sweden': 8, 
                                                         b'poland': 9, 
                                                         b'italy': 10, 
                                                         b'intunion': 11, 
                                                         b'lightTank': 15, 
                                                         b'mediumTank': 16, 
                                                         b'heavyTank': 17, 
                                                         b'SPG': 18, 
                                                         b'AT-SPG': 19, 
                                                         b'level_1': 20, 
                                                         b'level_2': 21, 
                                                         b'level_3': 22, 
                                                         b'level_4': 23, 
                                                         b'level_5': 24, 
                                                         b'level_6': 25, 
                                                         b'level_7': 26, 
                                                         b'level_8': 27, 
                                                         b'level_9': 28, 
                                                         b'level_10': 29, 
                                                         b'level_11': 30}, offsets={})), 
       (SETTINGS_SECTIONS.VERSUS_AI_CAROUSEL_FILTER_2): (Section(masks={b'premium': 0, 
                                                         b'elite': 1, 
                                                         b'rented': 2, 
                                                         b'igr': 3, 
                                                         b'gameMode': 4, 
                                                         b'favorite': 5, 
                                                         b'bonus': 6, 
                                                         b'event': 7, 
                                                         b'crystals': 8, 
                                                         b'role_HT_assault': 11, 
                                                         b'role_HT_break': 12, 
                                                         b'role_HT_support': 13, 
                                                         b'role_HT_universal': 14, 
                                                         b'role_MT_universal': 15, 
                                                         b'role_MT_sniper': 16, 
                                                         b'role_MT_assault': 17, 
                                                         b'role_MT_support': 18, 
                                                         b'role_ATSPG_assault': 19, 
                                                         b'role_ATSPG_universal': 20, 
                                                         b'role_ATSPG_sniper': 21, 
                                                         b'role_ATSPG_support': 22, 
                                                         b'role_LT_universal': 23, 
                                                         b'role_LT_wheeled': 24, 
                                                         b'role_SPG': 25, 
                                                         b'role_SPG_flame': 26, 
                                                         b'role_SPG_assault': 27, 
                                                         b'paragons': 29}, offsets={})), 
       (SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS): (Section(masks={}, offsets={(BATTLE_CONTEXT_HINTS.PLAYER_VEHICLE_OBSERVED): (Offset(0, 31)), 
                                                  (BATTLE_CONTEXT_HINTS.KILLED_WHILE_OBSERVED): (Offset(5, 127 << 5)), 
                                                  (BATTLE_CONTEXT_HINTS.IN_SAFETY_WHILE_NOT_OBSERVED): (Offset(12, 15 << 12)), 
                                                  (BATTLE_CONTEXT_HINTS.ENGINE_DAMAGE_REPAIR_KIT): (Offset(16, 7 << 16)), 
                                                  (BATTLE_CONTEXT_HINTS.AMMUNITION_DAMAGE_REPAIR_KIT): (Offset(19, 7 << 19)), 
                                                  (BATTLE_CONTEXT_HINTS.FUELTANK_DAMAGE_REPAIR_KIT): (Offset(22, 7 << 22)), 
                                                  (BATTLE_CONTEXT_HINTS.GUN_ROTATOR_DAMAGE_REPAIR_KIT): (Offset(25, 7 << 25)), 
                                                  (BATTLE_CONTEXT_HINTS.GUN_DAMAGE_REPAIR_KIT): (Offset(28, 7 << 28))})), 
       (SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS_2): (Section(masks={}, offsets={(BATTLE_CONTEXT_HINTS.AMMUNITION_CRIT): (Offset(0, 7)), 
                                                    (BATTLE_CONTEXT_HINTS.FUELTANK_CRIT): (Offset(3, 7 << 3)), 
                                                    (BATTLE_CONTEXT_HINTS.GUN_ROTATOR_DESTROY_REPAIR_KIT): (Offset(6, 7 << 6)), 
                                                    (BATTLE_CONTEXT_HINTS.ENGINE_DESTROY_REPAIR_KIT): (Offset(9, 7 << 9)), 
                                                    (BATTLE_CONTEXT_HINTS.GUN_DESTROY_REPAIR_KIT): (Offset(12, 7 << 12)), 
                                                    (BATTLE_CONTEXT_HINTS.TRACK_DESTROY_REPAIR_KIT): (Offset(15, 7 << 15)), 
                                                    (BATTLE_CONTEXT_HINTS.MODULE_DAMAGE): (Offset(18, 3 << 18)), 
                                                    (BATTLE_CONTEXT_HINTS.COMMANDER_DAMAGE_MED_KIT): (Offset(20, 7 << 20)), 
                                                    (BATTLE_CONTEXT_HINTS.DRIVER_DAMAGE_MED_KIT): (Offset(23, 7 << 23)), 
                                                    (BATTLE_CONTEXT_HINTS.GUNNER_DAMAGE_MED_KIT): (Offset(26, 7 << 26)), 
                                                    (BATTLE_CONTEXT_HINTS.LOADER_DAMAGE_MED_KIT): (Offset(29, 7 << 29))})), 
       (SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS_3): (Section(masks={}, offsets={(BATTLE_CONTEXT_HINTS.RADIOMAN_DAMAGE_MED_KIT): (Offset(0, 7)), 
                                                    (BATTLE_CONTEXT_HINTS.AMMO_TYPE_AVAILABLE): (Offset(3, 7 << 3)), 
                                                    (BATTLE_CONTEXT_HINTS.AMMO_TYPE_SWITCH): (Offset(6, 127 << 6))})), 
       (SETTINGS_SECTIONS.LOOT_BOX_VIEWED): (Section(masks={}, offsets={(WTLootBoxesViewedKeys.HUNTER_LAST_VIEWED): (Offset(0, 65535)), 
                                             (WTLootBoxesViewedKeys.BOSS_LAST_VIEWED): (Offset(16, 4294901760L))}))}
    AIM_MAPPING = {b'net': 1, 
       b'netType': 1, 
       b'centralTag': 1, 
       b'centralTagType': 1, 
       b'reloader': 2, 
       b'condition': 2, 
       b'mixing': 2, 
       b'mixingType': 2, 
       b'cassette': 3, 
       b'gunTag': 3, 
       b'gunTagType': 3, 
       b'reloaderTimer': 3, 
       b'zoomIndicator': 4}
    MARKERS_MAPPING = {b'markerBaseIcon': 1, 
       b'markerBaseLevel': 1, 
       b'markerBaseHpIndicator': 1, 
       b'markerBaseDamage': 1, 
       b'markerBaseVehicleName': 1, 
       b'markerBasePlayerName': 1, 
       b'markerBaseAimMarker2D': 1, 
       b'markerAltIcon': 1, 
       b'markerAltLevel': 1, 
       b'markerAltHpIndicator': 1, 
       b'markerAltDamage': 1, 
       b'markerAltVehicleName': 1, 
       b'markerAltPlayerName': 1, 
       b'markerAltAimMarker2D': 1, 
       b'markerBaseHp': 1, 
       b'markerAltHp': 1, 
       b'markerBaseVehicleDist': 2, 
       b'markerAltVehicleDist': 2}
    _MAX_AUTO_RELOAD_HIGHLIGHTS_COUNT = 5
    _MAX_DUAL_GUN_HIGHLIGHTS_COUNT = 5
    _MAX_TURBOSHAFT_HIGHLIGHTS_COUNT = 5
    _MAX_ROCKET_ACCELERATION_HIGHLIGHTS_COUNT = 5
    _MAX_DUAL_ACCURACY_HIGHLIGHTS_COUNT = 5
    _MAX_FLAMETHROWER_HIGHLIGHTS_COUNT = 5
    _MAX_THERMAL_VISION_HIGHLIGHTS_COUNT = 5
    _MAX_AUTO_RELOAD_DUAL_GUN_HIGHLIGHTS_COUNT = 5
    _MAX_CLIP_DUAL_GUN_HIGHLIGHTS_COUNT = 5
    _MAX_DUAL_GUN_DUAL_ACCURACY_HIGHLIGHTS_COUNT = 5

    def __init__(self, core):
        self._core = weakref.proxy(core)
        return

    @adisp_process
    def applySettings(self):
        import BattleReplay
        if not BattleReplay.isPlaying():
            yield self._updateToVersion()
        self._core.options.refresh()
        enableDynamicCamera = self._core.options.getSetting(self.GAME.DYNAMIC_CAMERA)
        enableDynamicCameraValue = enableDynamicCamera.get()
        enableSniperStabilization = self._core.options.getSetting(self.GAME.SNIPER_MODE_STABILIZATION)
        enableSniperStabilizationValue = enableSniperStabilization.get()
        enableSniperHullLock = self._core.options.getSetting(self.GAME.HULLLOCK_ENABLED)
        enableSniperHullLockValue = enableSniperHullLock.get()
        from AvatarInputHandler import AvatarInputHandler
        AvatarInputHandler.enableDynamicCamera(enableDynamicCameraValue, enableSniperStabilizationValue)
        AvatarInputHandler.enableHullLock(enableSniperHullLockValue)
        if not BattleReplay.isPlaying():
            from messenger.doc_loaders import user_prefs
            from messenger import g_settings as messenger_settings
            user_prefs.loadFromServer(messenger_settings)
        self._core.storages.get(b'FOV').apply(False, True)
        return

    def getAimSetting(self, section, key, default=None):
        number = self.AIM_MAPPING[key]
        storageKey = (b'AIM_{section}_{number}').format(section=section.upper(), number=number)
        settingsKey = (b'AIM_{number}').format(number=number)
        storedValue = self.settingsCache.getSectionSettings(storageKey, None)
        masks = self.SECTIONS[settingsKey].masks
        offsets = self.SECTIONS[settingsKey].offsets
        if storedValue is not None:
            return self._extractValue(key, storedValue, default, masks, offsets)
        else:
            return default

    def getOnceOnlyHintsSetting(self, key, default=None):
        if not self.settingsCache.isSynced():
            return default
        for onlyHintSection in SETTINGS_SECTIONS.ONCE_ONLY_HINTS_GROUP:
            if self._hasKeyInSection(onlyHintSection, key):
                return self.getSectionSettings(onlyHintSection, key, default)

        LOG_ERROR(b'Trying to extract unsupported key in once only hints group: ', key)
        return default

    def getOnceOnlyHintsSettings(self):
        return self.getSections(SETTINGS_SECTIONS.ONCE_ONLY_HINTS_GROUP)

    def setOnceOnlyHintsSettings(self, settings):
        settingToServer = {}
        onceOnlyHintsDiff = {}
        for section in SETTINGS_SECTIONS.ONCE_ONLY_HINTS_GROUP:
            keys = self.SECTIONS[section].masks.keys() + self.SECTIONS[section].offsets.keys()
            currentSettings = {key: value for key, value in settings.items() if key in keys}
            storedSettings = self.getSection(section)
            stored = self.settingsCache.getSectionSettings(section, None)
            storing = self._buildSectionSettings(section, currentSettings)
            if stored != storing:
                settingToServer[section] = storing
                for k, v in currentSettings.iteritems():
                    if storedSettings.get(k) != v:
                        onceOnlyHintsDiff[k] = v

        if settingToServer:
            self.setSettings(settingToServer)
        if onceOnlyHintsDiff:
            self._core.onOnceOnlyHintsChanged(onceOnlyHintsDiff)
        return

    def getUIStorage(self, defaults=None):
        return self.getSection(SETTINGS_SECTIONS.UI_STORAGE, defaults)

    def saveInUIStorage(self, fields):
        return self.setSections([SETTINGS_SECTIONS.UI_STORAGE], fields)

    def getNewYearStorage(self, defaults=None):
        if self.settingsCache.isSynced():
            return self.getSection(SETTINGS_SECTIONS.NEW_YEAR, defaults)
        return {}

    def saveInNewYearStorage(self, settings):
        return self.setSectionSettings(SETTINGS_SECTIONS.NEW_YEAR, settings)

    def getUIStorage2(self, defaults=None):
        return self.getSection(SETTINGS_SECTIONS.UI_STORAGE_2, defaults)

    def saveInUIStorage2(self, fields):
        return self.setSections([SETTINGS_SECTIONS.UI_STORAGE_2], fields)

    def getBPStorage(self, defaults=None):
        if not self.settingsCache.isSynced():
            return {}
        return self.getSection(SETTINGS_SECTIONS.BATTLE_PASS_STORAGE, defaults)

    def updateBPStorageData(self, data, defaults=None):
        if updateBattlePassSettings(data):
            self.saveInBPStorage(data)
        return

    def saveInBPStorage(self, settings):
        if self.settingsCache.isSynced():
            self.setSectionSettings(SETTINGS_SECTIONS.BATTLE_PASS_STORAGE, settings)
        return

    def checkAutoReloadHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.AUTO_RELOAD_HIGHLIGHTS_COUNTER, self._MAX_AUTO_RELOAD_HIGHLIGHTS_COUNT, increase)

    def checkDualGunHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.DUAL_GUN_HIGHLIGHTS_COUNTER, self._MAX_DUAL_GUN_HIGHLIGHTS_COUNT, increase)

    def checkTurboshaftHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.TURBOSHAFT_HIGHLIGHTS_COUNTER, self._MAX_TURBOSHAFT_HIGHLIGHTS_COUNT, increase)

    def checkRocketAccelerationHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.ROCKET_ACCELERATION_HIGHLIGHTS_COUNTER, self._MAX_ROCKET_ACCELERATION_HIGHLIGHTS_COUNT, increase)

    def checkDualAccuracyHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.DUAL_ACCURACY_HIGHLIGHTS_COUNTER, self._MAX_DUAL_ACCURACY_HIGHLIGHTS_COUNT, increase)

    def checkDualGunDualAccuracyHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.DUAL_GUN_DUAL_ACCURACY_HIGHLIGHTS_COUNTER, self._MAX_DUAL_GUN_DUAL_ACCURACY_HIGHLIGHTS_COUNT, increase)

    def checkFlamethrowerHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.FLAMETHROWER_HIGHLIGHTS_COUNTER, self._MAX_FLAMETHROWER_HIGHLIGHTS_COUNT, increase)

    def checkThermalVisionHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.THERMAL_VISION_HIGHLIGHTS_COUNTER, self._MAX_THERMAL_VISION_HIGHLIGHTS_COUNT, increase)

    def checkAutoReloadDualGunHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.AUTO_RELOAD_DUAL_GUN_HIGHLIGHTS_COUNTER, self._MAX_AUTO_RELOAD_DUAL_GUN_HIGHLIGHTS_COUNT, increase)

    def checkClipDualGunHighlights(self, increase=False):
        return self.__checkUIHighlights(UI_STORAGE_KEYS.CLIP_DUAL_GUN_HIGHLIGHTS_COUNTER, self._MAX_CLIP_DUAL_GUN_HIGHLIGHTS_COUNT, increase)

    def updateUIStorageCounter(self, key, step=1):
        storageSection = self.getSection(SETTINGS_SECTIONS.UI_STORAGE)
        if key in storageSection:
            self.saveInUIStorage({key: (storageSection[key] + step)})
        else:
            storageSection = self.getSection(SETTINGS_SECTIONS.UI_STORAGE_2)
            if key in storageSection:
                self.saveInUIStorage2({key: (storageSection[key] + step)})
        return

    def setDisableAnimTooltipFlag(self):
        self.saveInUIStorage({(UI_STORAGE_KEYS.DISABLE_ANIMATED_TOOLTIP): 1})
        return

    def getDisableAnimTooltipFlag(self):
        return self.getUIStorage().get(UI_STORAGE_KEYS.DISABLE_ANIMATED_TOOLTIP) == 1

    def isTankAcademyWelcomeScreenShown(self):
        return self.getUIStorage2().get(UI_STORAGE_KEYS.TANK_ACADEMY_WELCOME_SCREEN_SHOWN) == 1

    def setTankAcademyWelcomeScreenShown(self):
        self.saveInUIStorage2({(UI_STORAGE_KEYS.TANK_ACADEMY_WELCOME_SCREEN_SHOWN): 1})
        return

    def getBattleMattersQuestWasShowed(self):
        return self.getSectionSettings(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, BATTLE_MATTERS_KEYS.QUESTS_SHOWN, 0)

    def setBattleMattersQuestWasShowed(self, count):
        return self.setSectionSettings(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, {(BATTLE_MATTERS_KEYS.QUESTS_SHOWN): count})

    def getBattleMattersQuestProgress(self):
        return self.getSectionSettings(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, BATTLE_MATTERS_KEYS.QUEST_PROGRESS, 0)

    def setBattleMattersQuestProgress(self, lastSeenProgress):
        self.setSectionSettings(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, {(BATTLE_MATTERS_KEYS.QUEST_PROGRESS): lastSeenProgress})
        return

    def getLimitedUIProgress(self, ruleID, default=None):
        if not self.settingsCache.isSynced():
            return False
        for limitedUISection in SETTINGS_SECTIONS.LIMITED_UI_GROUP:
            if self._hasKeyInSection(limitedUISection, ruleID):
                return self.getSectionSettings(limitedUISection, ruleID, default)

        LOG_ERROR(b'Trying to extract unsupported key in limited ui group: ', ruleID)
        return default

    def setLimitedUIProgress(self, ruleIDs):
        if not self.settingsCache.isSynced():
            return False
        else:
            settingToServer = {}
            for section in SETTINGS_SECTIONS.LIMITED_UI_GROUP:
                keys = self.SECTIONS[section].masks.keys() + self.SECTIONS[section].offsets.keys()
                currentSettings = {ruleID: True for ruleID in ruleIDs if ruleID in keys}
                stored = self.settingsCache.getSectionSettings(section, None)
                storing = self._buildSectionSettings(section, currentSettings)
                if stored != storing:
                    settingToServer[section] = storing

            if settingToServer:
                self.setSettings(settingToServer)
            return True

    def setLimitedUIFullComplete(self):
        settings = {storage: 4294967295L for storage in SETTINGS_SECTIONS.LIMITED_UI_GROUP}
        self.setSettings(settings)
        return

    def setQuestProgressSettings(self, settings):
        self.setSectionSettings(SETTINGS_SECTIONS.QUESTS_PROGRESS, settings)
        return

    def getArmoryYardProgress(self):
        return self.getSectionSettings(SETTINGS_SECTIONS.ARMORY_YARD, ARMORY_YARD_KEYS.BUILD_PROGRESS, 0)

    def setArmoryYardProgress(self, lastSeenProgress):
        self.setSectionSettings(SETTINGS_SECTIONS.ARMORY_YARD, {(ARMORY_YARD_KEYS.BUILD_PROGRESS): lastSeenProgress})
        return

    def getArmoryYardSeason(self):
        return self.getSectionSettings(SETTINGS_SECTIONS.ARMORY_YARD, ARMORY_YARD_KEYS.CURRENT_SEASON, 0)

    def setArmoryYardSeason(self, seasonID):
        self.setSectionSettings(SETTINGS_SECTIONS.ARMORY_YARD, {(ARMORY_YARD_KEYS.CURRENT_SEASON): seasonID})
        return

    def _buildAimSettings(self, settings):
        settingToServer = {}
        for section, options in settings.iteritems():
            mapping = {}
            for key, value in options.iteritems():
                number = self.AIM_MAPPING[key]
                mapping.setdefault(number, {})[key] = value

            for number, value in mapping.iteritems():
                settingsKey = (b'AIM_{number}').format(number=number)
                storageKey = (b'AIM_{section}_{number}').format(section=section.upper(), number=number)
                storingValue = storedValue = self.settingsCache.getSetting(storageKey)
                masks = self.SECTIONS[settingsKey].masks
                offsets = self.SECTIONS[settingsKey].offsets
                storingValue = self._mapValues(value, storingValue, masks, offsets)
                if storedValue == storingValue:
                    continue
                settingToServer[storageKey] = storingValue

        return settingToServer

    def setAimSettings(self, settings):
        storingValue = self._buildAimSettings(settings)
        if not storingValue:
            return
        self.settingsCache.setSettings(storingValue)
        LOG_DEBUG(b'Applying AIM server settings: ', settings)
        self._core.onSettingsChanged(settings)
        return

    def getMarkersSetting(self, section, key, default=None):
        number = self.MARKERS_MAPPING[key]
        storageKey = (b'MARKERS_{section}_{number}').format(section=section.upper(), number=number)
        settingsKey = (b'MARKERS_{number}').format(number=number)
        storedValue = self.settingsCache.getSectionSettings(storageKey, None)
        masks = self.SECTIONS[settingsKey].masks
        offsets = self.SECTIONS[settingsKey].offsets
        if storedValue is not None:
            return self._extractValue(key, storedValue, default, masks, offsets)
        else:
            return default

    def _buildMarkersSettings(self, settings):
        settingToServer = {}
        for section, options in settings.iteritems():
            mapping = {}
            for key, value in options.iteritems():
                number = self.MARKERS_MAPPING[key]
                mapping.setdefault(number, {})[key] = value

            for number, value in mapping.iteritems():
                settingsKey = (b'MARKERS_{number}').format(number=number)
                storageKey = (b'MARKERS_{section}_{number}').format(section=section.upper(), number=number)
                storingValue = storedValue = self.settingsCache.getSetting(storageKey)
                masks = self.SECTIONS[settingsKey].masks
                offsets = self.SECTIONS[settingsKey].offsets
                storingValue = self._mapValues(value, storingValue, masks, offsets)
                if storedValue == storingValue:
                    continue
                settingToServer[storageKey] = storingValue

        return settingToServer

    def setMarkersSettings(self, settings):
        storingValue = self._buildMarkersSettings(settings)
        if not storingValue:
            return
        self.settingsCache.setSettings(storingValue)
        LOG_DEBUG(b'Applying MARKER server settings: ', settings)
        self._core.onSettingsChanged(settings)
        return

    def setSessionStatsSettings(self, settings):
        self.setSectionSettings(SETTINGS_SECTIONS.SESSION_STATS, settings)
        return

    def getSessionStatsSettings(self):
        return self.getSection(SETTINGS_SECTIONS.SESSION_STATS)

    def getVersion(self):
        return self.settingsCache.getVersion()

    def setSettings(self, settings):
        self.settingsCache.setSettings(settings)
        LOG_DEBUG(b'Applying server settings: ', settings)
        self._core.onSettingsChanged(settings)
        return

    def getSetting(self, key, default=None):
        return self.settingsCache.getSetting(key, default)

    def getSection(self, section, defaults=None):
        result = {}
        defaults = defaults or {}
        masks = self.SECTIONS[section].masks
        offsets = self.SECTIONS[section].offsets
        for m in masks:
            default = defaults.get(m, None)
            result[m] = self.getSectionSettings(section, m, default)

        for o in offsets:
            default = defaults.get(o, None)
            result[o] = self.getSectionSettings(section, o, default)

        return result

    def getSections(self, sections, defaults=None):
        result = {}
        for section in sections:
            result.update(self.getSection(section, defaults))

        return result

    def setSections(self, sections, settings):
        settingToServer = {}
        for section in sections:
            keys = self.SECTIONS[section].masks.keys() + self.SECTIONS[section].offsets.keys()
            currentSettings = {key: value for key, value in settings.items() if key in keys}
            stored = self.settingsCache.getSectionSettings(section, None)
            storing = self._buildSectionSettings(section, currentSettings)
            if stored != storing:
                settingToServer[section] = storing

        if settingToServer:
            self.setSettings(settingToServer)
        return

    def getSectionSettings(self, section, key, default=None):
        storedValue = self.settingsCache.getSectionSettings(section, None)
        masks = self.SECTIONS[section].masks
        offsets = self.SECTIONS[section].offsets
        if storedValue is not None:
            return self._extractValue(key, storedValue, default, masks, offsets)
        else:
            return default

    def setSectionSettings(self, section, settings):
        storedSettings = self.getSection(section)
        storedValue = self.settingsCache.getSectionSettings(section, None)
        storingValue = self._buildSectionSettings(section, settings)
        if storedValue == storingValue:
            return
        else:
            self.settingsCache.setSectionSettings(section, storingValue)
            settingsDiff = {}
            for k, v in settings.iteritems():
                sV = storedSettings.get(k)
                if sV != v:
                    settingsDiff[k] = v

            LOG_DEBUG(b'Applying %s server settings: ' % section, settingsDiff)
            self._core.onSettingsChanged(settingsDiff)
            return

    def _buildSectionSettings(self, section, settings):
        storedValue = self.settingsCache.getSectionSettings(section, None)
        storingValue = storedValue if storedValue is not None else 0
        sectionMasks = self.SECTIONS[section]
        masks = sectionMasks.masks
        offsets = sectionMasks.offsets
        return self._mapValues(settings, storingValue, masks, offsets)

    def _extractValue(self, key, storedValue, default, masks, offsets):
        if key in masks:
            return storedValue >> masks[key] & 1
        if key in offsets:
            return (storedValue & offsets[key].mask) >> offsets[key].offset
        LOG_ERROR(b'Trying to extract unsupported option: ', key)
        return default

    def _mapValues(self, settings, storingValue, masks, offsets):
        for key, value in settings.iteritems():
            if key in masks:
                storingValue &= ~(1 << masks[key])
                itemValue = int(value) << masks[key]
            elif key in offsets:
                storingValue &= ~longToInt32(offsets[key].mask)
                itemValue = int(value) << offsets[key].offset
            else:
                LOG_ERROR(b'Trying to apply unsupported option: ', key, value)
                continue
            storingValue |= itemValue

        return storingValue

    def _hasKeyInSection(self, section, key):
        return key in self.SECTIONS[section].masks or key in self.SECTIONS[section].offsets

    @adisp_async
    @adisp_process
    def _updateToVersion(self, callback=None):
        currentVersion = self.settingsCache.getVersion()
        data = {b'gameData': {}, b'gameExtData': {}, b'gameExtData2': {}, b'gameplayData': {}, b'controlsData': {}, b'aimData': {}, b'markersData': {}, b'graphicsData': {}, b'marksOnGun': {}, b'fallout': {}, b'carousel_filter': {}, b'feedbackDamageIndicator': {}, b'feedbackDamageLog': {}, b'feedbackBattleEvents': {}, b'feedbackSixthSense': {}, b'onceOnlyHints': {}, b'onceOnlyHints2': {}, b'onceOnlyHints3': {}, b'uiStorage': {}, (SETTINGS_SECTIONS.UI_STORAGE_2): {}, b'epicCarouselFilter2': {}, b'rankedCarouselFilter1': {}, b'rankedCarouselFilter2': {}, b'comp7CarouselFilter1': {}, b'comp7CarouselFilter2': {}, b'sessionStats': {}, b'battleComm': {}, b'dogTags': {}, b'battleHud': {}, b'spgAim': {}, GUI_START_BEHAVIOR: {}, b'battlePassStorage': {}, (SETTINGS_SECTIONS.CONTOUR): {}, (SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_1): {}, (SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_2): {}, b'lootboxViewed': {}, b'clear': {}, b'delete': [], (SETTINGS_SECTIONS.LIMITED_UI_1): {}, (SETTINGS_SECTIONS.LIMITED_UI_2): {}, (SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS): {}, b'nyStorage': {}, (SETTINGS_SECTIONS.ARMORY_YARD): {}, (SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS): {}, (SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS_2): {}, (SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS_3): {}}
        yield migrateToVersion(currentVersion, self._core, data)
        self._setSettingsSections(data)
        callback(self)
        return

    def _setSettingsSections(self, data):
        settings = {}
        clear = data.get(b'clear', {})
        gameData = data.get(b'gameData', {})
        clearGame = clear.get(SETTINGS_SECTIONS.GAME, 0)
        if gameData or clearGame:
            settings[SETTINGS_SECTIONS.GAME] = self._buildSectionSettings(SETTINGS_SECTIONS.GAME, gameData) ^ clearGame
        gameExtData = data.get(b'gameExtData', {})
        clearGameExt = clear.get(SETTINGS_SECTIONS.GAME_EXTENDED, 0)
        if gameExtData or clearGameExt:
            settings[SETTINGS_SECTIONS.GAME_EXTENDED] = self._buildSectionSettings(SETTINGS_SECTIONS.GAME_EXTENDED, gameExtData) ^ clearGameExt
        gameExtData = data.get(b'gameExtData2', {})
        clearGameExt = clear.get(SETTINGS_SECTIONS.GAME_EXTENDED_2, 0)
        if gameExtData or clearGameExt:
            settings[SETTINGS_SECTIONS.GAME_EXTENDED_2] = self._buildSectionSettings(SETTINGS_SECTIONS.GAME_EXTENDED_2, gameExtData) ^ clearGameExt
        gameplayData = data.get(b'gameplayData', {})
        clearGameplay = clear.get(SETTINGS_SECTIONS.GAMEPLAY, 0)
        if gameplayData or clearGameplay:
            settings[SETTINGS_SECTIONS.GAMEPLAY] = self._buildSectionSettings(SETTINGS_SECTIONS.GAMEPLAY, gameplayData) ^ clearGameplay
        controlsData = data.get(b'controlsData', {})
        clearControls = clear.get(SETTINGS_SECTIONS.CONTROLS, 0)
        if controlsData or clearControls:
            settings[SETTINGS_SECTIONS.CONTROLS] = self._buildSectionSettings(SETTINGS_SECTIONS.CONTROLS, controlsData) ^ clearControls
        graphicsData = data.get(b'graphicsData', {})
        clearGraphics = clear.get(SETTINGS_SECTIONS.GRAPHICS, 0)
        if graphicsData or clearGraphics:
            settings[SETTINGS_SECTIONS.GRAPHICS] = self._buildSectionSettings(SETTINGS_SECTIONS.GRAPHICS, graphicsData) ^ clearGraphics
        aimData = data.get(b'aimData', {})
        if aimData:
            settings.update(self._buildAimSettings(aimData))
        markersData = data.get(b'markersData', {})
        if markersData:
            settings.update(self._buildMarkersSettings(markersData))
        marksOnGun = data.get(b'marksOnGun', {})
        if marksOnGun:
            settings[SETTINGS_SECTIONS.MARKS_ON_GUN] = self._buildSectionSettings(SETTINGS_SECTIONS.MARKS_ON_GUN, marksOnGun)
        fallout = data.get(b'fallout', {})
        if fallout:
            settings[SETTINGS_SECTIONS.FALLOUT] = self._buildSectionSettings(SETTINGS_SECTIONS.FALLOUT, fallout)
        carousel_filter = data.get(b'carousel_filter', {})
        clearCarouselFilter = clear.get(b'carousel_filter', 0)
        if carousel_filter or clearCarouselFilter:
            settings[SETTINGS_SECTIONS.CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.CAROUSEL_FILTER_2, carousel_filter) ^ clearCarouselFilter
        epicFilterCarousel = data.get(b'epicCarouselFilter2', {})
        clearEpicFilterCarousel = clear.get(b'epicCarouselFilter2', 0)
        if epicFilterCarousel or clearEpicFilterCarousel:
            settings[SETTINGS_SECTIONS.EPICBATTLE_CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.EPICBATTLE_CAROUSEL_FILTER_2, epicFilterCarousel) ^ clearEpicFilterCarousel
        rankedFilterCarousel1 = data.get(b'rankedCarouselFilter1', {})
        clearRankedFilterCarousel1 = clear.get(b'rankedCarouselFilter1', 0)
        if rankedFilterCarousel1 or clearRankedFilterCarousel1:
            settings[SETTINGS_SECTIONS.RANKED_CAROUSEL_FILTER_1] = self._buildSectionSettings(SETTINGS_SECTIONS.RANKED_CAROUSEL_FILTER_1, rankedFilterCarousel1) ^ clearRankedFilterCarousel1
        rankedFilterCarousel2 = data.get(b'rankedCarouselFilter2', {})
        clearRankedFilterCarousel2 = clear.get(b'rankedCarouselFilter2', 0)
        if rankedFilterCarousel2 or clearRankedFilterCarousel2:
            settings[SETTINGS_SECTIONS.RANKED_CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.RANKED_CAROUSEL_FILTER_2, rankedFilterCarousel2) ^ clearRankedFilterCarousel2
        mapBoxFilterCarousel2 = data.get(b'mapBoxCarouselFilter2', {})
        clearMapBoxFilterCarousel2 = clear.get(b'mapBoxCarouselFilter2', 0)
        if mapBoxFilterCarousel2 or clearMapBoxFilterCarousel2:
            settings[SETTINGS_SECTIONS.MAPBOX_CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.MAPBOX_CAROUSEL_FILTER_2, mapBoxFilterCarousel2) ^ clearMapBoxFilterCarousel2
        funRandomFilterCarousel1 = data.get(SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_1, {})
        clearFunRandomFilterCarousel1 = clear.get(SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_1, 0)
        if funRandomFilterCarousel1 or clearFunRandomFilterCarousel1:
            settings[SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_1] = self._buildSectionSettings(SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_1, funRandomFilterCarousel1) ^ clearFunRandomFilterCarousel1
        funRandomFilterCarousel2 = data.get(SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_2, {})
        clearFunRandomFilterCarousel2 = clear.get(SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_2, 0)
        if funRandomFilterCarousel2 or clearFunRandomFilterCarousel2:
            settings[SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.FUN_RANDOM_CAROUSEL_FILTER_2, funRandomFilterCarousel2) ^ clearFunRandomFilterCarousel2
        comp7FilterCarousel1 = data.get(b'comp7CarouselFilter1', {})
        clearComp7FilterCarousel1 = clear.get(b'comp7CarouselFilter1', 0)
        if comp7FilterCarousel1 or clearComp7FilterCarousel1:
            settings[SETTINGS_SECTIONS.COMP7_CAROUSEL_FILTER_1] = self._buildSectionSettings(SETTINGS_SECTIONS.COMP7_CAROUSEL_FILTER_1, comp7FilterCarousel1) ^ clearComp7FilterCarousel1
        comp7FilterCarousel2 = data.get(b'comp7CarouselFilter2', {})
        clearComp7FilterCarousel2 = clear.get(b'comp7CarouselFilter2', 0)
        if comp7FilterCarousel2 or clearComp7FilterCarousel2:
            settings[SETTINGS_SECTIONS.COMP7_CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.COMP7_CAROUSEL_FILTER_2, comp7FilterCarousel2) ^ clearComp7FilterCarousel2
        feedbackDamageIndicator = data.get(b'feedbackDamageIndicator', {})
        if feedbackDamageIndicator:
            settings[SETTINGS_SECTIONS.DAMAGE_INDICATOR] = self._buildSectionSettings(SETTINGS_SECTIONS.DAMAGE_INDICATOR, feedbackDamageIndicator)
        feedbackDamageLog = data.get(b'feedbackDamageLog', {})
        if feedbackDamageLog:
            settings[SETTINGS_SECTIONS.DAMAGE_LOG] = self._buildSectionSettings(SETTINGS_SECTIONS.DAMAGE_LOG, feedbackDamageLog)
        feedbackBattleEvents = data.get(b'feedbackBattleEvents', {})
        if feedbackBattleEvents:
            settings[SETTINGS_SECTIONS.BATTLE_EVENTS] = self._buildSectionSettings(SETTINGS_SECTIONS.BATTLE_EVENTS, feedbackBattleEvents)
        feedbackSixthSense = data.get(b'feedbackSixthSense', {})
        if feedbackSixthSense:
            settings[SETTINGS_SECTIONS.SIXTH_SENSE] = self._buildSectionSettings(SETTINGS_SECTIONS.SIXTH_SENSE, feedbackSixthSense)
        onceOnlyHints = data.get(b'onceOnlyHints', {})
        clearOnceOnlyHints = clear.get(b'onceOnlyHints', 0)
        if onceOnlyHints or clearOnceOnlyHints:
            settings[SETTINGS_SECTIONS.ONCE_ONLY_HINTS] = self._buildSectionSettings(SETTINGS_SECTIONS.ONCE_ONLY_HINTS, onceOnlyHints) ^ clearOnceOnlyHints
        onceOnlyHints2 = data.get(b'onceOnlyHints2', {})
        clearOnceOnlyHints2 = clear.get(b'onceOnlyHints2', 0)
        if onceOnlyHints or clearOnceOnlyHints:
            settings[SETTINGS_SECTIONS.ONCE_ONLY_HINTS_2] = self._buildSectionSettings(SETTINGS_SECTIONS.ONCE_ONLY_HINTS_2, onceOnlyHints2) ^ clearOnceOnlyHints2
        onceOnlyHints3 = data.get(b'onceOnlyHints3', {})
        clearOnceOnlyHints3 = clear.get(b'onceOnlyHints3', 0)
        if onceOnlyHints3 or clearOnceOnlyHints3:
            settings[SETTINGS_SECTIONS.ONCE_ONLY_HINTS_3] = self._buildSectionSettings(SETTINGS_SECTIONS.ONCE_ONLY_HINTS_3, onceOnlyHints3) ^ clearOnceOnlyHints3
        uiStorage = data.get(b'uiStorage', {})
        clearUIStorage = clear.get(b'uiStorage', 0)
        if uiStorage or clearUIStorage:
            settings[SETTINGS_SECTIONS.UI_STORAGE] = self._buildSectionSettings(SETTINGS_SECTIONS.UI_STORAGE, uiStorage) ^ clearUIStorage
        uiStorage2 = data.get(SETTINGS_SECTIONS.UI_STORAGE_2, {})
        clearUIStorage2 = clear.get(SETTINGS_SECTIONS.UI_STORAGE_2, 0)
        if uiStorage2 or clearUIStorage2:
            settings[SETTINGS_SECTIONS.UI_STORAGE_2] = self._buildSectionSettings(SETTINGS_SECTIONS.UI_STORAGE_2, uiStorage2) ^ clearUIStorage2
        sessionStats = data.get(b'sessionStats', {})
        clearSessionStats = clear.get(b'sessionStats', 0)
        if sessionStats or clearSessionStats:
            settings[SETTINGS_SECTIONS.SESSION_STATS] = self._buildSectionSettings(SETTINGS_SECTIONS.SESSION_STATS, sessionStats) ^ clearSessionStats
        battleComm = data.get(b'battleComm', {})
        clearBattleComm = clear.get(b'battleComm', 0)
        if battleComm or clearBattleComm:
            settings[SETTINGS_SECTIONS.BATTLE_COMM] = self._buildSectionSettings(SETTINGS_SECTIONS.BATTLE_COMM, battleComm) ^ clearBattleComm
        dogTags = data.get(b'dogTags', {})
        clearDogTags = clear.get(b'dogTags', 0)
        if dogTags or clearDogTags:
            settings[SETTINGS_SECTIONS.DOG_TAGS] = self._buildSectionSettings(SETTINGS_SECTIONS.DOG_TAGS, dogTags) ^ clearDogTags
        battleHud = data.get(b'battleHud', {})
        clearBattleHud = clear.get(b'battleHud', 0)
        if battleHud or clearBattleHud:
            settings[SETTINGS_SECTIONS.BATTLE_HUD] = self._buildSectionSettings(SETTINGS_SECTIONS.BATTLE_HUD, battleHud) ^ clearBattleHud
        guiStartBehavior = data.get(GUI_START_BEHAVIOR, {})
        clearGuiStartBehavior = clear.get(GUI_START_BEHAVIOR, 0)
        if guiStartBehavior or clearGuiStartBehavior:
            settings[SETTINGS_SECTIONS.GUI_START_BEHAVIOR] = self._buildSectionSettings(SETTINGS_SECTIONS.GUI_START_BEHAVIOR, guiStartBehavior) ^ clearGuiStartBehavior
        BPStorage = data.get(b'battlePassStorage', {})
        clearBPStorage = clear.get(b'battlePassStorage', 0)
        if BPStorage or clearBPStorage:
            settings[SETTINGS_SECTIONS.BATTLE_PASS_STORAGE] = self._buildSectionSettings(SETTINGS_SECTIONS.BATTLE_PASS_STORAGE, BPStorage) ^ clearBPStorage
        lootboxesViewedStorage = data.get(b'lootboxViewed', {})
        if lootboxesViewedStorage:
            settings[SETTINGS_SECTIONS.LOOT_BOX_VIEWED] = self._buildSectionSettings(SETTINGS_SECTIONS.LOOT_BOX_VIEWED, lootboxesViewedStorage)
        spgAimData = data.get(b'spgAim', {})
        clearSpgAimData = clear.get(SETTINGS_SECTIONS.SPG_AIM, 0)
        if spgAimData or clearSpgAimData:
            settings[SETTINGS_SECTIONS.SPG_AIM] = self._buildSectionSettings(SETTINGS_SECTIONS.SPG_AIM, spgAimData) ^ clearSpgAimData
        contourData = data.get(SETTINGS_SECTIONS.CONTOUR, {})
        clearContourData = clear.get(SETTINGS_SECTIONS.CONTOUR, 0)
        if contourData or clearContourData:
            settings[SETTINGS_SECTIONS.CONTOUR] = self._buildSectionSettings(SETTINGS_SECTIONS.CONTOUR, contourData) ^ clearContourData
        royaleFilterCarousel1 = data.get(SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_1, {})
        clearRoyaleFilterCarousel1 = clear.get(SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_1, 0)
        if royaleFilterCarousel1 or clearRoyaleFilterCarousel1:
            settings[SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_1] = self._buildSectionSettings(SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_1, royaleFilterCarousel1) ^ clearRoyaleFilterCarousel1
        royaleFilterCarousel2 = data.get(SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_2, {})
        clearRoyaleFilterCarousel2 = clear.get(SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_2, 0)
        if royaleFilterCarousel2 or clearRoyaleFilterCarousel2:
            settings[SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_2] = self._buildSectionSettings(SETTINGS_SECTIONS.ROYALE_CAROUSEL_FILTER_2, royaleFilterCarousel2) ^ clearRoyaleFilterCarousel2
        battleMatters = data.get(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, {})
        clearBattleMatters = clear.get(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, 0)
        if battleMatters or clearBattleMatters:
            settings[SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS] = self._buildSectionSettings(SETTINGS_SECTIONS.BATTLE_MATTERS_QUESTS, battleMatters) ^ clearBattleMatters
        armoryYard = data.get(SETTINGS_SECTIONS.ARMORY_YARD, {})
        clearArmoryYard = clear.get(SETTINGS_SECTIONS.ARMORY_YARD, 0)
        if armoryYard or clearArmoryYard:
            settings[SETTINGS_SECTIONS.ARMORY_YARD] = self._buildSectionSettings(SETTINGS_SECTIONS.ARMORY_YARD, armoryYard) ^ clearArmoryYard
        nyData = data.get(b'nyStorage', {})
        if nyData:
            settings[SETTINGS_SECTIONS.NEW_YEAR] = self._buildSectionSettings(SETTINGS_SECTIONS.NEW_YEAR, nyData)
        for luiStorage in SETTINGS_SECTIONS.LIMITED_UI_GROUP:
            limitedUI = data.get(luiStorage, {})
            clearLimitedUI = clear.get(luiStorage, 0)
            if limitedUI or clearLimitedUI:
                settings[luiStorage] = self._buildSectionSettings(luiStorage, limitedUI) ^ clearLimitedUI

        for hintsSection in SETTINGS_SECTIONS.BATTLE_CONTEXT_HINTS_GROUP:
            hints = data.get(hintsSection, {})
            clearHints = clear.get(hintsSection, 0)
            if hints or clearHints:
                settings[hintsSection] = self._buildSectionSettings(hintsSection, hints) ^ clearHints

        version = data.get(VERSION)
        if version is not None:
            settings[VERSION] = version
        if settings:
            self.setSettings(settings)
        delete = data.get(b'delete', ())
        if delete:
            self.settingsCache.delSettings(delete)
        return

    def __checkUIHighlights(self, key, maxVal, increase):
        storage = self.getUIStorage()
        if key not in storage:
            storage = self.getUIStorage2()
        res = storage.get(key) < maxVal
        if res and increase:
            self.updateUIStorageCounter(key)
        return res
