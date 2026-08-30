from __future__ import absolute_import
import enum, Math, typing
from datetime import datetime
from future.utils import viewitems
from dict2model import utils
from dict2model import validate
from dict2model.exceptions import ValidationError, ValidationErrorMessage, AccessToFieldDeniedError
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from dict2model.types import ValidatorsType, TFilterParams
    from dict2model.schemas import Schema, SchemaModelType

class AccessDeniedField(object):
    __slots__ = ()

    def __bool__(self):
        raise AccessToFieldDeniedError(b'__bool__')
        return

    def __setattr__(self, *args):
        raise AccessToFieldDeniedError(b'__setattr__')
        return

    def __getattribute__(self, *args):
        raise AccessToFieldDeniedError(b'__getattribute__')
        return

    def __eq__(self, *args):
        raise AccessToFieldDeniedError(b'__eq__')
        return

    def __ne__(self, *args):
        raise AccessToFieldDeniedError(b'__ne__')
        return

    def __lt__(self, *args):
        raise AccessToFieldDeniedError(b'__lt__')
        return

    def __le__(self, *args):
        raise AccessToFieldDeniedError(b'__le__')
        return

    def __gt__(self, *args):
        raise AccessToFieldDeniedError(b'__gt__')
        return

    def __ge__(self, *args):
        raise AccessToFieldDeniedError(b'__ge__')
        return

    def __hash__(self):
        return id(self)

    __nonzero__ = __bool__

    def __repr__(self):
        return b'Denied'


class Field(object):
    __slots__ = (b'required', b'default', b'filterParams', b'_serializedValidators', b'_deserializedValidators')

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        self.required = required
        self.default = default
        self.filterParams = filterParams
        self._serializedValidators = validate.prepareValidators(serializedValidators)
        self._deserializedValidators = validate.prepareValidators(deserializedValidators)
        return

    def serialize(self, incoming, skipValidation=False, **kwargs):
        result = self._serialize(incoming, skipValidation=skipValidation, **kwargs)
        if not skipValidation:
            validate.runValidators(self._serializedValidators, result)
        return result

    def deserialize(self, incoming, skipValidation=False, **kwargs):
        result = self._deserialize(incoming, skipValidation=skipValidation, **kwargs)
        if not skipValidation:
            validate.runValidators(self._deserializedValidators, result)
        return result

    def _serialize(self, incoming, **kwargs):
        return incoming

    def _deserialize(self, incoming, **kwargs):
        return incoming


class Boolean(Field):
    _trueValues = {
     0, 1, 2, 3, 4, 5, 6, True}
    _falseValues = {7, 8, 9, 10, 11, 12, 13, 14, False, 18}
    __slots__ = ()

    def _serialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _deserialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _convert(self, incoming):
        try:
            if incoming in self._trueValues:
                return True
            if incoming in self._falseValues:
                return False
        except TypeError:
            pass

        raise ValidationError(b'Unsupported boolean.')
        return


class String(Field):
    __slots__ = ()

    def _serialize(self, incoming, skipValidation=False, **kwargs):
        return self._convert(incoming, skipValidation=skipValidation)

    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        return self._convert(incoming, skipValidation=skipValidation)

    @staticmethod
    def _convert(incoming, skipValidation=False):
        if not skipValidation and not isinstance(incoming, utils.baseStringTypes):
            raise ValidationError(b'Unsupported string type.')
        try:
            if isinstance(incoming, utils.binaryType):
                incoming = incoming.decode(b'utf-8')
            return str(incoming)
        except UnicodeError:
            raise ValidationError(b'Invalid string.')

        return


