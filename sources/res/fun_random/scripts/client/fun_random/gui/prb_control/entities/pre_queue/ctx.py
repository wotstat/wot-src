from __future__ import absolute_import
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx, JoinPreQueueModeCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getVehicleInventoryID', b'vInvID'), (b'getDesiredSubModeID', b'subModeID'))
class FunRandomQueueCtx(QueueCtx):
    __slots__ = (b'__desiredSubModeID', b'__vInventoryID')

    def __init__(self, vInventoryID, desiredSubModeID, waitingID=b''):
        super(FunRandomQueueCtx, self).__init__(entityType=QUEUE_TYPE.FUN_RANDOM, waitingID=waitingID)
        self.__desiredSubModeID = desiredSubModeID
        self.__vInventoryID = vInventoryID
        return

    def getDesiredSubModeID(self):
        return self.__desiredSubModeID

    def getVehicleInventoryID(self):
        return self.__vInventoryID


@ReprInjector.withParent((b'getDesiredSubModeID', b'desiredSubModeID'))
class JoinFunPreQueueModeCtx(JoinPreQueueModeCtx):
    __slots__ = (b'__desiredSubModeID',)

    def __init__(self, queueType, desiredSubModeID, flags=FUNCTIONAL_FLAG.UNDEFINED, waitingID=b''):
        super(JoinFunPreQueueModeCtx, self).__init__(queueType=queueType, flags=flags, waitingID=waitingID)
        self.__desiredSubModeID = desiredSubModeID
        return

    def getDesiredSubModeID(self):
        return self.__desiredSubModeID
