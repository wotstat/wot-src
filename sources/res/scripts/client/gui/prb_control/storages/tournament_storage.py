from gui.prb_control.storages.local_storage import LocalStorage

class TournamentStorage(LocalStorage):
    __slots__ = (b'_animationIdx',)

    def __init__(self):
        super(TournamentStorage, self).__init__()
        self._animationIdx = 0
        return

    def fini(self):
        super(TournamentStorage, self).fini()
        self.clear()
        return

    def clear(self):
        super(TournamentStorage, self).clear()
        self._animationIdx = 0
        return

    def suspend(self):
        super(TournamentStorage, self).suspend()
        self._animationIdx = 0
        return

    def setActiveAnimationIdx(self, animIdx):
        self._animationIdx = animIdx
        return

    def getActiveAnimationIdx(self):
        return self._animationIdx
