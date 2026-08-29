import os
from re import findall
from enum import Enum, unique
from typing import TYPE_CHECKING, NamedTuple
import items, nations
from ArenaType import readVisualScriptSection
from constants import IS_CLIENT, IS_CELLAPP, IS_WEB, VEHICLE_TTC_ASPECTS, ATTACK_REASON, ATTACK_REASON_INDICES, SERVER_TICK_LENGTH, SkillProcessorArgs, GroupSkillProcessorArgs, TTC_TOOLTIP_SECTIONS
from debug_utils import LOG_DEBUG_DEV
from items import ITEM_OPERATION, PREDEFINED_HEAL_GROUPS
from items import _xml, vehicles
from items.artefacts_helpers import VehicleFilter, _ArtefactFilter, readKpi, VehicleAttribute
from items.basic_item import BasicItem
from items.components import shared_components, component_constants
from items.components.supply_slot_categories import SupplySlotFilter, LevelsFactor, AttrsOperation, SlotCategories
from items.economic_directives import Operation
from items.vehicles import VehicleDescriptor
from soft_exception import SoftException
from tankmen import MAX_SKILL_LEVEL
from vehicles import _readPriceForOperation
from Math import Vector3
if TYPE_CHECKING:
    from ResMgr import DataSection
    from typing import Set, Dict, Optional, Any, Tuple
if IS_CLIENT:
    from helpers import i18n
    from gui.impl.backport import text
    from gui.impl.backport.backport_system_locale import getNiceNumberFormat
    from gui.impl.gen import R
elif IS_WEB:
    from web_stubs import i18n
else:

    class i18n(object):

        @classmethod
        def makeString(cls, key):
            raise SoftException(b'Unexpected call "i18n.makeString"')
            return


if IS_CELLAPP:
    from actions import vehicle as vehicleActions

@unique
class ExportParamsTag(Enum):
    VSE = b'vse'
    TOOLTIP = b'tooltip'


ArtefactID = NamedTuple(b'ArtefactID', [(b'nationIdx', int), (b'itemID', int)])

class CommonXmlSectionReader(object):

    def __init__(self, xmlTagKeyMap, dictInstance):
        self.__xmlTagKeyMap = xmlTagKeyMap
        self.__readersMap = self.__createReaders(dictInstance)
        return

    def read(self, xmlCtx, section, subsection_name):
        result = {}
        subsection = _xml.getSubsection(xmlCtx, section, subsection_name)
        for key, tag_name in self.__xmlTagKeyMap.iteritems():
            if _xml.getSubsection(xmlCtx, subsection, tag_name, throwIfMissing=False) is None:
                continue
            reader = self.__readersMap.get(key, None)
            if reader is None:
                raise SoftException((b"Cannot read '{}' xml tag for key '{}'. Reader for this tag wasn't found. Please make sure CommonXmlSectionReader was configured properly").format(tag_name, key))
            result[key] = reader(xmlCtx, subsection, tag_name)

        return result

    @staticmethod
    def __createReaders(dictInstance):
        readers = {}
        for name, value in dictInstance.iteritems():
            factor_type = type(value)
            reader_type = b'TupleOfFloats' if factor_type is list else findall(b"'(\\w+)'", str(factor_type))[0].capitalize()
            readers[name] = getattr(_xml, b'read' + reader_type)

        return readers


class VehicleFactorsXmlReader(CommonXmlSectionReader):
    __readerImpl = None

    def __init__(self):
        attrFactor = vehicles.vehicleAttributeFactors()
        _vehicle_attribute_factor_tags = {name: name.replace(b'/', b'-') for name in attrFactor.iterkeys()}
        super(VehicleFactorsXmlReader, self).__init__(_vehicle_attribute_factor_tags, attrFactor)
        return

    @staticmethod
    def readFactors(xmlCtx, section, subsection_name):
        if VehicleFactorsXmlReader.__readerImpl is None:
            VehicleFactorsXmlReader.__readerImpl = VehicleFactorsXmlReader()
        return VehicleFactorsXmlReader.__readerImpl.read(xmlCtx, section, subsection_name)


class Artefact(BasicItem):
    __slots__ = (b'name', b'id', b'compactDescr', b'tags', b'i18n', b'icon', b'removable', b'price', b'showInShop', b'_vehWeightFraction', b'_weight', b'_exportParams', b'__archetype', b'__vehicleFilter', b'__artefactFilter', b'__tooltipSection', b'isImproved', b'kpi', b'iconName', b'_groupName', b'__weakref__')

    def __init__(self, typeID, itemID, itemName, compactDescr):
        super(Artefact, self).__init__(typeID, itemID, itemName, compactDescr)
        self.icon = None
        self.iconName = None
        self.removable = False
        self.price = None
        self.showInShop = False
        self._vehWeightFraction = component_constants.ZERO_FLOAT
        self._weight = component_constants.ZERO_FLOAT
        self._exportParams = {}
        self.__vehicleFilter = None
        self.__artefactFilter = None
        self.isImproved = None
        self.kpi = None
        self._groupName = None
        self.__tooltipSection = None
        self.__archetype = None
        return

    def init(self, xmlCtx, section):
        self._readBasicConfig(xmlCtx, section)
        xmlCtx = (
         xmlCtx, b'script')
        section = section[b'script']
        self._readWeight(xmlCtx, section)
        self._readConfig(xmlCtx, section)
        return

    @property
    def isAvatarEquipment(self):
        return b'avatar' in self.tags

    @property
    def tooltipParams(self):
        return self._getExportParamsDict(ExportParamsTag.TOOLTIP)

    def updatePrice(self, newPrice, showInShop):
        self.price = newPrice
        self.showInShop = showInShop
        return

    def extraName(self):
        return

    def removeItem(self, *args, **kwargs):
        return

    @property
    def groupName(self):
        return self._groupName or self.name

    @property
    def tooltipSection(self):
        return self.__tooltipSection

    @property
    def archetype(self):
        return self.__archetype

    def _readWeight(self, xmlCtx, section):
        if section.has_key(b'vehicleWeightFraction'):
            self._vehWeightFraction = _xml.readNonNegativeFloat(xmlCtx, section, b'vehicleWeightFraction')
        else:
            self._vehWeightFraction = 0.0
        if section.has_key(b'weight'):
            self._weight = _xml.readNonNegativeFloat(xmlCtx, section, b'weight')
        else:
            self._weight = 0.0
        return

    def checkCompatibilityWithVehicle(self, vehicleDescr):
        if self.__vehicleFilter is None:
            return (True, None)
        else:
            return self.__vehicleFilter.checkCompatibility(vehicleDescr)

    def checkCompatibilityWithOther(self, other):
        if self is other:
            return False
        else:
            filter = self.__artefactFilter
            if filter is None:
                return True
            return not filter.inInstalled(other.tags)

    def checkCompatibilityWithActiveOther(self, other):
        if self is other:
            return False
        else:
            filter = self.__artefactFilter
            if filter is None:
                return True
            return not filter.inActive(other.tags)

    def compatibleNations(self):
        if self.__vehicleFilter:
            return self.__vehicleFilter.compatibleNations()
        return {nations.INDICES[n] for n in nations.AVAILABLE_NAMES}

    def checkCompatibilityWithComponents(self, vehicleDescr):
        if self.__vehicleFilter is None:
            return True
        else:
            return self.__vehicleFilter.checkCompatibilityWithComponents(vehicleDescr)

    def _readConfig(self, xmlCtx, scriptSection):
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        return

    def getVehicleFilter(self):
        return self.__vehicleFilter

    def _readBasicConfig(self, xmlCtx, section):
        self.name = section.name
        self.id = ArtefactID(nations.NONE_INDEX, _xml.readInt(xmlCtx, section, b'id', 0, 65535))
        self.compactDescr = vehicles.makeIntCompactDescrByID(self.itemTypeName, *self.id)
        if not section.has_key(b'tags'):
            self.tags = frozenset()
        else:
            self.tags = _readTags(xmlCtx, section, b'tags', self.itemTypeName)
        if IS_CLIENT or IS_WEB:
            self.i18n = shared_components.I18nComponent(userStringKey=section.readString(b'userString'), descriptionKey=section.readString(b'description'), shortDescriptionSpecialKey=section.readString(b'shortDescriptionSpecial'), longDescriptionSpecialKey=section.readString(b'longDescriptionSpecial'), shortFilterAlertKey=section.readString(b'shortFilterAlert'), longFilterAlertKey=section.readString(b'longFilterAlert'))
            self.icon = _xml.readIconWithDefaultParams(xmlCtx, section, b'icon')
            self.iconName = intern(os.path.splitext(os.path.basename(self.icon[0]))[0])
        if (IS_CLIENT or IS_WEB) and section.has_key(b'kpi'):
            self.kpi = readKpi(xmlCtx, section[b'kpi'])
        else:
            self.kpi = []
        if IS_CLIENT:
            if section.has_key(b'tooltipSection'):
                self.__tooltipSection = section.readString(b'tooltipSection', TTC_TOOLTIP_SECTIONS.EQUIPMENT).split()
            else:
                self.__tooltipSection = [
                 TTC_TOOLTIP_SECTIONS.EQUIPMENT]
            if section.has_key(b'archetype'):
                self.__archetype = intern(section.readString(b'archetype'))
        if section.has_key(b'vehicleFilter'):
            self.__vehicleFilter = VehicleFilter.readVehicleFilter((xmlCtx, b'vehicleFilter'), section[b'vehicleFilter'])
        else:
            self.__vehicleFilter = None
        if not section.has_key(b'incompatibleTags'):
            self.__artefactFilter = None
        else:
            self.__artefactFilter = _ArtefactFilter((xmlCtx, b'incompatibleTags'), section[b'incompatibleTags'], self.itemTypeName)
        self.removable = section.readBool(b'removable', False)
        self.isImproved = section.readBool(b'improved', False)
        if (IS_CLIENT or IS_WEB) and section.has_key(b'groupName'):
            self._groupName = intern(section.readString(b'groupName'))
        self._exportParams = self._readExportParams(section[b'script'])
        return

    def _getExportParamsDict(self, exportTag):
        return {k: getattr(self, k) for k in self._exportParams.get(exportTag.value, set())}

    @staticmethod
    def _readExportParams(section):
        params = {}
        for param, subsection in section.items():
            exports = subsection.readString(b'exports').split()
            for exportTag in exports:
                params.setdefault(exportTag, set()).add(param)

        return params


class OptionalDevice(Artefact):
    __slots__ = (b'categories', b'_overridableFactors', b'_tier', b'_tierlessName', b'_isModernized', b'_isUpgradable', b'_isUpgraded')

    def __init__(self):
        super(OptionalDevice, self).__init__(items.ITEM_TYPES.optionalDevice, 0, b'', 0)
        self.categories = set()
        self._overridableFactors = {}
        self._tier = None
        self._tierlessName = None
        self._isModernized = None
        self._isUpgradable = isinstance(self, UpgradableItem)
        self._isUpgraded = isinstance(self, UpgradedItem)
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(OptionalDevice, self)._readBasicConfig(xmlCtx, section)
        self._readCategories(xmlCtx, section)
        self._readTier(xmlCtx, section)
        self._readSpecFactorsFromConfig(xmlCtx, section[b'script'])
        self._isModernized = any(l.startswith(b'modernized') for l in self.tags)
        return

    def extraName(self):
        return

    @property
    def tier(self):
        return self._tier

    @property
    def tierlessName(self):
        return self._tierlessName or self.name

    @property
    def groupName(self):
        return self._groupName or self.tierlessName

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        return

    def updateVehicleDescrAttrs(self, vehicleDescr):
        return

    @property
    def canUseDemountKit(self):
        return not self.isDeluxe and not (b'modernized_2' in self.tags or b'modernized_3' in self.tags)

    @property
    def isDeluxe(self):
        return b'deluxe' in self.tags

    @property
    def isTrophy(self):
        return b'trophyBasic' in self.tags or b'trophyUpgraded' in self.tags

    @property
    def isModernized(self):
        return self._isModernized

    @property
    def isRestorable(self):
        return self.isDeluxe or self.isTrophy or self.isModernized

    @property
    def isUpgradable(self):
        return self._isUpgradable

    @property
    def isUpgraded(self):
        return self._isUpgraded

    def defineActiveLevel(self, vehicleDescr):
        supplySlot = vehicleDescr.getOptDevSupplySlot(self.compactDescr)
        if supplySlot is None:
            return
        else:
            return SupplySlotFilter.defineActiveValuesLevel(supplySlot.categories, self.categories)

    def defineActiveValueForSpecFactor(self, vehicleDescr, factorName, level=None):
        if level is None:
            level = self.defineActiveLevel(vehicleDescr)
        if level is None:
            return
        else:
            factor = self._defineFactorFor(vehicleDescr, factorName)
            if factor is None:
                return
            return factor.getActiveValue(level)

    def _defineFactorFor(self, vehicleDescr, factorName):
        vehOverridedFactor = vehicleDescr.type.optDevsOverrides.get(self.tierlessName, {}).get(factorName, None)
        if vehOverridedFactor is not None:
            factor = vehOverridedFactor
        else:
            factor = self._overridableFactors.get(factorName, None)
        return factor

    def _readSpecFactorsFromConfig(self, xmlCtx, section):
        factorsSection = section[b'overridableFactors']
        if factorsSection is None:
            return
        else:
            for name, subsection in factorsSection.items():
                factor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, factorsSection, name)
                self._overridableFactors[name] = factor

            return

    def _readCategories(self, xmlCtx, section):
        if section.has_key(b'categories'):
            self.categories = set(_xml.readTupleOfStrings(xmlCtx, section, b'categories'))
            for category in self.categories:
                if category not in SlotCategories.ALL:
                    raise SoftException((b"Unknown category '{}'").format(category))

        return

    def _readTier(self, xmlCtx, section):
        tierParts = self.name.split(b'_tier')
        if len(tierParts) == 2:
            self._tierlessName, tier = tierParts
            self._tier = int(tier)
        return


class StaticOptionalDevice(OptionalDevice):
    __slots__ = (b'_factors',)

    def __init__(self):
        super(StaticOptionalDevice, self).__init__()
        self._factors = {}
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(StaticOptionalDevice, self)._readConfig(xmlCtx, scriptSection)
        self._readFactorsFromConfig(xmlCtx, scriptSection)
        return

    def _readFactorsFromConfig(self, xmlCtx, section):
        factorsSection = section[b'factors']
        if factorsSection is None:
            return
        else:
            for name, subsection in factorsSection.items():
                attrPath, factor = LevelsFactor.readLevelsFactor(xmlCtx, subsection)
                splitted = tuple(attrPath.split(b'/'))
                self._factors[splitted] = factor

            return

    @staticmethod
    def defineAttrsDict(vehicleDescr, modulePath):
        attrDict = getattr(vehicleDescr, modulePath[0])
        for key in modulePath[1:]:
            attrDict = attrDict[key]

        return attrDict

    def updateVehicleDescrAttrs(self, vehicleDescr):
        level = self.defineActiveLevel(vehicleDescr)
        if level is None:
            LOG_DEBUG_DEV((b'updateVehicleDescrAttrs: optional device ({}) is not installed').format(self))
            return
        else:
            for splitted, factor in self._factors.iteritems():
                modulePath = splitted[:-1]
                shortName = splitted[-1]
                attrDict = self.defineAttrsDict(vehicleDescr, modulePath)
                factor.applyLevelToAttrsDict(level, attrDict, shortName)

            return


class StillVehicleOptionalDevice(StaticOptionalDevice):
    __slots__ = (b'activateWhenStillSec',)

    def _readConfig(self, xmlCtx, scriptSection):
        self.activateWhenStillSec = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'activateWhenStillSec')
        super(StillVehicleOptionalDevice, self)._readConfig(xmlCtx, scriptSection)
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        if not self._checkAspect(aspect):
            return
        else:
            level = self.defineActiveLevel(vehicleDescr)
            if level is not None:
                transformedFactors = self.transformFactors(level, vehicleDescr)
                self.updateFactorsDictWithTransformed(factors, transformedFactors)
            return

    def _checkAspect(self, aspect):
        raise NotImplementedError
        return

    def transformFactors(self, level, vehicleDescr):
        raise NotImplementedError
        return

    def updateFactorsDictWithTransformed(self, factorsDict, transformedFactors):
        raise NotImplementedError
        return


