from __future__ import absolute_import
import enum, constants, UnitBase, arena_bonus_type_caps
from chat_commands_consts import MarkerType, BattleChatCommandExtProcessorType
from constants_utils import ConstInjector, AbstractBattleMode
from last_stand_common.battle_results import ls_results
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BET
from messenger_common_chat2 import ExtBattleChatCommand

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    LAST_STAND = 102


class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    LAST_STAND = 107
    LAST_STAND_MEDIUM = 108
    LAST_STAND_HARD = 109


LAST_STAND_ARENA_BONUS_TYPES = (
 ARENA_BONUS_TYPE.LAST_STAND, ARENA_BONUS_TYPE.LAST_STAND_MEDIUM, ARENA_BONUS_TYPE.LAST_STAND_HARD)

class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    LAST_STAND = 107
    LAST_STAND_MEDIUM = 108
    LAST_STAND_HARD = 109


LAST_STAND_QUEUE_TYPES = (
 QUEUE_TYPE.LAST_STAND, QUEUE_TYPE.LAST_STAND_MEDIUM, QUEUE_TYPE.LAST_STAND_HARD)

class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    LAST_STAND = 102


class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    LAST_STAND = 8388608


class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    LAST_STAND = UNIT_MGR_FLAGS.SQUAD | UNIT_MGR_FLAGS.LAST_STAND


class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    LAST_STAND = PREBATTLE_TYPE.LAST_STAND


class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_LS_UNIT_DIFFICULTY_LEVEL = 2002


class UnitAssemblerImplType(UnitBase.UnitAssemblerImplType, ConstInjector):
    LAST_STAND = 107
    LAST_STAND_MEDIUM = 108
    LAST_STAND_HARD = 109


UNIT_ASSEMBLER_CONFIG_NAME = b'last_stand'
UNIT_ASSEMBLER_IMPL_TO_CONFIG = {(UnitAssemblerImplType.LAST_STAND): UNIT_ASSEMBLER_CONFIG_NAME, 
   (UnitAssemblerImplType.LAST_STAND_MEDIUM): UNIT_ASSEMBLER_CONFIG_NAME, 
   (UnitAssemblerImplType.LAST_STAND_HARD): UNIT_ASSEMBLER_CONFIG_NAME}
PREBATTLE_TYPE_TO_UNIT_ASSEMBLER = {(PREBATTLE_TYPE.LAST_STAND): (UnitAssemblerImplType.LAST_STAND)}
UNIT_LS_EXTRA_DATA_KEY = b'LS_Data'
UNIT_DIFFICULTY_LEVELS_KEY = b'LS_difficultyLevels'
UNIT_INFO_BOOSTERS_KEY = b'LS_boostersInfo'
DEFAULT_UNIT_DIFFICULTY_LEVELS = [QUEUE_TYPE.LAST_STAND]
LS_PLAYER_INFO_BOOSTERS_KEY = UNIT_INFO_BOOSTERS_KEY
LS_EXTRA_DATA_BOOSTERS_KEY = b'LS_ArenaBoosters'
LS_ADD_PARAM_BOOSTERS_KEY = b'LS_ArenaBoosters'
REQUIRED_VEHICLE_TAGS = {}
FORBIDDEN_VEHICLE_TAGS = (constants.BATTLE_MODE_VEHICLE_TAGS | {b'testTank'}) - {b'event_battles'}

class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type = str
    LS_BOMBER_EXPLOSION = b'ls_bomber_explosion'
    LS_ABILITY_VAMPIRE = b'ls_ability_vampire'
    LS_ABILITY_AOE_DAMAGE = b'ls_ability_aoe_damage'
    LS_ABILITY_IGNITE = b'ls_ability_ignite'
    LS_PHASE_TIMER = b'ls_phase_timer'
    LS_LEAVER = b'ls_leaver'
    LS_PASSIVE_IGNITE = b'ls_passive_ignite'
    LS_PASSIVE_VAMPIRE = b'ls_passive_vampire'
    LS_DEATH_PIT = b'ls_death_pit'
    LS_SHOT_AOE_DAMAGE = b'ls_shot_aoe_damage'
    LS_SHOT_AOE_DRAIN_ENEMY_HP = b'ls_shot_aoe_drain_enemy_hp'
    LS_SHOT_AOE_STUN = b'ls_shot_aoe_stun'
    LS_EXTRA_DAMAGE_SITUATIONAL = b'ls_extra_damage_situational'
    LS_OBELISK_DAMAGE_TRANSFER = b'ls_obelisk_damage_transfer'


