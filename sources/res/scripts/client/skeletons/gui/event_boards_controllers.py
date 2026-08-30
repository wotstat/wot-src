from __future__ import absolute_import
import typing
from adisp import adisp_process, adisp_async
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Type
    from gui.event_boards.event_boards_items import IPlayerProgression

class IEventBoardController(object):

    def isElenQuestsStatusWrong(self, currentEvent):
        raise NotImplementedError
        return

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

    @adisp_async
    @adisp_process
    def getPlayerProgression(self, eventID, leaderboardID, progressionClass, callback=None, showNotification=True):
        raise NotImplementedError
        return