class Stereoscope(StillVehicleOptionalDevice):
    __slots__ = (b'circularVisionRadiusFactor',)
    CIRCULAR_VISION_RADIUS = b'circularVisionRadius'

    def extraName(self):
        return b'stereoscope'

    def _checkAspect(self, aspect):
        return aspect in (VEHICLE_TTC_ASPECTS.DEFAULT, VEHICLE_TTC_ASPECTS.WHEN_STILL)

    def _readConfig(self, xmlCtx, scriptSection):
        super(Stereoscope, self)._readConfig(xmlCtx, scriptSection)
        self.circularVisionRadiusFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, self.CIRCULAR_VISION_RADIUS)
        return

    def transformFactors(self, level, vehicleDescr):
        activeValue = self.circularVisionRadiusFactor.getActiveValue(level)
        factorToCompensate = vehicleDescr.miscAttrs[b'circularVisionRadiusFactor']
        transformedFactor = activeValue / factorToCompensate
        res = (transformedFactor,)
        return res

    def updateFactorsDictWithTransformed(self, factorsDict, transformedFactors):
        transformedCVRFactor, = transformedFactors
        AttrsOperation.updateDictWithAttribute(factorsDict, self.CIRCULAR_VISION_RADIUS, AttrsOperation.MUL, transformedCVRFactor)
        return


class CamouflageNet(StillVehicleOptionalDevice):
    invisibilityBonusName = b'invisibilityBonus'
    invisibilityAttr = b'invisibility'

    def extraName(self):
        return b'camouflageNet'

    @property
    def competesBy(self):
        return b'invisibilityAdditiveTerm'

    def transformFactors(self, level, vehicleDescr):
        cnActiveValue = self.defineActiveValueForSpecFactor(vehicleDescr, self.invisibilityBonusName, level)
        staticActiveValue = vehicleDescr.miscAttrs[self.competesBy]
        activeValue = max(cnActiveValue, staticActiveValue) - staticActiveValue
        res = (activeValue,)
        return res

    def updateFactorsDictWithTransformed(self, factorsDict, transformedFactors):
        activeValue, = transformedFactors
        factorsDict[self.invisibilityAttr][0] += activeValue
        return

    def _checkAspect(self, aspect):
        return aspect in (VEHICLE_TTC_ASPECTS.WHEN_STILL,)


class LowNoiseTracks(StaticOptionalDevice):
    invisibilityBonusName = b'invisibilityBonus'

    def updateVehicleDescrAttrs(self, vehicleDescr):
        super(LowNoiseTracks, self).updateVehicleDescrAttrs(vehicleDescr)
        level = self.defineActiveLevel(vehicleDescr)
        activeValue = self.defineActiveValueForSpecFactor(vehicleDescr, self.invisibilityBonusName, level)
        vehicleDescr.miscAttrs[b'invisibilityAdditiveTerm'] += activeValue
        return


class ImprovedConfiguration(StaticOptionalDevice):
    __slots__ = (b'engineReduceFineFactor', b'ammoBayReduceFineFactor')

    def extraName(self):
        return b'improvedConfiguration'

    def _readConfig(self, xmlCtx, scriptSection):
        super(ImprovedConfiguration, self)._readConfig(xmlCtx, scriptSection)
        self.engineReduceFineFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'engineReduceFineFactor')
        self.ammoBayReduceFineFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'ammoBayReduceFineFactor')
        return


class Equipment(Artefact):
    __slots__ = (b'equipmentType', b'reuseCount', b'cooldownSeconds', b'soundNotification', b'stunResistanceEffect', b'stunResistanceDuration', b'repeatedStunDurationFactor', b'clientSelector', b'ownerPrefab', b'usagePrefab', b'playerMessagesKey', b'code', b'activationSound', b'deactivationSound', b'refillSound')

    def __init__(self):
        super(Equipment, self).__init__(items.ITEM_TYPES.equipment, 0, b'', 0)
        self.equipmentType = None
        self.stunResistanceEffect = component_constants.ZERO_FLOAT
        self.stunResistanceDuration = component_constants.ZERO_FLOAT
        self.repeatedStunDurationFactor = 1.0
        self.reuseCount = component_constants.ZERO_INT
        self.cooldownSeconds = component_constants.ZERO_INT
        self.soundNotification = None
        self.clientSelector = None
        self.playerMessagesKey = None
        self.clientSelector = None
        self.code = None
        self.activationSound = None
        self.deactivationSound = None
        self.refillSound = None
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(Equipment, self)._readBasicConfig(xmlCtx, section)
        self.equipmentType = items.EQUIPMENT_TYPES[section.readString(b'type', b'regular')]
        self.soundNotification = _xml.readStringOrNone(xmlCtx, section, b'soundNotification')
        self.activationSound = _xml.readStringOrNone(xmlCtx, section, b'activationSound')
        self.deactivationSound = _xml.readStringOrNone(xmlCtx, section, b'deactivationSound')
        self.refillSound = _xml.readStringOrNone(xmlCtx, section, b'refillSound')
        self.playerMessagesKey = _xml.readStringOrNone(xmlCtx, section, b'playerMessagesKey')
        scriptSection = section[b'script']
        self.stunResistanceEffect, self.stunResistanceDuration, self.repeatedStunDurationFactor = _readStun(xmlCtx, scriptSection)
        self.reuseCount, self.cooldownSeconds = _readReuseParams(xmlCtx, scriptSection)
        self.clientSelector = _xml.readStringOrNone(xmlCtx, scriptSection, b'clientSelector')
        self.ownerPrefab = _xml.readStringOrNone(xmlCtx, section, b'ownerPrefab')
        self.usagePrefab = _xml.readStringOrNone(xmlCtx, section, b'usagePrefab')
        self.code = section.readString(b'code') if section.has_key(b'code') else None
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        return

    def extraName(self):
        return self.name

    def checkCompatibilityWithEquipment(self, other):
        return self.checkCompatibilityWithOther(other)

    def checkCompatibilityWithActiveEquipment(self, other):
        return self.checkCompatibilityWithActiveOther(other)

    def offload(self, inventoryCallback):
        if not callable(inventoryCallback):
            return
        if b'builtin' not in self.tags:
            inventoryCallback(self.compactDescr)
        return

    def isActivatable(self):
        return False

    def doesDependOnOptionalDevice(self):
        return False

    def hasTag(self, tag):
        return tag in self.tags


class ExtraHealthReserve(StaticOptionalDevice):

    def updateVehicleDescrAttrs(self, vehicleDescr):
        super(ExtraHealthReserve, self).updateVehicleDescrAttrs(vehicleDescr)
        if not vehicleDescr.isWheeledVehicle:
            vehicleDescr.miscAttrs[b'chassisHealthAfterHysteresisFactor'] = 1.0
        return


class Grousers(StaticOptionalDevice):
    __slots__ = (b'rotationFactor', b'rollingFrictionFactor')

    def updateVehicleDescrAttrs(self, vehicleDescr):
        super(Grousers, self).updateVehicleDescrAttrs(vehicleDescr)
        level = self.defineActiveLevel(vehicleDescr)
        if level is None:
            LOG_DEBUG_DEV((b'updateVehicleDescrAttrs: optional device ({}) is not installed').format(self))
            return
        else:
            rotationFactorActiveValue = self.rotationFactor.getActiveValue(level)
            rollingFrictionFactorActiveValue = self.rollingFrictionFactor.getActiveValue(level)
            r = vehicleDescr.physics[b'terrainResistance']
            vehicleDescr.physics[b'terrainResistance'] = tuple(ri * rotationFactorActiveValue for ri in r)
            vehicleDescr.physics[b'groundRotationFactor'] *= rotationFactorActiveValue
            rff = vehicleDescr.physics[b'rollingFrictionFactors']
            vehicleDescr.physics[b'rollingFrictionFactors'] = list(rffi * rollingFrictionFactorActiveValue for rffi in rff)
            return

    def _readConfig(self, xmlCtx, section):
        super(Grousers, self)._readConfig(xmlCtx, section)
        self.rotationFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'rotationFactor')
        self.rollingFrictionFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'rollingFrictionFactor')
        return


class RotationMechanisms(StaticOptionalDevice):
    __slots__ = (b'trackMoveSpeedFactor', b'wheelMoveSpeedFactor', b'trackRotateSpeedFactor', b'wheelRotateSpeedFactor', b'wheelCenterRotationFwdSpeed')

    def updateVehicleDescrAttrs(self, vehicleDescr):
        super(RotationMechanisms, self).updateVehicleDescrAttrs(vehicleDescr)
        level = self.defineActiveLevel(vehicleDescr)
        if level is None:
            LOG_DEBUG_DEV((b'updateVehicleDescrAttrs: optional device ({}) is not installed').format(self))
            return
        else:
            isWheeledVehicle = vehicleDescr.type.isWheeledVehicle
            miscAttrs = vehicleDescr.miscAttrs
            onMoveFactor = (isWheeledVehicle or self).trackMoveSpeedFactor if 1 else self.wheelMoveSpeedFactor
            miscAttrs[b'onMoveRotationSpeedFactor'] *= onMoveFactor.getActiveValue(level)
            onRotationFactor = (isWheeledVehicle or self).trackRotateSpeedFactor if 1 else self.wheelRotateSpeedFactor
            miscAttrs[b'onStillRotationSpeedFactor'] *= onRotationFactor.getActiveValue(level)
            miscAttrs[b'centerRotationFwdSpeedFactor'] *= self.wheelCenterRotationFwdSpeed.getActiveValue(level)
            return

    def _readConfig(self, xmlCtx, section):
        super(RotationMechanisms, self)._readConfig(xmlCtx, section)
        self.trackMoveSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'trackMoveSpeedFactor')
        self.wheelMoveSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'wheelMoveSpeedFactor')
        self.trackRotateSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'trackRotateSpeedFactor')
        self.wheelRotateSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'wheelRotateSpeedFactor')
        self.wheelCenterRotationFwdSpeed = LevelsFactor.readTypelessLevelsFactor(xmlCtx, section, b'wheelCenterRotationFwdSpeed')
        return


class ActivatableEquipment(Equipment):
    __slots__ = (b'activeSeconds', b'activeDamageFactor')

    def __init__(self):
        super(ActivatableEquipment, self).__init__()
        self.activeSeconds = None
        self.activeDamageFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        self.activeSeconds = _xml.readIntOrNone(xmlCtx, section, b'activeSeconds')
        self.activeDamageFactor = _xml.readFloat(xmlCtx, section, b'activeDamageFactor', 0.0)
        return

    def isActivatable(self):
        return self.activeSeconds is not None


class Extinguisher(ActivatableEquipment):
    __slots__ = (b'fireStartingChanceFactor', b'autoactivate')

    def __init__(self):
        super(Extinguisher, self).__init__()
        self.fireStartingChanceFactor = component_constants.ZERO_FLOAT
        self.autoactivate = False
        return

    def _readConfig(self, xmlCtx, section):
        super(Extinguisher, self)._readConfig(xmlCtx, section)
        if not section.has_key(b'fireStartingChanceFactor'):
            self.fireStartingChanceFactor = 1.0
        else:
            self.fireStartingChanceFactor = _xml.readPositiveFloat(xmlCtx, section, b'fireStartingChanceFactor')
        self.autoactivate = section.readBool(b'autoactivate', False)
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        try:
            factors[b'engine/fireStartingChance'] *= self.fireStartingChanceFactor
        except:
            pass

        return


class Fuel(Equipment):
    __slots__ = (b'enginePowerFactor', b'turretRotationSpeedFactor')

    def __init__(self):
        super(Fuel, self).__init__()
        self.enginePowerFactor = component_constants.ZERO_FLOAT
        self.turretRotationSpeedFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, section, b'enginePowerFactor')
        self.turretRotationSpeedFactor = _xml.readPositiveFloat(xmlCtx, section, b'turretRotationSpeedFactor')
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        try:
            factors[b'engine/power'] *= self.enginePowerFactor
            factors[b'turret/rotationSpeed'] *= self.turretRotationSpeedFactor
        except:
            pass

        return


class Stimulator(Equipment):
    __slots__ = (b'crewLevelIncrease',)

    def __init__(self):
        super(Stimulator, self).__init__()
        self.crewLevelIncrease = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        self.crewLevelIncrease = _xml.readFloat(xmlCtx, section, b'crewLevelIncrease', component_constants.ZERO_FLOAT)
        return


class Repairkit(ActivatableEquipment):
    __slots__ = (b'repairAll', b'bonusValue', b'isMedkit', b'isRepairkit')

    def __init__(self):
        super(Repairkit, self).__init__()
        self.isMedkit = False
        self.repairAll = False
        self.isRepairkit = False
        self.bonusValue = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(Repairkit, self)._readConfig(xmlCtx, section)
        self.isMedkit = b'medkit' in self.tags
        self.isRepairkit = b'repairkit' in self.tags
        self.repairAll = section.readBool(b'repairAll', False)
        self.bonusValue = _xml.readFraction(xmlCtx, section, b'bonusValue')
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        if self.isRepairkit:
            factors[b'repairSpeed'] *= 1.0 + self.bonusValue
        return


class CountableConsumableConfigReader(object):
    _CONSUMABLE_SLOTS = (b'consumeAmmo',)

    def initCountableConsumableSlots(self):
        self.consumeAmmo = False
        return

    def readCountableConsumableConfig(self, xmlCtx, section):
        self.consumeAmmo = _xml.readBool(xmlCtx, section, b'consumeAmmo')
        return


class RepairkitBattleRoyale(Repairkit, CountableConsumableConfigReader):

    def __init__(self):
        super(RepairkitBattleRoyale, self).__init__()
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, section):
        super(RepairkitBattleRoyale, self)._readConfig(xmlCtx, section)
        self.readCountableConsumableConfig(xmlCtx, section)
        return


class RemovedRpmLimiter(Equipment):
    __slots__ = (b'enginePowerFactor', b'engineHpLossPerSecond')

    def __init__(self):
        super(RemovedRpmLimiter, self).__init__()
        self.enginePowerFactor = component_constants.ZERO_FLOAT
        self.engineHpLossPerSecond = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, section, b'enginePowerFactor')
        self.engineHpLossPerSecond = _xml.readPositiveFloat(xmlCtx, section, b'engineHpLossPerSecond')
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        try:
            factors[b'engine/power'] *= self.enginePowerFactor
        except:
            pass

        return


class Afterburning(Equipment):
    __slots__ = (b'deploySeconds', b'consumeSeconds', b'rechargeSeconds', b'enginePowerFactor', b'maxSpeedFactor')

    def __init__(self):
        super(Afterburning, self).__init__()
        self.deploySeconds = component_constants.ZERO_INT
        self.consumeSeconds = component_constants.ZERO_INT
        self.rechargeSeconds = component_constants.ZERO_INT
        self.enginePowerFactor = component_constants.ZERO_FLOAT
        self.maxSpeedFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        self.deploySeconds = _xml.readInt(xmlCtx, section, b'deploySeconds', 0)
        self.consumeSeconds = _xml.readInt(xmlCtx, section, b'consumeSeconds', 0)
        self.rechargeSeconds = _xml.readInt(xmlCtx, section, b'rechargeSeconds', 0)
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, section, b'enginePowerFactor')
        self.maxSpeedFactor = _xml.readPositiveFloat(xmlCtx, section, b'maxSpeedFactor')
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        try:
            factors[b'engine/power'] *= self.enginePowerFactor
            factors[b'vehicle/maxSpeed'] *= self.maxSpeedFactor
        except:
            pass

        return


class AfterburningBattleRoyale(Equipment, CountableConsumableConfigReader):
    __slots__ = (b'consumeSeconds', b'enginePowerFactor', b'maxSpeedFactor', b'vehicleRotationSpeed', b'deploySeconds', b'rechargeSeconds')

    def __init__(self):
        super(AfterburningBattleRoyale, self).__init__()
        self.consumeSeconds = component_constants.ZERO_INT
        self.enginePowerFactor = component_constants.ZERO_FLOAT
        self.maxSpeedFactor = component_constants.ZERO_FLOAT
        self.vehicleRotationSpeed = component_constants.ZERO_FLOAT
        self.deploySeconds = component_constants.ZERO_FLOAT
        self.rechargeSeconds = component_constants.ZERO_FLOAT
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, section):
        self.consumeSeconds = _xml.readInt(xmlCtx, section, b'consumeSeconds', 0)
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, section, b'enginePowerFactor')
        self.maxSpeedFactor = _xml.readPositiveFloat(xmlCtx, section, b'maxSpeedFactor')
        self.vehicleRotationSpeed = _xml.readPositiveFloat(xmlCtx, section, b'vehicleRotationSpeed')
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def updateVehicleAttrFactors(self, vehicleDescr, factors, aspect):
        try:
            from debug_utils import LOG_DEBUG_DEV
            factors[b'engine/power'] *= self.enginePowerFactor
            factors[b'vehicle/maxSpeed'] *= self.maxSpeedFactor
        except:
            pass

        return

    def _getDescription(self, descr):
        localizeDescr = super(AfterburningBattleRoyale, self)._getDescription(descr)
        return i18n.makeString(localizeDescr, duration=self.consumeSeconds)


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


