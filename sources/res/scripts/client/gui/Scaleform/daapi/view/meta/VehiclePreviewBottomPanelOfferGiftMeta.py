from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBottomPanelOfferGiftMeta(BaseDAAPIComponent):

    def onBuyClick(self):
        self._printOverrideError(b'onBuyClick')
        return

    def showTooltip(self, intCD, itemType):
        self._printOverrideError(b'showTooltip')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setSetItemsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetItemsData(data)
        return
