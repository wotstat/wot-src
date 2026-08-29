import enum, calendar, time, datetime
from math import cos, radians
from time import time as timestamp
from collections import namedtuple
from itertools import izip, chain
from Math import Vector3
from coordinate_system import AXIS_ALIGNED_DIRECTION
from realm import CURRENT_REALM, IS_CT
try:
    import BigWorld
except ImportError:

    class BigWorld:
        component = b'unknown'


IS_VS_EDITOR = BigWorld.component == b'vs_editor'
IS_UE_EDITOR = BigWorld.component == b'editor'
IS_CLIENT = BigWorld.component == b'client'
IS_EDITOR = IS_VS_EDITOR or IS_UE_EDITOR
IS_BOT = BigWorld.component == b'bot'
IS_CELLAPP = BigWorld.component == b'cell'
IS_BASEAPP = BigWorld.component in (b'base', b'service')
IS_WEB = BigWorld.component == b'web'
IS_DYNUPDATER = False
IS_LOAD_GLOSSARY = False
IS_CGF_DUMP = BigWorld.component == b'client_cgf_dump'
IS_PROCESS_REPLAY = BigWorld.component.endswith(b'process_replay')
DEFAULT_LANGUAGE = b'ru'
AUTH_REALM = b'RU'
IS_DEVELOPMENT = CURRENT_REALM == b'DEV'
IS_CHINA = CURRENT_REALM == b'CN'
IS_KOREA = CURRENT_REALM == b'KR'
IS_SINGAPORE = CURRENT_REALM == b'ASIA'
IS_SANDBOX = CURRENT_REALM == b'SB'
REALMS = frozenset([22, 28, 29, 26, 24, 25, 30, 31, 32, 23, 27])
OVERRIDE_CODES = frozenset([22, 28, 29, 26, 24, 25, 30, 31, 32, 23, 27, 33])
REGIONAL_REALMS = frozenset([22, 28, 29, 26, 24, 25])
CURRENT_REALM_IS_REGIONAL = CURRENT_REALM in REGIONAL_REALMS

class REALM_HELPER:

    @staticmethod
    def toRealm(override_code):
        return override_code

    @staticmethod
    def toOverride(realm):
        return realm


if CURRENT_REALM == b'NA':
    AUTH_REALM = b'NA'
elif CURRENT_REALM == b'ASIA':
    AUTH_REALM = b'ASIA'
elif CURRENT_REALM == b'CN':
    DEFAULT_LANGUAGE = b'cn'
    AUTH_REALM = b'CN'
elif CURRENT_REALM == b'KR':
    DEFAULT_LANGUAGE = b'ko'
    AUTH_REALM = b'KR'
elif CURRENT_REALM == b'CT':
    AUTH_REALM = b'CT'
elif CURRENT_REALM == b'RU':
    DEFAULT_LANGUAGE = b'ru'
    AUTH_REALM = b'RU' if not IS_CT else b'CT'
elif CURRENT_REALM in (b'EU', b'ST', b'QA', b'DEV', b'SB'):
    pass
SPECIAL_OL_FILTER = IS_KOREA or IS_SINGAPORE
IS_RENTALS_ENABLED = True
IS_SHOW_SERVER_STATS = not IS_CHINA
IS_CAT_LOADED = False
LEAKS_DETECTOR_MAX_EXECUTION_TIME = 2.0
IS_IGR_ENABLED = IS_KOREA or IS_CHINA
SERVER_TICK_LENGTH = 0.1
NULL_ENTITY_ID = 0
SHELL_TRAJECTORY_EPSILON_CLIENT = 0.03
SHELL_TRAJECTORY_EPSILON_SERVER = 0.1
SHELL_TRAJECTORY_EPSILON_AI = 1.0
ARENA_TYPE_XML_PATH = b'scripts/arena_defs/'
ITEM_DEFS_PATH = b'scripts/item_defs/'
VOICE_CHAT_INIT_TIMEOUT = 10
MAX_OPENED_ANOTHER_DOSSIERS = 4
ENABLE_DEBUG_DYNAMICS_INFO = False
if IS_CLIENT:
    import ResMgr
    IS_CLIENT_BUILD = not ResMgr.isFile(b'development.build')
else:
    IS_CLIENT_BUILD = False
ENABLE_TKILL_BANS = True
HAS_DEV_RESOURCES = IS_DEVELOPMENT and not IS_CLIENT_BUILD
IS_DEVELOPMENT_BUILD = IS_DEVELOPMENT and IS_CLIENT_BUILD
MODULE_NAME_SEPARATOR = b', '
MAX_LOG_EXT_INFO_LEN = 255

class SPT_MATKIND:
    SOLID = 71
    LEAVES = 72


class DESTRUCTIBLE_MATKIND:
    MIN = 71
    MAX = 100
    NORMAL_MIN = 73
    NORMAL_MAX = 86
    DAMAGED_MIN = 87
    DAMAGED_MAX = 100


class DOSSIER_TYPE:
    ACCOUNT = 1
    VEHICLE = 2
    TANKMAN = 4
    FORTIFIED_REGIONS = 8
    RATED7X7 = 16
    CLUB = 32
    CLAN = 64


class DOSSIER_RECORD_COMBINATION_TYPE:
    ADD = 0
    MAX = 1


class WOT_GAMEPLAY:
    BOOTCAMP = b'bootcamp'
    USUAL = b'usual'
    OFF = 0
    ON = 1


ARENA_GAMEPLAY_NAMES = (b'ctf', b'domination', b'assault', b'nations', b'ctf2', b'domination2', b'assault2', b'fallout', b'fallout2', b'fallout3', b'fallout4', b'ctf30x30', b'domination30x30', b'sandbox', b'bootcamp', b'epic', b'maps_training', b'rts', b'rts_1x1', b'rts_bootcamp', b'comp7', b'bob', b'domination3')
if IS_EDITOR:
    ARENA_GAMEPLAY_READABLE_NAMES = (b'Capture The Flag', b'Domination', b'Assault', b'Nations', b'Capture The Flag 2', b'Domination 2', b'Assault 2', b'Fallout Bomb', b'Fallout 2 Flag', b'Fallout 3', b'Fallout 4', b'Capture The Flag 30 vs 30', b'Domination 30 vs 30', b'Sandbox', b'Bootcamp', b'Epic', b'Maps Training', b'RTS', b'RTS 1 vs 1', b'RTS Boot Camp', b'Comp7', b'Battle of Bloggers', b'Domination 3')
ARENA_GAMEPLAY_IDS = dict((value, index) for index, value in enumerate(ARENA_GAMEPLAY_NAMES))
ARENA_GAMEPLAY_MASK_DEFAULT = 1048575
VALID_TRAINING_ARENA_GAMEPLAY_IDS = frozenset(ARENA_GAMEPLAY_IDS[gameplayName] for gameplayName in (b'ctf', b'domination', b'assault', b'nations', b'ctf2', b'domination2', b'assault2', b'epic', b'bootcamp', b'ctf30x30', b'domination30x30', b'rts', b'rts_1x1', b'rts_bootcamp', b'domination3'))
VALID_PREBATTLE_GAMEPLAY_IDS = VALID_TRAINING_ARENA_GAMEPLAY_IDS.union(frozenset(ARENA_GAMEPLAY_IDS[gameplayName] for gameplayName in (b'comp7',)))

class HANGAR_VISIBILITY_TAGS:
    LAYERS = (b'1', b'2', b'3', b'4', b'5', b'6', b'7')
    FIRST_BIT_RANKED = len(LAYERS)
    RANKED_TAGS = (b'R_ON', b'R_GAP', b'R_OFF')
    FIRST_BIT_REGIONS = 16
    REGIONS = (b'NA', b'ASIA', b'EU', b'RU')
    IDS = dict((value, index) for index, value in chain(enumerate(LAYERS), enumerate(RANKED_TAGS, FIRST_BIT_RANKED), enumerate(REGIONS, FIRST_BIT_REGIONS)))
    NAMES = dict((index, value) for index, value in chain(enumerate(LAYERS), enumerate(RANKED_TAGS, FIRST_BIT_RANKED), enumerate(REGIONS, FIRST_BIT_REGIONS)))
    ALL_BITS_DEFAULT = (1 << len(LAYERS)) - 1 | sum(1 << key for key in NAMES.iterkeys())


class ARENA_GUI_TYPE:
    UNKNOWN = 0
    RANDOM = 1
    TRAINING = 2
    CYBERSPORT = 5
    FALLOUT = 6
    EVENT_BATTLES = 7
    FALLOUT_CLASSIC = 13
    FALLOUT_MULTITEAM = 14
    SORTIE_2 = 15
    FORT_BATTLE_2 = 16
    RANKED = 17
    BOOTCAMP = 18
    EPIC_RANDOM = 19
    EPIC_RANDOM_TRAINING = 20
    EPIC_BATTLE = 21
    EPIC_TRAINING = 22
    BATTLE_ROYALE = 23
    MAPBOX = 24
    MAPS_TRAINING = 25
    RTS = 26
    RTS_TRAINING = 27
    RTS_BOOTCAMP = 28
    FUN_RANDOM = 29
    COMP7 = 30
    TOURNAMENT_COMP7 = 33
    VERSUS_AI = 31000
    RANGE = (
     UNKNOWN, RANDOM, TRAINING, CYBERSPORT, FALLOUT, EVENT_BATTLES, FALLOUT_CLASSIC,
     FALLOUT_MULTITEAM, SORTIE_2, FORT_BATTLE_2, RANKED, BOOTCAMP,
     EPIC_RANDOM, EPIC_RANDOM_TRAINING, EPIC_BATTLE, EPIC_TRAINING, BATTLE_ROYALE, MAPBOX,
     MAPS_TRAINING, RTS, RTS_TRAINING, RTS_BOOTCAMP, FUN_RANDOM, COMP7, VERSUS_AI, TOURNAMENT_COMP7)
    RANDOM_RANGE = (
     RANDOM, EPIC_RANDOM)
    FALLOUT_RANGE = (
     FALLOUT_CLASSIC, FALLOUT_MULTITEAM)
    EPIC_RANGE = (
     EPIC_BATTLE, EPIC_TRAINING)
    STRONGHOLD_RANGE = (
     SORTIE_2, FORT_BATTLE_2)
    COMP7_RANGE = (
     COMP7, TOURNAMENT_COMP7)
    VOIP_SUPPORTED = RANDOM_RANGE + EPIC_RANGE
    BATTLE_CHAT_SETTING_SUPPORTED = (
     RANDOM, RANKED, EPIC_RANDOM, EPIC_BATTLE, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI)


class ARENA_GUI_TYPE_LABEL:
    LABELS = {(ARENA_GUI_TYPE.UNKNOWN): b'special', 
       (ARENA_GUI_TYPE.RANDOM): b'random', 
       (ARENA_GUI_TYPE.TRAINING): b'training', 
       (ARENA_GUI_TYPE.CYBERSPORT): b'team7x7', 
       (ARENA_GUI_TYPE.EVENT_BATTLES): b'event', 
       (ARENA_GUI_TYPE.FALLOUT_CLASSIC): b'fallout_classic', 
       (ARENA_GUI_TYPE.FALLOUT_MULTITEAM): b'fallout_multiteam', 
       (ARENA_GUI_TYPE.BOOTCAMP): b'bootcamp', 
       (ARENA_GUI_TYPE.SORTIE_2): b'fortifications', 
       (ARENA_GUI_TYPE.FORT_BATTLE_2): b'fortifications', 
       (ARENA_GUI_TYPE.RANKED): b'ranked', 
       (ARENA_GUI_TYPE.EPIC_RANDOM): b'epic_random', 
       (ARENA_GUI_TYPE.EPIC_RANDOM_TRAINING): b'epic_random_training', 
       (ARENA_GUI_TYPE.EPIC_BATTLE): b'epicbattle', 
       (ARENA_GUI_TYPE.EPIC_TRAINING): b'epicbattle', 
       (ARENA_GUI_TYPE.BATTLE_ROYALE): b'battle_royale', 
       (ARENA_GUI_TYPE.MAPBOX): b'mapbox', 
       (ARENA_GUI_TYPE.MAPS_TRAINING): b'maps_training', 
       (ARENA_GUI_TYPE.FUN_RANDOM): b'fun_random', 
       (ARENA_GUI_TYPE.COMP7): b'comp7', 
       (ARENA_GUI_TYPE.VERSUS_AI): b'versusAI', 
       (ARENA_GUI_TYPE.TOURNAMENT_COMP7): b'tournament_comp7'}


class ARENA_BONUS_TYPE:
    UNKNOWN = 0
    REGULAR = 1
    TRAINING = 2
    TOURNAMENT = 4
    CLAN = 5
    CYBERSPORT = 7
    EVENT_BATTLES = 9
    GLOBAL_MAP = 13
    TOURNAMENT_REGULAR = 14
    TOURNAMENT_CLAN = 15
    FALLOUT_CLASSIC = 18
    FALLOUT_MULTITEAM = 19
    SORTIE_2 = 20
    FORT_BATTLE_2 = 21
    RANKED = 22
    BOOTCAMP = 23
    EPIC_RANDOM = 24
    EPIC_RANDOM_TRAINING = 25
    EVENT_BATTLES_2 = 26
    EPIC_BATTLE = 27
    EPIC_BATTLE_TRAINING = 28
    BATTLE_ROYALE_SOLO = 29
    BATTLE_ROYALE_SQUAD = 30
    TOURNAMENT_EVENT = 31
    BOB = 32
    EVENT_RANDOM = 33
    BATTLE_ROYALE_TRN_SOLO = 34
    BATTLE_ROYALE_TRN_SQUAD = 35
    WEEKEND_BRAWL = 36
    MAPBOX = 37
    MAPS_TRAINING = 38
    RTS = 39
    RTS_1x1 = 40
    RTS_BOOTCAMP = 41
    FUN_RANDOM = 42
    COMP7 = 43
    TOURNAMENT_COMP7 = 47
    VERSUS_AI = 50
    RANGE = (
     UNKNOWN, REGULAR, TRAINING, TOURNAMENT, CLAN, CYBERSPORT, EVENT_BATTLES, EVENT_BATTLES_2, GLOBAL_MAP,
     TOURNAMENT_REGULAR, TOURNAMENT_CLAN, TOURNAMENT_COMP7,
     FALLOUT_CLASSIC, FALLOUT_MULTITEAM, BOOTCAMP, SORTIE_2, FORT_BATTLE_2, RANKED,
     EPIC_RANDOM, EPIC_RANDOM_TRAINING, EPIC_BATTLE, EPIC_BATTLE_TRAINING, TOURNAMENT_EVENT, EVENT_RANDOM,
     BATTLE_ROYALE_SOLO, BATTLE_ROYALE_SQUAD, BOB, BATTLE_ROYALE_TRN_SOLO, BATTLE_ROYALE_TRN_SQUAD,
     MAPBOX, WEEKEND_BRAWL, MAPS_TRAINING, RTS, RTS_1x1, RTS_BOOTCAMP, FUN_RANDOM, COMP7, VERSUS_AI)
    RANDOM_RANGE = (
     REGULAR, EPIC_RANDOM)
    FALLOUT_RANGE = (FALLOUT_CLASSIC, FALLOUT_MULTITEAM)
    TOURNAMENT_RANGE = (TOURNAMENT, TOURNAMENT_REGULAR, TOURNAMENT_CLAN, TOURNAMENT_EVENT, TOURNAMENT_COMP7)
    BATTLE_ROYALE_RANGE = (BATTLE_ROYALE_SOLO, BATTLE_ROYALE_SQUAD, BATTLE_ROYALE_TRN_SOLO, BATTLE_ROYALE_TRN_SQUAD)
    BATTLE_ROYALE_REGULAR_RANGE = (BATTLE_ROYALE_SOLO, BATTLE_ROYALE_SQUAD)
    BATTLE_ROYALE_SQUAD_RANGE = (BATTLE_ROYALE_SQUAD, BATTLE_ROYALE_TRN_SQUAD)
    RTS_RANGE = (RTS, RTS_1x1, RTS_BOOTCAMP)
    RTS_BATTLES = (RTS, RTS_1x1)
    EXTERNAL_RANGE = (
     SORTIE_2, FORT_BATTLE_2, GLOBAL_MAP,
     TOURNAMENT, TOURNAMENT_CLAN, TOURNAMENT_REGULAR, TOURNAMENT_EVENT, TOURNAMENT_COMP7)


ARENA_BONUS_TYPE_NAMES = dict([(k, v) for k, v in ARENA_BONUS_TYPE.__dict__.iteritems() if isinstance(v, int)])
ARENA_BONUS_TYPE_IDS = dict([(v, k) for k, v in ARENA_BONUS_TYPE_NAMES.iteritems()])

class ARENA_BONUS_TYPE_LABEL:
    LABELS = {(ARENA_BONUS_TYPE.UNKNOWN): b'special', 
       (ARENA_BONUS_TYPE.REGULAR): b'random', 
       (ARENA_BONUS_TYPE.TRAINING): b'training', 
       (ARENA_BONUS_TYPE.TOURNAMENT): b'tournament', 
       (ARENA_BONUS_TYPE.CLAN): b'clan', 
       (ARENA_BONUS_TYPE.CYBERSPORT): b'team7x7', 
       (ARENA_BONUS_TYPE.EVENT_BATTLES): b'event', 
       (ARENA_BONUS_TYPE.GLOBAL_MAP): b'globalMap', 
       (ARENA_BONUS_TYPE.TOURNAMENT_REGULAR): b'tournament_regular', 
       (ARENA_BONUS_TYPE.TOURNAMENT_CLAN): b'tournament_clan', 
       (ARENA_BONUS_TYPE.FALLOUT_CLASSIC): b'fallout_classic', 
       (ARENA_BONUS_TYPE.FALLOUT_MULTITEAM): b'fallout_multiteam', 
       (ARENA_BONUS_TYPE.SORTIE_2): b'sortie_2', 
       (ARENA_BONUS_TYPE.FORT_BATTLE_2): b'fort_battle_2', 
       (ARENA_BONUS_TYPE.RANKED): b'ranked', 
       (ARENA_BONUS_TYPE.BOOTCAMP): b'bootcamp', 
       (ARENA_BONUS_TYPE.EPIC_RANDOM): b'epic_random', 
       (ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING): b'epic_random_training', 
       (ARENA_BONUS_TYPE.EVENT_BATTLES_2): b'event_battles_2', 
       (ARENA_BONUS_TYPE.EPIC_BATTLE): b'epic_battle', 
       (ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING): b'epic_battle_training', 
       (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO): b'battle_royale_solo', 
       (ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD): b'battle_royale_quad', 
       (ARENA_BONUS_TYPE.TOURNAMENT_EVENT): b'tournament_event', 
       (ARENA_BONUS_TYPE.BOB): b'bob', 
       (ARENA_BONUS_TYPE.EVENT_RANDOM): b'event_random', 
       (ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SOLO): b'battle_royale_trn_solo', 
       (ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SQUAD): b'battle_royale_trn_squad', 
       (ARENA_BONUS_TYPE.WEEKEND_BRAWL): b'weekend_brawl', 
       (ARENA_BONUS_TYPE.MAPBOX): b'mapbox', 
       (ARENA_BONUS_TYPE.MAPS_TRAINING): b'maps_training', 
       (ARENA_BONUS_TYPE.RTS): b'rts', 
       (ARENA_BONUS_TYPE.RTS_1x1): b'rts_1x1', 
       (ARENA_BONUS_TYPE.RTS_BOOTCAMP): b'rts_bootcamp', 
       (ARENA_BONUS_TYPE.FUN_RANDOM): b'fun_random', 
       (ARENA_BONUS_TYPE.COMP7): b'comp7', 
       (ARENA_BONUS_TYPE.VERSUS_AI): b'versusAI'}


class ARENA_BONUS_MASK:
    TYPE_BITS = dict((name, 2 ** id) for id, name in enumerate(ARENA_BONUS_TYPE.RANGE[1:]))
    ANY = sum(1 << index for index in xrange(len(TYPE_BITS)))

    @staticmethod
    def mask(*args):
        return reduce((lambda v, x: v | x), [ARENA_BONUS_MASK.TYPE_BITS[arg] for arg in args])

    @staticmethod
    def exclude(*args):
        return reduce((lambda v, x: v & ~x), [ARENA_BONUS_MASK.TYPE_BITS[arg] for arg in args], ARENA_BONUS_MASK.ANY)

    @classmethod
    def reInit(cls):
        cls.TYPE_BITS = dict((name, 2 ** id) for id, name in enumerate(ARENA_BONUS_TYPE.RANGE[1:]))
        return