class TrapPoint(Equipment, CountableConsumableConfigReader):
    __slots__ = (b'influenceZone',)

    def __init__(self):
        super(TrapPoint, self).__init__()
        self.influenceZone = InfluenceZone()
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, section):
        super(TrapPoint, self)._readConfig(xmlCtx, section)
        self.influenceZone._readConfig(xmlCtx, section[b'influenceZone'])
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def _getDescription(self, descr):
        localizeDescr = super(TrapPoint, self)._getDescription(descr)
        if self.influenceZone.debuffFactors:
            return i18n.makeString(localizeDescr, duration=int(self.influenceZone.timer), power=int((1 - self.influenceZone.debuffFactors[b'engine/power']) * 100), maxSpeed=int((1 - self.influenceZone.debuffFactors[b'vehicle/maxSpeed']) * 100), rotationSpeed=int((1 - self.influenceZone.debuffFactors[b'vehicle/rotationSpeed']) * 100), chassisRotationSpeed=int((1 - self.influenceZone.debuffFactors[b'chassis/shotDispersionFactors/rotation']) * 100), turretRotationSpeed=int((1 - self.influenceZone.debuffFactors[b'turret/rotationSpeed']) * 100))
        if self.influenceZone.hotParams:
            return i18n.makeString(localizeDescr, duration=int(self.influenceZone.timer), healPerSecond=int(self.influenceZone.hotParams.healPerTick * 100 / self.influenceZone.hotParams.tickInterval))
        return


class RageEquipmentConfigReader(object):
    _RAGE_EQUIPMENT_SLOTS = (b'reusable', b'cooldownTime', b'deployTime')

    def initRageEquipmentSlots(self):
        self.reusable = False
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.deployTime = component_constants.ZERO_FLOAT
        return

    def readRageEquipmentConfig(self, xmlCtx, section):
        self.reusable = _xml.readBool(xmlCtx, section, b'reusable')
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownTime') if self.reusable else 0.0
        self.deployTime = _xml.readNonNegativeFloat(xmlCtx, section, b'deployTime')
        return


class SharedCooldownConsumableConfigReader(object):
    _SHARED_COOLDOWN_CONSUMABLE_SLOTS = (b'cooldownTimeRespawnFactor', b'reserveUnlockFactor', b'startCooldownTimeFactor', b'cooldownTime', b'cooldownFactors', b'sharedCooldownTime', b'consumeAmmo', b'disableAllyDamage', b'setUnavailableAfterAmmoLeft')

    def initSharedCooldownConsumableSlots(self):
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.cooldownTimeRespawnFactor = component_constants.ZERO_FLOAT
        self.reserveUnlockFactor = component_constants.ZERO_FLOAT
        self.startCooldownTimeFactor = component_constants.ZERO_FLOAT
        self.cooldownFactors = component_constants.EMPTY_DICT
        self.consumeAmmo = False
        self.disableAllyDamage = False
        self.setUnavailableAfterAmmoLeft = False
        return

    def readSharedCooldownConsumableConfig(self, xmlCtx, section):
        self.cooldownTimeRespawnFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownTimeRespawnFactor', 1.0)
        self.reserveUnlockFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'reserveUnlockFactor', -1.0)
        self.startCooldownTimeFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'startCooldownTimeFactor', 1.0)
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownTime')
        self.cooldownFactors = self._readCooldownFactors(xmlCtx, section, b'cooldownFactors')
        self.sharedCooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'sharedCooldownTime')
        self.consumeAmmo = _xml.readBool(xmlCtx, section, b'consumeAmmo')
        self.disableAllyDamage = _xml.readBool(xmlCtx, section, b'disableAllyDamage')
        self.setUnavailableAfterAmmoLeft = _xml.readBool(xmlCtx, section, b'setUnavailableAfterAmmoLeft', False)
        return

    def _readCooldownFactors(self, xmlCtx, section, name):
        cooldownFactors = {}
        subXmlCtx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, name)
        for vehClass, _ in _xml.getItemsWithContext(subXmlCtx, subsection):
            cooldownFactors[vehClass] = _xml.readNonNegativeFloat(subXmlCtx, subsection, vehClass)

        return cooldownFactors


class CooldownConsumableConfigReader(object):
    _CONSUMABLE_SLOTS = (b'deployTime', b'cooldownTime')

    def initConsumableWithDeployTimeSlots(self):
        self.deployTime = component_constants.ZERO_FLOAT
        self.cooldownTime = component_constants.ZERO_FLOAT
        return

    def readConsumableWithTimeConfig(self, xmlCtx, section):
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownTime')
        return


class TooltipConfigReader(object):
    _SHARED_TOOLTIPS_CONSUMABLE_SLOTS = (b'shortDescription', b'longDescription', b'longFilterAlert', b'tooltipIdentifiers')

    def initTooltipInformation(self):
        self.shortDescription = component_constants.EMPTY_STRING
        self.longDescription = component_constants.EMPTY_STRING
        self.shortFilterAlert = component_constants.EMPTY_STRING
        self.longFilterAlert = component_constants.EMPTY_STRING
        self.tooltipIdentifiers = []
        return

    def readTooltipInformation(self, xmlCtx, section):
        if IS_CLIENT:
            self.shortDescription = _xml.readString(xmlCtx, section, b'shortDescription')
            self.longDescription = _xml.readString(xmlCtx, section, b'longDescription')
            self.shortFilterAlert = _xml.readStringOrEmpty(xmlCtx, section, b'shortFilterAlert')
            self.longFilterAlert = _xml.readStringOrEmpty(xmlCtx, section, b'longFilterAlert')
            tooltipsString = _xml.readStringOrNone(xmlCtx, section, b'tooltips')
            if tooltipsString is not None:
                self.tooltipIdentifiers = tooltipsString.split()
        return


class BaseMarkerConfigReader(object):
    _MARKER_SLOTS_ = (b'areaVisual', b'areaColor', b'areaMarker', b'areaUsedPrefab')

    def initMarkerInformation(self):
        self.areaVisual = None
        self.areaColor = None
        self.areaMarker = None
        self.areaUsedPrefab = None
        return

    def readMarkerConfig(self, xmlCtx, section):
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.areaMarker = _xml.readStringOrNone(xmlCtx, section, b'areaMarker')
        self.areaUsedPrefab = section.readString(b'areaUsedPrefab') or None
        return


class AreaMarkerConfigReader(BaseMarkerConfigReader):
    _MARKER_SLOTS_ = BaseMarkerConfigReader._MARKER_SLOTS_ + (b'areaRadius', b'areaLength', b'areaWidth')

    def initMarkerInformation(self):
        super(AreaMarkerConfigReader, self).initMarkerInformation()
        self.areaRadius = component_constants.ZERO_FLOAT
        self.areaLength = component_constants.ZERO_FLOAT
        self.areaWidth = component_constants.ZERO_FLOAT
        return

    def readMarkerConfig(self, xmlCtx, section):
        super(AreaMarkerConfigReader, self).readMarkerConfig(xmlCtx, section)
        self.areaRadius = _xml.readPositiveFloat(xmlCtx, section, b'areaRadius')
        self.areaLength = self.areaWidth = self.areaRadius * 2
        return


class EffectsConfigReader(object):
    _EFFECTS_SLOTS_ = (b'effects',)

    def initEffectsInformation(self):
        self.effects = None
        return

    def readEffectConfig(self, xmlCtx, section):
        self.effects = {name: self._readEffect((xmlCtx, b'effects'), effect) for name, effect in section[b'effects'].items()}
        return self.effects

    def _readEffect(self, xmlCtx, section):
        if not section:
            return None
        else:
            effect = {b'shotEffects': (section.readString(b'shotEffects').split()), 
               b'sequences': (self._readSequencesConfig(section[b'sequences'])), 
               b'groundRaycast': (section.readBool(b'groundRaycast')), 
               b'offsetDeviation': (section.readFloat(b'offsetDeviation')), 
               b'repeatCount': (section.readInt(b'repeatCount', 1)), 
               b'repeatDelay': (section.readFloat(b'repeatDelay')), 
               b'areaColor': (_xml.readIntOrNone(xmlCtx, section, b'areaColor')), 
               b'repeatDelayDeviationPercent': 0}
            if section.has_key(b'repeatDelayDeviationPercent'):
                effect[b'repeatDelayDeviationPercent'] = _xml.readInt(xmlCtx, section, b'repeatDelayDeviationPercent', minVal=0, maxVal=100)
            return effect

    def _readSequencesConfig(self, section):
        if not section:
            return {}
        sequences = {}
        for name, subsection in section.items():
            if name == b'sequence':
                sequenceID = subsection.readString(b'name')
                sequences[sequenceID] = {b'scale': (subsection.readVector3(b'scale', Vector3(1, 1, 1)))}

        return sequences


class ArtilleryConfigReader(AreaMarkerConfigReader):
    _ARTILLERY_SLOTS = AreaMarkerConfigReader._MARKER_SLOTS_ + (b'delay', b'duration', b'shotsNumber', b'areaRadius', b'shellCompactDescr', b'piercingPower', b'noOwner', b'shotSoundPreDelay', b'wwsoundShot', b'wwsoundEquipmentUsed')

    def initArtillerySlots(self):
        super(ArtilleryConfigReader, self).__init__()
        self.initMarkerInformation()
        self.delay = component_constants.ZERO_FLOAT
        self.duration = component_constants.ZERO_FLOAT
        self.shotsNumber = component_constants.ZERO_INT
        self.shellCompactDescr = component_constants.ZERO_INT
        self.piercingPower = component_constants.ZERO_FLOAT
        self.shotSoundPreDelay = component_constants.ZERO_FLOAT
        self.wwsoundShot = None
        self.wwsoundEquipmentUsed = None
        return

    def readArtilleryConfig(self, xmlCtx, section):
        self.readMarkerConfig(xmlCtx, section)
        self.delay = _xml.readPositiveFloat(xmlCtx, section, b'delay')
        self.duration = _xml.readPositiveFloat(xmlCtx, section, b'duration')
        self.shotsNumber = _xml.readNonNegativeInt(xmlCtx, section, b'shotsNumber')
        self.shellCompactDescr = _xml.readInt(xmlCtx, section, b'shellCompactDescr')
        self.piercingPower = _xml.readTupleOfPositiveInts(xmlCtx, section, b'piercingPower', 2)
        self.noOwner = _xml.readBool(xmlCtx, section, b'noOwner')
        self.shotSoundPreDelay = _xml.readIntOrNone(xmlCtx, section, b'shotSoundPreDelay')
        self.wwsoundShot = _xml.readStringOrNone(xmlCtx, section, b'wwsoundShot')
        self.wwsoundEquipmentUsed = _xml.readStringOrNone(xmlCtx, section, b'wwsoundEquipmentUsed')
        return


class PlaneConfigReader(object):
    _PLANE_SLOTS = (b'delay', b'speed', b'modelName', b'soundEvent', b'heights', b'areaVisual', b'areaColor', b'areaMarker')

    def initPlaneSlots(self):
        self.delay = component_constants.ZERO_FLOAT
        self.speed = component_constants.ZERO_INT
        self.modelName = component_constants.EMPTY_STRING
        self.soundEvent = component_constants.EMPTY_STRING
        self.heights = component_constants.EMPTY_TUPLE
        self.areaVisual = None
        self.areaColor = None
        self.areaMarker = None
        return

    def readPlaneConfig(self, xmlCtx, section):
        self.delay = _xml.readPositiveFloat(xmlCtx, section, b'delay')
        self.speed = _xml.readPositiveFloat(xmlCtx, section, b'speed')
        self.modelName = _xml.readString(xmlCtx, section, b'modelName')
        if IS_CLIENT:
            self.soundEvent = _xml.readString(xmlCtx, section, b'wwsoundEvent')
        self.heights = _xml.readTupleOfPositiveInts(xmlCtx, section, b'heights', 2)
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.areaMarker = _xml.readStringOrNone(xmlCtx, section, b'areaMarker')
        return


class BomberConfigReader(PlaneConfigReader):
    _BOMBER_SLOTS = PlaneConfigReader._PLANE_SLOTS + (b'areaLength', b'areaWidth', b'antepositions', b'lateropositions', b'bombingMask', b'waveFraction', b'bombsNumber', b'shellCompactDescr', b'tracerKind', b'piercingPower', b'gravity', b'noOwner', b'wwsoundEquipmentUsed', b'shootingDistance')

    def initBomberSlots(self):
        self.initPlaneSlots()
        self.areaLength = component_constants.ZERO_FLOAT
        self.areaWidth = component_constants.ZERO_FLOAT
        self.antepositions = component_constants.EMPTY_TUPLE
        self.lateropositions = component_constants.EMPTY_TUPLE
        self.bombingMask = component_constants.EMPTY_TUPLE
        self.waveFraction = component_constants.ZERO_FLOAT
        self.bombsNumber = component_constants.ZERO_INT
        self.shellCompactDescr = component_constants.ZERO_INT
        self.tracerKind = component_constants.ZERO_INT
        self.piercingPower = component_constants.EMPTY_TUPLE
        self.gravity = component_constants.ZERO_FLOAT
        self.shootingDistance = component_constants.ZERO_FLOAT
        self.noOwner = False
        self.wwsoundEquipmentUsed = None
        return

    def readBomberConfig(self, xmlCtx, section):
        self.readPlaneConfig(xmlCtx, section)
        self.areaLength = _xml.readPositiveFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, section, b'areaWidth')
        self.antepositions = _xml.readTupleOfFloats(xmlCtx, section, b'antepositions')
        self.lateropositions = _xml.readTupleOfFloats(xmlCtx, section, b'lateropositions')
        self.bombingMask = tuple(bool(v) for v in _xml.readTupleOfInts(xmlCtx, section, b'bombingMask'))
        if not len(self.antepositions) == len(self.lateropositions) == len(self.bombingMask):
            _xml.raiseWrongSection(xmlCtx, b'bombers number mismatch')
        self.waveFraction = _xml.readPositiveFloat(xmlCtx, section, b'waveFraction')
        self.bombsNumber = _xml.readNonNegativeInt(xmlCtx, section, b'bombsNumber')
        self.shellCompactDescr = _xml.readInt(xmlCtx, section, b'shellCompactDescr')
        self.tracerKind = _xml.readInt(xmlCtx, section, b'tracerKind')
        self.piercingPower = _xml.readTupleOfPositiveInts(xmlCtx, section, b'piercingPower', 2)
        self.gravity = _xml.readPositiveFloat(xmlCtx, section, b'gravity')
        self.shootingDistance = _xml.readNonNegativeFloat(xmlCtx, section, b'shootingDistance', 0.0)
        self.noOwner = _xml.readBool(xmlCtx, section, b'noOwner')
        self.wwsoundEquipmentUsed = _xml.readStringOrNone(xmlCtx, section, b'wwsoundEquipmentUsed')
        return


