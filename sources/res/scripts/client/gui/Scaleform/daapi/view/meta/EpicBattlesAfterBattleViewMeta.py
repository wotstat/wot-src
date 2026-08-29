from gui.Scaleform.framework.entities.View import View

class EpicBattlesAfterBattleViewMeta(View):

    def onIntroStartsPlaying(self):
        self._printOverrideError(b'onIntroStartsPlaying')
        return

    def onRibbonStartsPlaying(self):
        self._printOverrideError(b'onRibbonStartsPlaying')
        return

    def onNextBtnClick(self):
        self._printOverrideError(b'onNextBtnClick')
        return

    def onCloseBtnClick(self):
        self._printOverrideError(b'onCloseBtnClick')
        return

    def onRewardsBtnClick(self):
        self._printOverrideError(b'onRewardsBtnClick')
        return

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return

    def onProgressBarStartAnim(self):
        self._printOverrideError(b'onProgressBarStartAnim')
        return

    def onProgressBarCompleteAnim(self):
        self._printOverrideError(b'onProgressBarCompleteAnim')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