class ARENA_PERIOD:
    IDLE = 0
    WAITING = 1
    PREBATTLE = 2
    BATTLE = 3
    AFTERBATTLE = 4


ARENA_PERIOD_NAMES = dict([(v, k) for k, v in ARENA_PERIOD.__dict__.iteritems() if not k.startswith(b'_')])

class ARENA_UPDATE:
    VEHICLE_LIST = 1
    VEHICLE_ADDED = 2
    PERIOD = 3
    STATISTICS = 4
    VEHICLE_STATISTICS = 5
    VEHICLE_KILLED = 6
    AVATAR_READY = 7
    BASE_POINTS = 8
    BASE_CAPTURED = 9
    TEAM_KILLER = 10
    VEHICLE_UPDATED = 11
    COMBAT_EQUIPMENT_USED = 12
    FLAG_TEAMS = 16
    FLAG_STATE_CHANGED = 17
    INTERACTIVE_STATS = 19
    RESOURCE_POINT_STATE_CHANGED = 21
    OWN_VEHICLE_INSIDE_RP = 22
    OWN_VEHICLE_LOCKED_FOR_RP = 23
    SYNC_OBJECTS = 24
    SYNC_OBJECTS_DIFF = 25
    VIEW_POINTS = 26
    FOG_OF_WAR = 27
    VEHICLE_RECOVERED = 28
    RADAR_INFO_RECEIVED = 29
    SETTINGS = 30
    VEHICLE_DESCR = 31


class ARENA_SYNC_OBJECTS:
    PLAYER_GROUP = 1
    RESPAWN = 2
    PLAYER_RANK = 3
    FRONT_LINE = 4
    SECTOR = 5
    OVERTIME = 6
    SMOKE = 7
    BR_DEATH_ZONE = 8


ARENA_SYNC_OBJECT_NAMES = dict([(v, k) for k, v in ARENA_SYNC_OBJECTS.__dict__.iteritems() if not k.startswith(b'_')])

class JOIN_FAILURE:
    TIME_OUT = 1
    NOT_FOUND = 2
    ACCOUNT_LOCK = 3
    WRONG_VEHICLE = 4
    TEAM_IS_FULL = 5
    WRONG_ARGS = 6
    WRONG_ARENA_STATE = 8
    CANNOT_CREATE = 9
    PRIVACY = 10
    WRONG_ACCOUNT_TYPE = 11
    COOLDOWN = 12
    FORBIDDEN_IN_THIS_REGION = 13
    EVENT_DISABLED = 14
    WRONG_PERIPHERY_ID = 15
    WRONG_VEHICLE_LVL = 16
    QUEUE_FULL = 17
    QUEUE_FAILURE = 18
    QUEUE_FORBIDDEN = 19


JOIN_FAILURE_NAMES = dict([(v, k) for k, v in JOIN_FAILURE.__dict__.iteritems() if not k.startswith(b'_')])

class KICK_REASON:
    ARENA_CREATION_FAILURE = 1
    AVATAR_CREATION_FAILURE = 2
    VEHICLE_CREATION_FAILURE = 3
    PREBATTLE_CREATION_FAILURE = 4
    BASEAPP_CRASH = 5
    CELLAPP_CRASH = 6
    UNKNOWN_FAILURE = 7
    FINISHED = 8
    CREATOR_LEFT = 9
    PLAYERKICK = 10
    TIMEOUT = 11


KICK_REASON_NAMES = dict([(v, k) for k, v in KICK_REASON.__dict__.iteritems() if not k.startswith(b'_')])

class FINISH_REASON:
    UNKNOWN = 0
    EXTERMINATION = 1
    BASE = 2
    TIMEOUT = 3
    FAILURE = 4
    TECHNICAL = 5
    WIN_POINTS_CAP = 6
    WIN_POINTS = 7
    ALLY_KILLED = 8
    OWN_VEHICLE_DESTROYED = 9
    DESTROYED_OBJECTS = 10
    OBJECTIVES_COMPLETED = 11


FINISH_REASON_NAMES = dict([(v, k) for k, v in FINISH_REASON.__dict__.iteritems() if not k.startswith(b'_')])

class ARENA_EXT_MSG:
    UNKNOWN = 0
    ACCEPTED = 1
    CREATED = 2
    STARTED = 3
    FINISHED = 4
    FAILED = 5
    PLAYER_JOINED = 6
    PLAYER_LEFT = 7
    ALL_JOINED = STARTED


class PREBATTLE_TYPE:
    NONE = 0
    SQUAD = 1
    TRAINING = 2
    COMPANY = 3
    TOURNAMENT = 4
    CLAN = 5
    UNIT = 6
    CLUBS = 9
    FALLOUT = 10
    EVENT = 11
    STRONGHOLD = 12
    E_SPORT_COMMON = 14
    EPIC = 15
    EPIC_TRAINING = 16
    BATTLE_ROYALE = 17
    BATTLE_ROYALE_TOURNAMENT = 18
    MAPBOX = 19
    MAPS_TRAINING = 20
    RTS = 21
    RTS_TRAINING = 22
    FUN_RANDOM = 23
    COMP7 = 24
    RANKED = 25
    VERSUS_AI = 31000
    RANGE = (
     SQUAD, TRAINING, COMPANY, TOURNAMENT, CLAN, UNIT,
     CLUBS, FALLOUT, EVENT, STRONGHOLD, E_SPORT_COMMON,
     EPIC, EPIC_TRAINING, BATTLE_ROYALE, BATTLE_ROYALE_TOURNAMENT,
     MAPBOX, MAPS_TRAINING, RTS, RTS_TRAINING, FUN_RANDOM, COMP7, VERSUS_AI,
     RANKED)
    LEGACY_PREBATTLES = (
     TRAINING, TOURNAMENT, CLAN, EPIC_TRAINING, RTS_TRAINING)
    SQUAD_PREBATTLES = (
     SQUAD, FALLOUT, EVENT, EPIC, BATTLE_ROYALE, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI, RANKED)
    UNIT_MGR_PREBATTLES = (
     UNIT, SQUAD, CLAN, FALLOUT, EVENT, STRONGHOLD,
     E_SPORT_COMMON, EPIC, BATTLE_ROYALE, BATTLE_ROYALE_TOURNAMENT, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI)
    CREATE_FROM_CLIENT = (
     NONE, UNIT, SQUAD, EPIC, FALLOUT, EVENT, BATTLE_ROYALE, BATTLE_ROYALE_TOURNAMENT, MAPBOX, FUN_RANDOM, COMP7,
     VERSUS_AI, RANKED)
    CREATE_FROM_WEB = (
     UNIT, SQUAD, STRONGHOLD)
    TRAININGS = (
     TRAINING, EPIC_TRAINING, RTS_TRAINING)
    EXTERNAL_PREBATTLES = (
     STRONGHOLD, TOURNAMENT)
    CREATE_EX_FROM_SERVER = (
     SQUAD, CLAN, EPIC, BATTLE_ROYALE, EVENT, BATTLE_ROYALE_TOURNAMENT, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI, RANKED)
    CREATE_EX_FROM_WEB = (
     SQUAD, CLAN)
    JOIN_EX = (
     SQUAD, EPIC, EVENT, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI, RANKED)
    EPIC_PREBATTLES = (
     EPIC, EPIC_TRAINING)
    RTS_PREBATTLES = (
     RTS, RTS_TRAINING)
    REMOVED = (
     COMPANY, CLUBS)
    TRANSFER_PREBATTLES = (
     TRAINING, TOURNAMENT, CLAN, EPIC_TRAINING, RTS_TRAINING, STRONGHOLD)


PREBATTLE_TYPE_NAMES = dict([(v, k) for k, v in PREBATTLE_TYPE.__dict__.iteritems() if not k.startswith(b'_')])

class PREBATTLE_START_TYPE:
    DIRECT = 1
    SQUAD = 2
    RANGE = (
     DIRECT, SQUAD)


class PREBATTLE_ROLE:
    TEAM_READY_1 = 1
    TEAM_READY_2 = 2
    ASSIGNMENT_1 = 4
    ASSIGNMENT_2 = 8
    ASSIGNMENT_1_2 = 16
    SEE_1 = 32
    SEE_2 = 64
    SELF_ASSIGNMENT_1 = 128
    SELF_ASSIGNMENT_2 = 256
    KICK_1 = 512
    KICK_2 = 1024
    CHANGE_ARENA = 2048
    CHANGE_COMMENT = 4096
    OPEN_CLOSE = 8192
    INVITE = 16384
    CHANGE_ARENA_VOIP = 32768
    CHANGE_DIVISION = 65536
    CHANGE_GAMEPLAYSMASK = 131072
    TRAINING_DEFAULT = SEE_1 | SEE_2
    TRAINING_CREATOR = TRAINING_DEFAULT | TEAM_READY_1 | TEAM_READY_2 | ASSIGNMENT_1 | ASSIGNMENT_2 | ASSIGNMENT_1_2 | KICK_1 | KICK_2 | CHANGE_ARENA | CHANGE_COMMENT | OPEN_CLOSE | INVITE | CHANGE_ARENA_VOIP
    SQUAD_DEFAULT = SEE_1
    SQUAD_CREATOR = SQUAD_DEFAULT | TEAM_READY_1 | KICK_1 | INVITE | CHANGE_GAMEPLAYSMASK


class PREBATTLE_STATE:
    IDLE = 0
    IN_QUEUE = 1
    IN_BATTLE = 2


class PREBATTLE_TEAM_STATE:
    NOT_READY = 1
    READY = 2
    LOCKED = 3


class PREBATTLE_ACCOUNT_STATE:
    UNKNOWN = 0
    NOT_READY = 1
    AFK = 2 | NOT_READY
    READY = 4
    IN_BATTLE = 8
    OFFLINE = 16
    MAIN_STATE_MASK = NOT_READY | AFK | READY | IN_BATTLE


PREBATTLE_COMMENT_MAX_LENGTH = 400
PREBATTLE_MAX_OBSERVERS_IN_TEAM = 5
OBSERVERS_BONUS_TYPES = (
 ARENA_BONUS_TYPE.TRAINING, ARENA_BONUS_TYPE.TOURNAMENT,
 ARENA_BONUS_TYPE.TOURNAMENT_CLAN, ARENA_BONUS_TYPE.TOURNAMENT_REGULAR,
 ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING, ARENA_BONUS_TYPE.TOURNAMENT_EVENT,
 ARENA_BONUS_TYPE.TOURNAMENT_COMP7)

class PREBATTLE_ERRORS:
    ROSTER_LIMIT = b'ROSTER_LIMIT'
    INVALID_VEHICLE = b'INVALID_VEHICLE'
    OBSERVERS_LIMIT = b'OBSERVERS_LIMIT'
    PLAYERS_LIMIT = b'PLAYERS_LIMIT'
    INSUFFICIENT_ROLE = b'INSUFFICIENT_ROLE'


class PREBATTLE_UPDATE:
    ROSTER = 1
    PLAYER_ADDED = 2
    PLAYER_REMOVED = 3
    PLAYER_STATE = 4
    PLAYER_ROSTER = 5
    TEAM_STATES = 6
    SETTINGS = 7
    SETTING = 8
    KICKED_FROM_QUEUE = 9
    PROPERTIES = 10
    PROPERTY = 11
    PLAYER_GROUP = 12


class PREBATTLE_CACHE_KEY:
    TYPE = 1
    IS_OPENED = 2
    STATE = 3
    IS_FULL = 4
    PLAYER_COUNT = 5
    CREATOR = 6
    CREATE_TIME = 7
    START_TIME = 8
    COMMENT = 9
    DESCRIPTION = 10
    ARENA_TYPE_ID = 11
    ROUND_LENGTH = 12
    CREATOR_CLAN_DB_ID = 14
    CREATOR_CLAN_ABBREV = 15
    CREATOR_IGR_TYPE = 17
    CREATOR_DB_ID = 18
    CREATOR_BADGES = 19


class PREBATTLE_INVITE_STATE:
    ACTIVE = 1
    ACCEPTED = 2
    DECLINED = 3
    EXPIRED = 4


UNIT_COMMENT_MAX_LENGTH = 100
UNIT_MAX_SEND_INVITES = 100

class UNIT_FINDER:
    RESULTSET_SIZE = 20


class ACCOUNT_TYPE2:
    FIRST_FLAG = 1
    LAST_FLAG = 16384
    ACCOUNT_TYPE_DEFAULT = 16777216
    EXHIBITION = 67108864
    TOURNAMENT = 83886080
    DEMONSTRATOR = 100663296
    DEMONSTRATOR_EXP = 117440512
    EXHIBITION_CLAN = 134217728
    BOOTCAMP = 184549376
    PLAYER_ROAMING = 1677721600
    MODERATOR = 65536
    ADMIN = 131072
    ADMIN_MODERATOR = 196608
    MODERATOR_500 = 458752
    MODERATOR_250 = 524288
    MODERATOR_750 = 589824
    ADMIN_500 = 655360
    ADMIN_250 = 720896
    ADMIN_750 = 786432
    ADMIN_MODERATOR_500 = 851968
    ADMIN_MODERATOR_250 = 917504
    ADMIN_MODERATOR_750 = 983040
    AOGAS = 1114112

    @staticmethod
    def getPrimaryGroup(type):
        return type >> 24 & 255

    @staticmethod
    def getSecondaryGroup(type):
        return type >> 16 & 255

    @staticmethod
    def getFlags(type):
        return type & 65535

    @staticmethod
    def getAttrs(cache, type):
        attrsDct = cache[b'primary'].get(ACCOUNT_TYPE2.getPrimaryGroup(type), None)
        attrsPrimaryGroup = attrsDct[b'attributes']
        attrsDct = cache[b'secondary'].get(ACCOUNT_TYPE2.getSecondaryGroup(type), None)
        attrsSecondaryGroup = attrsDct and attrsDct[b'attributes'] or 0
        return attrsPrimaryGroup | attrsSecondaryGroup

    @staticmethod
    def makeAccountType(primary, secondary, flags):
        return (primary & 255) << 24 | (secondary & 255) << 16 | flags & 65535


class ACCOUNT_FLAGS:
    ALPHA = 1
    CBETA = 2
    OBETA = 4


class ACCOUNT_ATTR:
    RANDOM_BATTLES = 1
    CLAN = 4
    MERCENARY = 8
    RATING = 16
    USER_INFO = 32
    STATISTICS = 64
    ARENA_CHANGE = 128
    CHAT_ADMIN = 256
    ADMIN = 512
    ROAMING = 1024
    DAILY_MULTIPLIED_XP = 2048
    PAYMENTS = 4096
    OUT_OF_SESSION_WALLET = 8192
    EXCLUDED_FROM_FAIRPLAY = 16384
    BATTLE_TYPE_CHANGE = 32768
    DAILY_BONUS_1 = 2097152
    DAILY_BONUS_2 = 4194304
    ALPHA = 536870912
    CBETA = 1073741824
    OBETA = 2147483648L
    PREMIUM = 4294967296L
    AOGAS = 8589934592L
    TUTORIAL_COMPLETED = 17179869184L
    IGR_BASE = 34359738368L
    IGR_PREMIUM = 68719476736L
    SUSPENDED = 137438953472L
    FORCE_ONBOARDING_DISABLED = 274877906944L


class PREMIUM_TYPE:
    NONE = 0
    BASIC = 1
    PLUS = 2
    VIP = 4
    TYPES_SORTED = (
     BASIC, PLUS, VIP)
    ANY = BASIC | PLUS | VIP
    AFFECTING_TYPES = PLUS | VIP

    @classmethod
    def activePremium(cls, premMask):
        for premType in reversed(cls.TYPES_SORTED):
            if premMask & premType:
                return premType

        return cls.NONE

    @classmethod
    def initialData(cls):
        return {(cls.BASIC): 0, 
           (cls.PLUS): 0, 
           (cls.VIP): 0, 
           b'premMask': 0}


class PREMIUM_ENTITLEMENTS:
    BASIC = b'premium'
    PLUS = b'premium_plus'
    VIP = b'premium_vip'
    ALL_TYPES = (
     BASIC, PLUS, VIP)


SUBSCRIPTION_ENTITLEMENT = b'premium_subs'
ENTITLEMENT_TO_PREM_TYPE = {(PREMIUM_ENTITLEMENTS.BASIC): (PREMIUM_TYPE.BASIC), 
   (PREMIUM_ENTITLEMENTS.PLUS): (PREMIUM_TYPE.PLUS), 
   (PREMIUM_ENTITLEMENTS.VIP): (PREMIUM_TYPE.VIP)}
PREM_TYPE_TO_ENTITLEMENT = {v: k for k, v in ENTITLEMENT_TO_PREM_TYPE.iteritems()}

class ENTITLEMENT_OPS:
    GRANT = b'grant'
    GRANT_WITHOUT_EXCESS = b'grant_without_excess'
    CONSUME = b'consume'
    CONSUME_GREEDY = b'consume_greedy'
    ALL = (
     GRANT, GRANT_WITHOUT_EXCESS, CONSUME, CONSUME_GREEDY)
    GRANT_ALL = (GRANT, GRANT_WITHOUT_EXCESS)
    CONSUME_ALL = (CONSUME, CONSUME_GREEDY)


class PREM_BONUS_TYPES:
    CREDITS = 0
    XP = 1
    TMEN_XP = 2
    DYN_CURRENCIES = 3


class PremiumConfigs(object):
    DAILY_BONUS = b'additionalBonus_config'
    PREM_QUESTS = b'premQuests_config'
    PIGGYBANK = b'piggyBank_config'
    IS_PREFERRED_MAPS_ENABLED = b'isPreferredMapsEnabled'
    PREFERRED_MAPS = b'preferredMaps_config'
    PREM_SQUAD = b'premSquad_config'


DAILY_QUESTS_CONFIG = b'daily_quests_config'
DOG_TAGS_CONFIG = b'dog_tags_config'
RENEWABLE_SUBSCRIPTION_CONFIG = b'renewable_subscription_config'
PLAYER_SUBSCRIPTIONS_CONFIG = b'player_subscriptions_config'
IS_LOOT_BOXES_ENABLED = b'isLootBoxesEnabled'
SENIORITY_AWARDS_CONFIG = b'seniority_awards_config'
MAGNETIC_AUTO_AIM_CONFIG = b'magnetic_auto_aim_config'
BATTLE_NOTIFIER_CONFIG = b'battle_notifier_config'
BATTLE_ACHIEVEMENTS_CONFIG = b'battle_achievements_config'
ACTIVE_TEST_CONFIRMATION_CONFIG = b'active_test_confirmation_config'
TOURNAMENT_CONFIG = b'tournament_config'
MISC_GUI_SETTINGS = b'misc_gui_settings'
META_GAME_SETTINGS = b'meta_game_settings'
MAPS_TRAINING_ENABLED_KEY = b'isMapsTrainingEnabled'
OFFERS_ENABLED_KEY = b'isOffersEnabled'
OPT_DEVICES_RESTORE_SETTING = b'isOptionalDeviceRestoreEnabled'

