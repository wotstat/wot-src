from __future__ import absolute_import
import typing
from collections import OrderedDict
from future.utils import viewitems, viewvalues, iteritems
from constants import IS_DEVELOPMENT, SHELL_TYPES, BATTLE_LOG_SHELL_TYPES
if typing.TYPE_CHECKING:
    from items.vehicle_items import Shell
BATTLE_PARAMS_XML_PATH = b'scripts/item_defs/battle_params.xml'
REMAPPING_XML_PATH = b'scripts/item_defs/remapping.xml'
BATTLE_MODIFIERS_DIR = b'scripts/server_xml/battle_modifiers/'
BATTLE_MODIFIERS_XML = b'battle_modifiers.xml'
USE_VEHICLE_CACHE = True
USE_CONSTANTS_CACHE = True
MAX_VEHICLE_CACHE_LAYER_COUNT = 5
MAX_CONSTANTS_CACHE_LAYER_COUNT = 5
FAKE_PARAM_NAME = b'fakeParam'
DEBUG_MODIFIERS = IS_DEVELOPMENT
ERROR_TEMPLATE = b'[BattleModifiers] {} for param {}'

class DataType(object):
    INT = 0
    FLOAT = 1
    STRING = 2
    DICT = 3
    HASHABLE_DICT = 4
    HASHABLE_TYPES = (
     INT, FLOAT, STRING, HASHABLE_DICT)
    ID_TO_NAME = {INT: b'int', 
       FLOAT: b'float', 
       STRING: b'string', 
       DICT: b'dict', 
       HASHABLE_DICT: b'hashable_dict'}
    NAME_TO_ID = {v: k for k, v in viewitems(ID_TO_NAME)}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))


class UseType(object):
    UNDEFINED = 0
    VAL = 1
    MUL = 2
    ADD = 3
    DIMENSIONAL_TYPES = {
     VAL, ADD}
    ID_TO_NAME = {VAL: b'val', 
       MUL: b'mul', 
       ADD: b'add'}
    NAME_TO_ID = {v: k for k, v in viewitems(ID_TO_NAME)}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))
    ALL_WITH_UNDEFINED = ALL | {UNDEFINED}
    NON_DIMENSIONAL_TYPES = ALL_WITH_UNDEFINED - DIMENSIONAL_TYPES


class PhysicalType(object):
    UNDEFINED = 0
    SECONDS = 1
    MINUTES = 2
    MILLIMETERS = 3
    METERS = 4
    METERS_PER_SECOND = 5
    KILOMETERS_PER_HOUR = 6
    METER_PER_SECOND_SQUARED = 7
    DEGREES = 8
    RADIANS = 9
    DEGREES_PER_SECOND = 10
    RADIANS_PER_SECOND = 11
    HIT_POINTS = 12
    HORSEPOWER = 13
    PROBABILITY = 14
    DEVIATION = 15
    LOGIC = 16
    ID_TO_NAME = {UNDEFINED: b'undefined', 
       SECONDS: b'seconds', 
       MINUTES: b'minutes', 
       MILLIMETERS: b'millimeters', 
       METERS: b'meters', 
       METERS_PER_SECOND: b'metersPerSecond', 
       KILOMETERS_PER_HOUR: b'km_per_hour', 
       METER_PER_SECOND_SQUARED: b'meter_per_second_squared', 
       DEGREES: b'degrees', 
       RADIANS: b'radians', 
       DEGREES_PER_SECOND: b'degrees_per_second', 
       RADIANS_PER_SECOND: b'radians_per_second', 
       HIT_POINTS: b'hitPoints', 
       HORSEPOWER: b'horsepower', 
       PROBABILITY: b'probability', 
       DEVIATION: b'deviation', 
       LOGIC: b'logic'}
    NAME_TO_ID = {v: k for k, v in viewitems(ID_TO_NAME)}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))


class ModifierDomain(object):
    COMMON = 1
    VEH_TYPE = 2
    CHASSIS = 4
    TURRET = 8
    GUN = 16
    SHOT = 32
    SHELL = 64
    SHELL_TYPE = 128
    RADIO = 256
    PHYSICS = 512
    ENGINE = 1024
    HULL = 2048
    VEHICLE = 4096
    CONSTANTS = 8192
    VSE = 16384
    FAKE = 32768
    SHELL_COMPONENTS = SHELL | SHELL_TYPE
    SHOT_COMPONENTS = SHOT | SHELL_COMPONENTS
    GUN_COMPONENTS = GUN | SHOT_COMPONENTS
    TURRET_COMPONENTS = TURRET | GUN_COMPONENTS
    VEH_TYPE_COMPONENTS = VEH_TYPE | CHASSIS | TURRET_COMPONENTS | RADIO | PHYSICS | ENGINE | HULL
    VEHICLE_COMPONENTS = VEHICLE | VEH_TYPE_COMPONENTS
    DEFAULT = COMMON
    ID_TO_NAME = {COMMON: b'common', 
       VEH_TYPE: b'vehType', 
       CHASSIS: b'chassis', 
       TURRET: b'turret', 
       GUN: b'gun', 
       SHOT: b'shot', 
       SHELL: b'shell', 
       SHELL_TYPE: b'shellType', 
       RADIO: b'radio', 
       PHYSICS: b'physics', 
       ENGINE: b'engine', 
       HULL: b'hull', 
       VEHICLE: b'vehicle', 
       CONSTANTS: b'constants', 
       VSE: b'vse', 
       FAKE: b'fake'}
    NAME_TO_ID = {v: k for k, v in viewitems(ID_TO_NAME)}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))


