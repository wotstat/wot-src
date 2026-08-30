from items import _xml
from items.artefacts import Equipment, VehicleFactorsXmlReader, Repairkit, ArenaAimLimits, ArcadeEquipmentConfigReader, Smoke
from items.components import component_constants
from constants import IS_CLIENT
from debug_utils import LOG_WARNING
from items import vehicles

class WTBaseEquipment(object):

    def __init__(self):
        self.subType = b''
        return

    def readExtraData(self, xmlCtx, section):
        self.subType = _xml.readString(xmlCtx, section, b'subType')
        return


class WTRepairkit(Repairkit, WTBaseEquipment):

    def _readBasicConfig(self, xmlCtx, section):
        Repairkit._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTMedkit(Repairkit, WTBaseEquipment):

    def __init__(self):
        super(WTMedkit, self).__init__()
        self.removeDebuffsFromAbilities = component_constants.EMPTY_TUPLE
        return

    def _readConfig(self, xmlCtx, section):
        super(WTMedkit, self)._readConfig(xmlCtx, section)
        self.removeDebuffsFromAbilities = tuple(section.readString(b'removeDebuffsFromAbilities').split(b' '))
        return

    def _readBasicConfig(self, xmlCtx, section):
        Repairkit._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTPassiveHealing(Equipment, WTBaseEquipment):
    __slots__ = (b'maxHealthRegenPct', b'tickInterval', b'effects')

    def __init__(self):
        super(WTPassiveHealing, self).__init__()
        self.maxHealthRegenPct = 0.0
        self.tickInterval = 0.0
        self.effects = {}
        return

    def _readConfig(self, xmlCtx, section):
        super(WTPassiveHealing, self)._readConfig(xmlCtx, section)
        self.maxHealthRegenPct = _xml.readFloat(xmlCtx, section, b'maxHealthRegenPct', 0.0)
        self.tickInterval = _xml.readFloat(xmlCtx, section, b'tickInterval', 0.0)
        if IS_CLIENT:
            self.effects = _getVisualEffects(xmlCtx, section)
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTUnionStrength(Equipment, WTBaseEquipment):
    __slots__ = (b'effectDuration', b'receiveDamageFactor', b'effects', b'teamMateRadius', b'healingValue', b'healingTickInterval')

    def __init__(self):
        super(WTUnionStrength, self).__init__()
        self.effectDuration = component_constants.ZERO_INT
        self.receiveDamageFactor = component_constants.ZERO_FLOAT
        self.effects = component_constants.EMPTY_DICT
        self.hunterEffects = component_constants.EMPTY_DICT
        self.teamMateRadius = component_constants.ZERO_INT
        self.healingValue = component_constants.ZERO_INT
        self.healingTickInterval = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(WTUnionStrength, self)._readConfig(xmlCtx, section)
        self.effectDuration = _xml.readInt(xmlCtx, section, b'effectDuration', 0)
        self.receiveDamageFactor = _xml.readFloat(xmlCtx, section, b'receiveDamageFactor', 1.0)
        self.teamMateRadius = _xml.readInt(xmlCtx, section, b'teamMateRadius', 0)
        self.healingValue = _xml.readInt(xmlCtx, section, b'healingValue', 0)
        self.healingTickInterval = _xml.readFloat(xmlCtx, section, b'healingTickInterval', 0.0)
        if IS_CLIENT:
            self.effects = _getVisualEffects(xmlCtx, section, self.effectDuration)
            self.hunterEffects = _getHunterVisualEffects(xmlCtx, section)
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTInvisibilityBase(Equipment, WTBaseEquipment):
    __slots__ = (b'entrancePrefab', b'escapePrefab')

    def __init__(self):
        super(WTInvisibilityBase, self).__init__()
        self.entrancePrefab = component_constants.EMPTY_STRING
        self.escapePrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(WTInvisibilityBase, self)._readConfig(xmlCtx, section)
        if IS_CLIENT:
            self.entrancePrefab = _xml.readStringOrNone(xmlCtx, section, b'entrancePrefab')
            self.escapePrefab = _xml.readStringOrNone(xmlCtx, section, b'escapePrefab')
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTInvisibilityModA(WTInvisibilityBase):
    __slots__ = (b'procedureEffects',)

    def __init__(self):
        super(WTInvisibilityModA, self).__init__()
        self.procedureEffects = component_constants.EMPTY_DICT
        return

    def _readConfig(self, xmlCtx, section):
        super(WTInvisibilityModA, self)._readConfig(xmlCtx, section)
        self.procedureEffects = _getProcedureEffects(xmlCtx, section)
        return