DAMAGE_INFO_CODES_PER_ATTACK_REASON = {(ATTACK_REASON.LS_BOMBER_EXPLOSION): b'DEATH_FROM_LS_BOMBER_EXPLOSION', 
   (ATTACK_REASON.LS_ABILITY_VAMPIRE): b'DEATH_FROM_LS_ABILITY_VAMPIRE', 
   (ATTACK_REASON.LS_ABILITY_AOE_DAMAGE): b'DEATH_FROM_LS_ABILITY_AOE_DAMAGE', 
   (ATTACK_REASON.LS_ABILITY_IGNITE): b'DEATH_FROM_LS_ABILITY_IGNITE', 
   (ATTACK_REASON.LS_PHASE_TIMER): b'DEATH_FROM_LS_PHASE_TIMER', 
   (ATTACK_REASON.LS_LEAVER): b'DEATH_FROM_LS_PHASE_TIMER', 
   (ATTACK_REASON.LS_PASSIVE_IGNITE): b'DEATH_FROM_FIRE', 
   (ATTACK_REASON.LS_PASSIVE_VAMPIRE): b'DEATH_FROM_LS_PASSIVE_VAMPIRE', 
   (ATTACK_REASON.LS_DEATH_PIT): b'DEATH_FROM_LS_DEATH_PIT', 
   (ATTACK_REASON.LS_SHOT_AOE_DAMAGE): b'DEATH_FROM_LS_SHOT_AOE_DAMAGE', 
   (ATTACK_REASON.LS_SHOT_AOE_STUN): b'DEATH_FROM_LS_SHOT_AOE_STUN', 
   (ATTACK_REASON.LS_SHOT_AOE_DRAIN_ENEMY_HP): b'DEATH_FROM_LS_SHOT_AOE_DRAIN_ENEMY_HP', 
   (ATTACK_REASON.LS_EXTRA_DAMAGE_SITUATIONAL): b'DEATH_FROM_LS_EXTRA_DAMAGE_SITUATIONAL'}

class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type = str
    LAST_STAND = b'LAST_STAND'


LAST_STAND_GAME_PARAMS_KEY = b'last_stand_config'
LAST_STAND_BATTLE_PARAMS_KEY = b'last_stand_battle_config'
ENEMY_ROLE_TAG_PREFIX = b'lsrole_'
OBELISK_ROLE_TAG = b'lsrole_obelisk'
LS_BOSS_ROLE_TAG = b'lsrole_boss'
CONTINUOUS_TURRET_ROTATION_TAG = b'ls_continuous_turret_rotation'
LS_ROLE_PREFIX = b'ls_'
LS_BOMBER_ACTIVATE_REASON = (
 ATTACK_REASON.SHOT, ATTACK_REASON.LS_ABILITY_AOE_DAMAGE, ATTACK_REASON.LS_ABILITY_VAMPIRE,
 ATTACK_REASON.LS_SHOT_AOE_DAMAGE, ATTACK_REASON.LS_SHOT_AOE_STUN,
 ATTACK_REASON.LS_SHOT_AOE_DRAIN_ENEMY_HP)
PLAYERS_TEAM = 1
INVALID_BATTLE_PLACE = -1

class LastStandBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.LAST_STAND
    _QUEUE_TYPE = QUEUE_TYPE.LAST_STAND
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.LAST_STAND
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.LAST_STAND
    _INVITATION_TYPE = INVITATION_TYPE.LAST_STAND
    _BATTLE_MGR_NAME = b'LSBattlesMgr'
    _UNIT_MGR_NAME = b'LSUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.LAST_STAND
    _ROSTER_TYPE = ROSTER_TYPE.LAST_STAND
    _GAME_PARAMS_KEY = LAST_STAND_GAME_PARAMS_KEY
    _BATTLE_PARAMS_KEY = LAST_STAND_BATTLE_PARAMS_KEY
    _BATTLE_RESULTS_CONFIG = ls_results
    _REQUIRED_VEHICLE_TAGS = REQUIRED_VEHICLE_TAGS
    _FORBIDDEN_VEHICLE_TAGS = FORBIDDEN_VEHICLE_TAGS
    _SM_TYPE_REWARD_CONGRATS = b'lsRewardCongrats'
    _SM_TYPE_DIFFICULTY_OPEN_MESSAGE = b'lsDifficultyOpenMessage'
    _SM_TYPE_PROGRESS_POINTS_MESSAGE = b'lsProgressPointsMessage'
    _SM_TYPE_PURCHASE_BUNDLE_FOR_GOLD_MESSAGE = b'lsPurchaseBundleForGold'
    _SM_TYPE_BATTLE_RESULT = b'lsBattleResults'
    _SM_TYPE_BATTLE_PASS_POINTS_MESSAGE = b'lsBattlePassPointsMessage'
    _SM_TYPE_AUTO_MAINTENANCE = b'lsAutoMaintenance'
    _SM_TYPE_LS_INVOICE_RECEIVED = b'lsInvoiceReceived'
    _FAIRPLAY_VEHICLE_BATTLE_STATS_COMPONENT = b'LSFairplayVehicleBattleStatsComponent'
    _SM_TYPES = [
     _SM_TYPE_REWARD_CONGRATS, 
     _SM_TYPE_PROGRESS_POINTS_MESSAGE, 
     _SM_TYPE_BATTLE_RESULT, 
     _SM_TYPE_AUTO_MAINTENANCE, 
     _SM_TYPE_LS_INVOICE_RECEIVED]
    _CLIENT_SM_TYPES = [
     _SM_TYPE_PURCHASE_BUNDLE_FOR_GOLD_MESSAGE,
     _SM_TYPE_DIFFICULTY_OPEN_MESSAGE,
     _SM_TYPE_BATTLE_PASS_POINTS_MESSAGE]

    @property
    def _rosterClass(self):
        from last_stand_common.last_stand_roster_config import LastStandRoster
        return LastStandRoster

    @property
    def _client_attackReasonToCode(self):
        return {(ATTACK_REASON.getIndex(ATTACK_REASON.LS_ABILITY_VAMPIRE)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_ABILITY_AOE_DAMAGE)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_SHOT_AOE_DAMAGE)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_SHOT_AOE_DRAIN_ENEMY_HP)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_SHOT_AOE_STUN)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_BOMBER_EXPLOSION)): b'DEATH_FROM_LS_BOMBER_EXPLOSION', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_DEATH_PIT)): b'DEATH_FROM_LS_DEATH_PIT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_PHASE_TIMER)): b'DEATH_FROM_LS_PHASE_TIMER', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_LEAVER)): b'DEATH_FROM_LS_PHASE_TIMER', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_EXTRA_DAMAGE_SITUATIONAL)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.LS_OBELISK_DAMAGE_TRANSFER)): b'DEATH_FROM_SHOT'}


def registerLoggingParams(personality):
    from server_constants import BONUSES_WITH_HEATMAPS
    BONUSES_WITH_HEATMAPS.update({b'last_stand': (
                     constants.ARENA_BONUS_MASK.TYPE_BITS[ARENA_BONUS_TYPE.LAST_STAND], False), 
       b'last_stand_medium': (
                            constants.ARENA_BONUS_MASK.TYPE_BITS[ARENA_BONUS_TYPE.LAST_STAND_MEDIUM], False), 
       b'last_stand_hard': (
                          constants.ARENA_BONUS_MASK.TYPE_BITS[ARENA_BONUS_TYPE.LAST_STAND_HARD], False)})
    return


CURRENT_QUEUE_TYPE_KEY = b'currentQueueType'

class DifficultyLevelToken(object):
    EASY = b'ls_difficulty_level:easy'
    MEDIUM = b'ls_difficulty_level:medium'
    HARD = b'ls_difficulty_level:hard'
    ALWAYS_AVIABLED = (
     EASY,)
    ACCESS_REQUIRED = (MEDIUM, HARD)
    ALL_LEVELS = (EASY, MEDIUM, HARD)


TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE = {(DifficultyLevelToken.EASY): (QUEUE_TYPE.LAST_STAND), 
   (DifficultyLevelToken.MEDIUM): (QUEUE_TYPE.LAST_STAND_MEDIUM), 
   (DifficultyLevelToken.HARD): (QUEUE_TYPE.LAST_STAND_HARD)}
QUEUE_TYPE_TO_TOKEN_DIFFICULTY_LEVEL = {(QUEUE_TYPE.LAST_STAND): (DifficultyLevelToken.EASY), 
   (QUEUE_TYPE.LAST_STAND_MEDIUM): (DifficultyLevelToken.MEDIUM), 
   (QUEUE_TYPE.LAST_STAND_HARD): (DifficultyLevelToken.HARD)}
ARENA_BONUS_TYPE_TO_LEVEL = {(ARENA_BONUS_TYPE.LAST_STAND): 1, 
   (ARENA_BONUS_TYPE.LAST_STAND_MEDIUM): 2, 
   (ARENA_BONUS_TYPE.LAST_STAND_HARD): 3}

