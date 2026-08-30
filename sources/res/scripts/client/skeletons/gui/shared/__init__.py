from Event import Event
from skeletons.gui.shared.utils import IItemsRequester, requesters

class IItemsCache(requesters.IRequester):
    onSyncStarted = None
    onSyncCompleted = None

    @property
    def waitForSync(self):
        raise NotImplementedError
        return

    @property
    def items(self):
        raise NotImplementedError
        return

    @property
    def compatVehiclesCache(self):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def update(self, updateReason, diff=None, notify=True, callback=None):
        raise NotImplementedError
        return

    def onDisconnected(self):
        raise NotImplementedError
        return
