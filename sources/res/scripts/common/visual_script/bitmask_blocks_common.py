from visual_script.block import Block, InitParam, buildStrKeysValue, Meta
from visual_script.misc import errorVScript, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE

class BitMaskMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 4202496

    @classmethod
    def blockCategory(cls):
        return b'Bit Mask'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/automation'


class BitMaskBase(Block, BitMaskMeta):
    _MASK_TYPES = {}

    def __init__(self, *args, **kwargs):
        super(BitMaskBase, self).__init__(*args, **kwargs)
        self._flags = []
        flagsCount, bitMaskType = self._getInitParams()
        type = self._MASK_TYPES[bitMaskType]
        self._inFlags = {name: getattr(type, name) for name, value in type.__dict__.iteritems() if not name.startswith(b'_')}
        for _ in xrange(flagsCount):
            self._addInputNode()

        self._bitMask = self._makeDataOutputSlot(bitMaskType, SLOT_TYPE.INT, self._getValue)
        return

    def _addInputNode(self):
        self._flags.append(self._makeDataInputSlot(b'f' + str(len(self._flags)), SLOT_TYPE.STR, EDITOR_TYPE.ENUM_SELECTOR))
        self._flags[-1].setEditorData([name for name in self._inFlags.iterkeys()])
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Flags Count', SLOT_TYPE.INT, 1),
         InitParam(b'BitMask type', SLOT_TYPE.STR, buildStrKeysValue(*cls._MASK_TYPES.keys()), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def _getValue(self):
        bitMask = 0
        for f in self._flags:
            if f.hasValue():
                bitMask |= self._inFlags[f.getValue()]
            else:
                errorVScript(self, b'Not all input flags are specified')

        self._bitMask.setValue(bitMask)
        return


class BitwiseNOT(Block, BitMaskMeta):

    def __init__(self, *args, **kwargs):
        super(BitwiseNOT, self).__init__(*args, **kwargs)
        self._a = self._makeDataInputSlot(b'a', SLOT_TYPE.INT)
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.INT, self._getValue)
        return

    def _getValue(self):
        self._res.setValue(~self._a.getValue())
        return


class BitwiseOperationBase(Block, BitMaskMeta):

    def __init__(self, *args, **kwargs):
        super(BitwiseOperationBase, self).__init__(*args, **kwargs)
        self._masks = []
        masksCount, = self._getInitParams()
        for _ in xrange(masksCount):
            self._addInputNode()

        self._addOutputNode()
        return

    @classmethod
    def initParams(cls):
        return [InitParam(b'Masks Count', SLOT_TYPE.INT, 1)]

    @property
    def _maskValues(self):
        return [long(m.getValue()) for m in self._masks]

    def _addInputNode(self):
        self._masks.append(self._makeDataInputSlot(b'm' + str(len(self._masks)), SLOT_TYPE.INT))
        return

    def _addOutputNode(self):
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.INT, self._getValue)
        return

    def _getValue(self):
        raise NotImplementedError
        return


class BitwiseAND(BitwiseOperationBase):

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(reduce(long.__and__, masks[1:], masks[0]))
        return


class BitwiseOR(BitwiseOperationBase):

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(reduce(long.__or__, masks[1:], masks[0]))
        return


class BitwiseXOR(BitwiseOperationBase):

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(reduce(long.__xor__, masks[1:], masks[0]))
        return


class BitwiseEQUAL(BitwiseOperationBase):

    def _addOutputNode(self):
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._getValue)
        return

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(all(m == masks[0] for m in masks[1:]))
        return
