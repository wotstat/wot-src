from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getVehicleInventoryID', b'vInvID'), (b'getWaitingID', b'waitingID'))
class RankedQueueCtx(QueueCtx):

    def __init__(self, vInventoryID, waitingID=b''):
        super(RankedQueueCtx, self).__init__(entityType=QUEUE_TYPE.RANKED, waitingID=waitingID)
        self.__vInventoryID = vInventoryID
        return

    def getVehicleInventoryID(self):
        return self.__vInventoryID
