class INovelty(object):
    onUpdated = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @property
    def showNovelty(self):
        raise NotImplementedError
        return

    @property
    def noveltyCount(self):
        raise NotImplementedError
        return

    def setAsSeen(self):
        raise NotImplementedError
        return
