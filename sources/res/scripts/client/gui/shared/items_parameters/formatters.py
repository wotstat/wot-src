from __future__ import absolute_import
from builtins import zip
from collections import namedtuple
from future.utils import iteritems, lzip
from itertools import chain
from past.builtins import unicode
from typing import TYPE_CHECKING
from constants import BonusTypes, DAMAGE_INTERPOLATION_DIST_LAST
from debug_utils import LOG_ERROR
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.gui_items import KPI, kpiFormatValue, kpiFormatNoSignValue
from gui.shared.items_parameters import RELATIVE_PARAMS
from gui.shared.items_parameters.comparator import PARAM_STATE
from gui.shared.items_parameters.params_helper import hasGroupPenalties, getCommonParam, isValidEmptyValue, PARAMS_GROUPS
from gui.shared.items_parameters.shell_params import CriticalHitChanceType
from gui.shared.utils import AUTO_RELOAD_PROP_NAME, MAX_STEERING_LOCK_ANGLE, WHEELED_SWITCH_ON_TIME, WHEELED_SWITCH_OFF_TIME, WHEELED_SWITCH_TIME, WHEELED_SPEED_MODE_SPEED, DUAL_GUN_CHARGE_TIME, DUAL_GUN_RATE_TIME, TURBOSHAFT_SPEED_MODE_SPEED, TURBOSHAFT_ENGINE_POWER, TURBOSHAFT_INVISIBILITY_STILL_FACTOR, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_SWITCH_TIME, CHASSIS_REPAIR_TIME, CHASSIS_REPAIR_TIME_YOH, ROCKET_ACCELERATION_ENGINE_POWER, ROCKET_ACCELERATION_SPEED_LIMITS, ROCKET_ACCELERATION_REUSE_AND_DURATION, DUAL_ACCURACY_COOLING_DELAY, SHOT_DISPERSION_ANGLE, DISPERSION_RADIUS, BURST_FIRE_RATE, BURST_TIME_INTERVAL, BURST_SIZE, BURST_COUNT, AVG_DAMAGE_PER_SECOND, AUTO_SHOOT_CLIP_FIRE_RATE, CONTINUOUS_SHOTS_PER_MINUTE, CONTINUOUS_DAMAGE_PER_SECOND, TWIN_GUN_SWITCH_FIRE_MODE_TIME, TWIN_GUN_TOP_SPEED, TWIN_GUN_RELOAD_ONE_GUN_TIME, TWIN_GUN_RELOAD_TWO_GUN_TIME, TWIN_GUN_RELOAD_TIME, SHELL_RELOADING_TIME_PROP_NAME, SHELL_LOADING_TIME_PROP_NAME, RELOAD_TIME_PROP_NAME, TEMPERATURE_RELOAD_TIME, TEMPERATURE_AVG_DAMAGE_PER_MINUTE, NORMALIZATION_ANGLE, RICOCHET_ANGLE, PENETRATION_LOSS, CRITICAL_HIT_CHANCE
from helpers.i18n import makeString, isValidKey
from items import vehicles, artefacts, getTypeOfCompactDescr, ITEM_TYPES
from math_common import decimal_round, round_py2_style
from web_stubs import i18n
if TYPE_CHECKING:
    from typing import Optional, Tuple, Dict
    from gui.shared.items_parameters.comparator import _ParameterInfo
