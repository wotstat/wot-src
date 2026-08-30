from gui.Scaleform.framework.entities.View import View

class AmmunitionSetupViewMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return

    def as_gfSizeUpdatedS(self, x, width, bottomMargin):
        if self._isDAAPIInited():
            return self.flashObject.as_gfSizeUpdated(x, width, bottomMargin)
        return

    def as_showCloseAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showCloseAnim()
        return

    def as_onAnimationEndS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onAnimationEnd()
        return

    def as_toggleParamsS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleParams(isVisible)
        return
