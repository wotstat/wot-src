from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialDialogMeta(AbstractWindowView):

    def submit(self):
        self._printOverrideError(b'submit')
        return

    def cancel(self):
        self._printOverrideError(b'cancel')
        return

    def as_setContentS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setContent(data)
        return

    def as_updateContentS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateContent(data)
        return
