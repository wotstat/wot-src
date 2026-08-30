from gui.prb_control.storages.local_storage import LocalStorage

class StrongholdStorage(LocalStorage):
    __slots__ = (b'_animationIdx',)

    def __init__(self):
        super(StrongholdStorage, self).__init__()
        self._animationIdx = 0
        return

    def fini(self):
        super(StrongholdStorage, self).fini()
        self.clear()
        return

    def clear(self):
        super(StrongholdStorage, self).clear()
        self._animationIdx = 0
        return

    def suspend(self):
        super(StrongholdStorage, self).suspend()
        self._animationIdx = 0
        return

    def setActiveAnimationIdx(self, animIdx):
        self._animationIdx = animIdx
        return

    def getActiveAnimationIdx(self):
        return self._animationIdx