class WTInvisibilityModB(WTInvisibilityBase):
    pass


class WTHyperionModA(Equipment, WTBaseEquipment):
    __slots__ = (b'readyPrefab',)

    def __init__(self):
        super(WTHyperionModA, self).__init__()
        self.readyPrefab = component_constants.EMPTY_STRING
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTHyperionModA, self)._readConfig(xmlCtx, section)
        self.radius = _xml.readFloat(xmlCtx, section, b'radius', 0.0)
        self.height = _xml.readFloat(xmlCtx, section, b'height', 0.0)
        self.depth = _xml.readFloat(xmlCtx, section, b'depth', 0.0)
        self.chargeFactor = _xml.readFloat(xmlCtx, section, b'chargeFactor', 0.0)
        self.chargingDelay = _xml.readInt(xmlCtx, section, b'chargingDelay', 0)
        self.damagePerShot = _xml.readInt(xmlCtx, section, b'damagePerShot', 0)
        self.shotsAmount = _xml.readInt(xmlCtx, section, b'shotsAmount', 0)
        self.shotDuration = _xml.readFloat(xmlCtx, section, b'shotDuration', 0)
        self.minApplyRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'minApplyRadius', component_constants.ZERO_FLOAT)
        self.maxApplyRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'maxApplyRadius', component_constants.ZERO_FLOAT)
        self.arenaAimLimits = ArenaAimLimits.readConfig(xmlCtx, section, b'arenaAimLimits')
        self.readyPrefab = _xml.readStringOrNone(xmlCtx, section, b'readyPrefab')
        if IS_CLIENT:
            self.aimCircleVisual = _xml.readStringOrNone(xmlCtx, section, b'aimCircleVisual')
            self.shotPrefab = _xml.readStringOrNone(xmlCtx, section, b'shotPrefab')
            self.chargePrefab = _xml.readStringOrNone(xmlCtx, section, b'chargePrefab')
        return


class WTHyperionModB(WTHyperionModA):

    def _readConfig(self, xmlCtx, section):
        super(WTHyperionModB, self)._readConfig(xmlCtx, section)
        self.shotRadius = _xml.readFloat(xmlCtx, section, b'shotRadius', 0.0)
        self.destroyDelay = _xml.readFloat(xmlCtx, section, b'destroyDelay', 0.0)
        return


class WTTeleportModA(Equipment, WTBaseEquipment):

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTTeleportModA, self)._readConfig(xmlCtx, section)
        self.consumeSeconds = _xml.readInt(xmlCtx, section, b'consumeSeconds', 0)
        self.debuffFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'debuffFactors')
        self.prefabDeparture = _xml.readStringOrNone(xmlCtx, section, b'prefabDeparture')
        self.prefabDestination = _xml.readStringOrNone(xmlCtx, section, b'prefabDestination')
        return


class WTTeleportModB(WTTeleportModA):
    pass


