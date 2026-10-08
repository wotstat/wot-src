import typing
from collections import namedtuple
from itertools import chain
from constants import BonusTypes
from debug_utils import LOG_ERROR
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.gui_items import KPI, kpiFormatNoSignValue, kpiFormatWithSpec, kpiFormatNoSignWithSpec, kpiFormatNoSignList, kpiFormatNoSignEndingForEveryValueList
from gui.shared.items_parameters import RELATIVE_PARAMS, RELATIVE_PARAMS_WITHOUT_ABILITY
from gui.shared.items_parameters.comparator import PARAM_STATE
from gui.shared.items_parameters.params_helper import hasGroupPenalties, getCommonParam, isValidEmptyValue, PARAMS_GROUPS
from gui.shared.utils import AUTO_RELOAD_PROP_NAME, MAX_STEERING_LOCK_ANGLE, WHEELED_SWITCH_ON_TIME, WHEELED_SWITCH_OFF_TIME, WHEELED_SWITCH_TIME, WHEELED_SPEED_MODE_SPEED, DUAL_GUN_CHARGE_TIME, DUAL_GUN_RATE_TIME, TURBOSHAFT_SPEED_MODE_SPEED, TURBOSHAFT_ENGINE_POWER, TURBOSHAFT_INVISIBILITY_STILL_FACTOR, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_SWITCH_TIME, CHASSIS_REPAIR_TIME, CHASSIS_REPAIR_TIME_YOH, ROCKET_ACCELERATION_ENGINE_POWER, ROCKET_ACCELERATION_SPEED_LIMITS, ROCKET_ACCELERATION_REUSE_AND_DURATION, DUAL_ACCURACY_COOLING_DELAY, SHOT_DISPERSION_ANGLE, DISPERSION_RADIUS, BURST_FIRE_RATE, BURST_TIME_INTERVAL, BURST_SIZE, BURST_COUNT, DISTANCE_DAMAGE_PROP_NAME, CHASSIS_REPAIR_TIME_MULTITRACK_SEQUENT, CHASSIS_REPAIR_TIME_MULTITRACK_PARALLEL, AUTOSHOOT_FLAME_CHANGE_SHELL_TIME, AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME, RELOAD_TIME_PER_SECOND, AVG_DAMAGE_PER_SECOND, AUTOSHOOT_FIRE_UNTIL_OVERHEAT_TIME, THERMAL_VISION_REUSE_AND_DURATION, THERMAL_VISION_DISTANCE, THERMAL_VISION_RELOAD_TIME, THERMAL_VISION_OBSERVE_TIME, SHELLS_COUNT_PROP_NAME
from helpers.i18n import makeString
from items.vehicle_items import CHASSIS_ITEM_TYPE
from items import vehicles, artefacts, getTypeOfCompactDescr, ITEM_TYPES
from web_stubs import i18n
ChangeCondition = namedtuple(b'ChangeCondition', (b'predicate', b'alternativeParameter'))
_NBSP = backport.text(R.strings.common.common.nbsp())
_DASH = b'-'
_SLASH = b'/'
_COLON = b':'
_niceFormat = {b'rounder': (backport.getNiceNumberFormat)}
_niceRangeFormat = {b'rounder': (backport.getNiceNumberFormat), b'separator': _DASH}
_listFormat = {b'rounder': (lambda v: backport.getIntegralFormat(int(v))), b'separator': _SLASH}
_niceListFormat = {b'rounder': (backport.getNiceNumberFormat), b'separator': _SLASH}
_niceListFormatWithoutNone = {b'rounder': (backport.getNiceNumberFormat), b'separator': _SLASH, b'skipNone': True}
_integralFormat = {b'rounder': (backport.getIntegralFormat)}
_integralRangeFormat = {b'rounder': (backport.getIntegralFormat), b'separator': _DASH}
_percentFormat = {b'rounder': (lambda v: b'%d%%' % v)}
_plusPercentFormat = {b'rounder': (lambda v: b'+%d%%' % v)}
MEASURE_UNITS = {b'aimingTime': (MENU.TANK_PARAMS_S), 
   b'areaRadius': (MENU.TANK_PARAMS_M), 
   b'areaSquare': (MENU.TANK_PARAMS_SQM), 
   b'armor': (MENU.TANK_PARAMS_FACEFRONTBOARDINMM), 
   b'artDelayRange': (MENU.TANK_PARAMS_S), 
   b'avgDamageList': (MENU.TANK_PARAMS_VAL), 
   b'gunModuleAvgDamageList': (MENU.TANK_PARAMS_VAL), 
   b'avgPiercingPower': (MENU.TANK_PARAMS_MM), 
   b'bombDamage': (MENU.TANK_PARAMS_VAL), 
   b'bombsNumberRange': (MENU.TANK_PARAMS_CNT), 
   b'chassisRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'circularVisionRadius': (MENU.TANK_PARAMS_M), 
   b'clipFireRate': (MENU.TANK_PARAMS_CLIPSEC), 
   BURST_FIRE_RATE: (MENU.TANK_PARAMS_BURSTSEC), 
   AUTOSHOOT_FLAME_CHANGE_SHELL_TIME: (MENU.TANK_PARAMS_S), 
   AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME: (MENU.TANK_PARAMS_S), 
   AUTOSHOOT_FIRE_UNTIL_OVERHEAT_TIME: (MENU.TANK_PARAMS_S), 
   b'flameMaxDistance': (MENU.TANK_PARAMS_M), 
   b'turboshaftBurstFireRate': (MENU.TANK_PARAMS_BURSTSEC), 
   BURST_TIME_INTERVAL: (MENU.TANK_PARAMS_S), 
   BURST_COUNT: (MENU.TANK_PARAMS_CNT), 
   BURST_SIZE: (MENU.TANK_PARAMS_CNT), 
   b'avgDamage': (MENU.TANK_PARAMS_VAL), 
   DISTANCE_DAMAGE_PROP_NAME: (MENU.TANK_PARAMS_VAL), 
   b'distanceFactorDamage': (MENU.TANK_PARAMS_VAL), 
   b'distanceFactorPiercingPower': (MENU.TANK_PARAMS_MM), 
   b'avgDamagePerMinute': (MENU.TANK_PARAMS_VPM), 
   b'damagePerSecond': (MENU.TANK_PARAMS_VPS), 
   b'avgDamagePerSecond': (MENU.TANK_PARAMS_VPS), 
   b'fireStartingChance': (MENU.TANK_PARAMS_PERCENT), 
   b'maxHealth': (MENU.TANK_PARAMS_VAL), 
   b'flyDelayRange': (MENU.TANK_PARAMS_S), 
   b'enginePower': (MENU.TANK_PARAMS_P), 
   TURBOSHAFT_ENGINE_POWER: (MENU.TANK_PARAMS_P), 
   ROCKET_ACCELERATION_ENGINE_POWER: (MENU.TANK_PARAMS_P), 
   ROCKET_ACCELERATION_REUSE_AND_DURATION: (MENU.TANK_PARAMS_QPT), 
   THERMAL_VISION_REUSE_AND_DURATION: (MENU.TANK_PARAMS_QPT), 
   THERMAL_VISION_DISTANCE: (MENU.TANK_PARAMS_M), 
   THERMAL_VISION_RELOAD_TIME: (MENU.TANK_PARAMS_S), 
   THERMAL_VISION_OBSERVE_TIME: (MENU.TANK_PARAMS_S), 
   ROCKET_ACCELERATION_SPEED_LIMITS: (MENU.TANK_PARAMS_MPH), 
   b'enginePowerPerTon': (MENU.TANK_PARAMS_PT), 
   b'explosionRadius': (MENU.TANK_PARAMS_M), 
   b'gunYawLimits': (MENU.TANK_PARAMS_GRADS), 
   b'hullArmor': (MENU.TANK_PARAMS_FACEFRONTBOARDINMM), 
   b'piercingPower': (MENU.TANK_PARAMS_MM), 
   b'pitchLimits': (MENU.TANK_PARAMS_GRADS), 
   b'radioDistance': (MENU.TANK_PARAMS_M), 
   b'radarRadius': (MENU.TANK_PARAMS_M), 
   b'radarCooldown': (MENU.TANK_PARAMS_S), 
   b'maxHullHealth': (MENU.TANK_PARAMS_VAL), 
   b'forwardMaxSpeed': (MENU.TANK_PARAMS_MPH), 
   b'reloadMagazineTime': (MENU.TANK_PARAMS_S), 
   b'reloadTime': (MENU.TANK_PARAMS_SPM), 
   b'reloadTimeSecs': (MENU.TANK_PARAMS_S), 
   RELOAD_TIME_PER_SECOND: (MENU.TANK_PARAMS_SPS), 
   b'rotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'chassisModuleRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'turretModuleRotationSpeed': (MENU.TANK_PARAMS_GPS), 
   b'shellReloadingTime': (MENU.TANK_PARAMS_S), 
   SHOT_DISPERSION_ANGLE: (MENU.TANK_PARAMS_M), 
   b'shotsNumberRange': (MENU.TANK_PARAMS_CNT), 
   b'shellsCount': (MENU.TANK_PARAMS_CNT), 
   b'shellsBurstCount': (MENU.TANK_PARAMS_CNT), 
   b'shellsFlameBurstCount': (MENU.TANK_PARAMS_L), 
   b'speedLimits': (MENU.TANK_PARAMS_MPH), 
   b'turretArmor': (MENU.TANK_PARAMS_FACEFRONTBOARDINMM), 
   b'turretYawLimits': (MENU.TANK_PARAMS_GRADS), 
   b'vehicleWeight': (MENU.TANK_PARAMS_T), 
   b'weight': (MENU.TANK_PARAMS_KG), 
   b'hullWeight': (MENU.TANK_PARAMS_KG), 
   b'hullAndChassisWeight': (MENU.TANK_PARAMS_KG), 
   b'caliber': (MENU.TANK_PARAMS_MM), 
   b'damage': (MENU.TANK_PARAMS_VAL), 
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
   b'stunMaxDurationList': (MENU.TANK_PARAMS_S), 
   b'cooldownSeconds': (MENU.TANK_PARAMS_S), 
   b'cooldown': (MENU.TANK_PARAMS_S), 
   b'activeSeconds': (MENU.TANK_PARAMS_S), 
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
   b'shotSpeedAccelerated': (MENU.TANK_PARAMS_MPS), 
   CHASSIS_REPAIR_TIME: (MENU.TANK_PARAMS_S), 
   CHASSIS_REPAIR_TIME_YOH: (MENU.TANK_PARAMS_YOH_S_S), 
   CHASSIS_REPAIR_TIME_MULTITRACK_SEQUENT: (MENU.TANK_PARAMS_MULTITRACKSEQUENT_S_S), 
   CHASSIS_REPAIR_TIME_MULTITRACK_PARALLEL: (MENU.TANK_PARAMS_MULTITRACKPARALLEL_S_S), 
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
   b'vehicleGunShotStabilizationChassisMovement': (MENU.TANK_PARAMS_PERCENT), 
   b'vehicleGunShotStabilizationChassisRotation': (MENU.TANK_PARAMS_PERCENT), 
   b'reuseCount': (MENU.TANK_PARAMS_EMPTY)}
