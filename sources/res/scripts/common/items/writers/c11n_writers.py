from collections import namedtuple
from constants import IS_EDITOR
import Math, ResMgr, typing, re
from string import lower
import items.vehicles as iv
from items import _xml, parseIntCompactDescr
from serializable_types.types import C11nSerializationTypes as _C11nSerializationTypes
from soft_exception import SoftException
from items.components.c11n_constants import SeasonType, DecalType, CamouflageTilingType, CustomizationType, RENT_DEFAULT_BATTLES, EMPTY_ITEM_ID, ProjectionDecalType, CustomizationTypeNames, DEFAULT_SCALE_FACTOR_ID, DEFAULT_GLOSS, DEFAULT_METALLIC, DEFAULT_SCALE, DEFAULT_ROTATION, DEFAULT_POSITION, DEFAULT_FORWARD_EMISSION, DEFAULT_DEFERRED_EMISSION, DEFAULT_EMISSION_ANIMATION_SPEED, DEFAULT_NORMAL_MAP_FACTOR, DEFAULT_NORMAL_MAX_LOD
from items.components.c11n_components import StyleItem, ApplyArea
from items.customizations import FieldTypes, FieldFlags, FieldType, SerializableComponent, SerializationException
from items.type_traits import equalComparator
from nations import NAMES
from items.utils import getDefaultGlossTexture
if IS_EDITOR:
    from reflection_framework.helpers.editor_shared_properties import isPropertyShared
else:
    isPropertyShared = lambda instance, path: False
if IS_EDITOR:
    import UECommon
    from items.customizations import getEditorOnlySection

def findOrCreate(section, subsectionName):
    if not section.has_key(subsectionName):
        return section.createSection(subsectionName)
    else:
        return section[subsectionName]

    return


def resizeSection(section, newSize, newName):
    if len(section) == newSize:
        return False
    while len(section) > newSize:
        lastSection = section.child(len(section) - 1)
        section.deleteSection(lastSection)

    while len(section) < newSize:
        section.createSection(newName(len(section)))

    return True


def saveCustomizationItems(cache, folder):
    writeItemType(PaintXmlWriter(), cache, folder, b'paint')
    writeItemType(DecalXmlWriter(), cache, folder, b'decal')
    writeItemType(ProjectionDecalXmlWriter(), cache, folder, b'projection_decal')
    writeItemType(CamouflageXmlWriter(), cache, folder, b'camouflage')
    writeItemType(ModificationXmlWriter(), cache, folder, b'modification')
    writeItemType(StyleXmlWriter(), cache, folder, b'style')
    writeItemType(PersonalNumberXmlWriter(), cache, folder, b'personal_number')
    writeItemType(InsigniaXmlWriter(), cache, folder, b'insignia')
    writeFontType(FontXmlWriter(), cache, folder, b'font')
    writeItemType(SequenceXmlWriter(), cache, folder, b'sequence')
    writeItemType(AttachmentXmlWriter(), cache, folder, b'attachment')
    UECommon.writeAllLocalizationChanges()
    return


class GroupSectionPicker(object):

    def __init__(self, group):
        self.ids = set(map((lambda itemRef: itemRef().id), group.editorData.itemRefs))
        self.name = group.name
        return

    def __call__(self, gsections):
        bestSection = None
        bestMatch = 0
        for gsection in gsections:
            match = 0
            for iname, isection in gsection.items():
                if isection.has_key(b'id'):
                    id = isection[b'id'].asInt
                    if id in self.ids:
                        match += 1

            if match > bestMatch:
                bestMatch = match
                bestSection = gsection

        if bestSection is not None:
            return bestSection
        else:
            for gsection in gsections:
                if gsection.readString(b'name') == self.name:
                    return gsection

            return


def writeItemType(writer, cache, folder, itemName, endGroupWriter=None):
    refsections = {}
    changedRefs = set()
    fileListRewriters = {}
    groups = cache.editorData.groups[CUSTOMIZATION_ITEMS_NAME_TO_TYPE[itemName]]
    sourceFiles = cache.editorData.sourceFiles[CUSTOMIZATION_ITEMS_NAME_TO_TYPE[itemName]]
    for sourceXml in sourceFiles:
        rootSection = ResMgr.openSection(sourceXml)
        listRewriter = _xml.ListRewriter(rootSection, b'itemGroup')
        fileListRewriters[sourceXml] = listRewriter
        refsections[sourceXml] = rootSection

    for group in groups:
        if group.editorData.sourceXml is None:
            raise SoftException((b'Group {} has no sourceXml, data format has changed?').format(group.name))
        sourceXml = group.editorData.sourceXml
        listRewriter = fileListRewriters.get(sourceXml, None)
        if listRewriter is None:
            raise SoftException((b'Group {} sourceXml not found in fileListRewriters').format(group.name))
        groupSection = listRewriter.next(sectionPicker=GroupSectionPicker(group))
        changed = writeGroup(writer, group, groupSection, itemName, endGroupWriter)
        if changed:
            changedRefs.add(sourceXml)

    for ref in fileListRewriters:
        listRewriter = fileListRewriters[ref]
        changed = listRewriter.flush()
        if changed:
            changedRefs.add(ref)

    for ref, refsection in refsections.items():
        if ref in changedRefs:
            refsection.save()

    return


def writeGroup(itemWriter, group, groupSection, itemName, endGroupWriter=None):
    prototype = group.itemPrototype
    changed = _xml.rewriteString(groupSection, b'name', group.name, defaultValue=b'')
    changed |= itemWriter.write(prototype, groupSection, None)
    listRewriter = _xml.ListRewriter(groupSection, itemName)
    for itemRef in group.editorData.itemRefs:
        item = itemRef()
        if item.id == EMPTY_ITEM_ID:
            continue
        itemSection = listRewriter.next((lambda s, i=item: s[b'id'].asInt == i.id))
        changed |= itemWriter.write(item, itemSection, prototype)

    if endGroupWriter:
        endGroupWriter.write(groupSection)
    changed |= listRewriter.flush()
    return changed