class WTClone(Equipment, WTBaseEquipment, ArcadeEquipmentConfigReader):

    def __init__(self):
        super(WTClone, self).__init__()
        self.cloneSettings = {}
        self.cooldownSeconds = component_constants.ZERO_FLOAT
        self.shuffleOwner = False
        self.useVehPosition = False
        self.instantCooldown = False
        self.__initSelectorSettings()
        self.initArcadeInformation()
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        if self.consumeSeconds != 0:
            LOG_WARNING(b'WTClone consumeSeconds not equals to zero. Unsupported.')
        self.consumeSeconds = 0.1
        self.readArcadeInformation(xmlCtx, section)
        self.cooldownSeconds = _xml.readFloat(xmlCtx, section, b'cooldownSeconds')
        self.shuffleOwner = _xml.readBool(xmlCtx, section, b'shuffleOwner')
        self.useVehPosition = _xml.readBool(xmlCtx, section, b'useVehPosition')
        self.__readCloneSettings(xmlCtx, section[b'cloneSettings'])
        self.__readSelectorSettings(xmlCtx, section)
        return

    def __initSelectorSettings(self):
        self.areaLength = component_constants.ZERO_FLOAT
        self.areaWidth = component_constants.ZERO_FLOAT
        self.areaVisual = None
        self.areaColor = component_constants.ZERO_INT
        return

    def __readCloneSettings(self, xmlCtx, section):
        self.cloneSettings[b'vehName'] = _xml.readStringOrNone(xmlCtx, section, b'vehName')
        botConfigName = _xml.readStringOrNone(xmlCtx, section, b'botConfig')
        self.cloneSettings[b'botConfig'] = (b'bots/{}.xml').format(botConfigName)
        self.cloneSettings[b'cloneCount'] = _xml.readInt(xmlCtx, section, b'cloneCount')
        if self.cloneSettings[b'cloneCount'] > 0:
            self.cloneSettings[b'cloneRadius'] = _xml.readInt(xmlCtx, section, b'cloneRadius')
        self.cloneSettings[b'cloneLifetime'] = _xml.readFloat(xmlCtx, section, b'cloneLifetime')
        self.cloneSettings[b'cloneProperties'] = []
        self.cloneSettings[b'cloneFactors'] = {}
        cloneProperties = _xml.readStringOrNone(xmlCtx, section, b'cloneProperties')
        self.cloneSettings[b'cloneProperties'] = cloneProperties.split() or []
        if b'cloneFactors' in section.keys():
            self.cloneSettings[b'cloneFactors'] = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'cloneFactors')
        return

    def __readSelectorSettings(self, xmlCtx, section):
        self.areaWidth = _xml.readFloat(xmlCtx, section, b'areaWidth')
        self.areaLength = _xml.readFloat(xmlCtx, section, b'areaLength')
        self.areaVisual = _xml.readString(xmlCtx, section, b'areaVisual')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        return


class WTStunArea(Equipment, WTBaseEquipment):
    __slots__ = (b'damageRadius', b'effects', b'components', b'debuffDuration', b'shotData', b'effectsIndex')

    def __init__(self):
        super(WTStunArea, self).__init__()
        self.damageRadius = component_constants.ZERO_INT
        self.effects = component_constants.EMPTY_DICT
        self.components = component_constants.EMPTY_DICT
        self.debuffDuration = component_constants.ZERO_INT
        self.shotData = component_constants.EMPTY_DICT
        self.effectsIndex = component_constants.ZERO_INT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTStunArea, self)._readConfig(xmlCtx, section)
        self.damageRadius = section.readInt(b'damageRadius')
        self.debuffDuration = section.readInt(b'debuffDuration')
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        if IS_CLIENT:
            self.effects = _getVisualEffects(xmlCtx, section, self.debuffDuration)
        if section.has_key(b'shotData'):
            self.shotData = _readShotData(xmlCtx, section)
        if section.has_key(b'shotEffect'):
            self.effectsIndex = vehicles.g_cache.shotEffectsIndexes[_xml.readString(xmlCtx, section, b'shotEffect')]
        return


def _readFactorAppliers(xmlCtx, section):
    paramsSection = _xml.getSubsection(xmlCtx, section, b'params')
    return {b'factors': (VehicleFactorsXmlReader.readFactors(xmlCtx, paramsSection, b'factors')), 
       b'onceDamage': (paramsSection.readInt(b'onceDamage'))}


def _readAbilityLock(xmlCtx, section):
    paramsSection = _xml.getSubsection(xmlCtx, section, b'params')
    vehicleParams = _xml.getSubsection(xmlCtx, paramsSection, b'vehicleParams')
    result = {b'vehicleParams': {}}
    for vehicleSection in vehicleParams.values():
        vehName = vehicleSection.readString(b'name')
        vehCD = vehicles.makeVehicleTypeCompDescrByName(vehName)
        result[b'vehicleParams'][vehCD] = vehicleSection.readString(b'lockedAbilities').split()

    return result


def _readDynamicComponents(xmlCtx, section):
    paramsSection = _xml.getSubsection(xmlCtx, section, b'params')
    factorsByLevelSection = _xml.getSubsection(xmlCtx, paramsSection, b'factorsByLevel')
    factorsByLevel = []
    for factorsSection in factorsByLevelSection.values():
        factors = VehicleFactorsXmlReader.readFactors(xmlCtx, factorsSection, b'factors')
        factorsByLevel.append(factors)

    return {b'factors': factorsByLevel}


