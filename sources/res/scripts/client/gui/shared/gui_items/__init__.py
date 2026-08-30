from __future__ import absolute_import
import logging
from future.utils import viewitems, viewvalues
from typing import TYPE_CHECKING
from gui.impl import backport
from gui.impl.backport import getNiceNumberFormat
from gui.impl.gen import R
from gui.shared.items_parameters.param_name_helper import getVehicleParameterText
from shared_utils import CONST_CONTAINER
from items import ITEM_TYPE_NAMES, vehicles, ITEM_TYPE_INDICES, EQUIPMENT_TYPES, getTypeOfCompactDescr
from gui.shared.money import Currency
from skeletons.gui.shared.gui_items import IGuiItemsFactory
from helpers import dependency
if TYPE_CHECKING:
    from typing import Set, FrozenSet, Union
_logger = logging.getLogger(__name__)
CLAN_LOCK = 1
GUI_ITEM_TYPE_NAMES = tuple(ITEM_TYPE_NAMES) + tuple([b'reserved'] * (16 - len(ITEM_TYPE_NAMES)))
GUI_ITEM_TYPE_NAMES += (b'dossierAccount', b'dossierVehicle', b'dossierTankman', b'achievement', b'tankmanSkill', b'battleBooster', b'badge', b'battleAbility', b'lootBox', b'demountKit', b'vehPostProgression', b'recertificationForm', b'mentoringLicense', b'paint', b'camouflage', b'modification', b'outfit', b'style', b'decal', b'emblem', b'inscription', b'projectionDecal', b'insignia', b'personalNumber', b'sequence', b'attachment', b'statTracker', b'vehicleMechanic', b'moduleMechanic', b'shellMechanic')
GUI_ITEM_TYPE_INDICES = {n: idx for idx, n in enumerate(GUI_ITEM_TYPE_NAMES)}

