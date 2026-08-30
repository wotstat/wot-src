from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_type import FiltrableInventoryCategoryByTypeTabView

class StorageCategoryCustomizationViewMeta(FiltrableInventoryCategoryByTypeTabView):

    def navigateToCustomization(self):
        self._printOverrideError(b'navigateToCustomization')
        return

    def sellCustomizationItem(self, itemCD, vehicleCD):
        self._printOverrideError(b'sellCustomizationItem')
        return

    def previewItem(self, itemCD, vehicleCD):
        self._printOverrideError(b'previewItem')
        return
