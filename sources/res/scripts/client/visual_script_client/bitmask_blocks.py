from visual_script.bitmask_blocks_common import BitMaskBase
from visual_script.misc import ASPECT
from constants import EQUIPMENT_ERROR_STATES, CollisionFlags, VEHICLE_HIT_FLAGS

class BitMask(BitMaskBase):
    _MASK_TYPES = {b'Equipment ErrorStates': EQUIPMENT_ERROR_STATES, 
       b'Collision Flags': CollisionFlags, 
       b'Vehicle Hit Flags': VEHICLE_HIT_FLAGS}

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]