class GUI_ITEM_TYPE(CONST_CONTAINER):
    VEHICLE = GUI_ITEM_TYPE_INDICES[b'vehicle']
    CHASSIS = GUI_ITEM_TYPE_INDICES[b'vehicleChassis']
    TURRET = GUI_ITEM_TYPE_INDICES[b'vehicleTurret']
    GUN = GUI_ITEM_TYPE_INDICES[b'vehicleGun']
    ENGINE = GUI_ITEM_TYPE_INDICES[b'vehicleEngine']
    FUEL_TANK = GUI_ITEM_TYPE_INDICES[b'vehicleFuelTank']
    RADIO = GUI_ITEM_TYPE_INDICES[b'vehicleRadio']
    TANKMAN = GUI_ITEM_TYPE_INDICES[b'tankman']
    OPTIONALDEVICE = GUI_ITEM_TYPE_INDICES[b'optionalDevice']
    SHELL = GUI_ITEM_TYPE_INDICES[b'shell']
    EQUIPMENT = GUI_ITEM_TYPE_INDICES[b'equipment']
    BATTLE_ABILITY = GUI_ITEM_TYPE_INDICES[b'battleAbility']
    MODULE_MECHANIC = GUI_ITEM_TYPE_INDICES[b'moduleMechanic']
    VEHICLE_MECHANIC = GUI_ITEM_TYPE_INDICES[b'vehicleMechanic']
    CUSTOMIZATION = GUI_ITEM_TYPE_INDICES[b'customizationItem']
    CREW_SKINS = GUI_ITEM_TYPE_INDICES[b'crewSkin']
    CREW_BOOKS = GUI_ITEM_TYPE_INDICES[b'crewBook']
    PAINT = GUI_ITEM_TYPE_INDICES[b'paint']
    CAMOUFLAGE = GUI_ITEM_TYPE_INDICES[b'camouflage']
    MODIFICATION = GUI_ITEM_TYPE_INDICES[b'modification']
    DECAL = GUI_ITEM_TYPE_INDICES[b'decal']
    EMBLEM = GUI_ITEM_TYPE_INDICES[b'emblem']
    INSCRIPTION = GUI_ITEM_TYPE_INDICES[b'inscription']
    OUTFIT = GUI_ITEM_TYPE_INDICES[b'outfit']
    STYLE = GUI_ITEM_TYPE_INDICES[b'style']
    PROJECTION_DECAL = GUI_ITEM_TYPE_INDICES[b'projectionDecal']
    INSIGNIA = GUI_ITEM_TYPE_INDICES[b'insignia']
    PERSONAL_NUMBER = GUI_ITEM_TYPE_INDICES[b'personalNumber']
    SEQUENCE = GUI_ITEM_TYPE_INDICES[b'sequence']
    ATTACHMENT = GUI_ITEM_TYPE_INDICES[b'attachment']
    STAT_TRACKER = GUI_ITEM_TYPE_INDICES[b'statTracker']
    DEMOUNT_KIT = GUI_ITEM_TYPE_INDICES[b'demountKit']
    RECERTIFICATION_FORM = GUI_ITEM_TYPE_INDICES[b'recertificationForm']
    MENTORING_LICENSE = GUI_ITEM_TYPE_INDICES[b'mentoringLicense']
    COMMON = tuple(ITEM_TYPE_INDICES.keys())
    BATTLE_BOOSTER = GUI_ITEM_TYPE_INDICES[b'battleBooster']
    ARTEFACTS = (
     EQUIPMENT, OPTIONALDEVICE, BATTLE_BOOSTER)
    ACCOUNT_DOSSIER = GUI_ITEM_TYPE_INDICES[b'dossierAccount']
    VEHICLE_DOSSIER = GUI_ITEM_TYPE_INDICES[b'dossierVehicle']
    TANKMAN_DOSSIER = GUI_ITEM_TYPE_INDICES[b'dossierTankman']
    ACHIEVEMENT = GUI_ITEM_TYPE_INDICES[b'achievement']
    SKILL = GUI_ITEM_TYPE_INDICES[b'tankmanSkill']
    BADGE = GUI_ITEM_TYPE_INDICES[b'badge']
    LOOT_BOX = GUI_ITEM_TYPE_INDICES[b'lootBox']
    VEH_POST_PROGRESSION = GUI_ITEM_TYPE_INDICES[b'vehPostProgression']
    GUI = (
     ACCOUNT_DOSSIER, VEHICLE_DOSSIER, TANKMAN_DOSSIER,
     ACHIEVEMENT, SKILL, BADGE)
    VEHICLE_MODULES = (
     GUN, TURRET, ENGINE, CHASSIS, RADIO)
    VEHICLE_COMPONENTS = VEHICLE_MODULES + ARTEFACTS + (SHELL,)
    CUSTOMIZATIONS = (
     PAINT, CAMOUFLAGE, MODIFICATION,
     EMBLEM, INSCRIPTION, STYLE, PROJECTION_DECAL,
     PERSONAL_NUMBER, SEQUENCE, ATTACHMENT, STAT_TRACKER)
    CUSTOMIZATIONS_WITHOUT_STYLE = (PAINT, CAMOUFLAGE, MODIFICATION,
     EMBLEM, INSCRIPTION, PROJECTION_DECAL, PERSONAL_NUMBER)
    ATTACHMENT_TYPES = (
     ATTACHMENT, STAT_TRACKER)
    COMMON_C11NS = (
     ATTACHMENT, STAT_TRACKER)
    COMMON_C11N_COMPATIBLE_WITH_3D_STYLES = (STAT_TRACKER,)


def getItemTypeID(bonusName):
    if bonusName in GUI_ITEM_TYPE_INDICES:
        return GUI_ITEM_TYPE_INDICES[bonusName]
    else:
        itemTypeID = None
        if bonusName == b'projection_decal':
            itemTypeID = GUI_ITEM_TYPE.PROJECTION_DECAL
        elif bonusName == b'personal_number':
            itemTypeID = GUI_ITEM_TYPE.PERSONAL_NUMBER
        elif bonusName == b'stat_tracker':
            itemTypeID = GUI_ITEM_TYPE.STAT_TRACKER
        return itemTypeID


def formatMoneyError(currency):
    return (b'{}_error').format(currency)


