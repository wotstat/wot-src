from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleCompareConfiguratorBaseViewMeta(BaseDAAPIComponent):

    def applyConfig(self):
        self._printOverrideError(b'applyConfig')
        return

    def resetConfig(self):
        self._printOverrideError(b'resetConfig')
        return

    def onCloseView(self):
        self._printOverrideError(b'onCloseView')
        return

    def as_setResetEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setResetEnabled(value)
        return

    def as_setApplyEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setApplyEnabled(value)
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return
