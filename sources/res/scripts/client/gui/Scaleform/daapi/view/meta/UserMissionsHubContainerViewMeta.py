from gui.Scaleform.framework.entities.View import View

class UserMissionsHubContainerViewMeta(View):

    def resetFilters(self):
        self._printOverrideError(b'resetFilters')
        return

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def as_showFilterCounterS(self, countText, isFilterApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterCounter(countText, isFilterApplied)
        return

    def as_blinkFilterCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkFilterCounter()
        return

    def as_updateCommonMissionsTabVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommonMissionsTabVisibility(isVisible)
        return

    def as_updateCommonMissionsTabPositionS(self, posY, maxHeight):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommonMissionsTabPosition(posY, maxHeight)
        return

    def as_setBackgroundS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(source)
        return
