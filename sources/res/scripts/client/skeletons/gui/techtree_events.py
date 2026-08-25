from __future__ import absolute_import
from Event import Event

class ITechTreeEventsListener(object):
    onEventsUpdated = None
    onSettingsChanged = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @property
    def actions(self):
        raise NotImplementedError
        return

    def getUserName(self, actionID):
        raise NotImplementedError
        return

    def getVehicles(self, nationID=None):
        raise NotImplementedError
        return

    def setNationViewed(self, nationID):
        raise NotImplementedError
        return

    def getNations(self, unviewed=False, actionID=None):
        raise NotImplementedError
        return

    def getTimeTillEnd(self, actionID):
        raise NotImplementedError
        return

    def getFinishTime(self, actionID):
        raise NotImplementedError
        return

    def hasActiveAction(self, vehicleCD, nationID=None):
        raise NotImplementedError
        return

    def getActiveAction(self, vehicleCD=None, nationID=None):
        raise NotImplementedError
        return