def writeFontType(writer, cache, folder, itemName):

    def parseSourceSection(fontFilesPathes, fontItems, changedRefs):
        fontRefs = {}
        fontsSections = {}
        for fontFile in fontFilesPathes:
            refSection = ResMgr.openSection(fontFile)
            if refSection is None:
                _xml.raiseWrongXml(None, refSection, b"can't find datasection")
            fontRefs[fontFile] = refSection
            for name, isection in refSection.items():
                if isection.has_key(b'id'):
                    id = isection[b'id'].asInt
                    if id in fontsSections.keys():
                        raise SoftException((b'Some font items have the same id {}.').format(id))
                    if id in fontItems.keys():
                        fontsSections[id] = isection
                    else:
                        refSection.deleteSection(isection)
                        changedRefs.add(refSection)

            return (
             fontRefs, fontsSections)

        return

    sourceFiles = cache.editorData.sourceFiles[CUSTOMIZATION_ITEMS_NAME_TO_TYPE[itemName]]
    if len(sourceFiles) == 0:
        return
    else:
        if sourceFiles is None:
            raise SoftException((b'Item {} has no sourceXml, data format has changed?').format(itemName + str(id)))
        items = cache.fonts
        changedRefs = set()
        refSections, fontsSections = parseSourceSection(sourceFiles, items, changedRefs)
        for id, item in items.items():
            sourceFile = item.editorData.sourceXml
            if sourceFile not in refSections.keys():
                raise SoftException((b"writeFontType: Couldn't find file {} ").format(sourceFile))
            sourceRef = refSections[sourceFile]
            if id not in fontsSections.keys():
                fontsSections[id] = sourceRef.createSection(itemName)
                _xml.rewriteInt(fontsSections[id], b'id', id)
            isection = fontsSections[id]
            changed = writer.write(item, isection)
            if changed:
                changedRefs.add(sourceRef)

        for refsection in changedRefs:
            refsection.save()

        return


def _natkey(s):

    def convert(t):
        try:
            return int(t)
        except ValueError:
            return t.lower()

        return

    return map(convert, re.split(b'([0-9]+)', s))


def natsorted(seq):
    return sorted(seq, key=_natkey)


class VehicleFilterTagsConvertor(object):

    def convertToString(self, valuesList):
        result = (b' ').join(natsorted(valuesList))
        return result


class VehicleFilterLevelConvertor(object):

    def convertToString(self, valuesList):
        result = (b' ').join(map(str, sorted(valuesList)))
        return result


class VehicleFilterNationConvertor(object):

    def convertToString(self, valuesList):
        result = (b' ').join(natsorted(map((lambda item: NAMES[item]), valuesList)))
        return result


class VehicleFilterVehicleConvertor(object):

    def convertToString(self, valuesList):
        from items.vehicles import g_list

        def getTankName(vehCompactDesc):
            tankName = b''
            _, nationId, vehId = parseIntCompactDescr(vehCompactDesc)
            basicInfo = g_list.getList(nationId)[vehId]
            if basicInfo is not None:
                tankName = basicInfo.name
            return tankName

        result = (b' ').join(natsorted(map((lambda item: getTankName(item)), valuesList)))
        return result


class StringFilterConvertor(object):

    def convertToString(self, valuesList):
        result = (b' ').join(natsorted(valuesList))
        return result


class IntegerFilterConvertor(object):

    def convertToString(self, valuesList):
        result = (b' ').join(map(str, sorted(valuesList)))
        return result


class BoolFilterConvertor(object):

    def convertToString(self, valuesList):
        return str(valuesList)


DECAL_TYPE_STRING = {(DecalType.EMBLEM): b'EMBLEM', 
   (DecalType.INSCRIPTION): b'INSCRIPTION'}

class ItemsFilterDecalTypeConvertor(object):

    def convertToString(self, valuesList):

        def getDecalTypeMame(typeId):
            return DECAL_TYPE_STRING[typeId]

        result = (b' ').join(natsorted(map((lambda item: getDecalTypeMame(item)), valuesList)))
        return result


Description = namedtuple(b'FiltedFiels', (b'section', b'attributeName', b'convertor', b'defaultValue'))
VEHICLE_FILTER_VALUE_DESCRIPTION = (
 Description(b'nations', b'nations', VehicleFilterNationConvertor(), b''),
 Description(b'tags', b'tags', VehicleFilterTagsConvertor(), b''),
 Description(b'levels', b'levels', VehicleFilterLevelConvertor(), b''),
 Description(b'vehicles', b'vehicles', VehicleFilterVehicleConvertor(), b''))
ITEMS_FILTER_VALUE_DESCRIPTION = (
 Description(b'id', b'ids', IntegerFilterConvertor(), b'0'),
 Description(b'itemGroupName', b'itemGroupNames', StringFilterConvertor(), b''),
 Description(b'tags', b'tags', StringFilterConvertor(), b''),
 Description(b'type', b'types', ItemsFilterDecalTypeConvertor(), b'-1'),
 Description(b'historical', b'edCustomizationDisplayTypes', IntegerFilterConvertor(), b'0'))
FILTER_ID_NAME = {(CustomizationType.PROJECTION_DECAL): b'projection_decal', 
   (CustomizationType.PERSONAL_NUMBER): b'personal_number', 
   (CustomizationType.DECAL): b'decal'}
ALTERNATE_TO_NAME = {(CustomizationType.DECAL): b'decal', 
   (CustomizationType.PROJECTION_DECAL): b'projection_decal', 
   (CustomizationType.PAINT): b'paint', 
   (CustomizationType.CAMOUFLAGE): b'camouflage', 
   (CustomizationType.MODIFICATION): b'modification', 
   (CustomizationType.PERSONAL_NUMBER): b'personal_number'}
CUSTOMIZATION_ITEMS_TYPE_TO_NAME = {(CustomizationType.DECAL): b'decal', 
   (CustomizationType.PROJECTION_DECAL): b'projection_decal', 
   (CustomizationType.PAINT): b'paint', 
   (CustomizationType.CAMOUFLAGE): b'camouflage', 
   (CustomizationType.MODIFICATION): b'modification', 
   (CustomizationType.PERSONAL_NUMBER): b'personal_number', 
   (CustomizationType.STYLE): b'style', 
   (CustomizationType.INSIGNIA): b'insignia', 
   (CustomizationType.FONT): b'font', 
   (CustomizationType.ATTACHMENT): b'attachment', 
   (CustomizationType.SEQUENCE): b'sequence'}