MEASURE_UNITS_NO_BRACKETS = {b'weight': (MENU.TANK_PARAMS_NO_BRACKETS_KG), 
   b'cooldownSeconds': (MENU.TANK_PARAMS_NO_BRACKETS_S), 
   b'activeSeconds': (MENU.TANK_PARAMS_NO_BRACKETS_S), 
   b'reloadCooldownSeconds': (MENU.TANK_PARAMS_NO_BRACKETS_S), 
   b'caliber': (MENU.TANK_PARAMS_NO_BRACKETS_MM)}
KPIFormatter = namedtuple(b'KPIFormatter', [b'formatter', b'separator', b'addEnding'])
_kpiNoSignValue = KPIFormatter(formatter=kpiFormatNoSignValue, separator=None, addEnding=True)
_kpiNoSignNoEndingValue = KPIFormatter(formatter=kpiFormatNoSignValue, separator=None, addEnding=False)
_kpiNoSignList = KPIFormatter(formatter=kpiFormatNoSignList, separator=None, addEnding=True)
_kpiFormatNoSignEndingForEveryValueList = KPIFormatter(formatter=kpiFormatNoSignEndingForEveryValueList, separator=None, addEnding=True)
_kpiNoSignNoEndingList = KPIFormatter(formatter=kpiFormatNoSignList, separator=None, addEnding=False)
_kpiWithSpec = KPIFormatter(formatter=kpiFormatWithSpec, separator=None, addEnding=True)
_kpiNoSignWithSpec = KPIFormatter(formatter=kpiFormatNoSignWithSpec, separator=None, addEnding=True)
KPI_FORMATTERS = {(KPI.Name.DAMAGED_MODULES_DETECTION_TIME): _kpiNoSignValue, 
   (KPI.Name.ART_NOTIFICATION_DELAY_FACTOR): _kpiNoSignValue, 
   (KPI.Name.LIMITS_FOR_GUN_BOOST): _kpiNoSignWithSpec, 
   (KPI.Name.VEHICLE_GUN_AND_GUN_CLIP_COOLDOWN): _kpiWithSpec, 
   (KPI.Name.VEHICLE_GUN_DAMAGE): _kpiNoSignWithSpec, 
   (KPI.Name.VEHICLE_GUN_SPEC_DAMAGE): _kpiWithSpec, 
   (KPI.Name.TEMPERATURE_STATES_COUNT): _kpiNoSignNoEndingValue, 
   (KPI.Name.TEMPERATURE_HEATING_TIME): _kpiNoSignNoEndingList, 
   (KPI.Name.TEMPERATURE_COOLING_TIME): _kpiNoSignNoEndingList, 
   (KPI.Name.TEMPERATURE_COOLING_DELAY): _kpiNoSignNoEndingList, 
   (KPI.Name.TEMPERATURE_DAMAGE_FACTOR): _kpiFormatNoSignEndingForEveryValueList}
