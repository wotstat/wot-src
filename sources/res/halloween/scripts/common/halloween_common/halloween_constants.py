from __future__ import absolute_import
import enum, constants, UnitBase, arena_bonus_type_caps
from constants_utils import ConstInjector, AbstractBattleMode
from halloween_common.battle_results import halloween_results
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BET

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    HALLOWEEN = 101


class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    HALLOWEEN = 101
    HALLOWEEN_MEDIUM = 102
    HALLOWEEN_HARD = 103


class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    HALLOWEEN = 101
    HALLOWEEN_MEDIUM = 102
    HALLOWEEN_HARD = 103


class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    HALLOWEEN = 101


class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    HALLOWEEN = 2097152


class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    HALLOWEEN = UNIT_MGR_FLAGS.SQUAD | UNIT_MGR_FLAGS.HALLOWEEN


class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    HALLOWEEN = PREBATTLE_TYPE.HALLOWEEN


class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_UNIT_DIFFICULTY_LEVEL = 2001


UNIT_HALLOWEEN_EXTRA_DATA_KEY = b'halloweenData'
UNIT_DIFFICULTY_LEVELS_KEY = b'difficultyLevels'
UNIT_BLOCKED_RENT_VEHICLES_KEY = b'blockedRentVehicles'

class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type = str
    HALLOWEEN_BOMBER_EXPLOSION = b'halloween_bomber_explosion'
    HALLOWEEN_ABILITY_VAMPIRE = b'halloween_ability_vampire'
    HALLOWEEN_ABILITY_AOE_DAMAGE = b'halloween_ability_aoe_damage'
    HALLOWEEN_ABILITY_IGNITE = b'halloween_ability_ignite'
    HALLOWEEN_PHASE_TIMER = b'halloween_phase_timer'
    HALLOWEEN_LEAVER = b'halloween_leaver'
    HALLOWEEN_PASSIVE_IGNITE = b'halloween_passive_ignite'
    HALLOWEEN_PASSIVE_VAMPIRE = b'halloween_passive_vampire'
    HALLOWEEN_BOSS_AURA = b'halloween_boss_aura'
    HALLOWEEN_DEATH_PIT = b'halloween_death_pit'
    HALLOWEEN_SHOT_AOE_DAMAGE = b'halloween_shot_aoe_damage'
    HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP = b'halloween_shot_aoe_drain_enemy_hp'
    HALLOWEEN_SHOT_AOE_STUN = b'halloween_shot_aoe_stun'
    HALLOWEEN_DEATH_ZONE_IGNITE = b'halloween_death_zone_ignite'
    HALLOWEEN_DEATH_ZONE_STUN = b'halloween_death_zone_stun'
    HALLOWEEN_DEATH_ZONE_INTERVAL = b'halloween_death_zone_interval'
    HALLOWEEN_INSTANT_KILL = b'halloween_instance_kill'
    HALLOWEEN_CORROSION = b'halloween_corrosion'
    HALLOWEEN_STOMPING = b'halloween_stomping'
    HALLOWEEN_DEATH_ZONE = b'halloween_deathzone'


