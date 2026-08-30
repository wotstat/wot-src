from items.artefacts import BaseMarkerConfigReader, EffectsConfigReader, LevelBasedVisualScriptEquipment, VisualScriptEquipment

class Comp7CoreAoeHealEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'radius', b'heal', b'secondaryHealDebuff', b'tickInterval')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreAoeHealEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.radius = section.readFloat(b'radius')
        self.heal = tuple(map(float, section.readString(b'heal').split()))
        self.secondaryHealDebuff = section.readFloat(b'secondaryHealDebuff')
        self.tickInterval = section.readFloat(b'tickInterval')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreAllySupportEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'crewBuff')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreAllySupportEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.crewBuff = tuple(map(float, section.readString(b'crewBuff').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreAllyHunterEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'heal', b'gunReloadTimeBuff', b'tickInterval')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreAllyHunterEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.heal = tuple(map(float, section.readString(b'heal').split()))
        self.gunReloadTimeBuff = section.readFloat(b'gunReloadTimeBuff')
        self.tickInterval = section.readFloat(b'tickInterval')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreConcentrationEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'aimingTimeBuff', b'shotDispersionFactors', b'clipReloadTimeBoost')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreConcentrationEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.aimingTimeBuff = tuple(map(float, section.readString(b'aimingTimeBuff').split()))
        self.shotDispersionFactors = tuple(map(float, section.readString(b'shotDispersionFactors').split()))
        self.clipReloadTimeBoost = tuple(map(float, section.readString(b'clipReloadTimeBoost').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreBerserkEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'gunReloadTimeBuff', b'damageDistance', b'shotDispersionFactors')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreBerserkEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.gunReloadTimeBuff = tuple(map(float, section.readString(b'gunReloadTimeBuff').split()))
        self.damageDistance = section.readFloat(b'damageDistance')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.shotDispersionFactors = tuple(map(float, section.readString(b'shotDispersionFactors').split()))
        self._exportSlotsToVSE()
        return


class Comp7CoreAoeInspireEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'radius', b'crewBuff')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreAoeInspireEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.crewBuff = tuple(map(float, section.readString(b'crewBuff').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreRedlineEquipment(LevelBasedVisualScriptEquipment, BaseMarkerConfigReader, EffectsConfigReader):
    _CONFIG_SLOTS = LevelBasedVisualScriptEquipment._LEVEL_BASED_SLOTS + BaseMarkerConfigReader._MARKER_SLOTS_ + EffectsConfigReader._EFFECTS_SLOTS_ + (b'delay', b'damage', b'stunDuration', b'areaShow', b'fraction', b'requireAssists')

    def __init__(self):
        super(Comp7CoreRedlineEquipment, self).__init__()
        self.initMarkerInformation()
        self.initEffectsInformation()
        return

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreRedlineEquipment, self)._readConfig(xmlCtx, section)
        self.delay = section.readFloat(b'delay')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.damage = tuple(map(float, section.readString(b'damage').split()))
        self.stunDuration = tuple(map(float, section.readString(b'stunDuration').split()))
        self.areaShow = section.readString(b'areaShow').lower() or None
        self.duration = section.readFloat(b'duration')
        self.readMarkerConfig(xmlCtx, section)
        self.readEffectConfig(xmlCtx, section)
        self.fraction = section.readFloat(b'fraction')
        self.requireAssists = section.readBool(b'requireAssists', False)
        self._exportSlotsToVSE()
        return


class Comp7CoreFastRechargeEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'gunReloadTimeBuff', b'gunTemperatureBuff')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreFastRechargeEquipment, self)._readConfig(xmlCtx, section)
        self.gunReloadTimeBuff = tuple(map(float, section.readString(b'gunReloadTimeBuff').split()))
        self.gunTemperatureBuff = tuple(map(float, section.readString(b'gunTemperatureBuff').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreJuggernautEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'enginePowerFactor', b'dmgAbsorb', b'fwMaxSpeedBonus', b'bkMaxSpeedBonus', b'rammingDamageBonus', b'vehicleRotationSpeedFactor')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreJuggernautEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.enginePowerFactor = section.readFloat(b'enginePowerFactor')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.dmgAbsorb = tuple(map(float, section.readString(b'dmgAbsorb').split()))
        self.fwMaxSpeedBonus = section.readFloat(b'fwMaxSpeedBonus')
        self.bkMaxSpeedBonus = section.readFloat(b'bkMaxSpeedBonus')
        self.rammingDamageBonus = section.readFloat(b'rammingDamageBonus')
        self.vehicleRotationSpeedFactor = section.readFloat(b'vehicleRotationSpeedFactor')
        self._exportSlotsToVSE()
        return


class Comp7CoreSureShotEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'shotDispersionFactors', b'slvl', b'sdlvl')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreSureShotEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.shotDispersionFactors = tuple(map(float, section.readString(b'shotDispersionFactors').split()))
        self.slvl = tuple(map(float, section.readString(b'slvl').split()))
        self.sdlvl = tuple(map(float, section.readString(b'sdlvl').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreSniperEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'dispersionFactor', b'damageDistance', b'damageFactors')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreSniperEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.dispersionFactor = section.readFloat(b'dispersionFactor')
        self.damageDistance = section.readFloat(b'damageDistance')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.damageFactors = tuple(map(float, section.readString(b'damageFactors').split()))
        self._exportSlotsToVSE()
        return


class Comp7CoreRiskyAttackEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'healDuration', b'baseHeal', b'extraHealFactor', b'fwdSpeedBoost', b'bkwSpeedBoost', b'enginePowerBuff')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreRiskyAttackEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.healDuration = section.readFloat(b'healDuration')
        self.baseHeal = section.readFloat(b'baseHeal')
        self.extraHealFactor = tuple(map(float, section.readString(b'extraHealFactor').split()))
        self.fwdSpeedBoost = section.readFloat(b'fwdSpeedBoost')
        self.bkwSpeedBoost = section.readFloat(b'bkwSpeedBoost')
        self.enginePowerBuff = section.readFloat(b'enginePowerBuff')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreReconEquipment(LevelBasedVisualScriptEquipment, BaseMarkerConfigReader):
    _CONFIG_SLOTS = LevelBasedVisualScriptEquipment._LEVEL_BASED_SLOTS + BaseMarkerConfigReader._MARKER_SLOTS_ + (b'duration', b'delay', b'startupDelay')

    def __init__(self):
        super(Comp7CoreReconEquipment, self).__init__()
        self.initMarkerInformation()
        return

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreReconEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.delay = section.readFloat(b'delay')
        self.startupDelay = section.readFloat(b'startupDelay')
        self.readMarkerConfig(xmlCtx, section)
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreAggressiveDetectionEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'visionFactor')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreAggressiveDetectionEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.visionFactor = tuple(map(float, section.readString(b'visionFactor').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7CoreMarchEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS = (b'duration', b'enginePowerBuff', b'fwdSpeedBoost', b'invisibilityFactor')

    def _readConfig(self, xmlCtx, section):
        super(Comp7CoreMarchEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.enginePowerBuff = section.readFloat(b'enginePowerBuff')
        self.fwdSpeedBoost = section.readFloat(b'fwdSpeedBoost')
        self.invisibilityFactor = section.readFloat(b'invisibilityFactor')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return
