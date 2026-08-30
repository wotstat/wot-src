from gui.Scaleform.framework.entities.View import View

class BattleRoyaleLevelUpViewMeta(View):

    def onIntroStartsPlaying(self):
        self._printOverrideError(b'onIntroStartsPlaying')
        return

    def onRibbonStartsPlaying(self):
        self._printOverrideError(b'onRibbonStartsPlaying')
        return

    def onCloseBtnClick(self):
        self._printOverrideError(b'onCloseBtnClick')
        return

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