CUSTOMIZATION_ITEMS_NAME_TO_TYPE = {v: k for k, v in CUSTOMIZATION_ITEMS_TYPE_TO_NAME.items()}

def saveItemFilter(filter, section, filterName, valueDescription):
    changed = False
    includeCount = len(filter.include)
    excludeCount = len(filter.exclude)
    filterSection = findOrCreate(section, filterName)

    def countFilters(filterSection):
        includeCount = 0
        excludeCount = 0
        for iname, isection in filterSection.items():
            if iname == b'include':
                includeCount += 1
            elif iname == b'exclude':
                excludeCount += 1

        return (
         includeCount, excludeCount)

    includeSectCnt, excludeSectCnt = countFilters(filterSection)
    if includeSectCnt != includeCount or excludeSectCnt != excludeCount:
        changed = True
        while len(filterSection) > 0:
            lastSection = filterSection.child(len(filterSection) - 1)
            filterSection.deleteSection(lastSection)

        def createSections(parentSection, sectionName, count):
            while count > 0:
                parentSection.createSection(sectionName)
                count -= 1

            return

        createSections(filterSection, b'include', includeCount)
        createSections(filterSection, b'exclude', excludeCount)

    def saveFilter(filterSection, filterName, filters, valueDescription):
        if len(filters) == 0:
            return False
        changed = False
        index = 0

        def saveFilterValue(subFilterSection, valueSectionName, valueHolder, valuedescr):
            listOfValues = getattr(valueHolder, valuedescr.attributeName)
            if listOfValues is None:
                return False
            else:
                needWrite = True
                if isinstance(listOfValues, bool):
                    needWrite = listOfValues
                elif len(listOfValues) == 0:
                    needWrite = False
                if needWrite is False:
                    if subFilterSection.has_key(valueSectionName):
                        subFilterSection.deleteSection(valueSectionName)
                        return True
                else:
                    strValue = valuedescr.convertor.convertToString(listOfValues)
                    if strValue is None:
                        return False
                    return _xml.rewriteString(subFilterSection, valueSectionName, strValue, valuedescr.defaultValue)
                return False

        for iname, isection in filterSection.items():
            if iname == filterName:
                filterValue = filters[index]
                for valuedescr in valueDescription:
                    changed |= saveFilterValue(isection, valuedescr.section, filterValue, valuedescr)

                index += 1

        return changed

    changed |= saveFilter(filterSection, b'include', filter.include, valueDescription)
    changed |= saveFilter(filterSection, b'exclude', filter.exclude, valueDescription)
    return changed


def writeLocalizationProperty(item, generalLocalizationKey, propname, keyStr, propType, xmlSectionName, section):
    changed = False
    propStr = getattr(item, propname, None)
    if propStr is None:
        return changed
    else:
        key = getattr(item.i18n, keyStr, None)
        if key is not None and len(key) > 0:
            if UECommon.getTranslatedText(key) != propStr:
                UECommon.addChangedData(b'vehicle_customization', key, str(propStr))
        elif len(propStr) > 0:
            generalKey = generalLocalizationKey[0]
            if generalKey is None or len(generalKey) == 0:
                nameKey = getattr(item.i18n, b'userKey', b'')
                parts = nameKey.split(b'/')
                if len(parts) > 1:
                    if parts[:-1] is b'label' or parts[:-1] is b'name':
                        parts.pop()
                    generalKey = (b'/').join(parts)
                    generalLocalizationKey[0] = generalKey
            key = generalKey + b'/' + propType
            setattr(item.i18n, keyStr, key)
            changed |= rewriteString(section, xmlSectionName, item, b'i18n.' + keyStr, b'')
            UECommon.addChangedData(b'vehicle_customization', key, propStr)
        return changed


def writeLocalization(item, section):
    changed = False
    if getattr(item, b'shortDescriptionProp', None) is None:
        return changed
    else:
        generalLocalizationKey = [
         b'']
        keysGeneralPart = getattr(item, b'localizationKeysGeneralPart', None)
        if keysGeneralPart is not None:
            if len(keysGeneralPart) == 0:
                raise SoftException(b'Key field must be filled')
            generalLocalizationKey = [
             b'#vehicle_customization:' + keysGeneralPart]
        changed |= writeLocalizationProperty(item, generalLocalizationKey, b'nameProp', b'userKey', b'name', b'userString', section)
        changed |= writeLocalizationProperty(item, generalLocalizationKey, b'shortDescriptionProp', b'descriptionKey', b'description', b'description', section)
        changed |= writeLocalizationProperty(item, generalLocalizationKey, b'longDescriptionProp', b'longDescriptionSpecialKey', b'longDescription', b'longDescriptionSpecial', section)
        return changed


class BaseCustomizationItemXmlWriter(object):

    def writeBase(self, item, section):
        changed = False
        changed |= rewriteInt(section, b'id', item, b'id')
        changed |= rewriteString(section, b'texture', item, b'texture', b'')
        changed |= writeLocalization(item, section)
        return changed

    def writeBaseGroup(self, item, section):
        changed = False
        if _needWrite(item, b'season'):
            enumValue = encodeEnum(SeasonType, item.season)
            if enumValue is None:
                enumValue = encodeFlagEnum(SeasonType, item.season)
            if enumValue == b'all':
                enumValue = enumValue.upper()
            changed |= _xml.rewriteString(section, b'season', enumValue, b'undefined')
        else:
            section.deleteSection(b'season')
        changed |= rewriteInt(section, b'historical', item, b'customizationDisplayType', -1)
        changed |= rewriteTags(section, item)
        changed |= rewriteString(section, b'priceGroup', item, b'priceGroup', b'')
        if not _needWrite(item, b'filter'):
            changed |= section.deleteSection(b'filter')
        else:
            includeCount = len(item.filter.include)
            excludeCount = len(item.filter.exclude)
            needWriteFilter = True
            if includeCount == 0 and excludeCount == 0:
                needWriteFilter = False
                if section.has_key(b'vehicleFilter'):
                    section.deleteSection(b'vehicleFilter')
            if needWriteFilter:
                changed |= saveItemFilter(item.filter, section, b'vehicleFilter', VEHICLE_FILTER_VALUE_DESCRIPTION)
        changed |= rewriteString(section, b'requiredToken', item, b'requiredToken', b'')
        changed |= rewriteInt(section, b'maxNumber', item, b'maxNumber', 0)
        return changed


class PaintXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            color = item.color
            c_a, c_r, c_g, c_b = (0, 0, 0, 0)
            if color > 0:
                c_a = color >> 24 & 255
                c_r = color >> 16 & 255
                c_g = color >> 8 & 255
                c_b = color & 255
            color = Math.Vector4(c_b, c_g, c_r, c_a)
            if _needWrite(item, b'color'):
                changed |= _xml.rewriteVector4(section, b'color', color)
            else:
                changed |= section.deleteSection(b'color')
            changed |= rewriteFloat(section, b'gloss', item, b'gloss', 0.0)
            changed |= rewriteFloat(section, b'metallic', item, b'metallic', 0.0)
        else:
            changed |= _xml.rewriteString(section, b'userString', self._encodeGroup(item.colorGroup))
        changed |= self.writeBaseGroup(item, section)
        return changed

    @staticmethod
    def _encodeGroup(group):
        return (b'#vehicle_customization:repaint/{}').format(group)


class DecalXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        changed |= rewriteBool(section, b'mirror', item, b'canBeMirrored')
        changed |= self.writeBaseGroup(item, section)
        if _needWrite(item, b'type'):
            if group:
                changed |= section.deleteSection(b'type')
            else:
                changed |= _xml.rewriteString(section, b'type', encodeEnum(DecalType, item.type))
                if item.type == 0:
                    changed |= section.deleteSection(b'userString')
                else:
                    changed |= _xml.rewriteString(section, b'userString', self._encodeGroup(item.type, item.decalGroup))
        else:
            changed |= section.deleteSection(b'type')
        return changed

    @staticmethod
    def _encodeGroup(itemType, group):
        return (b'#vehicle_customization:{}/{}').format(encodeEnum(DecalType, itemType), group)


class ProjectionDecalXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        changed |= rewriteBool(section, b'mirror', item, b'canBeMirroredHorizontally')
        changed |= rewriteString(section, b'glossTexture', item, b'glossTexture', getDefaultGlossTexture())
        changed |= rewriteInt(section, b'scaleFactorId', item, b'scaleFactorId', DEFAULT_SCALE_FACTOR_ID)
        changed |= self.writeBaseGroup(item, section)
        changed |= rewriteEmissionSettings(section, item.emissionSettings)
        if not group:
            changed |= _xml.rewriteString(section, b'userString', self._encodeGroup(item.projectionDecalGroup))
        return changed

    @staticmethod
    def _encodeGroup(group):
        return (b'#vehicle_customization:projection_decals/{}').format(group)


class CamouflageXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteCamouflageScales(section, item)
        elif item.camoTypeIndex >= 0:
            changed |= _xml.rewriteString(section, b'userString', item.getCamoTypesTranslationKeys()[item.camoTypeIndex])
        changed |= self.writeBaseGroup(item, section)
        if group:
            changed |= rewriteFloat(section, b'invisibilityFactor', item, b'invisibilityFactor', 1.0)
            changed |= rewriteFloat(section, b'exclusionImpact', item, b'exclusionImpact', 1.0)
            changed |= rewriteBool(section, b'forceUv0', item, b'forceUv0', False)
            changed |= rewritePalettes(section, item)
            changed |= rewriteCamouflageRotation(section, item)
            changed |= rewriteCamouflageTiling(section, item)
            changed |= rewriteCamouflageTilingSettings(section, item)
            changed |= rewriteCamouflageGlossMetallicSettings(section, item)
            changed |= rewriteEmissionSettings(section, item.emissionSettings)
            changed |= rewriteNormalSettings(section, item.normalSettings)
        return changed


def rewriteEffects(item, section):
    if not _needWrite(item, b'effects'):
        return section.deleteSection(b'effects')
    else:
        changed = False
        effectsSection = findOrCreate(section, b'effects')
        changed |= resizeSection(effectsSection, 2, (lambda id: b'effect'))
        index = 0

        def writeEffectValue(effectSection, type, value):
            result = _xml.rewriteString(effectSection, b'type', type)
            result |= _xml.rewriteFloat(effectSection, b'value', value)
            return result

        while index < 2:
            effectSection = effectsSection.child(index)
            typeSection = findOrCreate(effectSection, b'type')
            effectType = typeSection.asString
            if effectType is None or effectType == b'':
                if index == 0:
                    effectType = b'paint_age'
                if index == 1:
                    effectType = b'paint_fading'
            effectValue = 0
            if effectType == b'paint_age':
                effectValue = item.strength
            elif effectType == b'paint_fading':
                effectValue = item.fading
            changed |= writeEffectValue(effectSection, effectType, effectValue)
            index += 1

        return changed


class ModificationXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteEffects(item, section)
        changed |= self.writeBaseGroup(item, section)
        return changed


