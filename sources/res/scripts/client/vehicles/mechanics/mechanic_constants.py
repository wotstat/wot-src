from __future__ import absolute_import
from enum import Enum
from future.utils import viewitems
from items.components import shared_components

class VehicleMechanic(Enum):
    MAGAZINE_GUN = b'magazineGun'
    AUTO_LOADER_GUN = b'autoLoaderGun'
    AUTO_LOADER_GUN_BOOST = b'autoLoaderGunBoost'
    DAMAGE_MUTABLE = b'damageMutable'
    DUAL_GUN = b'dualGun'
    HYDRAULIC_CHASSIS = b'hydraulicChassis'
    TRACK_WITHIN_TRACK = b'trackWithinTrack'
    SIEGE_MODE = b'siegeMode'
    STUN = b'stun'
    HYDRAULIC_WHEELED_CHASSIS = b'hydraulicWheeledChassis'
    TURBOSHAFT_ENGINE = b'turboshaftEngine'
    ROCKET_ACCELERATION = b'rocketAcceleration'
    DUAL_ACCURACY = b'dualAccuracy'
    AUTO_SHOOT_GUN = b'autoShootGun'
    TWIN_GUN = b'twinGun'
    IMPROVED_RAMMING = b'improvedRamming'
    CONCENTRATION_MODE = b'concentrationMode'
    BATTLE_FURY = b'battleFury'
    EXTRA_SHOT_CLIP = b'extraShotClip'
    POWER_MODE = b'powerMode'
    ACCURACY_STACKS = b'accuracyStacks'
    SUPPORT_WEAPON = b'supportWeapon'
    PILLBOX_SIEGE_MODE = b'pillboxSiegeMode'
    CHARGEABLE_BURST = b'chargeableBurst'
    RECHARGEABLE_NITRO = b'rechargeableNitro'
    CHARGE_SHOT = b'chargeShot'
    OVERHEAT_STACKS = b'overheatStacks'
    TARGET_DESIGNATOR = b'targetDesignator'
    STANCE_DANCE = b'stanceDance'
    STATIONARY_RELOAD = b'stationaryReload'
    TEMPERATURE_GUN = b'temperatureGun'
    OVERHEAT_GUN = b'overheatGun'
    HEATING_ZONES_GUN = b'heatingZonesGun'
    LOW_CHARGE_SHOT = b'lowChargeShot'
    STAGED_JET_BOOSTERS = b'stagedJetBoosters'
    PROPELLANT_GUN = b'propellantAfterburnerGun'
    WHEELED_DASH = b'wheeledDash'


VEHICLE_MECHANIC_DYN_COMPONENT_NAMES = {(VehicleMechanic.IMPROVED_RAMMING): b'improvedRammingController', 
   (VehicleMechanic.ROCKET_ACCELERATION): b'rocketAccelerationController', 
   (VehicleMechanic.DUAL_ACCURACY): b'dualAccuracy', 
   (VehicleMechanic.AUTO_SHOOT_GUN): b'autoShootGunController', 
   (VehicleMechanic.TWIN_GUN): b'twinGunController', 
   (VehicleMechanic.CONCENTRATION_MODE): b'concentrationModeComponent', 
   (VehicleMechanic.BATTLE_FURY): b'battleFuryController', 
   (VehicleMechanic.EXTRA_SHOT_CLIP): b'extraShotClipComponent', 
   (VehicleMechanic.POWER_MODE): b'powerModeController', 
   (VehicleMechanic.ACCURACY_STACKS): b'accuracyStacksController', 
   (VehicleMechanic.SUPPORT_WEAPON): b'supportWeaponComponent', 
   (VehicleMechanic.PILLBOX_SIEGE_MODE): b'pillboxSiegeComponent', 
   (VehicleMechanic.CHARGEABLE_BURST): b'chargeableBurstComponent', 
   (VehicleMechanic.RECHARGEABLE_NITRO): b'rechargeableNitroController', 
   (VehicleMechanic.CHARGE_SHOT): b'chargeShotComponent', 
   (VehicleMechanic.OVERHEAT_STACKS): b'overheatStacksController', 
   (VehicleMechanic.TARGET_DESIGNATOR): b'targetDesignatorController', 
   (VehicleMechanic.STANCE_DANCE): b'stanceDanceController', 
   (VehicleMechanic.STATIONARY_RELOAD): b'stationaryReloadController', 
   (VehicleMechanic.TEMPERATURE_GUN): b'temperatureGunController', 
   (VehicleMechanic.OVERHEAT_GUN): b'overheatGunComponent', 
   (VehicleMechanic.HEATING_ZONES_GUN): b'heatingZonesGunComponent', 
   (VehicleMechanic.LOW_CHARGE_SHOT): b'lowChargeShotController', 
   (VehicleMechanic.STAGED_JET_BOOSTERS): b'stagedJetBoostersController', 
   (VehicleMechanic.PROPELLANT_GUN): b'propellantGunController', 
   (VehicleMechanic.WHEELED_DASH): b'wheeledDashController'}