class GUI_ITEM_ECONOMY_CODE(CONST_CONTAINER):
    UNDEFINED = b''
    CENTER_UNAVAILABLE = b'center_unavailable'
    UNLOCK_ERROR = b'unlock_error'
    ITEM_IS_HIDDEN = b'isHidden'
    ITEM_NO_PRICE = b'noPrice'
    ITEM_IS_DUPLICATED = b'duplicatedItem'
    WALLET_NOT_AVAILABLE = b'wallet_not_available'
    RESTORE_DISABLED = b'restore_disabled'
    NO_RENT_PRICE = b'no_rent_price'
    RENTAL_TIME_EXCEEDED = b'rental_time_exceeded'
    RENTAL_DISABLED = b'rental_disabled'
    NOT_ENOUGH_GOLD = formatMoneyError(Currency.GOLD)
    NOT_ENOUGH_CREDITS = formatMoneyError(Currency.CREDITS)
    NOT_ENOUGH_CRYSTAL = formatMoneyError(Currency.CRYSTAL)
    NOT_ENOUGH_EVENT_COIN = formatMoneyError(Currency.EVENT_COIN)
    NOT_ENOUGH_BPCOIN = formatMoneyError(Currency.BPCOIN)
    NOT_ENOUGH_EQUIP_COIN = formatMoneyError(Currency.EQUIP_COIN)
    NOT_ENOUGH_CURRENCIES = (
     NOT_ENOUGH_GOLD, NOT_ENOUGH_CRYSTAL, NOT_ENOUGH_CREDITS, NOT_ENOUGH_EVENT_COIN, NOT_ENOUGH_BPCOIN,
     NOT_ENOUGH_EQUIP_COIN)
    NOT_ENOUGH_MONEY = b'not_enough_money'

    @classmethod
    def getCurrencyError(cls, currency):
        return formatMoneyError(currency)

    @classmethod
    def isCurrencyError(cls, errCode):
        return errCode in GUI_ITEM_ECONOMY_CODE.NOT_ENOUGH_CURRENCIES


class ItemsCollection(dict):

    def filter(self, criteria):
        result = self.__class__()
        for intCD, item in viewitems(self):
            if criteria(item):
                result.update({intCD: item})

        return result

    def __repr__(self):
        return b'%s<size:%d>' % (self.__class__.__name__, len(self))


def getVehicleComponentsByType(vehicle, itemTypeIdx):

    def packModules(modules):
        if not isinstance(modules, list):
            modules = [
             modules]
        return ItemsCollection([(module.intCD, module) for module in modules if module is not None])

    if itemTypeIdx == vehicles._CHASSIS:
        return packModules(vehicle.chassis)
    if itemTypeIdx == vehicles._TURRET:
        return packModules(vehicle.turret)
    if itemTypeIdx == vehicles._GUN:
        return packModules(vehicle.gun)
    if itemTypeIdx == vehicles._ENGINE:
        return packModules(vehicle.engine)
    if itemTypeIdx == vehicles._FUEL_TANK:
        return packModules(vehicle.fuelTank)
    if itemTypeIdx == vehicles._RADIO:
        return packModules(vehicle.radio)
    if itemTypeIdx == vehicles._TANKMAN:
        from gui.shared.gui_items.Tankman import TankmenCollection
        return TankmenCollection([(t.invID, t) for _, t in vehicle.crew])
    if itemTypeIdx == vehicles._OPTIONALDEVICE:
        return packModules(vehicle.optDevices.installed)
    if itemTypeIdx == vehicles._SHELL:
        return packModules(vehicle.shells.installed)
    if itemTypeIdx == vehicles._EQUIPMENT:
        return ItemsCollection([(eq.intCD, eq) for eq in vehicle.consumables.installed.getItems()])
    return ItemsCollection()


