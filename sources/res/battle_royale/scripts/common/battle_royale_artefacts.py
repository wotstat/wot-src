from __future__ import absolute_import, division
from Math import Vector3
from constants import IS_CLIENT, ATTACK_REASON, ATTACK_REASON_INDICES, SERVER_TICK_LENGTH
from items.artefacts import Repairkit, CountableConsumableConfigReader, Equipment, VehicleFactorsXmlReader, DOTParams, HOTParams, Bomber, ArcadeEquipmentConfigReader, Smoke, TooltipConfigReader, AreaMarkerConfigReader, HealPointConfigReader, PREDEFINED_HEAL_GROUPS, Minefield
from items import _xml, vehicles
from items.components import component_constants
from items.stun import g_cfg as stunConfig
if IS_CLIENT:
    from helpers import i18n
    from gui.impl.backport import text
    from gui.impl.backport.backport_system_locale import getNiceNumberFormat, getIntegralFormat
    from gui.impl.gen import R

class BattleDescriptionConfigReader(object):
    _BATTLE_DESCRIPTION_SLOTS = (b'battleDescription',)

    def initBattleDescriptionSlots(self):
        self.battleDescription = component_constants.EMPTY_STRING
        return

    def readBattleDescriptionConfig(self, xmlCtx, section):
        if IS_CLIENT:
            self.battleDescription = _xml.readString(xmlCtx, section, b'battleDescription')
        return


class RepairkitBattleRoyale(Repairkit, CountableConsumableConfigReader):

    def __init__(self):
        super(RepairkitBattleRoyale, self).__init__()
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(RepairkitBattleRoyale, self)._readConfig(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        return


class AfterburningBattleRoyale(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = (b'consumeSeconds', b'enginePowerFactor', b'maxSpeedFactor', b'vehicleRotationSpeed', b'deploySeconds', b'rechargeSeconds') + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS

    def __init__(self):
        super(AfterburningBattleRoyale, self).__init__()
        self.consumeSeconds = component_constants.ZERO_INT
        self.enginePowerFactor = component_constants.ZERO_FLOAT
        self.maxSpeedFactor = component_constants.ZERO_FLOAT
        self.vehicleRotationSpeed = component_constants.ZERO_FLOAT
        self.deploySeconds = component_constants.ZERO_FLOAT
        self.rechargeSeconds = component_constants.ZERO_FLOAT
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.consumeSeconds = _xml.readInt(xmlCtx, scriptSection, b'consumeSeconds', 0)
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'enginePowerFactor')
        self.maxSpeedFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'maxSpeedFactor')
        self.vehicleRotationSpeed = _xml.readPositiveFloat(xmlCtx, scriptSection, b'vehicleRotationSpeed')
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def updateVehicleAttrFactors(self, vehicleDescr, factors, aspect):
        try:
            factors[b'engine/power'] *= self.enginePowerFactor
            factors[b'vehicle/maxSpeed'] *= self.maxSpeedFactor
        except Exception:
            pass

        return

    def _getDescription(self, descr):
        localizeDescr = super(AfterburningBattleRoyale, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        enginePowerFactor = getNiceNumberFormat(100 * self.enginePowerFactor - 100)
        return i18n.makeString(descr, enginePowerFactor=enginePowerFactor + percentSymbol, maxSpeedFactor=int(self.maxSpeedFactor), consumeSeconds=int(self.consumeSeconds))


class InfluenceZone(object):
    __slots__ = (b'radius', b'height', b'depth', b'timer', b'terrainResistance', b'debuffFactors', b'dotParams', b'hotParams', b'influenceType', b'fireEffectName', b'componentName')

    def __init__(self):
        self.radius = component_constants.ZERO_FLOAT
        self.height = component_constants.ZERO_FLOAT
        self.depth = component_constants.ZERO_FLOAT
        self.timer = component_constants.ZERO_FLOAT
        self.terrainResistance = component_constants.ZERO_FLOAT
        self.debuffFactors = component_constants.EMPTY_DICT
        self.dotParams = component_constants.EMPTY_DICT
        self.hotParams = component_constants.EMPTY_DICT
        self.influenceType = component_constants.INFLUENCE_ALL
        self.fireEffectName = component_constants.EMPTY_STRING
        self.componentName = None
        return

    def _readConfig(self, xmlCtx, section):
        self.debuffFactors = component_constants.EMPTY_DICT
        self.dotParams = component_constants.EMPTY_DICT
        self.hotParams = component_constants.EMPTY_DICT
        self.radius = _xml.readPositiveFloat(xmlCtx, section, b'radius')
        self.height = _xml.readPositiveFloat(xmlCtx, section, b'height')
        self.depth = _xml.readNonNegativeFloat(xmlCtx, section, b'depth', 0.0)
        self.timer = _xml.readPositiveFloat(xmlCtx, section, b'timer')
        if section.has_key(b'fireEffectName'):
            self.fireEffectName = _xml.readString(xmlCtx, section, b'fireEffectName')
        if section.has_key(b'terrainResistance'):
            self.terrainResistance = _xml.readPositiveFloat(xmlCtx, section, b'terrainResistance')
        if section.has_key(b'influenceType'):
            self.influenceType = _xml.readInt(xmlCtx, section, b'influenceType', component_constants.INFLUENCE_ALL, component_constants.INFLUENCE_ENEMY)
        if section.has_key(b'debuffFactors'):
            self.debuffFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'debuffFactors')
        if section.has_key(b'dotParams'):
            self.dotParams = DOTParams()
            self.dotParams._readConfig(xmlCtx, section[b'dotParams'])
        if section.has_key(b'hotParams'):
            self.hotParams = HOTParams()
            self.hotParams._readConfig(xmlCtx, section[b'hotParams'])
        return


