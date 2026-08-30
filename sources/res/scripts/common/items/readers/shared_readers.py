import itertools, logging, typing
from collections import defaultdict
from copy import deepcopy
import ResMgr
from constants import IS_CLIENT, IS_BOT, ITEM_DEFS_PATH, IS_EDITOR, DeviceRepairMode
from items import _xml, getTypeInfoByName
from items.components import component_constants
from items.components import shared_components
from items.components import c11n_constants
_ALLOWED_EMBLEM_SLOTS = component_constants.ALLOWED_EMBLEM_SLOTS
_ALLOWED_SLOTS_ANCHORS = component_constants.ALLOWED_SLOTS_ANCHORS
_ALLOWED_MISC_SLOTS = component_constants.ALLOWED_MISC_SLOTS
_ALLOWED_PROJECTION_DECALS_ANCHORS = component_constants.ALLOWED_PROJECTION_DECALS_ANCHORS
_CUSTOMIZATION_CONSTANTS_PATH = ITEM_DEFS_PATH + b'/customization/constants.xml'
_logger = logging.getLogger(__name__)

def _readEmblemSlot(ctx, subsection, slotType):
    descr = shared_components.EmblemSlot(_xml.readVector3(ctx, subsection, b'rayStart'), _xml.readVector3(ctx, subsection, b'rayEnd'), _xml.readVector3(ctx, subsection, b'rayUp'), _xml.readPositiveFloat(ctx, subsection, b'size'), subsection.readBool(b'hideIfDamaged', False), slotType, subsection.readBool(b'isMirrored', False), subsection.readBool(b'isUVProportional', True), _xml.readIntOrNone(ctx, subsection, b'emblemId'), _xml.readInt(ctx, subsection, b'slotId'), subsection.readBool(b'applyToFabric', True), _readCompatibleModels(subsection, ctx), subsection.readBool(b'planeProjection', False))
    _verifySlotId(ctx, slotType, descr.slotId)
    return descr


def _readMiscSlot(ctx, subsection, slotType):
    descr = shared_components.MiscSlot(type=slotType, slotId=_xml.readInt(ctx, subsection, b'slotId'), position=_xml.readVector3OrNone(ctx, subsection, b'position'), rotation=_xml.readVector3OrNone(ctx, subsection, b'rotation'), attachNode=_xml.readStringOrNone(ctx, subsection, b'attachNode'))
    _verifySlotId(ctx, slotType, descr.slotId)
    return descr


def _customizationSlotTagsValidator(tag):
    availableTags = c11n_constants.ProjectionDecalDirectionTags.ALL + c11n_constants.ProjectionDecalFormTags.ALL + c11n_constants.ProjectionDecalPreferredTags.ALL + c11n_constants.ProjectionDecalMatchingTags.ALL
    return tag in availableTags


def _readCustomizationSlot(ctx, subsection, slotType):
    descr = shared_components.CustomizationSlotDescription(slotType=slotType, anchorPosition=_xml.readVector3OrNone(ctx, subsection, b'anchorPosition'), anchorDirection=_xml.readVector3OrNone(ctx, subsection, b'anchorDirection'), applyTo=_xml.readIntOrNone(ctx, subsection, b'applyTo'), slotId=_xml.readInt(ctx, subsection, b'slotId'))
    if descr.applyTo is not None and descr.applyTo not in c11n_constants.ApplyArea.RANGE:
        _xml.raiseWrongSection(ctx, b'applyTo')
    return descr