class ShopSettings(object):
    SHOP_BUNDLE_PREFFIX = b'ls_bundle'
    PURCHASED_SUFFIX = b':purchased'
    WG_MONEY_CALLBACK = b'lsPurchaseEventShopBundleWGMoney'
    TOKEN_TTL = 720


class ArtefactsSettings(object):
    ARTEFACT = b'ls_artefact'
    QUEST_PREFIX = b'ls_artefact:'
    TOKEN_PREFIX = b'ls_artefact:'
    TOKEN_TTL = 720


class ProgressPointsSettings(object):
    TOKEN = b'ls_progress:point'
    TOKEN_TTL = 720
    TOKEN_LIMIT = 10000
    NOTIFY_TOKEN = b'ls_progress:notifyPoint'
    BONUS_NAME = b'ls_progress_point'


class StoryPointsSettings(object):
    TOKEN_PREFIX = b'ls_story_point:'
    TOKEN_TTL = 720
    TOKEN_LIMIT = 10000


class BoostersSettings(object):
    BONUS_NAME = b'boosterToken'
    TOKEN_PREFIX = b'ls_booster:'
    TOKEN_TTL = 720


class DifficultyMissionsSettings(object):
    DIFFICULTY_MISSISONS_QUEST_PREFFIX = b'ls_difficulty_missions:'
    DIFFICULTY_MISSISONS_QUEST_TPL = b'ls_difficulty_missions:{difficulty}:{index}'


class ArtefactType(object):
    TEXT = b'text'
    SOUND = b'sound'
    FINAL = b'final'
    KING_REWARD = b'kingReward'


class ArtefactTypeOpen(object):
    AUTOMATICALLY = b'automatically'
    MANUALLY = b'manually'


class MsgDataCacheKeys(object):
    ARTEFACTS = b'artefacts'
    DIFFICULTIES = b'difficulties'
    DIFFICULTY_MISSISONS = b'difficultyMissions'
    NARRATIVE_STORY_POINTS = b'narrativeStoryPoints'
    ALL = (
     ARTEFACTS, DIFFICULTIES, DIFFICULTY_MISSISONS, NARRATIVE_STORY_POINTS)


ARTEFACT_ID_MASK = b'ls_artefact:{index}:'

class DailyMissionsSettings(object):
    DAILY_MISSION_QUEST_PREFIX = b'ls_daily_mission:'
    DAILY_MISSION_TOKEN_PREFIX = b'ls_daily_token:'
    DAILY_MISSION_TOKEN_FORMAT = DAILY_MISSION_TOKEN_PREFIX + b'{group}:{num}'
    DAILY_MISSION_TOKEN_TTL = 24
    TOKEN_LIMIT = 1
    BADGE_MISSION_QUEST = b'ls_badge:mission'


class LSSoulsChangeReason(object):
    CHEAT = 0
    COLLECTOR = 1
    PICK_UP = 3
    VEHICLE_DEATH = 5
    COLLECTOR_RESET = 6
    EQUIPMENT_USED = 7
    PHASE_PROGRESS = 8
    PHASE_START = 9
    RESPAWN = 10
    CAPACITY = 11
    INITIAL_GRANT = 12


class LSBuffSequenceVisibilityMode(enum.IntEnum):
    NONE = 0
    SELF = 1
    OTHERS = 2
    ALL = 3


class BATTLE_EVENT_TYPE(BET, ConstInjector):
    LS_GAMEPLAY_ACTION = 102


class LSMarkersType(object):
    CAMP = b'LS_CAMP'
    MAGNUS = b'LS_MAGNUS'


class LSMarkerComponentNames(object):
    CAMP = b'lsCampMarker'
    MAGNUS = b'lsMagnusMarker'
    ALL = (CAMP, MAGNUS)


class DamageResistanceReason(constants.DamageResistanceReason, ConstInjector):
    LS_NITRO = 105
    LS_DAMAGE_SHIELD = 106
    LS_MODULES_INVULNERABILITY_BUFF = 107
    LS_INVISIBILITY_BUFF = 108


class LSRepairReason(object):
    NONE = 0
    BASIC_REPAIR = 1
    REPAIR_BY_AOE_ABILITY_VAMPIRE = 2
    REPAIR_BY_PASSIVE_VAMPIRE = 3
    REPAIR_BY_INFINITE_REGENERATION = 4
    REPAIR_BY_AOE_TEAM_REPAIR_KIT = 5
    REPAIR_BY_SELF_SITUATIONAL = 6
    REPAIR_BY_OBELISK = 7


