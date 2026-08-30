from __future__ import absolute_import, division
import os
from re import findall
from enum import Enum, unique
from future.utils import listvalues, viewitems, viewvalues
from typing import NamedTuple, Set, Dict, Optional, Any, Tuple, List
from Math import Vector3
from ResMgr import DataSection
import items, nations
from ArenaType import readVisualScriptSection
from constants import IS_CLIENT, IS_CELLAPP, IS_WEB, VEHICLE_TTC_ASPECTS, ATTACK_REASON, ATTACK_REASON_INDICES, SERVER_TICK_LENGTH, SkillProcessorArgs, GroupSkillProcessorArgs, TTC_TOOLTIP_SECTIONS
from debug_utils import LOG_DEBUG_DEV
from extension_utils import importClass
from items import ITEM_OPERATION, PREDEFINED_HEAL_GROUPS
from items import _xml, vehicles
from items.artefacts_helpers import VehicleFilter, _ArtefactFilter, readKpi
from items.basic_item import BasicItem
from items.components import shared_components, component_constants
from items.components.supply_slot_categories import SupplySlotFilter, LevelsFactor, AttrsOperation, SlotCategories
from items.vehicles import VehicleDescriptor, _readPriceForOperation
from items.tankmen import MAX_SKILL_LEVEL
from soft_exception import SoftException
if IS_CLIENT:
    from helpers import i18n
elif IS_WEB:
    from web_stubs import i18n
else:

    class i18n(object):

        @classmethod
        def makeString(cls, key):
            raise SoftException(b'Unexpected call "i18n.makeString"')
            return


@unique
class ExportParamsTag(Enum):
    VSE = b'vse'
    TOOLTIP = b'tooltip'


@unique
class OrderTypes(str, Enum):
    RANDOM = b'random'
    SEQUENTIALLY = b'sequentially'

    @classmethod
    def values(cls):
        return [obj.value for obj in cls.__members__.values()]


class CommonXmlSectionReader(object):

    def __init__(self, xmlTagKeyMap, dictInstance):
        self.__xmlTagKeyMap = xmlTagKeyMap
        self.__readersMap = self.__createReaders(dictInstance)
        return

    def read(self, xmlCtx, section, subsection_name):
        result = {}
        subsection = _xml.getSubsection(xmlCtx, section, subsection_name)
        for key, tag_name in viewitems(self.__xmlTagKeyMap):
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
        for name, value in viewitems(dictInstance):
            factor_type = type(value)
            reader_type = b'TupleOfFloats' if factor_type is list else findall(b"'(\\w+)'", str(factor_type))[0].capitalize()
            readers[name] = getattr(_xml, b'read' + reader_type)

        return readers


class VehicleFactorsXmlReader(CommonXmlSectionReader):
    __readerImpl = None

    def __init__(self):
        attrFactor = vehicles.defaultVehicleAttributeFactors()
        _vehicle_attribute_factor_tags = {name: name.replace(b'/', b'-') for name in attrFactor}
        super(VehicleFactorsXmlReader, self).__init__(_vehicle_attribute_factor_tags, attrFactor)
        return

    @staticmethod
    def readFactors(xmlCtx, section, subsection_name):
        if VehicleFactorsXmlReader.__readerImpl is None:
            VehicleFactorsXmlReader.__readerImpl = VehicleFactorsXmlReader()
        return VehicleFactorsXmlReader.__readerImpl.read(xmlCtx, section, subsection_name)