ChangeCondition = namedtuple(b'ChangeCondition', (b'predicate', b'alternativeParameter'))
MEASURE_UNITS = {b'aimingTime': (MENU.TANK_PARAMS_S), 
   b'areaRadius': (MENU.TANK_PARAMS_M), 
   b'areaSquare': (MENU.TANK_PARAMS_SQM), 
   b'armor': (MENU.TANK_PARAMS_FACEFRONTBOARDINMM), 
   b'artDelayRange': (MENU.TANK_PARAMS_S), 
   b'avgDamageList': (MENU.TANK_PARAMS_VAL), 
   b'maxAvgMutableDamageList': (MENU.TANK_PARAMS_VAL), 
   b'minAvgMutableDamageList': (MENU.TANK_PARAMS_VAL), 
   b'gunModuleAvgDamageList': (MENU.TANK_PARAMS_VAL), 
   b'avgPiercingPower': (MENU.TANK_PARAMS_MM), 
   b'bombDamage': (MENU.TANK_PARAMS_VAL), 
   b'bombsNumberRange': (MENU.TANK_PARAMS_CNT), 
   b'chassisRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'circularVisionRadius': (MENU.TANK_PARAMS_M), 
   b'clipFireRate': (MENU.TANK_PARAMS_CLIPSEC), 
   AUTO_SHOOT_CLIP_FIRE_RATE: (MENU.TANK_PARAMS_AUTOSHOOTCLIPSEC), 
   BURST_FIRE_RATE: (MENU.TANK_PARAMS_BURSTSEC), 
   b'turboshaftBurstFireRate': (MENU.TANK_PARAMS_BURSTSEC), 
   BURST_TIME_INTERVAL: (MENU.TANK_PARAMS_S), 
   BURST_COUNT: (MENU.TANK_PARAMS_CNT), 
   BURST_SIZE: (MENU.TANK_PARAMS_CNT), 
   b'avgDamage': (MENU.TANK_PARAMS_VAL), 
   b'avgMutableDamage': (MENU.TANK_PARAMS_VAL), 
   b'avgDamagePerMinute': (MENU.TANK_PARAMS_VPM), 
   TEMPERATURE_AVG_DAMAGE_PER_MINUTE: (MENU.TANK_PARAMS_VPM), 
   AVG_DAMAGE_PER_SECOND: (MENU.TANK_PARAMS_VPS), 
   CONTINUOUS_DAMAGE_PER_SECOND: (MENU.TANK_PARAMS_VPS), 
   b'fireStartingChance': (MENU.TANK_PARAMS_PERCENT), 
   b'maxHealth': (MENU.TANK_PARAMS_VAL), 
   b'flyDelayRange': (MENU.TANK_PARAMS_S), 
   b'enginePower': (MENU.TANK_PARAMS_P), 
   TURBOSHAFT_ENGINE_POWER: (MENU.TANK_PARAMS_P), 
   ROCKET_ACCELERATION_ENGINE_POWER: (MENU.TANK_PARAMS_P), 
   ROCKET_ACCELERATION_REUSE_AND_DURATION: (MENU.TANK_PARAMS_QPT), 
   ROCKET_ACCELERATION_SPEED_LIMITS: (MENU.TANK_PARAMS_MPH), 
   b'enginePowerPerTon': (MENU.TANK_PARAMS_PT), 
   b'explosionRadius': (MENU.TANK_PARAMS_M), 
   b'gunYawLimits': (MENU.TANK_PARAMS_GRADS), 
   b'hullArmor': (MENU.TANK_PARAMS_FACEFRONTBOARDINMM), 
   b'piercingPower': (MENU.TANK_PARAMS_MM), 
   b'maxPiercingPower': (MENU.TANK_PARAMS_MM), 
   b'minPiercingPower': (MENU.TANK_PARAMS_MM), 
   b'pitchLimits': (MENU.TANK_PARAMS_GRADS), 
   b'radioDistance': (MENU.TANK_PARAMS_M), 
   b'radarRadius': (MENU.TANK_PARAMS_M), 
   b'radarCooldown': (MENU.TANK_PARAMS_S), 
   b'maxHullHealth': (MENU.TANK_PARAMS_VAL), 
   b'forwardMaxSpeed': (MENU.TANK_PARAMS_MPH), 
   b'reloadMagazineTime': (MENU.TANK_PARAMS_S), 
   RELOAD_TIME_PROP_NAME: (MENU.TANK_PARAMS_SPM), 
   TEMPERATURE_RELOAD_TIME: (MENU.TANK_PARAMS_SPM), 
   CONTINUOUS_SHOTS_PER_MINUTE: (MENU.TANK_PARAMS_SPM), 
   b'reloadTimeSecs': (MENU.TANK_PARAMS_S), 
   b'rotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'chassisModuleRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'turretModuleRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   SHELL_RELOADING_TIME_PROP_NAME: (MENU.TANK_PARAMS_S), 
   SHELL_LOADING_TIME_PROP_NAME: (MENU.TANK_PARAMS_S), 
   SHOT_DISPERSION_ANGLE: (MENU.TANK_PARAMS_M), 
   b'shotsNumberRange': (MENU.TANK_PARAMS_CNT), 
   b'shellsCount': (MENU.TANK_PARAMS_CNT), 
   b'speedLimits': (MENU.TANK_PARAMS_MPH), 
   b'turretArmor': (MENU.TANK_PARAMS_FACEFRONTBOARDINMM), 
   b'turretYawLimits': (MENU.TANK_PARAMS_GRADS), 
   b'vehicleWeight': (MENU.TANK_PARAMS_T), 
   b'weight': (MENU.TANK_PARAMS_KG), 
   b'hullWeight': (MENU.TANK_PARAMS_KG), 
   b'hullAndChassisWeight': (MENU.TANK_PARAMS_KG), 
   b'caliber': (MENU.TANK_PARAMS_MM), 
   b'damage': (MENU.TANK_PARAMS_VAL), 
   b'maxMutableDamage': (MENU.TANK_PARAMS_VAL), 
   b'minMutableDamage': (MENU.TANK_PARAMS_VAL), 
   b'turretRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'invisibilityStillFactor': (MENU.TANK_PARAMS_PERCENT), 
   b'invisibilityMovingFactor': (MENU.TANK_PARAMS_PERCENT), 
   TURBOSHAFT_INVISIBILITY_STILL_FACTOR: (MENU.TANK_PARAMS_PERCENT), 
   TURBOSHAFT_INVISIBILITY_MOVING_FACTOR: (MENU.TANK_PARAMS_PERCENT), 
   b'maxShotDistance': (MENU.TANK_PARAMS_M), 
   b'switchOnTime': (MENU.TANK_PARAMS_S), 
   b'switchOffTime': (MENU.TANK_PARAMS_S), 
   b'switchTime': (MENU.TANK_PARAMS_S), 
   TURBOSHAFT_SWITCH_TIME: (MENU.TANK_PARAMS_S), 
   b'stunMaxDuration': (MENU.TANK_PARAMS_S), 
   b'stunMinDuration': (MENU.TANK_PARAMS_S), 
   b'stunDurationList': (MENU.TANK_PARAMS_S), 
   b'stunMaxDurationList': (MENU.TANK_PARAMS_S), 
   b'stunMinDurationList': (MENU.TANK_PARAMS_S), 
   b'cooldownSeconds': (MENU.TANK_PARAMS_S), 
   AUTO_RELOAD_PROP_NAME: (MENU.TANK_PARAMS_S), 
   MAX_STEERING_LOCK_ANGLE: (MENU.TANK_PARAMS_GRADS), 
   WHEELED_SWITCH_ON_TIME: (MENU.TANK_PARAMS_S), 
   WHEELED_SWITCH_OFF_TIME: (MENU.TANK_PARAMS_S), 
   WHEELED_SWITCH_TIME: (MENU.TANK_PARAMS_S), 
   WHEELED_SPEED_MODE_SPEED: (MENU.TANK_PARAMS_MPH), 
   TURBOSHAFT_SPEED_MODE_SPEED: (MENU.TANK_PARAMS_MPH), 
   DUAL_GUN_CHARGE_TIME: (MENU.TANK_PARAMS_S), 
   DUAL_GUN_RATE_TIME: (MENU.TANK_PARAMS_S), 
   DUAL_ACCURACY_COOLING_DELAY: (MENU.TANK_PARAMS_S), 
   b'shotSpeed': (MENU.TANK_PARAMS_MPS), 
   CHASSIS_REPAIR_TIME: (MENU.TANK_PARAMS_S), 
   CHASSIS_REPAIR_TIME_YOH: (MENU.TANK_PARAMS_YOH_S_S), 
   b'commonDelay': (MENU.TANK_PARAMS_S), 
   b'duration': (MENU.TANK_PARAMS_S), 
   b'inactivationDelay': (MENU.TANK_PARAMS_S), 
   b'commonAreaRadius': (MENU.TANK_PARAMS_M), 
   b'crewRolesFactor': (MENU.TANK_PARAMS_PERCENT), 
   b'maxDamage': (MENU.TANK_PARAMS_VAL), 
   b'increaseHealth': (MENU.TANK_PARAMS_VAL), 
   b'artNotificationDelayFactor': (MENU.TANK_PARAMS_S), 
   b'vehicleOwnSpottingTime': (MENU.TANK_PARAMS_S), 
   b'damagedModulesDetectionTime': (MENU.TANK_PARAMS_S), 
   b'commanderLampDelay': (MENU.TANK_PARAMS_S), 
   TWIN_GUN_RELOAD_ONE_GUN_TIME: (MENU.TANK_PARAMS_S), 
   TWIN_GUN_RELOAD_TWO_GUN_TIME: (MENU.TANK_PARAMS_S), 
   TWIN_GUN_TOP_SPEED: (MENU.TANK_PARAMS_MPH), 
   TWIN_GUN_SWITCH_FIRE_MODE_TIME: (MENU.TANK_PARAMS_S), 
   TWIN_GUN_RELOAD_TIME: (MENU.TANK_PARAMS_S), 
   b'concentrationModeCooldown': (MENU.TANK_PARAMS_S), 
   b'concentrationModeDuration': (MENU.TANK_PARAMS_S), 
   b'extraShotClipReloadTime': (MENU.TANK_PARAMS_S), 
   b'powerModeThreshold': (MENU.TANK_PARAMS_S), 
   b'powerModeDuration': (MENU.TANK_PARAMS_S), 
   b'secondaryReloadTimeSecs': (MENU.TANK_PARAMS_S), 
   b'secondaryTotalBurstSize': (MENU.TANK_PARAMS_PERACTIVATION), 
   b'secondaryAvgDamage': (MENU.TANK_PARAMS_VAL), 
   b'secondaryAvgPiercingPower': (MENU.TANK_PARAMS_MM), 
   b'pillboxHorizontalRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'pillboxVerticalRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'pillboxSwitchOnTime': (MENU.TANK_PARAMS_S), 
   b'pillboxSwitchOffTime': (MENU.TANK_PARAMS_S), 
   b'chargeableBurstPenetrationCount': (MENU.TANK_PARAMS_QUANTITY), 
   b'chargeableBurstSize': (MENU.TANK_PARAMS_QUANTITY), 
   b'chargeableBurstReload': (MENU.TANK_PARAMS_S), 
   b'chargeableBurstDispersion': (MENU.TANK_PARAMS_M), 
   b'stationaryReloadSwitchOnTime': (MENU.TANK_PARAMS_S), 
   b'stationaryReloadSwitchOffTime': (MENU.TANK_PARAMS_S), 
   b'furyMaxReloadEffAvgDpm': (MENU.TANK_PARAMS_FACTOR), 
   b'furyReloadSpeedBonusPerEfficiencyLevel': (MENU.TANK_PARAMS_FACTOR), 
   b'furyReloadEfficiencyLevelDuration': (MENU.TANK_PARAMS_S), 
   b'accuracyDispersionCap': (MENU.TANK_PARAMS_FACTOR), 
   b'accuracyWhileMovingDispersionCap': (MENU.TANK_PARAMS_FACTOR), 
   b'accuracyDispersionPerLevel': (MENU.TANK_PARAMS_FACTOR), 
   b'accuracySpeedLimit': (MENU.TANK_PARAMS_MPH), 
   b'accuracyLevelGainTime': (MENU.TANK_PARAMS_S), 
   b'preheatDmgCap': (MENU.TANK_PARAMS_FACTOR), 
   b'preheatDispersionCap': (MENU.TANK_PARAMS_FACTOR), 
   b'preheatTimeToFull': (MENU.TANK_PARAMS_S), 
   b'preheatTimeToZero': (MENU.TANK_PARAMS_S), 
   b'preheatSpeedLimit': (MENU.TANK_PARAMS_MPH), 
   b'preheatTransitionDelay': (MENU.TANK_PARAMS_S), 
   b'enginePowerWithBoosters': (MENU.TANK_PARAMS_FACTOR), 
   b'topSpeedWithBoosters': (MENU.TANK_PARAMS_FACTOR), 
   b'reverseSpeedReductionWithBoosters': (MENU.TANK_PARAMS_FACTOR), 
   b'traverseSpeedReductionWithBoosters': (MENU.TANK_PARAMS_FACTOR), 
   b'boosterDuration': (MENU.TANK_PARAMS_S), 
   b'boosterCoolingTime': (MENU.TANK_PARAMS_S), 
   b'reactivationLimit': (MENU.TANK_PARAMS_FACTOR), 
   b'reactivationDelay': (MENU.TANK_PARAMS_S), 
   b'heatAvgDmgPerLvl': (MENU.TANK_PARAMS_FACTOR), 
   b'heatTimeToReachLevel': (MENU.TANK_PARAMS_S), 
   b'heatTimeBeforeOverheat': (MENU.TANK_PARAMS_S), 
   b'heatChargeOverheatDuration': (MENU.TANK_PARAMS_S), 
   b'coincidenceElectromechanicalSightDuration': (MENU.TANK_PARAMS_S), 
   b'switchEngineModeBothModes': (MENU.TANK_PARAMS_S), 
   b'ionAfterburnerDuration': (MENU.TANK_PARAMS_S), 
   b'designatorInitialCooldownS': (MENU.TANK_PARAMS_S), 
   b'designatorCooldownS': (MENU.TANK_PARAMS_S), 
   b'designatorMarkDurationS': (MENU.TANK_PARAMS_S), 
   b'designatorMarkedEnemiesAdditionalDamage': (MENU.TANK_PARAMS_FACTOR), 
   b'piercingHEShellsDistributionUpperBound': (MENU.TANK_PARAMS_PERCENT), 
   b'suspensionDamageReduction': (MENU.TANK_PARAMS_PERCENT), 
   b'hpRecover': (MENU.TANK_PARAMS_PERCENT), 
   b'coolingDelay': (MENU.TANK_PARAMS_S), 
   b'heatingPerShot': (MENU.TANK_PARAMS_FACTOR), 
   b'coolingTime': (MENU.TANK_PARAMS_S), 
   b'overheatDuration': (MENU.TANK_PARAMS_S), 
   b'timeToOverheat': (MENU.TANK_PARAMS_S), 
   NORMALIZATION_ANGLE: (MENU.TANK_PARAMS_GRADS), 
   RICOCHET_ANGLE: (MENU.TANK_PARAMS_GRADS), 
   PENETRATION_LOSS: (MENU.TANK_PARAMS_SHELLPENETRATIONLOSS), 
   b'propellantChargeLimit': (MENU.TANK_PARAMS_FACTOR), 
   b'propellantChargeSpendingAfterShot': (MENU.TANK_PARAMS_FACTOR), 
   b'propellantChargingPerSec': (MENU.TANK_PARAMS_PERCENT_PER_S), 
   b'propellantDischargingPerSec': (MENU.TANK_PARAMS_PERCENT_PER_S), 
   b'propellantOverchargeSwitchCooldown': (MENU.TANK_PARAMS_S), 
   b'propellantPreLimitDamageBonus': (MENU.TANK_PARAMS_FACTOR), 
   b'propellantPostLimitDamageSpike': (MENU.TANK_PARAMS_VAL), 
   b'propellantPostLimitDamageBonus': (MENU.TANK_PARAMS_FACTOR), 
   b'propellantPostLimitDispersion': (MENU.TANK_PARAMS_M), 
   b'propellantPostLimitAimingTime': (MENU.TANK_PARAMS_S), 
   b'shellParamsSwitchingTime': (MENU.TANK_PARAMS_S), 
   b'autoreloaderSurgeChargeTimeSlow': (MENU.TANK_PARAMS_S), 
   b'autoreloaderSurgeChargeTimeFast': (MENU.TANK_PARAMS_S), 
   b'autoreloaderSurgeBoostedReloadTime': (MENU.TANK_PARAMS_S), 
   b'sightPointerDeployTime': (MENU.TANK_PARAMS_S), 
   b'sightPointerReloadTime': (MENU.TANK_PARAMS_S), 
   b'sightPointerDuration': (MENU.TANK_PARAMS_S), 
   b'sightPointerRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'sightPointerSectorAngleStart': (MENU.TANK_PARAMS_GRADS), 
   b'sightPointerSectorAngleEnd': (MENU.TANK_PARAMS_GRADS), 
   b'sightPointerSelfSpottingTime': (MENU.TANK_PARAMS_S), 
   b'sightPointerViewRange': (MENU.TANK_PARAMS_M), 
   b'sightPointerConsealmentFoliage': (MENU.TANK_PARAMS_FACTOR), 
   b'sightPointerConsealmentMoving': (MENU.TANK_PARAMS_FACTOR)}