_COMPONENT_READERS = {b'WTVehicleFactorAppliers': _readFactorAppliers, 
   b'WTVehicleAbilityLock': _readAbilityLock, 
   b'WTVehicleDynamicFactors': _readDynamicComponents}

def _readComponents(xmlCtx, section):
    componentsSection = _xml.getSubsection(xmlCtx, section, b'components')
    componentsData = {}
    for component in componentsSection.values():
        name = component.readString(b'name')
        key = component.readString(b'key')
        componentsData[(name, key)] = _COMPONENT_READERS[name](xmlCtx, component)

    return componentsData


def _readShotData(xmlCtx, section):
    shellSection = _xml.getSubsection(xmlCtx, section, b'shotData')
    shotData = {}
    shotData[b'shellName'] = shellSection.readString(b'shellName')
    shotData[b'shotPiercing100m'] = shellSection.readInt(b'shotPiercing100m')
    shotData[b'shotPiercing500m'] = shellSection.readInt(b'shotPiercing500m')
    shotData[b'shotSpeed'] = shellSection.readInt(b'shotSpeed')
    shotData[b'shotGravity'] = shellSection.readFloat(b'shotGravity')
    shotData[b'shotMaxDistance'] = shellSection.readInt(b'shotMaxDistance')
    shotData[b'maxHeight'] = shellSection.readInt(b'maxHeight')
    return shotData


def _getSequences(xmlCtx, section, sequenceDuration=0):
    sequences = {}
    data = _xml.getSubsection(xmlCtx, section, b'sequences', False)
    if data is None:
        return sequences
    else:

        def getSequenceData(section):
            sequences = {}
            for _, subSec in section.items():
                sequenceID = subSec.readInt(b'sequenceID', 0)
                seqDurationConfig = subSec.readFloat(b'duration', 0.0)
                sequencesData = {b'path': (subSec.readString(b'path')), 
                   b'bindNode': (subSec.readString(b'bindNode')), 
                   b'loopCount': (subSec.readInt(b'loopCount', -1)), 
                   b'duration': (seqDurationConfig if seqDurationConfig else sequenceDuration)}
                if sequenceID in sequences:
                    LOG_WARNING((b'Sequence with ID {sequenceID} is already exist').format(sequenceID=sequenceID))
                sequences[sequenceID] = sequencesData

            return sequences

        owner = _xml.getSubsection(xmlCtx, data, b'owner', False)
        if owner is not None:
            sequences[b'owner'] = getSequenceData(owner)
        enemy = _xml.getSubsection(xmlCtx, data, b'enemy', False)
        if enemy is not None:
            sequences[b'enemy'] = getSequenceData(enemy)
        teamMate = _xml.getSubsection(xmlCtx, data, b'teamMate', False)
        if teamMate is not None:
            sequences[b'teamMate'] = getSequenceData(teamMate)
        return sequences


def _getVisualEffects(xmlCtx, section, sequenceDuration=0):
    effects = {}
    if not IS_CLIENT:
        return effects
    if not section.has_key(b'visualEffects'):
        return effects
    visualEffectsSection = section[b'visualEffects']
    effects[b'sequences'] = _getSequences(xmlCtx, visualEffectsSection, sequenceDuration)
    return effects


def _getHunterVisualEffects(xmlCtx, section):
    effects = {}
    if not section.has_key(b'hunterVisualEffects'):
        return effects
    hunterVisualEffectsSection = section[b'hunterVisualEffects']
    for hunter in hunterVisualEffectsSection.values():
        vehName = _xml.readStringOrNone(xmlCtx, hunter, b'vehicle')
        prefab = _xml.readStringOrNone(xmlCtx, hunter, b'prefab')
        effects[vehName] = prefab

    return effects


def _getProcedureEffects(xmlCtx, section):
    procedureEffects = []
    procedureEffectsSection = _xml.getSubsection(xmlCtx, section, b'procedureEffects', False)
    if procedureEffectsSection is None:
        return procedureEffects
    else:
        for effectSection in procedureEffectsSection.values():
            effectPath = effectSection.asString.strip()
            if effectPath:
                procedureEffects.append(effectPath)

        return procedureEffects


