import ResMgr
from debug_utils import LOG_ERROR
from items.components import shared_components, component_constants, c11n_constants
from items.components.component_constants import ALLOWED_PROJECTION_DECALS_ANCHORS, ALLOWED_SLOTS_ANCHORS, ALLOWED_EMBLEM_SLOTS, ALLOWED_MISC_SLOTS
from items import _xml
import typing
from constants import IS_UE_EDITOR
if IS_UE_EDITOR:
    from combined_data_section import CombinedDataSection

def writeProjectionSlots(slotDS, slot):
    if slot.type == b'projectionDecal':
        slotDS.write(b'tags', (b' ').join(slot.tags))
    if len(slot.compatibleModels) == 1 and slot.compatibleModels[0] == b'default':
        slotDS.deleteSection(b'compatibleModels')
    else:
        slotDS.write(b'compatibleModels', (b' ').join(slot.compatibleModels))
    slotDS.writeVector3(b'position', slot.position)
    slotDS.writeVector3(b'rotation', slot.rotation)
    slotDS.writeVector3(b'scale', slot.scale)
    _xml.rewriteBool(slotDS, b'doubleSided', slot.doubleSided, False)
    _xml.rewriteBool(slotDS, b'hiddenForUser', slot.hiddenForUser, False)
    slotDS.write(b'showOn', slot.showOn)
    _xml.rewriteFloat(slotDS, b'clipAngle', slot.clipAngle, c11n_constants.DEFAULT_DECAL_CLIP_ANGLE)
    _xml.rewriteBool(slotDS, b'verticalMirror', slot.canBeMirroredVertically, False)
    if slot.type == b'projectionDecal':
        _xml.rewriteFloat(slotDS, b'anchorShift', slot.anchorShift, c11n_constants.DEFAULT_DECAL_ANCHOR_SHIFT)
    elif slot.type == b'fixedProjectionDecal':
        slotDS.write(b'itemId', slot.itemId)
        slotDS.write(b'options', slot.options)
    return


def writeAnchorSlots(slotDS, slot):
    slotDS.deleteSection(b'tags')
    if slot.anchorPosition is not None:
        slotDS.write(b'anchorPosition', slot.anchorPosition)
    if slot.anchorDirection is not None:
        slotDS.write(b'anchorDirection', slot.anchorDirection)
    if slot.applyTo is not None:
        slotDS.write(b'applyTo', slot.applyTo)
    return


def writeEmblemSlots(slotDS, slot):
    if slot.type not in (b'attachment', b'sequence', b'paint', b'camouflage', b'style', b'effect', b'projectionDecal', b'fixedProjectionDecal'):
        _xml.rewriteBool(slotDS, b'isMirrored', slot.isMirrored, False)
        slotDS.writeVector3(b'rayStart', slot.rayStart)
        slotDS.writeVector3(b'rayEnd', slot.rayEnd)
        slotDS.writeVector3(b'rayUp', slot.rayUp)
    if slot.type in (b'fixedEmblem', b'fixedInscription'):
        slotDS.write(b'emblemId', slot.emblemId)
    if slot.type == b'insigniaOnGun':
        _xml.rewriteBool(slotDS, b'applyToFabric', slot.applyToFabric, True)
        _xml.rewriteString(slotDS, b'compatibleModels', (b' ').join(slot.compatibleModels), b'')
        _xml.rewriteBool(slotDS, b'planeProjection', slot.planeProjection, False)
    slotDS.write(b'size', slot.size)
    _xml.rewriteBool(slotDS, b'hideIfDamaged', slot.hideIfDamaged, False)
    _xml.rewriteBool(slotDS, b'isUVProportional', slot.isUVProportional, True)
    return


def writeMiscSlots(slotDS, slot):
    slotDS.write(b'position', slot.position)
    slotDS.write(b'rotation', slot.rotation)
    _xml.rewriteString(slotDS, b'attachNode', slot.attachNode, b'')
    return


def writeCustomizationSlots(slots, section, subsectionName):
    section.deleteSection(subsectionName)
    if not slots:
        return
    subsection = section.insertSection(subsectionName, section.getFirstIndex(b'customization'))
    slots.sort(key=(lambda x: x.slotId))
    for slot in slots:
        slotDS = subsection.createSection(b'slot')
        slotDS.write(b'slotType', slot.type)
        slotDS.write(b'slotId', slot.slotId)
        if slot.type in ALLOWED_PROJECTION_DECALS_ANCHORS:
            writeProjectionSlots(slotDS, slot)
        elif slot.type in ALLOWED_SLOTS_ANCHORS:
            writeAnchorSlots(slotDS, slot)
        elif slot.type in ALLOWED_EMBLEM_SLOTS:
            writeEmblemSlots(slotDS, slot)
        elif slot.type in component_constants.ALLOWED_MISC_SLOTS:
            writeMiscSlots(slotDS, slot)
        else:
            LOG_ERROR((b'unexpected slot type: {}').format(slot.type))

    return


def writeModelsSets(item, section):
    if item is None:
        return
    else:
        setsSection = section[b'sets'] if section.has_key(b'sets') else None
        if setsSection is not None:
            for setName in setsSection.keys():
                if setName not in item.keys():
                    setsSection.deleteSection(setName)

        if len(item) > 1:
            if not section.has_key(b'sets'):
                setsSection = section.createSection(b'sets')
            else:
                setsSection = section[b'sets']
        for key in item:
            if key == b'default':
                setSection = section
            elif setsSection.has_key(key):
                setSection = setsSection[key]
            else:
                setSection = setsSection.createSection(key)
            if item[key] is not None:
                _xml.rewriteString(setSection, b'undamaged', item[key].undamaged)
                _xml.rewriteString(setSection, b'destroyed', item[key].destroyed)
                _xml.rewriteString(setSection, b'exploded', item[key].exploded)

        return


def writeSwingingSettings(item, section):
    _xml.rewriteFloat(section, b'sensitivityToImpulse', item.sensitivityToImpulse)
    _xml.rewriteTupleOfFloats(section, b'pitchParams', item.pitchParams)
    _xml.rewriteTupleOfFloats(section, b'rollParams', item.rollParams)
    return


def writeLodDist(dist, section, subsectionName, cache):
    reversedLodLevels = {value: key for key, value in cache.commonConfig[b'lodLevels'].items()}
    return _xml.rewriteString(section, subsectionName, reversedLodLevels[dist])


def writeBuilders(builders, section, subsectionName):
    currentBuilderIndex = 0
    for node in section.items():
        if node[0] == subsectionName:
            if currentBuilderIndex > len(builders):
                _xml.raiseWrongXml(None, subsectionName, b'Unexpected builders count')
            builders[currentBuilderIndex].save(node[1])
            currentBuilderIndex += 1

    if currentBuilderIndex + 1 < len(builders):
        _xml.raiseWrongXml(None, subsectionName, b'Unexpected builders count')
    return