DAMAGE_INFO_CODES_PER_ATTACK_REASON = {(ATTACK_REASON.HALLOWEEN_BOMBER_EXPLOSION): b'DEATH_FROM_BOMBER_EXPLOSION', 
   (ATTACK_REASON.HALLOWEEN_ABILITY_VAMPIRE): b'DEATH_FROM_ABILITY_VAMPIRE', 
   (ATTACK_REASON.HALLOWEEN_ABILITY_AOE_DAMAGE): b'DEATH_FROM_ABILITY_AOE_DAMAGE', 
   (ATTACK_REASON.HALLOWEEN_ABILITY_IGNITE): b'DEATH_FROM_ABILITY_IGNITE', 
   (ATTACK_REASON.HALLOWEEN_PHASE_TIMER): b'DEATH_FROM_PHASE_TIMER', 
   (ATTACK_REASON.HALLOWEEN_LEAVER): b'DEATH_FROM_PHASE_TIMER', 
   (ATTACK_REASON.HALLOWEEN_PASSIVE_IGNITE): b'DEATH_FROM_FIRE', 
   (ATTACK_REASON.HALLOWEEN_PASSIVE_VAMPIRE): b'DEATH_FROM_PASSIVE_VAMPIRE', 
   (ATTACK_REASON.HALLOWEEN_BOSS_AURA): b'DEATH_FROM_HALLOWEEN_BOSS_AURA', 
   (ATTACK_REASON.HALLOWEEN_DEATH_PIT): b'DEATH_FROM_HALLOWEEN_DEATH_PIT', 
   (ATTACK_REASON.HALLOWEEN_SHOT_AOE_DAMAGE): b'DEATH_FROM_SHOT_AOE_DAMAGE', 
   (ATTACK_REASON.HALLOWEEN_SHOT_AOE_STUN): b'DEATH_FROM_SHOT_AOE_STUN', 
   (ATTACK_REASON.HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP): b'DEATH_FROM_SHOT_AOE_DRAIN_ENEMY_HP', 
   (ATTACK_REASON.HALLOWEEN_DEATH_ZONE_IGNITE): b'DEATH_FROM_HALLOWEEN_DEATH_ZONE_IGNITE', 
   (ATTACK_REASON.HALLOWEEN_DEATH_ZONE_STUN): b'DEATH_FROM_HALLOWEEN_DEATH_ZONE_STUN', 
   (ATTACK_REASON.HALLOWEEN_DEATH_ZONE_INTERVAL): b'DEATH_FROM_HALLOWEEN_DEATH_ZONE_INTERVAL', 
   (ATTACK_REASON.HALLOWEEN_INSTANT_KILL): b'DEATH_FROM_HALLOWEEN_INSTANT_KILL', 
   (ATTACK_REASON.HALLOWEEN_CORROSION): b'DEATH_FROM_HALLOWEEN_CORROSION', 
   (ATTACK_REASON.HALLOWEEN_STOMPING): b'DEATH_FROM_HALLOWEEN_STOMPING', 
   (ATTACK_REASON.HALLOWEEN_DEATH_ZONE): b'DEATH_FROM_HALLOWEEN_DEATH_ZONE'}

class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type = str
    HALLOWEEN = b'HALLOWEEN'


HALLOWEEN_GAME_PARAMS_KEY = b'halloween_config'
HALLOWEEN_BESTIARY_PARAMS_KEY = b'halloween_bestiary_config'
HALLOWEEN_GSW_PARAMS_KEY = b'halloween_gsw_config'
HALLOWEEN_LOOT_PARAMS_KEY = b'halloween_loot_config'
HALLOWEEN_ANOMALIES_PARAMS_KEY = b'halloween_anomalies_config'
NITRO_BUILTIN_EXTRA_PATTERN = b'nitroRamDamage'
BOSS_ROLE_TAG = b'hwrole_boss'
ENEMY_ROLE_TAG_PREFIX = b'hwrole_'
PLAYERS_TEAM = 1
INVALID_BATTLE_PLACE = -1
INVALID_PHASE = 0
HALLOWEEN_BOMBER_ACTIVATE_REASON = (
 ATTACK_REASON.SHOT, ATTACK_REASON.HALLOWEEN_ABILITY_AOE_DAMAGE, ATTACK_REASON.HALLOWEEN_ABILITY_VAMPIRE,
 ATTACK_REASON.HALLOWEEN_SHOT_AOE_DAMAGE, ATTACK_REASON.HALLOWEEN_SHOT_AOE_STUN,
 ATTACK_REASON.HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP)

class HalloweenBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.HALLOWEEN
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.HALLOWEEN
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.HALLOWEEN
    _INVITATION_TYPE = INVITATION_TYPE.HALLOWEEN
    _BATTLE_MGR_NAME = b'HalloweenBattlesMgr'
    _UNIT_MGR_NAME = b'HalloweenUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.HALLOWEEN
    _ROSTER_TYPE = ROSTER_TYPE.HALLOWEEN
    _GAME_PARAMS_KEY = HALLOWEEN_GAME_PARAMS_KEY
    _BATTLE_RESULTS_CONFIG = halloween_results
    _REQUIRED_VEHICLE_TAGS = (b'event_battles',)
    _FORBIDDEN_VEHICLE_TAGS = constants.BATTLE_MODE_VEHICLE_TAGS - {b'event_battles'}
    _SM_TYPE_ARTEFACT_REWARD_CONGRATS = b'hwArtefactRewardCongrats'
    _SM_TYPE_DIFFICULTY_REWARD_CONGRATS = b'hwDifficultyRewardCongrats'
    _SM_TYPE_DIFFICULTY_OPEN_MESSAGE = b'hwDifficultyOpenMessage'
    _SM_TYPE_VEHICLE_RENT_MESSAGE = b'hwVehicleRentMessage'
    _SM_TYPE_ARTEFACT_KEYS_MESSAGE = b'hwArtefactKeysMessage'
    _SM_TYPE_PURCHASE_BUNDLE_FOR_GOLD_MESSAGE = b'hwPurchaseBundleForGold'
    _SM_TYPE_BATTLE_RESULT = b'hwBattleResults'
    _SM_TYPE_BATTLE_PASS_POINTS_MESSAGE = b'hwBattlePassPointsMessage'
    _SM_TYPE_AUTO_MAINTENANCE = b'hwAutoMaintenance'
    _SM_TYPE_INVOICE_RECEIVED = b'hwInvoiceReceived'
    _SM_TYPE_INVOICE_RECEIVED_LOW_PRIORITY = b'hwInvoiceReceivedLowPriority'
    _FAIRPLAY_VEHICLE_BATTLE_STATS_COMPONENT = b'HWFairplayVehicleBattleStatsComponent'
    _SM_TYPES = [
     _SM_TYPE_ARTEFACT_REWARD_CONGRATS, 
     _SM_TYPE_DIFFICULTY_REWARD_CONGRATS, 
     _SM_TYPE_VEHICLE_RENT_MESSAGE, 
     _SM_TYPE_ARTEFACT_KEYS_MESSAGE, 
     _SM_TYPE_BATTLE_RESULT, 
     _SM_TYPE_AUTO_MAINTENANCE, 
     _SM_TYPE_INVOICE_RECEIVED, 
     _SM_TYPE_INVOICE_RECEIVED_LOW_PRIORITY]
    _CLIENT_SM_TYPES = [
     _SM_TYPE_PURCHASE_BUNDLE_FOR_GOLD_MESSAGE,
     _SM_TYPE_DIFFICULTY_OPEN_MESSAGE,
     _SM_TYPE_BATTLE_PASS_POINTS_MESSAGE]

    @property
    def _rosterClass(self):
        from halloween_common.halloween_roster_config import HalloweenRoster
        return HalloweenRoster

    @property
    def _client_attackReasonToCode(self):
        return {(ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_ABILITY_VAMPIRE)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_ABILITY_AOE_DAMAGE)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_SHOT_AOE_DAMAGE)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_SHOT_AOE_STUN)): b'DEATH_FROM_SHOT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_BOSS_AURA)): b'DEATH_FROM_HALLOWEEN_BOSS_AURA', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_BOMBER_EXPLOSION)): b'DEATH_FROM_BOMBER_EXPLOSION', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_DEATH_PIT)): b'DEATH_FROM_HALLOWEEN_DEATH_PIT', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_PHASE_TIMER)): b'DEATH_FROM_PHASE_TIMER', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_LEAVER)): b'DEATH_FROM_PHASE_TIMER', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_DEATH_ZONE_IGNITE)): b'DEATH_HALLOWEEN_DEATH_ZONE_IGNITE', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_DEATH_ZONE_STUN)): b'DEATH_HALLOWEEN_DEATH_ZONE_STUN', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_DEATH_ZONE_INTERVAL)): b'DEATH_HALLOWEEN_DEATH_ZONE_INTERVAL', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_INSTANT_KILL)): b'DEATH_FROM_HALLOWEEN_INSTANT_KILL', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_CORROSION)): b'DEATH_FROM_HALLOWEEN_CORROSION', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_STOMPING)): b'DEATH_FROM_HALLOWEEN_STOMPING', 
           (ATTACK_REASON.getIndex(ATTACK_REASON.HALLOWEEN_DEATH_ZONE)): b'DEATH_FROM_HALLOWEEN_DEATH_ZONE'}