class SmokeConfigReader(object):
    _SMOKE_SLOTS = (b'minDelay', b'deltaDelayRange', b'smokeModelName', b'startRadius', b'expandedRadius', b'startHeight', b'expandedHeight', b'heightUpFraction', b'postEffectTeams', b'expansionDuration', b'dispersionRadius', b'totalDuration', b'smokeOpacity', b'visionRadiusFactor', b'dotParams', b'areaLength', b'areaWidth', b'projectilesNumber', b'shellCompactDescr', b'areaVisual', b'areaMarker', b'noOwner', b'smokeEffectNameAlly', b'smokeEffectNameEnemy', b'shotSoundPreDelay', b'wwsoundShot', b'orthogonalDir', b'randomizeDuration', b'vignetteColor', b'vignetteIntensity')

    def initSmokeSlots(self):
        self.minDelay = component_constants.ZERO_FLOAT
        self.deltaDelayRange = component_constants.EMPTY_TUPLE
        self.smokeModelName = component_constants.EMPTY_STRING
        self.startRadius = component_constants.ZERO_FLOAT
        self.expandedRadius = component_constants.ZERO_FLOAT
        self.startHeight = component_constants.ZERO_FLOAT
        self.expandedHeight = component_constants.ZERO_FLOAT
        self.heightUpFraction = component_constants.ZERO_FLOAT
        self.expansionDuration = component_constants.ZERO_FLOAT
        self.dispersionRadius = component_constants.ZERO_FLOAT
        self.totalDuration = component_constants.ZERO_FLOAT
        self.smokeOpacity = component_constants.ZERO_FLOAT
        self.attrFactorMods = {}
        self.expireDelay = component_constants.ZERO_FLOAT
        self.postEffectTeams = []
        self.dotParams = None
        self.areaLength = component_constants.ZERO_FLOAT
        self.areaWidth = component_constants.ZERO_FLOAT
        self.projectilesNumber = component_constants.ZERO_INT
        self.shellCompactDescr = component_constants.ZERO_INT
        self.areaVisual = None
        self.areaColor = None
        self.areaMarker = None
        self.noOwner = False
        self.smokeEffectNameAlly = component_constants.EMPTY_STRING
        self.smokeEffectNameEnemy = component_constants.EMPTY_STRING
        self.shotSoundPreDelay = component_constants.ZERO_FLOAT
        self.wwsoundShot = None
        self.orthogonalDir = False
        self.randomizeDuration = None
        self.vignetteColor = Vector3()
        self.vignetteIntensity = component_constants.ZERO_FLOAT
        return

    def readSmokeConfig(self, xmlCtx, section):
        self.minDelay = _xml.readPositiveFloat(xmlCtx, section, b'minDelay')
        self.deltaDelayRange = _xml.readTupleOfPositiveFloats(xmlCtx, section, b'deltaDelayRange', 2)
        self.smokeModelName = _xml.readString(xmlCtx, section, b'smokeModelName')
        self.startRadius = _xml.readPositiveFloat(xmlCtx, section, b'startRadius')
        self.expandedRadius = _xml.readPositiveFloat(xmlCtx, section, b'expandedRadius')
        self.startHeight = _xml.readPositiveFloat(xmlCtx, section, b'startHeight')
        self.expandedHeight = _xml.readPositiveFloat(xmlCtx, section, b'expandedHeight')
        self.heightUpFraction = _xml.readPositiveFloat(xmlCtx, section, b'heightUpFraction')
        self.expansionDuration = _xml.readPositiveFloat(xmlCtx, section, b'expansionDuration')
        self.dispersionRadius = _xml.readPositiveFloat(xmlCtx, section, b'dispersionRadius')
        self.totalDuration = _xml.readPositiveFloat(xmlCtx, section, b'totalDuration')
        self.smokeOpacity = _xml.readPositiveFloat(xmlCtx, section, b'smokeOpacity')
        subXmlCtx, attrFactorModsSection = _xml.getSubSectionWithContext(xmlCtx, section, b'attrFactorMods', False)
        if attrFactorModsSection is not None:
            self._readAttrFactorMods(subXmlCtx, attrFactorModsSection)
        subXmlCtx, postEffectsSection = _xml.getSubSectionWithContext(xmlCtx, section, b'postEffect', False)
        if postEffectsSection is not None:
            self._readPostEffectTeams(subXmlCtx, postEffectsSection)
        self.expireDelay = _xml.readPositiveFloat(xmlCtx, section, b'expireDelay', component_constants.ZERO_FLOAT)
        self.areaLength = _xml.readPositiveFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, section, b'areaWidth')
        self.projectilesNumber = _xml.readNonNegativeInt(xmlCtx, section, b'projectilesNumber')
        self.shellCompactDescr = _xml.readInt(xmlCtx, section, b'shellCompactDescr')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.areaMarker = _xml.readStringOrNone(xmlCtx, section, b'areaMarker')
        self.noOwner = _xml.readBool(xmlCtx, section, b'noOwner')
        self.smokeEffectNameAlly = _xml.readString(xmlCtx, section, b'smokeEffectNameAlly')
        self.smokeEffectNameEnemy = _xml.readString(xmlCtx, section, b'smokeEffectNameEnemy')
        self.shotSoundPreDelay = _xml.readIntOrNone(xmlCtx, section, b'shotSoundPreDelay')
        self.wwsoundShot = _xml.readStringOrNone(xmlCtx, section, b'wwsoundShot')
        if section.has_key(b'randomizeDuration'):
            self.randomizeDuration = _xml.readFloat(xmlCtx, section, b'randomizeDuration')
        if section.has_key(b'dotParams'):
            self.dotParams = DOTParams(ATTACK_REASON_INDICES[ATTACK_REASON.SMOKE])
            self.dotParams._readConfig(xmlCtx, section[b'dotParams'])
        if IS_CLIENT:
            self.vignetteColor = _xml.readVector3(xmlCtx, section, b'vignetteColor')
            self.vignetteIntensity = _xml.readFloat(xmlCtx, section, b'vignetteIntensity')
        return

    def _readAttrFactorMods(self, xmlCtx, section):
        for factor, subSection in section.items():
            self.attrFactorMods[factor] = (
             _xml.readFloat(xmlCtx, subSection, b'value'),
             _xml.readBool(xmlCtx, subSection, b'ignoreAllies', True))

        return

    def _readPostEffectTeams(self, _, section):
        if section.has_key(b'enemy'):
            self.postEffectTeams.append(False)
        if section.has_key(b'ally'):
            self.postEffectTeams.append(True)
        return


class ReconConfigReader(PlaneConfigReader):
    _RECON_SLOTS = PlaneConfigReader._PLANE_SLOTS + (b'areaRadius', b'entitiesToSearch', b'scanPointsAmount', b'antepositions', b'lateropositions', b'areaWidth', b'areaLength', b'wwsoundEquipmentUsed')

    def initReconSlots(self):
        self.initPlaneSlots()
        self.entitiesToSearch = {}
        self.areaRadius = component_constants.ZERO_FLOAT
        self.scanPointsAmount = component_constants.ZERO_INT
        self.antepositions = component_constants.EMPTY_TUPLE
        self.lateropositions = component_constants.EMPTY_TUPLE
        self.areaLength = component_constants.ZERO_FLOAT
        self.areaWidth = component_constants.ZERO_FLOAT
        self.wwsoundEquipmentUsed = None
        return

    def readReconConfig(self, xmlCtx, section):
        self.readPlaneConfig(xmlCtx, section)
        self.entitiesToSearch = self.__readEntitiesToSearch(xmlCtx, section)
        self.scanPointsAmount = _xml.readNonNegativeInt(xmlCtx, section, b'scanPointsAmount')
        self.antepositions = _xml.readTupleOfFloats(xmlCtx, section, b'antepositions')
        self.lateropositions = _xml.readTupleOfFloats(xmlCtx, section, b'lateropositions')
        self.areaRadius = self.entitiesToSearch.get(b'Vehicle', {}).get(b'radius') or self.entitiesToSearch.values()[0][b'radius']
        self.areaWidth = self.areaRadius * 2
        self.areaLength = self.areaRadius * (2 + self.scanPointsAmount - 1)
        self.wwsoundEquipmentUsed = _xml.readStringOrNone(xmlCtx, section, b'wwsoundEquipmentUsed')
        return

    def __readEntitiesToSearch(self, xmlCtx, section):
        entitiesToSearch = {}
        for entity in section[b'entitiesToSearch'].values():
            entityClassName = _xml.readString(xmlCtx, entity, b'name')
            radius = _xml.readPositiveFloat(xmlCtx, entity, b'radius')
            spottingDuration = _xml.readPositiveFloat(xmlCtx, entity, b'spottingDuration')
            entitiesToSearch[entityClassName] = {b'radius': radius, b'spottingDuration': spottingDuration}

        return entitiesToSearch


class BuffConfigReader(object):
    _BUFF_SLOTS = (b'duration', b'inactivationDelay', b'radius', b'wwsoundEquipmentUsed')

    def initBuffSlots(self):
        self.duration = component_constants.ZERO_FLOAT
        self.inactivationDelay = component_constants.ZERO_FLOAT
        self.radius = component_constants.ZERO_FLOAT
        self.wwsoundEquipmentUsed = None
        return

    def readBuffConfig(self, xmlCtx, section):
        self.duration = _xml.readPositiveFloat(xmlCtx, section, b'duration')
        self.inactivationDelay = _xml.readNonNegativeFloat(xmlCtx, section, b'inactivationDelay')
        self.radius = _xml.readFloat(xmlCtx, section, b'radius')
        self.wwsoundEquipmentUsed = _xml.readStringOrNone(xmlCtx, section, b'wwsoundEquipmentUsed')
        return


class InspireConfigReader(BuffConfigReader):
    _INSPIRE_SLOTS = BuffConfigReader._BUFF_SLOTS + (b'increaseFactors',)

    def initInspireSlots(self):
        super(InspireConfigReader, self).initBuffSlots()
        self.increaseFactors = {}
        return

    def readInspireConfig(self, xmlCtx, section):
        super(InspireConfigReader, self).readBuffConfig(xmlCtx, section)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'increaseFactors')
        return


class HealPointConfigReader(BuffConfigReader):
    _HEAL_POINT_SLOTS = BuffConfigReader._BUFF_SLOTS + (b'healPerTick', b'expireByDamageReceived', b'healGroup', b'tickInterval', b'height', b'depth')

    def initHealPointSlots(self):
        super(HealPointConfigReader, self).initBuffSlots()
        self.healPerTick = component_constants.ZERO_FLOAT
        self.expireByDamageReceived = False
        self.healGroup = None
        self.tickInterval = 1.0
        self.height = 1.0
        self.depth = 1.0
        return

    def readHealPointConfig(self, xmlCtx, section):
        super(HealPointConfigReader, self).readBuffConfig(xmlCtx, section)
        self.healPerTick = _xml.readPositiveFloat(xmlCtx, section, b'healPerTick')
        self.expireByDamageReceived = _xml.readBool(xmlCtx, section, b'expireByDamageReceived')
        self.healGroup = _xml.readIntOrNone(xmlCtx, section, b'healGroup')
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, section, b'tickInterval', 1.0)
        self.height = _xml.readPositiveFloat(xmlCtx, section, b'height', 1.0)
        self.depth = _xml.readPositiveFloat(xmlCtx, section, b'depth', 1.0)
        return


class ArenaAimLimits(object):
    __slots__ = (b'insetRadius', b'areaSwitch', b'areaColor')

    def __init__(self):
        self.insetRadius = 0.0
        self.areaSwitch = None
        self.areaColor = None
        return

    def __repr__(self):
        return (b'ArenaAimLimits (Radius:{}, Visual:{}, Color:{}, )').format(self.insetRadius, self.areaSwitch, self.areaColor)

    def _readConfig(self, xmlCtx, section):
        self.insetRadius = _xml.readPositiveFloat(xmlCtx, section, b'insetRadius', 0)
        self.areaSwitch = _xml.readStringOrNone(xmlCtx, section, b'areaSwitch')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        return

    @staticmethod
    def readConfig(xmlCtx, section, subsection_name):
        if not section.has_key(subsection_name):
            return None
        else:
            result = ArenaAimLimits()
            result._readConfig(xmlCtx, section[subsection_name])
            return result


class ArcadeEquipmentConfigReader(object):
    _SHARED_ARCADE_SLOTS = (b'minApplyRadius', b'maxApplyRadius', b'cameraPivotPosMin', b'cameraPivotPosMax', b'arenaAimLimits')

    def initArcadeInformation(self):
        self.minApplyRadius = component_constants.ZERO_FLOAT
        self.maxApplyRadius = component_constants.ZERO_FLOAT
        self.cameraPivotPosMin = Vector3()
        self.cameraPivotPosMax = Vector3()
        self.arenaAimLimits = None
        return

    def readArcadeInformation(self, xmlCtx, section):
        self.minApplyRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'minApplyRadius', component_constants.ZERO_FLOAT)
        self.maxApplyRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'maxApplyRadius', component_constants.ZERO_FLOAT)
        self.arenaAimLimits = ArenaAimLimits.readConfig(xmlCtx, section, b'arenaAimLimits')
        if IS_CLIENT:
            self.cameraPivotPosMin = _xml.readVector3OrNone(xmlCtx, section, b'cameraPivotPosMin')
            self.cameraPivotPosMax = _xml.readVector3OrNone(xmlCtx, section, b'cameraPivotPosMax')
        return


class DynamicEquipment(Equipment):
    __slots__ = (b'_config',)

    def __init__(self):
        super(DynamicEquipment, self).__init__()
        self._config = []
        return

    def _readConfig(self, xmlCtx, section):
        self._config = []
        for subsection in section.values():
            if subsection.name == b'level':
                self._config.append(self._readLevelConfig(xmlCtx, subsection))
            else:
                _xml.raiseWrongXml(xmlCtx, subsection.name, b'should be <params>')

        return

    def getLevelIDForVehicle(self, vehicleDescr):
        for levelID, (levelFilter, _) in enumerate(self._config):
            if levelFilter.checkCompatibility(vehicleDescr):
                return levelID

        return

    def doesDependOnOptionalDevice(self):
        return True

    def getLevelParamsForDevice(self, optionalDevice):
        for levelFilter, levelParams in self._config:
            if levelFilter.checkCompatibilityWithDevice(optionalDevice):
                return levelParams

        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, _, *args, **kwargs):
        levelID = self.getLevelIDForVehicle(vehicleDescr)
        if levelID is not None:
            self.updateVehicleAttrFactorsForLevel(factors, levelID)
        return

    def updateVehicleAttrFactorsForLevel(self, factors, levelID):
        _, levelParams = self._config[levelID]
        self._updateVehicleAttrFactorsImpl(factors, levelParams)
        return

    def _readLevelConfig(self, xmlCtx, section):
        raise NotImplemented
        return

    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        raise NotImplemented
        return


class FactorBattleBooster(DynamicEquipment):
    __slots__ = ()

    def _readLevelConfig(self, xmlCtx, section):
        filter = _OptionalDeviceFilter(xmlCtx, section[b'deviceFilter'])
        attribute = _xml.readNonEmptyString(xmlCtx, section, b'attribute')
        factor = _xml.readPositiveFloat(xmlCtx, section, b'factor')
        return (filter, (attribute, factor))

    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        attribute, factor = levelParams
        factors[attribute] *= factor
        return


class AdditiveBattleBooster(DynamicEquipment):
    __slots__ = ()

    def _readLevelConfig(self, xmlCtx, section):
        filter = _OptionalDeviceFilter(xmlCtx, section[b'deviceFilter'])
        attribute = _xml.readNonEmptyString(xmlCtx, section, b'attribute')
        value = _xml.readPositiveFloat(xmlCtx, section, b'value')
        return (filter, (attribute, value))

    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        attribute, value = levelParams
        factors[attribute] += value
        return


class InvisibilityBattleBooster(DynamicEquipment):
    __slots__ = ()

    def _readLevelConfig(self, xmlCtx, section):
        filter = _OptionalDeviceFilter(xmlCtx, section[b'deviceFilter'])
        attribute = _xml.readNonEmptyString(xmlCtx, section, b'attribute')
        factors = _xml.readTupleOfPositiveFloats(xmlCtx, section, b'factors', count=2)
        return (filter, (attribute, factors))

    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        attribute, factor = levelParams
        factors[attribute][0] += factor[0]
        factors[attribute][1] *= factor[1]
        return


class SkillEquipment(Equipment):
    __slots__ = (b'skillName', b'perkLevelMultiplier')

    def __init__(self):
        super(SkillEquipment, self).__init__()
        self.skillName = component_constants.EMPTY_STRING
        self.perkLevelMultiplier = None
        return

    def _readConfig(self, xmlCtx, section):
        super(SkillEquipment, self)._readConfig(xmlCtx, section)
        self.skillName = _xml.readNonEmptyString(xmlCtx, section, b'skillName')
        self.perkLevelMultiplier = _xml.readFloatOrNone(xmlCtx, section, b'perkLevelMultiplier')
        return

    def updateCrewSkill(self, *args):
        return


class FactorSkillBattleBooster(SkillEquipment):
    __slots__ = (b'efficiencyFactor',)

    def __init__(self):
        super(FactorSkillBattleBooster, self).__init__()
        self.efficiencyFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(FactorSkillBattleBooster, self)._readConfig(xmlCtx, section)
        self.efficiencyFactor = _xml.readPositiveFloat(xmlCtx, section, b'efficiencyFactor')
        return

    def updateCrewSkill(self, a):
        if a.baseAvgLevel < 100:
            a.factor = max(1.0, a.factor)
            a.baseAvgLevel = 100
        else:
            a.factor = 0.57 + (a.factor - 0.57) * self.efficiencyFactor
        return


