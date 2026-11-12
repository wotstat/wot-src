from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NYSelectVehiclePopoverMeta(SmartPopOverView):

    def onSelectVehicle(self, index):
        self._printOverrideError(b'onSelectVehicle')
        return

    def applyFilters(self, nation, vehicleType, level):
        self._printOverrideError(b'applyFilters')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return