def registerLoggingParams(personality):
    from server_constants import BONUSES_WITH_HEATMAPS
    BONUSES_WITH_HEATMAPS.update({b'halloween': (
                    constants.ARENA_BONUS_MASK.TYPE_BITS[ARENA_BONUS_TYPE.HALLOWEEN], False), 
       b'halloween_medium': (
                           constants.ARENA_BONUS_MASK.TYPE_BITS[ARENA_BONUS_TYPE.HALLOWEEN_MEDIUM], False), 
       b'halloween_hard': (
                         constants.ARENA_BONUS_MASK.TYPE_BITS[ARENA_BONUS_TYPE.HALLOWEEN_HARD], False)})
    return


class DifficultyLevelToken(object):
    EASY = b'hw_difficulty_level:easy'
    MEDIUM = b'hw_difficulty_level:medium'
    HARD = b'hw_difficulty_level:hard'
    ALWAYS_AVIABLED = (
     EASY,)
    ACCESS_REQUIRED = (MEDIUM, HARD)
    ALL_LEVELS = (EASY, MEDIUM, HARD)


TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE = {(DifficultyLevelToken.EASY): (QUEUE_TYPE.HALLOWEEN), 
   (DifficultyLevelToken.MEDIUM): (QUEUE_TYPE.HALLOWEEN_MEDIUM), 
   (DifficultyLevelToken.HARD): (QUEUE_TYPE.HALLOWEEN_HARD)}
QUEUE_TYPE_TO_TOKEN_DIFFICULTY_LEVEL = {(QUEUE_TYPE.HALLOWEEN): (DifficultyLevelToken.EASY), 
   (QUEUE_TYPE.HALLOWEEN_MEDIUM): (DifficultyLevelToken.MEDIUM), 
   (QUEUE_TYPE.HALLOWEEN_HARD): (DifficultyLevelToken.HARD)}
ARENA_BONUS_TYPE_TO_LEVEL = {(ARENA_BONUS_TYPE.HALLOWEEN): 1, 
   (ARENA_BONUS_TYPE.HALLOWEEN_MEDIUM): 2, 
   (ARENA_BONUS_TYPE.HALLOWEEN_HARD): 3}
MIN_REWARD_PHASE = 2

class ShopSettings(object):
    SHOP_BUNDLE_PREFFIX = b'hw26bundle'
    PURCHASED_SUFFIX = b':purchased'
    WG_MONEY_CALLBACK = b'purchaseEventShopBundleWGMoney'


class ArtefactsSettings(object):
    ARTEFACT = b'hw_artefact'
    QUEST_PREFIX = b'hw_artefact:'
    TOKEN_PREFIX = b'hw_artefact:'
    KEY_TOKEN = b'hw_artefact:key'
    KEY_NOTIFY_TOKEN = b'hw_artefact:notifyKey'
    MEMORY = b'img:hw_artefact:memory'
    CREW_100 = b'hw_bonus_crew:100'
    KEY_TOKEN_TTL = 2160
    KEY_TOKEN_LIMIT = 10000


class ArtefactType(object):
    TEXT = b'text'
    SOUND = b'sound'
    FINAL = b'final'


class HWModifierColors(enum.IntEnum):
    blue = 0
    green = 1
    red = 2
    violet = 3
    orange = 4


class HalloweenSoulsChangeReason(object):
    CHEAT = 0
    COLLECTOR = 1
    BOSS_AURA = 2
    PICK_UP = 3
    VEHICLE_DEATH = 5
    COLLECTOR_RESET = 6
    EQUIPMENT_USED = 7
    PHASE_PROGRESS = 8
    PHASE_START = 9
    PHASE_MIRIUMIZATION = 10


class HWBuffSequenceVisibilityMode(enum.IntEnum):
    NONE = 0
    SELF = 1
    OTHERS = 2
    ALL = 3


class AnomalySettings(object):
    TOKEN_PREFIX = b'hw_anomaly:'


