from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class EventBoardsResultFilterVehiclesPopoverViewMeta(SmartPopOverView):

    def setVehicleSelected(self, dbID):
        self._printOverrideError(b'setVehicleSelected')
        return

    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        self._printOverrideError(b'applyFilters')
        return

    def resetFilters(self):
        self._printOverrideError(b'resetFilters')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_getTableDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDP()
        return

    def as_updateTableSortFieldS(self, sortField, sortDirection):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTableSortField(sortField, sortDirection)
        return