class WTChargedShot(Equipment, WTBaseEquipment):
    __slots__ = (b'factors', b'moduleDamageFactors', b'shotData')

    def __init__(self):
        super(WTChargedShot, self).__init__()
        self.factors = component_constants.EMPTY_DICT
        self.moduleDamageFactors = component_constants.EMPTY_DICT
        self.shotData = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTChargedShot, self)._readConfig(xmlCtx, section)
        self.factors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'factors')
        self.moduleDamageFactors = self.__readModuleDamageFactors(xmlCtx, section)
        if section.has_key(b'shotData'):
            self.shotData = _readShotData(xmlCtx, section)
        return

    def __readModuleDamageFactors(self, xmlCtx, section):
        res = {}
        subsection = _xml.getSubsection(xmlCtx, section, b'moduleDamageFactors')
        for factor, _ in subsection.items():
            res[factor] = subsection.readFloat(factor)

        return res


class WTExplosiveShot(Equipment, WTBaseEquipment):
    __slots__ = (b'damage', b'factors', b'damageRadius', b'arenaPrefab', b'shotData', b'effectsIndex')

    def __init__(self):
        super(WTExplosiveShot, self).__init__()
        self.damage = component_constants.ZERO_INT
        self.factors = component_constants.EMPTY_DICT
        self.damageRadius = component_constants.ZERO_INT
        self.barrelFlashPrefab = component_constants.EMPTY_STRING
        self.barrelFlashPrefabUnloadTimeoutAfterShot = component_constants.ZERO_FLOAT
        self.shotData = component_constants.EMPTY_STRING
        self.effectsIndex = component_constants.ZERO_INT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTExplosiveShot, self)._readConfig(xmlCtx, section)
        self.factors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'factors')
        self.damage = _xml.readInt(xmlCtx, section, b'damage', 0)
        self.damageRadius = section.readInt(b'damageRadius')
        if IS_CLIENT:
            self.barrelFlashPrefab = _xml.readString(xmlCtx, section, b'barrelFlashPrefab')
            self.barrelFlashPrefabUnloadTimeoutAfterShot = _xml.readFloat(xmlCtx, section, b'barrelFlashPrefabUnloadTimeoutAfterShot')
        if section.has_key(b'shotData'):
            self.shotData = _readShotData(xmlCtx, section)
        if section.has_key(b'shotEffect'):
            self.effectsIndex = vehicles.g_cache.shotEffectsIndexes[_xml.readString(xmlCtx, section, b'shotEffect')]
        return


class WTNitro(Equipment, WTBaseEquipment):

    def __init__(self):
        super(WTNitro, self).__init__()
        self.factors = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTNitro, self)._readConfig(xmlCtx, section)
        self.factors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'factors')
        return


class WTDamageShield(Equipment, WTBaseEquipment):

    def __init__(self):
        super(WTDamageShield, self).__init__()
        self.factors = component_constants.EMPTY_DICT
        self.durationSeconds = component_constants.ZERO_INT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTDamageShield, self)._readConfig(xmlCtx, section)
        self.factors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'factors')
        self.durationSeconds = section.readInt(b'durationSeconds')
        return


class WTBarrier(Equipment, WTBaseEquipment):
    __slots__ = (b'settingDistance', b'duration', b'staticPrefab', b'components')

    def __init__(self):
        super(WTBarrier, self).__init__()
        self.settingDistance = component_constants.ZERO_FLOAT
        self.duration = component_constants.ZERO_FLOAT
        self.staticPrefab = component_constants.EMPTY_STRING
        self.components = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        self.rawTags = section.readString(b'rawTags').split()
        return

    def _readConfig(self, xmlCtx, section):
        super(WTBarrier, self)._readConfig(xmlCtx, section)
        self.settingDistance = section.readFloat(b'settingDistance')
        self.duration = section.readFloat(b'duration')
        self.staticPrefab = section.readString(b'staticPrefab')
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        return


