from gui.Scaleform.framework.entities.View import View

class BCBattleResultMeta(View):

    def click(self):
        self._printOverrideError(b'click')
        return

    def onAnimationAwardStart(self, id):
        self._printOverrideError(b'onAnimationAwardStart')
        return

    def onToolTipShow(self, rendererId):
        self._printOverrideError(b'onToolTipShow')
        return

    def onVideoButtonClick(self, index):
        self._printOverrideError(b'onVideoButtonClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
