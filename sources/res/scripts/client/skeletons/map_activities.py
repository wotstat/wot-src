class IMapActivities(object):
    __slots__ = ()

    def start(self, name, targetTime):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def generateOfflineActivities(self, spacePath, usePossibility=True):
        raise NotImplementedError
        return

    def setPauseVisuals(self, isPause):
        raise NotImplementedError
        return
