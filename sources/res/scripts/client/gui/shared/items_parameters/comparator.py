import collections, sys, typing
from constants import BonusTypes
from gui.shared.gui_items import KPI
from gui.shared.items_parameters import params_cache
from shared_utils import first
from gui.shared.utils import WHEELED_SWITCH_ON_TIME, WHEELED_SWITCH_OFF_TIME, DUAL_GUN_CHARGE_TIME, SHOT_DISPERSION_ANGLE, TURBOSHAFT_INVISIBILITY_STILL_FACTOR, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, DISPERSION_RADIUS, CHASSIS_REPAIR_TIME, TURBOSHAFT_SWITCH_TIME, DUAL_GUN_RATE_TIME, DUAL_ACCURACY_COOLING_DELAY, BURST_FIRE_RATE, BURST_TIME_INTERVAL, AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME, AUTOSHOOT_FLAME_CHANGE_SHELL_TIME, THERMAL_VISION_OBSERVE_TIME, THERMAL_VISION_RELOAD_TIME
if typing.TYPE_CHECKING:
    from gui.shared.items_parameters.params import _PenaltyInfo
BACKWARD_QUALITY_PARAMS = frozenset([
 b'aimingTime',
 b'autoReloadTime',
 DISPERSION_RADIUS,
 b'fireStartingChance',
 b'reloadMagazineTime',
 b'reloadTimeSecs',
 b'shellReloadingTime',
 SHOT_DISPERSION_ANGLE,
 b'weight',
 b'turboshaftBurstFireRate',
 BURST_FIRE_RATE,
 BURST_TIME_INTERVAL,
 b'switchOnTime',
 b'switchOffTime',
 CHASSIS_REPAIR_TIME,
 DUAL_GUN_CHARGE_TIME,
 KPI.Name.CREW_STUN_DURATION,
 KPI.Name.CREW_STUN_RESISTANCE,
 KPI.Name.DAMAGE_AND_PIERCING_DISTRIBUTION_UPPER_BOUND,
 KPI.Name.DEMASK_FOLIAGE_FACTOR,
 KPI.Name.DEMASK_MOVING_FACTOR,
 KPI.Name.EQUIPMENT_PREPARATION_TIME,
 KPI.Name.STUN_RESISTANCE_EFFECT_FACTOR,
 KPI.Name.VEHICLE_CHASSIS_FALL_DAMAGE,
 KPI.Name.VEHICLE_FIRE_CHANCE,
 KPI.Name.VEHICLE_GUN_RELOAD_TIME,
 KPI.Name.VEHICLE_GUN_SHOT_DISPERSION,
 KPI.Name.VEHICLE_GUN_SHOT_DISPERSION_AFTER_SHOT,
 KPI.Name.VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_MOVEMENT,
 KPI.Name.VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_ROTATION,
 KPI.Name.VEHICLE_GUN_SHOT_DISPERSION_TURRET_ROTATION,
 KPI.Name.VEHICLE_GUN_SHOT_DISPERSION_WHILE_GUN_DAMAGED,
 KPI.Name.VEHICLE_GUN_SHOT_FULL_DISPERSION,
 KPI.Name.VEHICLE_GUN_DAMAGE,
 KPI.Name.VEHICLE_OWN_SPOTTING_TIME,
 KPI.Name.VEHICLE_PENALTY_FOR_DAMAGED_ENGINE_AND_COMBAT,
 KPI.Name.VEHICLE_RAM_DAMAGE_RESISTANCE,
 KPI.Name.VEHICLE_RAM_OR_EXPLOSION_DAMAGE_RESISTANCE,
 KPI.Name.VEHICLE_FUEL_TANK_LESION_CHANCE,
 WHEELED_SWITCH_OFF_TIME,
 WHEELED_SWITCH_ON_TIME,
 TURBOSHAFT_SWITCH_TIME,
 KPI.Name.TRACK_RAMMING_DAMAGE_FACTOR,
 KPI.Name.WOUNDED_CREW_EFFICIENCY,
 DUAL_GUN_RATE_TIME,
 DUAL_ACCURACY_COOLING_DELAY,
 KPI.Name.ART_NOTIFICATION_DELAY_FACTOR,
 KPI.Name.DAMAGED_MODULES_DETECTION_TIME,
 AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME,
 AUTOSHOOT_FLAME_CHANGE_SHELL_TIME,
 KPI.Name.TEMPERATURE_COOLING_TIME,
 KPI.Name.TEMPERATURE_COOLING_DELAY,
 THERMAL_VISION_OBSERVE_TIME,
 THERMAL_VISION_RELOAD_TIME,
 b'vehicleWeight'])