COLORLESS_SCHEME = (
 text_styles.stats, text_styles.stats, text_styles.stats)
NO_BONUS_SIMPLIFIED_SCHEME = (text_styles.warning, text_styles.warning, text_styles.warning)
NO_BONUS_BASE_SCHEME = (text_styles.error, text_styles.stats, text_styles.stats)
SIMPLIFIED_SCHEME = (text_styles.critical, text_styles.warning, text_styles.statInfo)
BASE_SCHEME = (text_styles.error, text_styles.stats, text_styles.bonusAppliedText)
EXTRACTED_BONUS_SCHEME = (text_styles.error, text_styles.bonusAppliedText, text_styles.bonusAppliedText)
SITUATIONAL_SCHEME = (text_styles.critical, text_styles.warning, text_styles.bonusPreviewText)
VEHICLE_PARAMS = tuple(chain(*[PARAMS_GROUPS[param] for param in RELATIVE_PARAMS_WITHOUT_ABILITY]))
ITEMS_PARAMS_LIST = {(ITEM_TYPES.vehicleRadio): (b'radioDistance', b'weight'), 
   (ITEM_TYPES.vehicleChassis): (
                               b'rotationSpeed', b'weight', MAX_STEERING_LOCK_ANGLE, CHASSIS_REPAIR_TIME,
                               b'vehicleGunShotStabilizationChassisMovement', b'vehicleGunShotStabilizationChassisRotation'), 
   (ITEM_TYPES.vehicleEngine): (
                              b'enginePower', TURBOSHAFT_ENGINE_POWER, ROCKET_ACCELERATION_ENGINE_POWER, b'fireStartingChance', b'weight'), 
   (ITEM_TYPES.vehicleTurret): (b'armor', b'rotationSpeed', b'circularVisionRadius', b'weight'), 
   (ITEM_TYPES.vehicle): VEHICLE_PARAMS, 
   (ITEM_TYPES.equipment): {(artefacts.RageArtillery): (b'damage', b'piercingPower', b'caliber', b'shotsNumberRange', b'areaRadius', b'artDelayRange'), 
                            (artefacts.RageBomber): (b'bombDamage', b'piercingPower', b'bombsNumberRange', b'areaSquare', b'flyDelayRange'), 
                            (artefacts.AttackArtilleryFortEquipment): (b'maxDamage', b'areaRadius', b'duration', b'commonDelay'), 
                            (artefacts.FortConsumableInspire): (b'crewRolesFactor', b'commonAreaRadius', b'inactivationDelay', b'duration'), 
                            (artefacts.ConsumableInspire): (b'crewRolesFactor', b'commonAreaRadius', b'inactivationDelay', b'duration')}, 
   (ITEM_TYPES.shell): (b'caliber', b'damage', b'damagePerSecond', b'avgPiercingPower', b'shotSpeed', b'explosionRadius', b'flameMaxDistance', b'stunMaxDuration', b'shotSpeedAccelerated'), 
   (ITEM_TYPES.optionalDevice): (b'weight',), 
   (ITEM_TYPES.vehicleGun): (
                           b'caliber', b'shellsCount', b'shellsBurstCount', b'shellsFlameBurstCount',
                           b'reloadTimeSecs', b'shellReloadingTime', b'reloadMagazineTime',
                           AUTO_RELOAD_PROP_NAME, b'reloadTime', b'rateTime', b'chargeTime', b'avgPiercingPower', b'avgDamageList',
                           b'stunMaxDurationList', DISPERSION_RADIUS, DUAL_ACCURACY_COOLING_DELAY,
                           b'aimingTime', b'maxShotDistance', b'weight', AUTOSHOOT_FLAME_CHANGE_SHELL_TIME,
                           AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME, AVG_DAMAGE_PER_SECOND, RELOAD_TIME_PER_SECOND)}
