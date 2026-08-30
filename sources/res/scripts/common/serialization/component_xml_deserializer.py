from __future__ import absolute_import
from typing import Tuple, Any
from future.utils import iteritems
import ResMgr
from constants import IS_EDITOR
from items import decodeEnum
from items.components.c11n_constants import ApplyArea, Options
from items.utils import getEditorOnlySection
from serialization.definitions import FieldFlags, FieldTypes
from serialization.exceptions import SerializationException
from serialization.serializable_component import SerializableComponent
__all__ = (b'ComponentXmlDeserializer',)

class ComponentXmlDeserializer(object):
    __slots__ = (b'customTypes',)

    def __init__(self, customTypes):
        self.customTypes = customTypes
        super(ComponentXmlDeserializer, self).__init__()
        return

    def decode(self, itemType, xmlCtx, section):
        obj = self.__decodeCustomType(itemType, xmlCtx, section)
        return obj

    def __decodeCustomType(self, customType, ctx, section):
        cls = self.customTypes[customType]
        instance = cls()
        for fname, finfo in iteritems(cls.fields):
            if finfo.flags & FieldFlags.NON_XML:
                continue
            if not section.has_key(fname):
                if not (IS_EDITOR and finfo.flags & FieldFlags.SAVE_AS_EDITOR_ONLY):
                    continue
                editorOnlySection = getEditorOnlySection(section)
                if not (editorOnlySection is not None and editorOnlySection.has_key(fname)):
                    continue
                section = editorOnlySection
            ftype = finfo.type
            if ftype == FieldTypes.VARINT:
                value = section.readInt(fname)
            elif ftype == FieldTypes.FLOAT:
                value = section.readFloat(fname)
            elif ftype == FieldTypes.APPLY_AREA_ENUM:
                value = self.__decodeEnum(section.readString(fname), ApplyArea)
            elif ftype == FieldTypes.TAGS:
                value = tuple(section.readString(fname).split())
            elif ftype == FieldTypes.STRING:
                value = section.readString(fname)
            elif ftype == FieldTypes.OPTIONS_ENUM:
                value = self.__decodeEnum(section.readString(fname), Options)
            elif ftype & FieldTypes.TYPED_ARRAY:
                itemType = ftype ^ FieldTypes.TYPED_ARRAY
                value = self.__decodeArray(itemType, (ctx, fname), section[fname])
            elif ftype >= FieldTypes.CUSTOM_TYPE_OFFSET:
                ftype = ftype // FieldTypes.CUSTOM_TYPE_OFFSET
                value = self.__decodeCustomType(ftype, (ctx, fname), section[fname])
            else:
                raise SerializationException(b'Unsupported item type')
            if not finfo.flags & FieldFlags.DEPRECATED or hasattr(instance, fname):
                setattr(instance, fname, value)
            if IS_EDITOR and finfo.flags & FieldFlags.SAVE_AS_EDITOR_ONLY:
                section = section.parentSection()

        return instance

    def __decodeArray(self, itemType, ctx, section):
        result = []
        for iname, isection in section.items():
            if itemType == FieldTypes.VARINT:
                result.append(isection.asInt)
            elif itemType == FieldTypes.FLOAT:
                result.append(isection.asFloat)
            elif itemType >= FieldTypes.CUSTOM_TYPE_OFFSET:
                customType = itemType // FieldTypes.CUSTOM_TYPE_OFFSET
                ictx = (ctx, (b'{0} {1}').format(iname, isection))
                result.append(self.__decodeCustomType(customType, ictx, isection))
            else:
                raise SerializationException(b'Unsupported item type')

        return result

    def __decodeEnum(self, value, enum):
        return decodeEnum(value, enum)[0]