class ComponentXmlSerializer(object):

    def __init__(self):
        super(ComponentXmlSerializer, self).__init__()
        return

    def encode(self, section, target, defaultValuesDict=None, deprecatedFieldsToWrite=None):
        return self.__encodeCustomType(section, None, target, defaultValuesDict, deprecatedFieldsToWrite)

    def __encodeCustomType(self, section, key, obj, defaultValuesDict=None, deprecatedFieldsToWrite=None, valueType=0):
        changed = False
        if key is None:
            objSection = section
        else:
            objSection = section[key]
            if objSection is None:
                objSection = section.createSection(key)
                changed = True
        for fieldName, fieldType in obj.fields.iteritems():
            if fieldType.flags & FieldFlags.DEPRECATED:
                continue
            if fieldType.flags & FieldFlags.NON_XML:
                continue
            value = getattr(obj, fieldName)
            lenght = 1
            if hasattr(value, b'__len__'):
                lenght = len(value)
            if value is not None and lenght > 0:
                changed |= self.__encodeValue(objSection, fieldName, value, fieldType, defaultValuesDict, deprecatedFieldsToWrite, obj.customType)
            else:
                changed |= objSection.deleteSection(fieldName)

        return changed

    def __encodeArray(self, section, key, value, fieldType, defaultValuesDict=None, deprecatedFieldsToWrite=None, valueType=0):
        changed = False
        if key is None:
            array = section
        else:
            array = section[key]
            if array is None:
                array = section.createSection(key)
                changed = True
        for index, (name, child) in list(enumerate(array.items())):
            if name != b'item' or IS_EDITOR and fieldType.saveTag and name != fieldType.saveTag.format(index):
                array.deleteSection(child)
                changed = True

        with _xml.ListRewriter(array, b'item') as children:
            for index, item in enumerate(value):
                preferred = None
                try:
                    if b'id' in item:
                        preferred = lambda s: s.readInt(b'id') == item.id
                except TypeError:
                    pass

                tagPath = fieldType.saveTag.format(index) if IS_EDITOR and fieldType.saveTag else None
                child = children.next(preferred, path=tagPath)
                changed |= self.__encodeValue(child, None, item, fieldType, defaultValuesDict, deprecatedFieldsToWrite, valueType)

        return changed

    def __encodeValue(self, section, key, value, fieldType, defaultValuesDict=None, deprecatedFieldsToWrite=None, valueType=0):
        if deprecatedFieldsToWrite:
            deprecatedFields = deprecatedFieldsToWrite.get(valueType)
            if deprecatedFields and key in deprecatedFields:
                return False
        defaultValue = None
        if defaultValuesDict:
            defaultValue = defaultValuesDict.get(key)
        if IS_EDITOR and fieldType.flags & FieldFlags.SAVE_AS_EDITOR_ONLY:
            section = getEditorOnlySection(section, True)
        if fieldType.type == FieldTypes.VARINT:
            return _xml.rewriteInt(section, key, value, defaultValue)
        else:
            if fieldType.type == FieldTypes.FLOAT:
                return _xml.rewriteFloat(section, key, value, defaultValue)
            if fieldType.type == FieldTypes.APPLY_AREA_ENUM:
                if fieldType.flags & FieldFlags.SAVE_AS_STRING:
                    return _xml.rewriteString(section, key, encodeFlagEnum(ApplyArea, value).upper(), defaultValue)
                return _xml.rewriteInt(section, key, value, defaultValue)
            if fieldType.type == FieldTypes.TAGS:
                return _xml.rewriteString(section, key, (b' ').join(value), defaultValue)
            if fieldType.type == FieldTypes.STRING:
                return _xml.rewriteString(section, key, value, defaultValue)
            if fieldType.type == FieldTypes.OPTIONS_ENUM:
                return _xml.rewriteInt(section, key, value, defaultValue)
            if fieldType.type & FieldTypes.TYPED_ARRAY:
                ft = fieldType._asdict()
                ft[b'type'] ^= FieldTypes.TYPED_ARRAY
                return self.__encodeArray(section, key, value, FieldType(**ft), defaultValuesDict, deprecatedFieldsToWrite, valueType)
            if fieldType.type >= FieldTypes.CUSTOM_TYPE_OFFSET:
                return self.__encodeCustomType(section, key, value, defaultValuesDict, deprecatedFieldsToWrite, valueType)
            raise SerializationException(b'Unsupported field type %d' % (fieldType.type,))
            return


