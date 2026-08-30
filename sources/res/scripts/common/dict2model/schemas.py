from __future__ import absolute_import
import typing, logging
from future.utils import viewitems
from soft_exception import SoftException
from dict2model import validate
from dict2model.models import Model
from dict2model.exceptions import ValidationError, ValidationErrorMessage
from dict2model.fields import AccessDeniedField
if typing.TYPE_CHECKING:
    from dict2model.fields import Field
    from dict2model.types import ValidatorsType, SchemaModelClassesType, SchemaModelTypes
_logger = logging.getLogger(__name__)
accessDeniedField = AccessDeniedField()

class Schema(object):
    __slots__ = (b'_modelClass', b'_checkUnknown', b'_fields', b'_serializedValidators', b'_deserializedValidators')

    def __init__(self, fields, modelClass=dict, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        if not issubclass(modelClass, (Model, dict)):
            raise SoftException(b'ClassModel is not Model or dict.')
        self._fields = dict(fields)
        self._modelClass = modelClass
        self._checkUnknown = checkUnknown
        self._serializedValidators = validate.prepareValidators(serializedValidators)
        self._deserializedValidators = validate.prepareValidators(deserializedValidators)
        return

    def serialize(self, incoming, onlyPublic=False, silent=False, logError=True):
        try:
            if not isinstance(incoming, self._modelClass):
                raise ValidationError((b'Data not a {} type.').format(self._modelClass))
            modelAsDict = incoming.toDict() if isinstance(incoming, Model) else incoming
            result = self._serialize(modelAsDict, onlyPublic=onlyPublic)
            validate.runValidators(self._serializedValidators, result)
            return result
        except Exception as errors:
            if not silent:
                raise
            if logError:
                _logger.error(b'Serialized validation errors: %s.', errors)

        return

    def deserialize(self, incoming, onlyPublic=False, silent=False, logError=True):
        try:
            if not isinstance(incoming, dict):
                raise ValidationError(b'Data not a dict type.')
            if self._checkUnknown:
                unknown = set(incoming) - set(self._fields)
                if unknown:
                    raise ValidationError((b'Unexpected attributes: {}.').format(unknown))
            result = self._deserialize(incoming, onlyPublic=onlyPublic)
            validate.runValidators(self._deserializedValidators, result)
            return result
        except Exception as errors:
            if not silent:
                raise
            if logError:
                _logger.error(b'Deserialized validation errors: %s.', errors)

        return

    def _serialize(self, incoming, onlyPublic=False):
        serialized, errors = {}, None
        for name, field in viewitems(self._fields):
            try:
                if onlyPublic and not field.public:
                    continue
                if name not in incoming:
                    if field.required:
                        raise ValidationError((b'Required attribute: {} missing.').format(name))
                elif not field.required:
                    default = field.default() if callable(field.default) else field.default
                    if incoming[name] == default:
                        continue
                serialized[name] = field.serialize(incoming[name], onlyPublic=onlyPublic)
            except ValidationError as ve:
                error = ValidationErrorMessage(ve.error.data, title=(b'Field({})').format(name))
                errors = errors + error if errors else error

        if errors:
            raise ValidationError(errors)
        return serialized

    def _deserialize(self, incoming, onlyPublic=False):
        deserialized, errors = {}, None
        for name, field in viewitems(self._fields):
            try:
                if onlyPublic and not field.public:
                    deserialized[name] = accessDeniedField
                elif name not in incoming:
                    if field.required:
                        raise ValidationError((b'Required attribute: {} missing.').format(name))
                    default = field.default() if callable(field.default) else field.default
                    deserialized[name] = default
                else:
                    deserialized[name] = field.deserialize(incoming[name], onlyPublic=onlyPublic)
            except ValidationError as ve:
                error = ValidationErrorMessage(ve.error.data, title=(b'Field({})').format(name))
                errors = errors + error if errors else error

        if errors:
            raise ValidationError(errors)
        try:
            return self._modelClass(**deserialized)
        except Exception as error:
            raise ValidationError((b'Model creation error: {}').format(error))

        return
