from gui.Scaleform.daapi.view.meta.VehicleCompareCommonViewMeta import VehicleCompareCommonViewMeta

class VehicleCompareViewMeta(VehicleCompareCommonViewMeta):

    def onBackClick(self):
        self._printOverrideError(b'onBackClick')
        return

    def onGoToPreviewClick(self, index):
        self._printOverrideError(b'onGoToPreviewClick')
        return

    def onGoToHangarClick(self, vehicleID):
        self._printOverrideError(b'onGoToHangarClick')
        return

    def onSelectModulesClick(self, vehicleID, index):
        self._printOverrideError(b'onSelectModulesClick')
        return

    def onParamDeltaRequested(self, index, paramID):
        self._printOverrideError(b'onParamDeltaRequested')
        return

    def onCrewLevelChanged(self, index, crewLevelID):
        self._printOverrideError(b'onCrewLevelChanged')
        return

    def onRemoveVehicle(self, index):
        self._printOverrideError(b'onRemoveVehicle')
        return

    def onRevertVehicle(self, index):
        self._printOverrideError(b'onRevertVehicle')
        return

    def onRemoveAllVehicles(self):
        self._printOverrideError(b'onRemoveAllVehicles')
        return

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)
        return

    def as_setParamsDeltaS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setParamsDelta(data)
        return

    def as_setVehicleParamsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleParamsData(data)
        return

    def as_getVehiclesDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getVehiclesDP()
        return

    def as_setVehiclesCountTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesCountText(text)
        return
