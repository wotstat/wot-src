from gui.Scaleform.daapi.view.lobby.storage.category_view import InventoryCategoryView

class StorageCategoryForSellViewMeta(InventoryCategoryView):

    def navigateToStore(self):
        self._printOverrideError(b'navigateToStore')
        return

    def selectItem(self, itemId, isSelected):
        self._printOverrideError(b'selectItem')
        return

    def selectAll(self, isSelected):
        self._printOverrideError(b'selectAll')
        return

    def sellItem(self, itemId):
        self._printOverrideError(b'sellItem')
        return

    def sellAll(self):
        self._printOverrideError(b'sellAll')
        return

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
        return
