from gui.Scaleform.daapi.view.lobby.rally.BaseRallyView import BaseRallyView

class BaseRallyListViewMeta(BaseRallyView):

    def getRallyDetails(self, index):
        self._printOverrideError(b'getRallyDetails')
        return

    def as_selectByIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)
        return

    def as_selectByIDS(self, rallyID):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByID(rallyID)
        return

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()
        return

    def as_setDetailsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDetails(value)
        return

    def as_setVehiclesTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesTitle(value)
        return
