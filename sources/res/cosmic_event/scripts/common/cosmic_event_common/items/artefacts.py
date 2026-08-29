import importlib
from items.components import component_constants
from items import _xml
from items.artefacts import Equipment
artefacts = importlib.import_module(b'items.artefacts')

class CosmicEventGravityFieldEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'duration', b'radius', b'gravityFactor', b'impulsePerSecond')

    @property
    def tooltipParams(self):
        params = super(CosmicEventGravityFieldEquipment, self).tooltipParams
        params[b'radius'] = self.radius
        params[b'gravityFactor'] = self.gravityFactor
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventGravityFieldEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.radius = section.readFloat(b'radius')
        self.gravityFactor = section.readFloat(b'gravityFactor')
        self.impulsePerSecond = section.readFloat(b'impulsePerSecond')
        self._exportSlotsToVSE()
        return


class CosmicEventWaveEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'radius', b'impulseFactor', b'duration', b'cooldownSeconds')

    @property
    def tooltipParams(self):
        params = super(CosmicEventWaveEquipment, self).tooltipParams
        params[b'radius'] = self.radius
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventWaveEquipment, self)._readConfig(xmlCtx, section)
        self.radius = section.readFloat(b'radius')
        self.impulseFactor = section.readFloat(b'impulseFactor')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.duration = section.readFloat(b'duration')
        self._exportSlotsToVSE()
        return


class CosmicEventRocketBoosterEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'duration', b'cooldownSeconds')

    @property
    def tooltipParams(self):
        params = super(CosmicEventRocketBoosterEquipment, self).tooltipParams
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventRocketBoosterEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class CosmicEventBlackHoleEquipment(artefacts.VisualScriptEquipment, artefacts.AreaMarkerConfigReader, artefacts.ArcadeEquipmentConfigReader, object):
    __slots__ = (b'duration', b'impulse', b'gravityFactor', b'radius', b'deploymentDelay') + artefacts.AreaMarkerConfigReader._MARKER_SLOTS_ + artefacts.ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS

    def __init__(self):
        super(CosmicEventBlackHoleEquipment, self).__init__()
        self.initMarkerInformation()
        self.initArcadeInformation()
        return

    @property
    def tooltipParams(self):
        params = super(CosmicEventBlackHoleEquipment, self).tooltipParams
        params[b'duration'] = self.duration
        params[b'impulse'] = self.impulse
        params[b'gravityFactor'] = self.gravityFactor
        params[b'radius'] = self.radius
        params[b'deploymentDelay'] = self.deploymentDelay
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventBlackHoleEquipment, self)._readConfig(xmlCtx, section)
        self.readMarkerConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.impulse = section.readFloat(b'impulse')
        self.gravityFactor = section.readFloat(b'gravityFactor')
        self.radius = section.readFloat(b'radius')
        self.deploymentDelay = section.readFloat(b'deploymentDelay')
        self._exportSlotsToVSE()
        return


class CosmicEventHookShotEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'duration', b'shellID', b'shotSpeed')

    @property
    def tooltipParams(self):
        params = super(CosmicEventHookShotEquipment, self).tooltipParams
        params[b'duration'] = self.duration
        params[b'shellID'] = self.shellID
        params[b'shotSpeed'] = self.shotSpeed
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventHookShotEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.shellID = section.readInt(b'shellID')
        self.shotSpeed = section.readInt(b'shotSpeed')
        self._exportSlotsToVSE()
        return


class CosmicEventShieldEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'duration', b'gravityFactor', b'cooldownSeconds', b'radius')

    @property
    def tooltipParams(self):
        params = super(CosmicEventShieldEquipment, self).tooltipParams
        params[b'cooldown'] = self.cooldownSeconds
        params[b'duration'] = self.duration
        params[b'cooldownSeconds'] = self.cooldownSeconds
        params[b'radius'] = self.radius
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventShieldEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.gravityFactor = section.readFloat(b'gravityFactor')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.radius = section.readFloat(b'radius')
        self._exportSlotsToVSE()
        return


class CosmicEventPowerShotEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'shellID', b'shotSpeed')

    @property
    def tooltipParams(self):
        params = super(CosmicEventPowerShotEquipment, self).tooltipParams
        params[b'shellID'] = self.shellID
        params[b'shotSpeed'] = self.shotSpeed
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventPowerShotEquipment, self)._readConfig(xmlCtx, section)
        self.shellID = section.readInt(b'shellID')
        self.shotSpeed = section.readInt(b'shotSpeed')
        self._exportSlotsToVSE()
        return


class CosmicEventStunShotEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'cooldownSeconds', b'stunDuration', b'vehicleSpeedMultiplier', b'turretRotationSpeedMultiplier', b'gunReloadTimeMultiplier', b'shellID', b'shotSpeed')

    @property
    def tooltipParams(self):
        params = super(CosmicEventStunShotEquipment, self).tooltipParams
        params[b'cooldownSeconds'] = self.cooldownSeconds
        params[b'stunDuration'] = self.stunDuration
        params[b'vehicleSpeedMultiplier'] = self.vehicleSpeedMultiplier
        params[b'turretRotationSpeedMultiplier'] = self.turretRotationSpeedMultiplier
        params[b'gunReloadTimeMultiplier'] = self.gunReloadTimeMultiplier
        params[b'shellID'] = self.shellID
        params[b'shotSpeed'] = self.shotSpeed
        return params

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventStunShotEquipment, self)._readConfig(xmlCtx, section)
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.stunDuration = section.readFloat(b'stunDuration')
        self.vehicleSpeedMultiplier = section.readFloat(b'vehicleSpeedMultiplier')
        self.turretRotationSpeedMultiplier = section.readFloat(b'turretRotationSpeedMultiplier')
        self.gunReloadTimeMultiplier = section.readFloat(b'gunReloadTimeMultiplier')
        self.shellID = section.readInt(b'shellID')
        self.shotSpeed = section.readInt(b'shotSpeed')
        self._exportSlotsToVSE()
        return


class CosmicEventMineEquipment(Equipment, artefacts.ArcadeEquipmentConfigReader):
    __slots__ = (b'duration', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'restrictedAreaColor')

    def __init__(self):
        super(CosmicEventMineEquipment, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.initArcadeInformation()
        self.areaLength = component_constants.ZERO_INT
        self.areaWidth = component_constants.ZERO_INT
        self.areaVisual = None
        self.areaColor = None
        self.restrictedAreaColor = None
        return

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventMineEquipment, self)._readConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.areaLength = _xml.readPositiveFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, section, b'areaWidth')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.restrictedAreaColor = _xml.readIntOrNone(xmlCtx, section, b'restrictedAreaColor')
        return


class CosmicEventTeleportEquipment(artefacts.Equipment, object):
    __slots__ = (b'lifeTime',)

    def _readConfig(self, xmlCtx, section):
        super(CosmicEventTeleportEquipment, self)._readConfig(xmlCtx, section)
        self.lifeTime = section.readFloat(b'lifeTime')
        return
