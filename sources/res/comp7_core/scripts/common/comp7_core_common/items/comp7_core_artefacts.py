from __future__ import absolute_import
from items.artefacts import BaseMarkerConfigReader, EffectsConfigReader, LevelBasedVisualScriptEquipment, VisualScriptEquipment

class Comp7CoreAoeHealEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'radius', b'heal', b'secondaryHealDebuff', b'tickInterval')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreAoeHealEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.radius = scriptSection.readFloat(b'radius')
        self.heal = tuple(map(float, scriptSection.readString(b'heal').split()))
        self.secondaryHealDebuff = scriptSection.readFloat(b'secondaryHealDebuff')
        self.tickInterval = scriptSection.readFloat(b'tickInterval')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreAllySupportEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'crewBuff')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreAllySupportEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.crewBuff = tuple(map(float, scriptSection.readString(b'crewBuff').split()))
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreAllyHunterEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'heal', b'gunReloadTimeBuff', b'tickInterval')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreAllyHunterEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.heal = tuple(map(float, scriptSection.readString(b'heal').split()))
        self.gunReloadTimeBuff = scriptSection.readFloat(b'gunReloadTimeBuff')
        self.tickInterval = scriptSection.readFloat(b'tickInterval')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreConcentrationEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'aimingTimeBuff', b'shotDispersionFactors', b'clipReloadTimeBoost')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreConcentrationEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.aimingTimeBuff = tuple(map(float, scriptSection.readString(b'aimingTimeBuff').split()))
        self.shotDispersionFactors = tuple(map(float, scriptSection.readString(b'shotDispersionFactors').split()))
        self.clipReloadTimeBoost = tuple(map(float, scriptSection.readString(b'clipReloadTimeBoost').split()))
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreBerserkEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'gunReloadTimeBuff', b'damageDistance', b'shotDispersionFactors')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreBerserkEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.gunReloadTimeBuff = tuple(map(float, scriptSection.readString(b'gunReloadTimeBuff').split()))
        self.damageDistance = scriptSection.readFloat(b'damageDistance')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self.shotDispersionFactors = tuple(map(float, scriptSection.readString(b'shotDispersionFactors').split()))
        self._exportSlotsToVSE()
        return


class Comp7CoreAoeInspireEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'radius', b'crewBuff')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreAoeInspireEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.crewBuff = tuple(map(float, scriptSection.readString(b'crewBuff').split()))
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreRedlineEquipment(LevelBasedVisualScriptEquipment, BaseMarkerConfigReader, EffectsConfigReader):
    _CONFIG_SLOTS = LevelBasedVisualScriptEquipment._LEVEL_BASED_SLOTS + BaseMarkerConfigReader._MARKER_SLOTS_ + EffectsConfigReader._EFFECTS_SLOTS_ + (b'delay', b'damage', b'stunDuration', b'areaShow', b'fraction', b'requireAssists')

    def __init__(self):
        super(Comp7CoreRedlineEquipment, self).__init__()
        self.initMarkerInformation()
        self.initEffectsInformation()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreRedlineEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.delay = scriptSection.readFloat(b'delay')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self.damage = tuple(map(float, scriptSection.readString(b'damage').split()))
        self.stunDuration = tuple(map(float, scriptSection.readString(b'stunDuration').split()))
        self.areaShow = scriptSection.readString(b'areaShow').lower() or None
        self.duration = scriptSection.readFloat(b'duration')
        self.readMarkerConfig(xmlCtx, scriptSection)
        self.readEffectConfig(xmlCtx, scriptSection)
        self.fraction = scriptSection.readFloat(b'fraction')
        self.requireAssists = scriptSection.readBool(b'requireAssists', False)
        self._exportSlotsToVSE()
        return