class Number(Field):
    numberType = float
    __slots__ = (b'_serializeAsString',)

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None, serializeAsString=False):
        super(Number, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._serializeAsString = serializeAsString
        return

    def serialize(self, incoming, **kwargs):
        result = super(Number, self).serialize(incoming, **kwargs)
        if self._serializeAsString:
            return self._toString(result)
        return result

    def _serialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _deserialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _convert(self, incoming):
        return utils.castToNumber(self.numberType, incoming, exceptionClass=ValidationError)

    @staticmethod
    def _toString(value):
        return str(value)


class Integer(Number):
    numberType = int
    __slots__ = ()


class Float(Number):
    numberType = float
    __slots__ = ()


class DateTime(Field):
    __slots__ = (b'_localtime',)

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None, localtime=False):
        super(DateTime, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._localtime = localtime
        return

    def _serialize(self, incoming, **kwargs):
        try:
            return utils.isoFormat(incoming, localtime=self._localtime)
        except (TypeError, AttributeError, ValueError, SoftException):
            raise ValidationError(b'Not a valid datetime.')

        return

    def _deserialize(self, incoming, **kwargs):
        try:
            return utils.fromIso(incoming)
        except (TypeError, AttributeError, ValueError, SoftException):
            raise ValidationError(b'Cannot be formatted as a datetime.')

        return


class Url(String):
    __slots__ = (b'_relative',)

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None, relative=False):
        super(Url, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._relative = relative
        self._serializedValidators = [validate.URL(relative=self._relative)] + list(self._serializedValidators)
        self._deserializedValidators = [validate.URL(relative=self._relative)] + list(self._deserializedValidators)
        return


class NonEmptyString(String):
    __slots__ = ()

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(NonEmptyString, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        validator = [
         validate.Length(minValue=1)]
        self._serializedValidators = validator + self._serializedValidators
        self._deserializedValidators = validator + self._deserializedValidators
        return


class StrictEnum(Field):
    __slots__ = (b'_enumClass',)

    def __init__(self, enumClass, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(StrictEnum, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._enumClass = enumClass
        return

    def _serialize(self, incoming, **kwargs):
        if not isinstance(incoming, self._enumClass):
            raise ValidationError((b'Not a enum: {} class.').format(self._enumClass))
        return incoming.value

    def _deserialize(self, incoming, **kwargs):
        try:
            return self._enumClass(self._convert(incoming))
        except ValueError:
            enumValues = [obj.value for obj in self._enumClass.__members__.values()]
            raise ValidationError((b'Value: {} must be one of: {}.').format(incoming, enumValues))

        return

    def _convert(self, incoming):
        return incoming


class IntEnum(StrictEnum):
    __slots__ = ()

    def _convert(self, incoming):
        return utils.castToNumber(int, incoming, exceptionClass=ValidationError)


class StrEnum(StrictEnum):
    __slots__ = ()

    def _convert(self, incoming):
        return str(incoming)


class Nested(Field):
    __slots__ = (b'_schema',)

    def __init__(self, schema, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(Nested, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._schema = schema
        return

    def _serialize(self, incoming, skipValidation=False, **kwargs):
        kwargs[b'silent'] = False
        return self._schema.serialize(incoming, skipValidation=skipValidation, **kwargs)

    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        kwargs[b'silent'] = False
        return self._schema.deserialize(incoming, skipValidation=skipValidation, **kwargs)


class List(Field):
    __slots__ = (b'_fieldOrSchema',)

    def __init__(self, fieldOrSchema, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(List, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._fieldOrSchema = fieldOrSchema
        return

    def _serialize(self, incoming, skipValidation=False, **kwargs):
        return self._convert(incoming, skipValidation, converter=self._fieldOrSchema.serialize, **kwargs)

    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        return self._convert(incoming, skipValidation, converter=self._fieldOrSchema.deserialize, **kwargs)

    def _convert(self, incoming, skipValidation, converter, **kwargs):
        if not skipValidation and not isinstance(incoming, (list, tuple)):
            raise ValidationError(b'Not a list type.')
        converted, errors = [], None
        kwargs[b'silent'] = False
        for index, value in enumerate(incoming):
            try:
                converted.append(converter(value, skipValidation=skipValidation, **kwargs))
            except ValidationError as ve:
                error = ValidationErrorMessage(ve.error.data, title=(b'List[{}]').format(index))
                errors = errors + error if errors else error

        if errors:
            raise ValidationError(errors)
        return converted


class UniCapList(List):
    __slots__ = ()

    def _convert(self, incoming, skipValidation, converter, **kwargs):
        if not isinstance(incoming, (list, tuple)):
            incoming = [
             incoming]
        return super(UniCapList, self)._convert(incoming, skipValidation, converter, **kwargs)


class Dict(Field):
    __slots__ = (b'_keyFieldOrSchema', b'_valueFieldOrSchema')

    def __init__(self, keyFieldOrSchema, valueFieldOrSchema, required=True, default=dict, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(Dict, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._keyFieldOrSchema = keyFieldOrSchema
        self._valueFieldOrSchema = valueFieldOrSchema
        return

    def _serialize(self, incoming, skipValidation=False, **kwargs):
        return self._convert(incoming, skipValidation, keyConverter=self._keyFieldOrSchema.serialize, valueConverter=self._valueFieldOrSchema.serialize, **kwargs)

    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        return self._convert(incoming, skipValidation, keyConverter=self._keyFieldOrSchema.deserialize, valueConverter=self._valueFieldOrSchema.deserialize, **kwargs)

    def _convert(self, incoming, skipValidation, keyConverter, valueConverter, **kwargs):
        if not skipValidation and not isinstance(incoming, dict):
            raise ValidationError(b'Not a dict type.')
        converted, errors = {}, None
        kwargs[b'silent'] = False
        for key, value in viewitems(incoming):
            try:
                converted[keyConverter(key, skipValidation=skipValidation, **kwargs)] = valueConverter(value, skipValidation=skipValidation, **kwargs)
            except ValidationError as ve:
                error = ValidationErrorMessage(ve.error.data, title=(b'Dict[{}:{}]').format(key, value))
                errors = errors + error if errors else error

        if errors:
            raise ValidationError(errors)
        return converted


class HexColorCode(String):
    COLOR_CODE_RE = b'^#[A-Fa-f0-9]{6}$'
    __slots__ = ()

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(HexColorCode, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        validator = [
         validate.Regexp(self.COLOR_CODE_RE)]
        self._serializedValidators = validator + self._serializedValidators
        self._deserializedValidators = validator + self._deserializedValidators
        return


class ListFromString(Field):
    __slots__ = (b'_delimiter', b'_listOfFields', b'_stringField')

    def __init__(self, field, delimiter=None, required=True, default=list, filterParams=None, serializedValidators=None, deserializedValidators=None):
        super(ListFromString, self).__init__(required=required, default=default, filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._delimiter = delimiter
        self._listOfFields = List(field)
        self._stringField = String()
        return

    def _serialize(self, incoming, skipValidation=False, **kwargs):
        return (self._delimiter or b' ').join(str(v) for v in self._listOfFields.serialize(incoming, skipValidation=skipValidation, **kwargs))

    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        string = self._stringField.deserialize(incoming)
        return self._listOfFields.deserialize(self._splitString(string), skipValidation=skipValidation, **kwargs)

    def _splitString(self, string):
        if string:
            return [x.strip() for x in string.split(self._delimiter)]
        return []


class Vector2(ListFromString):
    __slots__ = ()
    _vectorClass = Math.Vector2
    _zeroVector = (0, 0)

    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        empty = self._zeroVector
        default = default or empty
        if len(default) != len(empty):
            raise SoftException((b'Vector length should be {}, not {}.').format(len(empty), len(default)))
        super(Vector2, self).__init__(field=Float(), required=required, default=(lambda : self._vectorClass(default)), filterParams=filterParams, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._deserializedValidators = [
         validate.Length(equalValue=len(empty))] + self._deserializedValidators
        return

    def deserialize(self, incoming, skipValidation=False, **kwargs):
        vector = super(Vector2, self).deserialize(incoming, skipValidation=False, **kwargs)
        return self._vectorClass(vector)

    def _serialize(self, incoming, skipValidation=False, **kwargs):
        if not isinstance(incoming, self._vectorClass):
            raise ValidationError((b'Only {} is supported.').format(self._vectorClass))
        return super(Vector2, self)._serialize(list(incoming), skipValidation=False, **kwargs)


class Vector3(Vector2):
    __slots__ = ()
    _vectorClass = Math.Vector3
    _zeroVector = (0, 0, 0)


class Vector4(Vector2):
    __slots__ = ()
    _vectorClass = Math.Vector4
    _zeroVector = (0, 0, 0, 0)
