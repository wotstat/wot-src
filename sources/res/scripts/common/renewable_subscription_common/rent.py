from __future__ import absolute_import
from enum import Enum

class RentEventTypes(Enum):
    START_RENT = 1
    END_RENT = 2


class RentLogInfo(Enum):
    ADD = b'excl_veh:add'
    START = b'excl_veh:on'
    END = b'excl_veh:off'
