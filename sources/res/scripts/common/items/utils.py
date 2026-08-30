from __future__ import absolute_import, division
import copy, re
from operator import sub
from functools import partial
from future.utils import lmap, viewitems, viewvalues
from past.builtins import long, basestring
from typing import Any, Dict, Tuple
import ResMgr
from account_shared import AmmoIterator
from constants import VEHICLE_TTC_ASPECTS, IS_CLIENT
from debug_utils import LOG_ERROR
from items import tankmen, ITEM_TYPES
from items import vehicles
from items.components.c11n_constants import CUSTOMIZATION_SLOTS_VEHICLE_PARTS
from items.components.shared_components import ExtraShotClipParams
from items.tankmen import MAX_SKILL_LEVEL, MIN_ROLE_LEVEL, getSkillsConfig
from items.vehicles import vehicleAttributeFactors, VehicleDescriptor
from items.artefacts import StaticOptionalDevice, AdditiveBattleBooster
from items.components import component_constants
__defaultGlossTexture = None
_FORMAT_VEH_INFO_STRING_REXP = re.compile(b'{([a-zA-Z]+)}')
_VEH_INFO_STRING_CONVERTERS = {b'level': (lambda descr: str(descr.type.level)), 
   b'class': (lambda descr: descr.type.getVehicleClass()), 
   b'vehName': (lambda descr: descr.type.name.split(b':')[1]), 
   b'clip': (lambda descr: b'hasClip' if b'clip' in descr.gun.tags else b'noClip'), 
   b'autoreload': (lambda descr: b'hasAutoReload' if b'autoreload' in descr.gun.tags else b'noAutoreload'), 
   b'wheels': (lambda descr: b'hasWheels' if descr.isWheeledVehicle else b'noWheels'), 
   b'burst': (lambda descr: b'hasBurst' if descr.hasBurst else b'noBurst'), 
   b'dualGun': (lambda descr: b'hasDualGun' if descr.isDualgunVehicle else b'noDualGun'), 
   b'hydraulicChassis': (lambda descr: b'hasHydraulicChassis' if descr.type.hasSiegeMode and descr.type.hasHydraulicChassis else b'noHydraulicChassis')}

def getDefaultGlossTexture():
    global __defaultGlossTexture
    if __defaultGlossTexture is None:
        section = ResMgr.openSection(b'resources.xml')
        if section is None:
            return
        __defaultGlossTexture = section.readString(b'gameplay/projDecalDefaultGM', b'')
    return __defaultGlossTexture


def getItemDescrByCompactDescr(compDescr):
    itemTypeID, _, _ = vehicles.parseIntCompactDescr(compDescr)
    if itemTypeID in vehicles.VEHICLE_ITEM_TYPES:
        descr = vehicles.getItemByCompactDescr(compDescr)
    else:
        descr = tankmen.getItemByCompactDescr(compDescr)
    return descr


def isItemWithCompactDescrExist(compDescr):
    itemTypeID, _, _ = vehicles.parseIntCompactDescr(compDescr)
    if itemTypeID in vehicles.VEHICLE_ITEM_TYPES:
        return vehicles.isItemWithCompactDescrExist(compDescr)
    else:
        return tankmen.isItemWithCompactDescrExist(compDescr)

    return


def _makeDefaultVehicleFactors(sample):
    default = {}
    for key, value in viewitems(sample):
        if value is None:
            default[key] = value
        elif isinstance(value, (float, int, long, basestring)):
            default[key] = value
        elif isinstance(value, (list, tuple)):
            default[key] = value[:]
        else:
            LOG_ERROR(b'Default value of vehicle attribute can not be resolved', key, value)

    return default


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def generateDefaultCrew(vehicleType, level):
    nationID, vehicleTypeID = vehicleType.id
    skills = ()
    passport = (nationID, False, False, 0, 0, 0)
    res = []
    for roles in vehicleType.crewRoles:
        cd = tankmen.generateCompactDescr(passport, vehicleTypeID, roles[0], level, skills, level)
        res.append(tankmen.stripNonBattle(cd))

    return tuple(res)