FORMAT_NAME_C_S_VALUE_S_UNITS = b'{paramName} {paramValue} {paramUnits}'
_COUNT_OF_AUTO_RELOAD_SLOTS_TIMES_TO_SHOW_IN_INFO = 5
_EQUAL_TO_ZERO_LITERAL = b'~0'

def useYohChassisRepairTime(vehicleDescr):
    return vehicleDescr and vehicleDescr.isTrackWithinTrack


def useAutoShootGunShellsCount(vehicleDescr):
    return vehicleDescr and vehicleDescr.isAutoShootGunVehicle


def useMultiTrackSequentChassisRepairTime(vehicleDescr):
    return vehicleDescr and vehicleDescr.chassisType == CHASSIS_ITEM_TYPE.MULTITRACK_SEQUENT


def useMultiTrackParallelChassisRepairTime(vehicleDescr):
    return vehicleDescr and vehicleDescr.chassisType == CHASSIS_ITEM_TYPE.MULTITRACK_PARALLEL


def useAutoReloadBoost(vehicleDescr):
    return vehicleDescr and vehicleDescr.gun.autoreloadHasBoost


MULTIPLE_MEASURE_UNITS_PARAMS = {CHASSIS_REPAIR_TIME: (
                       ChangeCondition(useYohChassisRepairTime, CHASSIS_REPAIR_TIME_YOH),
                       ChangeCondition(useMultiTrackSequentChassisRepairTime, CHASSIS_REPAIR_TIME_MULTITRACK_SEQUENT),
                       ChangeCondition(useMultiTrackParallelChassisRepairTime, CHASSIS_REPAIR_TIME_MULTITRACK_PARALLEL))}

