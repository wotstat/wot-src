from __future__ import absolute_import
from typing import Dict
from Event import Event
from skeletons.gui.game_control import IGameController, ISeasonProvider

class IWhiteTigerController(IGameController, ISeasonProvider):
    onPrimeTimeStatusUpdated = None
    onEventPrbChanged = None
    onEventEnded = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isInAnnouncement(self):
        raise NotImplementedError
        return

    def isPromoScreenEnabled(self):
        raise NotImplementedError
        return

    def isEventPrbActive(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def getTimeLeft(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def getWTVehicles(self):
        raise NotImplementedError
        return

    def openHangar(self):
        raise NotImplementedError
        return

    def selectBattle(self, callback=None):
        raise NotImplementedError
        return

    def getSquadConfig(self):
        raise NotImplementedError
        return

    def selectRandomMode(self):
        raise NotImplementedError
        return

    def selectVehicle(self, invID=0):
        raise NotImplementedError
        return

    def isInWhiteTigerMode(self):
        raise NotImplementedError
        return

    def isSelectedVehicleWTVehicle(self):
        raise NotImplementedError
        return

    def getEndDate(self):
        raise NotImplementedError
        return

    def getStartDate(self):
        raise NotImplementedError
        return
