from block import Block
from slot_types import SLOT_TYPE, arrayOf
from visual_script.vehicle_blocks import VehicleMeta

class NoCrewCriticalBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(NoCrewCriticalBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        return


class NoDeviceCriticalBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(NoDeviceCriticalBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        return


class NoInnerDeviceDamagedBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(NoInnerDeviceDamagedBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        return


class OptionalDevicesBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(OptionalDevicesBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', arrayOf(SLOT_TYPE.STR), self._execute)
        return

    def _execute(self):
        return


class VehicleClassBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(VehicleClassBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'className', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        return


class GetTankOptDevicesHPModBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetTankOptDevicesHPModBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.FLOAT, self._execute)
        return

    def _execute(self):
        return


class GunTypeInfoBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GunTypeInfoBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', arrayOf(SLOT_TYPE.STR), self._execute)
        return

    def _execute(self):
        return


class VehicleForwardSpeedBase(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(VehicleForwardSpeedBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'fwdSpeed', SLOT_TYPE.FLOAT, self._execute)
        return

    def _execute(self):
        return


class VehicleCooldownEquipmentBase(Block):

    def __init__(self, *args, **kwargs):
        super(VehicleCooldownEquipmentBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'cdEquipment', arrayOf(SLOT_TYPE.STR), self._execute)
        return

    def _execute(self):
        return


class VehicleClipFullAndReadyBase(Block):

    def __init__(self, *args, **kwargs):
        super(VehicleClipFullAndReadyBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        return


class IsInHangarBase(Block):

    def __init__(self, *args, **kwargs):
        super(IsInHangarBase, self).__init__(*args, **kwargs)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        return


class VehicleRadioDistanceBase(Block):

    def __init__(self, *args, **kwargs):
        super(VehicleRadioDistanceBase, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'res', SLOT_TYPE.FLOAT, self._execute)
        return

    def _execute(self):
        return
