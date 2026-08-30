from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationStyleInfoMeta(BaseDAAPIComponent):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onApply(self):
        self._printOverrideError(b'onApply')
        return

    def onWidthUpdated(self, x, width, height):
        self._printOverrideError(b'onWidthUpdated')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_buttonUpdateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_buttonUpdate(data)
        return

    def as_setBackgroundAlphaS(self, alpha):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackgroundAlpha(alpha)
        return

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return