MEASURE_UNITS_NO_BRACKETS = {b'weight': (MENU.TANK_PARAMS_NO_BRACKETS_KG), 
   b'cooldownSeconds': (MENU.TANK_PARAMS_NO_BRACKETS_S), 
   b'reloadCooldownSeconds': (MENU.TANK_PARAMS_NO_BRACKETS_S), 
   b'caliber': (MENU.TANK_PARAMS_NO_BRACKETS_MM)}
KPI_FORMATTERS = {(KPI.Name.DAMAGED_MODULES_DETECTION_TIME): kpiFormatNoSignValue, 
   (KPI.Name.ART_NOTIFICATION_DELAY_FACTOR): kpiFormatNoSignValue}
COLORLESS_SCHEME = (
 text_styles.stats, text_styles.stats, text_styles.stats)
NO_BONUS_SIMPLIFIED_SCHEME = (text_styles.warning, text_styles.warning, text_styles.warning)
NO_BONUS_BASE_SCHEME = (text_styles.error, text_styles.stats, text_styles.stats)
SIMPLIFIED_SCHEME = (text_styles.critical, text_styles.warning, text_styles.statInfo)
BASE_SCHEME = (text_styles.error, text_styles.stats, text_styles.bonusAppliedText)
EXTRACTED_BONUS_SCHEME = (text_styles.error, text_styles.bonusAppliedText, text_styles.bonusAppliedText)
SITUATIONAL_SCHEME = (text_styles.critical, text_styles.warning, text_styles.bonusPreviewText)
VEHICLE_PARAMS = tuple(chain(*[PARAMS_GROUPS[param] for param in RELATIVE_PARAMS]))
ITEMS_PARAMS_LIST = {(ITEM_TYPES.vehicleRadio): (
                             b'radioDistance', b'weight'), 
   (ITEM_TYPES.vehicleChassis): (
                               b'rotationSpeed', b'weight', MAX_STEERING_LOCK_ANGLE, CHASSIS_REPAIR_TIME), 
   (ITEM_TYPES.vehicleEngine): (
                              b'enginePower', TURBOSHAFT_ENGINE_POWER, ROCKET_ACCELERATION_ENGINE_POWER, b'fireStartingChance', b'weight'), 
   (ITEM_TYPES.vehicleTurret): (
                              b'armor', b'rotationSpeed', b'circularVisionRadius', b'weight'), 
   (ITEM_TYPES.vehicle): VEHICLE_PARAMS, 
   (ITEM_TYPES.equipment): {(artefacts.RageArtillery): (
                                                      b'damage', b'piercingPower', b'caliber', b'shotsNumberRange',
                                                      b'areaRadius', b'artDelayRange'), 
                            (artefacts.RageBomber): (
                                                   b'bombDamage', b'piercingPower', b'bombsNumberRange', b'areaSquare', b'flyDelayRange'), 
                            (artefacts.AttackArtilleryFortEquipment): (
                                                                     b'maxDamage', b'areaRadius', b'duration', b'commonDelay'), 
                            (artefacts.FortConsumableInspire): (
                                                              b'crewRolesFactor', b'commonAreaRadius', b'inactivationDelay', b'duration'), 
                            (artefacts.ConsumableInspire): (
                                                          b'crewRolesFactor', b'commonAreaRadius', b'inactivationDelay', b'duration')}, 
   (ITEM_TYPES.shell): (
                      b'caliber', b'avgDamage', b'avgMutableDamage', AVG_DAMAGE_PER_SECOND, b'avgPiercingPower', b'shotSpeed',
                      b'explosionRadius', b'stunDurationList', NORMALIZATION_ANGLE, RICOCHET_ANGLE, CRITICAL_HIT_CHANCE,
                      PENETRATION_LOSS, b'screensArmorMultiplier'), 
   (ITEM_TYPES.optionalDevice): (
                               b'weight',), 
   (ITEM_TYPES.vehicleGun): (
                           b'caliber', b'avgDamageList', b'maxAvgDamageList', b'minAvgDamageList', CONTINUOUS_DAMAGE_PER_SECOND,
                           b'avgPiercingPower', b'shellsCount', b'reloadTimeSecs', b'shellReloadingTime', b'reloadMagazineTime',
                           AUTO_RELOAD_PROP_NAME, RELOAD_TIME_PROP_NAME, SHELL_LOADING_TIME_PROP_NAME, b'rateTime', b'chargeTime',
                           TWIN_GUN_SWITCH_FIRE_MODE_TIME, CONTINUOUS_SHOTS_PER_MINUTE, b'stunMinDurationList', b'stunMaxDurationList',
                           DISPERSION_RADIUS, DUAL_ACCURACY_COOLING_DELAY, b'maxShotDistance', b'aimingTime', b'weight')}
