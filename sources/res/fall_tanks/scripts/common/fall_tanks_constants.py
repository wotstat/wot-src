from __future__ import absolute_import
import constants
from constants_utils import ConstInjector, addArenaGuiTypesFromExtension, addAttackReasonTypesFromExtension, addDamageInfoCodes
from fun_random_common import fun_constants
from fun_random_common.fun_constants_utils import addArenaGuiTypesFromExtensionToFunRange, addFunRandomSubModeImpl, addFunProgressionConditions, addFunRandomQueueTypesFromExtension
VEHICLE_DESTROY_PERIOD = 5.0
EVACUATION_TIME = 5.0

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    FALL_TANKS = 200


class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type = str
    FALL_TANKS_FINISH = b'fall_tanks_finish'
    FALL_TANKS_FALLING = b'fall_tanks_falling'
    FALL_TANKS_LEAVER = b'fall_tanks_leaver'


class FunSubModeImpl(fun_constants.FunSubModeImpl, ConstInjector):
    FALL_TANKS = 3


class FunProgressionCondition(fun_constants.FunProgressionCondition, ConstInjector):
    _const_type = str
    FINISH_TIME = b'fallTanksFinishTime'
    FINISH_POSITION = b'fallTanksPosition'
    CHECKPOINTS_PASSED = b'fallTanksCheckpointsPassed'
    USED_SKILLS = b'fallTanksUsedSkillsN'


class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    FALL_TANKS = 111


DAMAGE_INFO_CODES_PER_ATTACK_REASON = {(ATTACK_REASON.FALL_TANKS_FINISH): b'DEATH_FROM_FALL_TANKS_FINISH', 
   (ATTACK_REASON.FALL_TANKS_FALLING): b'DEATH_FROM_FALL_TANKS_FALLING', 
   (ATTACK_REASON.FALL_TANKS_LEAVER): b'DEATH_FROM_FALL_TANKS_LEAVER'}

def injectConsts(personality):
    addArenaGuiTypesFromExtension(ARENA_GUI_TYPE, personality)
    addArenaGuiTypesFromExtensionToFunRange(ARENA_GUI_TYPE)
    constants.ARENA_GUI_TYPE.NON_DESERTION_ARENAS += (ARENA_GUI_TYPE.FALL_TANKS,)
    addAttackReasonTypesFromExtension(ATTACK_REASON, personality)
    addDamageInfoCodes(DAMAGE_INFO_CODES_PER_ATTACK_REASON, personality)
    addFunRandomSubModeImpl(FunSubModeImpl, personality)
    addFunProgressionConditions(FunProgressionCondition, personality)
    addFunRandomQueueTypesFromExtension(QUEUE_TYPE, personality)
    return
