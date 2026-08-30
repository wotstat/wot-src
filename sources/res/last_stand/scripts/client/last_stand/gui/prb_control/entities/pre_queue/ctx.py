from __future__ import absolute_import
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getVehicleInventoryID', b'vInvID'))
class LastStandQueueCtx(QueueCtx):

    def __init__(self, vehInvID, entityType, waitingID=b''):
        super(LastStandQueueCtx, self).__init__(entityType=entityType, waitingID=waitingID)
        self.__vehInvID = vehInvID
        return

    def getVehicleInventoryID(self):
        return self.__vehInvID
