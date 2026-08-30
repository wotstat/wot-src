import BigWorld
from block import Block, Meta, InitParam, buildStrKeysValue, makeResEditorData
from slot_types import SLOT_TYPE, arrayOf
from visual_script.misc import ASPECT, BLOCK_MODE, EDITOR_TYPE
from tunable_event_block import TunableEventBlock
from type import VScriptType, VScriptEnum, VScriptStruct, VScriptStructField
import weakref

class Example(Meta):

    @classmethod
    def blockCategory(cls):
        return b'Example'

    @classmethod
    def mode(cls):
        return BLOCK_MODE.DEV


class HelloFromPython(Block, Example):

    def __init__(self, *args, **kwargs):
        super(HelloFromPython, self).__init__(*args, **kwargs)
        self._inSlot = self._makeDataInputSlot(b'project_name', SLOT_TYPE.STR)
        self._outSlot = self._makeDataOutputSlot(b'result', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        res = (b' ').join((b'Hello', self._inSlot.getValue(), b'from python vse...'))
        self._outSlot.setValue(res)
        return


class HelloFromPythonOverride(HelloFromPython):

    def _execute(self):
        res = (b' ').join((b'(Override) Hello', self._inSlot.getValue(), b'from python vse...'))
        self._outSlot.setValue(res)
        return


class StringSelectorExample(Block, Example):

    def __init__(self, *args, **kwargs):
        super(StringSelectorExample, self).__init__(*args, **kwargs)
        self._inSlot = self._makeDataInputSlot(b'in_slot', SLOT_TYPE.STR, EDITOR_TYPE.ENUM_SELECTOR)
        self._inSlot.setEditorData([b'my string 1', b'my string 2', b'my string 3'])
        self._outSlot = self._makeDataOutputSlot(b'result', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        res = (b' ').join((b'String', self._inSlot.getValue(), b'was selected'))
        self._outSlot.setValue(res)
        return


class GetProjectName(Block, Example):

    def __init__(self, *args, **kwargs):
        super(GetProjectName, self).__init__(*args, **kwargs)
        self._outSlot = self._makeDataOutputSlot(b'result', SLOT_TYPE.STR, GetProjectName._execute)
        return

    def _execute(self):
        self._outSlot.setValue(b'MT')
        return


class PrintToTerminal(Block, Example):

    def __init__(self, *args, **kwargs):
        super(PrintToTerminal, self).__init__(*args, **kwargs)
        self._inSlot = self._makeEventInputSlot(b'in', PrintToTerminal._execute)
        self._outSlot = self._makeEventOutputSlot(b'out')
        self._msgSlot = self._makeDataInputSlot(b'msg', SLOT_TYPE.STR)
        return

    def _execute(self):
        self._writeLog(b'PrintToTerminal:MSG = ' + self._msgSlot.getValue())
        self._outSlot.call()
        return


class MulArray(Block, Example):

    def __init__(self, *args, **kwargs):
        super(MulArray, self).__init__(*args, **kwargs)
        self._mulValue = self._makeDataInputSlot(b'mulVal', SLOT_TYPE.INT)
        self._arrayIn = self._makeDataInputSlot(b'array', arrayOf(SLOT_TYPE.INT))
        self._arrayOut = self._makeDataOutputSlot(b'res_array', arrayOf(SLOT_TYPE.INT), MulArray._execute)
        return

    def _execute(self):
        array = self._arrayIn.getValue()
        mul = self._mulValue.getValue()
        array = map((lambda v: v * mul), array)
        self._arrayOut.setValue(array)
        return


class SumArray(Block, Example):

    def __init__(self, *args, **kwargs):
        super(SumArray, self).__init__(*args, **kwargs)
        self._inArray = self._makeDataInputSlot(b'array', arrayOf(SLOT_TYPE.FLOAT))
        self._out = self._makeDataOutputSlot(b'res', SLOT_TYPE.FLOAT, SumArray._execute)
        return

    def _execute(self):
        res = sum(self._inArray.getValue(), 0.0)
        self._out.setValue(res)
        return


class WeightSequence(Block, Example):

    def __init__(self, *args, **kwargs):
        super(WeightSequence, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', WeightSequence._execute)
        n, = self._getInitParams()
        self._weightSlots = [self._makeDataInputSlot(b'w' + str(i), SLOT_TYPE.FLOAT) for i in xrange(n)]
        self._outSlots = [self._makeEventOutputSlot(b'out' + str(i)) for i in xrange(n)]
        return

    def _execute(self):
        iterData = ((slot.getValue(), idx) for idx, slot in enumerate(self._weightSlots))
        for _, idx in sorted(iterData, key=(lambda data: data[0]), reverse=True):
            self._outSlots[idx].call()

        return

    @classmethod
    def initParams(cls):
        return [InitParam(b'outCount', SLOT_TYPE.INT, 1)]


class SelectProjectID(Block, Example):
    convert = {b'MT': 0, 
       b'MK': 2}

    def __init__(self, *args, **kwargs):
        super(SelectProjectID, self).__init__(*args, **kwargs)
        self.outSlot = self._makeDataOutputSlot(b'get', SLOT_TYPE.INT, None)
        self._name, = self._getInitParams()
        self.outSlot.setValue(SelectProjectID.convert[self._name])
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Names', SLOT_TYPE.STR, buildStrKeysValue(*cls.convert.keys()), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def captionText(self):
        return (b' : ').join((self.__class__.__name__, self._name))


class AnimalComplexKeySelect(Block, Example):
    animals = [
     (
      b'Carnivorous', (b'Tiger', b'Lion', b'Cat')),
     (
      b'Herbivorous', (b'Moose', b'Deer', b'Cow'))]

    def __init__(self, *args, **kwargs):
        super(AnimalComplexKeySelect, self).__init__(*args, **kwargs)
        animal, count = self._getInitParams()
        type_, name = animal.split(b'.')
        self.a = self._makeDataOutputSlot(b'animalType', SLOT_TYPE.STR, None)
        self.a.setValue(type_)
        self.b = self._makeDataOutputSlot(b'animalName', SLOT_TYPE.STR, None)
        self.b.setValue(name)
        self.c = self._makeDataOutputSlot(b'count', SLOT_TYPE.INT, None)
        self.c.setValue(count)
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Type, Name', SLOT_TYPE.STR, b'Herbivorous.Deer', EDITOR_TYPE.COMPLEX_KEY_SELECTOR, AnimalComplexKeySelect.animals),
         InitParam(b'Count', SLOT_TYPE.INT, 0)]


class TestTunableEvent(TunableEventBlock, Example):

    def __init__(self, *args, **kwargs):
        super(TestTunableEvent, self).__init__(*args, **kwargs)
        self._t = self._makeDataInputSlot(b'time', SLOT_TYPE.FLOAT)
        self._a = self._makeDataInputSlot(b'value', SLOT_TYPE.FLOAT)
        self._res = self._makeDataOutputSlot(b'sqrValue', SLOT_TYPE.FLOAT, None)
        self._cbID = None
        return

    def onStartScript(self):
        from constants import IS_VS_EDITOR
        if not IS_VS_EDITOR:
            self._cbID = BigWorld.callback(self._t.getValue(), self._exec)
        return

    def onFinishScript(self):
        if self._cbID is not None:
            BigWorld.cancelCallback(self._cbID)
            self._cbID = None
        return

    @TunableEventBlock.eventProcessor
    def _exec(self):
        a = self._a.getValue()
        self._res.setValue(a * a)
        self._cbID = BigWorld.callback(self._t.getValue(), self._exec)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class ModeBlock(Block, Example):

    def __init__(self, *args, **kwargs):
        super(ModeBlock, self).__init__(*args, **kwargs)
        self._out = self._makeDataOutputSlot(b'mode', SLOT_TYPE.INT, None)
        self._out.setValue(self.mode())
        return

    @classmethod
    def mode(cls):
        return BLOCK_MODE.UNIQUE | Example.mode()


class ClampedBlockEx(Block, Example):

    def __init__(self, *args, **kwargs):
        super(ClampedBlockEx, self).__init__(*args, **kwargs)
        self._int = self._makeDataInputSlot(b'int [0, 100]', SLOT_TYPE.INT)
        self._int.setEditorData([0, 100])
        self._float = self._makeDataInputSlot(b'float [0, 1]', SLOT_TYPE.FLOAT)
        self._float.setEditorData([0.0, 1.0])
        self._angle = self._makeDataInputSlot(b'angle [-45, 45]', SLOT_TYPE.ANGLE)
        self._angle.setEditorData([-45.0, 45.0])
        self._outInt = self._makeDataOutputSlot(b'intClamped', SLOT_TYPE.INT, self._clampInt)
        self._outFloat = self._makeDataOutputSlot(b'floatClamped', SLOT_TYPE.FLOAT, self._clampFloat)
        self._outAngle = self._makeDataOutputSlot(b'angleClamped', SLOT_TYPE.ANGLE, self._clampAngle)
        return

    def _clampInt(self):
        self._outInt.setValue(self._int.getValue())
        return

    def _clampFloat(self):
        self._outFloat.setValue(self._float.getValue())
        return

    def _clampAngle(self):
        self._outAngle.setValue(self._angle.getValue())
        return


class ClampedBlock(Block, Example):

    def __init__(self, *args, **kwargs):
        super(ClampedBlock, self).__init__(*args, **kwargs)
        value, = self._getInitParams()
        self._int = self._makeDataOutputSlot(b'res', SLOT_TYPE.INT, None)
        self._int.setValue(value)
        return

    @classmethod
    def initParams(cls):
        return [InitParam(b'value [0, 100]', SLOT_TYPE.INT, 0, None, [0, 100])]


class TestStruct(VScriptStruct):
    name = VScriptStructField(b'name', SLOT_TYPE.STR)
    value = VScriptStructField(b'year', SLOT_TYPE.INT)

    def __repr__(self):
        return (b'TestStruct(name = {}, year = {})').format(self.name, self.value)


class TestType(VScriptType):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        return

    @classmethod
    def vs_connectionColor(cls):
        return 7206136


class TestEnum(VScriptEnum):
    A = 0
    B = 1
    C = 2


class MakeTestType(Block, Example):

    def __init__(self, *args, **kwargs):
        super(MakeTestType, self).__init__(*args, **kwargs)
        self._name = self._makeDataInputSlot(b'name', SLOT_TYPE.STR)
        self._age = self._makeDataInputSlot(b'age', SLOT_TYPE.INT)
        self._out = self._makeDataOutputSlot(b'data', TestType.slotType(), self._exec)
        return

    def _exec(self):
        self._out.setValue(TestType(self._name.getValue(), self._age.getValue()))
        return


class BreakTestType(Block, Example):

    def __init__(self, *args, **kwargs):
        super(BreakTestType, self).__init__(*args, **kwargs)
        self._in = self._makeDataInputSlot(b'in', TestType.slotType())
        self._name = self._makeDataOutputSlot(b'name', SLOT_TYPE.STR, self._execName)
        self._age = self._makeDataOutputSlot(b'age', SLOT_TYPE.INT, self._execAge)
        return

    def _execName(self):
        self._name.setValue(self._in.getValue().name)
        return

    def _execAge(self):
        self._age.setValue(self._in.getValue().age)
        return


class MakeTestTypeArray(Block, Example):

    def __init__(self, *args, **kwargs):
        super(MakeTestTypeArray, self).__init__(*args, **kwargs)
        self._out = self._makeDataOutputSlot(b'data', arrayOf(TestType.slotType()), None)
        self._out.setValue([TestType(b'Bob', 1945), TestType(b'Marley', 1981)])
        return


class SelectTest(Block, Example):

    def __init__(self, *args, **kwargs):
        super(SelectTest, self).__init__(*args, **kwargs)
        self._enum = self._makeDataInputSlot(b'enumValue', TestEnum.slotType())
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.INT, self._exec)
        return

    def _exec(self):
        v = self._enum.getValue()
        self._res.setValue(v)
        return


class PrintTestStruct(Block, Example):

    def __init__(self, *args, **kwargs):
        super(PrintTestStruct, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._exec)
        self._out = self._makeEventOutputSlot(b'out')
        self._s = self._makeDataInputSlot(b'struct', TestStruct.slotType())
        self._ns = self._makeDataOutputSlot(b'changed', TestStruct.slotType(), None)
        return

    def _exec(self):
        self._writeLog((b'PrintTestStruct: {}').format(self._s.getValue()))
        newStuct = TestStruct()
        newStuct.name = b'Metallica'
        newStuct.value = 1981
        self._ns.setValue(newStuct)
        self._out.call()
        return
