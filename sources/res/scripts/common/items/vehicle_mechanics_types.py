from __future__ import absolute_import
import typing
from future.utils import viewitems
from enum import Enum
from items import _xml
if typing.TYPE_CHECKING:
    from items.components.shared_components import MechanicsParams

class VehicleMechanic(Enum):
    ACCURACY_STACKS = b'accuracyStacks'
    AUTO_LOADER_GUN = b'autoLoaderGun'
    AUTO_LOADER_GUN_BOOST = b'autoLoaderGunBoost'
    AUTORELOADER_SURGE = b'autoreloaderSurge'
    AUTO_SHOOT_GUN = b'autoShootGun'
    AUXILIARY_ROCKET_LAUNCHER = b'auxiliaryRocketLauncher'
    BATTLE_FURY = b'battleFury'
    BUSTLE_FEED = b'bustleFeed'
    CHARGEABLE_BURST = b'chargeableBurst'
    CHARGE_SHOT = b'chargeShot'
    CONCENTRATION_MODE = b'concentrationMode'
    CREST_MOVING = b'crestMoving'
    DAMAGE_MUTABLE = b'damageMutable'
    DUAL_ACCURACY = b'dualAccuracy'
    DUAL_GUN = b'dualGun'
    EXTRA_SHOT_CLIP = b'extraShotClip'
    HEATING_ZONES_GUN = b'heatingZonesGun'
    HYDRAULIC_CHASSIS = b'hydraulicChassis'
    HYDRAULIC_WHEELED_CHASSIS = b'hydraulicWheeledChassis'
    IMPROVED_RAMMING = b'improvedRamming'
    LOW_CHARGE_SHOT = b'lowChargeShot'
    MAGAZINE_GUN = b'magazineGun'
    OVERHEAT_GUN = b'overheatGun'
    OVERHEAT_STACKS = b'overheatStacks'
    PILLBOX_SIEGE_MODE = b'pillboxSiegeMode'
    POWER_MODE = b'powerMode'
    PROPELLANT_GUN = b'propellantAfterburnerGun'
    RECHARGEABLE_NITRO = b'rechargeableNitro'
    ROCKET_ACCELERATION = b'rocketAcceleration'
    SHELL_PARAMS_SWITCHER = b'shellParamsSwitcher'
    SHELL_CALIBRATION = b'shellCalibration'
    SIEGE_MODE = b'siegeMode'
    SIGHT_POINTER = b'sightPointer'
    SPEC_BOOST_MODE = b'specBoostMode'
    STAGED_JET_BOOSTERS = b'stagedJetBoosters'
    STANCE_DANCE = b'stanceDance'
    STATIONARY_RELOAD = b'stationaryReload'
    STUN = b'stun'
    SUPPORT_WEAPON = b'supportWeapon'
    TARGET_DESIGNATOR = b'targetDesignator'
    TEMPERATURE_GUN = b'temperatureGun'
    TRACK_WITHIN_TRACK = b'trackWithinTrack'
    TURBOSHAFT_ENGINE = b'turboshaftEngine'
    TWIN_GUN = b'twinGun'
    WHEELED_DASH = b'wheeledDash'

    @classmethod
    def find(cls, value):
        return cls._value2member_map_.get(value)


VEHICLE_MECHANIC_VALUES = frozenset(m.value for m in VehicleMechanic)

class VehicleMechanicVariant(object):

    @classmethod
    def fromString(cls, value):
        if value:
            return cls(value)
        else:
            return


class SpecBoostModeMechanicVariant(VehicleMechanicVariant, Enum):
    COMBAT_THROTTLE = b'combatThrottle'


class VehicleMechanicKey(typing.NamedTuple(b'VehicleMechanicKey', (
 (
  b'mechanic', VehicleMechanic), (b'mechanicVariant', VehicleMechanicVariant)))):
    __slots__ = ()

    def __new__(cls, mechanic, mechanicVariant=None):
        return super(VehicleMechanicKey, cls).__new__(cls, mechanic, mechanicVariant)

    @property
    def uniqueName(self):
        if self.mechanicVariant is not None:
            return self.mechanicVariant.value
        else:
            return self.mechanic.value


