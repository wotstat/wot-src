from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE, REQUEST_TYPE
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

class _PreQueueRequestCtx(PrbCtrlRequestCtx):

    def __init__(self, **kwargs):
        super(_PreQueueRequestCtx, self).__init__(ctrlType=CTRL_ENTITY_TYPE.PREQUEUE, **kwargs)
        return


class QueueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.QUEUE


class DequeueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.DEQUEUE


class JoinPreQueueModeCtx(_PreQueueRequestCtx):

    def __init__(self, queueType, flags=FUNCTIONAL_FLAG.UNDEFINED, waitingID=b''):
        super(JoinPreQueueModeCtx, self).__init__(entityType=queueType, flags=flags, waitingID=waitingID)
        return

    def getID(self):
        return 0


@ReprInjector.withParent((b'getWaitingID', b'waitingID'))
class LeavePreQueueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.LEAVE