class Configs(enum.Enum):
    BATTLE_ROYALE_CONFIG = b'battle_royale_config'
    EPIC_CONFIG = b'epic_config'
    MAPBOX_CONFIG = b'mapbox_config'
    GIFTS_CONFIG = b'gifts_config'
    RESOURCE_WELL = b'resource_well_config'
    FUN_RANDOM_CONFIG = b'fun_random_config'
    CRYSTAL_REWARDS_CONFIG = b'crystal_rewards_config'
    CUSTOMIZATION_QUESTS = b'customizationQuests'
    UI_LOGGING = b'ui_logging_config'
    BATTLE_MATTERS_CONFIG = b'battle_matters_config'
    COLLECTIVE_GOAL_ENTRY_POINT_CONFIG = b'collective_goal_entry_point_config'
    COLLECTIVE_GOAL_MARATHONS_CONFIG = b'collective_goal_marathons_config'
    UNIVERSAL_FLAG_ENTRY_POINT_CONFIG = b'universal_flag_entry_point_config'
    PERIPHERY_ROUTING_CONFIG = b'periphery_routing_config'
    COMP7_CONFIG = b'comp7_config'
    COMP7_RANKS_CONFIG = b'comp7_ranks_config'
    COMP7_REWARDS_CONFIG = b'comp7_rewards_config'
    COMP7_SKILLS_CONFIG = b'comp7_skills_config'
    PERSONAL_RESERVES_CONFIG = b'personal_reserves_config'
    PLAY_LIMITS_CONFIG = b'play_limits_config'
    PRE_MODERATION_CONFIG = b'pre_moderation_config'
    SPAM_PROTECTION_CONFIG = b'spam_protection_config'
    ARMORY_YARD_CONFIG = b'armory_yard_config'
    COLLECTIONS_CONFIG = b'collections_config'
    WINBACK_CONFIG = b'winback_config'
    ACHIEVEMENTS20_CONFIG = b'achievements20_config'
    AB_FEATURE_TEST = b'ab_feature_test'
    LIMITED_UI_CONFIG = b'limited_ui_config'
    REFERRAL_PROGRAM_CONFIG = b'referral_program_config'
    RESTORE_CONFIG = b'restore_config'
    DEBUT_BOXES_CONFIG = b'debut_boxes_config'
    VERSUS_AI_CONFIG = b'versus_ai_config'
    MAPS_IN_DEVELOPMENT_CONFIG = b'maps_in_development'
    TRIGGER_SYSTEM_CONFIG = b'trigger_system_config'
    EARLY_ACCESS_CONFIG = b'early_access_config'
    LOOTBOX_KEYS_CONFIG = b'lootBoxKeys_config'
    RANDOM_BATTLES_CONFIG = b'random_battles_config'
    MODE_SELECTOR_CONFIG = b'mode_selector_config'
    PARAGONS_CONFIG = b'paragons_config'
    BLACK_MARKET_CONFIG = b'black_market_config'
    INGAME_BROWSER_EVENT_CONFIG = b'ingame_browser_event_config'
    LOOTBOX_STATISTICS_CONFIG = b'lootbox_statistics_config'
    BATTLE_CONTEXT_HINTS_CONFIG = b'battle_context_hints_config'
    SETTINGS_LOGGING_CONFIG = b'settings_logging_config'
    RANDOM_MATCHMAKER_CONFIG = b'random_matchmaker_config'
    BATTLE_MODIFIER_CONFIG = b'battle_modifiers_config'
    NEWBIE_START_PAGE_CONFIG = b'newbie_start_page_config'
    STALL_CONFIG = b'stall_config'
    CONTROL_POINT_OVERRIDE_CONFIG = b'control_point_override_config'
    NEWBIE_CHAT_LOCK_CONFIG = b'newbie_chat_lock_config'


INBATTLE_CONFIGS = [
 b'spgRedesignFeatures',
 b'ranked_config',
 b'battle_royale_config',
 b'epic_config',
 b'vehicle_post_progression_config',
 Configs.COMP7_CONFIG.value,
 Configs.FUN_RANDOM_CONFIG.value,
 Configs.BATTLE_CONTEXT_HINTS_CONFIG.value,
 Configs.COMP7_SKILLS_CONFIG.value]

class RESTRICTION_TYPE:
    NONE = 0
    BAN = 1
    CHAT_BAN = 3
    CLAN = 5
    ARENA_BAN = 101
    RANGE = (
     BAN, CHAT_BAN, CLAN)
    LOCAL_RANGE = (ARENA_BAN,)


class RESTRICTION_SOURCE:
    UNKNOWN = 0
    SERVER = 1
    CLIENT = 2
    BACKYARD = 3
    MIGRATOR = 4
    FORUM = 5
    PAYMENT_SYSTEM = 6
    WARGAG = 7
    SUPPORT = 8
    WGRS = 9
    WGCOMMENTS = 10
    XMPPCS = 11
    WGPS = 12
    WGATS = 13
    ADIOS = 14
    PADRE = 15
    AUTOMAGIC_SCRIPTS = 16
    CSA = 17
    SPA = 18


SPA_RESTR_NAME_TO_RESTR_TYPE = {b'game': (RESTRICTION_TYPE.BAN), 
   b'chat': (RESTRICTION_TYPE.CHAT_BAN), 
   b'clan': (RESTRICTION_TYPE.CLAN)}
RESTR_TYPE_TO_SPA_NAME = dict((x[1], x[0]) for x in SPA_RESTR_NAME_TO_RESTR_TYPE.iteritems())
CURRENT_GAME_ID = b'%st' % (b'wo' if CURRENT_REALM else b'm')
GAME_ROOT_DIR_NAME = CURRENT_GAME_ID

class SPA_ATTRS:
    ANONYM_RESTRICTED = b'/%s/game/anonym_restricted/' % CURRENT_GAME_ID
    GOLFISH_BONUS_APPLIED = b'/common/goldfish_bonus_applied/'
    BOOTCAMP_DISABLED = b'/%s/game/bootcamp_disabled/' % CURRENT_GAME_ID
    LOGGING_ENABLED = b'/%s/game/logging_enabled/' % CURRENT_GAME_ID
    BOOTCAMP_VIDEO_DISABLED = b'/%s/game/bc_video_disabled/' % CURRENT_GAME_ID
    STEAM_ALLOW = b'/%s/steam/allow/' % CURRENT_GAME_ID
    RSS = b'/%s/game/service/rss/' % CURRENT_GAME_ID
    USER_COUNTRY = b'user_stated_country'

    @staticmethod
    def toClientAttrs():
        return [SPA_ATTRS.LOGGING_ENABLED,
         SPA_ATTRS.BOOTCAMP_DISABLED,
         SPA_ATTRS.BOOTCAMP_VIDEO_DISABLED,
         SPA_ATTRS.USER_COUNTRY]


class CLAN_MEMBER_FLAGS(object):
    LEADER = 1
    VICE_LEADER = 2
    RECRUITER = 4
    TREASURER = 8
    DIPLOMAT = 16
    COMMANDER = 32
    PRIVATE = 64
    RECRUIT = 128
    STAFF = 256
    JUNIOR = 512
    RESERVIST = 1024
    MAY_CHANGE_SETTINGS = LEADER | VICE_LEADER
    MAY_EDIT_RECRUIT_PROFILE = LEADER | VICE_LEADER | STAFF | RECRUITER
    MAY_CHANGE_ROLE = LEADER | VICE_LEADER | STAFF | COMMANDER
    MAY_CHANGE_COMMANDER = LEADER
    MAY_HANDLE_INVITES = LEADER | VICE_LEADER | STAFF | RECRUITER
    MAY_INVITE = LEADER | VICE_LEADER | STAFF | RECRUITER
    MAY_REMOVE_MEMBERS = LEADER | VICE_LEADER | STAFF
    MAY_REMOVE_CLAN = LEADER
    MAY_ACTIVATE_ORDER = LEADER | VICE_LEADER | STAFF | COMMANDER
    MAY_EXCHANGE_MONEY = LEADER | VICE_LEADER | STAFF | COMMANDER | DIPLOMAT | TREASURER | RECRUITER | JUNIOR | PRIVATE


class CLAN_ROLES(object):
    LEADER = b'commander'
    VICE_LEADER = b'executive_officer'
    RECRUITER = b'recruitment_officer'
    TREASURER = b'quartermaster'
    DIPLOMAT = b'intelligence_officer'
    COMMANDER = b'combat_officer'
    PRIVATE = b'private'
    RECRUIT = b'recruit'
    STAFF = b'personnel_officer'
    JUNIOR = b'junior_officer'
    RESERVIST = b'reservist'
    FLAGS_TO_ROLES = {(CLAN_MEMBER_FLAGS.LEADER): LEADER, 
       (CLAN_MEMBER_FLAGS.VICE_LEADER): VICE_LEADER, 
       (CLAN_MEMBER_FLAGS.RECRUITER): RECRUITER, 
       (CLAN_MEMBER_FLAGS.TREASURER): TREASURER, 
       (CLAN_MEMBER_FLAGS.DIPLOMAT): DIPLOMAT, 
       (CLAN_MEMBER_FLAGS.COMMANDER): COMMANDER, 
       (CLAN_MEMBER_FLAGS.PRIVATE): PRIVATE, 
       (CLAN_MEMBER_FLAGS.RECRUIT): RECRUIT, 
       (CLAN_MEMBER_FLAGS.STAFF): STAFF, 
       (CLAN_MEMBER_FLAGS.JUNIOR): JUNIOR, 
       (CLAN_MEMBER_FLAGS.RESERVIST): RESERVIST}

    @classmethod
    def getRole(cls, memberFlags):
        for i in range(len(cls.FLAGS_TO_ROLES)):
            flag = memberFlags & 1 << i
            if flag:
                return cls.FLAGS_TO_ROLES[flag]

        return b''

    @classmethod
    def getFlagByRole(cls, memberRole):
        for flag, role in cls.FLAGS_TO_ROLES.iteritems():
            if role == memberRole:
                return flag

        return


class AIMING_MODE:
    SHOOTING = 1
    TARGET_LOCK = 16
    USER_DISABLED = 256


class VEHICLE_SETTING:
    CURRENT_SHELLS = 0
    NEXT_SHELLS = 1
    AUTOROTATION_ENABLED = 2
    SIEGE_MODE_ENABLED = 3
    ACTIVATE_EQUIPMENT = 16
    RELOAD_PARTIAL_CLIP = 17


class VEHICLE_TTC_ASPECTS:
    DEFAULT = 0
    WHEN_MOVING = 1
    WHEN_STILL = 2
    WHEN_SIEGE = 3
    RANGE = (
     DEFAULT, WHEN_MOVING, WHEN_STILL, WHEN_SIEGE)


class VEHICLE_MISC_STATUS:
    OTHER_VEHICLE_DAMAGED_DEVICES_VISIBLE = 0
    IS_OBSERVED_BY_ENEMY = 1
    _NOT_USED = 2
    VEHICLE_IS_OVERTURNED = 3
    VEHICLE_DROWN_WARNING = 4
    IN_DEATH_ZONE = 5
    DESTROYED_DEVICE_IS_REPAIRING = 7
    SIEGE_MODE_STATE_CHANGED = 9
    BURNOUT_WARNING = 10
    BURNOUT_UNAVAILABLE_DUE_TO_BROKEN_ENGINE = 11
    DUALGUN_CHARGER_STATE = 14
    THERMAL_VISION_WARNING = 15


class DUALGUN_CHARGER_STATUS:
    BEFORE_PREPARING = -1
    APPLIED = 0
    CANCELED = 1
    PREPARING = 2
    UNAVAILABLE = 3


class DUALGUN_CHARGER_ACTION_TYPE:
    CANCEL = 0
    START_WITH_DELAY = 1
    START_IMMEDIATELY = 2


class EQUIPMENT_STAGES:
    NOT_RUNNING = 0
    DEPLOYING = 1
    UNAVAILABLE = 2
    READY = 3
    PREPARING = 4
    ACTIVE = 5
    COOLDOWN = 6
    SHARED_COOLDOWN = 7
    EXHAUSTED = 255
    ALL = (
     NOT_RUNNING, DEPLOYING, UNAVAILABLE, READY, PREPARING, ACTIVE, COOLDOWN, SHARED_COOLDOWN, EXHAUSTED)

    @classmethod
    def toString(cls, value):
        return {0: b'notrunning', 
           (cls.DEPLOYING): b'deploying', 
           (cls.UNAVAILABLE): b'unavailable', 
           (cls.READY): b'ready', 
           (cls.PREPARING): b'preparing', 
           (cls.ACTIVE): b'active', 
           (cls.COOLDOWN): b'cooldown', 
           (cls.EXHAUSTED): b'exhausted'}.get(value)


class DEVELOPMENT_INFO:
    ATTACK_RESULT = 1
    FIRE_RESULT = 2
    BONUSES = 3
    VISIBILITY = 4
    VEHICLE_ATTRS = 5
    QUERY_RESULT = 6
    EXPLOSION_RAY = 7
    FRONTLINE = 9
    SERVER_DEBUG = 10
    DEV_DATA_UPDATE = 11
    ENABLE_SENDING_VEH_ATTRS_TO_CLIENT = False


class AMMOBAY_DESTRUCTION_MODE:
    POWDER_BURN_OFF = 0
    POWDER_EXPLOSION = 1
    HE_DETONATION = 2


class SPECIAL_VEHICLE_HEALTH:
    DESTR_BY_FALL_RAMMING = -2
    FUEL_EXPLODED = -3
    AMMO_BAY_DESTROYED = -5
    TURRET_DETACHED = -13

    @staticmethod
    def IS_DESTR_BY_FALL_RAMMING(health):
        return health < 0 and health | SPECIAL_VEHICLE_HEALTH.DESTR_BY_FALL_RAMMING == SPECIAL_VEHICLE_HEALTH.DESTR_BY_FALL_RAMMING

    @staticmethod
    def IS_FUEL_EXPLODED(health):
        return health < 0 and health | SPECIAL_VEHICLE_HEALTH.FUEL_EXPLODED == SPECIAL_VEHICLE_HEALTH.FUEL_EXPLODED

    @staticmethod
    def IS_AMMO_BAY_DESTROYED(health):
        return health < 0 and health | SPECIAL_VEHICLE_HEALTH.AMMO_BAY_DESTROYED == SPECIAL_VEHICLE_HEALTH.AMMO_BAY_DESTROYED

    @staticmethod
    def IS_TURRET_DETACHED(health):
        return health < 0 and health | SPECIAL_VEHICLE_HEALTH.TURRET_DETACHED == SPECIAL_VEHICLE_HEALTH.TURRET_DETACHED


class AOI:
    ENABLE_MANUAL_RULES = True
    VEHICLE_CIRCULAR_AOI_RADIUS = 565.0
    CIRCULAR_AOI_MARGIN = 5.0
    VEHICLE_CIRCULAR_AOI_RADIUS_HYSTERESIS_MARGIN = VEHICLE_CIRCULAR_AOI_RADIUS + CIRCULAR_AOI_MARGIN
    UPDATE_INTERVAL = 1


class ATTACK_REASON(object):
    SHOT = b'shot'
    FIRE = b'fire'
    RAM = b'ramming'
    WORLD_COLLISION = b'world_collision'
    DEATH_ZONE = b'death_zone'
    DROWNING = b'drowning'
    GAS_ATTACK = b'gas_attack'
    OVERTURN = b'overturn'
    MANUAL = b'manual'
    ARTILLERY_PROTECTION = b'artillery_protection'
    ARTILLERY_SECTOR = b'artillery_sector'
    BOMBERS = b'bombers'
    RECOVERY = b'recovery'
    ARTILLERY_EQ = b'artillery_eq'
    BOMBER_EQ = b'bomber_eq'
    MINEFIELD_EQ = b'minefield_eq'
    SPAWNED_BOT_EXPLOSION = b'spawned_bot_explosion'
    BERSERKER = b'berserker_eq'
    SMOKE = b'smoke'
    CORRODING_SHOT = b'corrodingShot'
    ADAPTATION_HEALTH_RESTORE = b'AdaptationHealthRestore'
    THUNDER_STRIKE = b'thunderStrike'
    FIRE_CIRCLE = b'fireCircle'
    CLING_BRANDER = b'clingBrander'
    CLING_BRANDER_RAM = b'ram_cling_brander'
    BRANDER_RAM = b'ram_brander'
    FORT_ARTILLERY_EQ = b'fort_artillery_eq'
    STATIC_DEATH_ZONE = b'static_deathzone'
    CGF_WORLD = b'cgf_world'
    AUTOSHOOT = b'autoshoot'
    NONE = b'none'

    @classmethod
    def getIndex(cls, attackReason):
        return ATTACK_REASON_INDICES[attackReason]


ATTACK_REASONS = (
 ATTACK_REASON.SHOT, ATTACK_REASON.FIRE, ATTACK_REASON.RAM, ATTACK_REASON.WORLD_COLLISION,
 ATTACK_REASON.DEATH_ZONE, ATTACK_REASON.DROWNING, ATTACK_REASON.GAS_ATTACK,
 ATTACK_REASON.OVERTURN, ATTACK_REASON.MANUAL,
 ATTACK_REASON.ARTILLERY_PROTECTION, ATTACK_REASON.ARTILLERY_SECTOR, ATTACK_REASON.BOMBERS,
 ATTACK_REASON.RECOVERY, ATTACK_REASON.ARTILLERY_EQ, ATTACK_REASON.BOMBER_EQ, ATTACK_REASON.MINEFIELD_EQ,
 ATTACK_REASON.NONE,
 ATTACK_REASON.SPAWNED_BOT_EXPLOSION, ATTACK_REASON.BERSERKER, ATTACK_REASON.SMOKE,
 ATTACK_REASON.CORRODING_SHOT, ATTACK_REASON.ADAPTATION_HEALTH_RESTORE,
 ATTACK_REASON.THUNDER_STRIKE, ATTACK_REASON.FIRE_CIRCLE, ATTACK_REASON.CLING_BRANDER,
 ATTACK_REASON.CLING_BRANDER_RAM, ATTACK_REASON.BRANDER_RAM,
 ATTACK_REASON.FORT_ARTILLERY_EQ, ATTACK_REASON.STATIC_DEATH_ZONE, ATTACK_REASON.AUTOSHOOT,
 ATTACK_REASON.CGF_WORLD)
ATTACK_REASON_INDICES = dict((value, index) for index, value in enumerate(ATTACK_REASONS))
BOT_RAM_REASONS = (
 ATTACK_REASON.BRANDER_RAM, ATTACK_REASON.CLING_BRANDER_RAM)
WORLD_ATTACK_REASONS = (ATTACK_REASON.WORLD_COLLISION, ATTACK_REASON.CGF_WORLD)
DEATH_REASON_ALIVE = -1

class REPAIR_TYPE:
    AUTO = 0
    KIT = 1


class VEHICLE_HIT_EFFECT:
    ARMOR_PIERCED_NO_DAMAGE = 0
    INTERMEDIATE_RICOCHET = 1
    FINAL_RICOCHET = 2
    ARMOR_NOT_PIERCED = 3
    ARMOR_PIERCED = 4
    CRITICAL_HIT = 5
    ARMOR_PIERCED_DEVICE_DAMAGED = 6
    MAX_CODE = ARMOR_PIERCED_DEVICE_DAMAGED
    RICOCHETS = (INTERMEDIATE_RICOCHET, FINAL_RICOCHET)
    PIERCED_HITS = (ARMOR_PIERCED_NO_DAMAGE, ARMOR_PIERCED, CRITICAL_HIT, ARMOR_PIERCED_DEVICE_DAMAGED)


class VEHICLE_HIT_FLAGS:
    VEHICLE_KILLED = 1
    VEHICLE_WAS_DEAD_BEFORE_ATTACK = 2
    FIRE_STARTED = 4
    RICOCHET = 8
    MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_PROJECTILE = 16
    MATERIAL_WITH_POSITIVE_DF_NOT_PIERCED_BY_PROJECTILE = 32
    ARMOR_WITH_ZERO_DF_PIERCED_BY_PROJECTILE = 64
    ARMOR_WITH_ZERO_DF_NOT_PIERCED_BY_PROJECTILE = 128
    DEVICE_PIERCED_BY_PROJECTILE = 256
    DEVICE_NOT_PIERCED_BY_PROJECTILE = 512
    DEVICE_DAMAGED_BY_PROJECTILE = 1024
    CHASSIS_DAMAGED_BY_PROJECTILE = 2048
    GUN_DAMAGED_BY_PROJECTILE = 4096
    MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_EXPLOSION = 8192
    ARMOR_WITH_ZERO_DF_PIERCED_BY_EXPLOSION = 16384
    DEVICE_PIERCED_BY_EXPLOSION = 32768
    DEVICE_DAMAGED_BY_EXPLOSION = 65536
    CHASSIS_DAMAGED_BY_EXPLOSION = 131072
    GUN_DAMAGED_BY_EXPLOSION = 262144
    CHASSIS_DAMAGED_BY_RAMMING = 524288
    ATTACK_IS_DIRECT_PROJECTILE = 1048576
    ATTACK_IS_EXTERNAL_EXPLOSION = 2097152
    STUN_STARTED = 4194304
    ATTACK_IS_RICOCHET_PROJECTILE = 8388608
    ATTACK_IS_COMPRESSION = 16777216
    IS_ANY_DAMAGE_MASK = MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_PROJECTILE | MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_EXPLOSION | DEVICE_PIERCED_BY_PROJECTILE | DEVICE_PIERCED_BY_EXPLOSION
    IS_VEHICLE_DAMAGE_MASK = MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_PROJECTILE | MATERIAL_WITH_POSITIVE_DF_PIERCED_BY_EXPLOSION
    IS_ANY_ATTACK_MASK = ATTACK_IS_DIRECT_PROJECTILE | ATTACK_IS_EXTERNAL_EXPLOSION | ATTACK_IS_RICOCHET_PROJECTILE | ATTACK_IS_COMPRESSION
    IS_ANY_PIERCING_MASK = IS_ANY_DAMAGE_MASK | ARMOR_WITH_ZERO_DF_PIERCED_BY_PROJECTILE | ARMOR_WITH_ZERO_DF_PIERCED_BY_EXPLOSION