TRACKABLE_VEHICLE_MECHANICS = set(VEHICLE_MECHANIC_DYN_COMPONENT_NAMES)
VEHICLE_MECHANIC_TAGS = {(VehicleMechanic.ROCKET_ACCELERATION): b'rocketAcceleration', 
   (VehicleMechanic.DUAL_ACCURACY): b'dualAccuracy', 
   (VehicleMechanic.AUTO_SHOOT_GUN): b'autoShoot', 
   (VehicleMechanic.TWIN_GUN): b'twinGun'}
VEHICLE_MECHANIC_TO_PARAMS = {(VehicleMechanic.IMPROVED_RAMMING): (shared_components.ImprovedRammingParams.MECHANICS_NAME), 
   (VehicleMechanic.CONCENTRATION_MODE): (shared_components.ConcentrationModeParams.MECHANICS_NAME), 
   (VehicleMechanic.BATTLE_FURY): (shared_components.BattleFuryParams.MECHANICS_NAME), 
   (VehicleMechanic.EXTRA_SHOT_CLIP): (shared_components.ExtraShotClipParams.MECHANICS_NAME), 
   (VehicleMechanic.POWER_MODE): (shared_components.PowerModeParams.MECHANICS_NAME), 
   (VehicleMechanic.ACCURACY_STACKS): (shared_components.AccuracyStacksParams.MECHANICS_NAME), 
   (VehicleMechanic.SUPPORT_WEAPON): (shared_components.SupportWeaponParams.MECHANICS_NAME), 
   (VehicleMechanic.PILLBOX_SIEGE_MODE): (shared_components.PillboxSiegeModeParams.MECHANICS_NAME), 
   (VehicleMechanic.CHARGEABLE_BURST): (shared_components.ChargeableBurstParams.MECHANICS_NAME), 
   (VehicleMechanic.RECHARGEABLE_NITRO): (shared_components.RechargeableNitroParams.MECHANICS_NAME), 
   (VehicleMechanic.CHARGE_SHOT): (shared_components.ChargeShotParams.MECHANICS_NAME), 
   (VehicleMechanic.OVERHEAT_STACKS): (shared_components.OverheatStacksParams.MECHANICS_NAME), 
   (VehicleMechanic.TARGET_DESIGNATOR): (shared_components.TargetDesignatorParams.MECHANICS_NAME), 
   (VehicleMechanic.STANCE_DANCE): (shared_components.StanceDanceParams.MECHANICS_NAME), 
   (VehicleMechanic.STATIONARY_RELOAD): (shared_components.StationaryReloadParams.MECHANICS_NAME), 
   (VehicleMechanic.TEMPERATURE_GUN): (shared_components.TemperatureGunParams.MECHANICS_NAME), 
   (VehicleMechanic.OVERHEAT_GUN): (shared_components.OverheatGunParams.MECHANICS_NAME), 
   (VehicleMechanic.HEATING_ZONES_GUN): (shared_components.HeatingZonesGunParams.MECHANICS_NAME), 
   (VehicleMechanic.LOW_CHARGE_SHOT): (shared_components.LowChargeShotParams.MECHANICS_NAME), 
   (VehicleMechanic.STAGED_JET_BOOSTERS): (shared_components.StagedJetBoostersParams.MECHANICS_NAME), 
   (VehicleMechanic.PROPELLANT_GUN): (shared_components.PropellantGunParams.MECHANICS_NAME), 
   (VehicleMechanic.WHEELED_DASH): (shared_components.WheeledDashParams.MECHANICS_NAME)}
VEHICLE_PARAMS_TO_MECHANIC = {v: k for k, v in viewitems(VEHICLE_MECHANIC_TO_PARAMS)}
TRACKABLE_VEHICLE_DESCR_MECHANICS = set()
TRACKABLE_VEHICLE_DESCR_MECHANICS |= set(VEHICLE_MECHANIC_TAGS)
TRACKABLE_VEHICLE_DESCR_MECHANICS |= set(VEHICLE_MECHANIC_TO_PARAMS)

class VehicleMechanicCommand(Enum):
    PREPARING = b'preparing'
    CANCELLED = b'cancelled'
    ACTIVATE = b'activate'
    ALTERNATIVE_ACTIVATE = b'altActivate'
    DEACTIVATE = b'deactivate'
    SWITCH = b'switch'
    MANUAL_RELOAD = b'manual_reload'


VEHICLE_MECHANIC_USED_COMMANDS = {(VehicleMechanic.CONCENTRATION_MODE): (
                                        VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanic.SUPPORT_WEAPON): (
                                    VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanic.PILLBOX_SIEGE_MODE): (
                                        VehicleMechanicCommand.PREPARING, VehicleMechanicCommand.CANCELLED,
                                        VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.ALTERNATIVE_ACTIVATE), 
   (VehicleMechanic.RECHARGEABLE_NITRO): (
                                        VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.DEACTIVATE), 
   (VehicleMechanic.CHARGE_SHOT): (
                                 VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanic.TARGET_DESIGNATOR): (
                                       VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanic.STANCE_DANCE): (
                                  VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.SWITCH), 
   (VehicleMechanic.STATIONARY_RELOAD): (
                                       VehicleMechanicCommand.MANUAL_RELOAD,), 
   (VehicleMechanic.STAGED_JET_BOOSTERS): (
                                         VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanic.PROPELLANT_GUN): (
                                    VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanic.WHEELED_DASH): (
                                  VehicleMechanicCommand.ACTIVATE,)}
