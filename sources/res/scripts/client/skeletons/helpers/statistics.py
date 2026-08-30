class IStatisticsCollector(object):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def reset(self):
        raise NotImplementedError
        return

    @property
    def update(self):
        raise NotImplementedError
        return

    def needCollectSystemData(self, value):
        raise NotImplementedError
        return

    def needCollectSessionData(self, value):
        raise NotImplementedError
        return

    def getStatistics(self, andStop=True):
        raise NotImplementedError
        return

    def getSessionData(self):
        raise NotImplementedError
        return

    def noteHangarLoadingState(self, state, initialState=False, showSummaryNow=False):
        raise NotImplementedError
        return

    def noteLastArenaData(self, arenaTypeID, arenaUniqueID, arenaTeam):
        raise NotImplementedError
        return