VEHICLE_HIT_FLAGS_BY_NAME = dict([(k, v) for k, v in VEHICLE_HIT_FLAGS.__dict__.iteritems() if not k.startswith(b'_')])
FIRE_NOTIFICATION_CODES = (b'DEVICE_STARTED_FIRE_AT_SHOT', b'DEVICE_STARTED_FIRE_AT_RAMMING', b'FIRE_STOPPED')
FIRE_NOTIFICATION_INDICES = dict((x[1], x[0]) for x in enumerate(FIRE_NOTIFICATION_CODES))
DAMAGE_INFO_CODES = (b'DEVICE_CRITICAL', b'DEVICE_DESTROYED', b'TANKMAN_HIT', b'DEVICE_CRITICAL_AT_SHOT', b'DEVICE_DESTROYED_AT_SHOT', b'DEVICE_CRITICAL_AT_RAMMING', b'DEVICE_DESTROYED_AT_RAMMING', b'TANKMAN_HIT_AT_SHOT', b'DEATH_FROM_DEVICE_EXPLOSION_AT_SHOT', b'DEVICE_CRITICAL_AT_FIRE', b'DEVICE_DESTROYED_AT_FIRE', b'DEVICE_CRITICAL_AT_WORLD_COLLISION', b'DEVICE_DESTROYED_AT_WORLD_COLLISION', b'DEVICE_CRITICAL_AT_DROWNING', b'DEVICE_DESTROYED_AT_DROWNING', b'DEVICE_REPAIRED_TO_CRITICAL', b'DEVICE_REPAIRED', b'TANKMAN_HIT_AT_WORLD_COLLISION', b'TANKMAN_HIT_AT_DROWNING', b'TANKMAN_RESTORED', b'DEATH_FROM_DEVICE_EXPLOSION_AT_FIRE', b'ENGINE_CRITICAL_AT_UNLIMITED_RPM', b'ENGINE_DESTROYED_AT_UNLIMITED_RPM', b'ENGINE_CRITICAL_AT_BURNOUT', b'ENGINE_DESTROYED_AT_BURNOUT', b'DEATH_FROM_SHOT', b'DEATH_FROM_INACTIVE_CREW_AT_SHOT', b'DEATH_FROM_RAMMING', b'DEATH_FROM_MINE_EXPLOSION', b'DEATH_FROM_FIRE', b'DEATH_FROM_INACTIVE_CREW', b'DEATH_FROM_DROWNING', b'DEATH_FROM_WORLD_COLLISION', b'DEATH_FROM_INACTIVE_CREW_AT_WORLD_COLLISION', b'DEATH_FROM_DEATH_ZONE', b'DEATH_FROM_STATIC_DEATH_ZONE', b'DEATH_FROM_GAS_ATTACK', b'DEATH_FROM_OVERTURN', b'DEATH_FROM_ARTILLERY_PROTECTION', b'DEATH_FROM_ARTILLERY_SECTOR', b'DEATH_FROM_BOMBER', b'DEATH_FROM_RECOVERY', b'DEATH_FROM_KAMIKAZE', b'DEATH_FROM_FIRE_CIRCLE', b'DEATH_FROM_THUNDER_STRIKE', b'DEATH_FROM_CORRODING_SHOT', b'DEATH_FROM_CLING_BRANDER')

class IGR_TYPE:
    NONE = 0
    BASE = 1
    PREMIUM = 2
    RANGE = (
     BASE, PREMIUM)


class EVENT_TYPE:
    ACTION = 1
    BATTLE_QUEST = 2
    TOKEN_QUEST = 3
    PERSONAL_QUEST = 6
    REF_SYSTEM_QUEST_DEPRECATED = 7
    PERSONAL_MISSION = 8
    GROUP = 9
    TUTORIAL = 11
    MOTIVE_QUEST = 12
    RANKED_QUEST = 13
    ELEN_QUEST = 14
    HANGAR_QUEST = 15
    NT_QUEST = 16
    C11N_PROGRESSION = 17
    LAST = 17
    NAME_TO_TYPE = {b'battleQuest': BATTLE_QUEST, 
       b'tokenQuest': TOKEN_QUEST, 
       b'personalQuest': PERSONAL_QUEST, 
       b'personalMissionQuest': PERSONAL_MISSION, 
       b'group': GROUP, 
       b'tutorial': TUTORIAL, 
       b'motiveQuest': MOTIVE_QUEST, 
       b'rankedQuest': RANKED_QUEST, 
       b'elenQuest': ELEN_QUEST, 
       b'hangarQuest': HANGAR_QUEST, 
       b'NTQuest': NT_QUEST, 
       b'c11nProgression': C11N_PROGRESSION}
    TYPE_TO_NAME = dict(zip(NAME_TO_TYPE.values(), NAME_TO_TYPE.keys()))
    QUEST_RANGE = (
     BATTLE_QUEST, TOKEN_QUEST, PERSONAL_QUEST, PERSONAL_MISSION, GROUP, MOTIVE_QUEST, RANKED_QUEST,
     HANGAR_QUEST, NT_QUEST)
    LIKE_BATTLE_QUESTS = (BATTLE_QUEST, PERSONAL_QUEST, PERSONAL_MISSION,
     MOTIVE_QUEST, RANKED_QUEST, NT_QUEST)
    LIKE_TOKEN_QUESTS = (TOKEN_QUEST,)
    ONE_BONUS_QUEST = (TOKEN_QUEST, PERSONAL_MISSION, RANKED_QUEST)
    QUEST_WITH_DYNAMIC_CLIENT_DATA = (PERSONAL_QUEST,)
    SHARED_QUESTS = (
     PERSONAL_MISSION, MOTIVE_QUEST)
    QUESTS_WITH_SHOP_BUTTON = (BATTLE_QUEST, TOKEN_QUEST, PERSONAL_QUEST)
    QUEST_WITHOUT_DYNAMIC_UPDATE = (PERSONAL_MISSION, NT_QUEST)
    QUEST_USE_FOR_C11N_PROGRESS = (TOKEN_QUEST, BATTLE_QUEST)
    MISC_DATA_RANGE = (BATTLE_QUEST, TOKEN_QUEST)


class QUEST_DATA_IDX:
    QUESTS = 0
    IN_VARS = 1
    OUT_VARS = 2
    ALIASES = 3
    KILLED_CLAN_SETS = 4
    VEHICLE_SETS = 5
    ACHIEVEMENT_SETS = 6
    IN_CLAN_SETS = 7
    CLAN_CAMOUFLAGES = 8
    MISC = 9
    TOKEN2IDXS = 10
    INVENTORY_SETS = 11
    EXTRA_PARAMS = 12


class QUEST_SOURCE:
    DYNAMIC = 1
    STATIC = 2
    AUTO_GENERATED = 3
    ALIAS_PREFIXES = {DYNAMIC: b'd', 
       STATIC: b's', 
       AUTO_GENERATED: b'g'}


class QUEST_RUN_FLAGS:
    POSTBATTLE = 1
    LOGIN = 2
    CLICK = 3
    POSTRANKED = 4
    RANGE = (
     POSTBATTLE, LOGIN, CLICK, POSTRANKED)
    NAME_TO_TYPE = {b'postbattle': POSTBATTLE, 
       b'login': LOGIN, 
       b'click': CLICK, 
       b'postranked': POSTRANKED}
    TYPE_TO_NAME = dict((x[1], x[0]) for x in NAME_TO_TYPE.iteritems())


DEFAULT_QUEST_START_TIME = 1
DEFAULT_QUEST_FINISH_TIME = 4102444800L
PERSONAL_MISSION_FREE_TOKEN_NAME = b'free_award_list'
PERSONAL_MISSION_2_FREE_TOKEN_NAME = b'free_award_list_2'
PERSONAL_MISSION_3_FREE_TOKEN_NAME = b'free_award_list_3'
PERSONAL_MISSION_FREE_TOKEN_EXPIRE = 4104777660L
PERSONAL_MISSION_PAWN_COST = 1
PERSONAL_MISSION_FINAL_PAWN_COST = 4
PERSONAL_MISSION_2_FINAL_PAWN_COST = 3
PERSONAL_MISSION_3_FINAL_PAWN_COST = 2
PERSONAL_MISSION_FREE_TOKENS_LIMIT = 21
RESOURCE_TOKEN_PREFIX = b'resource:'
CURRENCY_TOKEN_PREFIX = b'currency:'
PREMIUM_TOKEN_PREFIX = b'prem_acc'
EPIC_ABILITY_PTS_NAME = b'abilityPts'
OFFER_TOKEN_PREFIX = b'offer:'
ENDLESS_TOKEN_TIME_STRING = b'28.01.2100 00:01'
ENDLESS_TOKEN_TIME = int(calendar.timegm(time.strptime(ENDLESS_TOKEN_TIME_STRING, b'%d.%m.%Y %H:%M')))
LOOTBOX_TOKEN_PREFIX = b'lootBox:'
LOOTBOX_LIMIT_ITEM_PREFIX = b'lb_limit_item:'
LOOTBOX_KEY_PREFIX = b'lb_key:'
LOOTBOX_MTL_CATEGORY = b'mtl_universal'
VERY_BIG_TIME = int(time.mktime(datetime.datetime(2050, 1, 1).timetuple()))
TWITCH_TOKEN_PREFIX = b'token:twitch'
CUSTOMIZATION_PROGRESS_PREFIX = b'cust_progress_'
LOOTBOX_CUSTOMIZATION_PROGRESS_PREFIX = b'lb_cust_progress'
LOOTBOX_CUSTOMIZATION_PROGRESS_FORMAT = LOOTBOX_CUSTOMIZATION_PROGRESS_PREFIX + b':{}_{}:{}'
EMAIL_CONFIRMATION_QUEST_ID = b'email_confirmation'
EMAIL_CONFIRMATION_TOKEN_NAME = b'acc_completion:email_confirm'
DEMO_ACCOUNT_ATTR = b'isDemoAccount'
HAS_PM1_COMPLETED_TOKEN = b'has_completed_pm1'
HAS_PM2_COMPLETED_TOKEN = b'has_completed_pm2'
HAS_PM3_COMPLETED_TOKEN = b'has_completed_pm3'
LINKED_SET_UNFINISHED_TOKEN = b'linkedset_unfinished'
FREE_PREMIUM_CREW_LOG_EXT_PREFIX = b'free_premium_crew:level:'
FREE_DROP_SKILL_TOKEN = b'drop_skill:free'
VERSUS_AI_PROGRESSION_TOKEN_PREFIX = b'img:versus_ai_'
WINBACK_SELECTOR_HINT_TOKEN = b'winback:show_selector_hint'

class QUEST_CODE_TYPE:
    XMLAUTOGENERATED = 0
    HANDCODED = 1


DAMAGE_INFO_INDICES = dict((x[1], x[0]) for x in enumerate(DAMAGE_INFO_CODES))
CLIENT_INACTIVITY_TIMEOUT = 40

class CHAT_LOG:
    NONE = 0
    MESSAGES = 1
    ACTIONS = 2


CHAT_MESSAGE_MAX_LENGTH = 1024
CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE = 140

class PROMO_CUTOUT:
    OFF = 0
    ON = 1


VEHICLE_CLASSES = (b'lightTank', b'mediumTank', b'heavyTank', b'SPG', b'AT-SPG')
VEHICLE_CLASS_INDICES = dict((x[1], x[0]) for x in enumerate(VEHICLE_CLASSES))
VEHICLE_CLASSES_DETECTED_BY_ENEMY_SHOT_PREDICTOR = {
 b'SPG'}
MIN_VEHICLE_LEVEL = 1
MAX_VEHICLE_LEVEL = 11
VEHICLE_NO_INV_ID = -1

class TEAMS_IN_ARENA:
    MAX_TEAMS = 40
    MIN_TEAMS = 2
    ANY_TEAM = 0


class QUEUE_TYPE:
    UNKNOWN = 0
    RANDOMS = 1
    COMPANIES = 2
    VOLUNTEERS = 3
    UNITS = 5
    EVENT_BATTLES = 7
    UNIT_ASSEMBLER = 8
    SPEC_BATTLE = 13
    FALLOUT_CLASSIC = 14
    FALLOUT_MULTITEAM = 15
    STRONGHOLD_UNITS = 16
    RANKED = 17
    BOOTCAMP = 18
    EPIC = 19
    TOURNAMENT_UNITS = 20
    BATTLE_ROYALE = 21
    BATTLE_ROYALE_TOURNAMENT = 22
    MAPBOX = 23
    MAPS_TRAINING = 24
    RTS = 25
    RTS_1x1 = 26
    RTS_BOOTCAMP = 27
    FUN_RANDOM = 28
    COMP7 = 29
    VERSUS_AI = 31000
    FALLOUT = (
     FALLOUT_CLASSIC, FALLOUT_MULTITEAM)
    ALL = (
     RANDOMS, COMPANIES, VOLUNTEERS, UNITS, EVENT_BATTLES, UNIT_ASSEMBLER, SPEC_BATTLE, FALLOUT,
     FALLOUT_CLASSIC, FALLOUT_MULTITEAM, STRONGHOLD_UNITS, RANKED, BOOTCAMP, EPIC, TOURNAMENT_UNITS, BATTLE_ROYALE,
     BATTLE_ROYALE_TOURNAMENT, MAPBOX, MAPS_TRAINING, RTS, RTS_1x1, RTS_BOOTCAMP, FUN_RANDOM, COMP7,
     VERSUS_AI)
    REMOVED = (
     COMPANIES,)
    BASE_ON_DEQUEUE = (
     RANDOMS, EVENT_BATTLES, UNITS, EPIC, BATTLE_ROYALE, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI, RANKED)


QUEUE_TYPE_NAMES = {v: k for k, v in QUEUE_TYPE.__dict__.iteritems() if isinstance(v, int)}
QUEUE_TYPE_IDS = {v.lower(): k for k, v in QUEUE_TYPE_NAMES.iteritems()}
USER_ACTIVE_CHANNELS_LIMIT = 100

class INVOICE_EMITTER:
    PAYMENT_SYSTEM = 1
    BACKYARD = 2
    COMMUNITY = 3
    PORTAL = 4
    DEVELOPMENT = 5
    CN_GIFT = 6
    CN_BUY = 7
    ACTION_APPLIER = 9
    DEPRECATED_PLATFORM_EMITTER = 10
    GLOBAL_MAP = 11
    PSS = 12
    MTRP = 13
    MTRP_CASHBACK = 14
    NEGATIVE = (
     BACKYARD, COMMUNITY, PORTAL, DEVELOPMENT, CN_GIFT, CN_BUY, GLOBAL_MAP, PSS, MTRP)
    RANGE = (
     PAYMENT_SYSTEM, BACKYARD, COMMUNITY, PORTAL, DEVELOPMENT,
     CN_GIFT, CN_BUY, ACTION_APPLIER, DEPRECATED_PLATFORM_EMITTER, GLOBAL_MAP, PSS, MTRP, MTRP_CASHBACK)


class INVOICE_ASSET:
    GOLD = 1
    CREDITS = 2
    PREMIUM = 3
    DATA = 4
    FREE_XP = 5
    FORT_RESOURCE = 6
    CRYSTAL = 7
    EVENT_COIN = 8
    BPCOIN = 9
    PURCHASE = 10
    EQUIP_COIN = 11


class INVOICE_LIMITS:
    GOLD_MAX = 1000000
    CRYSTAL_MAX = 1000000
    CREDITS_MAX = 100000000
    FORT_RESOURCE_MAX = 100000000
    FREEXP_MAX = 100000000
    EVENT_COIN_MAX = 1000000
    BPCOIN_MAX = 1000000
    SLOTS_MAX = 1000
    BERTHS_MAX = 1000
    TOKENS_MAX = 10000
    GOODIES_MAX = 1000
    PERMANENT_CUST_MAX = 100
    NON_PERMANENT_CUST_MAX = 365
    TMAN_FREEXP_MAX = 100000000
    TMAN_SKILLS_MAX = 5
    CREW_SKINS = 100
    BLUEPRINTS_MAX = 1000
    PREMIUM_DAYS_MAX = 1830
    BATTLE_PASS_POINTS = 100000
    ENTITLEMENTS_MAX = 10000
    RANKED_DAILY_BATTLES_MAX = 1000
    RANKED_BONUS_BATTLES_MAX = 1000
    EQUIP_COIN_MAX = 1000000


class RentType(object):
    NO_RENT = 0
    TIME_RENT = 1
    BATTLES_RENT = 2
    WINS_RENT = 3
    SEASON_RENT = 4
    SEASON_CYCLE_RENT = 5
    WOTPLUS_RENT = 6
    TELECOM_RENT = 7


class GameSeasonType(object):
    NONE = 0
    RANKED = 1
    EPIC = 2
    BATTLE_ROYALE = 3
    MAPBOX = 4
    EVENT_BATTLES = 5
    FUN_RANDOM = 6
    COMP7 = 7


SEASON_TYPE_BY_NAME = {b'ranked': (GameSeasonType.RANKED), 
   b'epic': (GameSeasonType.EPIC), 
   b'battle_royale': (GameSeasonType.BATTLE_ROYALE), 
   b'mapbox': (GameSeasonType.MAPBOX), 
   b'event_battles': (GameSeasonType.EVENT_BATTLES), 
   b'comp7': (GameSeasonType.COMP7)}
SEASON_NAME_BY_TYPE = {val: key for key, val in SEASON_TYPE_BY_NAME.iteritems()}
CHANNEL_SEARCH_RESULTS_LIMIT = 50
USER_SEARCH_RESULTS_LIMIT = 50

class USER_SEARCH_MODE:
    ALL = 0
    ONLINE = 1
    OFFLINE = 2


class AOGAS_TIME:
    REDUCED_GAIN = 10200
    NO_GAIN = 17400
    RESET = 18000


USE_SERVER_BAD_WORDS_FILTER = IS_CHINA

class SERVER_BAD_WORDS_FILTER_MODE:
    ACCOUNT = 1
    CHANNEL = 2


CURRENT_SERVER_BAD_WORDS_FILTER_MODE = SERVER_BAD_WORDS_FILTER_MODE.CHANNEL

class CREDENTIALS_RESTRICTION:
    BASIC = 0
    CHINESE = 1
    KOREA = 3
    SANDBOX = 4
    CT = 5


if IS_CHINA:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.CHINESE
elif IS_KOREA:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.KOREA
elif IS_SANDBOX:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.SANDBOX
elif IS_CT:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.CT
else:
    CREDENTIALS_RESTRICTION_SET = CREDENTIALS_RESTRICTION.BASIC

class AUTO_MAINTENANCE_TYPE:
    REPAIR = 1
    LOAD_AMMO = 2
    EQUIP = 3
    EQUIP_BOOSTER = 4
    CUSTOMIZATION = 5


