from __future__ import absolute_import
import typing, re
from soft_exception import SoftException
from dict2model.exceptions import ValidationError, ValidationErrorMessage, CumulativeIterableValidationError
if typing.TYPE_CHECKING:
    from dict2model.types import ValidatorType, ValidatorsType

def prepareValidators(validators):
    prepared = []
    if isinstance(validators, (list, tuple)):
        prepared += list(validators)
    elif validators is not None:
        prepared.append(validators)
    errors = None
    for validator in prepared:
        if not callable(validator):
            error = ValidationErrorMessage((b'Unsupported validator type: {}.').format(type(validator)))
            errors = errors + error if errors else error

    if errors:
        raise SoftException(str(errors))
    return prepared


def runValidators(validations, toValidate):
    errors = None
    for validation in validations:
        try:
            validation(toValidate)
        except ValidationError as ve:
            errors = errors + ve.error if errors else ve.error

    if errors:
        raise ValidationError(errors)
    return


class Validator(object):
    __slots__ = ()

    def __call__(self, incoming, *args, **kwargs):
        return

    def __repr__(self):
        return (b'<{}({})>').format(self.__class__.__name__, self._reprArgs() or b'')

    def _reprArgs(self):
        return b''


class Range(Validator):
    _messageMin = b'Must be at least {min}.'
    _messageMax = b'Must be at most {max}.'
    _messageAll = b'Must be between {min} and {max}.'
    __slots__ = (b'_min', b'_max')

    def __init__(self, minValue=None, maxValue=None):
        self._min = minValue
        self._max = maxValue
        return

    def __call__(self, incoming, *args, **kwargs):
        if self._min is not None and incoming < self._min:
            message = self._messageMin if self._max is None else self._messageAll
            raise ValidationError(self._formatError(message))
        if self._max is not None and incoming > self._max:
            message = self._messageMax if self._min is None else self._messageAll
            raise ValidationError(self._formatError(message))
        return

    def _reprArgs(self):
        return (b'min={}, max={}').format(self._min, self._max)

    def _formatError(self, message):
        return message.format(min=self._min, max=self._max)


class Length(Range):
    _messageMin = b'Shorter than minimum length {min}.'
    _messageMax = b'Longer than maximum length {max}.'
    _messageAll = b'Length must be between {min} and {max}.'
    _messageEqual = b'Length must be {equal}.'
    __slots__ = (b'_equal',)

    def __init__(self, minValue=None, maxValue=None, equalValue=None):
        if equalValue is not None and any([minValue, maxValue]):
            raise SoftException(b'The `equal` parameter was provided, `max` or `min` parameter must not be provided.')
        super(Length, self).__init__(minValue, maxValue)
        self._equal = equalValue
        return

    def __call__(self, incoming, *args, **kwargs):
        length = len(incoming)
        if self._equal is not None:
            if length != self._equal:
                raise ValidationError(self._formatError(self._messageEqual))
            return
        super(Length, self).__call__(length)
        return

    def _reprArgs(self):
        return (b'min={}, max={}, equal={}').format(self._min, self._max, self._equal)

    def _formatError(self, message):
        return message.format(min=self._min, max=self._max, equal=self._equal)


class URL(Validator):

    class RegexMemoizer(object):
        __slots__ = (b'_memoized',)

        def __init__(self):
            self._memoized = {}
            return

        def __call__(self, relative, requireTld):
            key = (
             relative, requireTld)
            if key not in self._memoized:
                self._memoized[key] = self._regexGenerator(relative, requireTld)
            return self._memoized[key]

        @staticmethod
        def _regexGenerator(relative, requireTld):
            return re.compile((b'').join((
             b'^',
             b'(' if relative else b'',
             b'(?:[a-z0-9\\.\\-\\+]*)://',
             b'(?:[^:@]+?(:[^:@]*?)?@|)',
             b'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+',
             b'(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?)|',
             b'localhost|',
             b'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.?)|' if not requireTld else b'',
             b'\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}|',
             b'\\[?[A-F0-9]*:[A-F0-9:]+\\]?)',
             b'(?::\\d+)?',
             b')?' if relative else b'',
             b'(?:/?|[/?]\\S+)\\Z')), re.IGNORECASE)

    _regex = RegexMemoizer()
    _message = b'Not a valid URL.'
    _schemes = {b'http', b'https', b'ftp', b'ftps'}
    __slots__ = (b'relative', b'requireTld')

    def __init__(self, relative=False, requireTld=True):
        self.relative = relative
        self.requireTld = requireTld
        return

    def __call__(self, incoming, *args, **kwargs):
        if not incoming:
            raise ValidationError(self._message)
        if b'://' in incoming:
            scheme = incoming.split(b'://')[0].lower()
            if scheme not in self._schemes:
                raise ValidationError(self._message)
        regex = self._regex(self.relative, self.requireTld)
        if not regex.search(incoming):
            raise ValidationError(self._message)
        return

    def _reprArgs(self):
        return (b'relative={}').format(self.relative)


