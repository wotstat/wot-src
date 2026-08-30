from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RecoveryPanelMeta(BaseDAAPIComponent):

    def as_updateTimerS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(time)
        return

    def as_displayHintS(self, display, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_displayHint(display, animate)
        return

    def as_displayCooldownS(self, display, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_displayCooldown(display, animate)
        return

    def as_setupTextsS(self, hint1, hint2, button):
        if self._isDAAPIInited():
            return self.flashObject.as_setupTexts(hint1, hint2, button)
        return

    def as_updateTextsS(self, button):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTexts(button)
        return
