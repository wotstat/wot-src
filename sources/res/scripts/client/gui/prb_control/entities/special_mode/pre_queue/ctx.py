from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getVehicleInventoryID', b'vInvID'), (b'getWaitingID', b'waitingID'))
class SpecialModeQueueCtx(QueueCtx):

    def __init__(self, entityType, vInventoryID, waitingID=b''):
        super(SpecialModeQueueCtx, self).__init__(entityType=entityType, waitingID=waitingID)
        self.__vInventoryID = vInventoryID
        return

    def getVehicleInventoryID(self):
        return self.__vInventoryID
