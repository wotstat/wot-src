from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class MapsTrainingIngameHelpWindowMeta(AbstractWindowView):

    def clickSettingWindow(self):
        self._printOverrideError(b'clickSettingWindow')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
