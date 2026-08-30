from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import RegularInventoryCategoryTabView

class RegularItemsTabViewMeta(RegularInventoryCategoryTabView):

    def navigateToStore(self):
        self._printOverrideError(b'navigateToStore')
        return

    def sellItem(self, itemId):
        self._printOverrideError(b'sellItem')
        return

    def upgradeItem(self, itemId):
        self._printOverrideError(b'upgradeItem')
        return