def _readProjectionDecalSlot(ctx, subsection, slotType):
    descr = shared_components.ProjectionDecalSlotDescription(slotType=slotType, slotId=_xml.readInt(ctx, subsection, b'slotId'), position=_xml.readVector3OrNone(ctx, subsection, b'position'), rotation=_xml.readVector3OrNone(ctx, subsection, b'rotation'), scale=_xml.readVector3OrNone(ctx, subsection, b'scale'), scaleFactors=_xml.readVector3(ctx, subsection, b'scaleFactors', c11n_constants.DEFAULT_DECAL_SCALE_FACTORS), doubleSided=_xml.readBool(ctx, subsection, b'doubleSided', False), hiddenForUser=_xml.readBool(ctx, subsection, b'hiddenForUser', False), canBeMirroredVertically=_xml.readBool(ctx, subsection, b'verticalMirror', False), showOn=_xml.readIntOrNone(ctx, subsection, b'showOn'), tags=readOrderedTagsOrEmpty(ctx, subsection, _customizationSlotTagsValidator), clipAngle=_xml.readFloat(ctx, subsection, b'clipAngle', c11n_constants.DEFAULT_DECAL_CLIP_ANGLE), anchorShift=_xml.readFloat(ctx, subsection, b'anchorShift', c11n_constants.DEFAULT_DECAL_ANCHOR_SHIFT))
    _verifySlotId(ctx, slotType, descr.slotId)
    _verifyMatchingSlotSettings(ctx, descr)
    if descr.showOn is not None:
        availableShowOnRegions = c11n_constants.ApplyArea.HULL | c11n_constants.ApplyArea.TURRET | c11n_constants.ApplyArea.GUN
        if descr.showOn | availableShowOnRegions != availableShowOnRegions:
            _xml.raiseWrongSection(ctx, b'showOn')
    if subsection.has_key(b'compatibleModels'):
        descr.compatibleModels = _xml.readTupleOfStrings(ctx, subsection, b'compatibleModels')
    if subsection.has_key(b'itemId'):
        descr.itemId = _xml.readInt(ctx, subsection, b'itemId')
    if subsection.has_key(b'options'):
        descr.options = _xml.readNonNegativeInt(ctx, subsection, b'options')
    return descr


def _readCompatibleModels(subsection, ctx):
    compatibleModels = component_constants.EMPTY_TUPLE
    if IS_CLIENT or IS_EDITOR:
        if subsection.has_key(b'compatibleModels'):
            compatibleModels = _xml.readTupleOfStrings(ctx, subsection, b'compatibleModels')
    return compatibleModels


__customizationSlotIdRanges = None

def __getInitedSlotIdRanges():
    global __customizationSlotIdRanges
    if __customizationSlotIdRanges is None:
        __customizationSlotIdRanges = defaultdict(dict)
        _readCustomizationSlotIdRanges()
    return __customizationSlotIdRanges


def getCustomizationSlotIdRanges():
    if IS_EDITOR:
        return __getInitedSlotIdRanges()
    else:
        return


def _readCustomizationSlotIdRanges():
    filePath = _CUSTOMIZATION_CONSTANTS_PATH
    section = ResMgr.openSection(filePath)
    if section is None:
        _xml.raiseWrongXml(None, filePath, b'can not open or read')
    xmlCtx = (None, filePath)
    slots = _xml.getSubsection(xmlCtx, section, b'slot_id_ranges')
    for partName, part in _xml.getChildren(xmlCtx, section, b'slot_id_ranges'):
        partIds = __customizationSlotIdRanges[partName]
        for itemName, item in _xml.getChildren(xmlCtx, slots, partName):
            range_min = _xml.readInt(xmlCtx, item, b'range_min')
            range_max = _xml.readInt(xmlCtx, item, b'range_max')
            partIds[itemName] = (range_min, range_max)

    return


def _verifySlotId(ctx, slotType, slotId):
    tankPart = ctx[0][1]
    if tankPart == b'hull':
        tankArea = tankPart
    elif tankPart.startswith(b'gun'):
        tankArea = b'gun'
    elif tankPart.startswith(b'turret'):
        tankArea = b'turret'
    elif tankPart.startswith(b'chassis'):
        tankArea = b'chassis'
    else:
        return
    slotIdRanges = __getInitedSlotIdRanges()
    minSlotId, maxSlotId = slotIdRanges[tankArea][slotType]
    if not minSlotId <= slotId <= maxSlotId:
        xmlContext, fileName = ctx
        while xmlContext is not None:
            xmlContext, fileName = xmlContext

        _logger.error(b'Wrong customization slot ID%s for %s', slotId, fileName)
    return


