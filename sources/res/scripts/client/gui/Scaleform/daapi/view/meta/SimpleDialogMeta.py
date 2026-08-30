from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleDialogMeta(AbstractWindowView):

    def onButtonClick(self, buttonId):
        self._printOverrideError(b'onButtonClick')
        return

    def as_setTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(text)
        return

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)
        return

    def as_setButtonsS(self, buttonNames):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonNames)
        return

    def as_setButtonEnablingS(self, id, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonEnabling(id, isEnabled)
        return

    def as_setButtonFocusS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonFocus(id)
        return