class Artefact(BasicItem):
    __slots__ = (b'icon', b'removable', b'price', b'showInShop', b'_vehWeightFraction', b'_weight', b'_exportParams', b'__archetype', b'__vehicleFilter', b'__artefactFilter', b'__tooltipSection', b'isImproved', b'kpi', b'iconName', b'_groupName', b'__weakref__')

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

    def weightOnVehicle(self, vehicleDescr):
        return (
         self._vehWeightFraction, self._weight)

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
        self.id = (nations.NONE_INDEX, _xml.readInt(xmlCtx, section, b'id', 0, 65535))
        self.compactDescr = vehicles.makeIntCompactDescrByID(self.itemTypeName, *self.id)
        if not section.has_key(b'tags'):
            self.tags = frozenset()
        else:
            self.tags = _readTags(xmlCtx, section, b'tags', self.itemTypeName)
        if IS_CLIENT or IS_WEB:
            self.i18n = shared_components.I18nComponent(userStringKey=section.readString(b'userString'), descriptionKey=section.readString(b'description'), shortDescriptionSpecialKey=section.readString(b'shortDescriptionSpecial'), longDescriptionSpecialKey=section.readString(b'longDescriptionSpecial'), shortFilterAlertKey=section.readString(b'shortFilterAlert'), longFilterAlertKey=section.readString(b'longFilterAlert'))
            self.icon = _xml.readIconWithDefaultParams(xmlCtx, section, b'icon')
            self.iconName = os.path.splitext(os.path.basename(self.icon[0]))[0]
        if (IS_CLIENT or IS_WEB) and section.has_key(b'kpi'):
            self.kpi = readKpi(xmlCtx, section[b'kpi'])
        else:
            self.kpi = []
        if IS_CLIENT:
            if section.has_key(b'tooltipSection'):
                self.__tooltipSection = section.readString(b'tooltipSection', TTC_TOOLTIP_SECTIONS.EQUIPMENT)
            else:
                self.__tooltipSection = TTC_TOOLTIP_SECTIONS.EQUIPMENT
            if section.has_key(b'archetype'):
                self.__archetype = section.readString(b'archetype')
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
            self._groupName = section.readString(b'groupName')
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
    def isUpgradable(self):
        return self._isUpgradable

    @property
    def isUpgraded(self):
        return self._isUpgraded

    @property
    def isRegular(self):
        return not (self.isDeluxe or self.isTrophy or self.isModernized)

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
            for name in factorsSection.keys():
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
            for subsection in factorsSection.values():
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
            for splitted, factor in viewitems(self._factors):
                modulePath = splitted[:-1]
                shortName = splitted[-1]
                attrDict = self.defineAttrsDict(vehicleDescr, modulePath)
                factor.applyLevelToAttrsDict(level, attrDict, shortName)

            return

    def getFactorValue(self, vehicleDescr, attrPath, default=0.0):
        splitted = tuple(attrPath.split(b'/'))
        factor = self._factors.get(splitted, None)
        if not factor:
            return default
        else:
            level = self.defineActiveLevel(vehicleDescr)
            return factor.getActiveValue(level)

    def factorsContainCrewLevelIncrease(self):
        return any(b'crewLevelIncrease' in splitted for splitted in self._factors)


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
    __slots__ = (b'equipmentType', b'reuseCount', b'cooldownSeconds', b'soundNotification', b'stunResistanceEffect', b'stunResistanceDuration', b'repeatedStunDurationFactor', b'clientSelector', b'ownerPrefab', b'usagePrefab', b'usagePrefabEnemy', b'playerMessagesKey', b'messagePostfix')

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
        self.messagePostfix = None
        self.usagePrefab = None
        self.usagePrefabEnemy = None
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(Equipment, self)._readBasicConfig(xmlCtx, section)
        self.equipmentType = items.EQUIPMENT_TYPES[section.readString(b'type', b'regular')]
        self.soundNotification = _xml.readStringOrNone(xmlCtx, section, b'soundNotification')
        self.playerMessagesKey = _xml.readStringOrNone(xmlCtx, section, b'playerMessagesKey')
        scriptSection = section[b'script']
        self.stunResistanceEffect, self.stunResistanceDuration, self.repeatedStunDurationFactor = _readStun(xmlCtx, scriptSection)
        self.reuseCount, self.cooldownSeconds = _readReuseParams(xmlCtx, scriptSection)
        self.clientSelector = _xml.readStringOrNone(xmlCtx, scriptSection, b'clientSelector')
        self.ownerPrefab = _xml.readStringOrNone(xmlCtx, section, b'ownerPrefab')
        self.usagePrefab = _xml.readStringOrNone(xmlCtx, section, b'usagePrefab')
        self.usagePrefabEnemy = _xml.readStringOrNone(xmlCtx, section, b'usagePrefabEnemy') if section.has_key(b'usagePrefabEnemy') else None
        self.messagePostfix = (section.readString(b'messagePostfix') or self.name.split(b'_')[0]).upper()
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

    def doesDependOnOptionalDevice(self):
        return False


