from __future__ import absolute_import
from enum import Enum
from items.vehicle_mechanics_types import VehicleMechanic, VehicleMechanicKeys, ALL_VEHICLE_MECHANIC_KEYS
VEHICLE_MECHANIC_DYN_COMPONENT_NAMES = {(VehicleMechanic.ACCURACY_STACKS): b'accuracyStacksController', 
   (VehicleMechanic.AUTO_SHOOT_GUN): b'autoShootGunController', 
   (VehicleMechanic.AUTORELOADER_SURGE): b'autoreloaderSurgeController', 
   (VehicleMechanic.AUXILIARY_ROCKET_LAUNCHER): b'auxiliaryRocketLauncherComponent', 
   (VehicleMechanic.BATTLE_FURY): b'battleFuryController', 
   (VehicleMechanic.BUSTLE_FEED): b'bustleFeedController', 
   (VehicleMechanic.CHARGE_SHOT): b'chargeShotComponent', 
   (VehicleMechanic.CHARGEABLE_BURST): b'chargeableBurstComponent', 
   (VehicleMechanic.CONCENTRATION_MODE): b'concentrationModeComponent', 
   (VehicleMechanic.CREST_MOVING): b'CrestMovingController', 
   (VehicleMechanic.DUAL_ACCURACY): b'dualAccuracy', 
   (VehicleMechanic.EXTRA_SHOT_CLIP): b'extraShotClipComponent', 
   (VehicleMechanic.HEATING_ZONES_GUN): b'heatingZonesGunComponent', 
   (VehicleMechanic.IMPROVED_RAMMING): b'improvedRammingController', 
   (VehicleMechanic.LOW_CHARGE_SHOT): b'lowChargeShotController', 
   (VehicleMechanic.OVERHEAT_GUN): b'overheatGunComponent', 
   (VehicleMechanic.OVERHEAT_STACKS): b'overheatStacksController', 
   (VehicleMechanic.PILLBOX_SIEGE_MODE): b'pillboxSiegeComponent', 
   (VehicleMechanic.POWER_MODE): b'powerModeController', 
   (VehicleMechanic.PROPELLANT_GUN): b'propellantGunController', 
   (VehicleMechanic.RECHARGEABLE_NITRO): b'rechargeableNitroController', 
   (VehicleMechanic.ROCKET_ACCELERATION): b'rocketAccelerationController', 
   (VehicleMechanic.SHELL_CALIBRATION): b'ShellCalibrationController', 
   (VehicleMechanic.SHELL_PARAMS_SWITCHER): b'shellParamsSwitcherController', 
   (VehicleMechanic.SIGHT_POINTER): b'sightPointerComponent', 
   (VehicleMechanic.SPEC_BOOST_MODE): b'specBoostModeComponent', 
   (VehicleMechanic.STAGED_JET_BOOSTERS): b'stagedJetBoostersController', 
   (VehicleMechanic.STANCE_DANCE): b'stanceDanceController', 
   (VehicleMechanic.STATIONARY_RELOAD): b'stationaryReloadController', 
   (VehicleMechanic.SUPPORT_WEAPON): b'supportWeaponComponent', 
   (VehicleMechanic.TARGET_DESIGNATOR): b'targetDesignatorController', 
   (VehicleMechanic.TEMPERATURE_GUN): b'temperatureGunController', 
   (VehicleMechanic.TWIN_GUN): b'twinGunController', 
   (VehicleMechanic.WHEELED_DASH): b'wheeledDashController'}
TRACKABLE_VEHICLE_MECHANICS = frozenset(m for m in ALL_VEHICLE_MECHANIC_KEYS if m.mechanic in VEHICLE_MECHANIC_DYN_COMPONENT_NAMES)
VEHICLE_MECHANIC_TAGS = {(VehicleMechanic.ROCKET_ACCELERATION): b'rocketAcceleration', 
   (VehicleMechanic.DUAL_ACCURACY): b'dualAccuracy', 
   (VehicleMechanic.AUTO_SHOOT_GUN): b'autoShoot', 
   (VehicleMechanic.TWIN_GUN): b'twinGun'}

class VehicleMechanicCommand(Enum):
    PREPARING = b'preparing'
    CANCELLED = b'cancelled'
    ACTIVATE = b'activate'
    ALTERNATIVE_ACTIVATE = b'altActivate'
    DEACTIVATE = b'deactivate'
    SWITCH = b'switch'
    MANUAL_RELOAD = b'manual_reload'


VEHICLE_MECHANIC_USED_COMMANDS = {(VehicleMechanicKeys.AUTORELOADER_SURGE): (
                                            VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.AUXILIARY_ROCKET_LAUNCHER): (
                                                   VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.BUSTLE_FEED): (
                                     VehicleMechanicCommand.SWITCH,), 
   (VehicleMechanicKeys.CHARGE_SHOT): (
                                     VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.COMBAT_THROTTLE): (
                                         VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.CONCENTRATION_MODE): (
                                            VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.PILLBOX_SIEGE_MODE): (
                                            VehicleMechanicCommand.PREPARING, VehicleMechanicCommand.CANCELLED,
                                            VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.ALTERNATIVE_ACTIVATE), 
   (VehicleMechanicKeys.PROPELLANT_GUN): (
                                        VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.RECHARGEABLE_NITRO): (
                                            VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.DEACTIVATE), 
   (VehicleMechanicKeys.SIGHT_POINTER): (
                                       VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.DEACTIVATE), 
   (VehicleMechanicKeys.SHELL_PARAMS_SWITCHER): (
                                               VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.STAGED_JET_BOOSTERS): (
                                             VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.STANCE_DANCE): (
                                      VehicleMechanicCommand.ACTIVATE, VehicleMechanicCommand.SWITCH), 
   (VehicleMechanicKeys.STATIONARY_RELOAD): (
                                           VehicleMechanicCommand.MANUAL_RELOAD,), 
   (VehicleMechanicKeys.SUPPORT_WEAPON): (
                                        VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.TARGET_DESIGNATOR): (
                                           VehicleMechanicCommand.ACTIVATE,), 
   (VehicleMechanicKeys.WHEELED_DASH): (
                                      VehicleMechanicCommand.ACTIVATE,)}
