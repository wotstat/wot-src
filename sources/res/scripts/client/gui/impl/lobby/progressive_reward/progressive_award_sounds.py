import WWISE
from shared_utils import CONST_CONTAINER

class ProgressiveRewardSoundEvents(CONST_CONTAINER):
    PROGRESSIVE_REWARD_VIEW_GROUP = b'STATE_overlay_hangar_general'
    PROGRESSIVE_REWARD_VIEW_ENTER = b'STATE_overlay_hangar_general_on'
    PROGRESSIVE_REWARD_VIEW_EXIT = b'STATE_overlay_hangar_general_off'
    PROGRESSIVE_REWARD_AWARD_GROUP = b'STATE_overlay_hangar_general'
    PROGRESSIVE_REWARD_AWARD_ENTER = b'STATE_overlay_hangar_general_on'
    PROGRESSIVE_REWARD_AWARD_EXIT = b'STATE_overlay_hangar_general_off'


def setSoundState(groupName, stateName, eventName=None):
    playSound(eventName=eventName)
    WWISE.WW_setState(groupName, stateName)
    return


def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)
    return