class EpicEmptySlot(Equipment):
    pass


class ExtraHealthReserve(StaticOptionalDevice):

    def updateVehicleDescrAttrs(self, vehicleDescr):
        super(ExtraHealthReserve, self).updateVehicleDescrAttrs(vehicleDescr)
        vehicleDescr.miscAttrs[b'isSetChassisMaxHealthAfterHysteresis'] = True
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
            rff = vehicleDescr.physics[b'rollingFrictionFactors']
            vehicleDescr.physics[b'rollingFrictionFactors'] = list(rffi * rollingFrictionFactorActiveValue for rffi in rff)
            return

    def _readConfig(self, xmlCtx, scriptSection):
        super(Grousers, self)._readConfig(xmlCtx, scriptSection)
        self.rotationFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'rotationFactor')
        self.rollingFrictionFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'rollingFrictionFactor')
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

    def _readConfig(self, xmlCtx, scriptSection):
        super(RotationMechanisms, self)._readConfig(xmlCtx, scriptSection)
        self.trackMoveSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'trackMoveSpeedFactor')
        self.wheelMoveSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'wheelMoveSpeedFactor')
        self.trackRotateSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'trackRotateSpeedFactor')
        self.wheelRotateSpeedFactor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'wheelRotateSpeedFactor')
        self.wheelCenterRotationFwdSpeed = LevelsFactor.readTypelessLevelsFactor(xmlCtx, scriptSection, b'wheelCenterRotationFwdSpeed')
        return


class Extinguisher(Equipment):
    __slots__ = (b'fireStartingChanceFactor', b'autoactivate')

    def __init__(self):
        super(Extinguisher, self).__init__()
        self.fireStartingChanceFactor = component_constants.ZERO_FLOAT
        self.autoactivate = False
        return

    def _readConfig(self, xmlCtx, scriptSection):
        if not scriptSection.has_key(b'fireStartingChanceFactor'):
            self.fireStartingChanceFactor = 1.0
        else:
            self.fireStartingChanceFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'fireStartingChanceFactor')
        self.autoactivate = scriptSection.readBool(b'autoactivate', False)
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'enginePowerFactor')
        self.turretRotationSpeedFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'turretRotationSpeedFactor')
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.crewLevelIncrease = _xml.readFloat(xmlCtx, scriptSection, b'crewLevelIncrease', component_constants.ZERO_FLOAT)
        return


class Repairkit(Equipment):
    __slots__ = (b'bonusValue',)

    def __init__(self):
        super(Repairkit, self).__init__()
        self.bonusValue = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.bonusValue = _xml.readFraction(xmlCtx, scriptSection, b'bonusValue')
        return


class CountableConsumableConfigReader(object):
    _CONSUMABLE_SLOTS = (b'consumeAmmo',)

    def initCountableConsumableSlots(self):
        self.consumeAmmo = False
        return

    def readCountableConsumableConfig(self, xmlCtx, section):
        self.consumeAmmo = _xml.readBool(xmlCtx, section, b'consumeAmmo')
        return


