from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_vehicle import FiltrableInventoryCategoryByVehicleTabView

class StorageDevicesTabViewMeta(FiltrableInventoryCategoryByVehicleTabView):

    def onRestoreButtonClick(self):
        self._printOverrideError(b'onRestoreButtonClick')
        return

    def as_initModulesFilterS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initModulesFilter(data)
        return

    def as_setRestoreButtonDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRestoreButtonData(data)
        return

    def as_setBalanceValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBalanceValue(value)
        return
