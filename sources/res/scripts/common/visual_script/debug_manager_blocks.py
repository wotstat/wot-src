from __future__ import absolute_import
import Math
from DebugManager import isGroupEnabled
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.debug_manager_blocks_base import DebugManagerBlock, DEFAULT_COLOR

class DebugManagerRegisterObject(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerRegisterObject, self).__init__(*args, **kwargs)
        return

    def _groupAutoEnable(self):
        return True


class DebugManagerClearObject(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerClearObject, self).__init__(*args, **kwargs)
        return

    def _groupAutoEnable(self):
        return True


class DebugManagerIsGroupEnabled(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerIsGroupEnabled, self).__init__(*args, **kwargs)
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        groupID = self._slotGetValue(b'groupID')
        res = isGroupEnabled(groupID)
        self._res.setValue(res)
        return

    def _eventSlotsEnabled(self):
        return False

    def _nameSlotEnabled(self):
        return False

    def _groupAutoEnable(self):
        return True


class DebugManagerRemoveObject(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerRemoveObject, self).__init__(*args, **kwargs)
        return

    def _groupAutoEnable(self):
        return True


class DebugManagerRemoveGroup(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerRemoveGroup, self).__init__(*args, **kwargs)
        return

    def _nameSlotEnabled(self):
        return False

    def _groupAutoEnable(self):
        return True


class DebugManagerShowMessage(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowMessage, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'value', SLOT_TYPE.STR)
        return


class DebugManagerShowText2D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowText2D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'text', SLOT_TYPE.STR)
        self._createDataInputSlot(b'position', SLOT_TYPE.VECTOR2)
        self._createDataInputSlot(b'isPixels', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowPoint2D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowPoint2D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'positions', arrayOf(SLOT_TYPE.VECTOR2))
        self._createDataInputSlot(b'isPixels', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowLine2D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowLine2D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'positions', arrayOf(SLOT_TYPE.VECTOR2))
        self._createDataInputSlot(b'isLabel', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'isPixels', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowCircle2D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowCircle2D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'center', SLOT_TYPE.VECTOR2)
        self._createDataInputSlot(b'radius', SLOT_TYPE.FLOAT)
        self._createDataInputSlot(b'isPixels', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowRectangle2D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowRectangle2D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'start', SLOT_TYPE.VECTOR2)
        self._createDataInputSlot(b'end', SLOT_TYPE.VECTOR2)
        self._createDataInputSlot(b'isPixels', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowText3D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowText3D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'info', SLOT_TYPE.DICTIONARY)
        self._createDataInputSlot(b'position', SLOT_TYPE.VECTOR3, Math.Vector3(0, 1, 0))
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowLine3D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowLine3D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'positions', arrayOf(SLOT_TYPE.VECTOR3))
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'isArrow', SLOT_TYPE.BOOL, False)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowPoint3D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowPoint3D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'positions', arrayOf(SLOT_TYPE.VECTOR3))
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowBox3D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowBox3D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'center', SLOT_TYPE.VECTOR3)
        self._createDataInputSlot(b'direction', SLOT_TYPE.VECTOR3, Math.Vector3(0, 0, 1))
        self._createDataInputSlot(b'size', SLOT_TYPE.VECTOR3, Math.Vector3(1, 1, 1))
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowCircle3D(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowCircle3D, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'center', SLOT_TYPE.VECTOR3)
        self._createDataInputSlot(b'radius', SLOT_TYPE.FLOAT)
        self._createDataInputSlot(b'normal', SLOT_TYPE.VECTOR3, Math.Vector3(0, 1, 0))
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowSphere(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowSphere, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'center', SLOT_TYPE.VECTOR3)
        self._createDataInputSlot(b'radius', SLOT_TYPE.FLOAT)
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return


class DebugManagerShowCylinder(DebugManagerBlock):

    def __init__(self, *args, **kwargs):
        super(DebugManagerShowCylinder, self).__init__(*args, **kwargs)
        self._createDataInputSlot(b'start', SLOT_TYPE.VECTOR3)
        self._createDataInputSlot(b'end', SLOT_TYPE.VECTOR3)
        self._createDataInputSlot(b'radius', SLOT_TYPE.FLOAT)
        self._createDataInputSlot(b'entityID', SLOT_TYPE.INT, -1)
        self._createDataInputSlot(b'color', SLOT_TYPE.COLOR, DEFAULT_COLOR)
        return