class EconomicDirectives(Equipment):
    __slots__ = (b'equipmentOperation', b'operatiomType')
    OPERATIONS_TYPE = {b'add': b'additive', b'mul': b'multiplicative'}

    def __init__(self):
        super(EconomicDirectives, self).__init__()
        self.equipmentOperation = None
        self.operatiomType = None
        return

    def _readConfig(self, xmlCtx, section):
        subXmlCtx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, b'modifiers')
        modifiers = []
        for opType, m in subsection.items():
            if not self.operatiomType:
                self.operatiomType = opType
            elif self.operatiomType != opType:
                _xml.raiseWrongXml(subXmlCtx, opType, b'Cannot be different modifier type')
            name = m.readString(b'name')
            value = m.readInt(b'value')
            if not name or not value:
                _xml.raiseWrongXml(subXmlCtx, opType, b'Has not attribute name or value')
            if not any(item[0] == name for item in modifiers):
                modifiers.append((name, value))
            else:
                _xml.raiseWrongXml(xmlCtx, b'modifiers', (b'modifier: {} is duplicated').format(name))
            if opType not in self.OPERATIONS_TYPE.keys():
                _xml.raiseWrongXml(xmlCtx, b'modifiers', (b'Unknown operation type: {}. Use one of the {}').format(opType, self.OPERATIONS_TYPE.keys()))

        self.equipmentOperation = Operation(self.OPERATIONS_TYPE[self.operatiomType], modifiers)
        return

    def getLevelParamsForDevice(self, *_):
        return

    def getLevelIDForVehicle(self, *_):
        return


class SixthSenseBattleBooster(SkillEquipment):
    __slots__ = (b'turnOnDelay', b'turnOffDelay')

    def __init__(self):
        super(SixthSenseBattleBooster, self).__init__()
        self.turnOnDelay = component_constants.ZERO_FLOAT
        self.turnOffDelay = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(SixthSenseBattleBooster, self)._readConfig(xmlCtx, section)
        self.turnOnDelay = _xml.readNonNegativeFloat(xmlCtx, section, b'turnOnDelay')
        self.turnOffDelay = _xml.readNonNegativeFloat(xmlCtx, section, b'turnOffDelay')
        return

    def updateCrewSkill(self, a):
        if not a.isBoosterApplicable():
            return
        if a.level < MAX_SKILL_LEVEL or not a.isActive:
            a.level = MAX_SKILL_LEVEL
            a.isActive = True
        else:
            a.skillConfig = a.skillConfig.recreate(self.turnOnDelay, self.turnOffDelay)
        return


class PedantBattleBooster(SkillEquipment):
    __slots__ = (b'ammoBayHealthFactor',)

    def __init__(self):
        super(PedantBattleBooster, self).__init__()
        self.ammoBayHealthFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(PedantBattleBooster, self)._readConfig(xmlCtx, section)
        self.ammoBayHealthFactor = _xml.readPositiveFloat(xmlCtx, section, b'ammoBayHealthFactor')
        return

    def updateCrewSkill(self, a):
        if a.level < MAX_SKILL_LEVEL:
            level = MAX_SKILL_LEVEL
        else:
            a.skillConfig = a.skillConfig.recreate(self.ammoBayHealthFactor)
        return


class LastEffortBattleBooster(SkillEquipment):
    __slots__ = (b'durationPerLevel',)

    def __init__(self):
        super(LastEffortBattleBooster, self).__init__()
        self.durationPerLevel = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(LastEffortBattleBooster, self)._readConfig(xmlCtx, section)
        self.durationPerLevel = _xml.readNonNegativeFloat(xmlCtx, section, b'durationPerLevel')
        return

    def updateCrewSkill(self, a):
        if not a.isBoosterApplicable():
            return
        if a.level < MAX_SKILL_LEVEL or not a.isActive:
            a.level = MAX_SKILL_LEVEL
            a.isActive = True
        else:
            a.skillConfig = a.skillConfig.recreate(self.durationPerLevel)
        return


class _OptionalDeviceFilter(object):

    def __init__(self, xmlCtx, section):
        self.__requiredTags = set()
        self.__incompatibleTags = set()
        for subsection in section[b'tags'].values():
            if subsection.name == b'required':
                self.__requiredTags.update(_readTags((xmlCtx, subsection.name), subsection, b'', b'equipment'))
            elif subsection.name == b'incompatible':
                self.__incompatibleTags.update(_readTags((xmlCtx, subsection.name), subsection, b'', b'equipment'))
            else:
                _xml.raiseWrongXml(xmlCtx, subsection.name, b'should be <required> or/and <incompatible>')

        return

    def checkCompatibility(self, vehicleDescr):
        for device in vehicleDescr.optionalDevices:
            if device is None:
                continue
            tags = device.tags
            if self.__requiredTags.issubset(tags) and len(self.__incompatibleTags.intersection(tags)) == 0:
                return True

        return False

    def checkCompatibilityWithDevice(self, optionalDevice):
        tags = optionalDevice.tags
        if self.__requiredTags.issubset(tags) and len(self.__incompatibleTags.intersection(tags)) == 0:
            return True
        return False


class RageArtillery(Equipment, RageEquipmentConfigReader, ArtilleryConfigReader):
    __slots__ = RageEquipmentConfigReader._RAGE_EQUIPMENT_SLOTS + ArtilleryConfigReader._ARTILLERY_SLOTS

    def __init__(self):
        super(RageArtillery, self).__init__()
        self.initRageEquipmentSlots()
        self.initArtillerySlots()
        return

    def _readConfig(self, xmlCtx, section):
        self.readRageEquipmentConfig(xmlCtx, section)
        self.readArtilleryConfig(xmlCtx, section)
        return


class RageBomber(Equipment, RageEquipmentConfigReader, BomberConfigReader):
    __slots__ = RageEquipmentConfigReader._RAGE_EQUIPMENT_SLOTS + BomberConfigReader._BOMBER_SLOTS

    def __init__(self):
        super(RageBomber, self).__init__()
        self.initRageEquipmentSlots()
        self.initBomberSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readRageEquipmentConfig(xmlCtx, scriptSection)
        self.readBomberConfig(xmlCtx, scriptSection)
        return


class ConsumableArtillery(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArtilleryConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + ArtilleryConfigReader._ARTILLERY_SLOTS

    def __init__(self):
        super(ConsumableArtillery, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initArtillerySlots()
        return

    def _readConfig(self, xmlCtx, section):
        self.readTooltipInformation(xmlCtx, section)
        self.readSharedCooldownConsumableConfig(xmlCtx, section)
        self.readArtilleryConfig(xmlCtx, section)
        return


class ConsumableBomber(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, BomberConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + BomberConfigReader._BOMBER_SLOTS

    def __init__(self):
        super(ConsumableBomber, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initBomberSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.readBomberConfig(xmlCtx, scriptSection)
        return


class ConsumableRecon(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ReconConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + ReconConfigReader._RECON_SLOTS

    def __init__(self):
        super(ConsumableRecon, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initReconSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.readReconConfig(xmlCtx, scriptSection)
        return


class ConsumableSmoke(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, SmokeConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + SmokeConfigReader._SMOKE_SLOTS

    def __init__(self):
        super(ConsumableSmoke, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initSmokeSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.readSmokeConfig(xmlCtx, scriptSection)
        return


class ConsumableInspire(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, InspireConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + InspireConfigReader._INSPIRE_SLOTS

    def __init__(self):
        super(ConsumableInspire, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initInspireSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.readInspireConfig(xmlCtx, scriptSection)
        return


class PassiveConsumable(Equipment, TooltipConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS

    def __init__(self):
        super(PassiveConsumable, self).__init__()
        self.initTooltipInformation()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        return


class PassiveEngineering(Equipment, TooltipConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + (b'captureStopping', b'captureBlockBonusTime', b'captureSpeedFactor', b'resupplyCooldownFactor', b'resupplyShellsFactor')

    def __init__(self):
        super(PassiveEngineering, self).__init__()
        self.initTooltipInformation()
        self.captureStopping = False
        self.captureBlockBonusTime = component_constants.ZERO_FLOAT
        self.captureSpeedFactor = component_constants.ZERO_FLOAT
        self.resupplyCooldownFactor = component_constants.ZERO_FLOAT
        self.resupplyShellsFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.captureStopping = _xml.readBool(xmlCtx, scriptSection, b'captureStopping')
        self.captureBlockBonusTime = _xml.readPositiveFloat(xmlCtx, scriptSection, b'captureBlockBonusTime')
        self.captureSpeedFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'captureSpeedFactor')
        self.resupplyCooldownFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'resupplyCooldownFactor')
        self.resupplyShellsFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'resupplyShellsFactor')
        return


class EpicArtillery(ConsumableArtillery):
    pass


class EpicBomber(ConsumableBomber):
    pass


class EpicRecon(ConsumableRecon):
    pass


class EpicSmoke(ConsumableSmoke):
    pass


class EpicInspire(ConsumableInspire):
    __slots__ = (b'selfIncreaseFactors',)

    def __init__(self):
        super(EpicInspire, self).__init__()
        self.selfIncreaseFactors = {}
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(EpicInspire, self)._readConfig(xmlCtx, scriptSection)
        self.selfIncreaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'selfIncreaseFactors')
        return


class EpicEngineering(PassiveEngineering):
    pass


class FortConsumableInspire(ConsumableInspire):
    pass


class AreaOfEffectEquipment(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArcadeEquipmentConfigReader, EffectsConfigReader):
    __slots__ = (b'delay', b'duration', b'lifetime', b'shotsNumber', b'areaRadius', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'areaColorBlind', b'areaShow', b'noOwner', b'attackerType', b'areaVisibleToEnemies', b'shotSoundPreDelay', b'wwsoundShot', b'wwsoundEquipmentUsed', b'shotEffect', b'actionsConfig', b'explodeDestructible', b'areaUsedPrefab', b'areaAccurateCollision') + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + EffectsConfigReader._EFFECTS_SLOTS_

    def __init__(self):
        super(AreaOfEffectEquipment, self).__init__()
        self.initEffectsInformation()
        return

    def _readConfig(self, xmlCtx, section):
        super(AreaOfEffectEquipment, self)._readConfig(xmlCtx, section)
        self.readTooltipInformation(xmlCtx, section)
        self.readSharedCooldownConsumableConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.readEffectConfig(xmlCtx, section)
        self.delay = section.readFloat(b'delay')
        self.duration = section.readFloat(b'duration')
        self.lifetime = section.readFloat(b'lifetime')
        self.shotsNumber = section.readInt(b'shotsNumber')
        self.areaRadius = section.readFloat(b'areaRadius')
        self.areaLength = section.readFloat(b'areaLength', self.areaRadius * 2)
        self.areaWidth = section.readFloat(b'areaWidth', self.areaRadius * 2)
        self.areaVisual = section.readString(b'areaVisual') or None
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.areaColorBlind = _xml.readIntOrNone(xmlCtx, section, b'areaColorBlind')
        self.areaShow = section.readString(b'areaShow').lower() or None
        self.areaAccurateCollision = section.readBool(b'areaAccurateCollision', True)
        self.areaVisibleToEnemies = section.readBool(b'areaVisibleToEnemies', True)
        self.areaUsedPrefab = section.readString(b'areaUsedPrefab') or None
        self.noOwner = section.readBool(b'noOwner')
        self.attackerType = section.readString(b'attackerType').upper()
        self.shotSoundPreDelay = section.readInt(b'shotSoundPreDelay')
        self.wwsoundShot = section.readString(b'wwsoundShot')
        self.wwsoundEquipmentUsed = section.readString(b'wwsoundEquipmentUsed')
        self.shotEffect = section.readString(b'shotEffect')
        if IS_CELLAPP:
            self.actionsConfig = [self._readActionConfig(conf) for conf in section[b'actions'].values()]
            self.explodeDestructible = section.readBool(b'explodeDestructible')
        else:
            self.actionsConfig = None
            self.explodeDestructible = None
        return

    def _readActionConfig(self, section):
        if not section:
            return None
        else:
            actionType = section.readString(b'type')
            actionClass = getattr(vehicleActions, actionType)
            return {b'type': actionType, 
               b'applyTo': (section.readString(b'applyTo')), 
               b'args': (actionClass.parseXML(section[b'args']))}


class AttackBomberEquipment(AreaOfEffectEquipment):
    pass


class AttackArtilleryFortEquipment(AreaOfEffectEquipment):
    __slots__ = (b'maxDamage', b'enemyAreaColor', b'enemyAreaColorBlind')

    def _readConfig(self, xmlCtx, section):
        super(AttackArtilleryFortEquipment, self)._readConfig(xmlCtx, section)
        self.enemyAreaColor = _xml.readIntOrNone(xmlCtx, section, b'enemyAreaColor')
        self.enemyAreaColorBlind = _xml.readIntOrNone(xmlCtx, section, b'enemyAreaColorBlind')
        if IS_CLIENT:
            damagePerShot = sum([self.__readDamageVehicleAction(action) for action in section[b'actions'].values()])
            self.maxDamage = damagePerShot * self.shotsNumber
        else:
            self.maxDamage = 0
        return

    @staticmethod
    def __readDamageVehicleAction(section):
        if not section:
            return 0
        if section.readString(b'type') != b'DamageVehicle':
            return 0
        args = section[b'args']
        if args.has_key(b'damage'):
            return args.readInt(b'damage')
        return 0


UpgradeInfo = NamedTuple(b'UpgradeInfo', [(b'upgradedCompDescr', int)])
DowngradeInfo = NamedTuple(b'DowngradeInfo', [(b'downgradedCompDescr', int)])

class UpgradableItem(Artefact):

    def __init__(self, typeID, itemID, itemName, compactDescr):
        super(UpgradableItem, self).__init__(typeID, itemID, itemName, compactDescr)
        self.__upgradeInfo = None
        self._downgradeInfo = None
        self._level = 1
        return

    @property
    def upgradeInfo(self):
        return self.__upgradeInfo

    @property
    def downgradeInfo(self):
        return self._downgradeInfo

    @property
    def level(self):
        return self._level

    def _readConfig(self, xmlCtx, section):
        super(UpgradableItem, self)._readConfig(xmlCtx, section)
        self._readUpgradableConfig(xmlCtx, section)
        return

    def _readUpgradableConfig(self, xmlCtx, scriptSection):
        upgradeInfoSection = scriptSection[b'upgradeInfo']
        if upgradeInfoSection.has_key(b'upgradedDevice'):
            deviceName = _xml.readString(xmlCtx, upgradeInfoSection, b'upgradedDevice')

            def defferedInitUpgrade(objsByIDs, idsByNames):
                device = objsByIDs.get(idsByNames.get(deviceName))
                self._initUpgradeInfo(xmlCtx, upgradeInfoSection, device.compactDescr)
                self._initDowngradeInfo(device)
                device._level = self._level + 1
                return

            vehicles.addArtefactsPostloadCallback(defferedInitUpgrade)
        else:
            upgradedCD = _xml.readInt(xmlCtx, upgradeInfoSection, b'upgradedCompDescr')

            def defferedInitUpgrade(objsByIDs, idsByNames):
                _, __, itemID = items.parseIntCompactDescr(upgradedCD)
                device = objsByIDs.get(itemID)
                device._level = self._level + 1
                self._initDowngradeInfo(device)
                return

            vehicles.addArtefactsPostloadCallback(defferedInitUpgrade)
            self._initUpgradeInfo(xmlCtx, upgradeInfoSection, upgradedCD)
        return

    def _initUpgradeInfo(self, xmlCtx, upgradeInfoSection, upgradedCD):
        self.__upgradeInfo = UpgradeInfo(upgradedCD)
        _readPriceForOperation(xmlCtx, upgradeInfoSection, ITEM_OPERATION.UPGRADE, (self.compactDescr, upgradedCD))
        return

    def _initDowngradeInfo(self, device):
        downgradedCD = self.compactDescr
        device._downgradeInfo = DowngradeInfo(downgradedCD)
        return


class UpgradedItem(Artefact):

    def __init__(self, typeID, itemID, itemName, compactDescr):
        super(UpgradedItem, self).__init__(typeID, itemID, itemName, compactDescr)
        self._downgradeInfo = None
        self._level = 1
        return

    @property
    def downgradeInfo(self):
        return self._downgradeInfo

    @property
    def level(self):
        return self._level


class UpgradableStaticDevice(StaticOptionalDevice, UpgradableItem):
    pass


class UpgradedStaticDevice(StaticOptionalDevice, UpgradedItem):
    pass


class UpgradableImprovedConfiguration(ImprovedConfiguration, UpgradableItem):
    pass


class UpgradableExtraHealthReserve(ExtraHealthReserve, UpgradableItem):
    pass


class UpgradedImprovedConfiguration(ImprovedConfiguration, UpgradedItem):
    pass


class UpgradedExtraHealthReserve(ExtraHealthReserve, UpgradedItem):
    pass


class UpgradableRotationMechanisms(RotationMechanisms, UpgradableItem):
    pass


class UpgradedRotationMechanisms(RotationMechanisms, UpgradedItem):
    pass


class UpgradableLowNoiseTracks(LowNoiseTracks, UpgradableItem):
    pass


class UpgradedLowNoiseTracks(LowNoiseTracks, UpgradedItem):
    pass


class Bomber(Equipment, TooltipConfigReader, CountableConsumableConfigReader, BomberConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CountableConsumableConfigReader._CONSUMABLE_SLOTS + CooldownConsumableConfigReader._CONSUMABLE_SLOTS + BomberConfigReader._BOMBER_SLOTS + (b'influenceZone', b'cooldownTime')

    def __init__(self):
        super(Bomber, self).__init__()
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.initBomberSlots()
        self.cooldownTime = component_constants.ZERO_INT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readBomberConfig(xmlCtx, scriptSection)
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds')
        if scriptSection.has_key(b'influenceZone'):
            self.influenceZone = InfluenceZone()
            self.influenceZone._readConfig(xmlCtx, scriptSection[b'influenceZone'])
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription)
        return


class BomberArcade(Bomber, ArcadeEquipmentConfigReader):
    __slots__ = Bomber.__slots__ + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS

    def __init__(self):
        super(BomberArcade, self).__init__()
        self.initArcadeInformation()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(BomberArcade, self)._readConfig(xmlCtx, scriptSection)
        self.readArcadeInformation(xmlCtx, scriptSection)
        return


class Smoke(Equipment, TooltipConfigReader, CountableConsumableConfigReader, SmokeConfigReader):
    __slots__ = (b'cooldownTime',) + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CountableConsumableConfigReader._CONSUMABLE_SLOTS + SmokeConfigReader._SMOKE_SLOTS

    def __init__(self):
        super(Smoke, self).__init__()
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.initSmokeSlots()
        self.cooldownTime = component_constants.ZERO_INT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readSmokeConfig(xmlCtx, scriptSection)
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds')
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription, duration=int(self.totalDuration))
        return


class SmokeArcade(Smoke, ArcadeEquipmentConfigReader):
    __slots__ = Smoke.__slots__ + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS

    def __init__(self):
        super(SmokeArcade, self).__init__()
        self.orthogonalDir = True
        self.initArcadeInformation()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(SmokeArcade, self)._readConfig(xmlCtx, scriptSection)
        self.readArcadeInformation(xmlCtx, scriptSection)
        return


class SelfBuff(Equipment, TooltipConfigReader, CountableConsumableConfigReader):
    __slots__ = (b'duration', b'increaseFactors', b'longDescription', b'cooldownTime') + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS

    def __init__(self):
        super(SelfBuff, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.increaseFactors = {}
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.cooldownTime = _xml.readFloat(xmlCtx, scriptSection, b'cooldownTime', 0.0)
        self.duration = _xml.readInt(xmlCtx, scriptSection, b'duration', 0)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, scriptSection, b'increaseFactors')
        self.readTooltipInformation(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription, duration=int(self.duration))
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        return

    def _getDescription(self, descr):
        return i18n.makeString(self.longDescription, duration=int(self.duration))


class Berserker(SelfBuff):
    __slots__ = (b'dotParams',)

    def __init__(self):
        super(Berserker, self).__init__()
        self.dotParams = DOTParams(ATTACK_REASON_INDICES[ATTACK_REASON.BERSERKER])
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(Berserker, self)._readConfig(xmlCtx, scriptSection)
        self.dotParams._readConfig(xmlCtx, scriptSection[b'dotParams'])
        return


class DOTParams(object):
    __slots__ = (b'damagePerTick', b'restoreHealth', b'tickInterval', b'canDie', b'groupID', b'attackReasonID')

    def __init__(self, attackReasonID=ATTACK_REASON_INDICES[ATTACK_REASON.NONE]):
        self.damagePerTick = 0.0
        self.tickInterval = 1.0
        self.restoreHealth = True
        self.canDie = False
        self.groupID = 0
        self.attackReasonID = attackReasonID
        return

    def __repr__(self):
        return (b'dotParams (Damage:{}, Tick:{}, RestoreHealth:{}, CanKill:{}, groupId:{}, attackReasonId:{})').format(self.damagePerTick, self.tickInterval, self.restoreHealth, self.canDie, self.groupID, self.attackReasonID)

    def _readConfig(self, xmlCtx, scriptSection):
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, scriptSection, b'tickInterval', 1.0)
        self.damagePerTick = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'damagePerTick', 0.0)
        self.restoreHealth = _xml.readBool(xmlCtx, scriptSection, b'restoreHealth', True)
        self.canDie = _xml.readBool(xmlCtx, scriptSection, b'canDie', True)
        self.groupID = scriptSection.readInt(b'groupID')
        return


class HOTParams(object):
    __slots__ = (b'healPerTick', b'healCrew', b'healDevices', b'healGroup', b'tickInterval')

    def __init__(self):
        self.healPerTick = 0.0
        self.healCrew = False
        self.healDevices = False
        self.healGroup = None
        self.tickInterval = 1.0
        return

    def __repr__(self):
        return (b'hotParams ({},{},{},{})').format(self.healPerTick, self.healCrew, self.healDevices, self.tickInterval)

    def _readConfig(self, xmlCtx, scriptSection):
        self.healPerTick = _xml.readPositiveFloat(xmlCtx, scriptSection, b'healPerTick', 0.0)
        self.healCrew = _xml.readBool(xmlCtx, scriptSection, b'healCrew', False)
        self.healDevices = _xml.readBool(xmlCtx, scriptSection, b'healDevices', False)
        self.healGroup = _xml.readIntOrNone(xmlCtx, scriptSection, b'healGroup')
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, scriptSection, b'tickInterval', 1.0)
        return


class _ClientSpawnBotVisuals(object):
    __slots__ = (b'markerPositionOffset', b'markerScale', b'deliveringAnimationDuration', b'deliveringAnimationStartDelay', b'highlightDelay')

    def __init__(self, xmlCtx, scriptSection):
        self.markerPositionOffset = _xml.readVector3(xmlCtx, scriptSection, b'markerPositionOffset', Vector3(0, 0, 0))
        self.markerScale = _xml.readVector3(xmlCtx, scriptSection, b'markerScale', Vector3(1, 1, 1))
        self.deliveringAnimationDuration = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'deliveringAnimationDuration', 0.0)
        self.deliveringAnimationStartDelay = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'deliveringAnimationStartDelay', 0.0)
        self.highlightDelay = _xml.readFloat(xmlCtx, scriptSection, b'highlightDelay', 0.0)
        return


class BRHealPoint(Equipment, TooltipConfigReader, CountableConsumableConfigReader, HealPointConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CountableConsumableConfigReader._CONSUMABLE_SLOTS + HealPointConfigReader._HEAL_POINT_SLOTS + (b'cooldownTime',)

    def __init__(self):
        super(BRHealPoint, self).__init__()
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.initHealPointSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'cooldownTime')
        self.readHealPointConfig(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription, duration=int(self.duration), count=int(self.healPerTick * 100 / self.tickInterval))
        return


class RegenerationKit(Equipment, CountableConsumableConfigReader):
    __slots__ = (b'healthRegenPerTick', b'initialHeal', b'healTime', b'healGroup', b'tickInterval')

    def __init__(self):
        super(RegenerationKit, self).__init__()
        self.healthRegenPerTick = component_constants.ZERO_FLOAT
        self.initialHeal = component_constants.ZERO_FLOAT
        self.healTime = component_constants.ZERO_FLOAT
        self.healGroup = None
        self.tickInterval = 1.0
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, section):
        self.healthRegenPerTick = _xml.readNonNegativeFloat(xmlCtx, section, b'healthRegenPerTick', 0.0)
        self.initialHeal = _xml.readNonNegativeFloat(xmlCtx, section, b'initialHeal', 0.0)
        self.healTime = _xml.readNonNegativeFloat(xmlCtx, section, b'healTime', 0.0)
        self.healGroup = _xml.readIntOrNone(xmlCtx, section, b'healGroup')
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, section, b'tickInterval', 1.0)
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def _getDescription(self, descr):
        localizeDescr = super(RegenerationKit, self)._getDescription(descr)
        return i18n.makeString(localizeDescr, count=int(self.healthRegenPerTick * 100 / self.tickInterval), duration=int(self.healTime))