def getMeasureParamName(vehicleDescr, paramName):
    if paramName in MULTIPLE_MEASURE_UNITS_PARAMS:
        measureConditions = MULTIPLE_MEASURE_UNITS_PARAMS[paramName]
        for measureCondition in measureConditions:
            if measureCondition.predicate(vehicleDescr):
                return measureCondition.alternativeParameter

    return paramName


MULTIPLE_TITLES_PARAMS = {CHASSIS_REPAIR_TIME: (ChangeCondition(useYohChassisRepairTime, CHASSIS_REPAIR_TIME_YOH)), 
   SHELLS_COUNT_PROP_NAME: (ChangeCondition(useAutoShootGunShellsCount, b'autoShootShellsCount'))}

def getTitleParamName(vehicleDescr, paramName):
    if paramName in MULTIPLE_TITLES_PARAMS:
        changeCondition = MULTIPLE_TITLES_PARAMS[paramName]
        if changeCondition.predicate(vehicleDescr):
            return changeCondition.alternativeParameter
    return paramName


MULTIPLE_FORMATTED_PARAMS = {CHASSIS_REPAIR_TIME: (
                       ChangeCondition(useYohChassisRepairTime, CHASSIS_REPAIR_TIME_YOH),
                       ChangeCondition(useMultiTrackSequentChassisRepairTime, CHASSIS_REPAIR_TIME_MULTITRACK_SEQUENT),
                       ChangeCondition(useMultiTrackParallelChassisRepairTime, CHASSIS_REPAIR_TIME_MULTITRACK_PARALLEL)), 
   b'autoReloadTime': (
                     ChangeCondition(useAutoReloadBoost, b'autoReloadTimeBoost'),)}

def getFormattedParamName(vehicleDescr, paramName):
    if paramName in MULTIPLE_FORMATTED_PARAMS:
        changeConditions = MULTIPLE_FORMATTED_PARAMS[paramName]
        for changeCondition in changeConditions:
            if changeCondition.predicate(vehicleDescr):
                return changeCondition.alternativeParameter

    return paramName


