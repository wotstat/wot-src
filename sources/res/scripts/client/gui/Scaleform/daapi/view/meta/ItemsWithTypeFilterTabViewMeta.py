from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import InventoryCategoryView

class ItemsWithTypeFilterTabViewMeta(InventoryCategoryView):

    def sellItem(self, itemId):
        self._printOverrideError(b'sellItem')
        return

    def resetFilter(self):
        self._printOverrideError(b'resetFilter')
        return

    def onFiltersChange(self, filters):
        self._printOverrideError(b'onFiltersChange')
        return

    def navigateToStore(self):
        self._printOverrideError(b'navigateToStore')
        return

    def upgradeItem(self, itemId):
        self._printOverrideError(b'upgradeItem')
        return

    def as_initTypeFilterS(self, typeFiltersVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initTypeFilter(typeFiltersVO)
        return

    def as_resetFilterS(self, resetData):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFilter(resetData)
        return

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)
        return
