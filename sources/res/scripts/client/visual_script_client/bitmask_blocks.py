from visual_script.bitmask_blocks_common import BitMaskBase
from visual_script.misc import ASPECT
from constants import EQUIPMENT_ERROR_STATES, CollisionFlags

class BitMask(BitMaskBase):
    _MASK_TYPES = {b'Equipment ErrorStates': EQUIPMENT_ERROR_STATES, 
       b'Collision Flags': CollisionFlags}

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]
