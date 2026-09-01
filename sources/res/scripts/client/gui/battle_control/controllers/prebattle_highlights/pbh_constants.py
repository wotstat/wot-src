from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
TANK_SIZE_LOWER_BOUNDS = (
 float(b'-inf'), 5.0, 8.0)
TANK_POS_TEMPLATE = b'pbh_top{}_{}'
TANK_CAMERA_TEMPLATE = b'pbh_camera_{}_{}'
MARKER_X_FACTOR = 0
MARKER_Y_FACTOR = 1.1

class TankSizes(CONST_CONTAINER):
    SMALL = b'small'
    MEDIUM = b'medium'
    BIG = b'big'
    ORDERED_SIZES = (
     SMALL, MEDIUM, BIG)
