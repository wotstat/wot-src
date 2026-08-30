from gui.Scaleform.framework.entities.View import View

class StorageRestoreDevicesViewMeta(View):

    def onBackClick(self):
        self._printOverrideError(b'onBackClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