class AUTO_MAINTENANCE_RESULT:
    OK = 0
    NOT_ENOUGH_ASSETS = 1
    NOT_PERFORMED = 2
    DISABLED_OPTION = 3
    NO_WALLET_SESSION = 4
    RENT_IS_OVER = 5
    RENT_IS_ALMOST_OVER = 6
    BUY_NOT_AUTO_EQUIP = 7
    NOT_ENOUGH_BOOSTER = 8


class REQUEST_COOLDOWN:
    PLAYER_DOSSIER = 1.0
    PLAYER_CLAN_INFO = 1.0
    PLAYER_GLOBAL_RATING = 1.0
    PLAYERS_GLOBAL_RATING = 1.0
    PREBATTLE_CREATION = 4.0
    PREBATTLE_NOT_READY = 2.0
    PREBATTLE_TEAM_NOT_READY = 1.0
    PREBATTLE_JOIN = 1.0
    PREBATTLE_INVITES = 8.0
    REQUEST_CHAT_TOKEN = 10.0
    REQUEST_WEB_TOKEN = 4.0
    REQUEST_TOKEN = 10.0
    UNIT_CHANGE_FLAGS = 4.0
    UNIT_SET_READY = 2.0
    UNIT_BROWSER_REFRESH = 4.0
    CLIENT_LOG_UX_DATA_COOLDOWN = 2.0
    CLIENT_LOG_XMPP_DATA_COOLDOWN = 10.0
    CALL_GM_METHOD = 0.5
    GM_KEEP_ALIVE = 60.0
    SEND_INVITATION_COOLDOWN = 1.0
    RUN_QUEST = 1.0
    PAWN_FREE_AWARD_LIST = 1.0
    LOOTBOX = 1.0
    BADGES = 2.0
    CREW_SKINS = 0.3
    BPF_COMMAND = 1.0
    BPF_SEEN = 0.2
    FL_REWARD = 5.0
    NATION_CHANGE = 5.0
    MAKE_DENUNCIATION = 1.0
    PREFERRED_MAPS = 1.0
    APPLY_ADDITIONAL_XP = 2.0
    SINGLE_TOKEN = 5.0
    CMD_BUY_VEHICLE = 5.0
    LOG_CLIENT_SESSION_STATS = 5.0
    LOG_CLIENT_SYSTEM = 5.0
    LOG_MEM_CRIT_EVENTS = 5.0
    LOG_CLIENT_PB_20_UX_STATS = 5.0
    ANONYMIZER = 1.0
    UPDATE_IN_BATTLE_PLAYER_RELATIONS = 1.0
    FLUSH_RELATIONS = 1.0
    EQUIP_ENHANCEMENT = 1.0
    DISMOUNT_ENHANCEMENT = 1.0
    BUY_BATTLE_PASS = 1.0
    BUY_BATTLE_PASS_LEVELS = 1.0
    ABILITIES = 1.0
    CREW_BOOKS = 0.5
    CUSTOMIZATION_NOVELTY = 0.5
    REPAIR_VEHICLE = 0.5
    RECEIVE_OFFER_GIFT = 1.0
    RECEIVE_OFFER_GIFT_MULTIPLE = 1.0
    SET_OFFER_BANNER_SEEN = 0.3
    EQUIP_OPTDEV = 1.0
    CHANGE_EVENT_ENQUEUE_DATA = 1.0
    CMD_EQUIP_OPT_DEVS_SEQUENCE = 1.0
    MAPS_TRAINING_INITIAL_CONFIGURATION = 2.5
    BLUEPRINTS_CONVERT_SALE = 1.0
    TANKMAN_RESPECIALIZE = 1.0
    POST_PROGRESSION_BASE = 1.0
    POST_PROGRESSION_CELL = 0.5
    SYNC_GIFTS = 0.5
    WATCH_REPLAY = 5.0
    RESOURCE_WELL_PUT = 1.0
    VEHICLE_IN_BATTLE_SWITCH = 2.0
    SET_VIVOX_PRESENCE = 0.5
    UNIT_UPDATE_EXTRAS = 2.0
    SURVEY_RESULT = 1.0
    ARMORY_YARD_COLLECT_REWARDS = 1.0
    ARMORY_YARD_BUY_STEPS = 1.0
    ARMORY_YARD_CLAIM_FINAL_REWARDS = 1.0
    ARMORY_YARD_BUY_SHOP_PRODUCT = 2.0
    DEV_ARMORY_YARD_ADD_TOKEN_S = 1.0
    SET_ACHIEVEMENTS20_LAYOUT = 1.0
    COMPLEX_OPERATION = 10.0
    CMD_EQUIP_TMAN = 0.5
    CMD_TMAN_DISMISS = 1.0
    CMD_TMAN_RESTORE = 1.0
    CMD_TMANS_RESTORE = 1.0
    COLLECT_RP_PGB_POINTS = 1.0
    RP_INCREMENT_RECRUIT_DELTA = 1.0
    RP_RESET_RECRUIT_DELTA = 1.0
    CMD_BUY_BERTHS = 1.0
    CMD_SELL_ITEM = 1.0
    EARLY_ACCESS_BUY_TOKENS = 1.0
    PARAGONS_RESET_BRANCH = 2.0
    PARAGONS_SELECT_CHAPTER = 1.0
    PARAGONS_UNLOCK_ITEM = 1.0
    PARAGONS_MARK_SELECTED_REWARDS = 1.0
    REROLL_DAILY_QUESTS = 1.0
    GET_PLAYERS_FROM_BATTLES = 2.0
    TANKMAN_PASSPORT = 1.0
    EQUIP_TANKMAN_SKIN = 1.0
    UNEQUIP_TANKMAN_SKIN = 1.0
    GET_VEHICLE_DAMAGE_DISTRIBUTION = 0.5
    GET_STATISTIC_LOOTBOX = 5.0
    GET_VEHICLE_XP_DISTRIBUTION = 0.5
    ARMORY_YARD_REROLL_ARMORY_QUEST = 1.0
    ARMORY_YARD_ACCEPT_REROLL_ARMORY_QUEST = 1.0
    CMD_SELL_VEHICLE = 1.0
    MARK_CUSTOMIZATION_ITEM = 0.5
    SET_INITIAL_PLAYER_EXP_LVL = 1.0
    CMD_EQUIP_COMP7_SKILL = 1.0
    CMD_EQUIP_COMP7_SKILL_CELL = 0.5
    CMD_OPTDEV_RESTORE = 1.0
    PURCHASE_STALL_PRODUCT = 1.0


IS_SHOW_INGAME_HELP_FIRST_TIME = False

class DENUNCIATION:
    NOT_FAIR_PLAY = 1
    FORBIDDEN_NICK = 2
    BOT = 3
    INCORRECT_BEHAVIOR = 7
    RANGE = (
     NOT_FAIR_PLAY, FORBIDDEN_NICK, BOT, INCORRECT_BEHAVIOR)


BATTLE_DENUNCIATIONS_PER_DAY = 10
HANGAR_DENUNCIATIONS_PER_DAY = 10

class VIOLATOR_KIND:
    UNKNOWN = 0
    ENEMY = 1
    ALLY = 2
    HANGAR_CHAT_MEMBER = 3
    RANGE = (
     UNKNOWN, ENEMY, ALLY, HANGAR_CHAT_MEMBER)


GROUND_TYPE_BY_NAME = {b'none': 0, 
   b'firm': 1, 
   b'medium': 2, 
   b'soft': 3, 
   b'slope': 4, 
   b'death_zone': 5}
GROUND_TYPE_NAME_BY_INDEX = dict((v, k) for k, v in GROUND_TYPE_BY_NAME.iteritems())

class DROWN_WARNING_LEVEL:
    SAFE = 0
    CAUTION = 1
    DANGER = 2

    @classmethod
    def isDrowning(cls, warningLevel):
        return warningLevel == cls.DANGER


class OVERTURN_WARNING_LEVEL:
    SAFE = 0
    CAUTION = 1
    DANGER = 2
    BLOCKED = 3

    @classmethod
    def isOverturned(cls, warningLevel):
        return warningLevel in (cls.CAUTION, cls.DANGER, cls.BLOCKED)


class OVERTURN_CONDITION:
    IGNOR_DELAY = 0.1
    WARNING_COSINE = cos(radians(70))
    ONBOARD_COSINE = cos(radians(80))
    OVERTURN_COSINE = cos(radians(120))
    HULL_PRESSURE = 0.2


class ARTILLERY_STRIKE_ZONE_STATUS:
    OUTSIDE_ZONE = 0
    INSIDE_ZONE = 1


TREE_TAG = b'tree'
CUSTOM_DESTRUCTIBLE_TAGS = (b'monument',)
DESTR_CODES_BY_TAGS = dict((tag, code) for code, tag in enumerate(CUSTOM_DESTRUCTIBLE_TAGS))
DESTR_CODES_BY_TAGS[TREE_TAG] = len(CUSTOM_DESTRUCTIBLE_TAGS)
DESTR_TAGS_BY_CODES = dict((code, tag) for tag, code in DESTR_CODES_BY_TAGS.iteritems())

class SYS_MESSAGE_CLAN_EVENT:
    LEFT_CLAN = 1


SYS_MESSAGE_CLAN_EVENT_NAMES = dict([(v, k) for k, v in SYS_MESSAGE_CLAN_EVENT.__dict__.iteritems() if not k.startswith(b'_')])

class SYS_MESSAGE_FORT_EVENT:
    FORT_READY = 1
    RESERVE_ACTIVATED = 2
    RESERVE_EXPIRED = 3
    RESERVE_PRODUCED = 4
    STORAGE_OVERFLOW = 5
    ORDER_CANCELED = 6
    REATTACHED_TO_BASE = 7
    DEF_HOUR_ACTIVATED = 8
    OFF_DAY_ACTIVATED = 9
    VACATION_STARTED = 10
    VACATION_FINISHED = 11
    DEF_HOUR_SHUTDOWN = 12
    DEF_HOUR_CHANGED = 13
    PERIPHERY_CHANGED = 14
    BUILDING_DAMAGED = 15
    BASE_DESTROYED = 16
    SPECIAL_ORDER_EXPIRED = 17
    ORDER_COMPENSATED = 18
    ATTACK_PLANNED = 19
    DEFENCE_PLANNED = 20
    BATTLE_DELETED = 21
    RESOURCE_SET = 22
    RESERVE_SET = 23
    FORT_GOT_8_LEVEL = 24
    BATTLE_DELETED_LEVEL = 25


SYS_MESSAGE_FORT_EVENT_NAMES = dict([(v, k) for k, v in SYS_MESSAGE_FORT_EVENT.__dict__.iteritems() if not k.startswith(b'_')])

class FORT_BUILDING_TYPE:
    MILITARY_BASE = 1
    FINANCIAL_DEPT = 2
    TANKODROME = 3
    TRAINING_DEPT = 4
    MILITARY_ACADEMY = 5
    TRANSPORT_DEPT = 6
    INTENDANT_SERVICE = 7
    TROPHY_BRIGADE = 8
    OFFICE = 9
    MILITARY_SHOP = 10
    ARTILLERY_SHOP = 11
    BOMBER_SHOP = 12
    _ALL = (
     MILITARY_BASE, FINANCIAL_DEPT, TANKODROME, TRAINING_DEPT,
     MILITARY_ACADEMY, TRANSPORT_DEPT, INTENDANT_SERVICE,
     TROPHY_BRIGADE, OFFICE, MILITARY_SHOP, ARTILLERY_SHOP, BOMBER_SHOP)


FORT_BUILDING_TYPE_NAMES = dict([(v, k) for k, v in FORT_BUILDING_TYPE.__dict__.iteritems() if not k.startswith(b'_')])

class FORT_ORDER_TYPE:
    COMBAT_PAYMENTS = 1
    TACTICAL_TRAINING = 2
    ADDITIONAL_BRIEFING = 3
    MILITARY_EXERCISES = 4
    HEAVY_TRANSPORT = 5
    EVACUATION = 6
    REQUISITION = 7
    SPECIAL_MISSION = 8
    EVACUATION_EXPIRE = 9
    REQUISITION_EXPIRE = 10
    ARTILLERY = 11
    BOMBER = 12
    COMBAT_PAYMENTS_2_0 = 13
    MILITARY_EXERCISES_2_0 = 14
    TACTICAL_TRAINING_2_0 = 15
    ADDITIONAL_BRIEFING_2_0 = 16
    HEAVY_TRANSPORT_2_0 = 17
    REQUISITION_2_0 = 18
    ALL = (
     COMBAT_PAYMENTS, TACTICAL_TRAINING, ADDITIONAL_BRIEFING, MILITARY_EXERCISES,
     HEAVY_TRANSPORT, EVACUATION, REQUISITION, SPECIAL_MISSION,
     EVACUATION_EXPIRE, REQUISITION_EXPIRE, ARTILLERY, BOMBER,
     COMBAT_PAYMENTS_2_0, MILITARY_EXERCISES_2_0, TACTICAL_TRAINING_2_0,
     ADDITIONAL_BRIEFING_2_0, HEAVY_TRANSPORT_2_0, REQUISITION_2_0)
    ACTIVATED = (
     COMBAT_PAYMENTS, TACTICAL_TRAINING, ADDITIONAL_BRIEFING, MILITARY_EXERCISES,
     HEAVY_TRANSPORT, EVACUATION, REQUISITION, SPECIAL_MISSION,
     COMBAT_PAYMENTS_2_0, MILITARY_EXERCISES_2_0, TACTICAL_TRAINING_2_0,
     ADDITIONAL_BRIEFING_2_0, HEAVY_TRANSPORT_2_0, REQUISITION_2_0)
    CONSUMABLES = (
     BOMBER, ARTILLERY)
    _EXPIRATION_TO_SOURCE = {EVACUATION_EXPIRE: EVACUATION, 
       REQUISITION_EXPIRE: REQUISITION}
    COMPATIBLES = (
     EVACUATION, REQUISITION, SPECIAL_MISSION)

    @staticmethod
    def isOrderPermanent(orderID):
        return orderID in (FORT_ORDER_TYPE.EVACUATION, FORT_ORDER_TYPE.REQUISITION)

    @staticmethod
    def isOrderCompatible(orderID):
        return orderID in FORT_ORDER_TYPE.COMPATIBLES


FORT_ORDER_TYPE_NAMES = dict([(v, k) for k, v in FORT_ORDER_TYPE.__dict__.iteritems() if v in FORT_ORDER_TYPE.ALL])

class USER_SERVER_SETTINGS:
    VERSION = 0
    HIDE_MARKS_ON_GUN = 500
    GAME_EXTENDED = 59
    GAME_EXTENDED_2 = 102
    EULA_VERSION = 54
    ARCADE_AIM_1 = 43
    ARCADE_AIM_2 = 44
    ARCADE_AIM_3 = 45
    ARCADE_AIM_4 = 63
    SNIPER_AIM_1 = 46
    SNIPER_AIM_2 = 47
    SNIPER_AIM_3 = 48
    SNIPER_AIM_4 = 64
    SPG_AIM = 65
    DOG_TAGS = 68
    BATTLE_COMM = 69
    BATTLE_HUD = 71
    BATTLE_EVENTS = 84
    BATTLE_MATTERS_QUESTS = 89
    QUESTS_PROGRESS = 90
    SESSION_STATS = 96
    NEW_YEAR = 105
    CONTOUR = 106
    UI_STORAGE_2 = 109
    _ALL = (
     HIDE_MARKS_ON_GUN, EULA_VERSION, GAME_EXTENDED, BATTLE_MATTERS_QUESTS, SESSION_STATS, DOG_TAGS,
     GAME_EXTENDED_2, BATTLE_HUD, CONTOUR, UI_STORAGE_2, BATTLE_EVENTS)

    @classmethod
    def isBattleInvitesForbidden(cls, settings):
        if settings and cls.GAME_EXTENDED in settings:
            return not settings[cls.GAME_EXTENDED] >> 2 & 1
        return False

    @classmethod
    def isMapsInDevEnabled(cls, settings):
        if settings and cls.GAME_EXTENDED_2 in settings:
            return bool(settings[cls.GAME_EXTENDED_2] >> 5 & 1)
        return False


INT_USER_SETTINGS_KEYS = {(USER_SERVER_SETTINGS.VERSION): b'Settings version', 
   1: b'Game section settings', 
   2: b'Graphics section settings', 
   3: b'Sound section settings', 
   4: b'Controls section settings', 
   5: b'Keyboard section settings', 
   6: b'Keyboard section settings', 
   7: b'Keyboard section settings', 
   8: b'Keyboard section settings', 
   9: b'Keyboard section settings', 
   10: b'Keyboard section settings', 
   11: b'Keyboard section settings', 
   12: b'Keyboard section settings', 
   13: b'Keyboard section settings', 
   14: b'Keyboard section settings', 
   15: b'Keyboard section settings', 
   16: b'Keyboard section settings', 
   17: b'Keyboard section settings', 
   18: b'Keyboard section settings', 
   19: b'Keyboard section settings', 
   20: b'Keyboard section settings', 
   21: b'Keyboard section settings', 
   22: b'Keyboard section settings', 
   23: b'Keyboard section settings', 
   24: b'Keyboard section settings', 
   25: b'Keyboard section settings', 
   26: b'Keyboard section settings', 
   27: b'Keyboard section settings', 
   28: b'Keyboard section settings', 
   29: b'Keyboard section settings', 
   30: b'Keyboard section settings', 
   31: b'Keyboard section settings', 
   32: b'Keyboard section settings', 
   33: b'Keyboard section settings', 
   34: b'Keyboard section settings', 
   35: b'Keyboard section settings', 
   36: b'Keyboard section settings', 
   37: b'Keyboard section settings', 
   38: b'Keyboard section settings', 
   39: b'Keyboard section settings', 
   40: b'Keyboard section settings', 
   41: b'Keyboard section settings', 
   42: b'Keyboard section settings', 
   (USER_SERVER_SETTINGS.ARCADE_AIM_1): b'Arcade aim setting', 
   (USER_SERVER_SETTINGS.ARCADE_AIM_2): b'Arcade aim setting', 
   (USER_SERVER_SETTINGS.ARCADE_AIM_3): b'Arcade aim setting', 
   (USER_SERVER_SETTINGS.SNIPER_AIM_1): b'Sniper aim setting', 
   (USER_SERVER_SETTINGS.SNIPER_AIM_2): b'Sniper aim setting', 
   (USER_SERVER_SETTINGS.SNIPER_AIM_3): b'Sniper aim setting', 
   49: b'Enemy marker setting', 
   50: b'Dead marker setting', 
   51: b'Ally marker setting', 
   52: b'GuiStartBehavior', 
   53: b'[Free]', 
   (USER_SERVER_SETTINGS.EULA_VERSION): b'EULAVersion', 
   55: b'Gameplay settings', 
   56: b'[Free]', 
   57: b'Users storage revision', 
   58: b'Contacts', 
   (USER_SERVER_SETTINGS.GAME_EXTENDED): b'Game extended section settings', 
   60: b'Fallout', 
   61: b'Limited UI 1', 
   62: b'Limited UI 2', 
   (USER_SERVER_SETTINGS.ARCADE_AIM_4): b'Arcade aim setting', 
   (USER_SERVER_SETTINGS.SNIPER_AIM_4): b'Sniper aim setting', 
   (USER_SERVER_SETTINGS.SPG_AIM): b'SPG aim setting', 
   66: b'[Free]', 
   67: b'[Free]', 
   (USER_SERVER_SETTINGS.DOG_TAGS): b'Dog tags', 
   (USER_SERVER_SETTINGS.BATTLE_COMM): b'Battle communication', 
   70: b'Once only hints', 
   71: b'Keyboard section settings', 
   73: b'Carousel filter', 
   74: b'Carousel filter', 
   75: b'[Free]', 
   76: b'[Free]', 
   77: b'Unit filter', 
   78: b'[Free]', 
   79: b'SixthSense indicator settings', 
   80: b'Ranked carousel filter', 
   81: b'Ranked carousel filter', 
   82: b'feedback damage indicator', 
   83: b'feedback damage log', 
   84: b'feedback battle events', 
   85: b'feedback border map', 
   86: b'ui storage, used for preserving first entry flags etc', 
   87: b'Frontline carousel filter 1', 
   88: b'Frontline carousel filter 2', 
   (USER_SERVER_SETTINGS.HIDE_MARKS_ON_GUN): b'Hide marks on gun', 
   (USER_SERVER_SETTINGS.BATTLE_MATTERS_QUESTS): b'battle matters quests show reward info', 
   (USER_SERVER_SETTINGS.QUESTS_PROGRESS): b'feedback quests progress', 
   91: b'Loot box last viewed count', 
   (USER_SERVER_SETTINGS.SESSION_STATS): b'sessiong statistics settings', 
   97: b'BattlePass carouse filter 1', 
   98: b'Battle Pass Storage', 
   99: b'Once only hints', 
   100: b'Battle Royale carousel filter 1', 
   101: b'Battle Royale carousel filter 2', 
   (USER_SERVER_SETTINGS.GAME_EXTENDED_2): b'Game extended section settings 2', 
   103: b'Mapbox carousel filter 1', 
   104: b'Mapbox carousel filter 2', 
   (USER_SERVER_SETTINGS.NEW_YEAR): b'New Year settings storage', 
   (USER_SERVER_SETTINGS.CONTOUR): b'Contour settings', 
   107: b'Fun Random carousel filter 1', 
   108: b'Fun Random carousel filter 2', 
   (USER_SERVER_SETTINGS.UI_STORAGE_2): b'ui storage 2, used for preserving first entry flags etc', 
   110: b'Competitive7x7 carousel filter 1', 
   111: b'Competitive7x7 carousel filter 2', 
   112: b'Enemy marker setting', 
   113: b'Dead marker setting', 
   114: b'Ally marker setting', 
   115: b'Once only hints', 
   31001: b'Armory Yard progression', 
   31002: b'Versus AI carousel filter 1', 
   31003: b'Versus AI carousel filter 2', 
   31004: b'Battle context hints counters', 
   31005: b'Battle context hints counters, section2', 
   31006: b'Battle context hints counters, section3'}