class FLRegenerationKit(Equipment, SharedCooldownConsumableConfigReader, TooltipConfigReader):
    __slots__ = SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + (b'expireByDamageReceived', b'resupplyHealthPointsFactor')

    def __init__(self):
        super(FLRegenerationKit, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.healthRegenPerTick = component_constants.ZERO_FLOAT
        self.initialHeal = component_constants.ZERO_FLOAT
        self.healTime = component_constants.ZERO_FLOAT
        self.healGroup = None
        self.tickInterval = 1.0
        self.expireByDamageReceived = False
        self.resupplyHealthPointsFactor = 1.0
        return

    def _readConfig(self, xmlCtx, section):
        self.readTooltipInformation(xmlCtx, section)
        self.readSharedCooldownConsumableConfig(xmlCtx, section)
        self.healthRegenPerTick = _xml.readNonNegativeFloat(xmlCtx, section, b'healthRegenPerTick', 0.0)
        self.initialHeal = _xml.readNonNegativeFloat(xmlCtx, section, b'initialHeal', 0.0)
        self.healTime = _xml.readNonNegativeFloat(xmlCtx, section, b'healTime', 0.0)
        self.healGroup = _xml.readIntOrNone(xmlCtx, section, b'healGroup')
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, section, b'tickInterval', 1.0)
        self.expireByDamageReceived = _xml.readBool(xmlCtx, section, b'expireByDamageReceived', False)
        self.resupplyHealthPointsFactor = _xml.readPositiveFloat(xmlCtx, section, b'resupplyHealthPointsFactor', 1.0)
        return


class FLAvatarStealthRadar(Equipment, SharedCooldownConsumableConfigReader, CooldownConsumableConfigReader, TooltipConfigReader, InspireConfigReader):
    __slots__ = SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CooldownConsumableConfigReader._CONSUMABLE_SLOTS + InspireConfigReader._INSPIRE_SLOTS + (b'passiveCircularVisionRadius', b'detectionTime', b'overridableFactors')

    def __init__(self):
        super(FLAvatarStealthRadar, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initConsumableWithDeployTimeSlots()
        self.initInspireSlots()
        self.passiveCircularVisionRadius = component_constants.ZERO_FLOAT
        self.detectionTime = component_constants.ZERO_FLOAT
        self.overridableFactors = {}
        return

    def _readConfig(self, xmlCtx, section):
        self.readTooltipInformation(xmlCtx, section)
        self.readSharedCooldownConsumableConfig(xmlCtx, section)
        self.readConsumableWithTimeConfig(xmlCtx, section)
        self.readInspireConfig(xmlCtx, section)
        self.passiveCircularVisionRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'passiveCircularVisionRadius', 0.0)
        self.detectionTime = _xml.readNonNegativeFloat(xmlCtx, section, b'minesDetectionTime', 0.0)
        self.readOverFactorsFromConfig(xmlCtx, section)
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription, activationDelay=int(self.inactivationDelay))
        return

    def readOverFactorsFromConfig(self, xmlCtx, section):
        factorsSection = section[b'overridableFactors']
        if factorsSection is None:
            return
        else:
            for name, subsection in factorsSection.items():
                factor = subsection.asFloat
                self.overridableFactors[name] = factor

            return


class MineParams(object):
    __slots__ = (b'triggerRadius', b'triggerHeight', b'triggerDepth', b'influenceType', b'lifetime', b'activationDelay', b'damage', b'shell', b'shellLowDamage', b'destroyMyMinesOverlappingAlliedMines', b'resistAllyDamage', b'directDetectionTypes')

    def __init__(self):
        self.triggerRadius = 1.0
        self.triggerHeight = 1.0
        self.triggerDepth = 0.0
        self.influenceType = component_constants.INFLUENCE_ALL
        self.lifetime = 10
        self.damage = 100
        self.shell = None
        self.shellLowDamage = None
        self.resistAllyDamage = False
        self.destroyMyMinesOverlappingAlliedMines = False
        self.directDetectionTypes = []
        return

    def __repr__(self):
        return (b'motParams ({}, {}, {}, {}, {}, {}, {}, {})').format(self.triggerRadius, self.triggerHeight, self.triggerDepth, self.influenceType, self.lifetime, self.damage, self.shell, self.shellLowDamage)

    def _readConfig(self, xmlCtx, section):
        self.activationDelay = section.readInt(b'activationDelay', 0)
        self.triggerRadius = _xml.readPositiveFloat(xmlCtx, section, b'triggerRadius')
        self.triggerHeight = _xml.readPositiveFloat(xmlCtx, section, b'triggerHeight')
        self.triggerDepth = _xml.readNonNegativeFloat(xmlCtx, section, b'triggerDepth', 0.0)
        self.influenceType = _xml.readInt(xmlCtx, section, b'influenceType', component_constants.INFLUENCE_ALL, component_constants.INFLUENCE_ENEMY)
        self.lifetime = _xml.readPositiveInt(xmlCtx, section, b'lifetime')
        self.damage = _xml.readNonNegativeInt(xmlCtx, section, b'damage')
        if section.has_key(b'shellCompactDescr'):
            self.shell = _xml.readInt(xmlCtx, section, b'shellCompactDescr')
        if section.has_key(b'shellCompactDescrLowDamage'):
            self.shellLowDamage = _xml.readInt(xmlCtx, section, b'shellCompactDescrLowDamage')
        if section.has_key(b'resistAllyDamage'):
            self.resistAllyDamage = _xml.readBool(xmlCtx, section, b'resistAllyDamage')
        if section.has_key(b'destroyMyMinesOverlappingAlliedMines'):
            self.resistAllyDamage = _xml.readBool(xmlCtx, section, b'destroyMyMinesOverlappingAlliedMines')
        if section.has_key(b'directDetectionTypes'):
            mapping = {b'RAYTRACE': 0, b'RECON': 1, b'RADAR': 2, b'STEALTH_RADAR': 3}
            DDTypes = _xml.readTupleOfStrings(xmlCtx, section, b'directDetectionTypes')
            self.directDetectionTypes = [mapping[t] for t in DDTypes]
        return


class Minefield(Equipment, TooltipConfigReader, ArcadeEquipmentConfigReader, CountableConsumableConfigReader):
    __slots__ = (b'mineParams', b'noOwner', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'cooldownTime', b'disableAllyDamage') + CountableConsumableConfigReader._CONSUMABLE_SLOTS + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS

    def __init__(self):
        super(Minefield, self).__init__()
        self.initTooltipInformation()
        self.initArcadeInformation()
        self.bombsPattern = []
        self.mineParams = MineParams()
        self.noOwner = False
        self.disableAllyDamage = True
        self.cooldownTime = component_constants.ZERO_INT
        self.areaLength = 0
        self.areaWidth = 0
        self.areaVisual = None
        self.areaColor = None
        self.areaMarker = None
        return

    def _readConfig(self, xmlCtx, section):
        bombs = _xml.readTupleOfFloats(xmlCtx, section, b'bombsPattern')
        self.bombsPattern = [(bombs[b], bombs[b + 1]) for b in range(0, len(bombs) - 1, 2)]
        self.mineParams._readConfig(xmlCtx, section[b'mineParams'])
        self.cooldownTime = _xml.readInt(xmlCtx, section, b'cooldownSeconds')
        self.disableAllyDamage = _xml.readBool(xmlCtx, section, b'disableAllyDamage')
        self.areaLength = _xml.readPositiveFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, section, b'areaWidth')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.readCountableConsumableConfig(xmlCtx, section)
        self.readTooltipInformation(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription, duration=int(self.mineParams.lifetime))
        return


