from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBoardsVehiclesOverlayMeta(BaseDAAPIComponent):

    def changeFilter(self, id):
        self._printOverrideError(b'changeFilter')
        return

    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        self._printOverrideError(b'applyFilters')
        return

    def as_setHeaderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)
        return

    def as_setFiltersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilters(data)
        return

    def as_setVehiclesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicles(data)
        return