AUTH_TOKEN_REQUEST_TIMEOUT = 35.0

class TOKEN_TYPE:
    XMPPCS = 1
    WGNI = 2
    WOTG = 3
    WOTB = 4
    WGNI_JWT = 5
    SERVICE_NAMES = {XMPPCS: b'xmppcs', 
       WGNI: b'wgni', 
       WOTG: b'wotg', 
       WOTB: b'wotb', 
       WGNI_JWT: b'wgni'}
    COOLDOWNS = {XMPPCS: b'REQUEST_CHAT_TOKEN', 
       WGNI: b'REQUEST_WEB_TOKEN', 
       WOTG: b'REQUEST_TOKEN', 
       WOTB: b'REQUEST_TOKEN', 
       WGNI_JWT: b'REQUEST_TOKEN'}


class NC_MESSAGE_TYPE:
    INFO = 1
    GOLD = 2
    PREMIUM = 3
    BACKYARD = 4
    POLL = 5
    REFERRAL = 6
    DEFAULT = INFO
    RANGE = (INFO, GOLD, PREMIUM, BACKYARD, POLL, REFERRAL)


class NC_MESSAGE_PRIORITY:
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    DEFAULT = MEDIUM
    ORDER = (LOW, MEDIUM, HIGH)


class NC_CONTEXT_ITEM_TYPE:
    GOLD = 1
    INTEGRAL = 2
    FRACTIONAL = 3
    NICE_NUMBER = 4
    SHORT_TIME = 5
    LONG_TIME = 6
    SHORT_DATE = 7
    LONG_DATE = 8
    DATETIME = 9
    STRING = 10


class WIN_XP_FACTOR_MODE:
    DAILY = 0
    ALWAYS = 1


OBSERVER_VEH_INVENTORY_ID = -5000

class PREBATTLE_INVITE_STATUS:
    OK = 0
    WRONG_CLAN = 1
    LEGIONARIES_NOT_ALLOWED = 2


PREBATTLE_INVITE_STATUS_NAMES = dict([(v, k) for k, v in PREBATTLE_INVITE_STATUS.__dict__.iteritems() if not k.startswith(b'_')])

class FAIRPLAY_VIOLATIONS:
    DESERTER = b'deserter'
    SUICIDE = b'suicide'
    AFK = b'afk'
    EVENT_DESERTER = b'event_deserter'
    EVENT_AFK = b'event_afk'
    EPIC_DESERTER = b'epic_deserter'
    COMP7_DESERTER = b'comp7_deserter'
    BATTLEROYALE_DESERTER = b'battleroyale_deserter'
    BATTLEROYALE_AFK = b'battleroyale_afk'


FAIRPLAY_VIOLATIONS_NAMES = (
 FAIRPLAY_VIOLATIONS.DESERTER, FAIRPLAY_VIOLATIONS.SUICIDE, FAIRPLAY_VIOLATIONS.AFK,
 FAIRPLAY_VIOLATIONS.EVENT_DESERTER, FAIRPLAY_VIOLATIONS.EVENT_AFK,
 FAIRPLAY_VIOLATIONS.EPIC_DESERTER, FAIRPLAY_VIOLATIONS.COMP7_DESERTER,
 FAIRPLAY_VIOLATIONS.BATTLEROYALE_DESERTER, FAIRPLAY_VIOLATIONS.BATTLEROYALE_AFK)
FAIRPLAY_VIOLATIONS_MASKS = {name: 1 << index for index, name in enumerate(FAIRPLAY_VIOLATIONS_NAMES)}

class INVALID_CLIENT_STATS:
    OK = 0
    CLIENT_DEATH = 1
    CLIENT_FOCUS_LOST = 2
    CLIENT_STRAIGHT_INTO_BATTLE = 4
    CLIENT_GS_MAJOR_CHANGED = 8
    CLIENT_GS_MINOR_CHANGED = 16
    CLIENT_RESOLUTION_CHANGED = 32
    CLIENT_WM_CHANGED = 64
    CLIENT_DRR_SCALE_CHANGED = 128


class EQUIP_TMAN_CODE:
    OK = 0
    NO_VEHICLE = 1
    VEHICLE_LOCKED = 2
    NO_FREE_SLOT = 3


class CustomizationInvData(object):
    ITEMS = 1
    OUTFITS = 2
    NOVELTY_DATA = 3
    DRESSED = 4
    PROGRESSION = 5
    OUTFITS_POOL = 6
    SERIAL_NUMBERS = 7
    ORDERING = 8
    TAG_MASK = 9


class SkinInvData(object):
    ITEMS = 1
    OUTFITS = 2


class EVENT_CLIENT_DATA:
    ACTION = 1
    ACTION_REV = 2
    QUEST = 3
    QUEST_REV = 4
    INGAME_EVENTS = 7
    INGAME_EVENTS_REV = 8
    NOTIFICATIONS = 9
    NOTIFICATIONS_REV = 10
    PERSONAL_QUEST = 11
    PERSONAL_QUEST_REV = 12
    FALLOUT = 15
    FALLOUT_REV = 16
    SQUAD_BONUSES = 17
    SQUAD_BONUSES_REV = 18
    FEATURES_SWITCH = 19
    FEATURES_SWITCH_REV = 20
    ACTION_ENTITIES = 21
    ACTION_ENTITIES_REV = 22
    ANNOUNCED_ACTION_DATA = 23
    ANNOUNCED_ACTION_DATA_REV = 24
    DAILY_QUESTS = 25
    DAILY_QUESTS_REV = 26
    OFFER = 27
    OFFER_REV = 28
    NUMBER_OF_ANNOUNCED_ACTIONS_STEPS = 1

    @staticmethod
    def REVISION(id):
        return id + 1


class FLAG_TYPES:
    BIG = 0
    MEDIUM = 1
    SMALL = 2
    RANGE = (
     BIG, MEDIUM, SMALL)


class FLAG_SPAWN_COOLDOWN:
    ABSORB = 10.0
    SOLO_ABSORB = 10.0
    DROP = 15.0


class FLAG_STATE:
    UNKNOWN = 0
    ON_SPAWN = 1
    ON_GROUND = 2
    ON_VEHICLE = 3
    ABSORBED = 4
    WAITING_FIRST_SPAWN = 5


class FLAG_ACTION:
    PICKED_UP_FROM_BASE = 0
    PICKED_UP_FROM_GROUND = 1
    CAPTURED = 2
    LOST = 3
    RANGE = (
     PICKED_UP_FROM_BASE, PICKED_UP_FROM_GROUND, CAPTURED, LOST)


FLAG_VOLUME_RADIUS = 10.0

class INVITATION_STATUS:
    ERROR = -1
    PENDING = 0
    ACCEPTED = 1
    DECLINED = 2
    REVOKED = 3
    CANCELED = 4
    POSTPONED = 5


class INVITATION_TYPE:
    SQUAD = PREBATTLE_TYPE.SQUAD
    EPIC = PREBATTLE_TYPE.EPIC
    EVENT = PREBATTLE_TYPE.EVENT
    BATTLE_ROYALE = PREBATTLE_TYPE.BATTLE_ROYALE
    MAPBOX = PREBATTLE_TYPE.MAPBOX
    FUN_RANDOM = PREBATTLE_TYPE.FUN_RANDOM
    COMP7 = PREBATTLE_TYPE.COMP7
    VERSUS_AI = PREBATTLE_TYPE.VERSUS_AI
    RANKED = PREBATTLE_TYPE.RANKED
    RANGE = (
     SQUAD, EVENT, EPIC, BATTLE_ROYALE, MAPBOX, FUN_RANDOM, COMP7, VERSUS_AI, RANKED)
    TYPES_WITH_EXTRA_DATA = (FUN_RANDOM,)
    INVITATION_TYPE_FROM_ARENA_BONUS_TYPE_MAPPING = {(ARENA_BONUS_TYPE.REGULAR): SQUAD, 
       (ARENA_BONUS_TYPE.EPIC_RANDOM): SQUAD, 
       (ARENA_BONUS_TYPE.EPIC_BATTLE): EPIC, 
       (ARENA_BONUS_TYPE.EVENT_BATTLES): EVENT, 
       (ARENA_BONUS_TYPE.MAPBOX): MAPBOX}

    @staticmethod
    def invitationTypeFromArenaBonusType(arenaBonusType):
        return INVITATION_TYPE.INVITATION_TYPE_FROM_ARENA_BONUS_TYPE_MAPPING.get(arenaBonusType)


class REPAIR_FLAGS:
    STOP_FIRE = 1
    HEAL_VEHICLE = 2
    HEAL_CREW = 4
    HEAL_DEVICES = 8
    REPLENISH_AMMO = 16
    REPLENISH_EQUIP = 32
    RELOAD_GUN = 64
    ALL = STOP_FIRE | HEAL_VEHICLE | HEAL_CREW | HEAL_DEVICES | REPLENISH_AMMO | REPLENISH_EQUIP | RELOAD_GUN


class REPAIR_POINT_STATE:
    READY = 0
    REPAIRING = 1
    COOLDOWN_VEH_INSIDE = 2
    COOLDOWN_VEH_OUTSIDE = 3
    DISABLED = 4
    FULL = 5


class REPAIR_POINT_ACTION:
    START_REPAIR = 0
    RESTART_REPAIR = 1
    CANCEL_REPAIR = 2
    COMPLETE_REPAIR = 3
    ENTER_WHILE_CD = 4
    LEAVE_WHILE_CD = 5
    BECOME_READY = 6
    BECOME_DISABLED = 7
    REPAIR_STEP = 8
    ENTER_WHILE_FULL = 9
    COOLDOWN = 10
    COOLDOWN_AFTER_COMPLETE = 11


class GLOBAL_MAP_DIVISION(object):
    MIDDLE = 0
    CHAMPION = 1
    ABSOLUTE = 2
    _ORDER = (
     MIDDLE, CHAMPION, ABSOLUTE)


GLOBAL_MAP_DIVISION_NAMES = dict([(v, k) for k, v in GLOBAL_MAP_DIVISION.__dict__.iteritems() if not k.startswith(b'_')])

class RESOURCE_POINT_STATE:
    UNKNOWN = 0
    FREE = 1
    COOLDOWN = 2
    CAPTURED = 3
    CAPTURED_LOCKED = 4
    BLOCKED = 5


DEFAULT_EXTERNAL_UNIT_DIVISION = 10

class VEHICLE_PHYSICS_MODE:
    STANDARD = 0
    DETAILED = 1


class VEHICLE_MODE:
    DEFAULT = 0
    SIEGE = 1


VEHICLE_MODES = (
 VEHICLE_MODE.DEFAULT,
 VEHICLE_MODE.SIEGE)
VEHICLE_MODE_INDICES = dict((value, index) for index, value in enumerate(VEHICLE_MODES))

class VEHICLE_SIEGE_STATE:
    DISABLED = 0
    SWITCHING_ON = 1
    ENABLED = 2
    SWITCHING_OFF = 3
    SWITCHING = {
     SWITCHING_ON, SWITCHING_OFF}
    DEFAULT_MODE = {DISABLED, SWITCHING_ON}
    SIEGE_MODE = {ENABLED, SWITCHING_OFF}

    @classmethod
    def getMode(cls, siegeState):
        if siegeState in cls.DEFAULT_MODE:
            return VEHICLE_MODE.DEFAULT
        else:
            if siegeState in cls.SIEGE_MODE:
                return VEHICLE_MODE.SIEGE
            return VEHICLE_MODE.DEFAULT

        return


class ROCKET_ACCELERATION_STATE:
    NOT_RUNNING = 0
    DEPLOYING = 1
    PREPARING = 2
    READY = 3
    ACTIVE = 4
    DISABLED = 5
    EMPTY = 6

    @classmethod
    def toString(cls, value):
        return {(cls.NOT_RUNNING): b'not running', 
           (cls.DEPLOYING): b'deploying', 
           (cls.PREPARING): b'preparing', 
           (cls.READY): b'ready', 
           (cls.ACTIVE): b'active', 
           (cls.DISABLED): b'disabled', 
           (cls.EMPTY): b'empty'}.get(value)


class THERMAL_VISION_STATE:
    IDLE = 0
    ACTIVE = 1
    RELOADING = 2
    DISABLED = 3


class DUAL_ACCURACY_STATE:
    NONE = 0
    ACTIVE = 1
    NOT_ACTIVE = 2

    @classmethod
    def toString(cls, value):
        return {(cls.ACTIVE): b'active', 
           (cls.NOT_ACTIVE): b'not active', 
           (cls.NONE): b'none'}.get(value)


class CONTENT_TYPE:
    DEFAULT = 0
    SD_TEXTURES = 1
    HD_TEXTURES = 2
    INCOMPLETE = 3
    TUTORIAL = 4
    SANDBOX = 5
    CEF = 6


class DEATH_ZONES:
    STATIC = 0
    SECTOR_BOMBING = 1
    SECTOR_AIRSTRIKE = 2
    SECTOR_AIRSUPPORT = 3


class FALLOUT_ARENA_TYPE:
    GAMEPLAY_NAMES = {b'multiteam': (b'fallout', b'fallout2', b'fallout3'), 
       b'classic': (b'fallout4', b'fallout5', b'fallout6')}

    @staticmethod
    def fromGameplayName(gameplayName):
        for type, names in FALLOUT_ARENA_TYPE.GAMEPLAY_NAMES.iteritems():
            if gameplayName in names:
                return type

        return


class RESPAWN_TYPES:
    NONE = 0
    INFINITE = 1
    SHARED = 2
    LIMITED = 3
    EPIC = 4
    SAFE = 5


class VISIBILITY:
    MAX_RADIUS = 445.0
    MIN_RADIUS = 50.0


VEHICLE_ATTRS_TO_SYNC = frozenset([b'circularVisionRadius', b'gun/piercing'])
VEHICLE_ATTRS_TO_SYNC_ALIASES = {b'gun/piercing': b'gunPiercing'}

class OBSTACLE_KIND:
    CHUNK_DESTRUCTIBLE = 1
    ENTITY_DESTRUCTIBLE = 2
    SMOKE = 3
    STATIC_GAME_OBJECT = 4


class SHELL_TYPES(object):
    HOLLOW_CHARGE = b'HOLLOW_CHARGE'
    HIGH_EXPLOSIVE = b'HIGH_EXPLOSIVE'
    ARMOR_PIERCING = b'ARMOR_PIERCING'
    ARMOR_PIERCING_HE = b'ARMOR_PIERCING_HE'
    ARMOR_PIERCING_CR = b'ARMOR_PIERCING_CR'
    ARMOR_PIERCING_FSDS = b'ARMOR_PIERCING_FSDS'
    SMOKE = b'SMOKE'
    FLAME = b'FLAME'


HAS_EXPLOSION_EFFECT = (
 SHELL_TYPES.HIGH_EXPLOSIVE, SHELL_TYPES.FLAME)
HAS_EXPLOSION = (SHELL_TYPES.HIGH_EXPLOSIVE,)
SHELL_TYPES_LIST = (
 SHELL_TYPES.HOLLOW_CHARGE, SHELL_TYPES.HIGH_EXPLOSIVE,
 SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_HE,
 SHELL_TYPES.ARMOR_PIERCING_CR, SHELL_TYPES.SMOKE,
 SHELL_TYPES.ARMOR_PIERCING_FSDS,
 SHELL_TYPES.FLAME)
BATTLE_RESULT_WAITING_TIMEOUT = 0.1
BATTLE_RESULTS_MAXIMUM_CACHE_SIZE = 3
SHELL_TYPES_INDICES = dict((value, index) for index, value in enumerate(SHELL_TYPES_LIST))

@enum.unique
class StunTypes(enum.IntEnum):
    NONE = 0
    DEFAULT = 1
    FLAME = 2
    BULLET = 3


AVAILABLE_STUN_TYPES_NAMES = [key for key, value in StunTypes.__members__.iteritems() if value > 0]

class SHELL_MECHANICS_TYPE:
    LEGACY = b'LEGACY'
    MODERN = b'MODERN'
    GUARANTEED_DAMAGE = b'GUARANTEED_DAMAGE'


class BATTLE_LOG_SHELL_TYPES(enum.IntEnum):
    HOLLOW_CHARGE = 0
    ARMOR_PIERCING = 1
    ARMOR_PIERCING_HE = 2
    ARMOR_PIERCING_CR = 3
    SMOKE = 4
    HE_MODERN = 5
    HE_LEGACY_STUN = 6
    HE_LEGACY_NO_STUN = 7
    FLAME = 8
    ARMOR_PIERCING_FSDS = 9
    HOLLOW_CHARGE_DF = 10
    ARMOR_PIERCING_DF = 11
    ARMOR_PIERCING_HE_DF = 12
    ARMOR_PIERCING_CR_DF = 13
    HE_MODERN_DF = 14

    @classmethod
    def getType(cls, shellDescr):
        shellKind = shellDescr.kind
        hasDistanceFactor = shellDescr.distanceFactor
        if shellKind not in HAS_EXPLOSION_EFFECT:
            if hasDistanceFactor is not None:
                shellKind += b'_DF'
            return cls[shellKind]
        else:
            if shellDescr.type.mechanics == SHELL_MECHANICS_TYPE.MODERN and shellKind == SHELL_TYPES.HIGH_EXPLOSIVE:
                if hasDistanceFactor is not None:
                    return cls.HE_MODERN_DF
                return cls.HE_MODERN
            else:
                if shellDescr.type.mechanics == SHELL_MECHANICS_TYPE.MODERN and shellKind == SHELL_TYPES.FLAME:
                    return cls.FLAME
                if shellDescr.hasStun:
                    return cls.HE_LEGACY_STUN
                return cls.HE_LEGACY_NO_STUN

            return

    @classmethod
    def getIndex(cls, shellDescr):
        return int(cls.getType(shellDescr))


class HIT_INDIRECTION:
    DIRECT_HIT = 0
    HIT_BY_EXTERNAL_EXPLOSION = 1
    HIT_BY_RICOCHET = 2
    MISS = 3
    CEILING_HIT = 4


class VEHICLE_FRICTION_STATE(object):
    VFS_START = 1
    VFS_UPDATE = 2
    VFS_FINISHED = 3
    _ALL = (VFS_START, VFS_UPDATE, VFS_FINISHED)


def getArenaStartTime(arenaUniqueID):
    return arenaUniqueID & 4294967295L


def getTimeOnArena(arenaUniqueID):
    return int(timestamp() - getArenaStartTime(arenaUniqueID))


