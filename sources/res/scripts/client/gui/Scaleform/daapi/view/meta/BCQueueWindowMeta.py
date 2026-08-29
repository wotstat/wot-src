from gui.Scaleform.framework.entities.View import View

class BCQueueWindowMeta(View):

    def cancel(self):
        self._printOverrideError(b'cancel')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_showCancelButtonS(self, value, label, info):
        if self._isDAAPIInited():
            return self.flashObject.as_showCancelButton(value, label, info)
        return

    def as_setStatusTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusText(value)
        return