def getVehicleSuitablesByType(vehDescr, itemTypeId, turretPID=0):
    descriptorsList = []
    current = []
    if itemTypeId == vehicles._CHASSIS:
        current = [
         vehDescr.chassis.compactDescr]
        descriptorsList = vehDescr.type.chassis
    elif itemTypeId == vehicles._ENGINE:
        current = [
         vehDescr.engine.compactDescr]
        descriptorsList = vehDescr.type.engines
    elif itemTypeId == vehicles._RADIO:
        current = [
         vehDescr.radio.compactDescr]
        descriptorsList = vehDescr.type.radios
    elif itemTypeId == vehicles._FUEL_TANK:
        current = [
         vehDescr.fuelTank.compactDescr]
        descriptorsList = vehDescr.type.fuelTanks
    elif itemTypeId == vehicles._TURRET:
        current = [
         vehDescr.turret.compactDescr]
        descriptorsList = vehDescr.type.turrets[turretPID]
    elif itemTypeId == vehicles._OPTIONALDEVICE:
        devs = vehicles.g_cache.optionalDevices()
        current = vehDescr.optionalDevices
        descriptorsList = [dev for dev in viewvalues(devs) if dev.checkCompatibilityWithVehicle(vehDescr)[0]]
    elif itemTypeId == vehicles._EQUIPMENT:
        eqs = vehicles.g_cache.equipments()
        current = []
        descriptorsList = [eq for eq in viewvalues(eqs) if eq.checkCompatibilityWithVehicle(vehDescr)[0]]
    elif itemTypeId == GUI_ITEM_TYPE.BATTLE_BOOSTER:
        eqs = vehicles.g_cache.equipments()
        current = []
        descriptorsList = [eq for eq in viewvalues(eqs) if eq.equipmentType == EQUIPMENT_TYPES.battleBoosters and eq.checkCompatibilityWithVehicle(vehDescr)[0]]
    elif itemTypeId == GUI_ITEM_TYPE.BATTLE_ABILITY:
        eqs = vehicles.g_cache.equipments()
        current = []
        descriptorsList = [eq for eq in viewvalues(eqs) if eq.equipmentType == EQUIPMENT_TYPES.battleAbilities and eq.checkCompatibilityWithVehicle(vehDescr)]
    elif itemTypeId == vehicles._GUN:
        current = [
         vehDescr.gun.compactDescr]
        for gun in vehDescr.turret.guns:
            descriptorsList.append(gun)

        for turret in vehDescr.type.turrets[turretPID]:
            if turret is not vehDescr.turret:
                for gun in turret.guns:
                    descriptorsList.append(gun)

    elif itemTypeId == vehicles._SHELL:
        for shot in vehDescr.gun.shots:
            current.append(shot.shell.compactDescr)

        for gun in vehDescr.turret.guns:
            for shot in gun.shots:
                descriptorsList.append(shot.shell)

        for turret in vehDescr.type.turrets[turretPID]:
            if turret is not vehDescr.turret:
                for gun in turret.guns:
                    for shot in gun.shots:
                        descriptorsList.append(shot.shell)

    return (
     descriptorsList, current)


def getItemIconName(itemName):
    return b'%s.png' % itemName.replace(b':', b'-')


def checkForTags(vTags, tags):
    if isinstance(tags, str):
        return tags in vTags
    return not vTags.isdisjoint(tags)


@dependency.replace_none_kwargs(itemsFactory=IGuiItemsFactory)
def isItemVehicleHull(intCD, vehicle, itemsFactory=None):
    typeCD = getTypeOfCompactDescr(intCD)
    if typeCD == GUI_ITEM_TYPE.CHASSIS:
        item = itemsFactory.createGuiItem(typeCD, intCompactDescr=intCD)
        hulls = vehicle.descriptor.type.hulls
        for hull in hulls:
            if item.innationID in hull.variantMatch:
                return True

    return False


class ACTION_ENTITY_ITEM(object):
    ACTION_NAME_IDX = 0
    ACTION_STEP_IDX = 1
    AFFECTED_ACTIONS_IDX = 2
    ENTITIES_SECTION_NAME = b'actionEntities'
    ACTIONS_SECTION_NAME = b'actions'
    STEPS_SECTION_NAME = b'steps'


