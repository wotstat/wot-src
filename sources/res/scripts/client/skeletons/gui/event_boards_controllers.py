from adisp import adisp_process, adisp_async

class IEventBoardController(object):

    def getPlayerEventsData(self):
        raise NotImplementedError
        return

    def hasEvents(self):
        raise NotImplementedError
        return

    def getEventsSettingsData(self):
        raise NotImplementedError
        return

    def getMyEventsTopData(self):
        raise NotImplementedError
        return

    def getHangarFlagData(self):
        raise NotImplementedError
        return

    def updateHangarFlag(self):
        raise NotImplementedError
        return

    def cleanEventsData(self):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def joinEvent(self, eventID, callback):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def leaveEvent(self, eventID, callback):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def getHangarFlag(self, callback, onLogin=False):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def getEvents(self, callback, onlySettings=True, isTabVisited=False, onLogin=False, prefetchKeyArtBig=True):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def getMyLeaderboardInfo(self, eventID, leaderboardID, callback, showNotification=True):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def getLeaderboard(self, eventID, leaderboardID, pageNumber, callback, leaderBoardClass=None, showNotification=True):
        raise NotImplementedError
        return
