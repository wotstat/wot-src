from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel

class PvePostmortemPanelMeta(PostmortemPanel):

    def updateTime(self, value):
        self._printOverrideError(b'updateTime')
        return

    def as_setHintTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintTitle(value)
        return

    def as_setHintDescrS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintDescr(value)
        return

    def as_setTimerS(self, totalTime, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(totalTime, currentTime)
        return

    def as_setCanExitS(self, canExit):
        if self._isDAAPIInited():
            return self.flashObject.as_setCanExit(canExit)
        return

    def as_showLockedLivesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showLockedLives()
        return

    def as_hidePanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hidePanel()
        return