FORMAT_NAME_C_S_VALUE_S_UNITS = b'{paramName} {paramValue} {paramUnits}'
_COUNT_OF_AUTO_RELOAD_SLOTS_TIMES_TO_SHOW_IN_INFO = 5
_EQUAL_TO_ZERO_LITERAL = b'~0'

def needUseYohChassisRepairTime(vehicleDescr):
    return vehicleDescr and vehicleDescr.isTrackWithinTrack


MULTIPLE_MEASURE_UNITS_PARAMS = {CHASSIS_REPAIR_TIME: (ChangeCondition(needUseYohChassisRepairTime, CHASSIS_REPAIR_TIME_YOH))}
CRITICAL_HIT_CHANCE_TYPE_DYN_PATH = {(CriticalHitChanceType.STANDARD): b'standard', 
   (CriticalHitChanceType.DECREASED): b'decreased', 
   (CriticalHitChanceType.INCREASED): b'increased'}

def formatCriticalHitChance(value, _=None):
    criticalHitChanceR = R.strings.ingame_gui.shells_kinds.params.criticalHitChance
    return (backport.text(criticalHitChanceR.dyn(CRITICAL_HIT_CHANCE_TYPE_DYN_PATH[value])()), None, None)


def getMeasureParamName(vehicleDescr, paramName):
    if paramName in MULTIPLE_MEASURE_UNITS_PARAMS:
        measureCondition = MULTIPLE_MEASURE_UNITS_PARAMS[paramName]
        if measureCondition.predicate(vehicleDescr):
            return measureCondition.alternativeParameter
    return paramName


