from gui.prb_control.entities.base.listener import IPrbListener

class IPreQueueListener(IPrbListener):

    def onEnqueued(self, queueType, *args):
        return

    def onDequeued(self, queueType, *args):
        return

    def onEnqueueError(self, queueType, *args):
        return

    def onKickedFromQueue(self, queueType, *args):
        return

    def onKickedFromArena(self, queueType, *args):
        return

    def onArenaJoinFailure(self, queueType, *args):
        return

    def onPreQueueSettingsChanged(self, diff):
        return
