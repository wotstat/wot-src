from __future__ import absolute_import
from fort_rush_common.fort_rush_constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getVehicleInventoryID', b'vInvID'))
class FortRushBattleQueueCtx(QueueCtx):

    def __init__(self, vehInvID, waitingID=b''):
        super(FortRushBattleQueueCtx, self).__init__(entityType=QUEUE_TYPE.FORT_RUSH, waitingID=waitingID)
        self.__vehInvID = vehInvID
        return

    def getVehicleInventoryID(self):
        return self.__vehInvID