def _verifyMatchingSlotSettings(xmlCtx, descr):

    def findTag(function, sequence):
        return next(itertools.ifilter(function, sequence), None)

    matchingTag = findTag((lambda tag: tag in c11n_constants.ProjectionDecalMatchingTags.ALL), descr.tags)
    if descr.hiddenForUser:
        if matchingTag is None:
            _xml.raiseWrongXml(xmlCtx, b'tags', b'matching tag for hidden slot is missed!')
    if matchingTag is not None:
        if not descr.hiddenForUser:
            _xml.raiseWrongXml(xmlCtx, b'hiddenForUser', b'slot:%s with matching tag must be hiddenForUser!' % descr.slotId)
        formFactorTag = findTag((lambda tag: tag in c11n_constants.ProjectionDecalFormTags.ALL), descr.tags)
        if formFactorTag is None:
            _xml.raiseWrongXml(xmlCtx, b'tags', b'slot:%s with matching tag must have form factor tag!' % descr.slotId)
        if matchingTag != c11n_constants.ProjectionDecalMatchingTags.COVER:
            directionTags = (c11n_constants.ProjectionDecalDirectionTags.LEFT,
             c11n_constants.ProjectionDecalDirectionTags.RIGHT,
             c11n_constants.ProjectionDecalDirectionTags.FRONT)
            directionTag = findTag((lambda tag: tag in directionTags), descr.tags)
            if directionTag is None:
                _xml.raiseWrongXml(xmlCtx, b'tags', b'slot:%s with matching tag must have direction tag!' % descr.slotId)
    return


def readTags(xmlCtx, section, allowedTagNames, subsectionName=b'tags'):
    tagNames = _xml.readString(xmlCtx, section, subsectionName).split()
    res = set()
    for tagName in tagNames:
        if tagName not in allowedTagNames:
            _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown tag '%s'" % tagName)
        res.add(intern(tagName))

    return frozenset(res)


def readAllowedTags(xmlCtx, section, subsectionName, itemTypeName):
    allowedTagNames = getTypeInfoByName(itemTypeName)[b'tags']
    return readTags(xmlCtx, section, allowedTagNames, subsectionName)


def readTagsOrEmpty(xmlCtx, section, allowedTagNames, subsectionName=b'tags'):
    tags = _xml.readStringOrNone(xmlCtx, section, subsectionName)
    res = set()
    if tags is not None:
        tagNames = tags.split()
        for tagName in tagNames:
            if tagName not in allowedTagNames:
                _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown tag '%s'" % tagName)
            res.add(intern(tagName))

    return frozenset(res)


def readOrderedTagsOrEmpty(xmlCtx, section, allowedTagValidator, subsectionName=b'tags'):
    tags = _xml.readStringOrNone(xmlCtx, section, subsectionName)
    res = []
    if tags is not None:
        tagNames = tags.split()
        for tagName in tagNames:
            if not allowedTagValidator(tagName):
                _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown tag '%s'" % tagName)
            res.append(intern(tagName))

    return tuple(res)


def readCustomizationSlots(xmlCtx, section, subsectionName):
    slots = []
    anchors = []
    slot_tag_name = b'slot'
    slotIDs = set()
    for sname, subsection in _xml.getChildren(xmlCtx, section, subsectionName):
        if sname != slot_tag_name:
            _xml.raiseWrongXml(xmlCtx, (b'customizationSlots/{}').format(sname), (b'expected {}').format(slot_tag_name))
        ctx = (xmlCtx, (b'customizationSlots/{}').format(sname))
        slotType = _xml.readString(ctx, subsection, b'slotType')
        descr = None
        if slotType in component_constants.ALLOWED_EMBLEM_SLOTS:
            descr = _readEmblemSlot(ctx, subsection, slotType)
            slots.append(descr)
        elif slotType in component_constants.ALLOWED_PROJECTION_DECALS_ANCHORS:
            descr = _readProjectionDecalSlot(ctx, subsection, slotType)
            anchors.append(descr)
        elif slotType in component_constants.ALLOWED_SLOTS_ANCHORS:
            descr = _readCustomizationSlot(ctx, subsection, slotType)
            anchors.append(descr)
        elif slotType in component_constants.ALLOWED_MISC_SLOTS:
            descr = _readMiscSlot(ctx, subsection, slotType)
            anchors.append(descr)
        else:
            _xml.raiseWrongXml(xmlCtx, (b'customizationSlots/{}/{}').format(sname, slotType), (b'expected value is {}').format(_ALLOWED_EMBLEM_SLOTS + _ALLOWED_SLOTS_ANCHORS + _ALLOWED_MISC_SLOTS + _ALLOWED_PROJECTION_DECALS_ANCHORS))
        if descr is not None and descr.slotId not in slotIDs:
            slotIDs.add(descr.slotId)
        else:
            xmlContext, fileName = xmlCtx
            while xmlContext is not None:
                xmlContext, fileName = xmlContext

            _logger.error(b'Repeated customization slot ID%s for %s', descr.slotId, fileName)

    return (
     tuple(slots), tuple(anchors))


