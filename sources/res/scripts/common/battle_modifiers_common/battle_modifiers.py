from __future__ import absolute_import
from builtins import object
from future.utils import viewitems, viewvalues
from ResMgr import DataSection
from constants import AOI, PIERCING_POWER_INTERPOLATION_DIST_FIRST, PIERCING_POWER_INTERPOLATION_DIST_LAST, DAMAGE_INTERPOLATION_DIST_FIRST, DAMAGE_INTERPOLATION_DIST_LAST
from typing import TYPE_CHECKING, Optional, Any, Tuple, Union, Dict, List
if TYPE_CHECKING:
    from items.vehicles import VehicleType
    from battle_modifiers_ext.battle_modifiers import BattleModifier
EXT_DATA_MODIFIERS_KEY = b'battleModifiers'

class BattleParams(object):
    VEHICLE_HEALTH = b'vehicleHealth'
    GRAVITY_FACTOR = b'gravityFactor'
    DISP_FACTOR_CHASSIS_MOVEMENT = b'dispFactorChassisMovement'
    DISP_FACTOR_CHASSIS_ROTATION = b'dispFactorChassisRotation'
    TURRET_ROTATION_SPEED = b'turretRotationSpeed'
    GUN_ROTATION_SPEED = b'gunRotationSpeed'
    RELOAD_TIME = b'reloadTime'
    TWIN_GUN_RELOAD_TIME = b'twinGunReloadTime'
    CLIP_INTERVAL = b'clipInterval'
    BURST_INTERVAL = b'burstInterval'
    AUTORELOAD_TIME = b'autoreloadTime'
    AIMING_TIME = b'aimingTime'
    SHOT_DISPERSION_RADIUS = b'shotDispersionRadius'
    DISP_FACTOR_TURRET_ROTATION = b'dispFactorTurretRotation'
    DISP_FACTOR_AFTER_SHOT = b'dispFactorAfterShot'
    DISP_FACTOR_WHILE_GUN_DAMAGED = b'dispFactorWhileGunDamaged'
    SHELL_GRAVITY = b'shellGravity'
    SHELL_SPEED = b'shellSpeed'
    PIERCING_POWER_FIRST = b'piercingPowerFirst'
    PIERCING_POWER_LAST = b'piercingPowerLast'
    DAMAGE_RANDOMIZATION = b'damageRandomization'
    PIERCING_POWER_RANDOMIZATION = b'piercingPowerRandomization'
    NORMALIZATION_ANGLE = b'normalizationAngle'
    RICOCHET_ANGLE = b'ricochetAngle'
    ENGINE_POWER = b'enginePower'
    ENGINE_FIRE_FACTOR = b'engineFireFactor'
    FW_MAX_SPEED = b'fwMaxSpeed'
    BK_MAX_SPEED = b'bkMaxSpeed'
    ROTATION_SPEED_ON_STILL = b'rotationSpeedOnStill'
    ROTATION_SPEED_ON_MOVE = b'rotationSpeedOnMove'
    ARMOR_DAMAGE_FIRST = b'armorDamageFirst'
    ARMOR_DAMAGE_LAST = b'armorDamageLast'
    DEVICE_DAMAGE_FIRST = b'deviceDamageFirst'
    DEVICE_DAMAGE_LAST = b'deviceDamageLast'
    INVISIBILITY_ON_STILL = b'invisibilityOnStill'
    INVISIBILITY_ON_MOVE = b'invisibilityOnMove'
    VISION_RADIUS = b'visionRadius'
    RADIO_DISTANCE = b'radioDistance'
    BATTLE_LENGTH = b'battleLength'
    VEHICLE_RAMMING_DAMAGE = b'vehicleRammingDamage'
    VEHICLE_PRESSURE_DAMAGE = b'vehiclePressureDamage'
    TURRET_RAMMING_DAMAGE = b'turretRammingDamage'
    TURRET_PRESSURE_DAMAGE = b'turretPressureDamage'
    ENV_HULL_DAMAGE = b'envHullDamage'
    ENV_CHASSIS_DAMAGE = b'envChassisDamage'
    ENV_TANKMAN_DAMAGE_CHANCE = b'envTankmanDamageChance'
    ENV_MODULE_DAMAGE_CHANCE = b'envModuleDamageChance'
    REPAIR_SPEED = b'repairSpeed'
    VISION_MIN_RADIUS = b'visionMinRadius'
    VISION_MAX_RADIUS = b'visionMaxRadius'
    VISION_TIME = b'visionTime'
    EQUIPMENT_COOLDOWN = b'equipmentCooldown'
    FWD_FRICTION = b'fwdFriction'
    SIDE_FRICTION = b'sideFriction'
    DIRT_RELEASE_RATE = b'dirtReleaseRate'
    MAX_DIRT = b'maxDirt'
    SHOT_EFFECTS = b'shotEffects'
    GUN_EFFECTS = b'gunEffects'
    SHOT_PREFAB_EFFECTS = b'shotPrefabEffects'
    GUN_PREFAB_EFFECTS = b'gunPrefabEffects'
    DESTRUCTION_EFFECT = b'destructionEffect'
    FULL_DESTRUCTION_EFFECT = b'fullDestructionEffect'
    CHASSIS_DECALS = b'chassisDecals'
    ENGINE_SOUNDS = b'engineSounds'
    EXHAUST_EFFECTS = b'exhaustEffects'
    ARMOR_SPALLS_ARMOR_DAMAGE_FIRST = b'armorSpallsArmorDamageFirst'
    ARMOR_SPALLS_ARMOR_DAMAGE_LAST = b'armorSpallsArmorDamageLast'
    ARMOR_SPALLS_DEVICE_DAMAGE_FIRST = b'armorSpallsDeviceDamageFirst'
    ARMOR_SPALLS_DEVICE_DAMAGE_LAST = b'armorSpallsDeviceDamageLast'
    ARMOR_SPALLS_IMPACT_RADIUS = b'armorSpallsImpactRadius'
    ARMOR_SPALLS_CONE_ANGLE = b'armorSpallsConeAngle'
    ARMOR_SPALLS_DAMAGE_ABSORPTION = b'armorSpallsDamageAbsorption'
    CHANGE_SHELL_TYPE = b'changeShellType'
    CALIBER_TO_EXPLOSION_RADIUS = b'caliberToExplosionRadius'
    MODE_CREDITS_FACTOR = b'modeCreditsFactor'
    INVISIBILITY_FACTOR_AT_SHOT = b'invisibilityFactorAtShot'
    VEHICLE_AOI_RADIUS = b'vehicleAoIRadius'
    SOUND_NOTIFICATIONS = b'soundNotifications'
    DIVING_DESTRUCTION_DELAY = b'divingDestructionDelay'
    STUN_FACTOR_ENGINE_POWER = b'stunFactorEnginePower'
    STUN_FACTOR_VEHICLE_ROTATION_SPEED = b'stunFactorVehicleRotationSpeed'
    STUN_FACTOR_TURRET_TRAVERSE = b'stunFactorTurretTraverse'
    STUN_FACTOR_MAX_SPEED = b'stunFactorMaxSpeed'
    PIERCING_POWER_INTERPOLATION_DIST_FIRST = b'piercingPowerInterpolationDistFirst'
    PIERCING_POWER_INTERPOLATION_DIST_LAST = b'piercingPowerInterpolationDistLast'
    DAMAGE_INTERPOLATION_DIST_FIRST = b'damageInterpolationDistFirst'
    DAMAGE_INTERPOLATION_DIST_LAST = b'damageInterpolationDistLast'
    BONUS_CAPS_OVERRIDES = b'bonusCapsOverrides'
    CRYSTAL_REWARDS = b'crystalRewards'
    GOLD_RESERVE_GAINS = b'goldReserveGains'
    DAMAGE_RANDOMIZATION_TYPE = b'damageRandomizationType'
    PIERCING_POWER_RANDOMIZATION_TYPE = b'piercingPowerRandomizationType'
    SHELL_STUN = b'shellStun'
    FORCED_RELOAD_TIME = b'forcedReloadTime'
    AUTO_SHOOT_DISPERSION_PER_SHOT = b'autoShootDispersionPerShot'
    AUTO_SHOOT_MAX_SHOT_DISPERSION_FACTOR = b'autoShootMaxShotDispersionFactor'
    GUN_MAIN_PREFAB = b'gunMainPrefab'
    POSTMORTEM_OVERRIDES = b'postMortemOverrides'
    ROOT_PREFABS_MECHANIC_EFFECTS = b'rootPrefabsMechanicEffects'
    AMMO_BAY_HEALTH = b'ammoBayHealth'
    ENGINE_HEALTH = b'engineHealth'
    FUEL_TANK_HEALTH = b'fuelTankHealth'
    TURRET_ROTATOR_HEALTH = b'turretRotatorHealth'
    SURVEYING_DEVICE_HEALTH = b'surveyingDeviceHealth'
    CHASSIS_HEALTH = b'chassisHealth'
    GUN_HEALTH = b'gunHealth'
    FAKE_MODIFIER = b'fakeModifier'
    VSE_MODIFIER = b'vseModifier'
    DYNAMIC = {
     FAKE_MODIFIER, VSE_MODIFIER}
    ALL = set()


