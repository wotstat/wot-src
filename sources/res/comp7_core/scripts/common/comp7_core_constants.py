from __future__ import absolute_import
import enum, constants
from constants_utils import ConstInjector
ROLE_EQUIPMENT_TAG = b'roleEquipment'

class ArenaPrebattlePhase(object):
    NONE = 0
    PREPICK = 1
    VOTING = 2
    PICK = 3


class FINISH_REASON(constants.FINISH_REASON, ConstInjector):
    SURVIVORS_LEFT = 201
    DAMAGE_DEALT = 202
    FIRST_KILL = 203
    DRAW_RESOLVED_REASONS = (
     SURVIVORS_LEFT, DAMAGE_DEALT, FIRST_KILL)


class SubMode(enum.Enum):
    REGULAR = b'regular'
    NIGHT_MAPS = b'night_maps'


def injectCommonConstants(personality):
    if not any(reason in FINISH_REASON.getExtraAttrs().values() for reason in FINISH_REASON.DRAW_RESOLVED_REASONS):
        FINISH_REASON.inject(personality)
    return
