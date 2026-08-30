from gui.Scaleform.framework.entities.View import View

class ColorSettingsViewMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onApply(self, diff):
        self._printOverrideError(b'onApply')
        return

    def onReset(self):
        self._printOverrideError(b'onReset')
        return

    def onSettingsChange(self, settingName, settingValue):
        self._printOverrideError(b'onSettingsChange')
        return

    def onTabSelected(self, selectedTab):
        self._printOverrideError(b'onTabSelected')
        return

    def setViewWidth(self, value):
        self._printOverrideError(b'setViewWidth')
        return

    def moveSpace(self, x, y, delta):
        self._printOverrideError(b'moveSpace')
        return

    def as_initDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)
        return

    def as_updateDataS(self, selectedTab, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateData(selectedTab, data)
        return
