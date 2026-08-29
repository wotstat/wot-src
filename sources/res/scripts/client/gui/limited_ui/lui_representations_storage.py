from collections import namedtuple
from itertools import chain
from constants import MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL
from helpers import int2roman
from gui.limited_ui.lui_tokens_storage import LimitedUITokenID
LimitedUIConditionRepresentation = namedtuple(b'LimitedUIConditionRepresentation', (b'condition', b'resourceName', b'kwargs'))
_VEHICLE_CONDITION_REPRESENTATIONS = tuple(representation for representation in chain.from_iterable((LimitedUIConditionRepresentation((b'{}>0').format(LimitedUITokenID.MIN_VEHICLE_LEVEL.format(vehLevel)), b'minVehicleLevel', {b'level': (int2roman(vehLevel))}),) for vehLevel in range(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1)))
_REGISTER_CONDITION_REPRESENTATIONS = (
 LimitedUIConditionRepresentation(LimitedUITokenID.IS_IN_CLAN, b'isInClan', {}),) + _VEHICLE_CONDITION_REPRESENTATIONS

def getRepresentations():
    return _REGISTER_CONDITION_REPRESENTATIONS
