from gui.Scaleform.framework.entities.View import View

class PersonalMissionsAwardsViewMeta(View):

    def showVehiclePreview(self):
        self._printOverrideError(b'showVehiclePreview')
        return

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def showMissionByVehicleType(self, vehicleType):
        self._printOverrideError(b'showMissionByVehicleType')
        return

    def buyMissionsByVehicleType(self, vehicleType):
        self._printOverrideError(b'buyMissionsByVehicleType')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)
        return
