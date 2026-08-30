from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RosterSlotSettingsWindowMeta(AbstractWindowView):

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._printOverrideError(b'onFiltersUpdate')
        return

    def requestVehicleFilters(self):
        self._printOverrideError(b'requestVehicleFilters')
        return

    def submitButtonHandler(self, value):
        self._printOverrideError(b'submitButtonHandler')
        return

    def cancelButtonHandler(self):
        self._printOverrideError(b'cancelButtonHandler')
        return

    def as_setVehicleSelectionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleSelection(data)
        return

    def as_setRangeSelectionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRangeSelection(data)
        return

    def as_resetSelectionS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetSelection()
        return

    def as_selectTabS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)
        return

    def as_setListDataS(self, listData):
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(listData)
        return

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)
        return

    def as_setRosterLimitsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterLimits(data)
        return

    def as_updateVehicleFiltersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleFilters(data)
        return
