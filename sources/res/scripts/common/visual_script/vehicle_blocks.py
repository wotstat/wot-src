from __future__ import absolute_import
from constants import NULL_ENTITY_ID
from visual_script.block import Block, Meta
from visual_script.misc import errorVScript
from visual_script.slot_types import SLOT_TYPE

class VehicleMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16738047

    @classmethod
    def blockCategory(cls):
        return b'Vehicle'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/tank'


class VehicleEventsMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16738047

    @classmethod
    def blockCategory(cls):
        return b'Vehicle'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena_event'


class GetVehicleId(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleId, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._res = self._makeDataOutputSlot(b'id', SLOT_TYPE.INT, self._exec)
        return

    def _exec(self):
        vehicle = self._vehicle.getValue()
        try:
            self._res.setValue(vehicle.id)
        except (AttributeError, ReferenceError):
            errorVScript(self, b'Dead weakref')
            self._res.setValue(NULL_ENTITY_ID)

        return


class GetVehicleOutfitId(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleOutfitId, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._id = self._makeDataOutputSlot(b'id', SLOT_TYPE.INT, self._getData)
        return

    def _getData(self, *args, **kwargs):
        vehicle = self._vehicle.getValue()
        outfit = vehicle.cp[b'outfit']
        self._id.setValue(outfit.styleId)
        return


class GetVehicleOutfitLevel(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleOutfitLevel, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._level = self._makeDataOutputSlot(b'level', SLOT_TYPE.INT, self._getLevel)
        return

    def _getLevel(self):
        vehicle = self._vehicle.getValue()
        level = vehicle.publicInfo[b'outfitLevel']
        self._level.setValue(level)
        return