class StyleXmlWriter(BaseCustomizationItemXmlWriter):
    __outfitSerializer = ComponentXmlSerializer()

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteBool(section, b'isRent', item, b'isRent')
            if item.isRent:
                changed |= rewriteInt(section, b'rentCount', item, b'rentCount', RENT_DEFAULT_BATTLES)
            else:
                changed |= section.deleteSection(b'rentCount')
            if item.modelsSet is None or item.modelsSet == b'':
                changed |= section.deleteSection(b'modelsSet')
            else:
                changed |= rewriteString(section, b'modelsSet', item, b'modelsSet', b'default')
            changed |= self.__writeOutfits(item.outfits, section)
            changed |= self.__writeFiltersItems(item.itemsFilters, section)
            changed |= self.__writeAlternateItems(item.alternateItems, section)
            changed |= self.__writeDependencies(item.dependencies, section)
            changed |= self.__write3dProgression(item.styleProgressions, section)
        else:
            changed |= _xml.rewriteString(section, b'userString', self._encodeGroup(item.styleGroup))
        changed |= self.writeBaseGroup(item, section)
        return changed

    def __writeOutfits(self, outfits, section):
        singleOutfit = None
        seasonsMask = 0
        for season, outfit in outfits.iteritems():
            seasonsMask |= season
            if singleOutfit is None:
                singleOutfit = outfit
                continue
            if outfit != singleOutfit:
                singleOutfit = None
                break

        if seasonsMask != SeasonType.ALL:
            singleOutfit = None
        changed = False
        with _xml.ListRewriter(section, b'outfits/outfit') as oSections:
            if singleOutfit is None:
                for season, outfit in outfits.iteritems():
                    changed |= self.__writeOutfit(oSections, season, outfit)

            else:
                changed |= self.__writeOutfit(oSections, seasonsMask, singleOutfit)
            changed |= oSections.changed
        return changed

    def __writeOutfit(self, oSections, season, outfit):
        changed = False
        seasonName = encodeEnum(SeasonType, season)
        oSection = oSections.next((lambda s: s.readString(b'season').lower() == seasonName))
        changed |= _xml.rewriteString(oSection, b'season', seasonName)
        defaultValuesDict = {b'styleProgressionLevel': 0, 
           b'slotId': 0, 
           b'scaleFactorId': DEFAULT_SCALE_FACTOR_ID, 
           b'options': 0, 
           b'overrideDefaultAttachments': 0}
        for projectionDecal in outfit.projection_decals:
            if projectionDecal.editorData.decalType == ProjectionDecalType.POSITION:
                projectionDecal.tags = None
                projectionDecal.scaleFactorId = None
                projectionDecal.options = None

                def checkDefault(val, defaultVal):
                    if tuple(val) != defaultVal:
                        return val
                    else:
                        return

                projectionDecal.position = checkDefault(projectionDecal.position, DEFAULT_POSITION)
                projectionDecal.rotation = checkDefault(projectionDecal.rotation, DEFAULT_ROTATION)
                projectionDecal.scale = checkDefault(projectionDecal.scale, DEFAULT_SCALE)
                defaultValuesDict[b'showOn'] = encodeFlagEnum(ApplyArea, ApplyArea.NONE).upper()
                defaultValuesDict[b'doubleSided'] = 0
            else:
                projectionDecal.position = None
                projectionDecal.rotation = None
                projectionDecal.scale = None
                projectionDecal.doubleSided = None
                projectionDecal.showOn = None

        deprecatedFieldsToWrite = {(_C11nSerializationTypes.SEQUENCE): (b'position', b'rotation'), (_C11nSerializationTypes.ATTACHMENT): (b'position', b'rotation'), 
           (_C11nSerializationTypes.PROJECTION_DECAL): (b'tintColor', b'preview', b'progressionLevel'), 
           (_C11nSerializationTypes.DECAL): b'progressionLevel'}
        changed |= self.__outfitSerializer.encode(oSection, outfit, defaultValuesDict, deprecatedFieldsToWrite)
        return changed

    def __writeAlternateItems(self, alterItems, isection):
        changed = False
        if len(alterItems) == 0:
            if isection.has_key(b'alternateItems'):
                isection.deleteSection(b'alternateItems')
                changed |= True
        else:
            alternateItemsSection = isection[b'alternateItems']
            if alternateItemsSection is None:
                alternateItemsSection = isection.createSection(b'alternateItems')
                changed |= True
            childCount = len(alternateItemsSection)
            childIndex = childCount - 1
            currentItemsNames = (b' ').join(natsorted(map((lambda item: ALTERNATE_TO_NAME[item]), alterItems.keys())))
            while childIndex >= 0:
                childSection = alternateItemsSection.child(childIndex)
                sectionName = childSection.name
                if sectionName not in currentItemsNames:
                    alternateItemsSection.deleteSection(sectionName)
                    changed |= True
                childIndex -= 1

            for itemType, itemValues in alterItems.iteritems():
                alternateItemSectionName = ALTERNATE_TO_NAME[itemType]
                oSection = alternateItemsSection[alternateItemSectionName]
                if oSection is None:
                    oSection = alternateItemsSection.createSection(alternateItemSectionName)
                    changed |= True
                itemsValue = (b' ').join(map(str, sorted(itemValues)))
                changed |= _xml.rewriteString(oSection, b'id', itemsValue)

        return changed

    def __writeDependencies(self, dependencies, isection):
        changed = False
        collection = dependencies
        camouflagesCount = len(collection)
        if camouflagesCount == 0:
            if isection.has_key(b'dependencies'):
                isection.deleteSection(b'dependencies')
                changed |= True
        else:
            dependenciesSection = findOrCreate(isection, b'dependencies')
            changed |= resizeSection(dependenciesSection, camouflagesCount, (lambda id: b'camouflage'))
            sectionIndex = 0
            for camoId in sorted(collection.keys()):
                items = collection[camoId]
                camoSection = dependenciesSection.child(sectionIndex)
                changed |= resizeSection(camoSection, 1, (lambda id: b'id'))
                changed |= _xml.rewriteInt(camoSection, b'id', camoId)
                for childKey, idsList in items.iteritems():
                    childName = (b'{}').format(lower(CustomizationTypeNames[childKey]))
                    idsStr = (b' ').join(map(str, idsList))
                    changed |= _xml.rewriteString(camoSection, childName, idsStr)

                sectionIndex += 1

        return changed

    def __writeFiltersItems(self, filters, isection):
        changed = False
        if len(filters) == 0:
            if isection.has_key(b'itemFilters'):
                isection.deleteSection(b'itemFilters')
                changed |= True
        else:
            itemFiltersSection = isection[b'itemFilters']
            if itemFiltersSection is None:
                itemFiltersSection = isection.createSection(b'itemFilters')
                changed |= True
            for filterId, filterValue in filters.iteritems():
                filterName = FILTER_ID_NAME[filterId]
                changed |= saveItemFilter(filterValue, itemFiltersSection, filterName, ITEMS_FILTER_VALUE_DESCRIPTION)

        return changed

    def __write3dProgression(self, progression, isection):
        sectionName = b'styleProgressions'
        if progression is None or len(progression) == 0:
            if isection.has_key(sectionName):
                isection.deleteSection(sectionName)
                return True
            return False
        changed = False
        stagesCount = len(progression)
        if stagesCount == 0:
            if isection.has_key(sectionName):
                isection.deleteSection(sectionName)
                changed |= True
        else:
            progression3dSection = isection[sectionName]
            if progression3dSection is None:
                progression3dSection = isection.createSection(sectionName)
                changed |= True
            if stagesCount != len(progression3dSection):
                changed |= resizeSection(progression3dSection, stagesCount, (lambda id: b'stage'))
            stageIndex = 0
            for stageName, progressionValue in progression.iteritems():
                stageSection = progression3dSection.child(stageIndex)
                if b'materials' in progressionValue.keys():
                    materialsList = progressionValue[b'materials']
                    materialsStr = (b' ').join(materialsList)
                    changed |= _xml.rewriteString(stageSection, b'materials', materialsStr)
                if b'additionalOutfit' in progressionValue.keys():
                    outfit = progressionValue[b'additionalOutfit']
                    changed |= self.__writeOutfits(outfit, stageSection)
                stageIndex += 1

        return changed

    @staticmethod
    def _encodeGroup(group):
        return (b'#vehicle_customization:styles/{}').format(group)


class PersonalNumberXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteInt(section, b'digitsCount', item, b'digitsCount')
            changed |= rewriteInt(section, b'fontId', item, b'fontId')
            changed |= rewriteString(section, b'preview_texture', item, b'previewTexture')
        changed |= self.writeBaseGroup(item, section)
        return changed


class InsigniaXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteString(section, b'atlas', item, b'atlas', b'')
            changed |= rewriteString(section, b'alphabet', item, b'alphabet', b'')
            changed |= rewriteBool(section, b'canBeMirrored', item, b'canBeMirrored', False)
            changed |= rewriteEmissionSettings(section, item.emissionSettings)
        else:
            changed |= _xml.rewriteString(section, b'userString', self._encodeGroup(item.insigniaGroup))
        changed |= self.writeBaseGroup(item, section)
        return changed

    @staticmethod
    def _encodeGroup(group):
        return (b'#vehicle_customization:insignias/{}').format(group)


class AttachmentXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteString(section, b'name', item, b'name', b'')
            changed |= rewriteInt(section, b'sequenceId', item, b'sequenceId', -1)
            changed |= rewriteString(section, b'modelName', item, b'modelName', b'')
            changed |= rewriteString(section, b'hangarModelName', item, b'hangarModelName', b'', writeEmptySections=False)
            changed |= rewriteString(section, b'attachmentLogic', item, b'attachmentLogic', b'')
            changed |= rewriteBool(section, b'initialVisibility', item, b'initialVisibility', False)
        changed |= self.writeBaseGroup(item, section)
        return changed


class SequenceXmlWriter(BaseCustomizationItemXmlWriter):

    def write(self, item, section, group=None):
        changed = self.writeBase(item, section)
        if group:
            changed |= rewriteString(section, b'name', item, b'name', b'')
            changed |= rewriteString(section, b'sequenceName', item, b'sequenceName', b'')
        changed |= self.writeBaseGroup(item, section)
        return changed


def writeFontAlphabet(item):
    xmlPath = item.editorData.alphabet
    if xmlPath is None or len(xmlPath) == 0:
        return
    section = ResMgr.openSection(xmlPath)
    if section is None:
        return
    else:
        changed = False
        if len(section.items()) != len(item.editorData.alphabetList):
            changed |= resizeSection(section, len(item.editorData.alphabetList), (lambda id: b'glyph'))
        itemIndex = 0
        for name, isection in section.items():
            glyphItem = item.editorData.alphabetList[itemIndex]
            changed |= _xml.rewriteString(isection, b'name', glyphItem.name)
            vBegin = Math.Vector2(glyphItem.position[0], glyphItem.position[1])
            changed |= _xml.rewriteVector2(isection, b'begin', vBegin)
            vEnd = Math.Vector2(glyphItem.position[2], glyphItem.position[3])
            changed |= _xml.rewriteVector2(isection, b'end', vEnd)
            itemIndex += 1

        if changed:
            section.save()
        return


class FontXmlWriter(object):

    def write(self, item, section, group=None):
        changed = _xml.rewriteString(section, b'texture', item.texture)
        changed |= _xml.rewriteString(section, b'alphabet', item.alphabet)
        extname = b''
        if item.id < 10:
            extname = b'0'
        changed |= _xml.rewriteString(section, b'name', b'font_' + extname + str(item.id))
        writeFontAlphabet(item)
        return changed


def _needWrite(item, propertyPath):
    return item.edIsPrototype or not isPropertyShared(item, propertyPath.split(b'.'))


def _rewriteFn(tp):
    eq = equalComparator(tp)
    readTp = b'read' + tp
    writeTp = b'write' + tp

    def read(section, name, defaultValue=None):
        r = getattr(section, readTp)
        if defaultValue is None:
            return r(name)
        else:
            return r(name, defaultValue)

    def rewrite(section, subsectionName, item, propertyPath, defaultValue=None, writeEmptySections=True):
        if not _needWrite(item, propertyPath):
            return section.deleteSection(subsectionName)
        else:
            path = propertyPath.split(b'.')
            value = item
            for propertyName in path:
                value = getattr(value, propertyName)

            if value is None:
                return False
            if not writeEmptySections and str(value) is b'':
                return section.deleteSection(subsectionName)
            if eq(read(section, subsectionName, defaultValue), value):
                return False
            w = getattr(section, writeTp)
            w(subsectionName, value)
            return True

    return rewrite


rewriteInt = _rewriteFn(b'Int')
rewriteBool = _rewriteFn(b'Bool')
rewriteString = _rewriteFn(b'String')
rewriteFloat = _rewriteFn(b'Float')
rewriteVector2 = _rewriteFn(b'Vector2')
rewriteVector3 = _rewriteFn(b'Vector3')
rewriteVector4 = _rewriteFn(b'Vector4')

def rewriteTags(section, item):
    if not _needWrite(item, b'tags'):
        return section.deleteSection(b'tags')
    else:
        tags = item.tags
        rewrite = len(tags) > 0
        if section.has_key(b'tags'):
            if not rewrite:
                section.deleteSection(b'tags')
                return True
            oldTags = iv._readTags(None, section, b'tags', b'customizationItem')
            rewrite = oldTags != tags
        if rewrite:
            tagsStr = (b' ').join(tags)
            return _xml.rewriteString(section, b'tags', tagsStr)
        return False


def rewritePalettes(section, item):
    if not _needWrite(item, b'palettes'):
        return section.deleteSection(b'palettes')
    changed = False
    palettes = item.palettes
    if not palettes or len(palettes) == 0:
        return section.deleteSection(b'palettes')
    palettesSection = findOrCreate(section, b'palettes')
    changed |= resizeSection(palettesSection, len(palettes), (lambda id: b'palette'))
    for index, palette in enumerate(palettes):

        def sectName(id):
            return b'c' + str(id)

        paletteSection = palettesSection.child(index)
        changed |= resizeSection(paletteSection, len(palette), sectName)
        for i, iPalette in enumerate(palette):
            r = iPalette & 255
            g = iPalette >> 8 & 255
            b = iPalette >> 16 & 255
            a = iPalette >> 24 & 255
            colorStr = (b' ').join([str(r), str(g), str(b), str(a)])
            changed |= _xml.rewriteString(paletteSection, sectName(i), colorStr)

    editorOnlySection = getEditorOnlySection(section, True)
    changed |= _xml.rewriteInt(editorOnlySection, b'paletteIndex', item.editorData.paletteIndex, 0)
    if len(editorOnlySection.items()) == 0:
        section.deleteSection(editorOnlySection)
    return changed


def rewriteCamouflageRotation(section, camouflageItem):
    if not _needWrite(camouflageItem, b'rotation'):
        return section.deleteSection(b'rotation')
    changed = False
    hullRotation = camouflageItem.rotation[b'hull']
    gunRotation = camouflageItem.rotation[b'gun']
    turretRotation = camouflageItem.rotation[b'turret']

    def rewritePartRotation(section, partName, value):
        return _xml.rewriteFloat(section, partName, value, 0)

    rotationSection = findOrCreate(section, b'rotation')
    changed |= rewritePartRotation(rotationSection, b'HULL', hullRotation)
    changed |= rewritePartRotation(rotationSection, b'TURRET', turretRotation)
    changed |= rewritePartRotation(rotationSection, b'GUN', gunRotation)
    if hullRotation == 0 and turretRotation == 0 and gunRotation == 0:
        if section.has_key(b'rotation'):
            return section.deleteSection(b'rotation')
    return changed


