import base64, cPickle, weakref
from visual_script.block import Block, InitParam, EDITOR_TYPE, buildStrKeysValue, Meta
from visual_script.misc import ASPECT, errorVScript
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.type import VScriptType
from debug_utils import LOG_ERROR
from Math import Vector2, Vector3, Vector4, Matrix

class DictionaryMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 11777386

    @classmethod
    def blockCategory(cls):
        return b'Dictionary'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/python'


class Dictionary(VScriptType, dict):

    def __init__(self, storage=None):
        super(Dictionary, self).__init__()
        if storage:
            self.update(storage)
        return

    @classmethod
    def vs_toString(cls, value):
        if value:
            return base64.b64encode(cPickle.dumps(value, -1))
        else:
            return b''

        return

    @classmethod
    def vs_fromString(cls, str_):
        try:
            if str_:
                return cPickle.loads(base64.b64decode(str_))
        except Exception as e:
            LOG_ERROR(b'[VScript]', b'Error of load Dictionary from string: %s' % e.message)

        return Dictionary()

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]

    @classmethod
    def vs_connectionColor(cls):
        return 11777386


ALLOWED_DATA_TYPES = {b'String': (
             str,), 
   b'Bool': (
           bool,), 
   b'Int': (
          int, long), 
   b'Float': (
            float,), 
   b'Vehicle': (
              weakref.ProxyType,), 
   b'Dictionary': (
                 dict, Dictionary), 
   b'Vector2': (
              Vector2,), 
   b'Vector3': (
              Vector3,), 
   b'Vector4': (
              Vector4,), 
   b'Matrix4': (
              Matrix,)}

class EmptyDictionary(Block, DictionaryMeta):

    def __init__(self, *args, **kwargs):
        super(EmptyDictionary, self).__init__(*args, **kwargs)
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.DICTIONARY, self._get)
        return

    def _get(self):
        return Dictionary()

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]


class AddToDictionary(Block, DictionaryMeta):

    def __init__(self, *args, **kwargs):
        super(AddToDictionary, self).__init__(*args, **kwargs)
        self._valueType, self._isArray = self._getInitParams()
        if self._isArray:
            self._valueType = arrayOf(self._valueType)
        self._in = self._makeEventInputSlot(b'in', self._exec)
        self._dict = self._makeDataInputSlot(b'dict', SLOT_TYPE.DICTIONARY)
        self._key = self._makeDataInputSlot(b'key', SLOT_TYPE.STR)
        self._value = self._makeDataInputSlot(b'value', self._valueType)
        self._override = self._makeDataInputSlot(b'override', SLOT_TYPE.BOOL)
        self._out = self._makeEventOutputSlot(b'out')
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.DICTIONARY, None)
        return

    def _exec(self):
        res = Dictionary(self._dict.getValue())
        key = self._key.getValue()
        value = self._value.getValue()
        override = self._override.getValue()
        if override or key not in res:
            res[key] = value
        self._res.setValue(res)
        self._out.call()
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Value type', SLOT_TYPE.STR, buildStrKeysValue(*ALLOWED_DATA_TYPES.iterkeys()), EDITOR_TYPE.STR_KEY_SELECTOR),
         InitParam(b'Is Array', SLOT_TYPE.BOOL, False)]

    def captionText(self):
        return (b'Add To Dictionary: {}').format(self._valueType)

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]


class IsInDictionary(Block, DictionaryMeta):

    def __init__(self, *args, **kwargs):
        super(IsInDictionary, self).__init__(*args, **kwargs)
        self._valueType, = self._getInitParams()
        self._dict = self._makeDataInputSlot(b'dict', SLOT_TYPE.DICTIONARY)
        self._key = self._makeDataInputSlot(b'key', SLOT_TYPE.STR)
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._checkKey)
        return

    def _checkKey(self):
        keyValueStorage = self._dict.getValue()
        key = self._key.getValue()
        if key in keyValueStorage:
            valueType = type(keyValueStorage[key])
            if valueType in ALLOWED_DATA_TYPES[self._valueType]:
                self._res.setValue(True)
                return
        self._res.setValue(False)
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Value type', SLOT_TYPE.STR, buildStrKeysValue(*ALLOWED_DATA_TYPES.iterkeys()), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def captionText(self):
        return (b'Is In Dictionary: {}').format(self._valueType)

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]


class GetFromDictionary(Block, DictionaryMeta):

    def __init__(self, *args, **kwargs):
        super(GetFromDictionary, self).__init__(*args, **kwargs)
        self._valueType, self._isArray = self._getInitParams()
        self._dict = self._makeDataInputSlot(b'dict', SLOT_TYPE.DICTIONARY)
        self._key = self._makeDataInputSlot(b'key', SLOT_TYPE.STR)
        self._value = self._makeDataOutputSlot(b'value', arrayOf(self._valueType), self._getArrayValue) if self._isArray else self._makeDataOutputSlot(b'value', self._valueType, self._getValue)
        return

    def _getArrayValue(self):
        keyValueStorage = self._dict.getValue()
        key = self._key.getValue()
        if key not in keyValueStorage:
            errorVScript(self, (b'Key {} is missing in the Dictionary').format(key))
            return
        value = keyValueStorage[key]
        valueType = type(value)
        if valueType not in (list, tuple):
            errorVScript(self, (b'Value type mismatch for key {} in the Dictionary.Expected {}, received {}').format(key, b'list or tuple', valueType))
            return
        if value and type(value[0]) not in ALLOWED_DATA_TYPES[self._valueType]:
            errorVScript(self, (b'List value type mismatch for key {} in the Dictionary.Expected {}, received {}').format(key, self._valueType, type(value[0])))
            return
        if valueType is dict:
            self._value.setValue([Dictionary(val) for val in value])
        else:
            self._value.setValue(value)
        return

    def _getValue(self):
        keyValueStorage = self._dict.getValue()
        key = self._key.getValue()
        if key in keyValueStorage:
            value = keyValueStorage[key]
            valueType = type(value)
            if valueType in ALLOWED_DATA_TYPES[self._valueType]:
                if valueType is dict:
                    self._value.setValue(Dictionary(value))
                else:
                    self._value.setValue(value)
            else:
                errorVScript(self, (b'Value type mismatch for key {} in the Dictionary. Expected {}, received {}').format(key, self._valueType, valueType))
        else:
            errorVScript(self, (b'Key {} is missing in the Dictionary').format(key))
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Value type', SLOT_TYPE.STR, buildStrKeysValue(*ALLOWED_DATA_TYPES.iterkeys()), EDITOR_TYPE.STR_KEY_SELECTOR),
         InitParam(b'Is Array', SLOT_TYPE.BOOL, False)]

    def captionText(self):
        return (b'Get From Dictionary: {}').format(arrayOf(self._valueType) if self._isArray else self._valueType)

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]