BattleParams.ALL = set(v for k, v in viewitems(BattleParams.__dict__) if not k.startswith(b'_') and k not in (b'DYNAMIC', b'ALL'))

class ConstantsSet(object):
    __slots__ = (b'VEHICLE_CIRCULAR_AOI_RADIUS', b'VEHICLE_CIRCULAR_AOI_RADIUS_HYSTERESIS_MARGIN', b'PIERCING_POWER_INTERPOLATION_DIST_FIRST', b'PIERCING_POWER_INTERPOLATION_DIST_LAST', b'DAMAGE_INTERPOLATION_DIST_FIRST', b'DAMAGE_INTERPOLATION_DIST_LAST')

    def __init__(self):
        self.VEHICLE_CIRCULAR_AOI_RADIUS = AOI.VEHICLE_CIRCULAR_AOI_RADIUS
        self.VEHICLE_CIRCULAR_AOI_RADIUS_HYSTERESIS_MARGIN = AOI.VEHICLE_CIRCULAR_AOI_RADIUS_HYSTERESIS_MARGIN
        self.PIERCING_POWER_INTERPOLATION_DIST_FIRST = PIERCING_POWER_INTERPOLATION_DIST_FIRST
        self.PIERCING_POWER_INTERPOLATION_DIST_LAST = PIERCING_POWER_INTERPOLATION_DIST_LAST
        self.DAMAGE_INTERPOLATION_DIST_FIRST = DAMAGE_INTERPOLATION_DIST_FIRST
        self.DAMAGE_INTERPOLATION_DIST_LAST = DAMAGE_INTERPOLATION_DIST_LAST
        return