PARAMS_WITH_BATTLE_MODIFIERS = {b'maxHealth': {
                b'vehicleHealth'}, 
   b'reloadTime': {
                 b'reloadTime'}, 
   b'reloadTimeSecs': {
                     b'reloadTime'}, 
   b'autoReloadTime': {
                     b'autoReloadTime'}, 
   b'avgDamagePerMinute': {
                         b'reloadTime', b'autoReloadTime'}, 
   b'clipFireRate': {
                   b'reloadTime', b'autoReloadTime'}}
NEGATIVE_PARAMS = [
 b'switchOnTime', b'switchOffTime', CHASSIS_REPAIR_TIME]
NOT_COMPARABLE_PARAMS = [
 KPI.Name.TEMPERATURE_STATES_COUNT]
PARAMS_WITH_IGNORED_EMPTY_VALUES = {
 SHOT_DISPERSION_ANGLE, DISPERSION_RADIUS, CHASSIS_REPAIR_TIME}

def normalizeShotDispersionValue(value):
    if len(value) == 1:
        return [None] + value
    else:
        return value


def normalizeChassisRepairTime(value):
    if len(value) == 1:
        return [None] + value
    else:
        return sorted(value, key=(lambda x: (
         x is None, x)), reverse=True)


PARAMS_NORMALIZATION_MAP = {SHOT_DISPERSION_ANGLE: normalizeShotDispersionValue, 
   CHASSIS_REPAIR_TIME: normalizeChassisRepairTime}
_CUSTOM_QUALITY_PARAMS = {b'clipFireRate': (
                   True, True, False), 
   BURST_FIRE_RATE: (
                   True, False, False), 
   b'turboshaftBurstFireRate': (
                              True, False, False), 
   b'pitchLimits': (
                  True, False)}

class PARAM_STATE(object):
    WORSE = b'worse'
    NORMAL = b'normal'
    BETTER = b'better'
    NOT_APPLICABLE = b'N/A'


DEFAULT_AVG_VALUE = (
 sys.maxint, -1)

def getParamExtendedData(paramName, value, otherValue, penalties=None, customQualityParams=None, isSituational=False, hasNormalization=False):
    possibleBonuses, bonuses, inactive, penalties = penalties if penalties is not None else ([], [], [], [])
    if paramName not in NEGATIVE_PARAMS:
        if otherValue is None or otherValue == DEFAULT_AVG_VALUE:
            otherValue = value
    if hasNormalization and paramName in PARAMS_NORMALIZATION_MAP:
        func = PARAMS_NORMALIZATION_MAP[paramName]
        value = func(value)
        otherValue = func(otherValue)
    return _ParameterInfo(paramName, value, rateParameterState(paramName, value, otherValue, customQualityParams=customQualityParams), possibleBonuses, inactive, bonuses, penalties, isSituational)


class ItemsComparator(object):

    def __init__(self, currentParams, otherParams):
        super(ItemsComparator, self).__init__()
        self._currentParams = currentParams
        self._otherParams = otherParams
        return

    def getAllDifferentParams(self):
        result = []
        for paramName in self._currentParams.keys():
            data = self.getExtendedData(paramName)
            if data.state[0] != PARAM_STATE.NORMAL:
                result.append(data)

        return result

    def getExtendedData(self, paramName, hasNormalization=False):
        return getParamExtendedData(paramName, self._currentParams.get(paramName), self._otherParams.get(paramName), self._getPenaltiesAndBonuses(paramName), hasNormalization=hasNormalization)

    def getPenalties(self, _):
        return []

    def _getPenaltiesAndBonuses(self, _):
        return ([], [], {}, [])


