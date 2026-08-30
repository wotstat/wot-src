from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PrequeueWindowMeta(AbstractWindowView):

    def requestToEnqueue(self):
        self._printOverrideError(b'requestToEnqueue')
        return

    def requestToLeave(self):
        self._printOverrideError(b'requestToLeave')
        return

    def showFAQWindow(self):
        self._printOverrideError(b'showFAQWindow')
        return

    def isEnqueueBtnEnabled(self):
        self._printOverrideError(b'isEnqueueBtnEnabled')
        return

    def isLeaveBtnEnabled(self):
        self._printOverrideError(b'isLeaveBtnEnabled')
        return

    def as_enableLeaveBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableLeaveBtn(value)
        return

    def as_enableEnqueueBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableEnqueueBtn(value)
        return
