from __future__ import absolute_import, division
import math
from visual_script.block import Block
from visual_script.qa_blocks import QAMeta
from visual_script.slot_types import SLOT_TYPE

class CheckTriangleLesson1(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(CheckTriangleLesson1, self).__init__(*args, **kwargs)
        self._a = self._makeDataInputSlot(b'a', SLOT_TYPE.FLOAT)
        self._b = self._makeDataInputSlot(b'b', SLOT_TYPE.FLOAT)
        self._c = self._makeDataOutputSlot(b'c', SLOT_TYPE.FLOAT, self._ex_c)
        self._S = self._makeDataOutputSlot(b'S', SLOT_TYPE.FLOAT, self._ex_s)
        return

    def _ex_c(self):
        self._c.setValue(math.sqrt(self._a.getValue() ** 2 + self._b.getValue() ** 2))
        return

    def _ex_s(self):
        self._S.setValue(0.5 * self._a.getValue() * self._b.getValue())
        return

    def validate(self):
        if not self._a.hasValue():
            return b'a value is required'
        if not self._b.hasValue():
            return b'b value is required'
        return b''

    @classmethod
    def blockCategory(cls):
        return b'QA Education Blocks'


class CheckTriangleLesson2(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(CheckTriangleLesson2, self).__init__(*args, **kwargs)
        self._r = self._makeDataInputSlot(b'r', SLOT_TYPE.FLOAT)
        self._S = self._makeDataInputSlot(b'S', SLOT_TYPE.FLOAT)
        self._a = self._makeDataOutputSlot(b'a', SLOT_TYPE.FLOAT, self._ex_a)
        self._b = self._makeDataOutputSlot(b'b', SLOT_TYPE.FLOAT, self._ex_b)
        self._c = self._makeDataOutputSlot(b'c', SLOT_TYPE.FLOAT, self._ex_c)
        return

    def _ex_a(self):
        self._a.setValue(0.5 * (self._r.getValue() + self._S.getValue() / self._r.getValue() - math.sqrt(self._r.getValue() ** 2 - 6 * self._S.getValue() + self._S.getValue() ** 2 / self._r.getValue() ** 2)))
        return

    def _ex_b(self):
        self._b.setValue(0.5 * (self._r.getValue() + self._S.getValue() / self._r.getValue() + math.sqrt(self._r.getValue() ** 2 - 6 * self._S.getValue() + self._S.getValue() ** 2 / self._r.getValue() ** 2)))
        return

    def _ex_c(self):
        self._c.setValue(self._S.getValue() / self._r.getValue() - self._r.getValue())
        return

    def validate(self):
        if not self._r.hasValue():
            return b'r value is required'
        if not self._S.hasValue():
            return b'S value is required'
        return b''

    @classmethod
    def blockCategory(cls):
        return b'QA Education Blocks'