class VehiclesComparator(ItemsComparator):

    def __init__(self, currentVehicleParams, otherVehicleParams, suitableArtefacts=None, bonuses=None, penalties=None):
        super(VehiclesComparator, self).__init__(currentVehicleParams, otherVehicleParams)
        self.__suitableArtefacts = set(suitableArtefacts or set())
        self.__bonuses = bonuses or set()
        self.__penalties = penalties or dict()
        return

    def hasBonusOfType(self, bnsType):
        return any(i == bnsType for _, i in self.__bonuses)

    def getPenalties(self, paramName):
        return self.__penalties.get(paramName, [])

    def _getPenaltiesAndBonuses(self, paramName):
        penalties = self.__penalties.get(paramName, [])
        allPossibleParamBonuses = self.__getPossibleParamBonuses(paramName)
        currentParamBonuses, inactive = self.__getCurrentParamBonuses(paramName, allPossibleParamBonuses)
        currentParamBonuses = currentParamBonuses.union(self.__getBattleModifierBonuses(paramName))
        possibleBonuses = allPossibleParamBonuses - currentParamBonuses
        return (possibleBonuses, currentParamBonuses, inactive, penalties)

    def __getPossibleParamBonuses(self, paramName):
        paramBonuses = params_cache.g_paramsCache.getBonuses().get(paramName, [])
        allPossibleParamBonuses = set()
        for bonusName, bonusGroup in paramBonuses:
            if (
             bonusName, bonusGroup) in self.__suitableArtefacts or bonusGroup in BonusTypes.POSSIBLE:
                allPossibleParamBonuses.add((bonusName, bonusGroup))

        return allPossibleParamBonuses

    def __getCurrentParamBonuses(self, paramName, possibleBonuses):
        if paramName in CONDITIONAL_BONUSES:
            return self.__getConditionalBonuses(paramName, possibleBonuses)
        result = possibleBonuses.intersection(self.__bonuses)
        return (
         result, {})

    def __getConditionalBonuses(self, paramName, possibleBonuses):
        currentBonuses, affectedBonuses = set(), {}
        bonuses = possibleBonuses.intersection(self.__bonuses)
        for bonus in bonuses:
            unmatchedDependency = self.__getUnmatchedDependency(paramName, bonuses, bonus)
            if unmatchedDependency is None:
                currentBonuses.add(bonus)
            else:
                affectedBonuses[bonus] = unmatchedDependency

        return (
         currentBonuses, affectedBonuses)

    def __getBattleModifierBonuses(self, paramName):
        result = set()
        suitableBattleModifiers = PARAMS_WITH_BATTLE_MODIFIERS.get(paramName, set())
        for bonusName, bonusGroup in self.__bonuses:
            if bonusGroup == BonusTypes.BATTLE_MODIFIERS and bonusName in suitableBattleModifiers:
                result.add((bonusName, bonusGroup))
                return result

        return result

    def __getUnmatchedDependency(self, paramName, activeBonuses, bonus):
        dependencies = CONDITIONAL_BONUSES[paramName].get(bonus, ())
        unmatchedDependencies = []
        for dependency in dependencies:
            unmatchedDependency = self.__getUnmatchedDependency(paramName, activeBonuses, dependency)
            if unmatchedDependency is not None and unmatchedDependency not in activeBonuses and bonus not in NOT_HARD_DEPENDENCY:
                unmatchedDependencies.append(unmatchedDependency)

        unmatchedDependency = first(unmatchedDependencies) if len(unmatchedDependencies) == len(dependencies) else None
        if bonus not in activeBonuses:
            unmatchedDependency = unmatchedDependency or bonus
        return unmatchedDependency


class _ParameterInfo(collections.namedtuple(b'_ParameterInfo', (b'name', b'value', b'state', b'possibleBonuses',
 b'inactiveBonuses', b'bonuses', b'penalties', b'isSituational'))):

    def getParamDiff(self):
        if isinstance(self.value, (tuple, list)):
            diff = [d for _, d in self.state if d is not None]
            if diff:
                return diff
        else:
            _, diff = self.state
            if diff is not None:
                return diff
        return


