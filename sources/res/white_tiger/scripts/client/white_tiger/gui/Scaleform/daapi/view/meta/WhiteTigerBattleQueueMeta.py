from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import BattleQueue

class WhiteTigerBattleQueueMeta(BattleQueue):

    def onQuickStartPanelAction(self, vehID):
        self._printOverrideError(b'onQuickStartPanelAction')
        return

    def as_setAverageTimeS(self, textLabel, timeLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setAverageTime(textLabel, timeLabel)
        return

    def as_setInfoTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfoText(text)
        return

    def as_showQuickStartPanelS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showQuickStartPanel(data)
        return

    def as_hideQuickStartPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideQuickStartPanel()
        return
