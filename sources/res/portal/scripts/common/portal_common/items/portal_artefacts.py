import BigWorld
from constants import IS_CLIENT
import items.artefacts as artefacts
from items import _xml
from items.artefacts import Equipment, VehicleFactorsXmlReader, ArcadeEquipmentConfigReader, _CommonMinefieldEquipment
from items.components import component_constants

class PortalAOEEquipment(artefacts.AreaOfEffectEquipment):
    __slots__ = ()

    def _readConfig(self, xmlCtx, section):
        super(PortalAOEEquipment, self)._readConfig(xmlCtx, section)
        if IS_CLIENT:
            presetIndex = BigWorld.detectGraphicsPresetFromSystemSettings()
            lowPresetIndex = BigWorld.getSystemPerformancePresetIdFromName(b'LOW')
            if presetIndex >= lowPresetIndex:
                self.areaVisibleToEnemies = False
        return

    def readSharedCooldownConsumableConfig(self, xmlCtx, section):
        return


class BasePortalArtefact(Equipment):
    __slots__ = (b'idx',)

    def __init__(self):
        super(BasePortalArtefact, self).__init__()
        self.idx = 0
        return

    def _readConfig(self, xmlCtx, section):
        super(BasePortalArtefact, self)._readConfig(xmlCtx, section)
        self.idx = _xml.readIntOrNone(xmlCtx, section, b'idx')
        return


class PortalVehicleChangeShot(BasePortalArtefact):
    __slots__ = (b'duration', b'shellCD', b'selfVehiclePrefab', b'capturedVehiclePrefab', b'gunFirePrefab')

    def __init__(self):
        super(PortalVehicleChangeShot, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.shellCD = component_constants.ZERO_INT
        self.selfVehiclePrefab = component_constants.EMPTY_STRING
        self.capturedVehiclePrefab = component_constants.EMPTY_STRING
        self.gunFirePrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(PortalVehicleChangeShot, self)._readConfig(xmlCtx, section)
        self.duration = _xml.readInt(xmlCtx, section, b'duration')
        self.shellCD = _xml.readInt(xmlCtx, section, b'shellCompactDescr')
        self.selfVehiclePrefab = _xml.readString(xmlCtx, section, b'selfVehiclePrefab')
        self.capturedVehiclePrefab = _xml.readString(xmlCtx, section, b'capturedVehiclePrefab')
        self.gunFirePrefab = _xml.readString(xmlCtx, section, b'gunFirePrefab')
        return


class PortalGuidedMissile(BasePortalArtefact):
    __slots__ = (b'duration',)

    def __init__(self):
        super(PortalGuidedMissile, self).__init__()
        self.duration = component_constants.ZERO_INT
        return


class PortalSentryGun(BasePortalArtefact, ArcadeEquipmentConfigReader):
    __slots__ = (b'attackRadius', b'sentryGunVehicle', b'deployEffectDuration', b'duration') + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS

    def __init__(self):
        super(PortalSentryGun, self).__init__()
        self.sentryGunVehicle = component_constants.EMPTY_STRING
        self.areaLength = component_constants.ZERO_FLOAT
        self.areaWidth = component_constants.ZERO_FLOAT
        self.areaColor = component_constants.ZERO_INT
        self.deployEffectDuration = component_constants.ZERO_FLOAT
        self.duration = component_constants.ZERO_INT
        self.initArcadeInformation()
        return

    def _readConfig(self, xmlCtx, section):
        super(PortalSentryGun, self)._readConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.duration = _xml.readInt(xmlCtx, section, b'duration')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.areaLength = _xml.readFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readFloat(xmlCtx, section, b'areaWidth')
        self.areaVisual = _xml.readString(xmlCtx, section, b'areaVisual')
        self.sentryGunVehicle = _xml.readString(xmlCtx, section, b'sentryGunVehicle')
        self.deployEffectDuration = _xml.readFloat(xmlCtx, section, b'deployEffectDuration')
        return


class PortalBerserk(BasePortalArtefact):
    __slots__ = (b'increaseFactors', b'duration')

    def __init__(self):
        super(PortalBerserk, self).__init__()
        self.increaseFactors = component_constants.EMPTY_DICT
        self.duration = component_constants.ZERO_INT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(PortalBerserk, self)._readConfig(xmlCtx, scriptSection)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'increaseFactors')
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration')
        return