class TrapPoint(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'influenceZone',)

    def __init__(self):
        super(TrapPoint, self).__init__()
        self.radius = component_constants.ZERO_FLOAT
        self.zonesCount = component_constants.ZERO_FLOAT
        self.influenceZone = InfluenceZone()
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(TrapPoint, self)._readConfig(xmlCtx, scriptSection)
        self.influenceZone._readConfig(xmlCtx, scriptSection[b'influenceZone'])
        self.radius = self.influenceZone.radius
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        localizeDescr = super(TrapPoint, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        if self.influenceZone.debuffFactors:
            vehicleMaxSpeed = getNiceNumberFormat(100 - self.influenceZone.debuffFactors[b'vehicle/maxSpeed'] * 100)
            gunReloadTime = getNiceNumberFormat(self.influenceZone.debuffFactors[b'gun/reloadTime'] * 100 - 100)
            return i18n.makeString(descr, duration=int(self.influenceZone.timer), vehicleMaxSpeed=vehicleMaxSpeed + percentSymbol, gunReloadTime=gunReloadTime + percentSymbol)
        if self.influenceZone.hotParams:
            healPerTick = getNiceNumberFormat(self.influenceZone.hotParams.healPerTick * 100)
            return i18n.makeString(descr, healPerTick=healPerTick + percentSymbol, timer=int(self.influenceZone.timer))
        return b''


class BomberArcade(Bomber, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__ = Bomber.__slots__ + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS

    def __init__(self):
        super(BomberArcade, self).__init__()
        self.initArcadeInformation()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(BomberArcade, self)._readConfig(xmlCtx, scriptSection)
        if scriptSection.has_key(b'influenceZone'):
            self.influenceZone = InfluenceZone()
            self.influenceZone._readConfig(xmlCtx, scriptSection[b'influenceZone'])
        self.readArcadeInformation(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        return


class BomberArcadeWithOwnDamage(Bomber, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__ = Bomber.__slots__ + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'abilityRadius', b'directHitRadius', b'stunRadius', b'maxDamage', b'minDamage', b'maxModuleDamage', b'minModuleDamage', b'damageSpread', b'stunTime', b'minStunTime')

    def __init__(self):
        super(BomberArcadeWithOwnDamage, self).__init__()
        self.initArcadeInformation()
        self.initOwnDamageParams()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(BomberArcadeWithOwnDamage, self)._readConfig(xmlCtx, scriptSection)
        self.readArcadeInformation(xmlCtx, scriptSection)
        self._readOwnDamageConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = self._prepareDescription(self.longDescription)
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def initOwnDamageParams(self):
        self.abilityRadius = component_constants.ZERO_FLOAT
        self.directHitRadius = component_constants.ZERO_FLOAT
        self.stunRadius = component_constants.ZERO_FLOAT
        self.maxDamage = component_constants.ZERO_INT
        self.minDamage = component_constants.ZERO_INT
        self.maxModuleDamage = component_constants.ZERO_INT
        self.minModuleDamage = component_constants.ZERO_INT
        self.damageSpread = component_constants.ZERO_FLOAT
        self.stunTime = component_constants.ZERO_INT
        self.minStunTime = component_constants.ZERO_INT
        return

    def _readOwnDamageConfig(self, xmlCtx, scriptSection):
        self.abilityRadius = _xml.readPositiveFloat(xmlCtx, scriptSection, b'abilityRadius')
        self.directHitRadius = _xml.readPositiveFloat(xmlCtx, scriptSection, b'directHitRadius')
        self.stunRadius = _xml.readPositiveFloat(xmlCtx, scriptSection, b'stunRadius')
        self.maxDamage = _xml.readPositiveInt(xmlCtx, scriptSection, b'maxDamage')
        self.minDamage = _xml.readPositiveInt(xmlCtx, scriptSection, b'minDamage')
        self.maxModuleDamage = _xml.readPositiveInt(xmlCtx, scriptSection, b'maxModuleDamage')
        self.minModuleDamage = _xml.readPositiveInt(xmlCtx, scriptSection, b'minModuleDamage')
        self.damageSpread = _xml.readPositiveFloat(xmlCtx, scriptSection, b'damageSpread')
        self.stunTime = _xml.readPositiveInt(xmlCtx, scriptSection, b'stunTime')
        self.minStunTime = _xml.readPositiveInt(xmlCtx, scriptSection, b'minStunTime')
        return

    def _getDescription(self, descr):
        localizeDescr = super(BomberArcadeWithOwnDamage, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        return i18n.makeString(descr, minDamage=int(self.minDamage), maxDamage=int(self.maxDamage), delay=int(self.delay))


class SmokeArcade(Smoke, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__ = Smoke.__slots__ + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS

    def __init__(self):
        super(SmokeArcade, self).__init__()
        self.orthogonalDir = True
        self.initArcadeInformation()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readSmokeConfig(xmlCtx, scriptSection)
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds')
        self.readArcadeInformation(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = self._prepareDescription(self.longDescription)
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _prepareDescription(self, descr):
        if self.dotParams:
            percentSymbol = text(R.strings.common.common.percent())
            damagePerTick = getNiceNumberFormat(self.dotParams.damagePerTick * 100)
            preparedDescr = i18n.makeString(descr, damagePerTick=damagePerTick + percentSymbol, duration=int(self.totalDuration))
        else:
            preparedDescr = i18n.makeString(self.longDescription, duration=int(self.totalDuration))
        return preparedDescr


class SelfBuff(Equipment, TooltipConfigReader, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = (b'duration', b'increaseFactors', b'longDescription', b'cooldownTime') + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS

    def __init__(self):
        super(SelfBuff, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.increaseFactors = {}
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.cooldownTime = _xml.readFloat(xmlCtx, scriptSection, b'cooldownTime', 0.0)
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration', 0)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'increaseFactors')
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        return self._prepareDescription(self.longDescription)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        gunAimingTime = getNiceNumberFormat(100 - self.increaseFactors[b'gun/aimingTime'] * 100)
        return i18n.makeString(descr, duration=int(self.duration), gunAimingTime=gunAimingTime + percentSymbol)


class Berserker(SelfBuff):
    __slots__ = (b'dotParams',)

    def __init__(self):
        super(Berserker, self).__init__()
        self.dotParams = DOTParams(ATTACK_REASON_INDICES[ATTACK_REASON.BERSERKER])
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.cooldownTime = _xml.readFloat(xmlCtx, scriptSection, b'cooldownTime', 0.0)
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration', 0)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'increaseFactors')
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        self.dotParams._readConfig(xmlCtx, scriptSection[b'dotParams'])
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        gunPiercing = getIntegralFormat(self.increaseFactors[b'gun/piercing'])
        gunAimingTime = getNiceNumberFormat(100 - self.increaseFactors[b'gun/aimingTime'] * 100)
        healthDebuff = getIntegralFormat(self.duration / self.dotParams.tickInterval * self.dotParams.damagePerTick * 100)
        return i18n.makeString(descr, gunPiercing=gunPiercing, gunAimingTime=gunAimingTime + percentSymbol, healthDebuff=healthDebuff + percentSymbol, duration=int(self.duration))


class _ClientSpawnBotVisuals(object):
    __slots__ = (b'markerPositionOffset', b'markerScale', b'deliveringAnimationDuration', b'deliveringAnimationStartDelay', b'highlightDelay')

    def __init__(self, xmlCtx, scriptSection):
        self.markerPositionOffset = _xml.readVector3(xmlCtx, scriptSection, b'markerPositionOffset', Vector3(0, 0, 0))
        self.markerScale = _xml.readVector3(xmlCtx, scriptSection, b'markerScale', Vector3(1, 1, 1))
        self.deliveringAnimationDuration = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'deliveringAnimationDuration', 0.0)
        self.deliveringAnimationStartDelay = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'deliveringAnimationStartDelay', 0.0)
        self.highlightDelay = _xml.readFloat(xmlCtx, scriptSection, b'highlightDelay', 0.0)
        return


class BRHealPoint(Equipment, TooltipConfigReader, CountableConsumableConfigReader, HealPointConfigReader, BattleDescriptionConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CountableConsumableConfigReader._CONSUMABLE_SLOTS + HealPointConfigReader._HEAL_POINT_SLOTS + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'cooldownTime',)

    def __init__(self):
        super(BRHealPoint, self).__init__()
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.initHealPointSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'cooldownTime')
        self.readHealPointConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = self._prepareDescription(self.longDescription)
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        healPerTick = getNiceNumberFormat(100 * self.healPerTick)
        return i18n.makeString(descr, healPerTick=healPerTick + percentSymbol, duration=int(self.duration))


class RegenerationKit(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = (b'healthRegenPerTick', b'initialHeal', b'healTime', b'healGroup', b'tickInterval')

    def __init__(self):
        super(RegenerationKit, self).__init__()
        self.healthRegenPerTick = component_constants.ZERO_FLOAT
        self.initialHeal = component_constants.ZERO_FLOAT
        self.healTime = component_constants.ZERO_FLOAT
        self.healGroup = None
        self.tickInterval = 1.0
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.healthRegenPerTick = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'healthRegenPerTick', 0.0)
        self.initialHeal = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'initialHeal', 0.0)
        self.healTime = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'healTime', 0.0)
        self.healGroup = _xml.readIntOrNone(xmlCtx, scriptSection, b'healGroup')
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, scriptSection, b'tickInterval', 1.0)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        localizeDescr = super(RegenerationKit, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        healPerTickDuration = getIntegralFormat(self.healthRegenPerTick * self.healTime * 100)
        return i18n.makeString(descr, healPerTickDuration=healPerTickDuration + percentSymbol, duration=int(self.healTime))


class BRMinefield(Minefield, BattleDescriptionConfigReader):
    __slots__ = Minefield.__slots__ + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS

    def __init__(self):
        super(BRMinefield, self).__init__()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(BRMinefield, self)._readConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = i18n.makeString(self.battleDescription, duration=int(self.mineParams.lifetime))
        return


class ConsumableSpawnBot(Equipment, TooltipConfigReader, CountableConsumableConfigReader, AreaMarkerConfigReader, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CountableConsumableConfigReader._CONSUMABLE_SLOTS + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + AreaMarkerConfigReader._MARKER_SLOTS_ + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'botType', b'botVehCompDescr', b'botLifeTime', b'botSpawnPointOffset', b'botXRayFactor', b'clientVisuals', b'explosionRadius', b'explosionDamage', b'explosionByShoot', b'damageReductionRate', b'delay', b'cooldownTime', b'disableAllyDamage')

    def __init__(self):
        super(ConsumableSpawnBot, self).__init__()
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.initArcadeInformation()
        self.initMarkerInformation()
        self.initBattleDescriptionSlots()
        self.botType = component_constants.EMPTY_STRING
        self.botVehCompDescr = component_constants.EMPTY_STRING
        self.botLifeTime = component_constants.ZERO_FLOAT
        self.botSpawnPointOffset = None
        self.botXRayFactor = 1.0
        self.explosionRadius = component_constants.ZERO_FLOAT
        self.explosionDamage = component_constants.ZERO_FLOAT
        self.explosionByShoot = False
        self.damageReductionRate = component_constants.ZERO_FLOAT
        self.clientVisuals = component_constants.EMPTY_DICT
        self.delay = component_constants.ZERO_FLOAT
        self.cooldownTime = component_constants.ZERO_INT
        self.disableAllyDamage = True
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readArcadeInformation(xmlCtx, scriptSection)
        self.readMarkerConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        self.botType = _xml.readString(xmlCtx, scriptSection, b'botType')
        self.botVehCompDescr = _xml.readString(xmlCtx, scriptSection, b'botVehCompDescr')
        self.delay = _xml.readFloat(xmlCtx, scriptSection, b'delay', 0.0)
        self.botLifeTime = _xml.readFloat(xmlCtx, scriptSection, b'botLifeTime', 0.0)
        self.botSpawnPointOffset = _xml.readVector3(xmlCtx, scriptSection, b'botSpawnPointOffset', Vector3())
        self.botXRayFactor = _xml.readFloat(xmlCtx, scriptSection, b'botXRayFactor', 0.0)
        self.explosionRadius = _xml.readFloat(xmlCtx, scriptSection, b'explosionRadius', 0.0)
        self.explosionDamage = _xml.readFloat(xmlCtx, scriptSection, b'explosionDamage', 0.0)
        self.explosionByShoot = _xml.readBool(xmlCtx, scriptSection, b'explosionByShoot', False)
        self.damageReductionRate = _xml.readFloat(xmlCtx, scriptSection, b'damageReductionRate', 0.0)
        self.clientRemovalNotificationDelay = _xml.readInt(xmlCtx, scriptSection, b'clientRemovalNotificationDelay', 0.0)
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds')
        self.disableAllyDamage = _xml.readBool(xmlCtx, scriptSection, b'disableAllyDamage', True)
        if IS_CLIENT:
            if scriptSection[b'clientVisuals'] is not None:
                self.clientVisuals = _ClientSpawnBotVisuals(scriptSection, scriptSection[b'clientVisuals'])
                self.longDescription = self._prepareDescription(self.longDescription)
                self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _prepareDescription(self, descr):
        return i18n.makeString(descr, botLifeTime=int(self.botLifeTime))


class ZonesCircle(Equipment):
    __slots__ = (b'influenceZone', b'radius', b'zonesCount', b'vehicleHeightMultiplier')

    def __init__(self):
        super(ZonesCircle, self).__init__()
        self.radius = component_constants.ZERO_FLOAT
        self.zonesCount = component_constants.ZERO_FLOAT
        self.vehicleHeightMultiplier = 1.0
        self.influenceZone = InfluenceZone()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(ZonesCircle, self)._readConfig(xmlCtx, scriptSection)
        self.radius = _xml.readFloat(xmlCtx, scriptSection, b'radius')
        self.zonesCount = _xml.readPositiveInt(xmlCtx, scriptSection, b'zonesCount')
        self.vehicleHeightMultiplier = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'vehicleHeightMultiplier')
        self.influenceZone._readConfig(xmlCtx, scriptSection[b'influenceZone'])
        return

    def _getDescription(self, descr):
        localizeDescr = super(ZonesCircle, self)._getDescription(descr)
        return i18n.makeString(localizeDescr, duration=int(self.influenceZone.timer))


class FireCircle(ZonesCircle, CountableConsumableConfigReader, BattleDescriptionConfigReader):

    def __init__(self):
        super(FireCircle, self).__init__()
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(FireCircle, self)._readConfig(xmlCtx, scriptSection)
        self.influenceZone.dotParams.attackReasonID = ATTACK_REASON_INDICES[ATTACK_REASON.FIRE_CIRCLE]
        self.influenceZone.componentName = b'VehicleFireCircleEffectComponent'
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        localizeDescr = super(ZonesCircle, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        dotParams = self.influenceZone.dotParams
        damagePerTickForInterval = getNiceNumberFormat(self.influenceZone.timer / dotParams.tickInterval * dotParams.damagePerTick * 100)
        return i18n.makeString(descr, damagePerTickForInterval=damagePerTickForInterval + percentSymbol, timer=int(self.influenceZone.timer))


class CorrodingShot(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'damagePercentAfterShot', b'canBeStoppedRepairKit', b'increaseFactors', b'dotEffectDuration', b'dotParams', b'tooltipMovie', b'effectsIndex')

    def __init__(self):
        super(CorrodingShot, self).__init__()
        self.damagePercentAfterShot = component_constants.ZERO_FLOAT
        self.canBeStoppedRepairKit = component_constants.ZERO_INT
        self.increaseFactors = {}
        self.dotParams = DOTParams(ATTACK_REASON_INDICES[ATTACK_REASON.CORRODING_SHOT])
        self.dotEffectDuration = component_constants.ZERO_INT
        self.tooltipMovie = component_constants.EMPTY_STRING
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.damagePercentAfterShot = _xml.readFloat(xmlCtx, scriptSection, b'damagePercentAfterShot', 0.0)
        self.canBeStoppedRepairKit = _xml.readBool(xmlCtx, scriptSection, b'canBeStoppedRepairKit', False)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'increaseFactors')
        self.dotEffectDuration = _xml.readInt(xmlCtx, scriptSection, b'dotEffectDuration', 0)
        self.dotParams._readConfig(xmlCtx, scriptSection[b'dotParams'])
        self.tooltipMovie = _xml.readStringOrEmpty(xmlCtx, scriptSection, b'tooltipMovie')
        self.effectsIndex = vehicles.g_cache.shotEffectsIndexes[_xml.readString(xmlCtx, scriptSection, b'shotEffect')]
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        localizeDescr = super(CorrodingShot, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        damagePerDotEffectDuration = getIntegralFormat(self.dotEffectDuration / self.dotParams.tickInterval * self.dotParams.damagePerTick * 100)
        return i18n.makeString(descr, damagePerDotEffectDuration=damagePerDotEffectDuration + percentSymbol, dotEffectDuration=int(self.dotEffectDuration))


class AdaptationHealthRestore(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'duration', b'areaVisual', b'immediatelyRestore', b'posteffectPrefab', b'restoringCoefficient', b'restoringCoefficientTeamMates', b'teamMateRestoringRadius')

    def __init__(self):
        super(AdaptationHealthRestore, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.restoringCoefficient = component_constants.ZERO_FLOAT
        self.restoringCoefficientTeamMates = component_constants.ZERO_FLOAT
        self.teamMateRestoringRadius = component_constants.ZERO_INT
        self.areaVisual = None
        self.posteffectPrefab = None
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(AdaptationHealthRestore, self)._readBasicConfig(xmlCtx, section)
        self.posteffectPrefab = _xml.readStringOrNone(xmlCtx, section, b'posteffectPrefab')
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration', 0)
        self.immediatelyRestore = _xml.readInt(xmlCtx, scriptSection, b'immediatelyRestore', 0.0)
        self.restoringCoefficient = _xml.readFloat(xmlCtx, scriptSection, b'restoringCoefficient', 0.0)
        self.restoringCoefficientTeamMates = _xml.readFloat(xmlCtx, scriptSection, b'restoringCoefficientTeamMates', 0.0)
        self.teamMateRestoringRadius = _xml.readInt(xmlCtx, scriptSection, b'teamMateRestoringRadius', 0)
        self.areaVisual = _xml.readStringOrNone(xmlCtx, scriptSection, b'areaVisual')
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        localizeDescr = super(AdaptationHealthRestore, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        restoringCoefficient = getNiceNumberFormat(100 * self.restoringCoefficient - 100)
        return i18n.makeString(descr, immediatelyRestore=int(self.immediatelyRestore), duration=int(self.duration), restoringCoefficient=restoringCoefficient + percentSymbol)


class ThunderStrike(Equipment, ArcadeEquipmentConfigReader, TooltipConfigReader, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'noOwner', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'delay', b'duration', b'damage', b'thunderCount', b'thunderPeriod', b'deployTime', b'cooldownTime', b'decreaseFactors', b'isDamageAll', b'canBeStoppedRepairKit')

    def __init__(self):
        super(ThunderStrike, self).__init__()
        self.initArcadeInformation()
        self.cooldownTime = component_constants.ZERO_INT
        self.canBeStoppedRepairKit = component_constants.ZERO_INT
        self.noOwner = False
        self.consumeAmmo = True
        self.duration = 0
        self.damage = 0
        self.thunderCount = 0
        self.thunderPeriod = 0
        self.areaLength = 0
        self.areaWidth = 0
        self.areaVisual = None
        self.areaColor = None
        self.damageRadius = 0
        self.decreaseFactors = {}
        self.isDamageAll = False
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'cooldownSeconds')
        self.canBeStoppedRepairKit = _xml.readBool(xmlCtx, scriptSection, b'canBeStoppedRepairKit', False)
        self.damageRadius = _xml.readInt(xmlCtx, scriptSection, b'damageRadius', 0)
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration', 0)
        self.delay = _xml.readPositiveFloat(xmlCtx, scriptSection, b'delay', 0)
        self.damage = _xml.readInt(xmlCtx, scriptSection, b'damage', 0)
        self.thunderCount = _xml.readInt(xmlCtx, scriptSection, b'thunderCount', 0)
        self.thunderPeriod = _xml.readPositiveFloat(xmlCtx, scriptSection, b'thunderPeriod', 0)
        self.areaLength = _xml.readPositiveFloat(xmlCtx, scriptSection, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, scriptSection, b'areaWidth')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, scriptSection, b'areaVisual')
        self.isDamageAll = _xml.readBool(xmlCtx, scriptSection, b'isDamageAll', False)
        self.decreaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'decreaseFactors')
        self.readArcadeInformation(xmlCtx, scriptSection)
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = self._prepareDescription(self.longDescription)
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _prepareDescription(self, descr):
        return i18n.makeString(descr, thunderCount=int(self.thunderCount), damage=int(self.damage), delay=int(self.delay))


class ShotPassion(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__ = BattleDescriptionConfigReader._BATTLE_DESCRIPTION_SLOTS + (b'duration', b'increaseFactors', b'enableRamDamage', b'enableHEDamage', b'damageIncreasePerShot', b'maxDamageIncreasePerShot', b'affectingAbilities', b'cooldownTime', b'enableThunderStrikeDamageIncrease', b'posteffectPrefab')

    def __init__(self):
        super(ShotPassion, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.damageIncreasePerShot = component_constants.ZERO_FLOAT
        self.maxDamageIncreasePerShot = component_constants.ZERO_FLOAT
        self.cooldownTime = component_constants.ZERO_INT
        self.initCountableConsumableSlots()
        self.initBattleDescriptionSlots()
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(ShotPassion, self)._readBasicConfig(xmlCtx, section)
        self.posteffectPrefab = _xml.readStringOrNone(xmlCtx, section, b'posteffectPrefab')
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration', 0)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'increaseFactors')
        self.damageIncreasePerShot = _xml.readFloat(xmlCtx, scriptSection, b'damageIncreasePerShot', component_constants.ZERO_FLOAT)
        self.maxDamageIncreasePerShot = _xml.readFloat(xmlCtx, scriptSection, b'maxDamageIncreasePerShot', component_constants.ZERO_FLOAT)
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds', component_constants.ZERO_INT)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBattleDescriptionConfig(xmlCtx, scriptSection)
        if IS_CLIENT:
            self.battleDescription = self._prepareDescription(self.battleDescription)
        return

    def _getDescription(self, descr):
        localizeDescr = super(ShotPassion, self)._getDescription(descr)
        return self._prepareDescription(localizeDescr)

    def _prepareDescription(self, descr):
        percentSymbol = text(R.strings.common.common.percent())
        gunAimingTime = getNiceNumberFormat(100 * self.increaseFactors[b'gun/aimingTime'] - 100)
        damageIncreasePerShot = getNiceNumberFormat(self.damageIncreasePerShot * 100)
        return i18n.makeString(descr, duration=getNiceNumberFormat(self.duration), gunAimingTime=gunAimingTime + percentSymbol, damageIncreasePerShot=damageIncreasePerShot + percentSymbol)
