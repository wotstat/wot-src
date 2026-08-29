from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SessionStatsOverviewMeta(BaseDAAPIComponent):

    def onClickMoreBtn(self):
        self._printOverrideError(b'onClickMoreBtn')
        return

    def onClickResetBtn(self):
        self._printOverrideError(b'onClickResetBtn')
        return

    def onClickSettingsBtn(self):
        self._printOverrideError(b'onClickSettingsBtn')
        return

    def onExpanded(self, value):
        self._printOverrideError(b'onExpanded')
        return

    def onTabSelected(self, alias):
        self._printOverrideError(b'onTabSelected')
        return

    def onCounterUpdated(self):
        self._printOverrideError(b'onCounterUpdated')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setButtonsStateS(self, states):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonsState(states)
        return

    def as_setHeaderTooltipS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderTooltip(value)
        return