def readEmblemSlots(xmlCtx, section, subsectionName):
    slots = []
    for sname, subsection in _xml.getChildren(xmlCtx, section, subsectionName):
        if sname not in component_constants.ALLOWED_EMBLEM_SLOTS:
            _xml.raiseWrongXml(xmlCtx, (b'emblemSlots/{}').format(sname), (b'expected {}').format(_ALLOWED_EMBLEM_SLOTS))
        ctx = (
         xmlCtx, (b'emblemSlots/{}').format(sname))
        descr = shared_components.EmblemSlot(_xml.readVector3(ctx, subsection, b'rayStart'), _xml.readVector3(ctx, subsection, b'rayEnd'), _xml.readVector3(ctx, subsection, b'rayUp'), _xml.readPositiveFloat(ctx, subsection, b'size'), subsection.readBool(b'hideIfDamaged', False), _ALLOWED_EMBLEM_SLOTS[_ALLOWED_EMBLEM_SLOTS.index(sname)], subsection.readBool(b'isMirrored', False), subsection.readBool(b'isUVProportional', True), _xml.readIntOrNone(ctx, subsection, b'emblemId'), _readCompatibleModels(subsection, ctx), subsection.readBool(b'planeProjection', False))
        slots.append(descr)

    return (tuple(slots), tuple())


def readLodDist(xmlCtx, section, subsectionName, cache):
    name = _xml.readNonEmptyString(xmlCtx, section, subsectionName)
    dist = cache.commonConfig[b'lodLevels'].get(name)
    if dist is None:
        _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown lod level '%s'" % name)
    return dist


def readLodSettings(xmlCtx, section, cache):
    return shared_components.LodSettings(maxLodDistance=readLodDist(xmlCtx, section, b'lodSettings/maxLodDistance', cache), maxPriority=_xml.readIntOrNone(xmlCtx, section, b'lodSettings/maxPriority'))


def readSwingingSettings(xmlCtx, section, cache):
    return shared_components.SwingingSettings(readLodDist(xmlCtx, section, b'swinging/lodDist', cache), _xml.readNonNegativeFloat(xmlCtx, section, b'swinging/sensitivityToImpulse'), _xml.readTupleOfFloats(xmlCtx, section, b'swinging/pitchParams', 6), _xml.readTupleOfFloats(xmlCtx, section, b'swinging/rollParams', 7))


def readModelsSets(xmlCtx, section, subsectionName):
    undamaged = _xml.readNonEmptyString(xmlCtx, section, subsectionName + b'/undamaged')
    destroyed = _xml.readNonEmptyString(xmlCtx, section, subsectionName + b'/destroyed')
    exploded = _xml.readNonEmptyString(xmlCtx, section, subsectionName + b'/exploded')
    modelsSets = {b'default': (shared_components.ModelStatesPaths(undamaged, destroyed, exploded))}
    subsection = section[subsectionName]
    if subsection:
        setSection = subsection[b'sets'] or {}
        for k, v in setSection.items():
            modelsSets[k] = shared_components.ModelStatesPaths(_xml.readStringOrNone(xmlCtx, v, b'undamaged') or undamaged, _xml.readStringOrNone(xmlCtx, v, b'destroyed') or destroyed, _xml.readStringOrNone(xmlCtx, v, b'exploded') or exploded)

    return modelsSets


def readUserText(section):
    return shared_components.I18nComponent(section.readString(b'userString'), section.readString(b'description'), section.readString(b'shortUserString'), section.readString(b'shortDescriptionSpecial'), section.readString(b'longDescriptionSpecial'))


