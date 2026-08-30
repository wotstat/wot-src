from Event import Event

class IPrebattleVehicle(object):
    onChanged = None

    def switchCamera(self, vehicle):
        raise NotImplementedError
        return

    def select(self, vehicle):
        raise NotImplementedError
        return

    def selectAny(self):
        raise NotImplementedError
        return

    def selectNone(self):
        raise NotImplementedError
        return

    def getViewState(self):
        raise NotImplementedError
        return

    def isPresent(self):
        raise NotImplementedError
        return

    def isPremiumIGR(self):
        raise NotImplementedError
        return

    def isInHangar(self):
        raise NotImplementedError
        return

    def isDisabled(self):
        raise NotImplementedError
        return

    def isBroken(self):
        raise NotImplementedError
        return

    def isDisabledInRent(self):
        raise NotImplementedError
        return

    def isOnlyForEventBattles(self):
        raise NotImplementedError
        return

    def isOutfitLocked(self):
        raise NotImplementedError
        return

    def isCustomizationEnabled(self):
        raise NotImplementedError
        return

    @property
    def item(self):
        raise NotImplementedError
        return

    @property
    def invID(self):
        raise NotImplementedError
        return

    @property
    def lastInvID(self):
        raise NotImplementedError
        return