class WTImpulseModA(Equipment, WTBaseEquipment):
    __slots__ = (b'radius', b'debuffDuration', b'consumeSeconds', b'components', b'reloadTimes')

    def __init__(self):
        super(WTImpulseModA, self).__init__()
        self.radius = component_constants.ZERO_INT
        self.debuffDuration = component_constants.ZERO_INT
        self.consumeSeconds = component_constants.ZERO_INT
        self.components = component_constants.EMPTY_DICT
        self.reloadTimes = component_constants.EMPTY_TUPLE
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTImpulseModA, self)._readConfig(xmlCtx, section)
        self.radius = section.readInt(b'radius')
        self.debuffDuration = section.readInt(b'debuffDuration')
        self.consumeSeconds = section.readInt(b'consumeSeconds')
        self.reloadTimes = tuple(map(int, section.readString(b'reloadTimes').split(b' ')))
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        return


class WTVampirism(Equipment, WTBaseEquipment):
    __slots__ = (b'partOfDamageToHP',)

    def __init__(self):
        super(WTVampirism, self).__init__()
        self.partOfDamageToHP = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(WTVampirism, self)._readConfig(xmlCtx, section)
        self.partOfDamageToHP = _xml.readFloat(xmlCtx, section, b'partOfDamageToHP', 0.0)
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTDecreaseReloadTime(Equipment, WTBaseEquipment):

    def __init__(self):
        super(WTDecreaseReloadTime, self).__init__()
        self.components = component_constants.EMPTY_DICT
        self.ignoredReasons = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        if section.has_key(b'ignoredReasons'):
            self.ignoredReasons = _xml.readTupleOfStrings(xmlCtx, section, b'ignoredReasons')
        super(WTDecreaseReloadTime, self)._readConfig(xmlCtx, section)
        return


class WTGroupRepair(Equipment, WTBaseEquipment):
    __slots__ = (b'healRangeRadius', b'instantHealthRestore', b'tickInterval', b'healAmountPerTick', b'healingAreaDuration', b'hunterEffects')

    def __init__(self):
        super(WTGroupRepair, self).__init__()
        self.healRangeRadius = component_constants.ZERO_INT
        self.instantHealthRestore = component_constants.ZERO_INT
        self.tickInterval = component_constants.ZERO_FLOAT
        self.healAmountPerTick = component_constants.ZERO_INT
        self.healingAreaDuration = component_constants.ZERO_INT
        self.hunterEffects = component_constants.EMPTY_DICT
        return

    def _readConfig(self, xmlCtx, section):
        super(WTGroupRepair, self)._readConfig(xmlCtx, section)
        self.healRangeRadius = _xml.readInt(xmlCtx, section, b'healRangeRadius', 0)
        self.instantHealthRestore = _xml.readInt(xmlCtx, section, b'instantHealthRestore', 0)
        self.tickInterval = _xml.readFloat(xmlCtx, section, b'tickInterval', 0.0)
        self.healAmountPerTick = _xml.readInt(xmlCtx, section, b'healAmountPerTick', 0.0)
        self.healingAreaDuration = _xml.readInt(xmlCtx, section, b'healingAreaDuration', 1)
        self.hunterEffects = _getHunterVisualEffects(xmlCtx, section)
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTMissile(Equipment, WTBaseEquipment):
    __slots__ = (b'missilePrefab', b'components')

    def __init__(self):
        super(WTMissile, self).__init__()
        self.missilePrefab = component_constants.EMPTY_STRING
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        self.rawTags = section.readString(b'rawTags').split()
        return

    def _readConfig(self, xmlCtx, section):
        super(WTMissile, self)._readConfig(xmlCtx, section)
        self.missilePrefab = section.readString(b'missilePrefab')
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        return


class WTSmokeScreen(Smoke, WTBaseEquipment):

    def _readConfig(self, xmlCtx, scriptSection):
        super(WTSmokeScreen, self)._readConfig(xmlCtx, scriptSection)
        if self.consumeSeconds is None:
            self.consumeSeconds = 0
        if self.consumeSeconds > 0:
            LOG_WARNING(b'consumeSeconds was read as %s and reset to 0 for WTSmokeScreen' % self.consumeSeconds)
            self.consumeSeconds = 0
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTPlasmaRetention(Equipment, WTBaseEquipment):

    def __init__(self):
        super(WTPlasmaRetention, self).__init__()
        self.plasmaSavedOnDeath = component_constants.ZERO_INT
        return

    def _readConfig(self, xmlCtx, section):
        super(WTPlasmaRetention, self)._readConfig(xmlCtx, section)
        self.plasmaSavedOnDeath = _xml.readInt(xmlCtx, section, b'plasmaSavedOnDeath', 0)
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return