def _generateTankman(vehicleDescr, roles, level):
    nationID, vehicleTypeID = vehicleDescr.type.id
    passport = (nationID, False, False, 0, 0, 0)
    skills = ()
    return tankmen.stripNonBattle(tankmen.generateCompactDescr(passport, vehicleTypeID, roles[0], level, skills, level))


def _replaceMissingTankmenWithDefaultOnes(vehicleDescr, crewCompactDescrs, level=MAX_SKILL_LEVEL):
    result = []
    for tankmanCompactDescr, roles in zip(crewCompactDescrs, vehicleDescr.type.crewRoles):
        if tankmanCompactDescr is None:
            result.append(_generateTankman(vehicleDescr, roles, level))
        else:
            result.append(tankmanCompactDescr)

    return result


def getRadioDistance(vehicleDescr, factors):
    return vehicleDescr.radio.distance * max(factors[b'radio/distance'], 0.0)


def getCircularVisionRadius(vehicleDescr, factors):
    penalty = max(factors[b'circularVisionRadius'], 0.0)
    circularVisionRadiusMul = (1 - (1 - penalty) * factors[b'penaltyToDamagedSurveyingDevice']) * factors[b'increaseCircularVisionRadius'] if penalty < vehicleDescr.miscAttrs[b'circularVisionRadiusBaseFactor'] else factors[b'increaseCircularVisionRadius'] * max(factors[b'circularVisionRadius'], 0.0)
    return vehicleDescr.turret.circularVisionRadius * vehicleDescr.miscAttrs[b'circularVisionRadiusBaseFactor'] * vehicleDescr.miscAttrs[b'circularVisionRadiusFactor'] * circularVisionRadiusMul


def getVehicleShotSpeedByFactors(factors, speed, gravity=1.0, factorName=b'gunShotsSpeed'):
    projectileSpeedFactor = vehicles.g_cache.commonConfig[b'miscParams'][b'projectileSpeedFactor']
    newProjectileSpeedFactor = projectileSpeedFactor * factors.get(factorName, 1.0)
    speed = speed / projectileSpeedFactor * newProjectileSpeedFactor
    gravity = gravity / projectileSpeedFactor ** 2 * newProjectileSpeedFactor ** 2
    return (
     speed, gravity)


def getFirstReloadTime(vehicleDescr, factors, ignoreRespawn=False, shellsAmount=0):
    respawnReloadFactor = max(factors[b'respawnReloadTimeFactor'], 0.0)
    factor = vehicleDescr.miscAttrs[b'gunReloadTimeFactor'] * max(factors[b'gun/reloadTime'], 0.0)
    firstShellReload = vehicleDescr.gun.reloadTime
    if b'dualGun' in vehicleDescr.gun.tags:
        firstShellReload = vehicleDescr.gun.dualGun.reloadTimes[0]
    elif b'clip' in vehicleDescr.gun.tags and b'autoreload' in vehicleDescr.gun.tags:
        firstShellReload = vehicleDescr.gun.autoreload.reloadTime[-1]
    elif b'twinGun' in vehicleDescr.gun.tags and shellsAmount > 1:
        firstShellReload = vehicleDescr.gun.twinGun.twinGunReloadTime
    reloadTime = firstShellReload * factor if ignoreRespawn else firstShellReload * factor * respawnReloadFactor
    return reloadTime + factors[b'gun/extraReloadTime']


def getReloadTime(vehicleDescr, factors, gunDescr=None, miscFactorName=None):
    gunDescr = gunDescr or vehicleDescr.gun
    if miscFactorName is None:
        miscFactorName = b'gunReloadTimeFactor'
    return gunDescr.reloadTime * vehicleDescr.miscAttrs[miscFactorName] * max(factors[b'gun/reloadTime'], 0.0) + factors[b'gun/extraReloadTime']