class RemovedRpmLimiter(Equipment):
    __slots__ = (b'enginePowerFactor', b'engineHpLossPerSecond')

    def __init__(self):
        super(RemovedRpmLimiter, self).__init__()
        self.enginePowerFactor = component_constants.ZERO_FLOAT
        self.engineHpLossPerSecond = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'enginePowerFactor')
        self.engineHpLossPerSecond = _xml.readPositiveFloat(xmlCtx, scriptSection, b'engineHpLossPerSecond')
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.deploySeconds = _xml.readInt(xmlCtx, scriptSection, b'deploySeconds', 0)
        self.consumeSeconds = _xml.readInt(xmlCtx, scriptSection, b'consumeSeconds', 0)
        self.rechargeSeconds = _xml.readInt(xmlCtx, scriptSection, b'rechargeSeconds', 0)
        self.enginePowerFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'enginePowerFactor')
        self.maxSpeedFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'maxSpeedFactor')
        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        try:
            factors[b'engine/power'] *= self.enginePowerFactor
            factors[b'vehicle/maxSpeed'] *= self.maxSpeedFactor
        except:
            pass

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
    _SHARED_COOLDOWN_CONSUMABLE_SLOTS = (b'prepareTime', b'cooldownTime', b'cooldownFactors', b'sharedCooldownTime', b'consumeAmmo', b'disableAllyDamage', b'setUnavailableAfterAmmoLeft')

    def initSharedCooldownConsumableSlots(self):
        self.cooldownTime = component_constants.ZERO_FLOAT
        self.cooldownFactors = component_constants.EMPTY_DICT
        self.prepareTime = None
        self.consumeAmmo = False
        self.disableAllyDamage = False
        self.setUnavailableAfterAmmoLeft = False
        return

    def readSharedCooldownConsumableConfig(self, xmlCtx, section):
        self.cooldownTime = _xml.readNonNegativeFloat(xmlCtx, section, b'cooldownTime')
        self.cooldownFactors = self._readCooldownFactors(xmlCtx, section, b'cooldownFactors')
        if section.has_key(b'prepareTime'):
            self.prepareTime = _xml.readNonNegativeFloat(xmlCtx, section, b'prepareTime')
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
            sOrderTypeName = section.readString(b'sequencesOrderType', OrderTypes.RANDOM.value)
            if sOrderTypeName not in OrderTypes.values():
                raise SoftException((b'Wrong sequencesOrderType. <{}> not in {}.').format(sOrderTypeName, OrderTypes.values()))
            effect = {b'shotEffects': (section.readString(b'shotEffects').split()), 
               b'sequences': (self._readSequencesConfig(section[b'sequences'])), 
               b'sequencesOrderType': (OrderTypes(sOrderTypeName)), 
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
        self.areaRadius = self.entitiesToSearch.get(b'Vehicle', {}).get(b'radius') or listvalues(self.entitiesToSearch)[0][b'radius']
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


class Marker(object):
    __slots__ = (b'name', b'textColor', b'_sectionName')

    def __init__(self, sectionName):
        self._sectionName = sectionName
        self.name = None
        self.textColor = None
        return

    def readConfig(self, xmlCtx, section):
        if not self._sectionName or not section.has_key(self._sectionName):
            return
        markerSection = section[self._sectionName]
        self.name = _xml.readStringOrNone(xmlCtx, markerSection, b'name')
        self.textColor = _xml.readStringOrNone(xmlCtx, markerSection, b'textColor')
        self._validate()
        return

    def _validate(self):
        if IS_CLIENT:
            from gui.Scaleform.daapi.view.battle.shared.minimap.settings import EQ_MARKER_TO_SYMBOL
            from gui.Scaleform.genConsts.BATTLE_MARKERS_CONSTS import BATTLE_MARKERS_CONSTS
            if self.name is not None and EQ_MARKER_TO_SYMBOL.get(self.name) is None:
                raise SoftException((b'Unknown minimap symbol for marker: {}. Supported: {}.').format(self.name, list(EQ_MARKER_TO_SYMBOL)))
            if self.textColor is not None and self.textColor not in BATTLE_MARKERS_CONSTS.COLORS:
                raise SoftException((b'Unknown text colors for marker: {}. Supported: {}.').format(self.name, BATTLE_MARKERS_CONSTS.COLORS))
        return


class Markers(object):
    __slots__ = (b'ally', b'enemy', b'_sectionName')

    def __init__(self, sectionName):
        self._sectionName = sectionName
        self.ally = None
        self.enemy = None
        return

    def readConfig(self, xmlCtx, section):
        if not self._sectionName or not section.has_key(self._sectionName):
            return
        markersSection = section[self._sectionName]
        self.ally = Marker(b'ally')
        self.enemy = Marker(b'enemy')
        self.ally.readConfig(xmlCtx, markersSection)
        self.enemy.readConfig(xmlCtx, markersSection)
        return


class MarkersConfigReader(object):
    _MARKERS_CONFIG_SLOTS = (b'markers',)

    def initMarkers(self):
        self.markers = None
        return

    def readMarkersConfig(self, xmlCtx, section):
        self.markers = Markers(b'markers')
        self.markers.readConfig(xmlCtx, section)
        return


class ArcadeEquipmentConfigReader(object):
    _SHARED_ARCADE_SLOTS = (b'minApplyRadius', b'maxApplyRadius', b'applyRadiusVisible', b'cameraPivotPosMin', b'cameraPivotPosMax', b'arenaAimLimits')

    def initArcadeInformation(self):
        self.minApplyRadius = component_constants.ZERO_FLOAT
        self.maxApplyRadius = component_constants.ZERO_FLOAT
        self.applyRadiusVisible = False
        self.cameraPivotPosMin = Vector3()
        self.cameraPivotPosMax = Vector3()
        self.arenaAimLimits = None
        return

    def readArcadeInformation(self, xmlCtx, section):
        self.minApplyRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'minApplyRadius', component_constants.ZERO_FLOAT)
        self.maxApplyRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'maxApplyRadius', component_constants.ZERO_FLOAT)
        self.applyRadiusVisible = _xml.readBool(xmlCtx, section, b'applyRadiusVisible', False)
        if (self.minApplyRadius or self.maxApplyRadius) and self.minApplyRadius >= self.maxApplyRadius:
            raise SoftException((b'Aiming radius limits: min[{}] >= max[{}]').format(self.minApplyRadius, self.maxApplyRadius))
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

    def _readConfig(self, xmlCtx, scriptSection):
        self._config = []
        for subsection in scriptSection.values():
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

    def configContainCrewLevelIncrease(self):
        return any(levelParams is not None and b'crewLevelIncrease' in levelParams for _, levelParams in self._config)

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
        raise NotImplementedError
        return

    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        raise NotImplementedError
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

    def _readConfig(self, xmlCtx, scriptSection):
        super(SkillEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.skillName = _xml.readNonEmptyString(xmlCtx, scriptSection, b'skillName')
        self.perkLevelMultiplier = _xml.readFloatOrNone(xmlCtx, scriptSection, b'perkLevelMultiplier')
        return

    def updateCrewSkill(self, *args):
        return


class FactorSkillBattleBooster(SkillEquipment):
    __slots__ = (b'efficiencyFactor',)

    def __init__(self):
        super(FactorSkillBattleBooster, self).__init__()
        self.efficiencyFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(FactorSkillBattleBooster, self)._readConfig(xmlCtx, scriptSection)
        self.efficiencyFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'efficiencyFactor')
        return

    def updateCrewSkill(self, a):
        efficiency = (a.factor - 0.57) / 0.43
        if a.baseAvgLevel < 100 or a.skillEfficiency < 1.0:
            efficiency = 1.0 + efficiency - float(a.baseAvgLevel) / 100
            a.factor = 0.57 + 0.43 * efficiency
            a.baseAvgLevel = efficiency * 100
        else:
            a.factor = 0.57 + 0.43 * efficiency * self.efficiencyFactor
        return


