from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import CarouselEnvironment

class TankCarouselMeta(CarouselEnvironment):

    def restoreTank(self):
        self._printOverrideError(b'restoreTank')
        return

    def buyTank(self):
        self._printOverrideError(b'buyTank')
        return

    def buySlot(self):
        self._printOverrideError(b'buySlot')
        return

    def buyRentPromotion(self, intCD):
        self._printOverrideError(b'buyRentPromotion')
        return

    def selectTelecomRentalVehicle(self, intCD):
        self._printOverrideError(b'selectTelecomRentalVehicle')
        return

    def getCarouselAlias(self):
        self._printOverrideError(b'getCarouselAlias')
        return

    def setFilter(self, id):
        self._printOverrideError(b'setFilter')
        return

    def as_rowCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_rowCount(value)
        return

    def as_setSmallDoubleCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSmallDoubleCarousel(value)
        return

    def as_useExtendedCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_useExtendedCarousel(value)
        return

    def as_scrollToSlotS(self, slotIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToSlot(slotIdx)
        return