def getMeasureUnitsForParameter(vehicleDescr, paramName):
    measureParamName = getMeasureParamName(vehicleDescr, paramName)
    measureUnitLoc = MEASURE_UNITS.get(measureParamName, b'')
    if isValidKey(measureUnitLoc):
        return makeString(measureUnitLoc)
    return b''


MULTIPLE_TITLES_PARAMS = {CHASSIS_REPAIR_TIME: (ChangeCondition(needUseYohChassisRepairTime, CHASSIS_REPAIR_TIME_YOH))}

def getTitleParamName(vDescr, paramName):
    if paramName in MULTIPLE_TITLES_PARAMS:
        changeCondition = MULTIPLE_TITLES_PARAMS[paramName]
        if changeCondition.predicate(vDescr):
            return changeCondition.alternativeParameter
    return paramName


def measureUnitsForParameter(paramName):
    return i18n.makeString(MEASURE_UNITS.get(paramName, b''))


def isRelativeParameter(paramName):
    return paramName in RELATIVE_PARAMS


def isRelativeParameterVisible(parameter):
    return isRelativeParameter(parameter.name) and isDiffEnoughToDisplay(parameter.state[1])


def isDiffEnoughToDisplay(value):
    return abs(int(value)) > 0


def getParameterSmallIconPath(parameter):
    return RES_ICONS.MAPS_ICONS_VEHPARAMS_SMALL + b'/%s.png' % parameter


def getParameterBigIconPath(parameter):
    return RES_ICONS.MAPS_ICONS_VEHPARAMS_BIG + b'/%s.png' % parameter


def formatModuleParamName(paramName, vDescr=None):
    builder = text_styles.builder(delimiter=backport.text(_NBSP))
    hasBoost = vDescr and vDescr.gun.autoreloadHasBoost
    titleName = getTitleParamName(vDescr, paramName)
    if paramName == b'minAvgMutableDamageList':
        dist = DAMAGE_INTERPOLATION_DIST_LAST
        if vDescr is not None:
            dist = int(min(vDescr.shot.maxDistance, DAMAGE_INTERPOLATION_DIST_LAST))
        textOrMsgId = backport.text(R.strings.menu.moduleInfo.params.dyn(titleName)(), dist=dist)
    else:
        resource = R.strings.menu.moduleInfo.params.dyn(titleName)
        textOrMsgId = backport.msgid(resource.dyn(b'boost')() if hasBoost and resource.dyn(b'boost') else resource())
    builder.addStyledText(text_styles.main, textOrMsgId)
    measureName = getMeasureParamName(vDescr, paramName)
    builder.addStyledText(text_styles.standard, MEASURE_UNITS.get(measureName, b''))
    return builder.render()


def formatNameColonValue(nameStr, valueStr):
    builder = text_styles.builder(delimiter=backport.text(_NBSP))
    builder.addStyledText(text_styles.main, (b'{}{}').format(makeString(nameStr), _COLON))
    builder.addStyledText(text_styles.expText, makeString(valueStr))
    return builder.render()


def formatParamNameColonValueUnits(paramName, paramValue):
    builder = text_styles.builder(delimiter=backport.text(_NBSP))
    resource = R.strings.menu.moduleInfo.params
    paramMsgId = backport.msgid(resource.dyn(paramName)()) if resource.dyn(paramName) else None
    builder.addStyledText(text_styles.main, (b'{}{}').format(makeString(paramMsgId), _COLON))
    builder.addStyledText(text_styles.expText, paramValue)
    builder.addStyledText(text_styles.standard, MEASURE_UNITS_NO_BRACKETS.get(paramName, b''))
    return builder.render()


def formatVehicleParamName(paramName, showMeasureUnit=True):
    if isRelativeParameter(paramName):
        return text_styles.middleTitle(MENU.tank_params(paramName))
    builder = text_styles.builder(delimiter=backport.text(_NBSP))
    builder.addStyledText(text_styles.main, MENU.tank_params(paramName))
    if showMeasureUnit:
        builder.addStyledText(text_styles.standard, MEASURE_UNITS.get(paramName, b''))
    return builder.render()


def getRelativeDiffParams(comparator):
    relativeParams = [p for p in comparator.getAllDifferentParams() if isRelativeParameterVisible(p)]
    return sorted(relativeParams, key=(lambda k: RELATIVE_PARAMS.index(k.name)))


_NBSP = R.strings.common.common.nbsp()
_DASH = b'-'
_SLASH = b'/'
_COLON = b':'
_niceFormat = {b'rounder': (backport.getNiceNumberFormat)}
_niceRangeFormat = {b'rounder': (backport.getNiceNumberFormat), b'separator': _DASH}
_listFormat = {b'rounder': (lambda v: backport.getIntegralFormat(int(v))), b'separator': _SLASH}
_niceListFormat = {b'rounder': (backport.getNiceNumberFormat), b'separator': _SLASH}
_niceListFormatWithoutNone = {b'rounder': (backport.getNiceNumberFormat), b'separator': _SLASH, b'skipNone': True}
_integralFormat = {b'rounder': (backport.getIntegralFormat)}
_percentFormat = {b'rounder': (lambda v: b'%d%%' % v)}
_plusPercentFormat = {b'rounder': (lambda v: b'+%d%%' % v)}