class SixthSenseBattleBooster(SkillEquipment):
    __slots__ = (b'delay',)

    def __init__(self):
        super(SixthSenseBattleBooster, self).__init__()
        self.delay = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(SixthSenseBattleBooster, self)._readConfig(xmlCtx, scriptSection)
        self.delay = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'delay')
        return

    def updateCrewSkill(self, a):
        if not a.isBoosterApplicable():
            return
        if a.level < MAX_SKILL_LEVEL or not a.isActive:
            a.level = MAX_SKILL_LEVEL
            a.isActive = True
        else:
            a.skillConfig = a.skillConfig.recreate(self.delay)
        return


class PedantBattleBooster(SkillEquipment):
    __slots__ = (b'ammoBayHealthFactor',)

    def __init__(self):
        super(PedantBattleBooster, self).__init__()
        self.ammoBayHealthFactor = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(PedantBattleBooster, self)._readConfig(xmlCtx, scriptSection)
        self.ammoBayHealthFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'ammoBayHealthFactor')
        return

    def updateCrewSkill(self, a):
        if a.level < MAX_SKILL_LEVEL:
            _ = MAX_SKILL_LEVEL
        else:
            a.skillConfig = a.skillConfig.recreate(self.ammoBayHealthFactor)
        return


class LastEffortBattleBooster(SkillEquipment):
    __slots__ = (b'durationPerLevel', b'chanceToHitPerLevel')

    def __init__(self):
        super(LastEffortBattleBooster, self).__init__()
        self.durationPerLevel = component_constants.ZERO_FLOAT
        self.chanceToHitPerLevel = component_constants.ZERO_FLOAT
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(LastEffortBattleBooster, self)._readConfig(xmlCtx, scriptSection)
        self.durationPerLevel = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'durationPerLevel')
        self.chanceToHitPerLevel = _xml.readFloat(xmlCtx, scriptSection, b'chanceToHitPerLevel')
        return

    def updateCrewSkill(self, a):
        if not a.isBoosterApplicable():
            return
        if a.level < MAX_SKILL_LEVEL or not a.isActive:
            a.level = MAX_SKILL_LEVEL
            a.isActive = True
        else:
            a.skillConfig = a.skillConfig.recreate(self.durationPerLevel, self.chanceToHitPerLevel)
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.readRageEquipmentConfig(xmlCtx, scriptSection)
        self.readArtilleryConfig(xmlCtx, scriptSection)
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.readArtilleryConfig(xmlCtx, scriptSection)
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


