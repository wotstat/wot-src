from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleInfoMeta(AbstractWindowView):

    def getVehicleInfo(self):
        self._printOverrideError(b'getVehicleInfo')
        return

    def onCancelClick(self):
        self._printOverrideError(b'onCancelClick')
        return

    def addToCompare(self):
        self._printOverrideError(b'addToCompare')
        return

    def changeNation(self):
        self._printOverrideError(b'changeNation')
        return

    def as_setVehicleInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleInfo(data)
        return

    def as_setCompareButtonDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCompareButtonData(data)
        return

    def as_setChangeNationButtonDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeNationButtonData(data)
        return