class KPI(object):
    __slots__ = (b'__name', b'__value', b'__type', b'__specValue', b'__vehicleTypes', b'__isDebuff', b'__isSituational')

    class Name(CONST_CONTAINER):
        COMPOUND_KPI = b'compoundKPI'
        VEHICLE_REPAIR_SPEED = b'vehicleRepairSpeed'
        VEHICLE_CHASSIS_REPAIR_SPEED = b'vehicleChassisRepairSpeed'
        VEHICLE_CHASSIS_REPAIR_TIME = b'vehicleChassisRepairTime'
        VEHICLE_ENGINE_POWER = b'vehicleEnginePower'
        VEHICLE_TURRET_ROTATION_SPEED = b'vehicleTurretRotationSpeed'
        VEHICLE_CIRCULAR_VISION_RADIUS = b'vehicleCircularVisionRadius'
        VEHICLE_STILL_CIRCULAR_VISION_RADIUS = b'vehicleStillCircularVisionRadius'
        VEHICLE_STILL_CIRCULAR_VISION_RADIUS_DELUXE = b'vehicleStillCircularVisionRadiusDeluxe'
        VEHICLE_CAMOUFLAGE = b'vehicleCamouflage'
        VEHICLE_STILL_CAMOUFLAGE = b'vehicleStillCamouflage'
        VEHICLE_STILL_CAMOUFLAGE_DELUXE = b'vehicleStillCamouflageDeluxe'
        VEHICLE_FIRE_CHANCE = b'vehicleFireChance'
        VEHICLE_GUN_RELOAD_TIME = b'vehicleGunReloadTime'
        VEHICLE_GUN_AIM_SPEED = b'vehicleGunAimSpeed'
        VEHICLE_GUN_SHOT_DISPERSION = b'vehicleGunShotDispersion'
        VEHICLE_GUN_SHOT_DISPERSION_AFTER_SHOT = b'vehicleGunShotDispersionAfterShot'
        VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_MOVEMENT = b'vehicleGunShotDispersionChassisMovement'
        VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_ROTATION = b'vehicleGunShotDispersionChassisRotation'
        VEHICLE_GUN_SHOT_DISPERSION_TURRET_ROTATION = b'vehicleGunShotDispersionTurretRotation'
        VEHICLE_GUN_SHOT_DISPERSION_WHILE_GUN_DAMAGED = b'vehicleGunShotDispersionWhileGunDamaged'
        VEHICLE_GUN_SHOT_FULL_DISPERSION = b'vehicleGunShotFullDispersion'
        VEHICLE_AMMO_BAY_STRENGTH = b'vehicleAmmoBayStrength'
        VEHICLE_FUEL_TANK_STRENGTH = b'vehicleFuelTankStrength'
        VEHICLE_ENGINE_STRENGTH = b'vehicleEngineStrength'
        VEHICLE_CHASSIS_STRENGTH = b'vehicleChassisStrength'
        VEHICLE_AMMO_BAY_ENGINE_FUEL_STRENGTH = b'vehicleAmmoBayEngineFuelStrength'
        VEHICLE_CHASSIS_FALL_DAMAGE = b'vehicleChassisFallDamage'
        VEHICLE_RAM_DAMAGE_RESISTANCE = b'vehicleRamDamageResistance'
        VEHICLE_DAMAGE_ENEMIES_BY_RAMMING = b'damageEnemiesByRamming'
        VEHICLE_SOFT_GROUND_PASSABILITY = b'vehicleSoftGroundPassability'
        VEHICLE_MEDIUM_GROUND_PASSABILITY = b'vehicleMediumGroundPassability'
        VEHICLE_ENEMY_SPOTTING_TIME = b'vehicleEnemySpottingTime'
        VEHICLE_OWN_SPOTTING_TIME = b'vehicleOwnSpottingTime'
        VEHICLE_INVISIBILITY_AFTER_SHOT = b'vehicleInvisibilityAfterShot'
        VEHICLE_RELOAD_TIME_AFTER_SHELL_CHANGE = b'vehicleReloadTimeAfterShellChange'
        VEHICLE_STRENGTH = b'vehicleStrength'
        VEHICLE_ALL_GROUND_ROTATION_SPEED = b'vehicleAllGroundRotationSpeed'
        VEHICLE_SPEED_GAIN = b'vehicleSpeedGain'
        VEHICLE_TURRET_OR_CUTTING_ROTATION_SPEED = b'vehicleTurretOrCuttingRotationSpeed'
        VEHICLE_FORWARD_MAX_SPEED = b'vehicleForwardMaxSpeed'
        VEHICLE_BACKWARD_MAX_SPEED = b'vehicleBackwardMaxSpeed'
        EQUIPMENT_PREPARATION_TIME = b'equipmentPreparationTime'
        DAMAGE_AND_PIERCING_DISTRIBUTION_LOWER_BOUND = b'damageAndPiercingDistributionLowerBound'
        DAMAGE_AND_PIERCING_DISTRIBUTION_UPPER_BOUND = b'damageAndPiercingDistributionUpperBound'
        PIERCING_HE_SHELLS_DISTRIBUTION_UPPER_BOUND = b'piercingHEShellsDistributionUpperBound'
        PENALTY_TO_DAMAGED_SURVEYING_DEVICE = b'penaltyToDamagedSurveyingDevice'
        STUN_RESISTANCE_EFFECT_FACTOR = b'stunResistanceEffectFactor'
        ART_NOTIFICATION_DELAY_FACTOR = b'artNotificationDelayFactor'
        MEDIUM_GROUND_FACTOR = b'mediumGroundFactor'
        SOFT_GROUND_FACTOR = b'softGroundFactor'
        WHEELS_ROTATION_SPEED = b'wheelsRotationSpeed'
        VEHICLE_FUEL_TANK_LESION_CHANCE = b'vehicleFuelTankLesionChance'
        FOLIAGE_MASKING_FACTOR = b'foliageMaskingFactor'
        ENEMY_MODULES_CREW_CRIT_CHANCE = b'enemyModulesCrewCritChance'
        VEHICLE_RAM_CHASSIS_DAMAGE_RESISTANCE = b'vehicleRamChassisDamageResistance'
        DAMAGED_MODULES_DETECTION_TIME = b'damagedModulesDetectionTime'
        FIRE_EXTINGUISHING_RATE = b'fireExtinguishingRate'
        WOUNDED_CREW_EFFICIENCY = b'woundedCrewEfficiency'
        VEHICLE_HE_SHELL_DAMAGE_RESISTANCE = b'vehicleHEShellDamageResistance'
        VEHICLE_FALLING_DAMAGE_RESISTANCE = b'vehicleFallingDamageResistance'
        VEHICLE_PENALTY_FOR_DAMAGED_ENGINE = b'vehPenaltyForDamagedEngine'
        VEHICLE_PENALTY_FOR_DAMAGED_AMMORACK = b'vehPenaltyForDamagedAmmorack'
        COMMANDER_LAMP_DELAY = b'commanderLampDelay'
        GUN_STABILIZATION = b'gunStabilization'
        HULL_ELEVATION_SPEED = b'hullElevationSpeed'
        ENGINE_HP = b'engineHP'
        FUEL_TANK_HP = b'fuelTankHP'
        VEHICLE_SPEED = b'vehicleSpeed'
        STANDARD_SHELL_PENETRATION = b'standardShellPenetration'
        SPECIAL_SHELL_PENETRATION = b'specialShellPenetration'
        ADDITIONAL_SHELL_AMMO_CAPACITY = b'additionalShellAmmoCapacity'
        NON_HE_SHELL_DAMAGE = b'nonHEShellDamage'
        HE_SHELL_DAMAGE = b'HEShellDamage'
        STANDARD_SHELL_DAMAGE = b'standardShellDamage'
        SPECIAL_SHELL_DAMAGE = b'specialShellDamage'
        ALL_SHELL_DAMAGE = b'allShellDamage'
        BASIC_SHELL_DAMAGE = b'basicShellDamage'
        HE_SHELL_PENETRATION = b'HEShellPenetration'
        GUN_DEPRESSION = b'gunDepression'
        GUN_TRAVERSE = b'gunTraverse'
        TURRET_TRAVERSE = b'turretTraverse'
        GUN_ELEVATION = b'gunElevation'
        STANDARD_SHELL_VELOCITY = b'standardShellVelocity'
        SPECIAL_SHELL_VELOCITY = b'specialShellVelocity'
        RELOAD_TIME_SALVO = b'reloadTimeSalvo'
        RELOAD_TIME_SINGLE = b'reloadTimeSingle'
        RELOAD_TIME_IN_CLIP = b'reloadTimeInClip'
        SHELL_VELOCITY = b'shellVelocity'
        ALL_SHELLS_VELOCITY = b'allShellsVelocity'
        SHELL_MODULE_DAMAGE = b'shellModuleDamage'
        SUSPENSION_DAMAGE_REDUCTION = b'suspensionDamageReduction'
        HP_RECOVER = b'hpRecover'
        COOLING_PER_SEC = b'coolingPerSec'
        HE_SHELL_VELOCITY = b'HEshellVelocity'
        MINIMUM_DAMAGE_AND_PIERCING_POWER = b'minimumDamageAndPiercingPower'
        VEHICLE_CAMOUFLAGE_GROUP = b'vehicleCamouflageGroup'
        VEHICLE_STILL_CAMOUFLAGE_GROUP = b'vehicleStillCamouflageGroup'
        VEHICLE_STILL_CAMOUFLAGE_GROUP_DELUXE = b'vehicleStillCamouflageGroupDeluxe'
        CREW_LEVEL = b'crewLevel'
        CREW_HIT_CHANCE = b'crewHitChance'
        CREW_STUN_DURATION = b'crewStunDuration'
        CREW_REPEATED_STUN_DURATION = b'crewRepeatedStunDuration'
        CREW_SKILL_REPAIR = b'crewSkillRepair'
        CREW_SKILL_FIRE_FIGHTING = b'crewSkillFireFighting'
        CREW_SKILL_CAMOUFLAGE = b'crewSkillCamouflage'
        CREW_SKILL_BROTHERHOOD = b'crewSkillBrotherHood'
        CREW_SKILL_SIXTH_SENSE = b'crewSkillSixthSense'
        CREW_SKILL_SIXTH_SENSE_DELAY = b'crewSkillSixthSenseDelay'
        CREW_SKILL_VIRTUOSO = b'crewSkillVirtuoso'
        CREW_SKILL_SMOOTH_DRIVING = b'crewSkillSmoothRiding'
        CREW_SKILL_RANCOROUS = b'crewSkillRancorous'
        CREW_SKILL_RANCOROUS_DURATION = b'crewSkillRancorousDuration'
        CREW_SKILL_PEDANT = b'crewSkillPedant'
        CREW_SKILL_SMOOTH_TURRET = b'crewSkillSmoothTurret'
        CREW_SKILL_PRACTICAL = b'crewSkillPractical'
        CREW_SKILL_STUN_RESISTANCE = b'crewSkillStunResistance'
        DEMASK_FOLIAGE_FACTOR = b'demaskFoliageFactor'
        DEMASK_MOVING_FACTOR = b'demaskMovingFactor'
        GAME_XP = b'gameXp'
        GAME_FREE_XP = b'gameFreeXp'
        GAME_CREW_XP = b'gameCrewXp'
        GAME_CREDITS = b'gameCredits'
        GAME_FL_XP = b'gameFlXp'
        GAME_FREE_XP_AND_CREW_XP = b'gameFreeXpAndCrewXp'
        VALUE = b'value'

    class Type(CONST_CONTAINER):
        MUL = b'mul'
        ADD = b'add'
        BOOST_SKILL = b'boostSkill'
        ONE_OF = b'oneOf'
        AGGREGATE_MUL = b'aggregateMul'

    def __init__(self, kpiName, kpiValue, kpiType=Type.MUL, specValue=None, vehicleTypes=None, situational=False):
        self.__name = kpiName
        self.__value = kpiValue
        self.__type = kpiType
        self.__specValue = specValue
        self.__vehicleTypes = vehicleTypes or None
        self.__isSituational = situational
        return

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def specValue(self):
        return self.__specValue

    @property
    def type(self):
        return self.__type

    @property
    def vehicleTypes(self):
        return self.__vehicleTypes

    @property
    def situational(self):
        return self.__isSituational

    @property
    def isDebuff(self):
        from gui.shared.items_parameters.comparator import BACKWARD_QUALITY_PARAMS
        if self.name in BACKWARD_QUALITY_PARAMS:
            return self.isPositive
        return not self.isPositive

    @property
    def isPositive(self):
        cmpValue = 0 if self.type == self.Type.ADD else 1
        return self.value >= cmpValue

    def getDescriptionR(self):
        return getVehicleParameterText(paramName=self.__name, isPositive=self.isPositive)

    def getLongDescriptionR(self):
        return getVehicleParameterText(paramName=self.__name, isPositive=self.isPositive, isLong=True)


