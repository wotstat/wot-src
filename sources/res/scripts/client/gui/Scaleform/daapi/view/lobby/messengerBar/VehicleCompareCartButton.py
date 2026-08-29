from gui.Scaleform.daapi.view.meta.ButtonWithCounterMeta import ButtonWithCounterMeta
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket

class VehicleCompareCartButton(ButtonWithCounterMeta):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def _populate(self):
        super(VehicleCompareCartButton, self)._populate()
        self.comparisonBasket.onChange += self.__onCountChanged
        self.comparisonBasket.onSwitchChange += self.__onVehCmpBasketStateChanged
        self.__changeCount(self.comparisonBasket.getVehiclesCount())
        return

    def _dispose(self):
        self.comparisonBasket.onChange -= self.__onCountChanged
        self.comparisonBasket.onSwitchChange -= self.__onVehCmpBasketStateChanged
        super(VehicleCompareCartButton, self)._dispose()
        return

    def __onVehCmpBasketStateChanged(self):
        if not self.comparisonBasket.isEnabled():
            self.destroy()
        return

    def __onCountChanged(self, _):
        self.__changeCount(self.comparisonBasket.getVehiclesCount())
        return

    def __changeCount(self, count):
        self.as_setCountS(count)
        return
