from helpers import dependency
from skeletons.gui.shared import IItemsCache

class ContextBase(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)
        return

    def update(self, *args, **kwargs):
        raise NotImplementedError
        return


class TankmanContext(ContextBase):
    __slots__ = (b'_tankmanID', b'_tankman', b'_tankmanCurrentVehicle', b'_tankmanNativeVehicle')

    def __init__(self, tankmanID, *args, **kwargs):
        self._tankmanID = None
        self._tankman = None
        super(TankmanContext, self).__init__(tankmanID)
        return

    @property
    def tankmanID(self):
        return self._tankmanID

    @property
    def tankman(self):
        return self._tankman

    def update(self, tankmanID):
        self._tankmanID = tankmanID
        self._tankman = self.itemsCache.items.getTankman(self._tankmanID)
        return
