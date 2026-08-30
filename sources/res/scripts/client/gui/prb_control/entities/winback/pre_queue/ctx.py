from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getVehicleInventoryID', b'vInvID'), (b'getWaitingID', b'waitingID'), (b'getWinbackFlags', b'winbackFlags'))
class WinbackModeQueueCtx(QueueCtx):

    def __init__(self, vInventoryID, waitingID=b'', winbackFlags=0):
        super(WinbackModeQueueCtx, self).__init__(entityType=QUEUE_TYPE.WINBACK, waitingID=waitingID)
        self.__vInventoryID = vInventoryID
        self.__winbackFlags = winbackFlags
        return

    def getVehicleInventoryID(self):
        return self.__vInventoryID

    def getWinbackFlags(self):
        return self.__winbackFlags