class FLPassiveEngineering(PassiveEngineering):
    pass


class FortConsumableInspire(ConsumableInspire):
    pass


class AreaOfEffectEquipment(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArcadeEquipmentConfigReader, EffectsConfigReader, MarkersConfigReader):
    __slots__ = (b'delay', b'duration', b'lifetime', b'shotsNumber', b'areaRadius', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'areaColorBlind', b'areaShow', b'noOwner', b'attackerType', b'areaVisibleToEnemies', b'shotSoundPreDelay', b'wwsoundShot', b'wwsoundEquipmentUsed', b'shotEffect', b'actionsConfig', b'explodeDestructible', b'areaUsedPrefab', b'areaAccurateCollision') + TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS + SharedCooldownConsumableConfigReader._SHARED_COOLDOWN_CONSUMABLE_SLOTS + ArcadeEquipmentConfigReader._SHARED_ARCADE_SLOTS + EffectsConfigReader._EFFECTS_SLOTS_ + MarkersConfigReader._MARKERS_CONFIG_SLOTS

    def __init__(self):
        super(AreaOfEffectEquipment, self).__init__()
        self.initEffectsInformation()
        self.initSharedCooldownConsumableSlots()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(AreaOfEffectEquipment, self)._readConfig(xmlCtx, scriptSection)
        section = scriptSection
        self.readTooltipInformation(xmlCtx, section)
        self.readSharedCooldownConsumableConfig(xmlCtx, section)
        self.readArcadeInformation(xmlCtx, section)
        self.readEffectConfig(xmlCtx, section)
        self.readMarkersConfig(xmlCtx, section)
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
            actionClass = importClass(actionType, b'actions.vehicle')
            return {b'type': actionType, 
               b'applyTo': (section.readString(b'applyTo', b'')), 
               b'applyToShotIDs': (tuple(map(int, section.readString(b'applyToShotIDs').split()))), 
               b'args': (actionClass.parseXML(section[b'args']))}