def kpiAddEnding(kpiName, text):
    res = text
    ending = R.strings.tank_setup.kpi.bonus.valueTypes.dyn(kpiName, R.strings.tank_setup.kpi.bonus.valueTypes.default)()
    if ending != R.strings.tank_setup.kpi.bonus.valueTypes.default():
        res += b' '
    res += backport.text(ending)
    return res


def kpiFormatValue(kpiName, value, addEnding=True):
    res = (b'+' if value > 0 else b'') + getNiceNumberFormat(value)
    if addEnding:
        return kpiAddEnding(kpiName, res)
    return res


def kpiFormatNoSignValue(kpiName, value, addEnding=True):
    res = getNiceNumberFormat(value)
    if addEnding:
        return kpiAddEnding(kpiName, res)
    return res


def kpiFormatValueRange(kpiName, valueRange, addEnding=True):
    minValue, maxValue = valueRange
    res = (b'{}-{}').format(getNiceNumberFormat(minValue), getNiceNumberFormat(maxValue))
    if addEnding:
        return kpiAddEnding(kpiName, res)
    return res


def getKpiValueString(kpi, value, addEnding=True):
    if kpi.type == KPI.Type.MUL:
        value = (value - 1.0) * 100
    elif kpi.type == KPI.Type.AGGREGATE_MUL:
        minValue, maxValue = value
        formatValue = ((minValue - 1.0) * 100, (maxValue - 1.0) * 100)
        return kpiFormatValueRange(kpi.name, formatValue, addEnding)
    return kpiFormatValue(kpi.name, value, addEnding)