def getClipReloadTime(vehicleDescr, factors):
    if b'clip' in vehicleDescr.gun.tags:
        factor = vehicleDescr.miscAttrs[b'gunReloadTimeFactor'] * max(factors[b'gun/reloadTime'], 0.0)
        if b'autoreload' in vehicleDescr.gun.tags:
            return tuple(reloadTime * factor for reloadTime in vehicleDescr.gun.autoreload.reloadTime)
        if b'autoShoot' in vehicleDescr.gun.tags:
            return (0.0,)
        reloadTime = vehicleDescr.gun.reloadTime * factor + factors[b'gun/extraReloadTime']
        return (reloadTime,)
    else:
        return (0.0,)
    return


def getDualGunReloadTime(vehicleDescr, factors):
    if b'dualGun' in vehicleDescr.gun.tags:
        factor = vehicleDescr.miscAttrs[b'gunReloadTimeFactor'] * max(factors[b'gun/reloadTime'], 0.0)
        return tuple(reloadTime * factor for reloadTime in vehicleDescr.gun.dualGun.reloadTimes)
    else:
        return (0.0,)

    return


def getTwinGunReloadTime(vehicleDescr, factors):
    if b'twinGun' in vehicleDescr.gun.tags:
        factor = vehicleDescr.miscAttrs[b'gunReloadTimeFactor'] * max(factors[b'gun/reloadTime'], 0.0)
        oneGunReloadTime = vehicleDescr.gun.reloadTime * factor
        twinGunsReloadTime = vehicleDescr.gun.twinGun.twinGunReloadTime * factor
        return (
         oneGunReloadTime, twinGunsReloadTime)
    return (0.0,)


def getExtraReloadTime(vehicleDescr):
    mechanicsParams = vehicleDescr.mechanicsParams
    if not mechanicsParams:
        return 0.0
    else:
        params = mechanicsParams.get(ExtraShotClipParams.MECHANICS_NAME)
        if params is None:
            return 0.0
        return params.extraReloadTime


def getTurretRotationSpeed(vehicleDescr, factors):
    return vehicleDescr.turret.rotationSpeed * getTurretRotationSpeedFactor(vehicleDescr, factors)


def getTurretRotationSpeedFactor(vehicleDescr, factors):
    return max(factors[b'turret/rotationSpeed'], 0.0) * vehicleDescr.miscAttrs[b'turretRotationSpeed']


def getGunRotationSpeed(vehicleDescr, factors):
    return vehicleDescr.gun.rotationSpeed * max(factors[b'gun/rotationSpeed'], 0.0)


def getGunAimingTime(vehicleDescr, factors, gunDescr=None, miscFactorName=None):
    gunDescr = gunDescr or vehicleDescr.gun
    if miscFactorName is None:
        miscFactorName = b'gunAimingTimeFactor'
    return gunDescr.aimingTime * vehicleDescr.miscAttrs[miscFactorName] * max(factors[b'gun/aimingTime'], 0.0)


def getClipTimeBetweenShots(vehicleDescr, factors):
    if b'autoShoot' not in vehicleDescr.gun.tags:
        return vehicleDescr.gun.clip[1] * max(factors[b'gun/clipTimeBetweenShots'], 0.0)
    return 0.0


def getChassisRotationSpeed(vehicleDescr, factors):
    return vehicleDescr.chassis.rotationSpeed * max(factors[b'vehicle/rotationSpeed'], 0.0) * max(vehicleDescr.miscAttrs[b'onMoveRotationSpeedFactor'], vehicleDescr.miscAttrs[b'onStillRotationSpeedFactor'])