class AttackBomberEquipment(AreaOfEffectEquipment):
    pass


class AttackArtilleryFortEquipment(AreaOfEffectEquipment):
    __slots__ = (b'maxDamage', b'enemyAreaColor', b'enemyAreaColorBlind')

    def _readConfig(self, xmlCtx, scriptSection):
        super(AttackArtilleryFortEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.enemyAreaColor = _xml.readIntOrNone(xmlCtx, scriptSection, b'enemyAreaColor')
        self.enemyAreaColorBlind = _xml.readIntOrNone(xmlCtx, scriptSection, b'enemyAreaColorBlind')
        if IS_CLIENT:
            damagePerShot = sum(self.__readDamageVehicleAction(action) for action in scriptSection[b'actions'].values())
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

    def _readConfig(self, xmlCtx, scriptSection):
        super(UpgradableItem, self)._readConfig(xmlCtx, scriptSection)
        self._readUpgradableConfig(xmlCtx, scriptSection)
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
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription)
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.healthRegenPerTick = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'healthRegenPerTick', 0.0)
        self.initialHeal = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'initialHeal', 0.0)
        self.healTime = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'healTime', 0.0)
        self.healGroup = _xml.readIntOrNone(xmlCtx, scriptSection, b'healGroup')
        self.tickInterval = _xml.readPositiveFloat(xmlCtx, scriptSection, b'tickInterval', 1.0)
        self.expireByDamageReceived = _xml.readBool(xmlCtx, scriptSection, b'expireByDamageReceived', False)
        self.resupplyHealthPointsFactor = _xml.readPositiveFloat(xmlCtx, scriptSection, b'resupplyHealthPointsFactor', 1.0)
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

    def _readConfig(self, xmlCtx, scriptSection):
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readSharedCooldownConsumableConfig(xmlCtx, scriptSection)
        self.readConsumableWithTimeConfig(xmlCtx, scriptSection)
        self.readInspireConfig(xmlCtx, scriptSection)
        self.passiveCircularVisionRadius = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'passiveCircularVisionRadius', 0.0)
        self.detectionTime = _xml.readNonNegativeFloat(xmlCtx, scriptSection, b'minesDetectionTime', 0.0)
        self.readOverFactorsFromConfig(xmlCtx, scriptSection)
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

    def _readConfig(self, xmlCtx, scriptSection):
        bombs = _xml.readTupleOfFloats(xmlCtx, scriptSection, b'bombsPattern')
        self.bombsPattern = [(bombs[b], bombs[b + 1]) for b in range(0, len(bombs) - 1, 2)]
        self.mineParams._readConfig(xmlCtx, scriptSection[b'mineParams'])
        self.cooldownTime = _xml.readInt(xmlCtx, scriptSection, b'cooldownSeconds')
        self.disableAllyDamage = _xml.readBool(xmlCtx, scriptSection, b'disableAllyDamage')
        self.areaLength = _xml.readPositiveFloat(xmlCtx, scriptSection, b'areaLength')
        self.areaWidth = _xml.readPositiveFloat(xmlCtx, scriptSection, b'areaWidth')
        self.areaVisual = _xml.readStringOrNone(xmlCtx, scriptSection, b'areaVisual')
        self.readCountableConsumableConfig(xmlCtx, scriptSection)
        self.readTooltipInformation(xmlCtx, scriptSection)
        self.readArcadeInformation(xmlCtx, scriptSection)
        if IS_CLIENT and self.longDescription:
            self.longDescription = i18n.makeString(self.longDescription, duration=int(self.mineParams.lifetime))
        return