class _CommonMinefieldEquipment(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArcadeEquipmentConfigReader, CooldownConsumableConfigReader):
    __slots__ = (b'bombsPattern', b'mineParams', b'noOwner', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'areaMarker', b'bombsNumber')

    def __init__(self):
        super(_CommonMinefieldEquipment, self).__init__()
        self.initTooltipInformation()
        self.initSharedCooldownConsumableSlots()
        self.initArcadeInformation()
        self.bombsPattern = []
        self.mineParams = MineParams()
        self.noOwner = False
        self.areaLength = 0
        self.areaWidth = 0
        self.areaVisual = None
        self.areaColor = None
        self.areaMarker = None
        self.bombsNumber = 0
        return

    def _readConfig(self, xmlCtx, section):
        bombs = _xml.readTupleOfFloats(xmlCtx, section, b'bombsPattern')
        self.bombsPattern = [(bombs[b], bombs[b + 1]) for b in range(0, len(bombs) - 1, 2)]
        self.mineParams._readConfig(xmlCtx, section[b'mineParams'])
        self.noOwner = _xml.readBool(xmlCtx, section, b'noOwner')
        self.areaLength = _xml.readPositiveFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, section, b'areaWidth')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.areaColor = _xml.readIntOrNone(xmlCtx, section, b'areaColor')
        self.areaMarker = _xml.readStringOrNone(xmlCtx, section, b'areaMarker')
        self.bombsNumber = _xml.readIntOrNone(xmlCtx, section, b'bombsNumber')
        self.readConsumableWithTimeConfig(xmlCtx, section)
        self.readTooltipInformation(xmlCtx, section)
        self.readSharedCooldownConsumableConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        return


class FrontLineMinefield(_CommonMinefieldEquipment):
    pass


class ConsumableSpawnBot(Equipment, TooltipConfigReader, CountableConsumableConfigReader, AreaMarkerConfigReader, ArcadeEquipmentConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + CountableConsumableConfigReader._CONSUMABLE_SLOTS + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + AreaMarkerConfigReader._MARKER_SLOTS_ + (b'botType', b'botVehCompDescr', b'botLifeTime', b'botSpawnPointOffset', b'botXRayFactor', b'clientVisuals', b'explosionRadius', b'explosionDamage', b'explosionByShoot', b'damageReductionRate', b'delay', b'cooldownTime', b'disableAllyDamage')

    def __init__(self):
        super(ConsumableSpawnBot, self).__init__()
        self.initTooltipInformation()
        self.initCountableConsumableSlots()
        self.initArcadeInformation()
        self.initMarkerInformation()
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
        self.vehicleRemoveDelay = _xml.readInt(xmlCtx, scriptSection, b'vehicleRemoveDelay', 0.0)
        self.clientRemovalNotificationDelay = _xml.readInt(xmlCtx, scriptSection, b'clientRemovalNotificationDelay', 0.0)
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds')
        self.disableAllyDamage = _xml.readBool(xmlCtx, scriptSection, b'disableAllyDamage', True)
        if IS_CLIENT:
            if scriptSection[b'clientVisuals'] is not None:
                self.clientVisuals = _ClientSpawnBotVisuals(scriptSection, scriptSection[b'clientVisuals'])
            self.longDescription = i18n.makeString(self.longDescription, duration=int(self.botLifeTime))
        return


class VisualScriptEquipment(Equipment):
    __slots__ = (b'visualScript',)

    def __init__(self):
        super(VisualScriptEquipment, self).__init__()
        self.visualScript = {}
        return

    def _readConfig(self, xmlCtx, section):
        self.visualScript = readVisualScriptSection(section)
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(VisualScriptEquipment, self)._readBasicConfig(xmlCtx, section)
        self._checkIconExist()
        return

    def _exportSlotsToVSE(self):
        params = self._getExportParamsDict(ExportParamsTag.VSE)
        if not params:
            return
        for _, plans in self.visualScript.iteritems():
            for planDef in plans:
                planDef[b'params'].update(params)

        self._exportParams[ExportParamsTag.VSE.value].clear()
        return

    def _checkIconExist(self):
        if not IS_CLIENT:
            return
        if self.hasTag(b'visualScriptAbilityEquipment') or self.hasTag(b'abilityEquipment'):
            resId = R.images.gui.maps.icons.artefact.dyn(self.iconName)
            if not resId.exists():
                self.iconName = b'not_found_artefact'
                self.icon = (self.iconName, self.icon[1], self.icon[2])
        return


class LevelBasedVisualScriptEquipment(VisualScriptEquipment):
    _LEVEL_BASED_SLOTS = (b'radius',)

    def __init__(self):
        super(LevelBasedVisualScriptEquipment, self).__init__()
        self.radius = ()
        return

    def _readConfig(self, xmlCtx, section):
        super(LevelBasedVisualScriptEquipment, self)._readConfig(xmlCtx, section)
        self.radius = tuple(map(float, section.readString(b'radius').split()))
        if len(self.radius) == 0:
            _xml.raiseWrongXml(xmlCtx, b'radius', b'should be multiple values separated by space.')
        return

    def getRadiusBasedOnSkillLevel(self, skillLevel):
        return self.radius[skillLevel - 1]


class SureShotEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'stabMovement', b'stabTurns', b'stabTurret', b'stabShot', b'reloadBonus', b'finalDispersion')

    def _readConfig(self, xmlCtx, section):
        super(SureShotEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.finalDispersion = section.readFloat(b'finalDispersion')
        self.stabMovement = section.readFloat(b'stabMovement')
        self.stabTurns = section.readFloat(b'stabTurns')
        self.stabTurret = section.readFloat(b'stabTurret')
        self.stabShot = section.readFloat(b'stabShot')
        self.reloadBonus = section.readFloat(b'reloadBonus')
        self._exportSlotsToVSE()
        return


class JuggernautEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'enginePowerFactor', b'stunDurationFactor', b'repairBuff', b'gunReloadBoostSeconds', b'shotsLimitForGunBoost', b'minTimeBetweenReloadBoost')

    def _readConfig(self, xmlCtx, section):
        super(JuggernautEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.enginePowerFactor = section.readFloat(b'enginePowerFactor')
        self.stunDurationFactor = section.readFloat(b'stunDurationFactor')
        self.repairBuff = section.readFloat(b'repairBuff')
        self.gunReloadBoostSeconds = section.readFloat(b'gunReloadBoostSeconds')
        self.shotsLimitForGunBoost = section.readInt(b'shotsLimitForGunBoost')
        self.minTimeBetweenReloadBoost = section.readFloat(b'minTimeBetweenReloadBoost')
        self._exportSlotsToVSE()
        return


class ConcentrationEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'stabMovement', b'stabTurns', b'stabTurret', b'stabShot', b'addSecToTimeBtmClips', b'reloadFactor')

    def _readConfig(self, xmlCtx, section):
        super(ConcentrationEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.stabMovement = section.readFloat(b'stabMovement')
        self.stabTurns = section.readFloat(b'stabTurns')
        self.stabTurret = section.readFloat(b'stabTurret')
        self.stabShot = section.readFloat(b'stabShot')
        self.addSecToTimeBtmClips = section.readFloat(b'addSecToTimeBtmClips')
        self.reloadFactor = section.readFloat(b'reloadFactor')
        self._exportSlotsToVSE()
        return


class Comp7AoeHealEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'radius', b'heal', b'secondaryHealDebuff', b'tickInterval')

    @property
    def tooltipParams(self):
        params = super(Comp7AoeHealEquipment, self).tooltipParams
        params[b'heal'] = tuple(map((lambda h: int(h * self.tickInterval * self.duration)), self.heal))
        if self.secondaryHealDebuff:
            debuf = 1.0 - self.secondaryHealDebuff / 100.0
            params[b'debuf'] = tuple(map((lambda h: int(int(h * debuf) * self.tickInterval * self.duration)), self.heal))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7AoeHealEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.radius = section.readFloat(b'radius')
        self.heal = tuple(map(float, section.readString(b'heal').split()))
        self.secondaryHealDebuff = section.readFloat(b'secondaryHealDebuff')
        self.tickInterval = section.readFloat(b'tickInterval')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7AllySupportEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'crewBuff')

    def _readConfig(self, xmlCtx, section):
        super(Comp7AllySupportEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.crewBuff = tuple(map(float, section.readString(b'crewBuff').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7AllyHunterEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'heal', b'gunReloadTimeBuff', b'tickInterval')

    @property
    def tooltipParams(self):
        params = super(Comp7AllyHunterEquipment, self).tooltipParams
        params[b'heal'] = tuple(map((lambda h: h * self.tickInterval * self.duration), self.heal))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7AllyHunterEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.heal = tuple(map(float, section.readString(b'heal').split()))
        self.gunReloadTimeBuff = section.readFloat(b'gunReloadTimeBuff')
        self.tickInterval = section.readFloat(b'tickInterval')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7ConcentrationEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'aimingTimeBuff', b'shotDispersionFactors', b'clipReloadTimeBoost')

    @property
    def tooltipParams(self):
        params = super(Comp7ConcentrationEquipment, self).tooltipParams
        params[b'shotDispersionFactorsBuff'] = tuple(map((lambda b: (1.0 - b) * 100), self.shotDispersionFactors))
        params[b'aimingTimeBuff'] = tuple(map((lambda b: (1.0 - b) * 100), self.aimingTimeBuff))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7ConcentrationEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.aimingTimeBuff = tuple(map(float, section.readString(b'aimingTimeBuff').split()))
        self.shotDispersionFactors = tuple(map(float, section.readString(b'shotDispersionFactors').split()))
        self.clipReloadTimeBoost = tuple(map(float, section.readString(b'clipReloadTimeBoost').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7BerserkEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'gunReloadTimeBuff', b'damageDistance', b'shotDispersionFactors')

    @property
    def tooltipParams(self):
        params = super(Comp7BerserkEquipment, self).tooltipParams
        params[b'gunReloadTimeBuff'] = tuple(map((lambda b: (1.0 - b) * 100), self.gunReloadTimeBuff))
        params[b'shotDispersionFactorsBuff'] = tuple(map((lambda b: (1.0 - b) * 100), self.shotDispersionFactors))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7BerserkEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.gunReloadTimeBuff = tuple(map(float, section.readString(b'gunReloadTimeBuff').split()))
        self.damageDistance = section.readFloat(b'damageDistance')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.shotDispersionFactors = tuple(map(float, section.readString(b'shotDispersionFactors').split()))
        self._exportSlotsToVSE()
        return


class Comp7AoeInspireEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'radius', b'crewBuff')

    def _readConfig(self, xmlCtx, section):
        super(Comp7AoeInspireEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.crewBuff = tuple(map(float, section.readString(b'crewBuff').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7RedlineEquipment(LevelBasedVisualScriptEquipment, BaseMarkerConfigReader, EffectsConfigReader):
    __slots__ = LevelBasedVisualScriptEquipment._LEVEL_BASED_SLOTS + BaseMarkerConfigReader._MARKER_SLOTS_ + EffectsConfigReader._EFFECTS_SLOTS_ + (b'delay', b'damage', b'stunDuration', b'areaShow', b'fraction', b'requireAssists')

    def __init__(self):
        super(Comp7RedlineEquipment, self).__init__()
        self.initMarkerInformation()
        self.initEffectsInformation()
        return

    def _readConfig(self, xmlCtx, section):
        super(Comp7RedlineEquipment, self)._readConfig(xmlCtx, section)
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


class Comp7FastRechargeEquipment(VisualScriptEquipment):
    __slots__ = (b'gunReloadTimeBuff',)

    @property
    def tooltipParams(self):
        params = super(Comp7FastRechargeEquipment, self).tooltipParams
        params[b'gunReloadTimeBuff'] = tuple(map((lambda b: (1.0 - b) * 100), self.gunReloadTimeBuff))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7FastRechargeEquipment, self)._readConfig(xmlCtx, section)
        self.gunReloadTimeBuff = tuple(map(float, section.readString(b'gunReloadTimeBuff').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7JuggernautEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'enginePowerFactor', b'stunDurationFactor', b'repairBuff', b'gunReloadBoost')

    @property
    def tooltipParams(self):
        params = super(Comp7JuggernautEquipment, self).tooltipParams
        params[b'enginePowerBuff'] = (self.enginePowerFactor - 1.0) * 100
        params[b'stunDurationResist'] = self.stunDurationFactor * 100
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7JuggernautEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.enginePowerFactor = section.readFloat(b'enginePowerFactor')
        self.stunDurationFactor = section.readFloat(b'stunDurationFactor')
        self.repairBuff = section.readFloat(b'repairBuff')
        self.gunReloadBoost = section.readFloat(b'gunReloadBoost')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7SureShotEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'shotDispersionFactors', b'slvl', b'sdlvl')

    @property
    def tooltipParams(self):
        params = super(Comp7SureShotEquipment, self).tooltipParams
        params[b'shotDispersionFactorsBuff'] = tuple(map((lambda b: (1.0 - b) * 100), self.shotDispersionFactors))
        params[b'gunReloadBuff'] = tuple(map((lambda b: b * 100), self.slvl))
        params[b'killGunReloadBuff'] = tuple(map((lambda b: b * 100), self.sdlvl))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7SureShotEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.shotDispersionFactors = tuple(map(float, section.readString(b'shotDispersionFactors').split()))
        self.slvl = tuple(map(float, section.readString(b'slvl').split()))
        self.sdlvl = tuple(map(float, section.readString(b'sdlvl').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7SniperEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'dispersionFactor', b'damageDistance', b'damageFactors')

    @property
    def tooltipParams(self):
        params = super(Comp7SniperEquipment, self).tooltipParams
        params[b'damageFactors'] = tuple(map((lambda f: int(round((f - 1) * 100))), self.damageFactors))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7SniperEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.dispersionFactor = section.readFloat(b'dispersionFactor')
        self.damageDistance = section.readFloat(b'damageDistance')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self.damageFactors = tuple(map(float, section.readString(b'damageFactors').split()))
        self._exportSlotsToVSE()
        return


class Comp7RiskyAttackEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'healDuration', b'baseHeal', b'extraHealFactor', b'fwdSpeedBoost', b'bkwSpeedBoost', b'enginePowerBuff')

    @property
    def tooltipParams(self):
        params = super(Comp7RiskyAttackEquipment, self).tooltipParams
        params[b'extraHealFactor'] = tuple(map((lambda b: b * 100), self.extraHealFactor))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7RiskyAttackEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.healDuration = section.readFloat(b'healDuration')
        self.baseHeal = section.readInt(b'baseHeal')
        self.extraHealFactor = tuple(map(float, section.readString(b'extraHealFactor').split()))
        self.fwdSpeedBoost = section.readFloat(b'fwdSpeedBoost')
        self.bkwSpeedBoost = section.readFloat(b'bkwSpeedBoost')
        self.enginePowerBuff = section.readFloat(b'enginePowerBuff')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7ReconEquipment(LevelBasedVisualScriptEquipment, BaseMarkerConfigReader):
    __slots__ = LevelBasedVisualScriptEquipment._LEVEL_BASED_SLOTS + BaseMarkerConfigReader._MARKER_SLOTS_ + (b'duration', b'delay')

    def __init__(self):
        super(Comp7ReconEquipment, self).__init__()
        self.initMarkerInformation()
        return

    def _readConfig(self, xmlCtx, section):
        super(Comp7ReconEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.delay = section.readFloat(b'delay')
        self.readMarkerConfig(xmlCtx, section)
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7AggressiveDetectionEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'visionFactor')

    @property
    def tooltipParams(self):
        params = super(Comp7AggressiveDetectionEquipment, self).tooltipParams
        params[b'visionBuff'] = tuple(map((lambda b: (b - 1.0) * 100), self.visionFactor))
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7AggressiveDetectionEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.visionFactor = tuple(map(float, section.readString(b'visionFactor').split()))
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class Comp7MarchEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'enginePowerBuff', b'fwdSpeedBoost', b'invisibilityFactor')

    @property
    def tooltipParams(self):
        params = super(Comp7MarchEquipment, self).tooltipParams
        params[b'enginePowerBuff'] = (self.enginePowerBuff - 1.0) * 100
        params[b'invisibilityFactor'] = (self.invisibilityFactor - 1.0) * 100
        return params

    def _readConfig(self, xmlCtx, section):
        super(Comp7MarchEquipment, self)._readConfig(xmlCtx, section)
        self.duration = tuple(map(float, section.readString(b'duration').split()))
        self.enginePowerBuff = section.readFloat(b'enginePowerBuff')
        self.fwdSpeedBoost = section.readFloat(b'fwdSpeedBoost')
        self.invisibilityFactor = section.readFloat(b'invisibilityFactor')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class PoiRadarEquipment(VisualScriptEquipment):
    __slots__ = (b'duration',)

    def _readConfig(self, xmlCtx, section):
        super(PoiRadarEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self._exportSlotsToVSE()
        return


class PoiArtilleryEquipment(AreaOfEffectEquipment):
    __slots__ = (b'maxCount', b'requireAssists')

    def _readConfig(self, xmlCtx, section):
        super(PoiArtilleryEquipment, self)._readConfig(xmlCtx, section)
        maxCount = section.readInt(b'maxCount')
        if maxCount < 1:
            maxCount = 1
        self.maxCount = maxCount
        self.requireAssists = section.readBool(b'requireAssists', False)
        return


class PoiSmokeEquipment(ConsumableSmoke):
    __slots__ = (b'areaRadius',)

    def _readConfig(self, xmlCtx, section):
        super(PoiSmokeEquipment, self)._readConfig(xmlCtx, section)
        self.areaRadius = section.readFloat(b'areaRadius')
        return

    @property
    def tooltipParams(self):
        params = super(PoiSmokeEquipment, self).tooltipParams
        params[b'duration'] = self.totalDuration
        params[b'size'] = self.areaRadius * 2
        params[b'vision'] = abs(self.attrFactorMods.get(b'circularVisionRadius', (0, 0, False))[0]) * 100
        params[b'efficiency'] = abs(self.attrFactorMods.get(b'crewRolesFactor', (0, 0, False))[0]) * 100
        params[b'delay'] = self.minDelay
        return params


class PoiMineFieldEquipment(_CommonMinefieldEquipment):

    @property
    def tooltipParams(self):
        params = super(PoiMineFieldEquipment, self).tooltipParams
        params[b'duration'] = self.mineParams.lifetime
        params[b'width'] = self.areaWidth
        params[b'length'] = self.areaLength
        params[b'count'] = self.bombsNumber
        params[b'delay'] = self.mineParams.activationDelay
        return params


_readTags = vehicles._readTags

def _readStun(xmlCtx, scriptSection):
    stunResistanceEffect = _xml.readFraction(xmlCtx, scriptSection, b'stunResistanceEffect') if scriptSection.has_key(b'stunResistanceEffect') else 0.0
    stunResistanceDuration = _xml.readFraction(xmlCtx, scriptSection, b'stunResistanceDuration') if scriptSection.has_key(b'stunResistanceDuration') else 0.0
    repeatedStunDurationFactor = _xml.readFraction(xmlCtx, scriptSection, b'repeatedStunDurationFactor') if scriptSection.has_key(b'repeatedStunDurationFactor') else 1.0
    return (stunResistanceEffect, stunResistanceDuration, repeatedStunDurationFactor)


def _readReuseParams(xmlCtx, scriptSection):
    return (
     _xml.readInt(xmlCtx, scriptSection, b'reuseCount', minVal=-1) if scriptSection.has_key(b'reuseCount') else 0,
     _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds', minVal=0) if scriptSection.has_key(b'cooldownSeconds') else 0)


class OPT_DEV_TYPE_TAG(object):
    TROPHY_BASIC = b'trophyBasic'
    TROPHY_UPGRADED = b'trophyUpgraded'
    DELUXE = b'deluxe'
    MODERNIZED1 = b'modernized_1'
    MODERNIZED2 = b'modernized_2'
    MODERNIZED3 = b'modernized_3'
    ALL = {
     TROPHY_BASIC, TROPHY_UPGRADED, DELUXE, MODERNIZED1, MODERNIZED2, 
     MODERNIZED3}

    @staticmethod
    def checkTags(tags):
        intersectionTags = tags & OPT_DEV_TYPE_TAG.ALL
        return len(intersectionTags) < 2


class AoeEffects(object):
    START = b'start'
    ACTION = b'action'


class AreaShow(object):
    BEFORE = b'before'
    ALWAYS = b'always'


class Circle(object):
    __slots__ = (b'abilityRadius', b'safeZoneRadius')

    def __init__(self):
        self.abilityRadius = 0.0
        self.safeZoneRadius = 0.0
        return

    def readConfig(self, xmlCtx, section):
        self.abilityRadius = _xml.readFloat(xmlCtx, section, b'abilityRadius', 0.0)
        self.safeZoneRadius = _xml.readFloat(xmlCtx, section, b'safeZoneRadius', 0.0)
        return


class ZonesCircle(Equipment):
    __slots__ = (b'influenceZone', b'radius', b'zonesCount', b'vehicleHeightMultiplier')

    def __init__(self):
        super(ZonesCircle, self).__init__()
        self.radius = component_constants.ZERO_FLOAT
        self.zonesCount = component_constants.ZERO_FLOAT
        self.vehicleHeightMultiplier = 1.0
        self.influenceZone = InfluenceZone()
        return

    def _readConfig(self, xmlCtx, section):
        super(ZonesCircle, self)._readConfig(xmlCtx, section)
        self.radius = _xml.readFloat(xmlCtx, section, b'radius')
        self.zonesCount = _xml.readPositiveInt(xmlCtx, section, b'zonesCount')
        self.vehicleHeightMultiplier = _xml.readNonNegativeFloat(xmlCtx, section, b'vehicleHeightMultiplier')
        self.influenceZone._readConfig(xmlCtx, section[b'influenceZone'])
        return

    def _getDescription(self, descr):
        localizeDescr = super(ZonesCircle, self)._getDescription(descr)
        return i18n.makeString(localizeDescr, duration=int(self.influenceZone.timer))


class FireCircle(ZonesCircle, CountableConsumableConfigReader):

    def __init__(self):
        super(FireCircle, self).__init__()
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, section):
        super(FireCircle, self)._readConfig(xmlCtx, section)
        self.influenceZone.dotParams.attackReasonID = ATTACK_REASON_INDICES[ATTACK_REASON.FIRE_CIRCLE]
        self.influenceZone.componentName = b'VehicleFireCircleEffectComponent'
        self.readCountableConsumableConfig(xmlCtx, section)
        return


class CorrodingShot(Equipment, CountableConsumableConfigReader):
    __slots__ = (b'damagePercentAfterShot', b'canBeStoppedRepairKit', b'increaseFactors', b'dotEffectDuration', b'dotParams', b'tooltipMovie', b'effectsIndex')

    def __init__(self):
        super(CorrodingShot, self).__init__()
        self.damagePercentAfterShot = component_constants.ZERO_FLOAT
        self.canBeStoppedRepairKit = component_constants.ZERO_INT
        self.increaseFactors = {}
        self.dotEffectDuration = component_constants.ZERO_INT
        self.dotParams = DOTParams(ATTACK_REASON_INDICES[ATTACK_REASON.CORRODING_SHOT])
        self.dotEffectDuration = component_constants.ZERO_INT
        self.tooltipMovie = component_constants.EMPTY_STRING
        self.initCountableConsumableSlots()
        return

    def _readConfig(self, xmlCtx, section):
        self.damagePercentAfterShot = _xml.readFloat(xmlCtx, section, b'damagePercentAfterShot', 0.0)
        self.canBeStoppedRepairKit = _xml.readBool(xmlCtx, section, b'canBeStoppedRepairKit', False)
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'increaseFactors')
        self.dotEffectDuration = _xml.readInt(xmlCtx, section, b'dotEffectDuration', 0)
        self.dotParams._readConfig(xmlCtx, section[b'dotParams'])
        self.tooltipMovie = _xml.readStringOrEmpty(xmlCtx, section, b'tooltipMovie')
        self.effectsIndex = vehicles.g_cache.shotEffectsIndexes[_xml.readString(xmlCtx, section, b'shotEffect')]
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def _getDescription(self, descr):
        localizeDescr = super(CorrodingShot, self)._getDescription(descr)
        return i18n.makeString(localizeDescr, duration=self.dotEffectDuration)


class AdaptationHealthRestore(Equipment, CountableConsumableConfigReader):
    __slots__ = (b'duration', b'areaVisual', b'immediatelyRestore', b'posteffectPrefab', b'restoringCoefficient', b'restoringCoefficientTeamMates', b'teamMateRestoringRadius')

    def __init__(self):
        super(AdaptationHealthRestore, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.restoringCoefficient = component_constants.ZERO_FLOAT
        self.restoringCoefficientTeamMates = component_constants.ZERO_FLOAT
        self.teamMateRestoringRadius = component_constants.ZERO_INT
        self.areaVisual = None
        self.posteffectPrefab = None
        self.initCountableConsumableSlots()
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(AdaptationHealthRestore, self)._readBasicConfig(xmlCtx, section)
        self.posteffectPrefab = _xml.readStringOrNone(xmlCtx, section, b'posteffectPrefab')
        return

    def _readConfig(self, xmlCtx, section):
        self.duration = _xml.readInt(xmlCtx, section, b'duration', 0)
        self.immediatelyRestore = _xml.readInt(xmlCtx, section, b'immediatelyRestore', 0.0)
        self.restoringCoefficient = _xml.readFloat(xmlCtx, section, b'restoringCoefficient', 0.0)
        self.restoringCoefficientTeamMates = _xml.readFloat(xmlCtx, section, b'restoringCoefficientTeamMates', 0.0)
        self.teamMateRestoringRadius = _xml.readInt(xmlCtx, section, b'teamMateRestoringRadius', 0)
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def _getDescription(self, descr):
        localizeDescr = super(AdaptationHealthRestore, self)._getDescription(descr)
        return i18n.makeString(localizeDescr, ownPercent=int(self.restoringCoefficient * 100), teamMatesPercent=int(self.restoringCoefficientTeamMates * 100))


class ThunderStrike(Equipment, ArcadeEquipmentConfigReader, TooltipConfigReader, CountableConsumableConfigReader):
    __slots__ = ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + (b'noOwner', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'delay', b'duration', b'damage', b'thunderCount', b'thunderPeriod', b'deployTime', b'cooldownTime', b'decreaseFactors', b'isDamageAll', b'canBeStoppedRepairKit')

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
        return

    def _readConfig(self, xmlCtx, section):
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownSeconds')
        self.canBeStoppedRepairKit = _xml.readBool(xmlCtx, section, b'canBeStoppedRepairKit', False)
        self.damageRadius = _xml.readInt(xmlCtx, section, b'damageRadius', 0)
        self.duration = _xml.readInt(xmlCtx, section, b'duration', 0)
        self.delay = _xml.readPositiveFloat(xmlCtx, section, b'delay', 0)
        self.damage = _xml.readInt(xmlCtx, section, b'damage', 0)
        self.thunderCount = _xml.readInt(xmlCtx, section, b'thunderCount', 0)
        self.thunderPeriod = _xml.readPositiveFloat(xmlCtx, section, b'thunderPeriod', 0)
        self.areaLength = _xml.readPositiveFloat(xmlCtx, section, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, section, b'areaWidth')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, section, b'areaVisual')
        self.isDamageAll = _xml.readBool(xmlCtx, section, b'isDamageAll', False)
        self.decreaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'decreaseFactors')
        self.readArcadeInformation(xmlCtx, section)
        self.readTooltipInformation(xmlCtx, section)
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def readTooltipInformation(self, xmlCtx, section):
        super(ThunderStrike, self).readTooltipInformation(xmlCtx, section)
        if IS_CLIENT:
            self.longDescription = i18n.makeString(self.longDescription, duration=self.duration)
        return


class ShotPassion(Equipment, CountableConsumableConfigReader):
    __slots__ = (b'duration', b'increaseFactors', b'enableRamDamage', b'enableHEDamage', b'damageIncreasePerShot', b'maxDamageIncreasePerShot', b'affectingAbilities', b'cooldownTime', b'enableThunderStrikeDamageIncrease', b'posteffectPrefab')

    def __init__(self):
        super(ShotPassion, self).__init__()
        self.duration = component_constants.ZERO_INT
        self.damageIncreasePerShot = component_constants.ZERO_FLOAT
        self.maxDamageIncreasePerShot = component_constants.ZERO_FLOAT
        self.cooldownTime = component_constants.ZERO_INT
        self.initCountableConsumableSlots()
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(ShotPassion, self)._readBasicConfig(xmlCtx, section)
        self.posteffectPrefab = _xml.readStringOrNone(xmlCtx, section, b'posteffectPrefab')
        return

    def _readConfig(self, xmlCtx, section):
        self.duration = _xml.readPositiveFloat(xmlCtx, section, b'duration')
        self.increaseFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'increaseFactors')
        self.damageIncreasePerShot = _xml.readNonNegativeFloat(xmlCtx, section, b'damageIncreasePerShot')
        self.maxDamageIncreasePerShot = _xml.readNonNegativeFloat(xmlCtx, section, b'maxDamageIncreasePerShot')
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownSeconds')
        self.readCountableConsumableConfig(xmlCtx, section)
        return

    def _getDescription(self, descr):
        localizeDescr = super(ShotPassion, self)._getDescription(descr)
        percentSymbol = text(R.strings.common.common.percent())
        return i18n.makeString(localizeDescr, duration=getNiceNumberFormat(self.duration), dmgPerShot=getNiceNumberFormat(self.damageIncreasePerShot * 100) + percentSymbol, maxDmgPerShot=getNiceNumberFormat(self.maxDamageIncreasePerShot * 100) + percentSymbol)