class PIERCING_POWER(object):
    PIERCING_POWER_LAW_POINT = 100.0
    PIERCING_POWER_LAW_DIST = 400.0

    @staticmethod
    def computePiercingPowerAtDist(piercingPower, dist, maxDist):
        pFirst, pLast = piercingPower
        if dist <= PIERCING_POWER.PIERCING_POWER_LAW_POINT:
            return pFirst
        if dist < maxDist + 4.0:
            return max(0.0, pFirst + (pLast - pFirst) * (dist - PIERCING_POWER.PIERCING_POWER_LAW_POINT) / PIERCING_POWER.PIERCING_POWER_LAW_DIST)
        return 0.0


EPIC_RANDOM_GROUPS = 3
EPIC_RANDOM_GAMEPLAY_NAMES = (b'ctf30x30', b'domination30x30')
EPIC_RANDOM_GAMEPLAY_IDS = tuple(ARENA_GAMEPLAY_IDS[name] for name in EPIC_RANDOM_GAMEPLAY_NAMES)
EPIC_RANDOM_GAMEPLAY_MASK = reduce((lambda a, b: a | b), map((lambda x: 1 << x), EPIC_RANDOM_GAMEPLAY_IDS))

class LGC_STATE:
    OFF = 0
    READY_TO_LOGIN = 1
    LOGIN_IN_PROGRESS = 2
    WAITING_TOKEN_1 = 3
    DISABLED = 4
    ERROR = 5
    LOGGEDIN = 6


class LGC_PUBLICATION:
    LGC_UNKNOWN = -1
    LGC_BASE = 0
    LGC_CN360 = 1
    LGC_STEAM = 2
    LGC_PC = 3
    NAMES = {LGC_UNKNOWN: b'Unknown', 
       LGC_BASE: b'Base', 
       LGC_CN360: b'360', 
       LGC_STEAM: b'Steam', 
       LGC_PC: b'PC'}


class DISTRIBUTION_PLATFORM(enum.Enum):
    BASE = b'wg_platform'
    CHINA_360 = b'china_360'
    STEAM = b'steam'
    WIN_STORE = b'winstore'
    EPIC = b'epic'


LGC_PUBLICATION_TO_DISTRIBUTION_PLATFORM = {(LGC_PUBLICATION.LGC_UNKNOWN): (DISTRIBUTION_PLATFORM.BASE), 
   (LGC_PUBLICATION.LGC_BASE): (DISTRIBUTION_PLATFORM.BASE), 
   (LGC_PUBLICATION.LGC_CN360): (DISTRIBUTION_PLATFORM.CHINA_360), 
   (LGC_PUBLICATION.LGC_STEAM): (DISTRIBUTION_PLATFORM.STEAM), 
   (LGC_PUBLICATION.LGC_PC): (DISTRIBUTION_PLATFORM.BASE)}

class TARGET_LOST_FLAGS:
    INVALID = 1
    KILLED_BY_ME = 2
    KILLED_BY_OTHERS = 4
    UNREACHABLE = 8


GIFT_TANKMAN_TOKEN_NAME = b'WOTD-95479_gift_tankman'
GAMEPLAY_NAMES_WITH_DISABLED_QUESTS = (b'bootcamp',)

class BASE_TYPE:
    TEAM_BASE = 1
    SECTOR_BASE = 2


class SECTOR_STATE:
    CLOSED = 0
    OPEN = 1
    TRANSITION = 2
    CAPTURED = 3
    BOMBING = 4


class SECTOR_BASE_ACTION:
    ENTER = 0
    ENTER_WHILE_CD = 1
    COOLDOWN = 2
    LEAVE = 3
    LEAVE_WHILE_CD = 4
    RESUME = 5
    CAPTURED = 6


class PLAYER_RANK:
    NO_RANK = 0
    PRIVATE = 1
    SERGEANT = 2
    LIEUTENANT = 3
    CAPTAIN = 4
    MAJOR = 5
    GENERAL = 6
    DEFAULT_RANK = NO_RANK
    MAX_RANK = GENERAL
    NAMES = {NO_RANK: b'norank', 
       PRIVATE: b'private', 
       SERGEANT: b'sergeant', 
       LIEUTENANT: b'lieutenant', 
       CAPTAIN: b'captain', 
       MAJOR: b'major', 
       GENERAL: b'general'}
    RANK_BY_NAME = {d: k for k, d in NAMES.iteritems()}

    @staticmethod
    def getPlayerRankByName(name):
        return PLAYER_RANK.RANK_BY_NAME[name]


class CHAT_COMMAND_FLAGS:
    EPIC_BATTLE_COMMANDS = 1
    NAMES = {EPIC_BATTLE_COMMANDS: b'EPIC_BATTLE_COMMANDS'}
    FLAG_BY_NAME = {d: k for k, d in NAMES.iteritems()}


class RM_STATE:
    NOT_RECOVERING = 0
    RECOVERING = 1
    TEMPORARILY_BLOCKED_FROM_RECOVERING = 2
    PERMANENTLY_BLOCKED_FROM_RECOVERING = 3
    RECOVERING_RESPAWNING = 4
    TEMPORARILY_BLOCKED_RECOVER_TRY = 5
    NAMES = {NOT_RECOVERING: b'NOT_RECOVERING', 
       RECOVERING: b'RECOVERING', 
       TEMPORARILY_BLOCKED_FROM_RECOVERING: b'TEMPORARILY_BLOCKED_FROM_RECOVERING', 
       PERMANENTLY_BLOCKED_FROM_RECOVERING: b'PERMANENTLY_BLOCKED_FROM_RECOVERING', 
       RECOVERING_RESPAWNING: b'RECOVERING_RESPAWNING', 
       TEMPORARILY_BLOCKED_RECOVER_TRY: b'TEMPORARILY_BLOCKED_RECOVER_TRY'}


class RM_TEMPORARY_BLOCKING_REASON:
    HAS_SHOT = 0
    HAS_RECEIVED_DAMAGE = 1
    NAMES = {HAS_SHOT: b'HAS_SHOT', 
       HAS_RECEIVED_DAMAGE: b'HAS_RECEIVED_DAMAGE'}


class QUEST_PROGRESS_STATE:
    NOT_STARTED = 1
    IN_PROGRESS = 2
    FAILED = 3
    PRELIMINARY_FAILED = 4
    COMPLETED = 5
    PRELIMINARY_COMPLETED = 6
    COMPLETED_STATES = (
     COMPLETED, PRELIMINARY_COMPLETED)
    FINISHED_STATES = (FAILED, PRELIMINARY_FAILED, COMPLETED, PRELIMINARY_COMPLETED)


class QUEST_TYPE_OPERATION_FOR_KAFKA:
    START = 1
    STOP = 2
    COMPLETED = 3
    FAILED = 4
    START_PAUSE = 5
    STOP_PAUSE = 6
    RESET = 7
    COMPLETED_AFTER_REBALANCE = 8
    FAILED_AFTER_REBALANCE = 9


class BotNamingType(object):
    CREW_MEMBER = 1
    VEHICLE_MODEL = 2
    CUSTOM = 3
    DEFAULT = CREW_MEMBER
    _parseDict = {b'crew': CREW_MEMBER, 
       b'vehicle': VEHICLE_MODEL, 
       b'custom': CUSTOM, 
       b'default': DEFAULT}

    @classmethod
    def parse(cls, typeString):
        if typeString in cls._parseDict:
            return cls._parseDict[typeString]
        else:
            return


BotNamingConfig = namedtuple(b'BotNamingConfig', (b'prefix', b'argTypes', b'argSeparator'))

class LocalizableBotName(object):
    CONFIGS = {(BotNamingType.CREW_MEMBER): (BotNamingConfig(b'BotCrew_', (int, int, int), b'_')), 
       (BotNamingType.VEHICLE_MODEL): (BotNamingConfig(b'BotVeh_', (int, int, int), b'_')), 
       (BotNamingType.CUSTOM): (BotNamingConfig(b'BotLoc_', (int, str), b' '))}

    @staticmethod
    def create(namingType, *args):
        cfg = LocalizableBotName.CONFIGS[namingType]
        return cfg.prefix + cfg.argSeparator.join(map(str, args))

    @staticmethod
    def parse(name):
        if name:
            for namingType, cfg in LocalizableBotName.CONFIGS.iteritems():
                if name.startswith(cfg.prefix):
                    argsStr = name[len(cfg.prefix):]
                    argTokens = argsStr.split(cfg.argSeparator) if cfg.argSeparator else [argsStr]
                    args = tuple(t(v) for t, v in izip(cfg.argTypes, argTokens))
                    return (
                     namingType, args)

        return (None, None)


class LOOT_TYPE(object):
    NONE = 0
    BASIC = 1
    ADVANCED = 2
    AIRDROP = 3
    CORPSE = 4


class AirdropType(object):
    LOOT = 1
    BOT = 2
    BOT_CLING = 3


class LootAction(object):
    PICKUP_STARTED = 0
    PICKUP_FAILED = 1
    PICKUP_SUCCEEDED = 2


class BattleRoyaleMode(object):
    SOLO = b'solo'
    SQUAD = b'squad'
    ALL = (
     SOLO, SQUAD)


class BattleRoyaleResult(object):
    DISQUALIFIED = -2
    WIN = 1
    LOSE = -1
    DRAW = 0


class CLIENT_COMMAND_SOURCES:
    UNDEFINED = 0
    RENTED_STYLE_RADIAL_MENU = 1
    RANGE = (
     UNDEFINED, RENTED_STYLE_RADIAL_MENU)


EMPTY_GEOMETRY_ID = 0
ROLE_LEVELS = range(6, MAX_VEHICLE_LEVEL + 1)

class ROLE_TYPE:
    NOT_DEFINED = 0
    SPG = 1
    HT_ASSAULT = 2
    HT_BREAK = 3
    HT_UNIVERSAL = 4
    HT_SUPPORT = 5
    MT_ASSAULT = 6
    MT_SUPPORT = 7
    MT_UNIVERSAL = 8
    MT_SNIPER = 9
    ATSPG_ASSAULT = 10
    ATSPG_UNIVERSAL = 11
    ATSPG_SNIPER = 12
    ATSPG_SUPPORT = 13
    LT_UNIVERSAL = 14
    LT_WHEELED = 15
    SPG_FLAME = 16
    SPG_ASSAULT = 17


ROLE_LABEL_TO_TYPE = {b'NotDefined': (ROLE_TYPE.NOT_DEFINED), 
   b'role_SPG': (ROLE_TYPE.SPG), 
   b'role_SPG_flame': (ROLE_TYPE.SPG_FLAME), 
   b'role_SPG_assault': (ROLE_TYPE.SPG_ASSAULT), 
   b'role_HT_assault': (ROLE_TYPE.HT_ASSAULT), 
   b'role_HT_break': (ROLE_TYPE.HT_BREAK), 
   b'role_HT_universal': (ROLE_TYPE.HT_UNIVERSAL), 
   b'role_HT_support': (ROLE_TYPE.HT_SUPPORT), 
   b'role_MT_assault': (ROLE_TYPE.MT_ASSAULT), 
   b'role_MT_universal': (ROLE_TYPE.MT_UNIVERSAL), 
   b'role_MT_sniper': (ROLE_TYPE.MT_SNIPER), 
   b'role_MT_support': (ROLE_TYPE.MT_SUPPORT), 
   b'role_ATSPG_assault': (ROLE_TYPE.ATSPG_ASSAULT), 
   b'role_ATSPG_universal': (ROLE_TYPE.ATSPG_UNIVERSAL), 
   b'role_ATSPG_sniper': (ROLE_TYPE.ATSPG_SNIPER), 
   b'role_ATSPG_support': (ROLE_TYPE.ATSPG_SUPPORT), 
   b'role_LT_universal': (ROLE_TYPE.LT_UNIVERSAL), 
   b'role_LT_wheeled': (ROLE_TYPE.LT_WHEELED)}
ROLE_TYPE_TO_LABEL = dict((index, label) for label, index in ROLE_LABEL_TO_TYPE.items())
ANY_ROLE = b'<any>'
ANY_TYPE = b'<any>'
ANY_SPAWN_POINT = b'<any>'

class ACTION_TYPE:
    BLOCK_AND_TAKE_DAMAGE = 1
    DO_NEAR_DAMAGE = 2
    DO_OWN_DAMAGE = 3
    BLOCK_DAMAGE = 4
    SEARCH_ENEMY = 5
    DO_FAR_DAMAGE = 6
    FRAG_ASSIST = 7
    DO_STUN = 8
    DO_SPG_DAMAGE = 9
    DO_NEAR_DAMAGE_SQ = 10
    DO_GROUP_STUN = 11
    DO_INVIS_ASSIST = 12
    DO_RADIO_ASSIST = 13
    DO_TRACK_ASSIST = 14
    DO_CRIT = 15
    DO_KILL = 16
    BASE_CAPTURE_POINTS = 17
    BASE_CAPTURE_DROPPED = 18
    DO_ARTILLERY_EQ = 19
    DO_HEAL_ALLY = 20
    DO_CAPTURE_ENTITY = 21
    DO_VISIBLE_ALL_ENEMIES = 22
    DO_INSPIRE_ASSIST = 23
    DO_SMOKE_ASSIST = 24
    DO_MINEFIELD_EQ = 25


ACTION_LABEL_TO_TYPE = {b'blockAndTakeDamage': (ACTION_TYPE.BLOCK_AND_TAKE_DAMAGE), 
   b'doNearDamage': (ACTION_TYPE.DO_NEAR_DAMAGE), 
   b'doOwnDamage': (ACTION_TYPE.DO_OWN_DAMAGE), 
   b'blockDamage': (ACTION_TYPE.BLOCK_DAMAGE), 
   b'searchEnemy': (ACTION_TYPE.SEARCH_ENEMY), 
   b'doFarDamage': (ACTION_TYPE.DO_FAR_DAMAGE), 
   b'fragAssist': (ACTION_TYPE.FRAG_ASSIST), 
   b'doStun': (ACTION_TYPE.DO_STUN), 
   b'doSpgDamage': (ACTION_TYPE.DO_SPG_DAMAGE), 
   b'doNearDamageSq': (ACTION_TYPE.DO_NEAR_DAMAGE_SQ), 
   b'doGroupStun': (ACTION_TYPE.DO_GROUP_STUN), 
   b'doInvisAssist': (ACTION_TYPE.DO_INVIS_ASSIST), 
   b'doTrackAssist': (ACTION_TYPE.DO_TRACK_ASSIST), 
   b'doRadioAssist': (ACTION_TYPE.DO_RADIO_ASSIST), 
   b'doCrit': (ACTION_TYPE.DO_CRIT), 
   b'doKill': (ACTION_TYPE.DO_KILL), 
   b'baseCapturePoints': (ACTION_TYPE.BASE_CAPTURE_POINTS), 
   b'baseCaptureDropped': (ACTION_TYPE.BASE_CAPTURE_DROPPED), 
   b'doArtilleryEq': (ACTION_TYPE.DO_ARTILLERY_EQ), 
   b'doHealAlly': (ACTION_TYPE.DO_HEAL_ALLY), 
   b'doCaptureEntity': (ACTION_TYPE.DO_CAPTURE_ENTITY), 
   b'doVisibleAllEnemies': (ACTION_TYPE.DO_VISIBLE_ALL_ENEMIES), 
   b'doInspireAssist': (ACTION_TYPE.DO_INSPIRE_ASSIST), 
   b'doSmokeAssist': (ACTION_TYPE.DO_SMOKE_ASSIST), 
   b'doMineFieldEq': (ACTION_TYPE.DO_MINEFIELD_EQ)}
ACTION_TYPE_TO_LABEL = dict((index, label) for label, index in ACTION_LABEL_TO_TYPE.items())
ROLES_COLLAPSE = b'rolesSectionCollapsed'

class ASSIST_TYPES(object):
    TRACK = 0
    RADIO = 1
    STUN = 2
    SMOKE = 3
    INSPIRE = 4


class DUAL_GUN:

    class ACTIVE_GUN:
        LEFT = 0
        RIGHT = 1

    class GUN_STATE:
        EMPTY = 0
        RELOADING = 1
        READY = 2

    class RELOAD_ORDER:
        FIRST = 0
        SECOND = 1

    class COOLDOWNS:
        LEFT = 0
        RIGHT = 1
        SWITCH = 2
        DEBUFF = 3
        COUNT = 4


class MarathonConfig(object):
    EMPTY_PATH = b''
    URL = b'marathonUrl'
    REWARD_VEHICLE_URL = b'rewardVehicleUrl'
    REWARD_VEHICLE_URL_IGB = b'rewardVehicleUrlIgb'
    REWARD_STYLE_URL_IGB = b'rewardStyleUrlIgb'
    FINISH_SALE_TIME = b'finishSaleTime'


class ClansConfig(object):
    SECTION_NAME = b'clans_config'
    NOTIFICATION_ENABLED = b'isClanNotificationEnabled'
    QUEST_URL = b'clanQuestUrl'
    CRAFT_MACHINE_URL = b'craftMachineUrl'
    STRONGHOLD_EVENT_URL = b'strongholdEventUrl'
    STRONGHOLD_EVENT_PROGRESSION_URL = b'strongholdEventProgressionUrl'
    NOTIFICATION_START_TIME = b'notificationStartTime'
    ON_ENTER_CLAN_BONUS = b'onEnterClanBonus'
    STRONGHOLD_EVENT_ENABLED = b'strongholdEventEnabled'
    STRONGHOLD_EVENT_BATTLE_MODE = b'strongholdEventBattleMode'
    STRONGHOLD_EVENT_FREEZE_JOURNAL_URL = b'strongholdEventFreezeJournalUrl'


class EnhancementsConfig(object):
    SECTION_NAME = b'enhancements_config'
    ENABLED = b'enabled'


SECONDS_IN_DAY = 86400
SECONDS_IN_THIRTY_DAYS = SECONDS_IN_DAY * 30

class BattleUserActions(object):
    ADD_FRIEND = 1
    REMOVE_FRIEND = 2
    ADD_IGNORED = 4
    REMOVE_IGNORED = 8


class PM3_LEVEL(object):
    LEVEL_GROUP1 = b'LevelGroup1'
    LEVEL_GROUP2 = b'LevelGroup2'
    LEVEL_GROUP3 = b'LevelGroup3'


PM3_LEVEL_TAGS = frozenset((PM3_LEVEL.LEVEL_GROUP1, PM3_LEVEL.LEVEL_GROUP2, PM3_LEVEL.LEVEL_GROUP3))

class DailyQuestsDecorations(object):
    WIN = b'win'
    DEAL_DAMAGE = b'hurt_vehicles'
    GET_EXPERIENCE = b'experience'
    DESTROY_TANK = b'kill_vehicles'
    DAMAGE_TANK = b'damage'
    FINISH_TOP1 = b'top1'
    FINISH_TOP3 = b'top3'
    FINISH_TOP5 = b'top5'
    FINISH_TOP7 = b'top7'
    DAMAGE_A_MODULE = b'module_crit'
    SPOT = b'discover'
    ALL = (
     WIN, DEAL_DAMAGE, GET_EXPERIENCE, DESTROY_TANK, DAMAGE_TANK, FINISH_TOP1, FINISH_TOP3, FINISH_TOP5,
     FINISH_TOP7, DAMAGE_A_MODULE, SPOT)