class WTStunAreaModA(Equipment, WTBaseEquipment):
    __slots__ = (b'damageRadius', b'effects', b'components', b'debuffDuration')

    def __init__(self):
        super(WTStunAreaModA, self).__init__()
        self.damageRadius = component_constants.ZERO_INT
        self.effects = component_constants.EMPTY_DICT
        self.components = component_constants.EMPTY_DICT
        self.debuffDuration = component_constants.ZERO_INT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTStunAreaModA, self)._readConfig(xmlCtx, section)
        self.damageRadius = section.readInt(b'damageRadius')
        self.debuffDuration = section.readInt(b'debuffDuration')
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        if IS_CLIENT:
            self.effects = _getVisualEffects(xmlCtx, section, self.debuffDuration)
        return


class WTIncreaseDamage(Equipment, WTBaseEquipment):

    def __init__(self):
        super(WTIncreaseDamage, self).__init__()
        self.components = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        super(WTIncreaseDamage, self)._readConfig(xmlCtx, section)
        return


class WTExtractorShot(Equipment, WTBaseEquipment):
    __slots__ = (b'damageRadius', b'shotData', b'damageMultiplierPerPlasma', b'maxPlasmaTakeFromHunter', b'maxPlasmaCounter', b'debuffDuration', b'components', b'effects')

    def __init__(self):
        super(WTExtractorShot, self).__init__()
        self.damageRadius = component_constants.ZERO_INT
        self.shotData = component_constants.EMPTY_DICT
        self.damageMultiplierPerPlasma = component_constants.ZERO_FLOAT
        self.maxPlasmaTakeFromHunter = component_constants.ZERO_INT
        self.maxPlasmaCounter = component_constants.ZERO_INT
        self.debuffDuration = component_constants.ZERO_INT
        self.components = component_constants.EMPTY_DICT
        self.effects = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTExtractorShot, self)._readConfig(xmlCtx, section)
        self.damageRadius = section.readInt(b'damageRadius')
        self.damageMultiplierPerPlasma = section.readFloat(b'damageMultiplierPerPlasma')
        self.maxPlasmaTakeFromHunter = section.readInt(b'maxPlasmaTakeFromHunter')
        self.maxPlasmaCounter = section.readInt(b'maxPlasmaCounter')
        self.debuffDuration = section.readInt(b'debuffDuration')
        if section.has_key(b'components'):
            self.components = _readComponents(xmlCtx, section)
        if section.has_key(b'shotData'):
            self.shotData = _readShotData(xmlCtx, section)
        if IS_CLIENT:
            self.effects = _getVisualEffects(xmlCtx, section)
        return


class WTExplosiveDamageShield(Equipment, WTBaseEquipment):

    def __init__(self):
        super(WTExplosiveDamageShield, self).__init__()
        self.factors = component_constants.EMPTY_DICT
        self.maxDamage = component_constants.ZERO_INT
        self.explosionDamageFactor = 1.0
        self.effects = component_constants.EMPTY_DICT
        return

    def _readBasicConfig(self, xmlCtx, section):
        Equipment._readBasicConfig(self, xmlCtx, section)
        WTBaseEquipment.readExtraData(self, xmlCtx, section)
        return

    def _readConfig(self, xmlCtx, section):
        super(WTExplosiveDamageShield, self)._readConfig(xmlCtx, section)
        self.factors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'factors')
        self.damageRadius = section.readInt(b'damageRadius')
        self.maxDamage = section.readInt(b'maxDamage')
        self.explosionDamageFactor = section.readFloat(b'explosionDamageFactor')
        return


class WTDome(Equipment, WTBaseEquipment):
    __slots__ = (b'receiveDamageFactor', b'objPrefab')

    def __init__(self):
        super(WTDome, self).__init__()
        self.moduleDamageFactor = component_constants.ZERO_FLOAT
        self.receiveDamageFactor = component_constants.ZERO_FLOAT
        self.objPrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(WTDome, self)._readConfig(xmlCtx, section)
        self.receiveDamageFactor = section.readFloat(b'receiveDamageFactor', 1.0)
        self.moduleDamageFactor = section.readFloat(b'moduleDamageFactor', 1.0)
        self.objPrefab = section.readString(b'objPrefab')
        return
