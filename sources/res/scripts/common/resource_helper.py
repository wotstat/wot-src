from __future__ import absolute_import
import importlib, inspect
from contextlib import contextmanager
from collections import namedtuple
from past.builtins import basestring
import ResMgr
from debug_utils import LOG_CURRENT_EXCEPTION
from soft_exception import SoftException

class RESOURCE_ITEM_TYPE(object):
    BOOL = b'bool'
    INTEGER = b'int'
    FLOAT = b'float'
    STRING = b'string'
    URL = b'url'
    VECTOR2 = b'vector2'
    VECTOR3 = b'vector3'
    VECTOR4 = b'vector4'
    LIST = b'list'
    DICT = b'dict'
    SEQ_PAIRS = b'seq-pairs'
    CLASS = b'class'


class ResourceError(SoftException):

    def __init__(self, ctx, message):
        super(ResourceError, self).__init__()
        self.ctx = ctx
        self.errorMessage = message
        return

    def __str__(self):
        return (b'Error in {0:>s}. {1:>s}').format(self.ctx, self.errorMessage)


class ResourceCtx(object):

    def __init__(self, filePath, xpath=None):
        super(ResourceCtx, self).__init__()
        self.__filePath = filePath
        if xpath is None:
            self.__xpath = []
        elif isinstance(xpath, list):
            self.__xpath = xpath
        else:
            raise ValueError(b'xpath must be list.')
        return

    def next(self, section):
        xpath = self.__xpath[:]
        if isinstance(section, basestring):
            xpath.append(section)
        else:
            xpath.append(section.name)
        return ResourceCtx(self.__filePath, xpath)

    def prev(self):
        return ResourceCtx(self.__filePath, self.__xpath[:-1])

    def __str__(self):
        path = self.__xpath[:]
        path.insert(0, self.__filePath)
        return (b'/').join(path)


def getRoot(filePath, msg=b'', safe=False):
    section = ResMgr.openSection(filePath)
    ctx = ResourceCtx(filePath)
    if section is None and safe:
        raise ResourceError(ctx, msg or (b'File {0} is not found.').format(filePath))
    return (ctx, section)


def purgeResource(filePath):
    ResMgr.purge(filePath, True)
    return


@contextmanager
def root_generator(filePath):
    try:
        ctx, section = getRoot(filePath)
    except ResourceError as error:
        raise error
    else:
        try:
            try:
                yield (
                 ctx, section)
            except:
                LOG_CURRENT_EXCEPTION()

        finally:
            ResMgr.purge(filePath, True)

    return


def root_iterator(filePath, customReaders=None, nameFromSection=False):
    readers = customReaders or {}
    _ITEM_VALUE_READERS.update(readers)
    with root_generator(filePath) as ctx, section:
        for ctx, subSection in getIterator(ctx, section):
            sectionName = subSection.name if nameFromSection else b'setting'
            yield readItem(ctx, subSection, name=sectionName, nameFromSection=nameFromSection)

    for k in readers.keys():
        _ITEM_VALUE_READERS.pop(k)

    return


def getSubSection(ctx, section, name, safe=False):
    subSection = section[name]
    if subSection is None and not safe:
        raise ResourceError(ctx, (b'Section {0} is not found.').format(name))
    return (ctx.next(name), subSection)


def getIterator(xmlCtx, section):
    if section is None:
        raise ResourceError(xmlCtx, b'Section is not found')
    for _, subSection in section.items():
        yield (
         xmlCtx.next(subSection), subSection)

    return


def readItemAttr(xmlCtx, section, attr, default=None, keys=None):
    if keys is None:
        keys = section.keys()
    if attr not in keys:
        value = default
        if default is None:
            raise ResourceError(xmlCtx, (b'Attribute {0} is not found.').format(attr))
    else:
        value = section[attr].asString
    return value


def readItemName(xmlCtx, section, keys=None, nameFromSection=False):
    if nameFromSection:
        return section.name
    return readItemAttr(xmlCtx, section, b'name', default=b'', keys=keys)


def _readItemType(xmlCtx, section, keys=None):
    return readItemAttr(xmlCtx, section, b'type', default=b'string', keys=keys)


ResourceItem = namedtuple(b'_Item', (b'type', b'name', b'value'))

