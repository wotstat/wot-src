from gui.Scaleform.framework.entities.View import View

class GammaWizardViewMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onApply(self):
        self._printOverrideError(b'onApply')
        return

    def onChangeGamma(self, value):
        self._printOverrideError(b'onChangeGamma')
        return

    def onReset(self):
        self._printOverrideError(b'onReset')
        return

    def updateTexture(self, x, y, size):
        self._printOverrideError(b'updateTexture')
        return

    def as_initDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)
        return
