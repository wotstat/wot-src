from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class VehicleCompareCartPopoverMeta(SmartPopOverView):

    def remove(self, id):
        self._printOverrideError(b'remove')
        return

    def removeAll(self):
        self._printOverrideError(b'removeAll')
        return

    def gotoCompareView(self):
        self._printOverrideError(b'gotoCompareView')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_updateToCmpBtnPropsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateToCmpBtnProps(data)
        return

    def as_updateClearBtnPropsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateClearBtnProps(data)
        return
