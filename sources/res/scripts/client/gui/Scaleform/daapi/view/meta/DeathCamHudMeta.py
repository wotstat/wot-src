from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DeathCamHudMeta(BaseDAAPIComponent):

    def onAnimationFinished(self):
        self._printOverrideError(b'onAnimationFinished')
        return

    def as_setTextsS(self, cameraText, skipText):
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(cameraText, skipText)
        return

    def as_showBarsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBars()
        return

    def as_hideBarsS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBars(isActive)
        return