class NoneOf(Validator):
    _message = b'Value: {value} must not be one of: {values}.'
    __slots__ = (b'_choices', b'_choicesText')

    def __init__(self, choices):
        self._choices = choices
        self._choicesText = (b', ').join(str(each) for each in self._choices)
        return

    def __call__(self, incoming, *args, **kwargs):
        try:
            if incoming in self._choices:
                raise ValidationError(self._message.format(value=incoming, values=self._choicesText))
        except TypeError:
            pass

        return

    def _reprArgs(self):
        return (b'choices={}').format(self._choices)


class OneOf(NoneOf):
    _message = b'Value: {value} must be one of: {values}.'
    __slots__ = ()

    def __call__(self, incoming, *args, **kwargs):
        try:
            if incoming not in self._choices:
                raise ValidationError(self._message.format(value=incoming, values=self._choicesText))
        except TypeError:
            raise ValidationError(self._message.format(value=incoming, values=self._choicesText))

        return


class Regexp(Validator):
    _message = b'String: {value} does not match pattern: {pattern}.'
    __slots__ = (b'_regex',)

    def __init__(self, regex, flags=0):
        self._regex = re.compile(regex, flags) if isinstance(regex, str) else regex
        return

    def __call__(self, incoming, *args, **kwargs):
        if self._regex.match(incoming) is None:
            raise ValidationError(self._message.format(value=incoming, pattern=self._regex.pattern))
        return

    def _reprArgs(self):
        return (b'regex={}').format(self._regex.pattern)


class IterableValidator(Validator):
    __slots__ = ()

    def __call__(self, incoming, storage, isLastIteration, *args, **kwargs):
        return

    def createStorage(self):
        return {}


class _IterableAttrValidator(IterableValidator):
    __slots__ = (b'_attrName',)

    def __init__(self, attrName=None):
        self._attrName = attrName
        return

    def getValue(self, incoming):
        if self._attrName is not None and not hasattr(incoming, self._attrName):
            raise ValidationError((b'Incoming {} does not have attribute {}').format(incoming, self._attrName))
        if self._attrName is None:
            return incoming
        else:
            return getattr(incoming, self._attrName)


class IterableOfUnique(_IterableAttrValidator):
    __slots__ = ()

    def __call__(self, incoming, storage, *args, **kwargs):
        value = self.getValue(incoming)
        if value not in storage:
            storage.add(value)
        else:
            raise ValidationError((b'Value {} of {} is duplicate.').format(value, self._attrName))
        return

    def createStorage(self):
        return set()


class IterableOfSequential(_IterableAttrValidator):
    __slots__ = (b'_firstValue',)

    def __init__(self, attrName=None, firstValue=1):
        super(IterableOfSequential, self).__init__(attrName)
        self._firstValue = firstValue
        return

    def __call__(self, incoming, storage, *args, **kwargs):
        value = self.getValue(incoming)
        isMismatch = value != storage[0]
        storage[0] += 1
        if isMismatch:
            raise ValidationError((b'Value {}  of {} is out of order').format(value, self._attrName))
        return

    def createStorage(self):
        return [self._firstValue]


class IterableAnyTrue(_IterableAttrValidator):
    __slots__ = ()

    def __call__(self, incoming, storage, lastIteration, *args, **kwargs):
        value = self.getValue(incoming)
        storage[0] |= value
        if lastIteration and not storage[0]:
            raise CumulativeIterableValidationError((b'At least one of {} must be True.').format(self._attrName))
        return

    def createStorage(self):
        return [False]


class ValidateIterable(Validator):
    __slots__ = (b'_validators', b'_storageCreator')

    def __init__(self, validators, storageCreator=dict):
        self._validators = validators
        self._storageCreator = storageCreator
        return

    def __call__(self, incoming, *args, **kwargs):
        storages = {}
        errors = None
        lastIndex = len(incoming) - 1
        for index, elem in enumerate(incoming):
            lastIteration = index == lastIndex
            for validator in self._validators:
                try:
                    validatorId = id(validator)
                    if validatorId in storages:
                        storage = storages[validatorId]
                    else:
                        if isinstance(validator, IterableValidator):
                            storage = validator.createStorage()
                        else:
                            storage = self._storageCreator()
                        storages[validatorId] = storage
                    validator(elem, storage, lastIteration)
                except CumulativeIterableValidationError as ve:
                    errors = errors + ve.error if errors else ve.error
                except ValidationError as ve:
                    error = ValidationErrorMessage(ve.error.data, title=(b'Elem[{}]').format(index))
                    errors = errors + error if errors else error

        if errors is not None:
            raise ValidationError(errors)
        return