def measureUnitsForParameter(paramName):
    return i18n.makeString(MEASURE_UNITS[paramName])


def isRelativeParameter(paramName):
    return paramName in RELATIVE_PARAMS


def isRelativeParameterVisible(parameter):
    return isRelativeParameter(parameter.name) and isDiffEnoughToDisplay(parameter.state[1])


def isDiffEnoughToDisplay(value):
    return abs(int(value)) > 0


def getParameterSmallIconPath(parameter):
    parameter = _getResAvailable(R.images.gui.maps.icons.vehParams.small, parameter)
    return RES_ICONS.MAPS_ICONS_VEHPARAMS_SMALL + b'/%s.png' % parameter


def getParameterBigIconPath(parameter):
    parameter = _getResAvailable(R.images.gui.maps.icons.vehParams.big, parameter)
    return RES_ICONS.MAPS_ICONS_VEHPARAMS_BIG + b'/%s.png' % parameter


def formatModuleParamName(paramName, vDescr=None):
    builder = text_styles.builder(delimiter=_NBSP)
    hasBoost = vDescr and vDescr.gun.autoreloadHasBoost
    titleName = getTitleParamName(vDescr, paramName)
    resource = R.strings.menu.moduleInfo.params.dyn(titleName)
    paramMsgId = backport.msgid(resource.dyn(b'boost')() if hasBoost and resource.dyn(b'boost') else resource())
    builder.addStyledText(text_styles.main, paramMsgId)
    measureName = getMeasureParamName(vDescr, paramName)
    builder.addStyledText(text_styles.standard, MEASURE_UNITS.get(measureName, b''))
    return builder.render()


def formatNameColonValue(nameStr, valueStr):
    builder = text_styles.builder(delimiter=_NBSP)
    builder.addStyledText(text_styles.main, (b'{}{}').format(makeString(nameStr), _COLON))
    builder.addStyledText(text_styles.expText, makeString(valueStr))
    return builder.render()


def formatParamNameColonValueUnits(paramName, paramValue):
    builder = text_styles.builder(delimiter=_NBSP)
    resource = R.strings.menu.moduleInfo.params
    paramMsgId = backport.msgid(resource.dyn(paramName)()) if resource.dyn(paramName) else None
    builder.addStyledText(text_styles.main, (b'{}{}').format(makeString(paramMsgId), _COLON))
    builder.addStyledText(text_styles.expText, paramValue)
    builder.addStyledText(text_styles.standard, MEASURE_UNITS_NO_BRACKETS.get(paramName, b''))
    return builder.render()


def formatVehicleParamName(paramName, showMeasureUnit=True):
    if isRelativeParameter(paramName):
        return text_styles.middleTitle(MENU.tank_params(paramName))
    else:
        builder = text_styles.builder(delimiter=_NBSP)
        builder.addStyledText(text_styles.main, MENU.tank_params(paramName))
        if showMeasureUnit:
            builder.addStyledText(text_styles.standard, MEASURE_UNITS.get(paramName, b''))
        return builder.render()

    return


def getRelativeDiffParams(comparator):
    relativeParams = [p for p in comparator.getAllDifferentParams() if isRelativeParameterVisible(p)]
    return sorted(relativeParams, cmp=(lambda a, b: cmp(RELATIVE_PARAMS.index(a.name), RELATIVE_PARAMS.index(b.name))))


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
        minTime, maxTime = times[0], times[-1]
        if states:
            minState, maxState = (None, None)
            for idx, time in enumerate(times):
                if time == minTime:
                    minState = states[idx]
                if time == maxTime:
                    maxState = states[idx]

            return (
             (
              minTime, maxTime), _DASH, (minState, maxState))
        return ((minTime, maxTime), _DASH, None)
    else:
        return (
         times, _SLASH, states if states else None)


def shotDispersionAnglePreprocessor(values, states):
    _, dualAccuracyParamDiff = states[0]
    states = [(PARAM_STATE.WORSE, dualAccuracyParamDiff)] + [states[1]] if len(states) > 1 else states
    return (values, _SLASH, states)


def chassisRepairTimePreprocessor(values, states):
    if states is not None:
        _, chassisRepairTimeDiff = states[0]
        if chassisRepairTimeDiff == 0 and len(states) == 2:
            states = [
             (
              PARAM_STATE.NOT_APPLICABLE, chassisRepairTimeDiff)] + [states[1]]
    return (
     values, _SLASH, states)


