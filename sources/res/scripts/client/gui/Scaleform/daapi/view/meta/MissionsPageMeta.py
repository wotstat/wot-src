from gui.Scaleform.framework.entities.View import View

class MissionsPageMeta(View):

    def resetFilters(self):
        self._printOverrideError(b'resetFilters')
        return

    def onTabSelected(self, alias, prefix):
        self._printOverrideError(b'onTabSelected')
        return

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def as_setTabsDataProviderS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsDataProvider(dataProvider)
        return

    def as_showFilterS(self, visible, topShadowVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilter(visible, topShadowVisible)
        return

    def as_showFilterCounterS(self, countText, isFilterApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterCounter(countText, isFilterApplied)
        return

    def as_blinkFilterCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkFilterCounter()
        return

    def as_setTabsCounterDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsCounterData(data)
        return

    def as_showBattleMattersAnimationS(self, animPath, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showBattleMattersAnimation(animPath, data)
        return