class PortalMinefield(_CommonMinefieldEquipment):
    __slots__ = (b'cooldownSeconds', b'duration', b'idx')

    def __init__(self):
        super(PortalMinefield, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.idx = component_constants.ZERO_INT
        return

    def _readConfig(self, xmlCtx, section):
        super(PortalMinefield, self)._readConfig(xmlCtx, section)
        self.cooldownSeconds = self.sharedCooldownTime
        self.duration = self.mineParams.lifetime
        self.idx = _xml.readIntOrNone(xmlCtx, section, b'idx')
        return


class PortalVehicleShield(BasePortalArtefact):
    __slots__ = (b'duration',)

    def __init__(self):
        super(PortalVehicleShield, self).__init__()
        self.duration = component_constants.ZERO_INT
        return

    def _readConfig(self, xmlCtx, section):
        super(PortalVehicleShield, self)._readConfig(xmlCtx, section)
        self.duration = _xml.readInt(xmlCtx, section, b'duration')
        return


class VehicleFireShot(BasePortalArtefact):
    __slots__ = (b'duration', b'gunFirePrefab', b'hitPrefab')

    def __init__(self):
        super(VehicleFireShot, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.gunFirePrefab = component_constants.EMPTY_STRING
        self.hitPrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(VehicleFireShot, self)._readConfig(xmlCtx, section)
        self.gunFirePrefab = _xml.readString(xmlCtx, section, b'gunFirePrefab')
        self.hitPrefab = _xml.readString(xmlCtx, section, b'hitPrefab')
        return


class VehicleFrozenShot(BasePortalArtefact):
    __slots__ = (b'params', b'duration', b'gunFirePrefab', b'hitPrefab')

    def __init__(self):
        super(VehicleFrozenShot, self).__init__()
        self.params = {b'debuffFactors': (component_constants.EMPTY_DICT), 
           b'debuffDuration': (component_constants.ZERO_FLOAT), 
           b'equipmentID': (component_constants.ZERO_INT)}
        self.duration = self.cooldownSeconds
        self.gunFirePrefab = component_constants.EMPTY_STRING
        self.hitPrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(VehicleFrozenShot, self)._readConfig(xmlCtx, section)
        self.params[b'debuffDuration'] = section.readFloat(b'debuffDuration')
        if section.has_key(b'debuffFactors'):
            self.params[b'debuffFactors'] = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'debuffFactors')
        self.params[b'equipmentID'] = self.id[1]
        self.gunFirePrefab = _xml.readString(xmlCtx, section, b'gunFirePrefab')
        self.hitPrefab = _xml.readString(xmlCtx, section, b'hitPrefab')
        return


class VehicleLaughShot(BasePortalArtefact):
    __slots__ = (b'params', b'duration', b'gunFirePrefab', b'hitPrefab')

    def __init__(self):
        super(VehicleLaughShot, self).__init__()
        self.params = {b'damagePerSecond': (component_constants.ZERO_FLOAT), 
           b'debuffFactors': (component_constants.EMPTY_DICT), 
           b'debuffDuration': (component_constants.ZERO_FLOAT), 
           b'equipmentID': (component_constants.ZERO_INT)}
        self.duration = self.cooldownSeconds
        self.gunFirePrefab = component_constants.EMPTY_STRING
        self.hitPrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(VehicleLaughShot, self)._readConfig(xmlCtx, section)
        self.params[b'debuffDuration'] = section.readFloat(b'debuffDuration')
        self.params[b'damagePerSecond'] = section.readFloat(b'damagePerSecond')
        if section.has_key(b'debuffFactors'):
            self.params[b'debuffFactors'] = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'debuffFactors')
        self.params[b'equipmentID'] = self.id[1]
        self.gunFirePrefab = _xml.readString(xmlCtx, section, b'gunFirePrefab')
        self.hitPrefab = _xml.readString(xmlCtx, section, b'hitPrefab')
        return


