import BigWorld
from block import Block, Meta, InitParam, buildStrKeysValue, makeResEditorData
from slot_types import SLOT_TYPE, arrayOf
from misc import ASPECT, BLOCK_MODE, EDITOR_TYPE
from constants import IS_DEVELOPMENT

class QAMeta(Meta):

    @classmethod
    def blockCategory(cls):
        return b'QA Blocks'

    @classmethod
    def blockColor(cls):
        return 10375605

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/debug'

    @classmethod
    def mode(cls):
        return BLOCK_MODE.DEV


class TestIdentifier(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(TestIdentifier, self).__init__(*args, **kwargs)
        self._nameType, = self._getInitParams()
        if self._nameType == b'single id':
            self.inInt = self._makeDataInputSlot(b'test_id', SLOT_TYPE.INT)
            self.outID = self._makeDataOutputSlot(b'Identifier', SLOT_TYPE.ID, self._execute)
        elif self._nameType == b'array of IDs':
            self.inInt = self._makeDataInputSlot(b'multiple_test_ids', arrayOf(SLOT_TYPE.INT))
            self.outID = self._makeDataOutputSlot(b'Array of Identifiers', arrayOf(SLOT_TYPE.ID), self._execute)
        return

    def _execute(self):
        res = self.inInt.getValue()
        self.outID.setValue(res)
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'amount of test IDs', SLOT_TYPE.STR, buildStrKeysValue(b'single id', b'array of IDs'), EDITOR_TYPE.STR_KEY_SELECTOR)]


class TestSlotPyObjectToArrayVSEBlock(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(TestSlotPyObjectToArrayVSEBlock, self).__init__(*args, **kwargs)
        self._res = self._makeDataOutputSlot(b'res', arrayOf(SLOT_TYPE.STR), self._exec)
        return

    def _exec(self):
        self._res.setValue(set([1, 2, 3]))
        return


class Assert(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(Assert, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', Assert._execute)
        self._value = self._makeDataInputSlot(b'value', SLOT_TYPE.BOOL)
        self._msg = self._makeDataInputSlot(b'msg', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        self._out.call()
        return


class AddTestResult(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(AddTestResult, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._success = self._makeDataInputSlot(b'success', SLOT_TYPE.BOOL)
        self._msg = self._makeDataInputSlot(b'msg', SLOT_TYPE.STR)
        self._arena = self._makeDataInputSlot(b'arena', SLOT_TYPE.ARENA)
        self._out = self._makeEventOutputSlot(b'out')
        return

    @property
    def _storageKey(self):
        arena = self._arena.getValue()
        runnerID = arena.ai.gameMode.arenaInfo.runnerID
        return b'runnerID_%d' % runnerID

    def _execute(self):
        if not IS_DEVELOPMENT:
            return
        BigWorld.globalData[self._storageKey][b'results'].append(dict(success=self._success.getValue(), message=self._msg.getValue()))
        BigWorld.globalData[self._storageKey] = BigWorld.globalData[self._storageKey]
        self._out.call()
        return

    def onStartScript(self):
        if not IS_DEVELOPMENT:
            return
        arena = self._arena.getValue()
        BigWorld.globalData[self._storageKey] = dict(arenaID=arena.id, results=[])
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]


class TestCase(Block):

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', TestCase._execute)
        self._name = self._makeDataInputSlot(b'name', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        self._out.call()
        return
