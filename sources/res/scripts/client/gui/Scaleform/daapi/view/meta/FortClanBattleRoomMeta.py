from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortClanBattleRoomMeta(BaseRallyRoomView):

    def onTimerAlert(self):
        self._printOverrideError(b'onTimerAlert')
        return

    def openConfigureWindow(self):
        self._printOverrideError(b'openConfigureWindow')
        return

    def toggleRoomStatus(self):
        self._printOverrideError(b'toggleRoomStatus')
        return

    def onFiltersChange(self, slotIndex, filters):
        self._printOverrideError(b'onFiltersChange')
        return

    def resetFilters(self, slotIndex):
        self._printOverrideError(b'resetFilters')
        return

    def onUnfrozenVehicleSlotClick(self, slotIndex):
        self._printOverrideError(b'onUnfrozenVehicleSlotClick')
        return

    def as_updateTeamHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTeamHeaderText(value)
        return

    def as_setBattleRoomDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleRoomData(data)
        return

    def as_updateReadyStatusS(self, mineValue, enemyValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReadyStatus(mineValue, enemyValue)
        return

    def as_updateReadyDirectionsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReadyDirections(value)
        return

    def as_setConfigureButtonStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setConfigureButtonState(data)
        return

    def as_setTimerDeltaS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerDelta(data)
        return

    def as_setDirectionS(self, value, animationNotAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_setDirection(value, animationNotAvailable)
        return

    def as_setReservesEnabledS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setReservesEnabled(data)
        return

    def as_setReservesDataS(self, reservesData):
        if self._isDAAPIInited():
            return self.flashObject.as_setReservesData(reservesData)
        return

    def as_setOpenedS(self, buttonLabel, statusLabel, tooltipLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(buttonLabel, statusLabel, tooltipLabel)
        return

    def as_setTableHeaderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)
        return

    def as_setFiltersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFiltersData(data)
        return