class VehicleCurseShot(BasePortalArtefact):
    __slots__ = (b'params', b'duration', b'gunFirePrefab', b'hitPrefab')

    def __init__(self):
        super(VehicleCurseShot, self).__init__()
        self.params = {b'damagedDevices': (component_constants.EMPTY_DICT), 
           b'equipmentID': (component_constants.ZERO_INT)}
        self.duration = self.cooldownSeconds
        self.gunFirePrefab = component_constants.EMPTY_STRING
        self.hitPrefab = component_constants.EMPTY_STRING
        return

    def _readConfig(self, xmlCtx, section):
        super(VehicleCurseShot, self)._readConfig(xmlCtx, section)
        if section.has_key(b'damagedDevices'):
            subsection = _xml.getSubsection(xmlCtx, section, b'damagedDevices')
            devices = {}
            for device, _ in subsection.items():
                devices[device] = subsection.readFloat(device)

            self.params[b'damagedDevices'] = devices
        self.params[b'equipmentID'] = self.id[1]
        self.gunFirePrefab = _xml.readString(xmlCtx, section, b'gunFirePrefab')
        self.hitPrefab = _xml.readString(xmlCtx, section, b'hitPrefab')
        return


class VehicleInfluenceZone(BasePortalArtefact):
    __slots__ = (b'params', b'duration')

    def __init__(self):
        super(VehicleInfluenceZone, self).__init__()
        self.params = {b'increaseFactors': (component_constants.EMPTY_DICT), 
           b'duration': (component_constants.ZERO_FLOAT), 
           b'radius': (component_constants.ZERO_INT), 
           b'equipmentID': (component_constants.ZERO_INT)}
        return

    def _readConfig(self, xmlCtx, section):
        super(VehicleInfluenceZone, self)._readConfig(xmlCtx, section)
        self.params[b'increaseFactors'] = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'increaseFactors')
        self.duration = self.params[b'duration'] = _xml.readInt(xmlCtx, section, b'duration')
        self.params[b'radius'] = _xml.readInt(xmlCtx, section, b'radius')
        self.params[b'equipmentID'] = self.id[1]
        self.params[b'usagePrefab'] = _xml.readString(xmlCtx, section, b'usagePrefab')
        return


class VehicleTrap(artefacts.VisualScriptEquipment, artefacts.AreaMarkerConfigReader, artefacts.ArcadeEquipmentConfigReader, object):
    __slots__ = (b'duration', b'impulse', b'gravityFactor', b'radius', b'offsetY', b'deploymentDelay', b'damagePerSecond', b'cooldown', b'idx') + artefacts.AreaMarkerConfigReader._MARKER_SLOTS_ + artefacts.ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS

    def __init__(self):
        super(VehicleTrap, self).__init__()
        self.initMarkerInformation()
        self.initArcadeInformation()
        self.duration = 0.0
        self.impulse = 0.0
        self.gravityFactor = 0.0
        self.radius = 0.0
        self.offsetY = 0.0
        self.deploymentDelay = 0.0
        self.damagePerSecond = 0.0
        self.cooldown = 0.0
        self.idx = 0
        return

    @property
    def tooltipParams(self):
        params = super(VehicleTrap, self).tooltipParams
        params[b'duration'] = self.duration
        params[b'impulse'] = self.impulse
        params[b'gravityFactor'] = self.gravityFactor
        params[b'radius'] = self.radius
        params[b'offsetY'] = self.offsetY
        params[b'deploymentDelay'] = self.deploymentDelay
        params[b'damagePerSecond'] = self.damagePerSecond
        params[b'cooldown'] = self.cooldown
        return params

    def _readConfig(self, xmlCtx, section):
        super(VehicleTrap, self)._readConfig(xmlCtx, section)
        self.readMarkerConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.impulse = section.readFloat(b'impulse')
        self.gravityFactor = section.readFloat(b'gravityFactor')
        self.radius = section.readFloat(b'radius')
        self.offsetY = section.readFloat(b'offsetY')
        self.deploymentDelay = section.readFloat(b'deploymentDelay')
        self.damagePerSecond = section.readFloat(b'damagePerSecond')
        self.cooldown = section.readFloat(b'cooldown')
        self.idx = section.readInt(b'idx')
        self._exportSlotsToVSE()
        return
