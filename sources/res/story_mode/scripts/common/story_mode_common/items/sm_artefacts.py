from __future__ import absolute_import
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

    def _readConfig(self, xmlCtx, scriptSection):
        super(SPGZoneEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.yawHitPrediction = scriptSection.readInt(b'yawHitPrediction', 0)
        self.hitPredictionDuration = scriptSection.readFloat(b'hitPredictionDuration', 0)
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

    def _readConfig(self, xmlCtx, scriptSection):
        super(AOENavmeshEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.readNavmeshConfig(xmlCtx, scriptSection)
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

    def _readConfig(self, xmlCtx, scriptSection):
        super(BaseAbilityEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readArcadeInformation(xmlCtx, scriptSection)
        self.readMarkerConfig(xmlCtx, scriptSection)
        self.readNavmeshConfig(xmlCtx, scriptSection)
        self.prepareTime = scriptSection.readFloat(b'prepareTime')
        self.respawnTime = scriptSection.readFloat(b'respawnTime')
        self.cooldownTime = scriptSection.readFloat(b'cooldownTime')
        self.unspotDelay = scriptSection.readFloat(b'unspotDelay')
        self.directVisionRadius = scriptSection.readFloat(b'directVisionRadius')
        self.visionMinRadius = scriptSection.readFloat(b'visionMinRadius')
        self.detectFromVehicle = scriptSection.readBool(b'detectFromVehicle')
        self.observationPoints = self._readPointList(*_xml.getSubSectionWithContext(xmlCtx, scriptSection, b'observationPoints'))
        return

    @staticmethod
    def _readPointList(xmlCtx, section):
        result = []
        for _, ((_, _), point) in _xml.getItemsWithContext(xmlCtx, section, b'point'):
            result.append(point.asVector3)

        return result


class ReconAbilityEquipment(BaseAbilityEquipment):

    def _readConfig(self, xmlCtx, scriptSection):
        super(ReconAbilityEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.activatingTime = scriptSection.readFloat(b'activatingTime')
        self.deactivatingTime = scriptSection.readFloat(b'deactivatingTime')
        return


class DistractionAbilityEquipment(BaseAbilityEquipment):

    def _readConfig(self, xmlCtx, scriptSection):
        super(DistractionAbilityEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.pointRadius = scriptSection.readFloat(b'pointRadius')
        self.detectTime = _xml.readPositiveFloat(xmlCtx, scriptSection, b'detectTime', 0.5)
        self.autoDestroyTime = scriptSection.readFloat(b'autoDestroyTime')
        self.changeBrainDelay = scriptSection.readFloat(b'changeBrainDelay')
        self.investigateTime = scriptSection.readFloat(b'investigateTime')
        self.showXrayMarker = scriptSection.readBool(b'showXrayMarker')
        self.detectSequence = scriptSection.readString(b'detectSequence')
        return