class VehicleMechanicKeys(object):
    ACCURACY_STACKS = VehicleMechanicKey(VehicleMechanic.ACCURACY_STACKS)
    AUTO_LOADER_GUN = VehicleMechanicKey(VehicleMechanic.AUTO_LOADER_GUN)
    AUTO_LOADER_GUN_BOOST = VehicleMechanicKey(VehicleMechanic.AUTO_LOADER_GUN_BOOST)
    AUTORELOADER_SURGE = VehicleMechanicKey(VehicleMechanic.AUTORELOADER_SURGE)
    AUTO_SHOOT_GUN = VehicleMechanicKey(VehicleMechanic.AUTO_SHOOT_GUN)
    AUXILIARY_ROCKET_LAUNCHER = VehicleMechanicKey(VehicleMechanic.AUXILIARY_ROCKET_LAUNCHER)
    BATTLE_FURY = VehicleMechanicKey(VehicleMechanic.BATTLE_FURY)
    BUSTLE_FEED = VehicleMechanicKey(VehicleMechanic.BUSTLE_FEED)
    CHARGEABLE_BURST = VehicleMechanicKey(VehicleMechanic.CHARGEABLE_BURST)
    CHARGE_SHOT = VehicleMechanicKey(VehicleMechanic.CHARGE_SHOT)
    CONCENTRATION_MODE = VehicleMechanicKey(VehicleMechanic.CONCENTRATION_MODE)
    CREST_MOVING = VehicleMechanicKey(VehicleMechanic.CREST_MOVING)
    DAMAGE_MUTABLE = VehicleMechanicKey(VehicleMechanic.DAMAGE_MUTABLE)
    DUAL_ACCURACY = VehicleMechanicKey(VehicleMechanic.DUAL_ACCURACY)
    DUAL_GUN = VehicleMechanicKey(VehicleMechanic.DUAL_GUN)
    EXTRA_SHOT_CLIP = VehicleMechanicKey(VehicleMechanic.EXTRA_SHOT_CLIP)
    HEATING_ZONES_GUN = VehicleMechanicKey(VehicleMechanic.HEATING_ZONES_GUN)
    HYDRAULIC_CHASSIS = VehicleMechanicKey(VehicleMechanic.HYDRAULIC_CHASSIS)
    HYDRAULIC_WHEELED_CHASSIS = VehicleMechanicKey(VehicleMechanic.HYDRAULIC_WHEELED_CHASSIS)
    IMPROVED_RAMMING = VehicleMechanicKey(VehicleMechanic.IMPROVED_RAMMING)
    LOW_CHARGE_SHOT = VehicleMechanicKey(VehicleMechanic.LOW_CHARGE_SHOT)
    MAGAZINE_GUN = VehicleMechanicKey(VehicleMechanic.MAGAZINE_GUN)
    OVERHEAT_GUN = VehicleMechanicKey(VehicleMechanic.OVERHEAT_GUN)
    OVERHEAT_STACKS = VehicleMechanicKey(VehicleMechanic.OVERHEAT_STACKS)
    PILLBOX_SIEGE_MODE = VehicleMechanicKey(VehicleMechanic.PILLBOX_SIEGE_MODE)
    POWER_MODE = VehicleMechanicKey(VehicleMechanic.POWER_MODE)
    PROPELLANT_GUN = VehicleMechanicKey(VehicleMechanic.PROPELLANT_GUN)
    RECHARGEABLE_NITRO = VehicleMechanicKey(VehicleMechanic.RECHARGEABLE_NITRO)
    ROCKET_ACCELERATION = VehicleMechanicKey(VehicleMechanic.ROCKET_ACCELERATION)
    SHELL_PARAMS_SWITCHER = VehicleMechanicKey(VehicleMechanic.SHELL_PARAMS_SWITCHER)
    SHELL_CALIBRATION = VehicleMechanicKey(VehicleMechanic.SHELL_CALIBRATION)
    SIGHT_POINTER = VehicleMechanicKey(VehicleMechanic.SIGHT_POINTER)
    SIEGE_MODE = VehicleMechanicKey(VehicleMechanic.SIEGE_MODE)
    STAGED_JET_BOOSTERS = VehicleMechanicKey(VehicleMechanic.STAGED_JET_BOOSTERS)
    STANCE_DANCE = VehicleMechanicKey(VehicleMechanic.STANCE_DANCE)
    STATIONARY_RELOAD = VehicleMechanicKey(VehicleMechanic.STATIONARY_RELOAD)
    STUN = VehicleMechanicKey(VehicleMechanic.STUN)
    SUPPORT_WEAPON = VehicleMechanicKey(VehicleMechanic.SUPPORT_WEAPON)
    TARGET_DESIGNATOR = VehicleMechanicKey(VehicleMechanic.TARGET_DESIGNATOR)
    TEMPERATURE_GUN = VehicleMechanicKey(VehicleMechanic.TEMPERATURE_GUN)
    TRACK_WITHIN_TRACK = VehicleMechanicKey(VehicleMechanic.TRACK_WITHIN_TRACK)
    TURBOSHAFT_ENGINE = VehicleMechanicKey(VehicleMechanic.TURBOSHAFT_ENGINE)
    TWIN_GUN = VehicleMechanicKey(VehicleMechanic.TWIN_GUN)
    WHEELED_DASH = VehicleMechanicKey(VehicleMechanic.WHEELED_DASH)
    COMBAT_THROTTLE = VehicleMechanicKey(VehicleMechanic.SPEC_BOOST_MODE, SpecBoostModeMechanicVariant.COMBAT_THROTTLE)


ALL_VEHICLE_MECHANIC_KEYS = tuple(v for v in vars(VehicleMechanicKeys).values() if isinstance(v, VehicleMechanicKey))
MECHANIC_KEY_BY_NAME = {k.uniqueName: k for k in ALL_VEHICLE_MECHANIC_KEYS}
_MECHANIC_VARIANT_TYPES_BY_MECHANIC = {(VehicleMechanic.SPEC_BOOST_MODE): SpecBoostModeMechanicVariant}
_MECHANIC_VARIANT_VALUES_BY_MECHANIC = {mechanic: frozenset(variant.value for variant in variantType) for mechanic, variantType in viewitems(_MECHANIC_VARIANT_TYPES_BY_MECHANIC)}

def getVehicleMechanicKey(mechanic, mechanicParams):
    variant = getattr(mechanicParams, b'mechanicVariant', None)
    uniqueName = variant if variant is not None else mechanic.value
    return MECHANIC_KEY_BY_NAME[uniqueName]


def readMechanicVariant(xmlCtx, section, mechanic):
    allowedVariants = _MECHANIC_VARIANT_VALUES_BY_MECHANIC.get(VehicleMechanic.find(mechanic))
    if not allowedVariants:
        _xml.raiseWrongXml(xmlCtx, b'mechanicVariant', (b'[{}] Section <mechanicVariant> is not supported for this mechanic').format(mechanic))
    mechanicVariant = _xml.readStringOrEmpty(xmlCtx, section, b'mechanicVariant')
    if mechanicVariant not in allowedVariants:
        _xml.raiseWrongXml(xmlCtx, b'mechanicVariant', (b'[{}] Section <mechanicVariant> with value {} is invalid!').format(mechanic, mechanicVariant))
    return mechanicVariant
