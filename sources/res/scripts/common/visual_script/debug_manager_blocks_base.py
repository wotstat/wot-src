from __future__ import absolute_import
import DebugManager
from DebugManager import COLORS, isGroupEnabled, setGroupEnabled
from visual_script.block import Block, Meta
from visual_script.misc import ASPECT, errorVScript
from visual_script.slot_types import SLOT_TYPE

def uint32toInt32(value):
    if value <= 2147483647:
        return value
    else:
        return -(4294967295L - value + 1)

    return


def int32ToUint32(value):
    if value >= 0:
        return value
    else:
        return 4294967295L + value + 1

    return


DEFAULT_COLOR = uint32toInt32(COLORS.DEFAULT)

class DebugManagerBlockMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16711765

    @classmethod
    def blockCategory(cls):
        return b'Debug Manager'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER, ASPECT.HANGAR]


class DebugManagerBlock(Block, DebugManagerBlockMeta):

    def __init__(self, *args, **kwargs):
        super(DebugManagerBlock, self).__init__(*args, **kwargs)
        self._params = []
        self._func = self.__class__.__name__[len(b'DebugManager'):]
        self._func = self._func[:1].lower() + self._func[1:]
        if self._eventSlotsEnabled():
            self._in = self._makeEventInputSlot(b'in', self._execute)
            self._out = self._makeEventOutputSlot(b'out')
        self._createDataInputSlot(b'groupID', SLOT_TYPE.STR)
        if self._nameSlotEnabled():
            self._createDataInputSlot(b'name', SLOT_TYPE.STR)
        return

    def _execute(self):
        if hasattr(DebugManager, self._func):
            func = getattr(DebugManager, self._func)
            params = {}
            for slotName in self._params:
                slotValue = self._slotGetValue(slotName)
                params[slotName] = slotValue

            func(**params)
            if self._groupAutoEnable():
                groupID = self._slotGetValue(b'groupID')
                if not isGroupEnabled(groupID):
                    setGroupEnabled(groupID, True)
        else:
            errorVScript(self, (b'Unknown DebugManager function {}').format(self._func))
        self._out.call()
        return

    def _createDataInputSlot(self, slotName, slotType=SLOT_TYPE.STR, slotDefaultValue=None):
        setattr(self, b'_' + slotName, self._makeDataInputSlot(slotName, slotType))
        if slotDefaultValue is not None:
            getattr(self, b'_' + slotName).setDefaultValue(slotDefaultValue)
        self._params.append(slotName)
        return

    def _eventSlotsEnabled(self):
        return True

    def _nameSlotEnabled(self):
        return True

    def _groupAutoEnable(self):
        return True

    def _slotGetValue(self, slotName):
        slot = getattr(self, b'_' + slotName)
        slotValue = slot.getValue()
        if slotName == b'entityID' and slotValue < 0:
            slotValue = None
        if slotName == b'color':
            slotValue = int32ToUint32(slotValue)
        return slotValue

    def captionText(self):
        return b'DebugManager: ' + self._func
