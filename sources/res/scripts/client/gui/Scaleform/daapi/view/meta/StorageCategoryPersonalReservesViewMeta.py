from gui.Scaleform.daapi.view.lobby.storage.category_view import BaseCategoryView

class StorageCategoryPersonalReservesViewMeta(BaseCategoryView):

    def navigateToStore(self):
        self._printOverrideError(b'navigateToStore')
        return

    def activateReserve(self, boosterId):
        self._printOverrideError(b'activateReserve')
        return

    def resetFilter(self):
        self._printOverrideError(b'resetFilter')
        return

    def onFiltersChange(self, filters):
        self._printOverrideError(b'onFiltersChange')
        return

    def onInfoClicked(self):
        self._printOverrideError(b'onInfoClicked')
        return

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
        return

    def as_initFilterS(self, typeFiltersVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initFilter(typeFiltersVO)
        return

    def as_resetFilterS(self, resetData):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFilter(resetData)
        return

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)
        return