def _autoReloadPreprocessor(reloadTimes, rowStates):
    times = []
    states = []
    if not hasattr(reloadTimes, b'__iter__'):
        return (
         times, _SLASH, states if states else None)
    for idx, slotTime in enumerate(reloadTimes):
        if isinstance(slotTime, (float, int)) or slotTime is None:
            times.append(slotTime)
            if rowStates:
                states.append(rowStates[idx])
            continue
        if isinstance(slotTime, tuple):
            minSlotTime, maxSlotTime = slotTime
            if minSlotTime == maxSlotTime:
                times.append(minSlotTime)
                if rowStates:
                    states.append(rowStates[idx][0])
            else:
                LOG_ERROR(b'Different auto-reload times for same gun and slot')
                return

    if len(times) > _COUNT_OF_AUTO_RELOAD_SLOTS_TIMES_TO_SHOW_IN_INFO:
        if states:
            minTime, maxTime = min(times), max(times)
            minState, maxState = (None, None)
            for idx, time in enumerate(times):
                if time == minTime:
                    minState = states[idx]
                if time == maxTime:
                    maxState = states[idx]

            return (
             (
              min(times), max(times)), _DASH, (minState, maxState))
        return ((min(times), max(times)), _DASH, None)
    else:
        return (
         times, _SLASH, states if states else None)


def clipFireRatePreprocessor(values, states):
    internalClipState, internalClipStateDiff = states[1]
    internalClipState = PARAM_STATE.WORSE if values[1] is None else internalClipState
    states = [states[0], (internalClipState, internalClipStateDiff), states[2]]
    return (values, _SLASH, states)


def shotDispersionAnglePreprocessor(values, states):
    _, dualAccuracyParamDiff = states[0]
    states = [(PARAM_STATE.WORSE, dualAccuracyParamDiff)] + [states[1]] if len(states) > 1 else states
    return (values, _SLASH, states)


def _getRoundReload(value):
    return backport.getNiceNumberFormat(decimal_round(value, 1))


FORMAT_SETTINGS = {b'relativePower': _integralFormat, 
   b'damage': _niceRangeFormat, 
   b'maxMutableDamage': _niceRangeFormat, 
   b'minMutableDamage': _niceRangeFormat, 
   b'piercingPower': _niceRangeFormat, 
   b'maxPiercingPower': _niceRangeFormat, 
   b'minPiercingPower': _niceRangeFormat, 
   RELOAD_TIME_PROP_NAME: _niceRangeFormat, 
   TEMPERATURE_RELOAD_TIME: _niceFormat, 
   CONTINUOUS_SHOTS_PER_MINUTE: _niceRangeFormat, 
   b'reloadTimeSecs': _niceListFormat, 
   b'turretRotationSpeed': _niceListFormat, 
   b'turretYawLimits': _niceListFormat, 
   b'gunYawLimits': _niceListFormat, 
   b'pitchLimits': _niceListFormat, 
   b'clipFireRate': _niceListFormat, 
   AUTO_SHOOT_CLIP_FIRE_RATE: _niceListFormat, 
   BURST_FIRE_RATE: _niceListFormat, 
   BURST_TIME_INTERVAL: _niceFormat, 
   BURST_COUNT: _integralFormat, 
   BURST_SIZE: _integralFormat, 
   b'turboshaftBurstFireRate': _niceListFormat, 
   b'aimingTime': _niceListFormat, 
   b'avgDamagePerMinute': _niceFormat, 
   TEMPERATURE_AVG_DAMAGE_PER_MINUTE: _niceFormat, 
   b'relativeArmor': _integralFormat, 
   b'avgDamage': _niceFormat, 
   b'avgMutableDamage': _niceRangeFormat, 
   AVG_DAMAGE_PER_SECOND: _niceFormat, 
   CONTINUOUS_DAMAGE_PER_SECOND: _niceRangeFormat, 
   b'maxHealth': _integralFormat, 
   b'hullArmor': _listFormat, 
   b'turretArmor': _listFormat, 
   b'relativeMobility': _integralFormat, 
   b'vehicleWeight': _niceFormat, 
   b'weight': _niceRangeFormat, 
   b'enginePower': _integralFormat, 
   TURBOSHAFT_ENGINE_POWER: _integralFormat, 
   ROCKET_ACCELERATION_ENGINE_POWER: _integralFormat, 
   b'enginePowerPerTon': _niceListFormat, 
   b'speedLimits': _niceListFormat, 
   b'chassisRotationSpeed': _niceFormat, 
   b'relativeVisibility': _integralFormat, 
   b'relativeCamouflage': _integralFormat, 
   b'circularVisionRadius': _niceListFormat, 
   b'radioDistance': _niceFormat, 
   b'rotationSpeed': _niceFormat, 
   b'fireStartingChance': _percentFormat, 
   b'armor': _listFormat, 
   b'caliber': _niceFormat, 
   b'shotsNumberRange': _niceFormat, 
   b'areaRadius': _niceFormat, 
   b'artDelayRange': _niceFormat, 
   b'bombDamage': _niceRangeFormat, 
   b'bombsNumberRange': _niceFormat, 
   b'areaSquare': _niceFormat, 
   b'flyDelayRange': _niceFormat, 
   b'explosionRadius': _niceFormat, 
   b'shellsCount': _niceRangeFormat, 
   b'shellReloadingTime': _niceRangeFormat, 
   b'reloadMagazineTime': _niceRangeFormat, 
   SHELL_LOADING_TIME_PROP_NAME: _niceFormat, 
   b'avgPiercingPower': _listFormat, 
   b'avgDamageList': _listFormat, 
   b'maxAvgMutableDamageList': _listFormat, 
   b'minAvgMutableDamageList': _listFormat, 
   SHOT_DISPERSION_ANGLE: _niceListFormatWithoutNone, 
   DISPERSION_RADIUS: _niceListFormatWithoutNone, 
   b'invisibilityStillFactor': _niceListFormat, 
   b'invisibilityMovingFactor': _niceListFormat, 
   TURBOSHAFT_INVISIBILITY_STILL_FACTOR: _niceListFormat, 
   TURBOSHAFT_INVISIBILITY_MOVING_FACTOR: _niceListFormat, 
   b'switchOnTime': _niceFormat, 
   b'switchOffTime': _niceFormat, 
   b'switchTime': _niceListFormat, 
   TURBOSHAFT_SWITCH_TIME: _niceListFormat, 
   b'stunMaxDuration': _niceFormat, 
   b'stunMinDuration': _niceFormat, 
   b'stunMaxDurationList': _niceListFormat, 
   b'stunMinDurationList': _niceListFormat, 
   b'stunDurationList': _niceRangeFormat, 
   b'cooldownSeconds': _niceFormat, 
   AUTO_RELOAD_PROP_NAME: {b'preprocessor': _autoReloadPreprocessor, b'rounder': _getRoundReload}, MAX_STEERING_LOCK_ANGLE: _niceFormat, 
   WHEELED_SWITCH_ON_TIME: _niceFormat, 
   WHEELED_SWITCH_OFF_TIME: _niceFormat, 
   WHEELED_SWITCH_TIME: _niceListFormat, 
   WHEELED_SPEED_MODE_SPEED: _niceListFormat, 
   DUAL_GUN_CHARGE_TIME: _niceListFormat, 
   DUAL_GUN_RATE_TIME: _niceListFormat, 
   DUAL_ACCURACY_COOLING_DELAY: _niceFormat, 
   b'shotSpeed': _integralFormat, 
   b'extraRepairSpeed': _percentFormat, 
   TURBOSHAFT_SPEED_MODE_SPEED: _niceListFormat, 
   ROCKET_ACCELERATION_SPEED_LIMITS: _niceListFormat, 
   ROCKET_ACCELERATION_REUSE_AND_DURATION: _niceListFormat, 
   CHASSIS_REPAIR_TIME: _niceListFormat, 
   b'commonDelay': _niceFormat, 
   b'duration': _niceFormat, 
   b'inactivationDelay': _niceFormat, 
   b'commonAreaRadius': _niceFormat, 
   b'crewRolesFactor': _plusPercentFormat, 
   b'maxDamage': _niceFormat, 
   b'artNotificationDelayFactor': _niceFormat, 
   b'vehicleOwnSpottingTime': _niceFormat, 
   b'damagedModulesDetectionTime': _niceFormat, 
   b'commanderLampDelay': _niceFormat, 
   TWIN_GUN_SWITCH_FIRE_MODE_TIME: _niceListFormat, 
   TWIN_GUN_TOP_SPEED: _niceListFormat, 
   TWIN_GUN_RELOAD_ONE_GUN_TIME: _niceFormat, 
   TWIN_GUN_RELOAD_TWO_GUN_TIME: _niceFormat, 
   b'piercingHEShellsDistributionUpperBound': _niceFormat, 
   b'suspensionDamageReduction': _percentFormat, 
   b'hpRecover': _percentFormat, 
   CRITICAL_HIT_CHANCE: {b'preprocessor': formatCriticalHitChance, b'rounder': (lambda v: v)}}