class DailyQuestsLevels(object):
    NONE = b''
    EASY = b'easy'
    MEDIUM = b'medium'
    HARD = b'hard'
    BONUS = b'bonus'
    EPIC = b'epic'
    EASY_SUBS = b'easy_subs'
    MEDIUM_SUBS = b'medium_subs'
    HARD_SUBS = b'hard_subs'
    BONUS_SUBS = b'bonus_subs'
    EASY_PREMIUM = b'easy_premium'
    MEDIUM_PREMIUM = b'medium_premium'
    HARD_PREMIUM = b'hard_premium'
    EPIC_ACCESS = b'epic_access'
    ALL = (
     EASY, EASY_SUBS, EASY_PREMIUM,
     MEDIUM, MEDIUM_SUBS, MEDIUM_PREMIUM,
     HARD, HARD_SUBS, HARD_PREMIUM,
     BONUS, BONUS_SUBS, EPIC)
    DAILY = (
     EASY, MEDIUM, HARD, BONUS)
    DAILY_SIMPLE = (EASY, MEDIUM, HARD)
    SUBS = (EASY_SUBS, MEDIUM_SUBS, HARD_SUBS, BONUS_SUBS)
    DAILY_PREMIUM = (EASY_PREMIUM, MEDIUM_PREMIUM, HARD_PREMIUM)
    DAILY_SIMPLE_WITH_PREMIUM = DAILY_SIMPLE + DAILY_PREMIUM
    DAILY_QUESTS_WITHOUT_EPIC = DAILY + DAILY_PREMIUM
    SORTED = DAILY + (EPIC,) + DAILY_PREMIUM + SUBS
    MAP_DAILY_QUESTS = {EASY: EASY_SUBS, MEDIUM: MEDIUM_SUBS, 
       HARD: HARD_SUBS, 
       BONUS: BONUS_SUBS}


DailyQuestDecorationMap = {1: (DailyQuestsDecorations.WIN), 
   2: (DailyQuestsDecorations.DEAL_DAMAGE), 
   3: (DailyQuestsDecorations.GET_EXPERIENCE), 
   4: (DailyQuestsDecorations.DESTROY_TANK), 
   5: (DailyQuestsDecorations.DAMAGE_TANK), 
   6: (DailyQuestsDecorations.FINISH_TOP1), 
   7: (DailyQuestsDecorations.FINISH_TOP3), 
   8: (DailyQuestsDecorations.FINISH_TOP5), 
   9: (DailyQuestsDecorations.FINISH_TOP7), 
   10: (DailyQuestsDecorations.DAMAGE_A_MODULE), 
   11: (DailyQuestsDecorations.SPOT)}

class DailyQuestsTokensPrefixes(object):
    QUEST_TOKEN = b'dq:'
    QUEST_TICKET = b'dqt:'
    EPIC_ACCESS_TOKEN = b'dqa:'


class OVERRIDDEN_BADGE(object):
    NONE = 0
    ENHANCEMENTS_LEVEL_1 = 1


DEFAULT_VECTOR_3 = (0.0, 0.0, 0.0)

class BonusTypes(object):
    SKILL = b'skill'
    ROLE = b'role'
    EXTRA = b'extra'
    PERK = b'perk'
    OPTIONAL_DEVICE = b'optionalDevice'
    EQUIPMENT = b'equipment'
    BATTLE_BOOSTER = b'battleBooster'
    PAIR_MODIFICATION = b'postProgressionPairModifications'
    BASE_MODIFICATION = b'postProgressionBaseModifications'
    BATTLE_MODIFIERS = b'battleModifiers'
    POSSIBLE = (
     SKILL, ROLE, EXTRA, PERK)


class PenaltyTypes(object):
    CREW = b'crew'
    BATTLE_MODIFIERS = b'battleModifiers'


class TTC_TOOLTIP_SECTIONS(object):
    EQUIPMENT = b'equipment'
    SKILLS = b'skills'
    CREW_MASTERY = b'crew_mastery'
    BATTLE_MODIFIERS = b'battle_modifiers'
    ALL = (
     EQUIPMENT, SKILLS, CREW_MASTERY, BATTLE_MODIFIERS)


class GF_RES_PROTOCOL(object):
    IMG = b'img://'
    CAMO = b'camo://'
    PNUM = b'pnum://'
    SWF = b'swf://'


class CollisionFlags(object):
    TRIANGLE_NOT_IN_BSP = 255
    TRIANGLE_CAMERANOCOLLIDE = 1
    TRIANGLE_TRANSPARENT = 2
    TRIANGLE_BLENDED = 4
    TRIANGLE_TERRAIN = 8
    TRIANGLE_NOCOLLIDE = 16
    TRIANGLE_DOUBLESIDED = 32
    TRIANGLE_WATER = 64
    TRIANGLE_PROJECTILENOCOLLIDE = 128
    TRIANGLE_COLLISIONFLAG_MASK = 255
    TRIANGLE_MATERIALKIND_MASK = 65280
    TRIANGLE_MATERIALKIND_SHIFT = 8


class UpgradeProhibitionReason(object):
    UNDEFINED = 0
    COMBATING = 1
    DROWNING = 2
    OVERTURNED = 3
    SETTLING = 4


class AreaTriggerActionType(enum.IntEnum):
    ENTER = 0
    LEAVE = 1


class EPlatoonButtonState(enum.Enum):
    SEARCHING_STATE = b'SEARCHING'
    IN_PLATOON_STATE = b'IN_PLATOON'
    CREATE_STATE = b'CREATE'


class HighExplosiveImpact(object):
    BLAST_WAVE = b'blastWave'
    SHELL_FRAGMENTS = b'shellFragments'
    ARMOR_SPALLS = b'armorSpalls'
    ALL = (
     BLAST_WAVE, SHELL_FRAGMENTS, ARMOR_SPALLS)


class DamageAbsorptionTypes(object):
    FRAGMENTS = 0
    BLAST = 1
    SPALLS = 2


DamageAbsorptionLabelToType = {b'FRAGMENTS': (DamageAbsorptionTypes.FRAGMENTS), 
   b'BLAST': (DamageAbsorptionTypes.BLAST), 
   b'SPALLS': (DamageAbsorptionTypes.SPALLS)}
DamageAbsorptionTypeToLabel = dict((type, label) for label, type in DamageAbsorptionLabelToType.items())
EQUIPMENT_COOLDOWN_MOD_SUFFIX = b'CooldownMod'
CHANCE_TO_HIT_SUFFIX_FACTOR = b'ChanceToHitDeviceMod'

class AbilitySystemScopeNames(object):
    DETACHMENT = b'detachment'
    CREW = b'crew'


PerkData = namedtuple(b'PerkData', b'level, args')
CrewContextArgs = namedtuple(b'CrewContextArgs', b'skillData')

class SkillProcessorArgs(object):
    __slots__ = (b'level', b'levelIncrease', b'isActive', b'isFire', b'skillConfig', b'hasActiveTankmanForBooster', b'tankmenSkillConfig')

    def __init__(self, level, levelIncrease, isActive, isFire, skillConfig, hasActiveTankmanForBooster):
        self.level = level
        self.levelIncrease = levelIncrease
        self.isActive = isActive
        self.isFire = isFire
        self.skillConfig = skillConfig
        self.tankmenSkillConfig = self.skillConfig
        self.hasActiveTankmanForBooster = hasActiveTankmanForBooster
        return

    def isSkillActive(self):
        return self.isActive and not self.isFire

    def isBoosterApplicable(self):
        return (self.isActive or self.hasActiveTankmanForBooster) and not self.isFire


class GroupSkillProcessorArgs(object):
    __slots__ = (b'factor', b'baseAvgLevel')

    def __init__(self, factor, baseAvgLevel):
        self.factor = factor
        self.baseAvgLevel = baseAvgLevel
        return


class ReloadRestriction(object):
    CYCLE_RELOAD = 1.0
    OTHER_RELOAD = 2.5

    @staticmethod
    def getBy(vehTypeDescr):
        if vehTypeDescr.gun.tags:
            return ReloadRestriction.OTHER_RELOAD
        return ReloadRestriction.CYCLE_RELOAD


class MapsTrainingParameters(enum.IntEnum):
    MAPS = 0
    VEHICLES = 1
    VISUAL_SCRIPT = 2
    SCENARIOS = 3
    MAP_SCENARIOS = 4
    MATCHMAKER = 5
    BOTS = 6
    MAP_REWARDS = 7


MAPS_REWARDS_INDEX = {b'scenarioComplete': 0, 
   b'mapComplete': 1}

class EquipSideEffect(enum.IntEnum):
    AMMO_AUTO_LOADED = 1
    AMMO_AUTO_LOAD_FAILED = 2


class VehicleSide(enum.IntEnum):
    FRONT = 0
    BACK = 1
    LEFT = 2
    RIGHT = 3


class SwitchState(enum.Enum):
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    INACTIVE = b'inactive'


class DeviceRepairMode(enum.IntEnum):
    NORMAL = 0
    SLOWED = 1
    SUSPENDED = 2


BATTLE_MODE_VEHICLE_TAGS = {
 384, 
 67, 
 850, 
 81, 
 382, 
 851, 
 852, 
 80, 
 381}
BATTLE_MODE_VEH_TAGS_EXCEPT_EVENT = BATTLE_MODE_VEHICLE_TAGS - {b'event_battles'}
BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC = BATTLE_MODE_VEHICLE_TAGS - {b'epic_battles'}
BATTLE_MODE_VEH_TAGS_EXCEPT_CLAN = BATTLE_MODE_VEHICLE_TAGS - {b'clanWarsBattles'}
BATTLE_MODE_VEH_TAGS_EXCEPT_FUN = BATTLE_MODE_VEHICLE_TAGS - {b'fun_random'}
BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7 = BATTLE_MODE_VEHICLE_TAGS - {b'comp7'}
BATTLE_MODE_VEH_TAGS_EXCEPT_RANKED = BATTLE_MODE_VEHICLE_TAGS - {b'ranked'}

@enum.unique
class EventPhase(enum.Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 2


class ACCOUNT_KICK_REASONS(object):
    UNAVAILABLE_PERIPHERY = -4
    VERSION_MISMATCH = -3
    NO_CONNECTION = -2
    UNKNOWN = 0
    LOGIN_TO_OTHER_GAME = 1
    SESSION_TRACKER_KICK = 2
    CLIENT_INACTIVE = 4
    SYSTEM_FAILURE = 5
    ROAMING_NOT_ALLOWED = 6
    SERVER_SHUT_DOWN = 7
    BAN = 8
    STEAM_LOGIN_NOT_ALLOWED = 9
    DOSSIERS_UNAVAILABLE = 10
    PRIVATE_CHANNEL_NAME_PROTECTION = 11
    PRIVATE_CHANNEL_IS_DISABLED = 12
    ACCOUNT_WAS_RESTORED = 13
    SPAM_PROTECTION_PDATA = 14
    SPAM_PROTECTION_SHOP = 15
    SPAM_PROTECTION_DOSSIER = 16
    CURFEW_BAN = 17
    DEMO_ACCOUNT_BOOTCAMP_FAILURE = 18
    BAN_RANGE = (
     BAN, CURFEW_BAN)


class BATTLE_MODE_LOCK_MASKS(object):
    _COMMON_FIRST_BIT = 0
    _CLAN_RENTED_VEHICLE_FIRST_BIT = 4
    _COMMON = 15 << _COMMON_FIRST_BIT
    _CLAN_RENTED_VEHICLE = 15 << _CLAN_RENTED_VEHICLE_FIRST_BIT

    @staticmethod
    def getCommonVehLockMode(vehLockMode):
        return (vehLockMode & BATTLE_MODE_LOCK_MASKS._COMMON) >> BATTLE_MODE_LOCK_MASKS._COMMON_FIRST_BIT

    @staticmethod
    def getClanRentedVehLockMode(vehLockMode):
        return (vehLockMode & BATTLE_MODE_LOCK_MASKS._CLAN_RENTED_VEHICLE) >> BATTLE_MODE_LOCK_MASKS._CLAN_RENTED_VEHICLE_FIRST_BIT

    @staticmethod
    def makeCompactVehLockMode(commonVehLockMode, clanRentedVehLockMode):
        return commonVehLockMode << BATTLE_MODE_LOCK_MASKS._COMMON_FIRST_BIT & BATTLE_MODE_LOCK_MASKS._COMMON | clanRentedVehLockMode << BATTLE_MODE_LOCK_MASKS._CLAN_RENTED_VEHICLE_FIRST_BIT & BATTLE_MODE_LOCK_MASKS._CLAN_RENTED_VEHICLE

    @staticmethod
    def getUnpackedVehLockMode(vehLockMode, vehType):
        if b'clanWarsBattles' in vehType.tags:
            return BATTLE_MODE_LOCK_MASKS.getClanRentedVehLockMode(vehLockMode)
        return BATTLE_MODE_LOCK_MASKS.getCommonVehLockMode(vehLockMode)


RESOURCE_WELL_FORBIDDEN_TOKEN = b'rws{}_forbidden'
RESOURCE_WELL_ALL_SEASON_FORBIDDEN_TOKEN = b'rws_forbidden'
QUESTS_SUPPORTED_EXCLUDE_TAGS = {
 861, 862, 863, 864, 865, 384}
VEHICLE_HEALTH_DECIMALS = 1
GUARANTEED_RANDOMIZED_DAMAGE = 1.0
GUARANTEED_RANDOMIZED_PIERCING_POWER = 1.0

class VehicleDirection(object):
    FORWARD = Vector3(0.0, 0.0, 1.0)
    SIDE = Vector3(1.0, 0.0, 0.0)
    UP = Vector3(0.0, 1.0, 0.0)


class Progress(object):
    DEFAULT = 0
    START = 1
    STOP = 2
    FAILED = 3
    SUCCEED = 4


class EQUIPMENT_ERROR_STATES(object):
    CAN_BE_ACTIVATED = 0
    CANNOT_BE_ACTIVATED = 1
    VEHICLE_IS_NOT_DAMAGED = 2
    NO_DAMAGED_ENEMY_VEHICLES = 4
    ALREADY_ACTIVATED = 8
    NOT_SUITABLE_LOADING_STATE = 16
    ALL = (
     CAN_BE_ACTIVATED, CANNOT_BE_ACTIVATED, VEHICLE_IS_NOT_DAMAGED, NO_DAMAGED_ENEMY_VEHICLES,
     ALREADY_ACTIVATED, NOT_SUITABLE_LOADING_STATE)


class BuffDisplayedState(enum.IntEnum):
    EMPTY = 0
    AOE_INSPIRE = 1
    AOE_HEAL = 2
    RISKY_ATTACK_BUFF = 3
    RISKY_ATTACK_HEAL = 4
    BERSERK = 5
    SNIPER = 6
    HUNTER = 7
    FAST_RECHARGE = 8
    ALLY_SUPPORT = 9
    JUGGERNAUT = 10
    SURE_SHOT = 11
    CONCENTRATION = 12
    MARCH = 13
    AGGRESSIVE_DETECTION = 14
    ABILITY_JUGGERNAUT = 15
    ABILITY_CONCENTRATION = 16
    ABILITY_SURE_SHOT = 17
    ABILITY_RECOIL_RECUPERATOR = 18
    ABILITY_COOLANT_TANK = 19
    ABILITY_TANK_RAM = 20
    ABILITY_SHOT_PASSION = 21


class EntityCaptured(object):
    POI_CAPTURABLE = b'poiCapturable'


class VehicleSelectionPlayerStatus(object):
    NOT_CONFIRMED = 0
    CONFIRMED = 1


INVALID_TIMESTAMP = -1
DEFAULT_HANGAR_SCENE = b'DEFAULT'
BATTLE_ROYALE_SCENE = b'BATTLE_ROYALE'
FESTIVAL_SCENE = b'FESTIVAL'
COMP7_SCENE = b'COMP7'
BOOTCAMP = b'BOOTCAMP'
VEHICLE_SELECTION_BLOCK_DELAY = 2

class BootcampVersion(object):
    DEFAULT = 1
    SHORT = 2


CURFEW_PLAY_LIMIT = b'curfew'
WEEKLY_PLAY_LIMIT = b'weeklyPlayLimit'
DAILY_PLAY_LIMIT = b'dailyPlayLimit'
SESSION_PLAY_LIMIT = b'sessionLimit'
PLAY_LIMITS = (
 CURFEW_PLAY_LIMIT, WEEKLY_PLAY_LIMIT, DAILY_PLAY_LIMIT, SESSION_PLAY_LIMIT)

class WoTPlusBonusType(object):
    GOLD_BANK = b'gold_bank'
    IDLE_CREW_XP = b'idle_crew_xp'
    EXCLUDED_MAP = b'excluded_map'
    FREE_EQUIPMENT_DEMOUNTING = b'free_equipment_demounting'
    EXCLUSIVE_VEHICLE = b'exclusive_vehicle'
    ATTENDANCE_REWARD = b'attendance_reward'
    TEAM_CREDITS_BONUS = b'team_credits_bonus'
    DAILY_QUESTS_REWARDS = b'daily_quests_rewards'


class PremiumSubsDailyAttendance(object):
    INITIAL_CYCLE_STEP = 1
    MAXIMUM_DISPLAYED_REWARDS = 3
    CYCLE_STEPS = 5


VEHICLE_NO_CREW_TRANSFER_PENALTY_TAG = b'noCrewTransferPenalty'
VEHICLE_PREMIUM_TAG = b'premium'
VEHICLE_WOT_PLUS_TAG = b'wotPlus'

class InitialVehsAdditionStrategy(object):
    REALM_AND_COUNTRY = 0
    COUNTRY = 1


class WINBACK_BATTLE_TOKEN_DRAW_REASON(enum.IntEnum):
    REGULAR = 0
    MANUAL = 1
    SQUAD = 2


class MarkerItem(object):
    DEFAULT = 0
    COMP7_RECON = 1
    POLYGONAL_ZONE = 2
    STATIC_DEATH_ZONE = 3
    STATIC_DEATH_ZONE_PROXIMITY = 4


class DROP_SKILL_OPTIONS(object):
    FREE_DROP_WITH_TOKEN_INDEX = 99


class BOT_DISPLAY_STATUS(enum.IntEnum):
    REGULAR = 0
    ELITE = 1
    BOSS = 2


class AchievementsLayoutStates(enum.IntEnum):
    AUTO = 0
    MANUAL = 1


class ShootImpulseApplicationPoint(object):
    VEHICLE_COM = b'vehicleCOM'
    SHOOT_POINT = b'shootPoint'
    ALL = {
     VEHICLE_COM, SHOOT_POINT}


RP_POINT = b'rp_point'
RP_PGB_POINT = b'rp_pgb_point'

class EdgeColorMode(enum.IntEnum):
    ENEMY = 1
    ALLY = 2


class EdgeDrawMode(enum.IntEnum):
    FULL = 0
    OCCLUDED = 1
    UNOCCLUDED = 2


class LootBoxTiers(enum.IntEnum):
    SIMPLE = 1
    BRONZE = 2
    SILVER = 3
    GOLD = 4


ALL_LOOTBOX_TIERS = tuple(t for t in LootBoxTiers)

class MinimapLayerType(object):
    BASE = b'base'
    ALERT = b'alert'
    ALL = (BASE, ALERT)


class RANDOM_FLAGS:
    IS_ONLY_10_MODE_ENABLED = 1
    IS_MAPS_IN_DEVELOPMENT_ENABLED = 2


class VEHICLE_MOVEMENT_STATES(object):
    NORMAL = b'normal'
    SLOW = b'slow'
    STOP = b'stop'


class UNIQUE_UNLOCK_FEATURE_NAMES:
    EARLY_ACCESS_FEATURE_NAME = b'earlyAccess'
    PARAGONS_FEATURE_NAME = b'paragons'


ALL_EVENT_TYPES_FOR_BONUSES = b'all'
EXTENSIONS_BONUSES = {}

class FRONTLINE_PROGRESSION:
    BORDERS_Z = 4
    BORDERS_X = 4
    DIRECTION = AXIS_ALIGNED_DIRECTION.PLUS_Z


class CoolantTankAbilityState(enum.IntEnum):
    ACTIVE = 0
    DEACTIVATED = 1
    GUN_RELOAD_FINISHED = 2


class InitialExperienceChoice(enum.IntEnum):
    UNSPECIFIED = 0
    NEWBIE = 1
    INEXPERIENCED = 2
    EXPERIENCED = 3
    SKIPPED = 4


LIMITED_UI_VERSION = 18
SERVICE_TOKEN_PREFIX = b'cmd:'
INVULNERABLE_EXTRAS = (b'engine', b'ammoBay', b'fuelTank', b'radio', b'gun', b'track', b'turretRotator', b'surveyingDevice', b'crew')

class DUAL_SHOT_CNT(enum.IntEnum):
    SINGLE = 1
    DUAL = 2


NOVICE_RESTRICTIONS_BAN_TYPE = b'novice_restrictions'
NOVICE_RESTRICTIONS_BAN_REASON = b'#ban_reason:novice_restrictions'