class LootAnomalyType(object):
    INDIVIDUAL = b'individual'
    SECRET = b'secret'


ALL_LOOT_ANOMALY_TYPES = (
 LootAnomalyType.INDIVIDUAL, LootAnomalyType.SECRET)

class AnomalyType(LootAnomalyType):
    EPIC = b'epic'
    REGULAR = b'regular'


class BATTLE_EVENT_TYPE(BET, ConstInjector):
    HW_GAMEPLAY_ACTION = 101


class HalloweenMarkersType(object):
    SOULS_COLLECTOR = b'SOULS_COLLECTOR'
    CAMP = b'HW_CAMP_1'


class HalloweenMarkerComponentNames(object):
    CAMP = b'hwCampMarker'
    SOULS_COLLECTOR = b'hwSoulsCollectorMarker'


class DamageResistanceReason(constants.DamageResistanceReason, ConstInjector):
    DAMAGE_SHIELD = 102
    MODULES_INVULNERABILITY_BUFF = 103
    BOSS_DAMAGE_SHIELD = 104
    BOMBER_EXPLOSION_RESIST = 109


class HWRepairReason(object):
    NONE = 0
    BASIC_REPAIR = 1
    REPAIR_BY_AOE_ABILITY_VAMPIRE = 2
    REPAIR_BY_PASSIVE_VAMPIRE = 3
    REPAIR_BY_INFINITE_REGENERATION = 4
    REPAIR_BY_AOE_TEAM_REPAIR_KIT = 5


class HWDeathZoneShapes(enum.IntEnum):
    RECT = 1
    CIRCLE = 2


TOKEN_LIFETIME_HOURS = 2160
HALLOWEEN_CHAT_CHANNEL = b'#halloween.halloween_chat:channels/halloween'
HW_EMPTY_SLOTS_EQ = (b'halloweenEmptySlot0', b'halloweenEmptySlot1', b'halloweenEmptySlot2')
HW_BUILT_IN_EQUIPMENT = (b'nitroRamDamage',)
CURRENT_QUEUE_TYPE_KEY = b'currentQueueType'
HALLOWEEN_QUESTS_PREFFIX = b'hw_'
RENT_VEHICLE_PREFIX = b'hw_rent_vehicle'
KEY_DAILY_QUEST_TPL = b'hw_key_daily_quest:{intCD}'
ARTEFACT_ID_MASK = b'hw_artefact:{index}:'
ANOMALIES_SYSTEM_UNLOCKED = b'hw_unlock_recipes'
HW_UPGRADE_OPTIONS_REASON_UNLOCKED = -1

class HWStoryChoiceSettings(object):
    STORY_CHOICE_TOKEN_LIFETIME_HOURS = 9360
    FAKE_MEDAL = b'hw_fake_choice_medal:hw2026Medal'
    MEDAL_BONUS_NAME, _medalSuffix = FAKE_MEDAL.split(b':')
    MEDAL_FORMAT = _medalSuffix + b'_{}'
    OPTION_1 = b'hw26_ending:1'
    OPTION_2 = b'hw26_ending:2'
    OPTION_SKIP = b'option_skip'
    ALL_OPTIONS = (OPTION_1, OPTION_2)


class HWVehicleModifiers(object):
    EQUIPMENT_COOLDOWN = b'equipment/cooldown'
    EQUIPMENT_DURATION = b'equipment/duration'
    EQUIPMENT_USAGE_COST = b'equipment/usageCost'
    SHELLS_DEATH_KEEPER = b'shells/deathKeeper'
    SOULS_EXTRA_DROP_FROM_BOTS = b'souls/extraDropFromBots'
    SOULS_CAPACITY = b'souls/capacity'
    SOULS_REFUND_AMOUNT = b'souls/refundAmount'
    SOULS_REFUND_CHANCE = b'souls/refundChance'
    SOULS_DEATH_KEEPER = b'souls/deathKeeper'
    SOULS_DEATH_DROP_RATE = b'souls/deathDropRate'


HALLOWEEN_SCOPE_ID = b'halloween'

class HWSoundEventType(enum.IntEnum):
    OVERRIDING = 0
    INITIAL = 1
    FINAL = 2
