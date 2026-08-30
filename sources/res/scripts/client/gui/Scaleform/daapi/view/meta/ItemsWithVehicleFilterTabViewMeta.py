from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_type import FiltrableInventoryCategoryByTypeTabView

class ItemsWithVehicleFilterTabViewMeta(FiltrableInventoryCategoryByTypeTabView):

    def resetVehicleFilter(self):
        self._printOverrideError(b'resetVehicleFilter')
        return

    def as_initVehicleFilterS(self, vehicleFilterVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initVehicleFilter(vehicleFilterVO)
        return

    def as_updateVehicleFilterButtonS(self, vehicleFilterVO):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleFilterButton(vehicleFilterVO)
        return