def getInvisibility(vehicleDescr, factors, baseInvisibility, isMoving):
    baseValue = baseInvisibility[0 if isMoving else 1]
    additiveTerm = factors[b'invisibility'][0] + factors.get(b'invisibilityAdditiveTerm', 0.0) + vehicleDescr.miscAttrs[b'invisibilityBaseAdditive'] + vehicleDescr.miscAttrs[b'invisibilityAdditiveTerm']
    multFactor = factors[b'invisibility'][1] * factors.get(b'invisibilityMultFactor', 1.0)
    return max(0.0, (baseValue + additiveTerm) * multFactor)


if IS_CLIENT:
    CLIENT_VEHICLE_ATTRIBUTE_FACTORS = {b'camouflage': 1.0, 
       b'shotDispersion': 1.0, 
       b'dualAccuracyCoolingDelay': 1.0}
    CLIENT_VEHICLE_ATTRIBUTE_FACTORS.update(vehicleAttributeFactors())

    def makeDefaultClientVehicleAttributeFactors():
        return _makeDefaultVehicleFactors(CLIENT_VEHICLE_ATTRIBUTE_FACTORS)


    def _isFactor(a):
        return isinstance(a, (int, long, float))


    def _comparableFactors(original, changed):
        if all(isinstance(x, list) for x in (original, changed)):
            return all(_isFactor(a) and _isFactor(b) for a, b in zip(original, changed))
        else:
            return _isFactor(original) and _isFactor(changed)

        return


    def _compareFactors(original, changed):
        result = {}
        for factor in original:
            if not _comparableFactors(original[factor], changed[factor]):
                continue
            if all(isinstance(x, list) for x in (original[factor], changed[factor])):
                if not all(lmap(isclose, original[factor], changed[factor])):
                    result[factor] = lmap(sub, original[factor], changed[factor])
            elif not isclose(original[factor], changed[factor]):
                originalFactor = original.get(factor, CLIENT_VEHICLE_ATTRIBUTE_FACTORS[factor])
                changedFactor = changed[factor]
                if originalFactor == changedFactor:
                    continue
                result[factor] = originalFactor - changedFactor

        return result


    def getClientInvisibility(vehicleDescr, vehicle, camouflageFactor, factors):
        camouflageId = None
        camouflage = vehicle.getBonusCamo()
        if camouflage is not None:
            camouflageId = camouflage.id
        baseInvisibility = vehicleDescr.computeBaseInvisibility(camouflageFactor, camouflageId)
        invisibilityFactors = factors[b'invisibility']
        factors[b'invisibility'] = invisibilityFactors[VEHICLE_TTC_ASPECTS.DEFAULT]
        moving = getInvisibility(vehicleDescr, factors, baseInvisibility, True)
        factors[b'invisibility'] = invisibilityFactors[VEHICLE_TTC_ASPECTS.WHEN_STILL]
        still = getInvisibility(vehicleDescr, factors, baseInvisibility, False)
        factors[b'invisibility'] = invisibilityFactors
        return (moving, still)


    def updateAttrFactorsWithSplit(vehicleDescr, crewCompactDescrs, eqs, factors, additionalCrewLevelIncrease=0, isModifySkillProcessors=False):
        extras = {}
        extraAspects = {(VEHICLE_TTC_ASPECTS.WHEN_STILL): (b'invisibility',)}
        for aspect, coefficients in viewitems(extraAspects):
            currFactors = copy.deepcopy(factors)
            updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, currFactors, aspect, additionalCrewLevelIncrease, isModifySkillProcessors)
            for coefficient in coefficients:
                extras.setdefault(coefficient, {})[aspect] = currFactors[coefficient]

        updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, factors, VEHICLE_TTC_ASPECTS.DEFAULT, additionalCrewLevelIncrease, isModifySkillProcessors)
        for coefficientName, coefficientValue in viewitems(extras):
            coefficientValue[VEHICLE_TTC_ASPECTS.DEFAULT] = factors[coefficientName]
            factors[coefficientName] = coefficientValue

        return


    def getCrewAffectedFactors(vehicleDescr, crewCompactDescrs):
        defaultCrewCompactDescrs = _replaceMissingTankmenWithDefaultOnes(vehicleDescr, crewCompactDescrs)
        defaultFactors = makeDefaultClientVehicleAttributeFactors()
        updateAttrFactorsWithSplit(vehicleDescr, defaultCrewCompactDescrs, [], defaultFactors)
        result = {}
        for i, (tankmanCompactDescr, roles) in enumerate(zip(crewCompactDescrs, vehicleDescr.type.crewRoles)):
            backupedtankmanCompactDescr = defaultCrewCompactDescrs[i]
            defaultCrewCompactDescrs[i] = _generateTankman(vehicleDescr, roles, MIN_ROLE_LEVEL if tankmanCompactDescr is None else MAX_SKILL_LEVEL)
            tankmanAffectedFactors = makeDefaultClientVehicleAttributeFactors()
            updateAttrFactorsWithSplit(vehicleDescr, defaultCrewCompactDescrs, [], tankmanAffectedFactors)
            changedFactors = _compareFactors(tankmanAffectedFactors, defaultFactors)
            if changedFactors:
                result[i] = changedFactors
            defaultCrewCompactDescrs[i] = backupedtankmanCompactDescr

        return result


    def _sumCrewLevelIncrease(eqs):
        return sum(filter(None, [getattr(eq, b'crewLevelIncrease', None) for eq in eqs]))


    def updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, factors, aspect, additionalCrewLevelIncrease=0, isModifySkillProcessors=False):
        from items.VehicleDescrCrew import VehicleDescrCrew
        factors[b'crewLevelIncrease'] = _sumCrewLevelIncrease(eqs)
        for eq in eqs:
            if eq is not None:
                eq.updateVehicleAttrFactorsForAspect(vehicleDescr, factors, aspect)

        vehicleDescr.applyOptDevFactorsForAspect(factors, aspect)
        factors[b'crewLevelIncrease'] += additionalCrewLevelIncrease
        vehicleDescrCrew = VehicleDescrCrew(vehicleDescr, crewCompactDescrs)
        if isModifySkillProcessors:
            vehicleDescrCrew.modifySkillProcessors()
        for eq in eqs:
            if eq is not None and b'crewSkillBattleBooster' in eq.tags:
                vehicleDescrCrew.boostSkillBy(eq)

        vehicleDescrCrew.onCollectFactors(factors)
        factors[b'camouflage'] = vehicleDescrCrew.camouflageFactor
        if vehicleDescr.hasDualAccuracy:
            crewData = vehicleDescrCrew.collectDefaultCrewData()
            vehicleDescrCrew.extendSkillProcessor(b'dualAccuracyCoolingDelay', crewData, partial(_updateDualAccuracyCoolingDelay, factors=factors))
        multShotDispersionFactor = factors.get(b'multShotDispersionFactor', 1.0)
        shotDispersionFactors = [multShotDispersionFactor, 0.0]
        vehicleDescrCrew.onCollectShotDispersionFactors(shotDispersionFactors)
        factors[b'shotDispersion'] = shotDispersionFactors
        for mechanic in viewvalues(vehicleDescr.mechanicsParams):
            mechanic.updateVehicleAttrFactorsForAspect(vehicleDescr, factors, aspect)

        return


    def _updateDualAccuracyCoolingDelay(_, attr, factors):
        coolingDelayFactor = factors.get(b'dualAccuracyCoolingDelay', 1.0)
        factors[b'dualAccuracyCoolingDelay'] = coolingDelayFactor / attr.factor
        return


