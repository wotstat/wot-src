from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleHintMeta(BaseDAAPIComponent):

    def onFadeOutFinished(self):
        self._printOverrideError(b'onFadeOutFinished')
        return

    def as_showHintS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(data)
        return

    def as_hideHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint()
        return

    def as_clearPinnableHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearPinnableHint()
        return

    def as_cancelFadeOutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelFadeOut()
        return
