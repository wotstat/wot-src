from gui.Scaleform.framework.entities.View import View

class BattleQueueMeta(View):

    def startClick(self):
        self._printOverrideError(b'startClick')
        return

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

    def as_setPlayersS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayers(text)
        return

    def as_setDPS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_setDP(dataProvider)
        return

    def as_showStartS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showStart(vis)
        return

    def as_showExitS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showExit(vis)
        return
