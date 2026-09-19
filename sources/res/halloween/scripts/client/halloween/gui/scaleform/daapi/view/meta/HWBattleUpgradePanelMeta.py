from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HWBattleUpgradePanelMeta(BaseDAAPIComponent):

    def onSelectItem(self, itemID):
        self._printOverrideError(b'onSelectItem')
        return

    def onAppear(self):
        self._printOverrideError(b'onAppear')
        return

    def onItemHover(self):
        self._printOverrideError(b'onItemHover')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setAnomaliesMatrixHotkeyS(self, hotKey):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnomaliesMatrixHotkey(hotKey)
        return

    def as_toggleAlertStateS(self, isVisible, alertText=None):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleAlertState(isVisible, alertText)
        return

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)
        return

    def as_showSelectAnimS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectAnim(idx)
        return

    def as_showNotificationAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showNotificationAnim()
        return

    def as_hideNotificationAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideNotificationAnim()
        return