class Comp7CoreFastRechargeEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'gunReloadTimeBuff', b'gunTemperatureBuff')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreFastRechargeEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.gunReloadTimeBuff = tuple(map(float, scriptSection.readString(b'gunReloadTimeBuff').split()))
        self.gunTemperatureBuff = tuple(map(float, scriptSection.readString(b'gunTemperatureBuff').split()))
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreJuggernautEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'enginePowerFactor', b'dmgAbsorb', b'fwMaxSpeedBonus', b'bkMaxSpeedBonus', b'rammingDamageBonus', b'vehicleRotationSpeedFactor')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreJuggernautEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = tuple(map(float, scriptSection.readString(b'duration').split()))
        self.enginePowerFactor = scriptSection.readFloat(b'enginePowerFactor')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self.dmgAbsorb = tuple(map(float, scriptSection.readString(b'dmgAbsorb').split()))
        self.fwMaxSpeedBonus = scriptSection.readFloat(b'fwMaxSpeedBonus')
        self.bkMaxSpeedBonus = scriptSection.readFloat(b'bkMaxSpeedBonus')
        self.rammingDamageBonus = scriptSection.readFloat(b'rammingDamageBonus')
        self.vehicleRotationSpeedFactor = scriptSection.readFloat(b'vehicleRotationSpeedFactor')
        self._exportSlotsToVSE()
        return


class Comp7CoreSureShotEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'shotDispersionFactors', b'slvl', b'sdlvl')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreSureShotEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.shotDispersionFactors = tuple(map(float, scriptSection.readString(b'shotDispersionFactors').split()))
        self.slvl = tuple(map(float, scriptSection.readString(b'slvl').split()))
        self.sdlvl = tuple(map(float, scriptSection.readString(b'sdlvl').split()))
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreSniperEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'dispersionFactor', b'damageDistance', b'damageFactors')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreSniperEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = tuple(map(float, scriptSection.readString(b'duration').split()))
        self.dispersionFactor = scriptSection.readFloat(b'dispersionFactor')
        self.damageDistance = scriptSection.readFloat(b'damageDistance')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self.damageFactors = tuple(map(float, scriptSection.readString(b'damageFactors').split()))
        self._exportSlotsToVSE()
        return


class Comp7CoreRiskyAttackEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'healDuration', b'baseHeal', b'extraHealFactor', b'fwdSpeedBoost', b'bkwSpeedBoost', b'enginePowerBuff')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreRiskyAttackEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.healDuration = scriptSection.readFloat(b'healDuration')
        self.baseHeal = scriptSection.readFloat(b'baseHeal')
        self.extraHealFactor = tuple(map(float, scriptSection.readString(b'extraHealFactor').split()))
        self.fwdSpeedBoost = scriptSection.readFloat(b'fwdSpeedBoost')
        self.bkwSpeedBoost = scriptSection.readFloat(b'bkwSpeedBoost')
        self.enginePowerBuff = scriptSection.readFloat(b'enginePowerBuff')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreReconEquipment(LevelBasedVisualScriptEquipment, BaseMarkerConfigReader):
    _CONFIG_SLOTS = LevelBasedVisualScriptEquipment._LEVEL_BASED_SLOTS + BaseMarkerConfigReader._MARKER_SLOTS_ + (b'duration', b'delay', b'startupDelay')

    def __init__(self):
        super(Comp7CoreReconEquipment, self).__init__()
        self.initMarkerInformation()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreReconEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = tuple(map(float, scriptSection.readString(b'duration').split()))
        self.delay = scriptSection.readFloat(b'delay')
        self.startupDelay = scriptSection.readFloat(b'startupDelay')
        self.readMarkerConfig(xmlCtx, scriptSection)
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreAggressiveDetectionEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'visionFactor')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreAggressiveDetectionEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self.visionFactor = tuple(map(float, scriptSection.readString(b'visionFactor').split()))
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreMarchEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'enginePowerBuff', b'fwdSpeedBoost', b'invisibilityFactor')

    def _readConfig(self, xmlCtx, scriptSection):
        super(Comp7CoreMarchEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = tuple(map(float, scriptSection.readString(b'duration').split()))
        self.enginePowerBuff = scriptSection.readFloat(b'enginePowerBuff')
        self.fwdSpeedBoost = scriptSection.readFloat(b'fwdSpeedBoost')
        self.invisibilityFactor = scriptSection.readFloat(b'invisibilityFactor')
        self.cooldownSeconds = scriptSection.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return