def rewriteCamouflageScales(section, camouflageItem):
    if not _needWrite(camouflageItem, b'scales'):
        return section.deleteSection(b'scales')
    scalesResult = Math.Vector3(camouflageItem.scales[0], camouflageItem.scales[1], camouflageItem.scales[2])
    return _xml.rewriteVector3(section, b'scales', scalesResult)


def correctTankNameByCurrentSectionName(section, tankName):
    if section.has_key(tankName):
        return tankName
    index = tankName.find(b':')
    if index > 0:
        tmpTankName = tankName[index + 1:len(tankName)]
        if section.has_key(tmpTankName):
            return tmpTankName
    return tankName


def rewriteCamouflageTiling(section, camouflageItem):
    if not _needWrite(camouflageItem, b'tiling') or not camouflageItem.tiling:
        return section.deleteSection(b'tiling')
    else:
        changed = False
        tilingSection = findOrCreate(section, b'tiling')
        for key, value in camouflageItem.tiling.items():
            if value is None:
                continue
            tankName = camouflageItem.editorData.tilingName[key]
            correctedTankName = correctTankNameByCurrentSectionName(tilingSection, tankName)
            tilingRes = Math.Vector4(value[0], value[1], value[2], value[3])
            changed |= _xml.rewriteVector4(tilingSection, correctedTankName, tilingRes)

        for iname, isection in tilingSection.items():
            found = False
            for tankTilingName in camouflageItem.editorData.tilingName.values():
                if tankTilingName.find(iname) != -1:
                    found = True
                    break

            if not found:
                tilingSection.deleteSection(iname)
                changed = True

        return changed


def rewriteCamouflageTilingSettings(section, camouflageItem):
    if not _needWrite(camouflageItem, b'tilingSettings') or camouflageItem.tilingSettings is None:
        return section.deleteSection(b'tilingSettings')
    else:
        changed = False
        tilingSettings = camouflageItem.tilingSettings
        tilingType = tilingSettings[0]
        if section.has_key(b'tilingSettings'):
            tilingSettingsSection = section[b'tilingSettings']
        elif tilingType != CamouflageTilingType.LEGACY:
            tilingSettingsSection = section.createSection(b'tilingSettings')
        else:
            return changed
        tilingTypeStr = encodeEnum(CamouflageTilingType, tilingType)
        changed |= _xml.rewriteString(tilingSettingsSection, b'type', tilingTypeStr, b'legacy')
        if tilingSettings[1] is not None:
            factor = Math.Vector2(tilingSettings[1][0], tilingSettings[1][1])
            changed |= _xml.rewriteVector2(tilingSettingsSection, b'factor', factor)
        if tilingSettings[2] is not None:
            offset = Math.Vector2(tilingSettings[2][0], tilingSettings[2][1])
            changed |= _xml.rewriteVector2(tilingSettingsSection, b'offset', offset)
        return changed


def rewriteCamouflageGlossMetallicSettings(section, camouflageItem):
    changed = False
    if camouflageItem.editorData.glossMetallicSettingsType == 0:
        defaultGloss = Math.Vector4(DEFAULT_GLOSS, DEFAULT_GLOSS, DEFAULT_GLOSS, DEFAULT_GLOSS)
        defaultMetallic = Math.Vector4(DEFAULT_METALLIC, DEFAULT_METALLIC, DEFAULT_METALLIC, DEFAULT_METALLIC)
        changed |= section.deleteSection(b'glossMetallicMap')
        changed |= _xml.rewriteVector4(section, b'gloss', camouflageItem.glossMetallicSettings[b'gloss'], defaultGloss)
        changed |= _xml.rewriteVector4(section, b'metallic', camouflageItem.glossMetallicSettings[b'metallic'], defaultMetallic)
    elif camouflageItem.editorData.glossMetallicSettingsType == 1:
        changed |= section.deleteSection(b'gloss')
        changed |= section.deleteSection(b'metallic')
        changed |= _xml.rewriteString(section, b'glossMetallicMap', camouflageItem.glossMetallicSettings[b'glossMetallicMap'])
    return changed


def rewriteEmissionSettings(section, emissionSettings):
    changed = _xml.rewriteString(section, b'emissionMap', emissionSettings[b'emissionMap'], b'')
    changed |= _xml.rewriteString(section, b'emissionPatternMap', emissionSettings[b'emissionPatternMap'], b'')
    changed |= _xml.rewriteFloat(section, b'forwardEmissionBrightness', emissionSettings[b'forwardEmissionBrightness'], DEFAULT_FORWARD_EMISSION)
    changed |= _xml.rewriteFloat(section, b'deferredEmissionBrightness', emissionSettings[b'deferredEmissionBrightness'], DEFAULT_DEFERRED_EMISSION)
    changed |= _xml.rewriteFloat(section, b'emissionAnimationSpeed', emissionSettings[b'emissionAnimationSpeed'], DEFAULT_EMISSION_ANIMATION_SPEED)
    return changed


def rewriteNormalSettings(section, normalSettings):
    changed = _xml.rewriteString(section, b'normalMap', normalSettings[b'normalMap'], b'')
    changed |= _xml.rewriteFloat(section, b'normalMapFactor', normalSettings[b'normalMapFactor'], DEFAULT_NORMAL_MAP_FACTOR)
    changed |= _xml.rewriteInt(section, b'normalMaxLod', normalSettings[b'normalMaxLod'], DEFAULT_NORMAL_MAX_LOD)
    return changed


def encodeFlagEnum(enumClass, intValue):
    items = []
    degree = 0
    while intValue > 0:
        if intValue % 2 == 1:
            items.append(encodeEnum(enumClass, 1 << degree))
        intValue = intValue >> 1
        degree += 1

    return (b' ').join(items)


def encodeEnum(enumClass, intValue):
    for enum, value in enumClass.__dict__.iteritems():
        if enum.startswith(b'_'):
            continue
        if intValue == value:
            return enum.lower()

    return
