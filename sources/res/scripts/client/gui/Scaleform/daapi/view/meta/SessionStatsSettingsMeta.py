from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SessionStatsSettingsMeta(BaseDAAPIComponent):

    def onClickApplyBtn(self):
        self._printOverrideError(b'onClickApplyBtn')
        return

    def onClickBackBtn(self):
        self._printOverrideError(b'onClickBackBtn')
        return

    def onClickResetBtn(self):
        self._printOverrideError(b'onClickResetBtn')
        return

    def onSettingsInputChanged(self, identifier, value):
        self._printOverrideError(b'onSettingsInputChanged')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setControlsStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsState(data)
        return

    def as_setBattleSettingsStatusS(self, value, showWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleSettingsStatus(value, showWarning)
        return
