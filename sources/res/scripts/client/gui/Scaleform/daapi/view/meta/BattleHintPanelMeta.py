from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleHintPanelMeta(BaseDAAPIComponent):

    def onPlaySound(self, soundType):
        self._printOverrideError(b'onPlaySound')
        return

    def onHideComplete(self):
        self._printOverrideError(b'onHideComplete')
        return

    def as_setDataS(self, vKey, key, messageLeft, messageRight, offsetX, offsetY, reducedPanning, centeredMessage=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(vKey, key, messageLeft, messageRight, offsetX, offsetY, reducedPanning, centeredMessage)
        return

    def as_toggleS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_toggle(isShow)
        return