CONSTANTS_ORIGINAL = ConstantsSet()

class ModifierScope(object):
    BASE = 1
    CELL = 2
    CLIENT = 4
    POST_BATTLE = 8
    HANGAR = 16
    BATTLE = BASE | CELL | CLIENT | POST_BATTLE
    FULL = BATTLE | HANGAR
    ID_TO_NAME = {BASE: b'base', 
       CELL: b'cell', 
       CLIENT: b'client', 
       POST_BATTLE: b'postBattle', 
       HANGAR: b'hangar'}
    NAME_TO_ID = {v: k for k, v in ID_TO_NAME.items()}
    ALL = set(viewvalues(NAME_TO_ID))
    NAMES = set(viewvalues(ID_TO_NAME))


class BattleModifiers(object):

    def __init__(self, source=None):
        return

    def __call__(self, paramId, value, ctx=None):
        return value

    def __iter__(self):
        return iter([])

    def __getitem__(self, paramId):
        return

    def __len__(self):
        return 0

    def __contains__(self, paramId):
        return False

    def __bool__(self):
        return False

    __nonzero__ = __bool__

    def __hash__(self):
        return 0

    def __eq__(self, other):
        return False

    def __repr__(self):
        return b'BattleModifiers()'

    @staticmethod
    def retrieveDescr(descr, scope=ModifierScope.FULL):
        return ()

    @staticmethod
    def getConstantsOriginal():
        return CONSTANTS_ORIGINAL

    @staticmethod
    def clearVehicleModifications():
        return

    @staticmethod
    def clearConstantsModifications():
        return

    def get(self, paramId):
        return

    def descr(self, scope=ModifierScope.FULL):
        return ()

    def domain(self):
        return 0

    def haveDomain(self, domain):
        return False

    def scope(self):
        return 0

    def haveScope(self, scope):
        return False

    def id(self):
        return 0

    def getVehicleModification(self, vehType):
        return vehType

    def getConstantsModification(self):
        return CONSTANTS_ORIGINAL

    def getVsePlansByAspect(self, aspect):
        return []


class ModifiersContext(object):
    __slots__ = (b'__modifiers', b'__modificationCtx')

    def __init__(self, modifiers, **modificationCtx):
        self.__modifiers = modifiers
        self.__modificationCtx = modificationCtx or {}
        return

    def __getattr__(self, item):
        return getattr(self.__modifiers, item)

    def __deepcopy__(self, memo):
        return ModifiersContext(self.__modifiers, **self.__modificationCtx)

    def __copy__(self):
        return ModifiersContext(self.__modifiers, **self.__modificationCtx)

    def __call__(self, paramId, value):
        return self.__modifiers(paramId, value, self)

    def __iter__(self):
        return iter(self.__modifiers)

    def __getitem__(self, paramId):
        return self.__modifiers[paramId]

    def __len__(self):
        return len(self.__modifiers)

    def __contains__(self, paramId):
        return paramId in self.__modifiers

    def __bool__(self):
        return bool(self.__modifiers)

    __nonzero__ = __bool__

    def __hash__(self):
        return hash(self.__modifiers)

    def __eq__(self, other):
        return self.modifiers == other.modifiers

    def __repr__(self):
        return (b'ModifiersContext(modifiers {}, modificationCtx {})').format(self.__modifiers, self.__modificationCtx)

    @property
    def modifiers(self):
        return self.__modifiers

    @property
    def modificationCtx(self):
        return self.__modificationCtx


BATTLE_MODIFIERS_TYPE = Union[BattleModifiers, ModifiersContext]

def getGlobalModifiers():
    return BattleModifiers()
