from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class CyberSportUnitMeta(BaseRallyRoomView):

    def toggleFreezeRequest(self):
        self._printOverrideError(b'toggleFreezeRequest')
        return

    def toggleStatusRequest(self):
        self._printOverrideError(b'toggleStatusRequest')
        return

    def showSettingsRoster(self, vaue):
        self._printOverrideError(b'showSettingsRoster')
        return

    def resultRosterSlotsSettings(self, value):
        self._printOverrideError(b'resultRosterSlotsSettings')
        return

    def cancelRosterSlotsSettings(self):
        self._printOverrideError(b'cancelRosterSlotsSettings')
        return

    def lockSlotRequest(self, slotIndex):
        self._printOverrideError(b'lockSlotRequest')
        return

    def as_updateSlotSettingsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlotSettings(value)
        return

    def as_closeSlotS(self, slotIdx, cost, slotsLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_closeSlot(slotIdx, cost, slotsLabel)
        return

    def as_openSlotS(self, slotIdx, canBeTaken, slotsLabel, compatibleVehiclesCount):
        if self._isDAAPIInited():
            return self.flashObject.as_openSlot(slotIdx, canBeTaken, slotsLabel, compatibleVehiclesCount)
        return

    def as_lockUnitS(self, isLocked, slotsLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_lockUnit(isLocked, slotsLabel)
        return

    def as_setOpenedS(self, isOpened, statusLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(isOpened, statusLabel)
        return

    def as_setTotalLabelS(self, hasTotalLevelError, totalLevelLabel, totalLevel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLabel(hasTotalLevelError, totalLevelLabel, totalLevel)
        return

    def as_setPlayerCountLblS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerCountLbl(value)
        return
