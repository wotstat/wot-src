from gui.Scaleform.framework.entities.View import View

class VehiclePostProgressionViewBaseMeta(View):

    def demountAllPairs(self):
        self._printOverrideError(b'demountAllPairs')
        return

    def as_setVehicleTitleS(self, vo):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTitle(vo)
        return

    def as_setDataS(self, vo):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(vo)
        return

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()
        return

    def as_onEscPressedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onEscPressed()
        return
