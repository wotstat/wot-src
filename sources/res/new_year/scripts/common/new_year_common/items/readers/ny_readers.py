import typing, contextlib
from extension_utils import ResMgr
from new_year_common.ny_exception import NYSoftException
from new_year_common.items.components.ny_components import SlotDescriptor, VariadicDiscountDescriptor, ToyTransformation, ToyModelOverride
from new_year_common.items.components.ny_constants import TOY_TYPES

@contextlib.contextmanager
def openSection(path):
    try:
        yield ResMgr.openSection(path)
    finally:
        ResMgr.purge(path)

    return


def _readSlotSection(section):
    cfg = {b'id': (section.readInt(b'id'))}
    cfg[b'type'] = slotType = section.readString(b'type')
    if slotType not in TOY_TYPES:
        raise NYSoftException(b"Wrong slot type '%s'" % slotType)
    return cfg


def readSlots(xmlPath):
    cache = None
    with openSection(xmlPath) as section:
        if section is None:
            raise NYSoftException(b"Can't open '%s'" % xmlPath)
        subsections = section[b'slots'].values()
        numSlots = len(subsections)
        cache = [
         None] * numSlots
        for slotSec in subsections:
            cfg = _readSlotSection(slotSec)
            slotID = cfg[b'id']
            if not 0 <= slotID < numSlots:
                raise NYSoftException((b'Wrong slotID {}, {}').format(slotID, numSlots))
            if cache[slotID] is not None:
                raise NYSoftException(b"Repeated slotID '%d'" % slotID)
            cache[slotID] = SlotDescriptor(cfg)

    return cache


def _readToyTransformationNode(node):
    toyTransformation = ToyTransformation(transform=node.readMatrix(b'transform') if node.has_key(b'transform') else None, modelOverride=ToyModelOverride.createModel(node))
    return (
     node.readString(b'node'), node.readString(b'object'), toyTransformation)


def _readToyTransformationsSection(section):
    nodes = {}
    for subSection in section.values():
        if subSection.name == b'node':
            nodeName, objectName, transformation = _readToyTransformationNode(subSection)
            nodes[(intern(objectName), intern(nodeName))] = transformation

    return (
     section.readString(b'name'), nodes)


def readToysTransformations(xmlPath):
    cache = {}
    with openSection(xmlPath) as section:
        if section is None:
            raise NYSoftException(b"Can't open '%s" % xmlPath)
        for subSection in section.values():
            modelName, nodes = _readToyTransformationsSection(subSection)
            cache[modelName] = nodes

    return cache


def buildVariadicDiscountsCache(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        raise NYSoftException(b"Can't open '%s'" % xmlPath)
    cache = {}
    for vdSec in section.values():
        cfg = _readVariadicDiscount(vdSec)
        vdID = cfg[b'id']
        if vdID in cache:
            raise NYSoftException(b"Repeated variadic discount ID '%s'" % vdID)
        cache[vdID] = VariadicDiscountDescriptor(cfg[b'id'], cfg[b'firstGoodieId'], cfg[b'lastGoodieId'], cfg[b'level'])

    return cache


def _readVariadicDiscount(section):
    cfg = {}
    cfg[b'id'] = section.readString(b'id')
    cfg[b'firstGoodieId'] = section.readInt(b'firstGoodieId')
    cfg[b'lastGoodieId'] = section.readInt(b'lastGoodieId')
    cfg[b'level'] = section.readInt(b'level')
    return cfg