def _deltaWrapper(fn):

    def wrapped(paramValue):
        formattedValue = fn(paramValue)
        if formattedValue in (b'0', b'-0'):
            return _EQUAL_TO_ZERO_LITERAL
        if isinstance(paramValue, (int, float)) and paramValue > 0:
            return b'+%s' % formattedValue
        return formattedValue

    return wrapped


def _getDeltaSettings():
    detlaSettings = {}
    for paramName, setting in iteritems(FORMAT_SETTINGS):
        settingCopy = setting.copy()
        rounder = settingCopy[b'rounder']
        settingCopy[b'rounder'] = _deltaWrapper(rounder)
        detlaSettings[paramName] = settingCopy

    return detlaSettings


DELTA_PARAMS_SETTING = _getDeltaSettings()
SMART_ROUND_PARAMS = {
 83, 59, 42, 74, 199, 68, 
 RELOAD_TIME_PROP_NAME, DISPERSION_RADIUS, 32, 
 79, DUAL_GUN_RATE_TIME, DUAL_GUN_CHARGE_TIME, 
 104, CONTINUOUS_SHOTS_PER_MINUTE, 
 CONTINUOUS_DAMAGE_PER_SECOND}
_STATES_INDEX_IN_COLOR_MAP = {(PARAM_STATE.WORSE): 0, 
   (PARAM_STATE.NORMAL): 1, 
   (PARAM_STATE.BETTER): 2, 
   (PARAM_STATE.SITUATIONAL): 2}

def colorize(paramStr, state, colorScheme):
    if isinstance(state, (tuple, list)):
        stateType, _ = state
    else:
        stateType = state
    if stateType == PARAM_STATE.NOT_APPLICABLE:
        return paramStr
    return colorScheme[_STATES_INDEX_IN_COLOR_MAP[stateType]](paramStr)


def colorizedFormatParameter(parameter, colorScheme):
    return formatParameter(parameter.name, parameter.value, parameter.state, colorScheme)


def colorizedFullFormatParameter(parameter, colorScheme):
    return formatParameter(parameter.name, parameter.value, parameter.state, colorScheme, allowSmartRound=False)


def simplifiedDeltaParameter(parameter, isSituational=False, isApproximately=False):
    mainFormatter = SIMPLIFIED_SCHEME[1]
    delta = int(parameter.state[1])
    paramStr = formatParameter(parameter.name, parameter.value)
    if delta:
        sign = b'-' if delta < 0 else b'+'
        approximatelySymbol = b'*' if isApproximately else b''
        scheme = SITUATIONAL_SCHEME if isSituational else SIMPLIFIED_SCHEME
        deltaStr = colorize(b'%s%s%s' % (sign, abs(delta), approximatelySymbol), parameter.state, scheme)
        return b'(%s) %s' % (deltaStr, mainFormatter(paramStr))
    return mainFormatter(paramStr)


def _applyFormat(value, state, settings, doSmartRound, colorScheme):
    if doSmartRound:
        value = _cutDigits(value)
    if isinstance(value, (str, unicode)):
        paramStr = value
    elif value is None or value == 0 and state is not None and state[0] == PARAM_STATE.NOT_APPLICABLE:
        paramStr = b'--'
    else:
        paramStr = settings[b'rounder'](value)
    if state is not None and colorScheme is not None:
        if paramStr == _EQUAL_TO_ZERO_LITERAL and isinstance(state, (tuple, list)):
            stateType, value = state
            if value > 0:
                paramStr = b'+&lt;0.01'
            elif value < 0:
                paramStr = b'-&lt;0.01'
            if stateType == PARAM_STATE.NORMAL:
                paramStr = b'0'
        paramStr = colorize(paramStr, state, colorScheme)
    return paramStr


