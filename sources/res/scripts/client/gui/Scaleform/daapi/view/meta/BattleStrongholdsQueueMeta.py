from gui.Scaleform.framework.entities.View import View

class BattleStrongholdsQueueMeta(View):

    def exitClick(self):
        self._printOverrideError(b'exitClick')
        return

    def onEscape(self):
        self._printOverrideError(b'onEscape')
        return

    def as_setTimerS(self, textLabel, timeLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(textLabel, timeLabel)
        return

    def as_setTypeInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTypeInfo(data)
        return

    def as_setLeaguesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setLeagues(data)
        return

    def as_showExitS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showExit(vis)
        return

    def as_showWaitingS(self, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(description)
        return

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()
        return
