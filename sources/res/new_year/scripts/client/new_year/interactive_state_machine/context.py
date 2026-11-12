from new_year.skeletons.i_sm_queue_context import IQueueContext

class QueueContext(IQueueContext):
    __slots__ = (b'wasInBattle', b'isLocked', b'firstBattleLatch')

    def __init__(self):
        super(QueueContext, self).__init__()
        self.reset()
        return

    def reset(self):
        self.wasInBattle = False
        self.isLocked = False
        self.firstBattleLatch = False
        return
