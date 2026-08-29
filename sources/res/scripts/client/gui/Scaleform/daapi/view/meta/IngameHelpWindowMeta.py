from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameHelpWindowMeta(AbstractWindowView):

    def clickSettingWindow(self):
        self._printOverrideError(b'clickSettingWindow')
        return

    def as_setKeysS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setKeys(data)
        return