class ClientDomain(object):
    UNDEFINED = b'undefined'
    ACCURACY = b'accuracy'
    ARMOR_PIERCING = b'armorPiercing'
    BATTLE_PARAMS = b'battleParams'
    CONCEALMENT = b'concealment'
    DAMAGE_DEALING = b'damageDealing'
    MOBILITY = b'mobility'
    RANDOMIZATION = b'randomization'
    SUSTAINING = b'sustaining'
    VISIBILITY = b'visibility'
    VITALITY = b'vitality'
    ALL = set()


ClientDomain.ALL = set(v for k, v in viewitems(ClientDomain.__dict__) if not k.startswith(b'_') and k not in (b'UNDEFINED', b'ALL'))

class GameplayImpact(object):
    UNDEFINED = 0
    POSITIVE = 1
    NEGATIVE = 2
    HIDDEN = 3
    ID_TO_NAME = {UNDEFINED: b'undefined', 
       POSITIVE: b'positive', 
       NEGATIVE: b'negative', 
       HIDDEN: b'hidden'}
    NAME_TO_ID = {v: k for k, v in viewitems(ID_TO_NAME)}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))


class ModifierRestriction(object):
    MIN = 0
    MAX = 1
    USE_TYPES = 2
    LIMITS = (
     MIN, MAX)
    ID_TO_NAME = {MIN: b'min', 
       MAX: b'max', 
       USE_TYPES: b'useTypes'}
    NAME_TO_ID = {v: k for k, v in viewitems(ID_TO_NAME)}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))


class NodeType(object):
    ROOT = b'root'
    SHELL = b'shell'
    VEHICLE = b'vehicle'
    SUPPORTED_DOMAINS = {ROOT: 0, 
       SHELL: (ModifierDomain.SHOT_COMPONENTS), 
       VEHICLE: (ModifierDomain.VEHICLE_COMPONENTS)}


class Caliber(object):
    AUTO = b'auto'
    SMALL = b'small'
    MEDIUM = b'medium'
    MAIN = b'main'
    LARGE = b'large'
    HUGE = b'huge'
    NAME_TO_CALIBER = OrderedDict()

    @classmethod
    def get(cls, targetCaliber):
        for name, caliber in iteritems(cls.NAME_TO_CALIBER):
            if targetCaliber >= caliber:
                return name

        return cls.AUTO


class GunCaliber(Caliber):
    NAME_TO_CALIBER = OrderedDict((
     (
      Caliber.HUGE, 140),
     (
      Caliber.LARGE, 105),
     (
      Caliber.MAIN, 85),
     (
      Caliber.MEDIUM, 50),
     (
      Caliber.SMALL, 20),
     (
      Caliber.AUTO, 7)))


class ShellCaliber(Caliber):
    NAME_TO_CALIBER = OrderedDict((
     (
      Caliber.HUGE, 155),
     (
      Caliber.LARGE, 108),
     (
      Caliber.MAIN, 85),
     (
      Caliber.MEDIUM, 50),
     (
      Caliber.SMALL, 20),
     (
      Caliber.AUTO, 7)))


class ShellKind(object):
    IMPROVED_POSTFIX = SHELL_TYPES.IMPROVED_POSTFIX
    ALL_KEY = b'ALL'
    ALL_REGULAR = {
     SHELL_TYPES.HOLLOW_CHARGE, SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_HE,
     SHELL_TYPES.ARMOR_PIERCING_CR, SHELL_TYPES.SMOKE,
     SHELL_TYPES.HIGH_EXPLOSIVE_MODERN, SHELL_TYPES.HIGH_EXPLOSIVE_LEGACY_STUN,
     SHELL_TYPES.HIGH_EXPLOSIVE_LEGACY_NO_STUN}
    ALL_IMPROVED = set(key + SHELL_TYPES.IMPROVED_POSTFIX for key in ALL_REGULAR)

    @classmethod
    def get(cls, shellDescr, withGold=True):
        return BATTLE_LOG_SHELL_TYPES.getShellType(shellDescr, withGold)


class ModifiersWithRemapping(object):
    GUN_EFFECTS = b'gunEffects'
    GUN_MAIN_PREFAB = b'gunMainPrefab'
    SHOT_EFFECTS = b'shotEffects'
    GUN_PREFAB_EFFECTS = b'gunPrefabEffects'
    SHOT_PREFAB_EFFECTS = b'shotPrefabEffects'
    SOUND_NOTIFICATIONS = b'soundNotifications'
    EXHAUST_EFFECTS = b'exhaustEffects'
    ROOT_PREFABS_MECHANIC_EFFECTS = b'rootPrefabsMechanicEffects'
    ALL = {
     GUN_EFFECTS, GUN_MAIN_PREFAB, SHOT_EFFECTS, 
     GUN_PREFAB_EFFECTS, 
     SHOT_PREFAB_EFFECTS, 
     SOUND_NOTIFICATIONS, EXHAUST_EFFECTS, 
     ROOT_PREFABS_MECHANIC_EFFECTS}


class RemappingConditionNames(object):
    REMAPPING_NAME = b'remappingName'
    NATION = b'nation'
    OUTFIT = b'outfit'
    GUN_NAME = b'gunName'
    GUN_CALIBER = b'gunCaliber'
    SHELL_KIND = b'shellKind'
    SHELL_SHOTS_COUNT = b'shellShotsCount'
    SHELL_CALIBER = b'shellCaliber'
    ALL = {
     REMAPPING_NAME, NATION, OUTFIT, GUN_NAME, GUN_CALIBER, SHELL_KIND, 
     SHELL_SHOTS_COUNT, SHELL_CALIBER}


class RemappingNames(object):
    TEST = b'test'
    FEP_FALL_TANKS = b'fep_fall_tanks'
    ALL = set((FEP_FALL_TANKS,) + ((TEST,) if IS_DEVELOPMENT else ()))