CONDITIONAL_BONUSES = {(b'invisibilityMovingFactor', b'invisibilityStillFactor', TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_INVISIBILITY_STILL_FACTOR): {((b'brotherhood', BonusTypes.SKILL), (b'chocolate', BonusTypes.EQUIPMENT), (b'cocacola', BonusTypes.EQUIPMENT), (b'ration', BonusTypes.EQUIPMENT), (b'hotCoffee', BonusTypes.EQUIPMENT), (b'ration_china', BonusTypes.EQUIPMENT), (b'ration_uk', BonusTypes.EQUIPMENT), (b'ration_japan', BonusTypes.EQUIPMENT), (b'ration_czech', BonusTypes.EQUIPMENT), (b'ration_sweden', BonusTypes.EQUIPMENT), (b'ration_poland', BonusTypes.EQUIPMENT), (b'ration_italy', BonusTypes.EQUIPMENT), (b'ration_intunion', BonusTypes.EQUIPMENT), (b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE), (b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE), (b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE), (b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE), (b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE), (b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE), (b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE), (b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE), (b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)): (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 b'camouflage', BonusTypes.SKILL),), 
                                                                                                                                            ((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                (
                                                                                                                                                                                                                 b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                                                                                                                                            ((b'additInvisibilityDeviceBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                     b'additionalInvisibilityDevice_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                     b'additionalInvisibilityDevice_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                     b'additionalInvisibilityDevice_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                     b'trophyBasicAdditionalInvisibilityDevice', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                                                                    (
                                                                                                                                                                                                                     b'trophyUpgradedAdditionalInvisibilityDevice', BonusTypes.OPTIONAL_DEVICE))}, 
   (CHASSIS_REPAIR_TIME,): {((b'brotherhood', BonusTypes.SKILL), (b'chocolate', BonusTypes.EQUIPMENT), (b'cocacola', BonusTypes.EQUIPMENT), (b'ration', BonusTypes.EQUIPMENT), (b'hotCoffee', BonusTypes.EQUIPMENT), (b'ration_china', BonusTypes.EQUIPMENT), (b'ration_uk', BonusTypes.EQUIPMENT), (b'ration_japan', BonusTypes.EQUIPMENT), (b'ration_czech', BonusTypes.EQUIPMENT), (b'ration_sweden', BonusTypes.EQUIPMENT), (b'ration_poland', BonusTypes.EQUIPMENT), (b'ration_italy', BonusTypes.EQUIPMENT), (b'ration_intunion', BonusTypes.EQUIPMENT), (b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE), (b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE), (b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE), (b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE), (b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE), (b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE), (b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE), (b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE), (b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)): (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 b'repair', BonusTypes.SKILL),), 
                            ((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                (
                                                                                                 b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                (
                                                                                                 b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                            ((b'improvedConfigurationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                  (
                                                                                                   b'improvedConfiguration_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                  (
                                                                                                   b'improvedConfiguration_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                  (
                                                                                                   b'deluxImprovedConfiguration', BonusTypes.OPTIONAL_DEVICE),
                                                                                                  (
                                                                                                   b'trophyBasicImprovedConfiguration', BonusTypes.OPTIONAL_DEVICE),
                                                                                                  (
                                                                                                   b'trophyUpgradedImprovedConfiguration', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'reloadTime', b'reloadTimeSecs', b'avgDamagePerMinute', AUTOSHOOT_FLAME_CHANGE_SHELL_TIME): {((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                                                      (
                                                                                                                                                                       b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                      (
                                                                                                                                                                       b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                                                                                                  ((b'rammerBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                                         (
                                                                                                                                                          b'tankRammer_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'tankRammer_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'tankRammer_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'deluxRammer', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'trophyBasicTankRammer', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'trophyUpgradedTankRammer', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'modernizedTankRammerSights1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'modernizedTankRammerSights2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                         (
                                                                                                                                                          b'modernizedTankRammerSights3', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'clipFireRate', b'autoReloadTime', b'dualAccuracyCoolingDelay'): {((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                           (
                                                                                                                                            b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                           (
                                                                                                                                            b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'circularVisionRadius',): {((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                    (
                                                                                                     b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                                ((b'coatedOpticsBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                             (
                                                                                              b'coatedOptics_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                             (
                                                                                              b'coatedOptics_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                             (
                                                                                              b'coatedOptics_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                             (
                                                                                              b'deluxCoatedOptics', BonusTypes.OPTIONAL_DEVICE),
                                                                                             (
                                                                                              b'trophyBasicCoatedOptics', BonusTypes.OPTIONAL_DEVICE),
                                                                                             (
                                                                                              b'trophyUpgradedCoatedOptics', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'shotDispersionAngle',): {((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                   (
                                                                                                    b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                   (
                                                                                                    b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                               ((b'improvedSightsBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                              (
                                                                                               b'improvedSights_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'improvedSights_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'improvedSights_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'deluxeImprovedSights', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'trophyBasicImprovedSights', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'trophyUpgradedImprovedSights', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'modernizedTankRammerSights1', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'modernizedTankRammerSights2', BonusTypes.OPTIONAL_DEVICE),
                                                                                              (
                                                                                               b'modernizedTankRammerSights3', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'aimingTime',): {((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                          (
                                                                                           b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                          (
                                                                                           b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                      ((b'enhancedAimDrivesBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                        (
                                                                                         b'enhancedAimDrives_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'enhancedAimDrives_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'enhancedAimDrives_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'deluxEnhancedAimDrives', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'trophyBasicAimDrives', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'trophyUpgradedAimDrives', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'modernizedAimDrivesAimingStabilizer1', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'modernizedAimDrivesAimingStabilizer2', BonusTypes.OPTIONAL_DEVICE),
                                                                                        (
                                                                                         b'modernizedAimDrivesAimingStabilizer3', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'turretRotationSpeed', b'chassisRotationSpeed', b'radioDistance'): {((b'improvedVentilationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                             (
                                                                                                                                              b'improvedVentilation_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'improvedVentilation_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'improvedVentilation_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'deluxImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'trophyBasicImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'trophyUpgradedImprovedVentilation', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                             (
                                                                                                                                              b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE)), 
                                                                         ((b'driver_virtuoso', BonusTypes.SKILL),): (
                                                                                                                   (
                                                                                                                    b'brotherhood', BonusTypes.SKILL),)}, 
   (b'enginePower', b'rocketAccelerationEnginePower', b'enginePowerPerTon', b'turboshaftEnginePower'): {((b'turbochargerBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                                                                                     (
                                                                                                                                                                      b'turbocharger_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'turbocharger_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'turbocharger_tier3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'modernizedTurbochargerRotationMechanism1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'modernizedTurbochargerRotationMechanism2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'modernizedTurbochargerRotationMechanism3', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'deluxeTurbocharger', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'trophyBasicTurbocharger', BonusTypes.OPTIONAL_DEVICE),
                                                                                                                                                                     (
                                                                                                                                                                      b'trophyUpgradedTurbocharger', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'vehicleRepairSpeed',): {((b'improvedConfigurationBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                    (
                                                                                                     b'improvedConfiguration_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'improvedConfiguration_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'deluxImprovedConfiguration', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'trophyBasicImprovedConfiguration', BonusTypes.OPTIONAL_DEVICE),
                                                                                                    (
                                                                                                     b'trophyUpgradedImprovedConfiguration', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'vehicleGunShotDispersion',): {((b'aimingStabilizerBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                                     (
                                                                                                      b'aimingStabilizer_tier1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'aimingStabilizer_tier2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'deluxAimingStabilizer', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'trophyBasicAimingStabilizer', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'trophyUpgradedAimingStabilizer', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'modernizedAimDrivesAimingStabilizer1', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'modernizedAimDrivesAimingStabilizer2', BonusTypes.OPTIONAL_DEVICE),
                                                                                                     (
                                                                                                      b'modernizedAimDrivesAimingStabilizer3', BonusTypes.OPTIONAL_DEVICE))}, 
   (b'fireExtinguishingRate',): {((b'fireFightingBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                              (
                                                                                               b'fireFighting', BonusTypes.SKILL),)}, 
   (b'wheelsRotationSpeed',): {((b'virtuosoBattleBooster', BonusTypes.BATTLE_BOOSTER),): (
                                                                                        (
                                                                                         b'driver_virtuoso', BonusTypes.SKILL),)}, 
   (b'avgDamage',): {((),): (
                           (
                            b'modernizedDamageVentilation1', BonusTypes.OPTIONAL_DEVICE),
                           (
                            b'modernizedDamageVentilation2', BonusTypes.OPTIONAL_DEVICE),
                           (
                            b'modernizedDamageVentilation3', BonusTypes.OPTIONAL_DEVICE))}}
CONDITIONAL_BONUSES = {k: {k1: v1 for k1 in values.iteritems()} for k in CONDITIONAL_BONUSES.items()}
NOT_HARD_DEPENDENCY = {
 (
  b'driver_virtuoso', BonusTypes.SKILL),
 (
  b'fireFightingBattleBooster', BonusTypes.BATTLE_BOOSTER),
 (
  b'virtuosoBattleBooster', BonusTypes.BATTLE_BOOSTER)}

def _getComparableValue(currentValue, comparableList, idx):
    if len(comparableList) > idx:
        return comparableList[idx]
    return currentValue


PARAM_STATE_ROUND_DIGITS = 6

def _getParamStateInfo(paramName, val1, val2, customReverted=False):
    if paramName in NOT_COMPARABLE_PARAMS:
        return (PARAM_STATE.NORMAL, 0)
    else:
        if val1 is None or val2 is None:
            hasNoParam = True
            diff = 0
        else:
            hasNoParam = False
            if isinstance(val1, float) and isinstance(val2, float):
                diff = val1 - val2
                diff = round(diff, PARAM_STATE_ROUND_DIGITS)
            elif isinstance(val1, float):
                val1 = round(val1, PARAM_STATE_ROUND_DIGITS)
            if isinstance(val2, float):
                val2 = round(val2, PARAM_STATE_ROUND_DIGITS)
            diff = val1 - val2
        if paramName in NEGATIVE_PARAMS and hasNoParam:
            if val1 is None and val2 is None:
                return (PARAM_STATE.NORMAL, diff)
            if val1 is None:
                return (PARAM_STATE.BETTER, diff)
            return (PARAM_STATE.WORSE, diff)
        if diff == 0:
            if hasNoParam and paramName in PARAMS_WITH_IGNORED_EMPTY_VALUES:
                return (PARAM_STATE.NOT_APPLICABLE, diff)
            return (PARAM_STATE.NORMAL, diff)
        isInverted = paramName in BACKWARD_QUALITY_PARAMS or customReverted
        if isInverted and diff > 0 or not isInverted and diff < 0:
            return (PARAM_STATE.WORSE, diff)
        return (
         PARAM_STATE.BETTER, diff)


def rateParameterState(paramName, val1, val2, customQualityParams=None):
    if isinstance(val1, (tuple, list)):
        if customQualityParams is None:
            customQualityParams = _CUSTOM_QUALITY_PARAMS.get(paramName)
        customQualityLen = len(customQualityParams) if customQualityParams else 0
        result = []
        val2Len = len(val2) if isinstance(val2, (tuple, list)) else 0
        for i, val in enumerate(val1):
            if val2Len == 0:
                result.append((PARAM_STATE.NORMAL, None))
                continue
            if val2Len > i:
                val2ToCompare = val2[i]
            else:
                result.append((PARAM_STATE.NOT_APPLICABLE, None))
                continue
            if customQualityParams is not None:
                customQuality = customQualityParams[min(i, customQualityLen - 1)]
            else:
                customQuality = None
            result.append(rateParameterState(paramName, val, val2ToCompare, customQuality))

        return tuple(result)
    else:
        return _getParamStateInfo(paramName, val1, val2, customQualityParams)
