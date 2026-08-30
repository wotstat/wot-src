from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TabScreenMeta(BaseDAAPIComponent):

    def onSelectQuest(self, questID):
        self._printOverrideError(b'onSelectQuest')
        return

    def onStatsTableVisibiltyToggled(self, isVisible):
        self._printOverrideError(b'onStatsTableVisibiltyToggled')
        return

    def as_questProgressPerformS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_questProgressPerform(data)
        return

    def as_updateProgressTrackingS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressTracking(data)
        return

    def as_setActiveTabS(self, tabIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setActiveTab(tabIndex)
        return

    def as_resetActiveTabS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetActiveTab()
        return

    def as_updateTabsS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTabs(dataProvider)
        return
