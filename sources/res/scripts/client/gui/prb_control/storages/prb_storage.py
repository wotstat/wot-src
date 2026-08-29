from gui.prb_control.storages.local_storage import LocalStorage

class TrainingStorage(LocalStorage):
    __slots__ = (b'isObserver',)

    def __init__(self):
        super(TrainingStorage, self).__init__()
        self.isObserver = False
        return

    def clear(self):
        self.isObserver = False
        return

    def suspend(self):
        self.clear()
        return
