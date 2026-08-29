from __future__ import absolute_import
import typing, enum
from datetime import datetime
from soft_exception import SoftException
from dict2model import utils
from dict2model import validate
from dict2model.exceptions import ValidationError, ValidationErrorMessage, AccessToFieldDeniedError
if typing.TYPE_CHECKING:
    from dict2model.types import ValidatorsType, SchemaModelTypes
    from dict2model.schemas import Schema

class AccessDeniedField(object):

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
        return b'AccessToFieldDenied'


class Field(object):
    __slots__ = (b'required', b'default', b'public', b'_serializedValidators', b'_deserializedValidators')

    def __init__(self, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None):
        self.required = required
        self.default = default
        self.public = public
        self._serializedValidators = validate.prepareValidators(serializedValidators)
        self._deserializedValidators = validate.prepareValidators(deserializedValidators)
        return

    def serialize(self, incoming, **kwargs):
        result = self._serialize(incoming, **kwargs)
        validate.runValidators(self._serializedValidators, result)
        return result

    def deserialize(self, incoming, **kwargs):
        result = self._deserialize(incoming, **kwargs)
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

    def _serialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _deserialize(self, incoming, **kwargs):
        return self._convert(incoming)

    @staticmethod
    def _convert(incoming):
        if not isinstance(incoming, utils.baseStringTypes):
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

    def __init__(self, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None, serializeAsString=False):
        super(Number, self).__init__(required=required, default=default, public=public, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._serializeAsString = serializeAsString
        return

    def serialize(self, incoming, **kwargs):
        result = super(Number, self).serialize(incoming)
        if self._serializeAsString:
            return self._toString(result)
        return result

    def _serialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _deserialize(self, incoming, **kwargs):
        return self._convert(incoming)

    def _convert(self, incoming):
        try:
            return self._formatNumber(incoming)
        except (TypeError, ValueError):
            raise ValidationError(b'Not a valid number.')
        except OverflowError:
            raise ValidationError(b'Number too large.')

        return

    def _formatNumber(self, value):
        return self.numberType(value)

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

    def __init__(self, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None, localtime=False):
        super(DateTime, self).__init__(required=required, default=default, public=public, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
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

    def __init__(self, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None, relative=False):
        super(Url, self).__init__(required=required, default=default, public=public, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._relative = relative
        self._serializedValidators = [validate.URL(relative=self._relative)] + list(self._serializedValidators)
        self._deserializedValidators = [validate.URL(relative=self._relative)] + list(self._deserializedValidators)
        return


class Enum(Field):
    __slots__ = (b'_enumClass',)

    def __init__(self, enumClass, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None):
        super(Enum, self).__init__(required=required, default=default, public=public, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._enumClass = enumClass
        return

    def _serialize(self, incoming, **kwargs):
        if not isinstance(incoming, self._enumClass):
            raise ValidationError((b'Not a enum: {} class.').format(self._enumClass))
        return incoming.value

    def _deserialize(self, incoming, **kwargs):
        try:
            return self._enumClass(incoming)
        except ValueError:
            enumValues = [obj.value for obj in self._enumClass.__members__.values()]
            raise ValidationError((b'Value: {} must be one of: {}.').format(incoming, enumValues))

        return


class Nested(Field):
    __slots__ = (b'_schema',)

    def __init__(self, schema, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None):
        super(Nested, self).__init__(required=required, default=default, public=public, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._schema = schema
        return

    def _serialize(self, incoming, onlyPublic=False):
        return self._schema.serialize(incoming, onlyPublic=False, silent=False)

    def _deserialize(self, incoming, onlyPublic=False):
        return self._schema.deserialize(incoming, onlyPublic=False, silent=False)


class List(Field):
    __slots__ = (b'_fieldOrSchema',)

    def __init__(self, fieldOrSchema, required=True, default=None, public=True, serializedValidators=None, deserializedValidators=None):
        super(List, self).__init__(required=required, default=default, public=public, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators)
        self._fieldOrSchema = fieldOrSchema
        return

    def _serialize(self, incoming, onlyPublic=False):
        return self._convert(incoming, onlyPublic, method=b'serialize')

    def _deserialize(self, incoming, onlyPublic=False):
        return self._convert(incoming, onlyPublic, method=b'deserialize')

    def _convert(self, incoming, onlyPublic, method):
        if not isinstance(incoming, (list, tuple)):
            raise ValidationError(b'Not a list type.')
        converted, errors = [], None
        for index, value in enumerate(incoming):
            try:
                converter = getattr(self._fieldOrSchema, method, None)
                if converter is None:
                    raise ValidationError((b'{} method {} not found.').format(self._fieldOrSchema, method))
                converted.append(converter(value, onlyPublic=onlyPublic, silent=False))
            except ValidationError as ve:
                error = ValidationErrorMessage(ve.error.data, title=(b'List[{}]').format(index))
                errors = errors + error if errors else error

        if errors:
            raise ValidationError(errors)
        return converted


class UniCapList(List):

    def _convert(self, incoming, onlyPublic, method):
        if not isinstance(incoming, (list, tuple)):
            incoming = [
             incoming]
        return super(UniCapList, self)._convert(incoming, onlyPublic, method)