def _getRoundReload(value):
    return backport.getNiceNumberFormat(round(value, 1))


def _getResAvailable(resPath, parameter):
    resId = resPath.dyn(parameter)
    if resId.exists():
        return parameter
    return b'param_not_found'


FORMAT_SETTINGS = {b'relativePower': _integralFormat, b'damage': _niceRangeFormat, 
   DISTANCE_DAMAGE_PROP_NAME: _niceRangeFormat, 
   b'piercingPower': _niceRangeFormat, 
   b'reloadTime': _niceRangeFormat, 
   b'reloadTimeSecs': _niceListFormat, 
   RELOAD_TIME_PER_SECOND: _niceFormat, 
   b'turretRotationSpeed': _niceListFormat, 
   b'turretYawLimits': _niceListFormat, 
   b'gunYawLimits': _niceListFormat, 
   b'pitchLimits': _niceListFormat, 
   b'clipFireRate': _niceListFormat, 
   BURST_FIRE_RATE: _niceListFormat, 
   BURST_TIME_INTERVAL: _niceFormat, 
   BURST_COUNT: _integralFormat, 
   BURST_SIZE: _integralFormat, 
   b'flameMaxDistance': _niceListFormat, 
   b'turboshaftBurstFireRate': _niceListFormat, 
   b'aimingTime': _niceListFormat, 
   b'avgDamagePerMinute': _niceFormat, 
   b'avgDamagePerSecond': _niceFormat, 
   b'relativeArmor': _integralFormat, 
   b'avgDamage': _niceFormat, 
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
   b'shellsBurstCount': _niceListFormat, 
   b'shellsFlameBurstCount': _niceListFormat, 
   b'shellReloadingTime': _niceRangeFormat, 
   b'reloadMagazineTime': _niceRangeFormat, 
   b'avgPiercingPower': _listFormat, 
   b'damagePerSecond': _integralFormat, 
   b'avgDamageList': _listFormat, 
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
   b'stunMaxDurationList': _niceListFormat, 
   b'cooldownSeconds': _niceFormat, 
   b'cooldown': _niceFormat, 
   b'activeSeconds': _niceFormat, 
   AUTO_RELOAD_PROP_NAME: {b'preprocessor': _autoReloadPreprocessor, b'rounder': _getRoundReload}, MAX_STEERING_LOCK_ANGLE: _niceFormat, 
   WHEELED_SWITCH_ON_TIME: _niceFormat, 
   WHEELED_SWITCH_OFF_TIME: _niceFormat, 
   WHEELED_SWITCH_TIME: _niceListFormat, 
   WHEELED_SPEED_MODE_SPEED: _niceListFormat, 
   DUAL_GUN_CHARGE_TIME: _niceListFormat, 
   DUAL_GUN_RATE_TIME: _niceListFormat, 
   DUAL_ACCURACY_COOLING_DELAY: _niceFormat, 
   b'shotSpeed': _integralFormat, 
   b'shotSpeedAccelerated': _integralRangeFormat, 
   b'extraRepairSpeed': _percentFormat, 
   TURBOSHAFT_SPEED_MODE_SPEED: _niceListFormat, 
   ROCKET_ACCELERATION_SPEED_LIMITS: _niceListFormat, 
   ROCKET_ACCELERATION_REUSE_AND_DURATION: _niceListFormat, 
   THERMAL_VISION_REUSE_AND_DURATION: _niceListFormat, 
   THERMAL_VISION_DISTANCE: _niceFormat, 
   THERMAL_VISION_RELOAD_TIME: _niceFormat, 
   THERMAL_VISION_OBSERVE_TIME: _niceFormat, 
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
   b'vehicleGunShotStabilizationChassisMovement': _percentFormat, 
   b'vehicleGunShotStabilizationChassisRotation': _percentFormat, 
   b'reuseCount': _niceFormat, 
   (KPI.Name.VEHICLE_GUN_AND_GUN_CLIP_COOLDOWN): _niceListFormat, 
   AUTOSHOOT_FLAME_CHANGE_SHELL_TIME: _niceFormat, 
   AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME: _niceFormat, 
   AUTOSHOOT_FIRE_UNTIL_OVERHEAT_TIME: _niceFormat, 
   (KPI.Name.TEMPERATURE_HEATING_TIME): _niceListFormat, 
   (KPI.Name.TEMPERATURE_COOLING_TIME): _niceListFormat, 
   (KPI.Name.TEMPERATURE_COOLING_DELAY): _niceListFormat}