class FrontLineMinefield(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArcadeEquipmentConfigReader, CooldownConsumableConfigReader):
    __slots__ = (b'bombsPattern', b'mineParams', b'noOwner', b'areaLength', b'areaWidth', b'areaVisual', b'areaColor', b'areaMarker', b'bombsNumber')

    def __init__(self):
        super(FrontLineMinefield, self).__init__()
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

    def _readConfig(self, xmlCtx, scriptSection):
        section = scriptSection
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


class VisualScriptEquipment(Equipment):
    __slots__ = (b'visualScript',)

    def __init__(self):
        super(VisualScriptEquipment, self).__init__()
        self.visualScript = {}
        return

    def _readConfig(self, xmlCtx, scriptSection):
        self.visualScript = readVisualScriptSection(scriptSection)
        return

    def _exportSlotsToVSE(self):
        params = self._getExportParamsDict(ExportParamsTag.VSE)
        if not params:
            return
        for plans in viewvalues(self.visualScript):
            for planDef in plans:
                planDef[b'params'].update(params)

        self._exportParams[ExportParamsTag.VSE.value].clear()
        return


class LevelBasedVisualScriptEquipment(VisualScriptEquipment):
    _LEVEL_BASED_SLOTS = (b'radius',)

    def __init__(self):
        super(LevelBasedVisualScriptEquipment, self).__init__()
        self.radius = ()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(LevelBasedVisualScriptEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.radius = tuple(map(float, scriptSection.readString(b'radius').split()))
        if len(self.radius) == 0:
            _xml.raiseWrongXml(xmlCtx, b'radius', b'should be multiple values separated by space.')
        return

    def getRadiusBasedOnSkillLevel(self, skillLevel):
        return self.radius[skillLevel - 1]


class DynComponentsGroupEquipment(Equipment):
    __slots__ = (b'durationSeconds', b'dynComponentsGroups')

    def _readConfig(self, xmlCtx, scriptSection):
        super(DynComponentsGroupEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.durationSeconds = _xml.readFloat(xmlCtx, scriptSection, b'durationSeconds')
        self.dynComponentsGroups = frozenset(_xml.readString(xmlCtx, scriptSection, b'dynComponentsGroups').split())
        return


class PoiRadarEquipment(VisualScriptEquipment):
    __slots__ = (b'duration',)

    def _readConfig(self, xmlCtx, scriptSection):
        super(PoiRadarEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.duration = scriptSection.readFloat(b'duration')
        self._exportSlotsToVSE()
        return


class PoiArtilleryEquipment(VisualScriptEquipment, BaseMarkerConfigReader, EffectsConfigReader):
    __slots__ = BaseMarkerConfigReader._MARKER_SLOTS_ + EffectsConfigReader._EFFECTS_SLOTS_ + (b'delay', b'radius', b'damage', b'stunDuration', b'duration', b'areaShow', b'fraction', b'requireAssists')

    def __init__(self):
        super(PoiArtilleryEquipment, self).__init__()
        self.initMarkerInformation()
        self.initEffectsInformation()
        return

    def _readConfig(self, xmlCtx, scriptSection):
        super(PoiArtilleryEquipment, self)._readConfig(xmlCtx, scriptSection)
        self.delay = scriptSection.readFloat(b'delay')
        self.radius = scriptSection.readFloat(b'radius')
        self.damage = scriptSection.readFloat(b'damage')
        self.stunDuration = scriptSection.readFloat(b'stunDuration')
        self.areaShow = scriptSection.readString(b'areaShow').lower() or None
        self.duration = scriptSection.readFloat(b'duration')
        self.readMarkerConfig(xmlCtx, scriptSection)
        self.readEffectConfig(xmlCtx, scriptSection)
        self.fraction = scriptSection.readFloat(b'fraction')
        self.requireAssists = scriptSection.readBool(b'requireAssists', False)
        self._exportSlotsToVSE()
        return


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
    POSTSTART = b'poststart'
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
