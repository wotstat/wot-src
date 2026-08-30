import typing
from collections import OrderedDict
from constants import IS_DEVELOPMENT, SHELL_TYPES, SHELL_MECHANICS_TYPE
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
FAKE_MODIFIER_NAME = b'fakeModifier'
FAKE_PARAM_NAME = b'fakeParam'
DEBUG_MODIFIERS = IS_DEVELOPMENT
ERROR_TEMPLATE = b"[BattleModifiers] {} for param '{}'"

class DataType(object):
    INT = 0
    FLOAT = 1
    STRING = 2
    ID_TO_NAME = {INT: b'int', 
       FLOAT: b'float', 
       STRING: b'string'}
    NAME_TO_ID = dict((v, k) for k, v in ID_TO_NAME.iteritems())
    ALL = set(NAME_TO_ID.itervalues())
    NAMES = set(ID_TO_NAME.itervalues())


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
    NAME_TO_ID = dict((v, k) for k, v in ID_TO_NAME.iteritems())
    ALL = set(NAME_TO_ID.itervalues())
    NAMES = set(ID_TO_NAME.itervalues())
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
    POINTS_PER_SECOND = 17
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
       LOGIC: b'logic', 
       POINTS_PER_SECOND: b'points_per_second'}
    NAME_TO_ID = dict((v, k) for k, v in ID_TO_NAME.iteritems())
    ALL = set(NAME_TO_ID.itervalues())
    NAMES = set(ID_TO_NAME.itervalues())


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
       CONSTANTS: b'constants'}
    NAME_TO_ID = dict((v, k) for k, v in ID_TO_NAME.items())
    ALL = set(NAME_TO_ID.itervalues())
    NAMES = set(ID_TO_NAME.itervalues())


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
    REPAIR_POINT = b'stepRepairPoint'
    ALL = None


ClientDomain.ALL = set([v for k, v in ClientDomain.__dict__.iteritems() if not k.startswith(b'_') and k not in (b'UNDEFINED', b'ALL')])

class GameplayImpact(object):
    UNDEFINED = 0
    POSITIVE = 1
    NEGATIVE = 2
    HIDDEN = 3
    ID_TO_NAME = {UNDEFINED: b'undefined', 
       POSITIVE: b'positive', 
       NEGATIVE: b'negative', 
       HIDDEN: b'hidden'}
    NAME_TO_ID = dict((v, k) for k, v in ID_TO_NAME.items())
    ALL = set(NAME_TO_ID.itervalues())
    NAMES = set(ID_TO_NAME.itervalues())


class ModifierRestriction(object):
    MIN = 0
    MAX = 1
    USE_TYPES = 2
    LIMITS = (
     MIN, MAX)
    ID_TO_NAME = {MIN: b'min', 
       MAX: b'max', 
       USE_TYPES: b'useTypes'}
    NAME_TO_ID = dict((v, k) for k, v in ID_TO_NAME.items())
    ALL = set(NAME_TO_ID.itervalues())
    NAMES = set(ID_TO_NAME.itervalues())


class NodeType(object):
    ROOT = b'root'
    SHELL = b'shell'
    VEHICLE = b'vehicle'
    SUPPORTED_DOMAINS = {ROOT: 0, 
       SHELL: (ModifierDomain.SHOT_COMPONENTS), 
       VEHICLE: (ModifierDomain.VEHICLE_COMPONENTS)}


class ShellCaliber(object):
    AUTO = b'auto'
    SMALL = b'small'
    MEDIUM = b'medium'
    MAIN = b'main'
    LARGE = b'large'
    HUGE = b'huge'
    NAME_TO_CALIBER = OrderedDict((
     (
      HUGE, 155),
     (
      LARGE, 108),
     (
      MAIN, 85),
     (
      MEDIUM, 50),
     (
      SMALL, 20),
     (
      AUTO, 7)))
    CALIBERS_AND_NAMES = None

    @classmethod
    def get(cls, targetCaliber):
        for name, caliber in cls.NAME_TO_CALIBER.iteritems():
            if targetCaliber >= caliber:
                return name

        return cls.AUTO


class ShellKind(object):
    HOLLOW_CHARGE = b'HOLLOW_CHARGE'
    ARMOR_PIERCING = b'ARMOR_PIERCING'
    ARMOR_PIERCING_HE = b'ARMOR_PIERCING_HE'
    ARMOR_PIERCING_CR = b'ARMOR_PIERCING_CR'
    ARMOR_PIERCING_FSDS = b'ARMOR_PIERCING_FSDS'
    SMOKE = b'SMOKE'
    HIGH_EXPLOSIVE_MODERN = b'HIGH_EXPLOSIVE_MODERN'
    HIGH_EXPLOSIVE_LEGACY_STUN = b'HIGH_EXPLOSIVE_LEGACY_STUN'
    HIGH_EXPLOSIVE_LEGACY_NO_STUN = b'HIGH_EXPLOSIVE_LEGACY_NO_STUN'
    IMPROVED_POSTFIX = b'_GOLD'
    ALL_KEY = b'ALL'
    ALL_REGULAR = {
     HOLLOW_CHARGE, 
     ARMOR_PIERCING, ARMOR_PIERCING_HE, ARMOR_PIERCING_CR, 
     ARMOR_PIERCING_FSDS, 
     SMOKE, 
     HIGH_EXPLOSIVE_MODERN, 
     HIGH_EXPLOSIVE_LEGACY_STUN, HIGH_EXPLOSIVE_LEGACY_NO_STUN}
    ALL_IMPROVED = set([key + IMPROVED_POSTFIX for key in ALL_REGULAR])

    @classmethod
    def get(cls, shellDescr, withGold=True):
        if shellDescr.kind != SHELL_TYPES.HIGH_EXPLOSIVE:
            kind = shellDescr.kind
        elif shellDescr.type.mechanics == SHELL_MECHANICS_TYPE.MODERN:
            kind = cls.HIGH_EXPLOSIVE_MODERN
        elif shellDescr.hasStun:
            kind = cls.HIGH_EXPLOSIVE_LEGACY_STUN
        else:
            kind = cls.HIGH_EXPLOSIVE_LEGACY_NO_STUN
        if shellDescr.isGold and withGold:
            return kind + cls.IMPROVED_POSTFIX
        return kind


class ModifiersWithRemapping(object):
    GUN_EFFECTS = b'gunEffects'
    SHOT_EFFECTS = b'shotEffects'
    SOUND_NOTIFICATIONS = b'soundNotifications'
    ALL = {
     GUN_EFFECTS, SHOT_EFFECTS, SOUND_NOTIFICATIONS}


class RemappingConditionNames(object):
    CALIBER = b'caliber'
    SHELL_KIND = b'shellKind'
    ALL = {
     CALIBER, SHELL_KIND}


class RemappingNames(object):
    TEST = b'test'
    ALL = set(() + ((TEST,) if IS_DEVELOPMENT else ()))
