from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class AdventCalendarEvent(HasCtxEvent):
    PROGRESSION_REWARD_VIEWED = b'progressionRewardViewed'
    CHANGE_BLUR_STATUS = b'changeBlurStatus'
    INTRO_CLOSE_STARTED = b'introCloseStarted'
