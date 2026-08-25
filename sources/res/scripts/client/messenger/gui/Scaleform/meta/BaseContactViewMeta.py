from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseContactViewMeta(BaseDAAPIComponent):

    def onOk(self, data):
        self._printOverrideError(b'onOk')
        return

    def onCancel(self):
        self._printOverrideError(b'onCancel')
        return

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
        return

    def as_setOkBtnEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setOkBtnEnabled(isEnabled)
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_closeViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeView()
        return