def readBoolItem(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readBool(b'value')
    else:
        value = section.asBool
    return ResourceItem(RESOURCE_ITEM_TYPE.BOOL, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readIntItem(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readInt(b'value')
    else:
        value = section.asInt
    return ResourceItem(RESOURCE_ITEM_TYPE.INTEGER, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readFloatItem(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readFloat(b'value')
    else:
        value = section.asFloat
    return ResourceItem(RESOURCE_ITEM_TYPE.FLOAT, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readStringItem(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readWideString(b'value')
    else:
        value = section.asWideString
    return ResourceItem(RESOURCE_ITEM_TYPE.STRING, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readVector2Item(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readVector2(b'value')
    else:
        value = section.asVector2
    return ResourceItem(RESOURCE_ITEM_TYPE.VECTOR2, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readVector3Item(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readVector3(b'value')
    else:
        value = section.asVector3
    return ResourceItem(RESOURCE_ITEM_TYPE.VECTOR3, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readVector4Item(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readVector4(b'value')
    else:
        value = section.asVector4
    return ResourceItem(RESOURCE_ITEM_TYPE.VECTOR4, readItemName(xmlCtx, section, nameFromSection=nameFromSection), value)


def readList(xmlCtx, section, valueName=b'value', nameFromSection=False):
    result = []
    name = readItemName(xmlCtx, section, nameFromSection=nameFromSection)
    subCtx, subSection = getSubSection(xmlCtx, section, valueName)
    for nextCtx, nextSection in getIterator(subCtx, subSection):
        result.append(readItem(nextCtx, nextSection).value)

    return ResourceItem(RESOURCE_ITEM_TYPE.LIST, name, result)


def readDict(xmlCtx, section, valueName=b'value', nameFromSection=False):
    result = {}
    name = readItemName(xmlCtx, section, nameFromSection=nameFromSection)
    subCtx, subSection = getSubSection(xmlCtx, section, valueName)
    for nextCtx, nextSection in getIterator(subCtx, subSection):
        item = readItem(nextCtx, nextSection)
        if not item.name:
            raise ResourceError(nextCtx, (b'{0}: name is required in each item').format(name))
        result[item.name] = item.value

    return ResourceItem(RESOURCE_ITEM_TYPE.DICT, name, result)


def readSeqPairs(xmlCtx, section, valueName=b'value', nameFromSection=False):
    result = []
    name = readItemName(xmlCtx, section, nameFromSection=nameFromSection)
    subCtx, subSection = getSubSection(xmlCtx, section, valueName)
    for nextCtx, nextSection in getIterator(subCtx, subSection):
        item = readItem(nextCtx, nextSection)
        result.append((item.name, item.value))

    return ResourceItem(RESOURCE_ITEM_TYPE.SEQ_PAIRS, name, tuple(result))


def readClassItem(xmlCtx, section, nameFromSection=False):
    if b'value' in section.keys():
        value = section.readString(b'value')
    else:
        value = section.asString
    parts = value.split(b'.')
    if len(parts) == 1:
        raise ResourceError(xmlCtx, (b'Class path {0} is invalid').format(value))
    try:
        module = importlib.import_module((b'.').join(parts[:-1]))
    except ImportError:
        raise ResourceError(xmlCtx, (b'Class path {0} is invalid').format(value))

    clazz = getattr(module, parts[-1], None)
    if clazz is None or not inspect.isclass(clazz):
        raise ResourceError(xmlCtx, (b'There is not path to class {0}').format(value))
    return ResourceItem(RESOURCE_ITEM_TYPE.STRING, readItemName(xmlCtx, section, nameFromSection=nameFromSection), clazz)


_ITEM_VALUE_READERS = {(RESOURCE_ITEM_TYPE.BOOL): readBoolItem, 
   (RESOURCE_ITEM_TYPE.INTEGER): readIntItem, 
   (RESOURCE_ITEM_TYPE.FLOAT): readFloatItem, 
   (RESOURCE_ITEM_TYPE.STRING): readStringItem, 
   (RESOURCE_ITEM_TYPE.URL): readStringItem, 
   (RESOURCE_ITEM_TYPE.VECTOR2): readVector2Item, 
   (RESOURCE_ITEM_TYPE.VECTOR3): readVector3Item, 
   (RESOURCE_ITEM_TYPE.VECTOR4): readVector4Item, 
   (RESOURCE_ITEM_TYPE.LIST): readList, 
   (RESOURCE_ITEM_TYPE.DICT): readDict, 
   (RESOURCE_ITEM_TYPE.SEQ_PAIRS): readSeqPairs, 
   (RESOURCE_ITEM_TYPE.CLASS): readClassItem}

def readItem(ctx, section, name=b'item', nameFromSection=False):
    if section.name != name:
        raise ResourceError(ctx, (b'Resource {0} is invalid').format(section.name))
    keys = section.keys()
    itemType = _readItemType(ctx, section, keys=keys)
    name = readItemName(ctx, section, keys=keys, nameFromSection=nameFromSection)
    if itemType in _ITEM_VALUE_READERS:
        reader = _ITEM_VALUE_READERS[itemType]
        item = reader(ctx, section, nameFromSection=nameFromSection)
    else:
        raise ResourceError(ctx, (b'"{0}: type {1} is invalid.').format(name, itemType))
    return item