def getKpiFormatDescription(kpi):
    value = getKpiValueString(kpi, kpi.value)
    specValue = getKpiValueString(kpi, kpi.specValue) if kpi.specValue else None
    generalValue = (b' / ').join((value, specValue)) if specValue is not None else value
    description = (b' ').join((generalValue, backport.text(kpi.getDescriptionR(), default=b'')))
    return description


def mergeAggregateKpi(aggregateKpi):

    def _mergeValue(value, currentRange):
        if currentRange is None:
            return (value, value)
        else:
            minValue, maxValue = currentRange
            return (min(minValue, value), max(maxValue, value))

    if aggregateKpi.type not in (KPI.Type.AGGREGATE_MUL,):
        _logger.debug(b'Only aggregate kpi type supported merge')
        return aggregateKpi
    else:
        specValue = None
        vehicleTypes = []
        value = None
        for kpi in aggregateKpi.value:
            value = _mergeValue(kpi.value, value)
            if kpi.specValue:
                specValue = _mergeValue(kpi.specValue, specValue)
            if kpi.vehicleTypes:
                vehicleTypes.extend(kpi.vehicleTypes)

        return KPI(aggregateKpi.name, value, aggregateKpi.type, specValue, vehicleTypes)


def collectKpi(descriptor, vehicle=None):
    if vehicle is None:
        return [mergeAggregateKpi(kpi) if kpi.type == KPI.Type.AGGREGATE_MUL else kpi for kpi in descriptor.kpi]
    else:
        result = []
        for kpi in descriptor.kpi:
            if kpi.type == KPI.Type.AGGREGATE_MUL:
                for subKpi in kpi.value:
                    if not subKpi.vehicleTypes or vehicle.type in subKpi.vehicleTypes:
                        result.append(subKpi)

            elif not kpi.vehicleTypes or vehicle.type in kpi.vehicleTypes:
                result.append(kpi)

        return result