def readDeviceHealthParams(xmlCtx, section, subsectionName=b'', withHysteresis=True):
    if subsectionName:
        section = _xml.getSubsection(xmlCtx, section, subsectionName)
        xmlCtx = (xmlCtx, subsectionName)
    component = shared_components.DeviceHealth(_xml.readInt(xmlCtx, section, b'maxHealth', 1), _xml.readNonNegativeFloat(xmlCtx, section, b'repairCost'), _xml.readInt(xmlCtx, section, b'maxRegenHealth', 0))
    if component.maxRegenHealth > component.maxHealth:
        _xml.raiseWrongSection(xmlCtx, b'maxRegenHealth')
    if not IS_CLIENT and not IS_BOT:
        component.healthRegenPerSec = _xml.readNonNegativeFloat(xmlCtx, section, b'healthRegenPerSec')
        component.healthBurnPerSec = _xml.readNonNegativeFloat(xmlCtx, section, b'healthBurnPerSec')
        if section.has_key(b'chanceToHit'):
            component.chanceToHit = _xml.readFraction(xmlCtx, section, b'chanceToHit')
        else:
            component.chanceToHit = None
        if withHysteresis:
            hysteresisHealth = _xml.readInt(xmlCtx, section, b'hysteresisHealth', 0)
            if hysteresisHealth > component.maxRegenHealth:
                _xml.raiseWrongSection(xmlCtx, b'hysteresisHealth')
            component.hysteresisHealth = hysteresisHealth
        component.invulnerable = _xml.readBool(xmlCtx, section, b'invulnerable', False)
        component.repairSpeedLimiter = _readRepairSpeedLimiter(xmlCtx, section)
    if IS_CLIENT:
        if section.has_key(b'repairTime'):
            component.repairTime = _xml.readFloat(xmlCtx, section, b'repairTime')
    return component


def _readRepairSpeedLimiter(xmlCtx, section):
    if not section.has_key(b'repairSpeedLimiter'):
        return None
    else:
        ctx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, b'repairSpeedLimiter')
        repairSpeedModifier = _xml.readNonNegativeFloat(ctx, subsection, b'repairSpeedModifier')
        return {b'repairSpeedModifier': repairSpeedModifier, 
           b'speedToStartLimitedRepair': (component_constants.KMH_TO_MS * _xml.readNonNegativeFloat(ctx, subsection, b'speedToStartLimitedRepair')), 
           b'speedToStopLimitedRepair': (component_constants.KMH_TO_MS * _xml.readNonNegativeFloat(ctx, subsection, b'speedToStopLimitedRepair')), 
           b'repairMode': (DeviceRepairMode.SLOWED if repairSpeedModifier > 0.0 else DeviceRepairMode.SUSPENDED)}


def _refDefaultCamouflageAttribute(defaultCamo, attr):
    val = getattr(defaultCamo, attr)
    if IS_EDITOR:
        return deepcopy(val)
    return val


def readCamouflage(xmlCtx, section, sectionName, default=None):
    tiling, mask, density, aoTextureSize = (None, None, None, None)
    tilingKey = sectionName + b'/tiling'
    if section.has_key(tilingKey):
        readTiling = _xml.readTupleOfFloats(xmlCtx, section, tilingKey, 4)
        if readTiling[0] > 0 and readTiling[1] > 0:
            tiling = readTiling
    if tiling is None:
        if default is not None:
            tiling = _refDefaultCamouflageAttribute(default, b'tiling')
        else:
            _xml.raiseWrongSection(xmlCtx, tilingKey)
    maskKey = sectionName + b'/exclusionMask'
    mask = section.readString(maskKey)
    if not mask and default is not None:
        mask = default.exclusionMask
    densityKey = sectionName + b'/density'
    if section.has_key(densityKey):
        density = _xml.readTupleOfFloats(xmlCtx, section, densityKey, 2)
    if density is None and default is not None:
        density = _refDefaultCamouflageAttribute(default, b'density')
    aoTextureSizeKey = sectionName + b'/aoTextureSize'
    if section.has_key(aoTextureSizeKey):
        aoTextureSize = _xml.readTupleOfFloats(xmlCtx, section, aoTextureSizeKey, 2)
    if aoTextureSize is None and default is not None:
        aoTextureSize = _refDefaultCamouflageAttribute(default, b'aoTextureSize')
    return shared_components.Camouflage(tiling, mask, density, aoTextureSize)


def readBuilder(xmlCtx, section, subsectionName, builderType):
    subsection = section[subsectionName]
    if subsection is not None:
        product = builderType(subsection)
        if product is not None:
            return product
        _xml.raiseWrongXml(xmlCtx, subsectionName, (b'Failed builder {0} loading from {1}').format(builderType, subsectionName))
    else:
        _xml.raiseWrongSection(xmlCtx, subsectionName)
    return


def readBuilders(xmlCtx, section, subsectionName, builderType):
    products = []
    for node in section.items():
        if node[0] == subsectionName:
            product = builderType(node[1])
            if product is not None:
                products.append(product)
            else:
                _xml.raiseWrongXml(xmlCtx, subsectionName, (b'Failed builder {0} loading from {1}').format(builderType, subsectionName))

    if not products:
        _xml.raiseWrongSection(xmlCtx, subsectionName)
    return products