def getEditorOnlySection(section, createNewSection=False):
    editorOnlySection = section[b'editorOnly']
    if editorOnlySection is None and createNewSection:
        from items.writers.c11n_writers import findOrCreate
        editorOnlySection = findOrCreate(section, b'editorOnly')
    return editorOnlySection


def getDifferVehiclePartNames(newVehDescr, oldVehDescr):
    differPartNames = []
    for partName in CUSTOMIZATION_SLOTS_VEHICLE_PARTS:
        if getattr(newVehDescr, partName).compactDescr != getattr(oldVehDescr, partName).compactDescr:
            differPartNames.append(partName)

    if b'turret' in differPartNames:
        if b'gun' not in differPartNames:
            differPartNames.append(b'gun')
    elif b'gun' in differPartNames:
        differPartNames.append(b'turret')
    return differPartNames


def commanderTutorXpBonusFactorForCrew(crew, ammo, vehCompDescr):
    tutorLevel = component_constants.ZERO_FLOAT
    brotherhoodSum = 0.0
    vehDescriptor = VehicleDescriptor(compactDescr=vehCompDescr)
    for t in crew:
        if t.role == b'commander':
            tutorLevel = t.skillLevel(b'commander_tutor')
            if not tutorLevel:
                return component_constants.ZERO_FLOAT
            if not t.isOwnVehicleOrPremium(vehDescriptor.type):
                return component_constants.ZERO_FLOAT
            tutorLevel *= t.skillsEfficiency
        tmanBrotherhoodLevel = t.skillLevel(b'brotherhood') or 0
        brotherhoodSum += tmanBrotherhoodLevel * t.skillsEfficiency

    brotherhoodLevel = brotherhoodSum / (len(crew) * MAX_SKILL_LEVEL)
    skillsConfig = getSkillsConfig()
    brotherhoodBonus = brotherhoodLevel * skillsConfig.getSkill(b'brotherhood').crewLevelIncrease
    tutorLevel += brotherhoodBonus
    equipCrewLevelIncrease = component_constants.ZERO_FLOAT
    optionalDevCrewLevelIncrease = component_constants.ZERO_FLOAT
    cache = vehicles.g_cache
    optDev = set()
    for compDescr, _ in AmmoIterator(ammo):
        itemTypeIdx, _, itemIdx = vehicles.parseIntCompactDescr(compDescr)
        if itemTypeIdx == ITEM_TYPES.optionalDevice:
            obj = cache.optionalDevices()[itemIdx]
            if isinstance(obj, StaticOptionalDevice):
                optionalDevCrewLevelIncrease += obj.getFactorValue(vehDescriptor, b'miscAttrs/crewLevelIncrease')
                optDev.add(obj)

    for compDescr, _ in AmmoIterator(ammo):
        itemTypeIdx, _, itemIdx = vehicles.parseIntCompactDescr(compDescr)
        if itemTypeIdx == ITEM_TYPES.equipment:
            eqip = cache.equipments()[itemIdx]
            equipCrewLevelIncrease += getattr(eqip, b'crewLevelIncrease', component_constants.ZERO_FLOAT)
            if isinstance(eqip, AdditiveBattleBooster):
                for device in optDev:
                    levelParams = eqip.getLevelParamsForDevice(device)
                    if levelParams is not None and b'crewLevelIncrease' in levelParams:
                        equipCrewLevelIncrease += levelParams[1]
                        break

    tutorLevel += optionalDevCrewLevelIncrease
    tutorLevel += equipCrewLevelIncrease
    return tutorLevel * skillsConfig.getSkill(b'commander_tutor').xpBonusFactorPerLevel


def formatVehicleInfoString(fmtStr, descr):

    def _replaceMatch(match):
        converter = _VEH_INFO_STRING_CONVERTERS.get(match.group(1))
        if converter:
            return converter(descr)
        return match.group(0)

    return _FORMAT_VEH_INFO_STRING_REXP.sub(_replaceMatch, fmtStr)


def getVehicleDescriptorWithoutMechanics(vDescr, mechanicsToDrop):
    vDescrCopy = copy.copy(vDescr)
    vDescrCopy.mechanicsParams = {key: value for key, value in vDescr.mechanicsParams.items() if key not in mechanicsToDrop}
    return vDescrCopy
