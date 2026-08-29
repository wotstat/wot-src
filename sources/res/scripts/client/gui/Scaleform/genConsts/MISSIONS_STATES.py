class MISSIONS_STATES(object):
    COMPLETED = b'done'
    FULL_COMPLETED = b'fullDone'
    NOT_AVAILABLE = b'notAvailable'
    WRONG_TIME = b'wrongTime'
    NONE = b''
    IN_PROGRESS = b'inProgress'
    DISABLED = b'disabled'
    IS_ON_PAUSE = b'isOnPause'
    EVENT_STATUS = [COMPLETED, FULL_COMPLETED, NOT_AVAILABLE, WRONG_TIME, NONE, IN_PROGRESS, 
     DISABLED, IS_ON_PAUSE]