class BOOSTER_FACTOR_NAMES(object):
    HEAL = b'heal'
    RESTORE_SOULS_ON_RESPAWN = b'restore_souls_on_respawn'
    ABILITY_RADIUS = b'ability_radius'
    SOULS_CAPACITY = b'souls_capacity'
    RECEIVE_SOULS_AFTER_WAVE = b'receive_souls_after_wave'
    PICK_UP_SOULS = b'pick_up_souls'
    PICK_UP_RADIUS = b'pick_up_radius'
    ABILITY_COST = b'ability_cost'
    ABILITY_DURATION = b'ability_duration'
    OBELISK_TRANSLATED_DAMAGE = b'obelisk_translated_damage'
    ALL = (
     HEAL, RESTORE_SOULS_ON_RESPAWN, ABILITY_RADIUS, SOULS_CAPACITY, RECEIVE_SOULS_AFTER_WAVE,
     PICK_UP_SOULS, PICK_UP_RADIUS, ABILITY_COST, ABILITY_DURATION, OBELISK_TRANSLATED_DAMAGE)
    RETENTION_FACTORS = (
     OBELISK_TRANSLATED_DAMAGE,)


SOULS_CHANGE_REASON_TO_BOOSTER_FACTOR_NAMES = {(LSSoulsChangeReason.RESPAWN): (BOOSTER_FACTOR_NAMES.RESTORE_SOULS_ON_RESPAWN), 
   (LSSoulsChangeReason.PICK_UP): (BOOSTER_FACTOR_NAMES.PICK_UP_SOULS), 
   (LSSoulsChangeReason.CAPACITY): (BOOSTER_FACTOR_NAMES.SOULS_CAPACITY), 
   (LSSoulsChangeReason.PHASE_START): (BOOSTER_FACTOR_NAMES.RECEIVE_SOULS_AFTER_WAVE)}

class BOOSTER_FACTOR_OPERATIONS(object):
    ADD = b'add'
    ADD_PERCENT = b'add_percent'
    ALL = (ADD, ADD_PERCENT)


class LS_CHAT_CHANNELS(object):
    LS_CHAT_CHANNEL = b'#last_stand.last_stand_chat:channels/last_stand'
    LS_CHAT_CHANNEL_EASY = b'#last_stand.last_stand_chat:channels/last_stand_easy'
    LS_CHAT_CHANNEL_MEDIUM = b'#last_stand.last_stand_chat:channels/last_stand_medium'
    LS_CHAT_CHANNEL_HARD = b'#last_stand.last_stand_chat:channels/last_stand_hard'


LS_INVENTORY_PDATA_KEY = b'LS_inventory'
LS_INFO_PDATA_KEY = b'LS_info'
LS_EMPTY_SLOTS_EQ = (b'LS_emptySlot0', b'LS_emptySlot1', b'LS_emptySlot2')
LS_BUILT_IN_EQUIPMENT = []
LS_DEFAULT_AUTO_MAINTENANCE = True
LS_VEHILCE_DAILY_QUEST = b'ls_vehicle_daily_quest:points'
INVALID_PHASE = 0
LS_QUESTS_PREFIX = b'ls_'
LS_TOKENS_PREFIX = b'ls_'
DEFAULT_DIFFICULTY_MODIFIER = 1

class LS_BATTLE_CHAT_COMMANDS(object):
    LS_OBELISK = b'lsObelisk'
    LS_OBELISK_HELP = b'lsObeliskHelp'


LS_OBELISK_ACTIVE_TIME = 10.0
LS_OBELISK_VEH_MARKER = b'lsObelisk'
LS_BATTLE_CHAT_COMMAND_SETTINGS = (
 ExtBattleChatCommand(name=LS_BATTLE_CHAT_COMMANDS.LS_OBELISK, markerType=MarkerType.VEHICLE_MARKER_TYPE, cooldownPeriod=5.0, processorType=BattleChatCommandExtProcessorType.TEAM_BROADCAST, msgText=b'lsObelisk', vehMarker=LS_OBELISK_VEH_MARKER, soundNotification=b'ibc_ping_action'),
 ExtBattleChatCommand(name=LS_BATTLE_CHAT_COMMANDS.LS_OBELISK_HELP, markerType=MarkerType.VEHICLE_MARKER_TYPE, cooldownPeriod=5.0, processorType=BattleChatCommandExtProcessorType.TEAM_BROADCAST, msgText=b'lsObeliskHelp', soundNotification=b'ibc_ping_request'))
