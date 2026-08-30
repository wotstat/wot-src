from block import Block, makeResEditorData, InitParam
from constants import GAME_ROOT_DIR_NAME
from slot_types import SLOT_TYPE
from uuid_utils import genUUID

class ResourceSelector(Block):

    def __init__(self, *args, **kwargs):
        super(ResourceSelector, self).__init__(*args, **kwargs)
        root, ext = self._getInitParams()
        self._res = self._makeDataInputSlot(b'res', SLOT_TYPE.RESOURCE)
        self._res.setEditorData(makeResEditorData(root, ext))
        self._out = self._makeDataOutputSlot(b'out', SLOT_TYPE.RESOURCE, self._exec)
        return

    def _exec(self):
        self._out.setValue(self._res.getValue())
        return

    @classmethod
    def initParams(cls):
        return [InitParam(b'root', SLOT_TYPE.STR, GAME_ROOT_DIR_NAME), InitParam(b'ext', SLOT_TYPE.STR, b'xml')]


class GenerateUniqueString(Block):

    def __init__(self, *args, **kwargs):
        super(GenerateUniqueString, self).__init__(*args, **kwargs)
        self._prefix = self._makeDataInputSlot(b'prefix', SLOT_TYPE.STR)
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.STR, self._getData)
        return

    @classmethod
    def hasValidation(cls):
        return True

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/text'

    @classmethod
    def blockCategory(cls):
        return b'Strings'

    def _getData(self):
        prefix = self._prefix.getValue() if self._prefix.hasValue() else b''
        self._res.setValue((b'{prefix}_{ts}').format(prefix=prefix, ts=genUUID().time))
        return
