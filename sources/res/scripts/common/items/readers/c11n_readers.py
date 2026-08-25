from __future__ import absolute_import
import re, os
from copy import deepcopy
from future.utils import lmap, viewitems, viewvalues
from past.builtins import intern
import Math, items._xml as ix, items.components.c11n_components as cc, items.customizations as c11n, items.vehicles as iv, nations
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS, parseArenaBonusType
from constants import IS_CLIENT, IS_EDITOR, IS_UE_EDITOR, IS_WEB, IS_LOAD_GLOSSARY, DEFAULT_QUEST_FINISH_TIME
from items.components import shared_components
from items.components.c11n_constants import CustomizationType, CustomizationTypeNames, ProjectionDecalFormTags, CustomizationNamesToTypes, CustomizationDisplayType, EMPTY_ITEM_ID, SeasonType, ApplyArea, DecalType, ModificationType, RENT_DEFAULT_BATTLES, ItemTags, ProjectionDecalType, DEFAULT_GLOSS, DEFAULT_METALLIC
from extension_utils import ResMgr
from typing import Dict, Type, Tuple, Any, TypeVar
from contextlib import contextmanager
from customization_quests_common import serializeToken, PREFIX
from bonus_readers import readUTC
from soft_exception import SoftException
if IS_EDITOR:
    from items.components.c11n_components import CUSTOMIZATION_CLASSES
    from reflection_framework.unintrusive_weakref import ref as UnintrusiveWeakRef
    from meta_objects.items.components.c11n_components_meta import I18nExposedComponentMeta

    @contextmanager
    def storeChangedProperties(obj, props):

        def storeCallback(event):
            props.add(event.propertyName)
            return

        obj.onChanged += storeCallback
        yield
        obj.onChanged -= storeCallback
        return


else:

    @contextmanager
    def storeChangedProperties(obj, props):
        yield
        return


_itemType = TypeVar(b'_itemType', bound=cc.BaseCustomizationItem)

class BaseCustomizationItemXmlReader(object):
    __slots__ = ()

    def __init__(self):
        super(BaseCustomizationItemXmlReader, self).__init__()
        return

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        if section.has_key(b'id'):
            target.id = ix.readInt(xmlCtx, section, b'id', 1)
        if section.has_key(b'tags'):
            target.tags = iv._readTags(xmlCtx, section, b'tags', b'customizationItem')
            if target.itemType == CustomizationType.PROJECTION_DECAL:
                formTags = [tag for tag in target.tags if tag in ProjectionDecalFormTags.ALL]
                if len(formTags) > 1:
                    ix.raiseWrongXml(xmlCtx, b'tags', b'wrong formfactor for prjection decal ID%i' % target.id)
        if section.has_key(b'vehicleFilter'):
            target.filter = self.readVehicleFilterFromXml((xmlCtx, b'vehicleFilter'), section[b'vehicleFilter'])
        target.season = readFlagEnum(xmlCtx, section, b'season', SeasonType, target.season)
        target.customizationDisplayType = section.readInt(b'historical', target.customizationDisplayType)
        if section.has_key(b'priceGroup'):
            target.priceGroup = section.readString(b'priceGroup')
        if section.has_key(b'requiredToken'):
            target.requiredToken = section.readString(b'requiredToken')
            target.requiredTokenCount = 1
        if section.has_key(b'maxNumber'):
            target.maxNumber = ix.readPositiveInt(xmlCtx, section, b'maxNumber')
            if target.maxNumber <= 0:
                ix.raiseWrongXml(xmlCtx, b'maxNumber', b'should not be less then 1')
        if section.has_key(b'rarity'):
            target.rarity = ix.readStringOrEmpty(xmlCtx, section, b'rarity')
        if IS_CLIENT or IS_EDITOR or IS_WEB or IS_LOAD_GLOSSARY:
            self._readClientOnlyFromXml(target, xmlCtx, section, cache)
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        if IS_EDITOR:
            target.i18n = I18nExposedComponentMeta(section.readString(b'name'), section.readString(b'userString'), section.readString(b'description'), section.readString(b'longDescriptionSpecial'), section.readString(b'shortDescriptionSpecial'))
        else:
            target.i18n = shared_components.I18nExposedComponent(section.readString(b'userString'), section.readString(b'description'), section.readString(b'longDescriptionSpecial'), section.readString(b'name'), section.readString(b'shortDescriptionSpecial'))
        return

    @staticmethod
    def readVehicleFilterFromXml(xmlCtx, section):
        vc = cc.VehicleFilter()
        readNode = BaseCustomizationItemXmlReader.__readFilterNodeFromXml
        for subsection in section.values():
            if subsection.name == b'include':
                vc.include.append(readNode((xmlCtx, b'include'), subsection))
            elif subsection.name == b'exclude':
                vc.exclude.append(readNode((xmlCtx, b'exclude'), subsection))
            else:
                ix.raiseWrongXml(xmlCtx, subsection.name, b'should be <include> or <exclude>')

        return vc

    @staticmethod
    def __readFilterNodeFromXml(xmlCtx, section):
        fn = cc.VehicleFilterNode()
        strNations = ix.readStringOrNone(xmlCtx, section, b'nations')
        if strNations:
            r = []
            for nation in strNations.split():
                nationId = nations.INDICES.get(nation)
                if nationId is None:
                    ix.raiseWrongXml(xmlCtx, b'nations', b'unknown nation "%s"' % nation)
                r.append(nationId)

            fn.nations = r
        if section.has_key(b'levels'):
            fn.levels = ix.readTupleOfPositiveInts(xmlCtx, section, b'levels')
        if section.has_key(b'vehicles'):
            fn.vehicles = iv._readNationVehiclesByNames(xmlCtx, section, b'vehicles', None)
        if section.has_key(b'tags'):
            fn.tags = iv._readTags(xmlCtx, section, b'tags', b'vehicle')
        return fn


class PaintXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(PaintXmlReader, self)._readFromXml(target, xmlCtx, section)
        if section.has_key(b'color'):
            target.color = iv._readColor(xmlCtx, section, b'color')
        if section.has_key(b'gloss'):
            target.gloss = ix.readFloat(xmlCtx, section, b'gloss', 0.0)
        if section.has_key(b'metallic'):
            target.metallic = ix.readFloat(xmlCtx, section, b'metallic', 0.0)
        if section.has_key(b'usages'):
            xmlSubCtx = (
             xmlCtx, b'usages')
            for _, sub in ix.getChildren(xmlCtx, section, b'usages'):
                ctype, cost = self._readUsage(xmlSubCtx, sub)
                for i in ApplyArea.RANGE:
                    if ctype & i:
                        target.usageCosts[i] = cost

        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(PaintXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        return

    @staticmethod
    def _readUsage(xmlCtx, section):
        componentType = readFlagEnum(xmlCtx, section, b'componentType', ApplyArea)
        cost = section.readInt(b'cost', 1)
        return (componentType, cost)


class DecalXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(DecalXmlReader, self)._readFromXml(target, xmlCtx, section)
        if section.has_key(b'type'):
            target.type = readEnum(xmlCtx, section, b'type', DecalType)
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(DecalXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        if section.has_key(b'mirror'):
            target.canBeMirrored = ix.readBool(xmlCtx, section, b'mirror')
        readEmissionParams(target, xmlCtx, section)
        return


class ProjectionDecalXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(ProjectionDecalXmlReader, self)._readFromXml(target, xmlCtx, section)
        if b'mirror' in section.keys():
            target.canBeMirroredHorizontally = ix.readBool(xmlCtx, section, b'mirror')
        if b'onlyVerticalMirror' in target.tags:
            if target.canBeMirroredHorizontally:
                ix.raiseWrongXml(xmlCtx, b'tags', b'mirror must be false when onlyVerticalMirror set')
            if b'disableVerticalMirror' in target.tags:
                ix.raiseWrongXml(xmlCtx, b'tags', b'disableVerticalMirror and onlyVerticalMirror cannot be set at the same time')
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(ProjectionDecalXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        if section.has_key(b'glossTexture'):
            target.glossTexture = section.readString(b'glossTexture')
        if section.has_key(b'scaleFactorId'):
            target.scaleFactorId = section.readInt(b'scaleFactorId')
        readEmissionParams(target, xmlCtx, section)
        return


class PersonalNumberXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        if section.has_key(b'digitsCount'):
            target.digitsCount = section.readInt(b'digitsCount')
        super(PersonalNumberXmlReader, self)._readFromXml(target, xmlCtx, section, cache)
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(PersonalNumberXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section, cache)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        if section.has_key(b'preview_texture'):
            target.previewTexture = section.readString(b'preview_texture')
        if section.has_key(b'fontId'):
            target.fontInfo = cache.fonts[section.readInt(b'fontId')]
        return


class SequenceXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(SequenceXmlReader, self)._readFromXml(target, xmlCtx, section)
        target.sequenceName = ix.readStringOrNone(xmlCtx, section, b'sequenceName')
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(SequenceXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        target.sequenceName = ix.readStringOrNone(xmlCtx, section, b'sequenceName')
        if IS_EDITOR:
            target.name = ix.readStringOrNone(xmlCtx, section, b'name')
        return


class AttachmentXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(AttachmentXmlReader, self)._readFromXml(target, xmlCtx, section)
        target.applyType = ix.readStringOrEmpty(xmlCtx, section, b'applyType')
        target.size = ix.readStringOrEmpty(xmlCtx, section, b'size')
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(AttachmentXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        target.modelName = ix.readStringOrEmpty(xmlCtx, section, b'modelName')
        target.hangarModelName = ix.readStringOrEmpty(xmlCtx, section, b'hangarModelName')
        target.crashModelName = ix.readStringOrEmpty(xmlCtx, section, b'crashModelName')
        target.leftModelName = ix.readStringOrEmpty(xmlCtx, section, b'leftModelName')
        target.rightModelName = ix.readStringOrEmpty(xmlCtx, section, b'rightModelName')
        target.sequenceId = ix.readNonNegativeInt(xmlCtx, section, b'sequenceId', 0)
        target.attachmentLogic = ix.readStringOrEmpty(xmlCtx, section, b'attachmentLogic')
        if IS_EDITOR:
            target.name = ix.readStringOrNone(xmlCtx, section, b'name')
        return


class StatTrackerXmlReader(AttachmentXmlReader):
    __slots__ = ()

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(StatTrackerXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        target.trackedStatistic = ix.readStringOrEmpty(xmlCtx, section, b'trackedStatistic')
        return


class ModificationXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(ModificationXmlReader, self)._readFromXml(target, xmlCtx, section)
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(ModificationXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        if section.has_key(b'effects'):
            xmlSubCtx = (
             xmlCtx, b'effects')
            i = 0
            result = {}
            for name, sub in ix.getChildren(xmlCtx, section, b'effects'):
                itemCtx = (
                 xmlSubCtx, (b'{}[{}]').format(name, i))
                mtype = readEnum(itemCtx, sub, b'type', ModificationType)
                result[mtype] = ix.readFloat(itemCtx, sub, b'value', 0.0)
                i += 1

            target.effects = result
        if section.has_key(b'useNewWear'):
            xmlSubCtx = (
             xmlCtx, b'useNewWear')
            target.useNewWear = ix.readBool(xmlSubCtx, section, b'useNewWear', False)
        return


class CamouflageXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(CamouflageXmlReader, self)._readFromXml(target, xmlCtx, section)
        target.compatibleParts = readFlagEnum(xmlCtx, section, b'compatibleParts', ApplyArea, target.compatibleParts)
        target.componentsCovering = readFlagEnum(xmlCtx, section, b'componentsCovering', ApplyArea, target.componentsCovering)
        target.invisibilityFactor = section.readFloat(b'invisibilityFactor', 1.0)
        target.glossMetallicSettings = {b'glossMetallicMap': (section.readString(b'glossMetallicMap', b'')), 
           b'gloss': (section.readVector4(b'gloss', Math.Vector4(DEFAULT_GLOSS))), 
           b'metallic': (section.readVector4(b'metallic', Math.Vector4(DEFAULT_METALLIC)))}
        if IS_EDITOR:
            target.editorData.glossMetallicSettingsType = 0
            if target.glossMetallicSettings[b'glossMetallicMap'] != b'':
                target.editorData.glossMetallicSettingsType = 1
            editorOnlySection = c11n.getEditorOnlySection(section)
            if editorOnlySection is not None:
                target.editorData.paletteIndex = editorOnlySection.readInt(b'paletteIndex', 0)
        if section.has_key(b'palettes'):
            palettes = []
            spalettes = section[b'palettes']
            for psection in spalettes.values():
                res = []
                pctx = (
                 xmlCtx, b'palettes')
                for j, (cname, _) in enumerate(psection.items()):
                    res.append(iv._readColor((pctx, b'palette %s' % (j,)), psection, cname))

                palettes.append(res)
                target.palettes = tuple(palettes)

        if section.has_key(b'style'):
            target.styleId = section.readInt(b'style')
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(CamouflageXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        if section.has_key(b'tiling'):
            if IS_EDITOR:
                target.tiling, target.editorData.tilingName = iv._readCamouflageTilings(xmlCtx, section, b'tiling', self.getDefaultNationId(target))
            else:
                target.tiling = iv._readCamouflageTilings(xmlCtx, section, b'tiling', self.getDefaultNationId(target))
        if section.has_key(b'tilingSettings'):
            target.tilingSettings = iv._readCamouflageTilingSettings(xmlCtx, section)
        if section.has_key(b'scales'):
            target.scales = ix.readTupleOfFloats(xmlCtx, section, b'scales')
        if section.has_key(b'rotation'):
            rotation = section[b'rotation']
            target.rotation = {b'hull': (rotation.readFloat(b'HULL', 0.0)), 
               b'turret': (rotation.readFloat(b'TURRET', 0.0)), 
               b'gun': (rotation.readFloat(b'GUN', 0.0))}
        if section.has_key(b'normal'):
            scamo_normal = section[b'normal']
            if target.normalMapSettings is not None:
                target.normalMapSettings = deepcopy(target.normalMapSettings)
            else:
                target.normalMapSettings = {b'normalMap': b'', b'normalStrength': 0.0}
            if scamo_normal.has_key(b'normalMap'):
                target.normalMapSettings[b'normalMap'] = scamo_normal.readString(b'normalMap', b'')
            if scamo_normal.has_key(b'normalStrength'):
                target.normalMapSettings[b'normalStrength'] = scamo_normal.readFloat(b'normalStrength', 0.0)
        readEmissionParams(target, xmlCtx, section)
        return

    @staticmethod
    def getDefaultNationId(target):
        if target.filter and target.filter.include and target.filter.include[0].nations:
            return target.filter.include[0].nations[0]
        return nations.NONE_INDEX


class StyleXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()
    __outfitDeserializer = c11n.ComponentXmlDeserializer(c11n._CUSTOMIZATION_CLASSES)

    def __readOutfitSection(self, targetId, section, xmlCtx):
        outfits = {}
        for i, (_, oSection) in enumerate(section[b'outfits'].items()):
            oCtx = ((xmlCtx, b'outfits'), (b'outfit {}').format(i))
            season = readFlagEnum(oCtx, oSection, b'season', SeasonType)
            outfit = self.__outfitDeserializer.decode(c11n.CustomizationOutfit.customType, oCtx, oSection)
            for s in SeasonType.SEASONS:
                if s & season:
                    outfits[s] = outfit

            if IS_EDITOR:
                for projectionDecal in outfit.projection_decals:
                    if projectionDecal.tags is not None and len(projectionDecal.tags) > 0:
                        projectionDecal.editorData.decalType = ProjectionDecalType.TAGS

            outfit.styleId = targetId

        return outfits

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(StyleXmlReader, self)._readFromXml(target, xmlCtx, section)
        prototype = True
        if section.has_key(b'modelsSet'):
            target.modelsSet = section.readString(b'modelsSet')
            if IS_EDITOR:
                target.editorData.modelsSet = target.modelsSet
        if section.has_key(b'itemFilters'):
            target.isEditable = True
            itemsFilters = {}
            for sectionName, oSection in section[b'itemFilters'].items():
                c11nType = CustomizationNamesToTypes[sectionName.upper()]
                itemsFilters[c11nType] = self._readItemsFilterFromXml(c11nType, xmlCtx, oSection)

            target.itemsFilters = itemsFilters
        if section.has_key(b'alternateItems'):
            target.isEditable = True
            alternateItems = {}
            for sectionName, oSection in section[b'alternateItems'].items():
                c11nType = CustomizationNamesToTypes[sectionName.upper()]
                if oSection.has_key(b'id'):
                    alternateItems[c11nType] = ix.readTupleOfPositiveInts(xmlCtx, oSection, b'id')

            target.alternateItems = alternateItems
        if section.has_key(b'dependencies'):
            target.isEditable = True
            dependencies = {}
            dependenciesAncestors = {}
            for _, camouflageSection in section[b'dependencies'].items():
                camouflageDependencies = {}
                for sectionName in camouflageSection.keys():
                    if sectionName == b'id':
                        camouflageIDs = ix.readTupleOfPositiveInts(xmlCtx, camouflageSection, b'id')
                    else:
                        c11nType = CustomizationNamesToTypes[sectionName.upper()]
                        camouflageDependencies[c11nType] = ix.readTupleOfPositiveInts(xmlCtx, camouflageSection, sectionName)

                for camouflageID in camouflageIDs:
                    dependencies[camouflageID] = camouflageDependencies
                    for itemType, itemIDs in viewitems(camouflageDependencies):
                        itemTypeAncestors = dependenciesAncestors.setdefault(itemType, {})
                        for customizationItemID in itemIDs:
                            itemTypeAncestors.setdefault(customizationItemID, []).append(camouflageID)

            target.dependencies = dependencies
            target.dependenciesAncestors = dependenciesAncestors
        if section.has_key(b'outfits'):
            prototype = False
            outfits = self.__readOutfitSection(target.id, section, xmlCtx)
            target.outfits = outfits
        if section.has_key(b'isRent'):
            target.isRent = section.readBool(b'isRent')
        if target.isRent:
            target.rentCount = section.readInt(b'rentCount', RENT_DEFAULT_BATTLES)
            target.tags = target.tags.union(frozenset((ItemTags.VEHICLE_BOUND,)))
        totalSeason = sum(target.outfits)
        if totalSeason != target.season and not prototype:
            ix.raiseWrongXml(xmlCtx, b'outfits', b'style season must correspond to declared outfits')
        return

    @staticmethod
    def _readItemsFilterFromXml(itemType, xmlCtx, section):
        f = cc.ItemsFilter()
        readNode = StyleXmlReader.__readItemFilterNodeFromXml
        for subsection in section.values():
            if subsection.name == b'include':
                f.include.append(readNode(itemType, (xmlCtx, b'include'), subsection))
            elif subsection.name == b'exclude':
                f.exclude.append(readNode(itemType, (xmlCtx, b'exclude'), subsection))

        return f

    @staticmethod
    def __readItemFilterNodeFromXml(itemType, xmlCtx, section):
        fn = cc.ItemsFilterNode()
        if section.has_key(b'id'):
            fn.ids = ix.readTupleOfPositiveInts(xmlCtx, section, b'id')
        if section.has_key(b'itemGroupName'):
            fn.itemGroupNames = ix.readTupleOfStrings(xmlCtx, section, b'itemGroupName', separator=b';')
        if section.has_key(b'tags'):
            fn.tags = iv._readTags(xmlCtx, section, b'tags', b'customizationItem')
        if section.has_key(b'type'):
            if itemType is not CustomizationType.DECAL:
                ix.raiseWrongXml(xmlCtx, b'type', b'type can be used only with decals')
            types = set(getattr(DecalType, typeName) for typeName in ix.readTupleOfStrings(xmlCtx, section, b'type'))
            if not types.issubset(DecalType.ALL):
                ix.raiseWrongXml(xmlCtx, b'type', b'unsupported type is used')
            fn.types = types
        if section.has_key(b'historical'):
            fn.customizationDisplayType = ix.readInt(xmlCtx, section, b'historical', CustomizationDisplayType.NON_HISTORICAL)
        return fn

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(StyleXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        if section.has_key(b'styleProgressions'):
            styleProgressions = {}
            for i, (_, spSection) in enumerate(section[b'styleProgressions'].items()):
                stageId = i + 1
                styleProgressions[stageId] = {}
                if spSection.has_key(b'materials'):
                    styleProgressions[stageId][b'materials'] = spSection[b'materials'].asString.split()
                if spSection.has_key(b'outfits'):
                    outfits = self.__readOutfitSection(target.id, spSection, xmlCtx)
                    styleProgressions[stageId][b'additionalOutfit'] = outfits

            target.styleProgressions = styleProgressions
        return


class InsigniaXmlReader(BaseCustomizationItemXmlReader):
    __slots__ = ()

    def _readFromXml(self, target, xmlCtx, section, cache=None):
        super(InsigniaXmlReader, self)._readFromXml(target, xmlCtx, section)
        return

    def _readClientOnlyFromXml(self, target, xmlCtx, section, cache=None):
        super(InsigniaXmlReader, self)._readClientOnlyFromXml(target, xmlCtx, section)
        if section.has_key(b'atlas'):
            target.atlas = section.readString(b'atlas')
        if section.has_key(b'alphabet'):
            target.alphabet = section.readString(b'alphabet')
        if section.has_key(b'texture'):
            target.texture = section.readString(b'texture')
        target.canBeMirrored = section.readBool(b'canBeMirrored', True)
        return


def readCustomizationCacheFromXml(cache, folder):

    def __readItemFolder(itemCls, folder, itemName, storage):
        progressionFileName = os.path.join(folder, itemName + b's', b'progression.xml')
        dataSection = ResMgr.openSection(progressionFileName)
        progression = {}
        if dataSection:
            try:
                _readProgression(cache, (None, itemName + b's/progression.xml'), dataSection, progression)
            finally:
                ResMgr.purge(progressionFileName)

        itemsFileName = os.path.join(folder, itemName + b's', b'list.xml')
        dataSection = ResMgr.openSection(itemsFileName)
        try:
            _readItems(cache, itemCls, (None, itemName + b's/list.xml'), dataSection, itemName, storage, progression)
        finally:
            ResMgr.purge(itemsFileName)

        return

    pgFile = os.path.join(folder, b'priceGroups', b'list.xml')
    _readPriceGroups(cache, (None, b'priceGroups/list.xml'), ResMgr.openSection(pgFile), b'priceGroup')
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, b'default.xml')
    _readDefault(cache, (None, b'default.xml'), ResMgr.openSection(pgFile), b'default')
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, b'fonts', b'list.xml')
    _readFonts(cache, (None, b'fonts/list.xml'), ResMgr.openSection(pgFile), b'font')
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, b'personal_numbers', b'prohibitedNumbers.xml')
    _readProhibitedNumbers(cc.PersonalNumberItem, (None, b'personal_numbers/prohibitedNumbers.xml'), ResMgr.openSection(pgFile))
    ResMgr.purge(pgFile)
    pgFile = os.path.join(folder, b'stat_trackers', b'prohibitedNumbers.xml')
    _readProhibitedNumbers(cc.StatTrackerItem, (None, b'stat_trackers/prohibitedNumbers.xml'), ResMgr.openSection(pgFile))
    ResMgr.purge(pgFile)
    __readItemFolder(cc.PaintItem, folder, b'paint', cache.paints)
    __readItemFolder(cc.CamouflageItem, folder, b'camouflage', cache.camouflages)
    __readItemFolder(cc.ModificationItem, folder, b'modification', cache.modifications)
    __readItemFolder(cc.DecalItem, folder, b'decal', cache.decals)
    __readItemFolder(cc.ProjectionDecalItem, folder, b'projection_decal', cache.projection_decals)
    __readItemFolder(cc.StyleItem, folder, b'style', cache.styles)
    __readItemFolder(cc.InsigniaItem, folder, b'insignia', cache.insignias)
    __readItemFolder(cc.PersonalNumberItem, folder, b'personal_number', cache.personal_numbers)
    __readItemFolder(cc.SequenceItem, folder, b'sequence', cache.sequences)
    __readItemFolder(cc.AttachmentItem, folder, b'attachment', cache.attachments)
    __readItemFolder(cc.StatTrackerItem, folder, b'stat_tracker', cache.stat_trackers)
    pgFile = os.path.join(folder, b'progression', b'list.xml')
    for style, questProgression in readQuestProgression(cache, (None, b'progression/list.xml'), ResMgr.openSection(pgFile), b'styleProgress'):
        style.questsProgression = questProgression

    ResMgr.purge(pgFile)
    _validateStyles(cache)
    _validateCamouflages(cache)
    return


def _validateStyles(cache):

    def customizationItemInOutfits(style, itemID, itemType):
        for season in SeasonType.RANGE:
            outfit = style.outfits.get(season)
            if outfit:
                customizationItems = getattr(outfit, (b'{}s').format(CustomizationTypeNames[itemType].lower()))
                for customizationItem in customizationItems:
                    if itemID == customizationItem.id:
                        return True

        return False

    styleOnlyItemsFromStyles = set()
    for style in viewvalues(cache.styles):
        if style.isEditable:
            alternateItemsIDs = {}
            if style.alternateItems:
                for itemType, ids in viewitems(style.alternateItems):
                    alternateItemsIDs[itemType] = ids
                    items = lmap(cache.itemTypes[itemType].get, ids)
                    styleOnlyItemsFromStyles.update(items)

            if style.dependencies:
                for camouflageID, camouflageDependencies in viewitems(style.dependencies):
                    if camouflageID not in alternateItemsIDs.get(CustomizationType.CAMOUFLAGE, {}) and not customizationItemInOutfits(style, camouflageID, CustomizationType.CAMOUFLAGE):
                        raise SoftException((b'Items {} itemType {} from dependencies must be included in alternateItems or outfits').format(camouflageID, 2))
                    for itemType, ids in viewitems(camouflageDependencies):
                        inStyle = False
                        idsDiff = set(ids).difference(set(alternateItemsIDs.get(itemType, {})))
                        for itemID in idsDiff:
                            if not customizationItemInOutfits(style, itemID, itemType):
                                break
                        else:
                            inStyle = True

                        if not inStyle:
                            raise SoftException((b'Items {} itemType {} from dependencies must be included in alternateItems or outfits').format(ids, itemType))

    if any(item is None or not item.isStyleOnly for item in styleOnlyItemsFromStyles):
        raise SoftException(b'Items shall contain styleOnly tag in tags to be used in alternateItems')
    return


def _validateCamouflages(cache):
    for camouflage in viewvalues(cache.camouflages):
        styleId = camouflage.styleId
        if styleId:
            if styleId not in cache.styles:
                raise SoftException((b'Link style {} in camouflage {} not exist ').format(styleId, camouflage.id))

    return


def _readProhibitedNumbers(itemCls, xmlCtx, section):
    prohibitedNumbers = ix.readTupleOfStrings(xmlCtx, section, b'ProhibitedNumbers')
    if all(prohibitedNumber == b'' for prohibitedNumber in prohibitedNumbers):
        return
    for prohibitedNumber in prohibitedNumbers:
        if not prohibitedNumber.isdigit():
            ix.raiseWrongXml(xmlCtx, b'ProhibitedNumbers', b'%s is not a number' % prohibitedNumber)

    itemCls.setProhibitedNumbers(prohibitedNumbers)
    return


def __readProgressLevel(xmlCtx, section):
    level = {}
    for sectionName, subSections in section.items():
        if sectionName == b'price':
            level.update({b'price': (ix.readPrice(xmlCtx, section, b'price')), 
               b'notInShop': (section.readBool(b'notInShop', False))})
        elif sectionName == b'condition':
            conditions = level.setdefault(b'conditions', [])
            condition = {}
            for subSection in subSections.values():
                sectionName = subSection.name
                if sectionName == b'description':
                    condition.update({b'description': (ix.readNonEmptyString(xmlCtx, subSection, b''))})
                else:
                    condition.update(__readCondition((xmlCtx, subSection.name), subSection, [sectionName]))

            if not condition:
                ix.raiseWrongXml(xmlCtx, b'progression', b"Customization don't have conditions")
            conditions.append(condition)

    return level


def __readCondition(xmlCtx, section, path):
    subSections = section.values()
    if subSections:
        path.append(subSections[0].name)
        return __readCondition((xmlCtx, subSections[0].name), subSections[0], path)
    else:
        return {b'path': (tuple(path)), b'value': (ix.readNonEmptyString(xmlCtx, section, b''))}

    return


def __readProgress(xmlCtx, section):
    progress = cc.ProgressForCustomization()
    itemId = ix.readInt(xmlCtx, section, b'id')
    if section.has_key(b'autobound'):
        progress.autobound = True
    for sectionName, subSection in section.items():
        if sectionName == b'levels':
            for levelSectionName, levelSection in subSection.items():
                level = int(re.findall(b'\\d+', levelSectionName)[0])
                if levelSection[b'default'] is not None:
                    progress.defaultLvl = level if level > progress.defaultLvl else progress.defaultLvl
                progress.levels[level] = __readProgressLevel((xmlCtx, levelSectionName), levelSection)

        if sectionName == b'autoGrantCount':
            progress.autoGrantCount = ix.readPositiveInt(xmlCtx, subSection, b'')
        if sectionName == b'bonusType':
            bonusTypes = ix.readStringOrEmpty(xmlCtx, subSection, b'').split()
            parseArenaBonusType(progress.bonusTypes, bonusTypes, ARENA_BONUS_TYPE_CAPS.CUSTOMIZATION_PROGRESSION)
        if sectionName == b'priceGroup':
            progress.priceGroup = ix.readStringOrEmpty(xmlCtx, subSection, b'')

    if len(progress.levels) < 2:
        ix.raiseWrongXml(xmlCtx, b'tags', b'wrong progression. Minimum count progression = 2. Current count progression %i' % len(progress.levels))
    for i in range(1, len(progress.levels) + 1):
        if i not in progress.levels:
            ix.raiseWrongXml(xmlCtx, b'tags', b'wrong progression. Skipped level %i' % i)

    if progress.levels[1].get(b'notInShop'):
        ix.raiseWrongXml(xmlCtx, b'tags', b'wrong progression. First level should always be available for purchase.')
    return (itemId, progress)


def _readProgression(cache, xmlCtx, section, progression):
    for gname, gsection in section.items():
        if gname != b'progress':
            ix.raiseWrongSection(xmlCtx, gname)
        itemId, progress = __readProgress((xmlCtx, b'progress'), gsection)
        if progress.priceGroup:
            if progress.priceGroup not in cache.priceGroupNames:
                if IS_EDITOR:
                    continue
                ix.raiseWrongXml(xmlCtx, b'priceGroup', b'unknown price group %s for item %s' % (
                 progress.priceGroup, itemId))
            priceGroupId = cache.priceGroupNames[progress.priceGroup]
            pgDescr = cache.priceGroups[priceGroupId].compactDescr
            for num, level in viewitems(progress.levels):
                if b'price' not in level and progress.defaultLvl != num:
                    priceInfo = iv.getPriceForItemDescr(pgDescr)
                    if priceInfo:
                        level.update({b'price': (priceInfo[0]), 
                           b'notInShop': (priceInfo[1])})

        progression[itemId] = progress

    return


def _readItems(cache, itemCls, xmlCtx, section, itemSectionName, storage, progression):
    reader = __xmlReaders[itemCls]
    priceGroupsDict = cache.priceGroups
    itemToPriceGroup = cache.itemToPriceGroup
    if IS_EDITOR:
        itemType = CUSTOMIZATION_CLASSES[itemCls]
        cache.editorData.groups[itemType] = []
        sourceFiles = set()
        if section is None:
            return
    for i, (gname, gsection) in enumerate(section.items()):
        if gname != b'itemGroup' and b'xmlns:' not in gname:
            ix.raiseWrongSection(xmlCtx, gname)
        if gname != b'itemGroup':
            continue
        group = cc.ItemGroup(itemCls)
        gCtx = (xmlCtx, (b'itemGroup {0}').format(i))
        itemPrototype = itemCls()
        sharedProps = set()
        with storeChangedProperties(itemPrototype, sharedProps):
            reader._readFromXml(itemPrototype, gCtx, gsection, cache)
        group.itemPrototype = itemPrototype
        groupItems = []
        if gsection.has_key(b'name'):
            group.name = gsection.readString(b'name')
        j = 0
        for iname, isection in gsection.items():
            if iname != itemSectionName:
                continue
            iCtx = (
             gCtx, (b'{0} {1}').format(iname, j))
            j += 1
            item = itemCls(group)
            overrideProps = set()
            with storeChangedProperties(item, overrideProps):
                reader._readFromXml(item, iCtx, isection, cache)
            if IS_EDITOR:
                item.editorData.sharedPropertiesInfo.markAsOverride(*overrideProps)
            groupItems.append(item)
            if item.compactDescr in itemToPriceGroup:
                ix.raiseWrongXml(iCtx, b'id', b'duplicate item. id: %s found in group %s' % (
                 item.id, itemToPriceGroup[item.compactDescr]))
            storage[item.id] = item
            item.progression = progression.get(item.id, None)
            if item.progression is not None:
                cache.customizationWithProgression[item.compactDescr] = item
                iv._readPriceForProgressionLvl(item.compactDescr, item.progression.levels)
                for arenaTypeID, items in viewitems(cache.itemGroupByProgressionBonusType):
                    if arenaTypeID in item.progression.bonusTypes:
                        items.append(item)

            if isection.has_key(b'price'):
                iv._readPriceForItem(iCtx, isection, item.compactDescr)
            elif item.priceGroup:
                if item.priceGroup not in cache.priceGroupNames:
                    if IS_EDITOR:
                        continue
                    ix.raiseWrongXml(iCtx, b'priceGroup', b'unknown price group %s for item %s' % (
                     item.priceGroup, item.id))
                priceGroupId = cache.priceGroupNames[item.priceGroup]
                item.priceGroupTags = priceGroupsDict[priceGroupId].tags
                itemToPriceGroup[item.compactDescr] = priceGroupsDict[priceGroupId].compactDescr
                itemNotInShop = isection.readBool(b'notInShop', False)
                iv._copyPriceForItem(priceGroupsDict[priceGroupId].compactDescr, item.compactDescr, itemNotInShop)
            else:
                ix.raiseWrongXml(iCtx, b'priceGroup', b'no price for item %s' % item.id)

        if IS_EDITOR:
            refs = gsection.references
            if len(refs) == 1:
                group.editorData.sourceXml = refs[0]
                sourceFiles.add(refs[0])
            itemPrototype.edIsPrototype = True
            group.editorData.itemRefs = [UnintrusiveWeakRef(item) for item in groupItems]
            cache.editorData.groups[itemType].append(group)

    if IS_EDITOR:
        cache.editorData.sourceFiles[itemType] = list(sourceFiles)
    _addEmptyItem(itemCls, storage, itemSectionName)
    return


def _addEmptyItem(itemCls, storage, itemSectionName):
    if IS_EDITOR and itemSectionName != b'style':
        return
    item = itemCls()
    item.id = EMPTY_ITEM_ID
    storage[EMPTY_ITEM_ID] = item
    return


def _readPriceGroups(cache, xmlCtx, section, sectionName, prices=None):
    if IS_EDITOR and section is None:
        return
    else:
        for tag, iSection in section.items():
            if tag != sectionName:
                continue
            priceGroup = cc.PriceGroup()
            priceGroup.id = ix.readInt(xmlCtx, iSection, b'id', 1)
            iCtx = (xmlCtx, b'id %s' % priceGroup.id)
            if priceGroup.id in cache.priceGroups:
                ix.raiseWrongXml(iCtx, b'id', b'duplicate price group id')
            priceGroup.name = intern(ix.readString(iCtx, iSection, b'name'))
            if priceGroup.name in cache.priceGroupNames:
                ix.raiseWrongXml(iCtx, b'id', b'duplicate price group name "%s"' % priceGroup.name)
            priceGroup.notInShop = iSection.readBool(b'notInShop', False)
            iv._readPriceForItem(iCtx, iSection, priceGroup.compactDescr, prices)
            if iSection.has_key(b'tags'):
                tags = iSection.readString(b'tags').split()
                priceGroup.tags = frozenset(intern(tag) for tag in tags)
                for priceTag in priceGroup.tags:
                    cache.priceGroupTags.setdefault(priceTag, []).append(priceGroup)

            cache.priceGroupNames[priceGroup.name] = priceGroup.id
            cache.priceGroups[priceGroup.id] = priceGroup

        return


def _readFonts(cache, xmlCtx, section, sectionName):
    if IS_EDITOR:
        itemType = CUSTOMIZATION_CLASSES[cc.Font]
        sourceFiles = set()
        if section is None:
            return
    for tag, iSection in section.items():
        if tag != sectionName:
            continue
        font = cc.Font()
        font.id = ix.readInt(xmlCtx, iSection, b'id', 1)
        iCtx = (xmlCtx, b'id %s' % font.id)
        if font.id in cache.fonts:
            ix.raiseWrongXml(iCtx, b'id', b'duplicate price group id')
        font.texture = ix.readString(xmlCtx, iSection, b'texture')
        font.alphabet = ix.readString(xmlCtx, iSection, b'alphabet')
        if iSection.has_key(b'mask'):
            font.mask = ix.readString(xmlCtx, iSection, b'mask')
        cache.fonts[font.id] = font
        if IS_EDITOR:
            refs = iSection.references
            if len(refs) == 1:
                font.editorData.sourceXml = refs[0]
                sourceFiles.add(refs[0])

    if IS_EDITOR:
        cache.editorData.sourceFiles[itemType] = list(sourceFiles)
    return


def _readDefault(cache, xmlCtx, section, sectionName):
    for tag, iSection in section.items():
        if tag != sectionName:
            continue
        nation = ix.readString(xmlCtx, iSection, b'nation')
        colors = []
        scolors = iSection[b'colors']
        for idx, (ctag, _) in enumerate(scolors.items()):
            colors.append(iv._readColor((xmlCtx, (b'color {}').format(idx)), scolors, ctag))

        cache.defaultColors[nations.INDICES[nation]] = tuple(colors)
        itemId = ix.readInt(xmlCtx, iSection, b'insignia_id')
        cache.defaultInsignias[nations.INDICES[nation]] = itemId
        itemId = ix.readInt(xmlCtx, iSection, b'emblem_id')
        cache.defaultPlayerEmblems[nations.INDICES[nation]] = itemId
        if iSection.has_key(b'top_vehicle'):
            topVehicle = ix.readString(xmlCtx, iSection, b'top_vehicle')
            cache.topVehiclesByNation[nation] = topVehicle

    return


def readQuestProgression(cache, xmlCtx, section, sectionName):
    cls = cc.QuestProgressForCustomization
    for gname, gsection in section.items():
        if gname != sectionName:
            continue
        styleId = ix.readInt(xmlCtx, gsection, b'id')
        if styleId not in cache.styles:
            ix.raiseWrongXml(xmlCtx, b'id', (b'Style id {} not found ').format(styleId))
        style = cache.styles[styleId]
        finishTime = readUTC(gsection, b'finishTime', DEFAULT_QUEST_FINISH_TIME)
        unlockChains = {}
        for tname, psection in gsection[b'unlockChains'].items():
            groupId = 0
            try:
                groupId = int(tname[len(PREFIX):])
            except:
                ix.raiseWrongXml(xmlCtx, tname, (b'Wrong section format use: {}').format(b'cust_progress_{groupID}'))

            token = serializeToken(styleId, groupId)
            if token in unlockChains:
                ix.raiseWrongXml(xmlCtx, tname, (b'GroupId dublicate id {}').format(groupId))
            concurrent = ix.readBool(xmlCtx, psection, b'concurrent', False)
            items = {}
            unlockChains[token] = (
             items, concurrent)
            for lname, lsection in psection.items():
                if lname != b'item':
                    continue
                count = ix.readInt(xmlCtx, lsection, b'level')
                levelFinishTime = readUTC(lsection, b'finishTime', finishTime)
                unlockItems = {}
                for subSectionName, oSection in lsection.items():
                    if oSection.has_key(b'id'):
                        c11nType = CustomizationNamesToTypes[subSectionName.upper()]
                        unlockItems[c11nType] = ix.readTupleOfPositiveInts(xmlCtx, oSection, b'id')
                        if not all(False for id in unlockItems[c11nType] if id not in cache.itemTypes[c11nType]):
                            ix.raiseWrongXml(xmlCtx, tname, (b'id for {} not in cache').format(subSectionName))

                if count < 0:
                    ix.raiseWrongXml(xmlCtx, tname, b'level < 0')
                for c11nType, ids in viewitems(unlockItems):
                    for id in ids:
                        item = cache.itemTypes[c11nType][id]
                        if count > 0:
                            item.requiredToken = token
                            item.requiredTokenCount = count
                        if not IS_UE_EDITOR:
                            item.tags = item.tags.union(frozenset((ItemTags.QUESTS_PROGRESSION,)))
                        cache.itemToQuestProgressionStyle[item.compactDescr] = style

                items.update({count: (unlockItems, levelFinishTime)})

        yield (
         style, cls(styleId, unlockChains))

    return


def readFlagEnum(xmlCtx, section, subsectionName, enumClass, defaultValue=None):
    result = 0
    if not section.has_key(subsectionName) and defaultValue is not None:
        return defaultValue
    else:
        for value in ix.readNonEmptyString(xmlCtx, section, subsectionName).split():
            valueInt = getattr(enumClass, value.upper(), None)
            if valueInt is None:
                ix.raiseWrongSection(xmlCtx, subsectionName)
            result |= valueInt

        return result


def readEnum(xmlCtx, section, subsectionName, enumClass, defaultValue=None):
    if not section.has_key(subsectionName) and defaultValue is not None:
        return defaultValue
    else:
        value = ix.readNonEmptyString(xmlCtx, section, subsectionName).upper()
        valueInt = getattr(enumClass, value, None)
        if valueInt is None:
            ix.raiseWrongXml(xmlCtx, subsectionName, b'Invalid enum value %s in class %s' % (value, enumClass))
        return valueInt


def readEmissionParams(target, xmlCtx, section):
    if section.has_key(b'emission'):
        emissionSection = ix.getSubsection(xmlCtx, section, b'emission')
        if target.emissionParams is not None:
            target.emissionParams = deepcopy(target.emissionParams)
        else:
            target.emissionParams = cc.EmissionParams()
        if emissionSection.has_key(b'emission_texture'):
            target.emissionParams.emissionTexture = emissionSection.readString(b'emission_texture')
        if emissionSection.has_key(b'emission_deferred_power'):
            target.emissionParams.emissionDeferredPower = emissionSection.readFloat(b'emission_deferred_power')
        if emissionSection.has_key(b'emission_forward_power'):
            target.emissionParams.emissionForwardPower = emissionSection.readFloat(b'emission_forward_power')
    return


__xmlReaders = {(cc.PaintItem): (PaintXmlReader()), 
   (cc.DecalItem): (DecalXmlReader()), 
   (cc.ProjectionDecalItem): (ProjectionDecalXmlReader()), 
   (cc.CamouflageItem): (CamouflageXmlReader()), 
   (cc.ModificationItem): (ModificationXmlReader()), 
   (cc.StyleItem): (StyleXmlReader()), 
   (cc.InsigniaItem): (InsigniaXmlReader()), 
   (cc.PersonalNumberItem): (PersonalNumberXmlReader()), 
   (cc.SequenceItem): (SequenceXmlReader()), 
   (cc.AttachmentItem): (AttachmentXmlReader()), 
   (cc.StatTrackerItem): (StatTrackerXmlReader())}
