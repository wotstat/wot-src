from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBottomPanelMeta(BaseDAAPIComponent):

    def onBuyOrResearchClick(self):
        self._printOverrideError(b'onBuyOrResearchClick')
        return

    def onCarouselVehicleSelected(self, intCD):
        self._printOverrideError(b'onCarouselVehicleSelected')
        return

    def onOfferSelected(self, offerID):
        self._printOverrideError(b'onOfferSelected')
        return

    def showTooltip(self, intCD, itemType):
        self._printOverrideError(b'showTooltip')
        return

    def updateData(self, useCompactData):
        self._printOverrideError(b'updateData')
        return

    def onCouponSelected(self, isActive):
        self._printOverrideError(b'onCouponSelected')
        return

    def as_setBuyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuyData(data)
        return

    def as_setSetItemsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetItemsData(data)
        return

    def as_setCouponS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoupon(data)
        return

    def as_setSetVehiclesDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetVehiclesData(data)
        return

    def as_setOffersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setOffersData(data)
        return

    def as_setSetTitleTooltipS(self, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetTitleTooltip(tooltip)
        return

    def as_updateLeftTimeS(self, formattedTime, hasHoursAndMinutes=False):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLeftTime(formattedTime, hasHoursAndMinutes)
        return