def _deltaWrapper(fn):

    def wrapped(paramValue):
        formattedValue = fn(paramValue)
        if formattedValue == b'0':
            return _EQUAL_TO_ZERO_LITERAL
        if isinstance(paramValue, (int, float)) and paramValue > 0:
            return b'+%s' % formattedValue
        return formattedValue

    return wrapped


def _getDeltaSettings():
    detlaSettings = {}
    for paramName, setting in FORMAT_SETTINGS.iteritems():
        settingCopy = setting.copy()
        rounder = settingCopy[b'rounder']
        settingCopy[b'rounder'] = _deltaWrapper(rounder)
        detlaSettings[paramName] = settingCopy

    return detlaSettings


DELTA_PARAMS_SETTING = _getDeltaSettings()
_SMART_ROUND_PARAMS = (
 b'damage', b'piercingPower', b'bombDamage', b'shellsCount', b'shellReloadingTime',
 b'reloadMagazineTime', b'reloadTime', DISPERSION_RADIUS, b'aimingTime', b'weight',
 DUAL_GUN_RATE_TIME, DUAL_GUN_CHARGE_TIME, b'crewRolesFactor')
_STATES_INDEX_IN_COLOR_MAP = {(PARAM_STATE.WORSE): 0, (PARAM_STATE.NORMAL): 1, (PARAM_STATE.BETTER): 2, (PARAM_STATE.NOT_APPLICABLE): 1}

def colorize(paramStr, state, colorScheme):
    if isinstance(state, (tuple, list)):
        stateType, _ = state
    else:
        stateType = state
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
    doSmartRound = allowSmartRound and parameterName in _SMART_ROUND_PARAMS
    preprocessor = settings.get(b'preprocessor')
    if KPI.Name.hasValue(parameterName):
        formatter, separator, addEnding = KPI_FORMATTERS.get(parameterName, _kpiNoSignValue)
        values = formatter(parameterName, paramValue, addEnding)
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
                params = zip(values, parameterState)
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
    isVehicleDescr = vehicles.isVehicleDescr(descriptor)
    if isVehicleDescr:
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
                if isVehicleDescr:
                    paramName = getFormattedParamName(descriptor, paramName)
                params.append((paramName, fmtValue))

    return params


def getBonusIconRes(bonusId, bonusType, archetype=None):
    if bonusType == BonusTypes.PAIR_MODIFICATION:
        mod = vehicles.g_cache.postProgression().getModificationByName(bonusId)
        if mod is not None:
            iconR = R.images.gui.maps.icons.vehPostProgression.actionItems.pairModifications.c_24x24.dyn(mod.imgName, R.invalid)()
        else:
            iconR = R.invalid()
    elif bonusType == BonusTypes.BATTLE_MODIFIERS:
        if archetype:
            iconR = R.images.gui.maps.icons.vehParams.tooltips.bonuses.dyn(archetype, R.invalid)()
        else:
            iconR = R.images.gui.maps.icons.vehParams.tooltips.bonuses.battleModifiers()
    elif bonusId.find(b'Rammer') >= 0 and bonusId != b'deluxRammer' and bonusId.find(b'modernizedTankRammerSights') == -1 and bonusId.find(b'trophy') == -1:
        iconR = R.images.gui.maps.icons.vehParams.tooltips.bonuses.rammer()
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


def getAllParametersTitles():
    result = []
    for groupName in RELATIVE_PARAMS_WITHOUT_ABILITY:
        data = getCommonParam(HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_SIMPLE_TOP, groupName)
        data[b'titleText'] = formatVehicleParamName(groupName)
        data[b'isEnabled'] = True
        data[b'tooltip'] = TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS
        result.append(data)
        for paramName in PARAMS_GROUPS[groupName]:
            data = getCommonParam(HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_ADVANCED, paramName, groupName)
            data[b'iconSource'] = getParameterSmallIconPath(paramName)
            data[b'titleText'] = formatVehicleParamName(paramName)
            data[b'isEnabled'] = False
            data[b'tooltip'] = TOOLTIPS_CONSTANTS.BASE_VEHICLE_PARAMETERS
            result.append(data)

    return result


def _cutDigits(value):
    if abs(value) > 99:
        return round(value)
    if abs(value) > 9:
        return round(value, 1)
    return round(value, 2)
