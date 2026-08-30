from __future__ import absolute_import
import constants, UnitBase
from constants_utils import ConstInjector
DEFAULT_ASSETS_PACK = b'undefined'
DEFAULT_SETTINGS_KEY = b'undefined'
DEFAULT_PRIORITY = 0
FUN_EVENT_ID_KEY = b'funEventID'
UNKNOWN_EVENT_ID = 0
UNKNOWN_EVENT_NAME = b'unknown_event'
UNKNOWN_WWISE_REMAPPING = b'unknownRemapping'
FUN_GAME_PARAMS_KEY = b'fun_random_config'
BATTLE_MODE_VEH_TAGS_EXCEPT_FUN = constants.BATTLE_MODE_VEHICLE_TAGS - {b'fun_random'}

class FunSubModeImpl(object):
    UNDEFINED = 0
    DEFAULT = 1
    DEV_TEST = 2
    ALL = (
     DEFAULT,) + ((DEV_TEST,) if constants.IS_DEVELOPMENT else ())


class FunProgressionCondition(object):
    BATTLES = b'battles'
    DAMAGE = b'damage'
    TOP = b'top'
    WIN = b'win'
    ALL = (BATTLES, DAMAGE, TOP, WIN)


class FunEfficiencyParameter(object):
    KILLS = b'kills'
    SPOTTED = b'spotted'
    STUN = b'damageAssistedStun'
    DAMAGE_DEALT = b'damageDealt'
    DAMAGE_ASSISTED = b'damageAssisted'
    DAMAGE_BLOCKED_BY_ARMOR = b'damageBlockedByArmor'
    CAPTURE_POINTS = b'capturePoints'
    DROPPED_CAPTURE_POINTS = b'droppedCapturePoints'
    ALL = (
     KILLS, SPOTTED, STUN, DAMAGE_DEALT, DAMAGE_ASSISTED, DAMAGE_BLOCKED_BY_ARMOR,
     CAPTURE_POINTS, DROPPED_CAPTURE_POINTS)


class FunPerformanceParameter(object):
    RECOMMENDED_GRAPHICS_PRESET = b'recommendedGraphicsPreset'
    RENDER_PIPELINE = b'renderPipeline'
    MEDIUM_RISK = b'mediumRisk'
    HIGH_RISK = b'highRisk'
    ALL = (RECOMMENDED_GRAPHICS_PRESET, RENDER_PIPELINE, MEDIUM_RISK, HIGH_RISK)


class FunEfficiencyParameterCount(object):
    MIN = 3
    MAX = 5


class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    FUN_RANDOM = 29
    FUN_RANDOM_RANGE = (
     FUN_RANDOM,)


class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    FUN_RANDOM = 42


class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    FUN_RANDOM = 131072


class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    FUN_RANDOM_ROSTER = UNIT_MGR_FLAGS.FUN_RANDOM | UNIT_MGR_FLAGS.SQUAD


class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    FUN_RANDOM = constants.PREBATTLE_TYPE.FUN_RANDOM


class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    CHANGE_FUN_EVENT_ID = 29