class BaseAbilityEquipment(VisualScriptEquipment):
    __slots__ = (b'duration', b'factors')

    def __init__(self):
        super(BaseAbilityEquipment, self).__init__()
        self.duration = component_constants.ZERO_FLOAT
        self.factors = []
        return

    def _readConfig(self, xmlCtx, section):
        super(BaseAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        addFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'additiveFactors')
        mulFactors = VehicleFactorsXmlReader.readFactors(xmlCtx, section, b'multiplicativeFactors')
        for name, value in addFactors.items():
            self.factors.append(VehicleAttribute(name, AttrsOperation.ADD, value))

        for name, value in mulFactors.items():
            self.factors.append(VehicleAttribute(name, AttrsOperation.MUL, value))

        self._exportSlotsToVSE()
        return


class CoolantTankAbilityEquipment(BaseAbilityEquipment):
    __slots__ = (b'penaltyReloadTime',)

    def __init__(self):
        super(CoolantTankAbilityEquipment, self).__init__()
        self.penaltyReloadTime = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(CoolantTankAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.penaltyReloadTime = _xml.readPositiveFloat(xmlCtx, section, b'penaltyReloadTime')
        return


class TankRamAbilityEquipment(BaseAbilityEquipment):
    __slots__ = (b'cooldownAfterRamKill',)

    def __init__(self):
        super(TankRamAbilityEquipment, self).__init__()
        self.cooldownAfterRamKill = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(TankRamAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.cooldownAfterRamKill = _xml.readPositiveFloat(xmlCtx, section, b'cooldownAfterRamKill')
        return


class DamageModifierAbilityEquipment(BaseAbilityEquipment):
    __slots__ = (b'damageIncreasePerShot', b'maxDamageIncreasePerShot', b'damageFirstIncrease', b'addDuration')

    def __init__(self):
        super(DamageModifierAbilityEquipment, self).__init__()
        self.damageIncreasePerShot = component_constants.ZERO_FLOAT
        self.maxDamageIncreasePerShot = component_constants.ZERO_FLOAT
        self.damageFirstIncrease = component_constants.ZERO_FLOAT
        self.addDuration = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, section):
        super(DamageModifierAbilityEquipment, self)._readConfig(xmlCtx, section)
        self.damageIncreasePerShot = _xml.readPositiveFloat(xmlCtx, section, b'damageIncreasePerShot', component_constants.ZERO_FLOAT)
        self.maxDamageIncreasePerShot = _xml.readPositiveFloat(xmlCtx, section, b'maxDamageIncreasePerShot', component_constants.ZERO_FLOAT)
        self.damageFirstIncrease = _xml.readPositiveFloat(xmlCtx, section, b'damageFirstIncrease', component_constants.ZERO_FLOAT)
        self.addDuration = _xml.readPositiveFloat(xmlCtx, section, b'addDuration', component_constants.ZERO_FLOAT)
        return