def formatParameter(parameterName, paramValue, parameterState=None, colorScheme=None, formatSettings=None, allowSmartRound=True, showZeroDiff=False):
    formatSettings = formatSettings or FORMAT_SETTINGS
    settings = formatSettings.get(parameterName, _listFormat)
    doSmartRound = allowSmartRound and parameterName in SMART_ROUND_PARAMS
    preprocessor = settings.get(b'preprocessor')
    if KPI.Name.hasValue(parameterName):
        formatter = KPI_FORMATTERS.get(parameterName, kpiFormatValue)
        values, separator = formatter(parameterName, decimal_round(paramValue, 3)), None
    elif preprocessor:
        values, separator, parameterState = preprocessor(paramValue, parameterState)
    else:
        values = paramValue
        separator = None
    if values is None:
        return
    else:
        if isinstance(values, (tuple, list)):
            if parameterState is None:
                parameterState = [
                 None] * len(values)
            if doSmartRound and len(set(values)) == 1:
                if values[0] > 0:
                    return _applyFormat(values[0], parameterState[0], settings, doSmartRound, colorScheme)
                return
            separator = separator or settings.get(b'separator', b'')
            skipNone = settings.get(b'skipNone', False)
            if skipNone:
                params = [(val, state) for val, state in zip(values, parameterState) if val is not None]
            else:
                params = lzip(values, parameterState)
            paramsList = [_applyFormat(val, state, settings, doSmartRound, colorScheme) for val, state in params]
            return separator.join(paramsList)
        if not showZeroDiff and values == 0 and not isValidEmptyValue(parameterName, paramValue):
            return
        return _applyFormat(values, parameterState, settings, doSmartRound, colorScheme)


def formatParameterDelta(pInfo, deltaScheme=None, formatSettings=None):
    diff = pInfo.getParamDiff()
    if diff is not None:
        return formatParameter(pInfo.name, diff, pInfo.state, deltaScheme or BASE_SCHEME, formatSettings or DELTA_PARAMS_SETTING, allowSmartRound=False, showZeroDiff=True)
    else:
        return


def getFormattedParamsList(descriptor, parameters, excludeRelative=False):
    if vehicles.isVehicleDescr(descriptor):
        compactDescr = descriptor.type.compactDescr
    else:
        compactDescr = descriptor.compactDescr
    itemTypeIdx = getTypeOfCompactDescr(compactDescr)
    if itemTypeIdx == ITEM_TYPES.equipment:
        eqDescr = vehicles.getItemByCompactDescr(compactDescr)
        paramsList = ITEMS_PARAMS_LIST[itemTypeIdx].get(type(eqDescr), [])
    else:
        paramsList = ITEMS_PARAMS_LIST[itemTypeIdx]
    params = []
    for paramName in paramsList:
        if excludeRelative and isRelativeParameter(paramName):
            continue
        paramValue = parameters.get(paramName)
        if paramValue or isValidEmptyValue(paramName, paramValue):
            fmtValue = formatParameter(paramName, paramValue)
            if fmtValue:
                if paramName == b'autoReloadTime' and descriptor.gun.autoreloadHasBoost:
                    paramName = b'autoReloadTimeBoost'
                elif paramName == CHASSIS_REPAIR_TIME and descriptor.isTrackWithinTrack:
                    paramName = CHASSIS_REPAIR_TIME_YOH
                params.append((paramName, fmtValue))

    return params


def getBonusIconRes(bonusId, bonusType, archetype=None):
    if bonusType == BonusTypes.PAIR_MODIFICATION:
        mod = vehicles.g_cache.postProgression().getModificationByName(bonusId)
        if mod is not None:
            iconR = R.images.gui.maps.icons.vehPostProgression.actionItems.pairModifications.c_24x24.dyn(mod.imgName, R.invalid)()
        else:
            iconR = R.invalid()
    elif bonusId.find(b'Rammer') >= 0 and bonusId != b'deluxRammer' and bonusId.find(b'trophy') == -1:
        iconR = R.images.gui.maps.icons.vehParams.tooltips.bonuses.rammer()
    elif archetype:
        iconR = R.images.gui.maps.icons.vehParams.tooltips.bonuses.archetypes.dyn(archetype, R.invalid)()
    else:
        iconR = R.images.gui.maps.icons.vehParams.tooltips.bonuses.dyn(bonusId.split(b'_class')[0], R.invalid)()
    return iconR


def getBonusIcon(bonusId, bonusType, archetype=None):
    return backport.image(getBonusIconRes(bonusId, bonusType, archetype))


def getPenaltyIconRes(penaltyId):
    return R.images.gui.maps.icons.vehParams.tooltips.penalties.dyn(penaltyId, R.invalid)()


def getPenaltyIcon(penaltyId):
    return backport.image(getPenaltyIconRes(penaltyId))


def packSituationalIcon(text, icon):
    return (b'<nobr>').join((text, icon))


def getGroupPenaltyIcon(parameter, comparator):
    if hasGroupPenalties(parameter.name, comparator):
        return RES_ICONS.MAPS_ICONS_VEHPARAMS_ICON_DECREASE
    return b''


def getAllParametersTitles(hiddenParams=()):
    result = []
    for groupName in RELATIVE_PARAMS:
        data = getCommonParam(HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_SIMPLE_TOP, groupName)
        data[b'titleText'] = formatVehicleParamName(groupName)
        data[b'isEnabled'] = True
        data[b'tooltip'] = TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS
        result.append(data)
        for paramName in (p for p in PARAMS_GROUPS[groupName] if p not in hiddenParams):
            data = getCommonParam(HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_ADVANCED, paramName, groupName)
            data[b'iconSource'] = getParameterSmallIconPath(paramName)
            data[b'titleText'] = formatVehicleParamName(paramName)
            data[b'isEnabled'] = False
            data[b'tooltip'] = TOOLTIPS_CONSTANTS.BASE_VEHICLE_PARAMETERS
            result.append(data)

    return result


def _cutDigits(value):
    if abs(value) > 99:
        return round_py2_style(value)
    if abs(value) > 9:
        return decimal_round(value, 1)
    return decimal_round(value, 2)
