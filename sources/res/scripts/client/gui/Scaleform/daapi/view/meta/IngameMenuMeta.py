from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):

    def quitBattleClick(self):
        self._printOverrideError(b'quitBattleClick')
        return

    def settingsClick(self):
        self._printOverrideError(b'settingsClick')
        return

    def helpClick(self):
        self._printOverrideError(b'helpClick')
        return

    def cancelClick(self):
        self._printOverrideError(b'cancelClick')
        return

    def onCounterNeedUpdate(self):
        self._printOverrideError(b'onCounterNeedUpdate')
        return

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState)
        return

    def as_setServerStatsS(self, stats, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)
        return

    def as_setCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(counters)
        return

    def as_removeCounterS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_removeCounter(counters)
        return

    def as_setMenuButtonsLabelsS(self, helpLabel, settingsLabel, cancelLabel, quitLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuButtonsLabels(helpLabel, settingsLabel, cancelLabel, quitLabel)
        return

    def as_setMenuButtonsS(self, buttons):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuButtons(buttons)
        return

    def as_setVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibility(value)
        return
