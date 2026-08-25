import typing
from items.artefacts import Equipment, AreaOfEffectEquipment, TooltipConfigReader, ArcadeEquipmentConfigReader, AreaMarkerConfigReader
from items.components import component_constants
from items import _xml
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
    from Math import Vector3

class SPGZoneEquipment(AreaOfEffectEquipment):
    __slots__ = (b'yawHitPrediction', b'hitPredictionDuration')

    def _readConfig(self, xmlCtx, section):
        super(SPGZoneEquipment, self)._readConfig(xmlCtx, section)
        self.yawHitPrediction = section.readInt(b'yawHitPrediction', 0)
        self.hitPredictionDuration = section.readFloat(b'hitPredictionDuration', 0)
        return


class NavmeshSettingsReader(object):
    _SLOTS = (b'navmeshGirth', b'navmeshHeightTolerance')

    def initNavmeshConfig(self):
        self.navmeshGirth = component_constants.EMPTY_STRING
        self.navmeshHeightTolerance = component_constants.ZERO_FLOAT
        return

    def readNavmeshConfig(self, xmlCtx, section):
        self.navmeshGirth = section.readString(b'navmeshGirth')
        if not self.navmeshGirth:
            raise SoftException((b'[Equipment=<{}>] Param=<navmeshGirth> is required.').format(self.id))
        self.navmeshHeightTolerance = _xml.readNonNegativeFloat(xmlCtx, section, b'navmeshHeightTolerance', 1.0)
        return


class AOENavmeshEquipment(AreaOfEffectEquipment, NavmeshSettingsReader):
    __slots__ = NavmeshSettingsReader._SLOTS

    def __init__(self):
        super(AOENavmeshEquipment, self).__init__()
        self.initNavmeshConfig()
        return

    def _readConfig(self, xmlCtx, section):
        super(AOENavmeshEquipment, self)._readConfig(xmlCtx, section)
        self.readNavmeshConfig(xmlCtx, section)
        return


class BaseAbilityEquipment(Equipment, TooltipConfigReader, ArcadeEquipmentConfigReader, AreaMarkerConfigReader, NavmeshSettingsReader):
    __slots__ = (b'heightAboveBase', b'prepareTime', b'respawnTime', b'cooldownTime', b'unspotDelay', b'directVisionRadius', b'visionMinRadius', b'detectFromVehicle', b'observationPoints') + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + AreaMarkerConfigReader._MARKER_SLOTS_ + NavmeshSettingsReader._SLOTS

    def __init__(self):
        super(BaseAbilityEquipment, self).__init__()
        self.initTooltipInformation()
        self.initArcadeInformation()
        self.initMarkerInformation()
        self.initNavmeshConfig()
        return

    def _readConfig(self, xmlCtx, section):
        super(BaseAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.readTooltipInformation(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.readMarkerConfig(xmlCtx, section)
        self.readNavmeshConfig(xmlCtx, section)
        self.prepareTime = section.readFloat(b'prepareTime')
        self.respawnTime = section.readFloat(b'respawnTime')
        self.cooldownTime = section.readFloat(b'cooldownTime')
        self.unspotDelay = section.readFloat(b'unspotDelay')
        self.directVisionRadius = section.readFloat(b'directVisionRadius')
        self.visionMinRadius = section.readFloat(b'visionMinRadius')
        self.detectFromVehicle = section.readBool(b'detectFromVehicle')
        self.observationPoints = self._readPointList(*_xml.getSubSectionWithContext(xmlCtx, section, b'observationPoints'))
        return

    @staticmethod
    def _readPointList(xmlCtx, section):
        result = []
        for _, ((_, _), point) in _xml.getItemsWithContext(xmlCtx, section, b'point'):
            result.append(point.asVector3)

        return result


class ReconAbilityEquipment(BaseAbilityEquipment):

    def _readConfig(self, xmlCtx, section):
        super(ReconAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.activatingTime = section.readFloat(b'activatingTime')
        self.deactivatingTime = section.readFloat(b'deactivatingTime')
        return


class DistractionAbilityEquipment(BaseAbilityEquipment):

    def _readConfig(self, xmlCtx, section):
        super(DistractionAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.pointRadius = section.readFloat(b'pointRadius')
        self.detectTime = _xml.readPositiveFloat(xmlCtx, section, b'detectTime', 0.5)
        self.autoDestroyTime = section.readFloat(b'autoDestroyTime')
        self.changeBrainDelay = section.readFloat(b'changeBrainDelay')
        self.investigateTime = section.readFloat(b'investigateTime')
        self.showXrayMarker = section.readBool(b'showXrayMarker')
        self.detectSequence = section.readString(b'detectSequence')
        return