VEHICLE_ATTR_TO_KPI_NAME_MAP = {b'repairSpeed': (KPI.Name.VEHICLE_REPAIR_SPEED), 
   b'repairSpeedFactor': (KPI.Name.VEHICLE_REPAIR_SPEED), 
   b'circularVisionRadius': (KPI.Name.VEHICLE_CIRCULAR_VISION_RADIUS), 
   b'circularVisionRadiusFactor': (KPI.Name.VEHICLE_CIRCULAR_VISION_RADIUS), 
   b'circularVisionRadiusBaseFactor': (KPI.Name.VEHICLE_CIRCULAR_VISION_RADIUS), 
   b'gunReloadTimeFactor': (KPI.Name.VEHICLE_GUN_RELOAD_TIME), 
   b'gunAimingTimeFactor': (KPI.Name.VEHICLE_GUN_AIM_SPEED), 
   b'ammoBayHealthFactor': (KPI.Name.VEHICLE_AMMO_BAY_STRENGTH), 
   b'fuelTankHealthFactor': (KPI.Name.VEHICLE_FUEL_TANK_STRENGTH), 
   b'engineHealthFactor': (KPI.Name.VEHICLE_ENGINE_STRENGTH), 
   b'additiveShotDispersionFactor': (KPI.Name.VEHICLE_GUN_SHOT_DISPERSION), 
   b'movingAimingDispersion': (KPI.Name.VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_MOVEMENT), 
   b'shotDemaskFactor': (KPI.Name.VEHICLE_INVISIBILITY_AFTER_SHOT), 
   b'lowDamageDispersion': (KPI.Name.DAMAGE_AND_PIERCING_DISTRIBUTION_LOWER_BOUND), 
   b'lowPenetrationDispersion': (KPI.Name.DAMAGE_AND_PIERCING_DISTRIBUTION_LOWER_BOUND)}
CREW_SKILL_TO_KPI_NAME_MAP = {b'repair': (KPI.Name.CREW_SKILL_REPAIR), 
   b'fireFighting': (KPI.Name.CREW_SKILL_FIRE_FIGHTING), 
   b'camouflage': (KPI.Name.CREW_SKILL_CAMOUFLAGE), 
   b'brotherhood': (KPI.Name.CREW_SKILL_BROTHERHOOD), 
   b'commander_sixthSense': (KPI.Name.CREW_SKILL_SIXTH_SENSE), 
   b'driver_virtuoso': (KPI.Name.CREW_SKILL_VIRTUOSO), 
   b'driver_smoothDriving': (KPI.Name.CREW_SKILL_SMOOTH_DRIVING), 
   b'gunner_smoothTurret': (KPI.Name.CREW_SKILL_SMOOTH_TURRET), 
   b'loader_pedant': (KPI.Name.CREW_SKILL_PEDANT), 
   b'gunner_rancorous': (KPI.Name.CREW_SKILL_RANCOROUS)}
AGGREGATE_TO_SINGLE_TYPE_KPI_MAP = {(KPI.Type.AGGREGATE_MUL): (KPI.Type.MUL)}
