from __future__ import absolute_import
import constants
from constants import RentType, GameSeasonType
from rent_common import parseRentID, isWithinMaxRentTime, SeasonRentDuration
from soft_exception import SoftException
from gui.impl import backport
from gui.impl.gen.resources import R
from gui.Scaleform.daapi.view.meta.RentalTermSelectionPopoverMeta import RentalTermSelectionPopoverMeta
from gui.Scaleform.locale.STORE import STORE
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import ShopEvent
from gui.shared.formatters import text_styles, getItemPricesVO, getMoneyVO
from gui.shared.money import Money
from gui.shared.gui_items.gui_item_economics import ItemPrice
from helpers import dependency, i18n
from skeletons.gui.shared import IItemsCache
_NOT_RENT_IDX = -1
_SEASON_RENT_TERMS = {(GameSeasonType.EPIC): {(RentType.SEASON_RENT): (STORE.RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_EPICSEASON), 
                           (RentType.SEASON_CYCLE_RENT): (STORE.RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_EPICCYCLE)}, 
   (GameSeasonType.RANKED): {(RentType.SEASON_RENT): (STORE.RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_RANKEDSEASON), 
                             (RentType.SEASON_CYCLE_RENT): (STORE.RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_RANKEDCYCLE)}}

class RentalTermSelectionPopover(RentalTermSelectionPopoverMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(RentalTermSelectionPopover, self).__init__()
        data = ctx.get(b'data')
        self.__vehicleIntCD = int(data.vehicleIntCD)
        self.__selectedRentID = int(data.selectedRentTerm)
        return

    def selectTerm(self, itemId):
        self.fireEvent(ShopEvent(ShopEvent.SELECT_RENT_TERM, ctx=itemId), EVENT_BUS_SCOPE.LOBBY)
        self.itemsCache.onSyncCompleted -= self.__onItemCacheSyncCompleted
        self.destroy()
        return

    def _populate(self):
        super(RentalTermSelectionPopover, self)._populate()
        self.as_setInitDataS(self.__getInitialVO())
        self.itemsCache.onSyncCompleted += self.__onItemCacheSyncCompleted
        return

    def __onItemCacheSyncCompleted(self, *args):
        self.as_setInitDataS(self.__getInitialVO())
        return

    def __getInitialVO(self):
        vehicle = self.itemsCache.items.getItemByCD(self.__vehicleIntCD)
        isEnoughStatuses = getMoneyVO(Money.makeFromMoneyTuple((True, True, True)))
        rentalTermSlots = []
        isRestoreAvailable = vehicle.isRestoreAvailable()
        if isRestoreAvailable:
            enabled = isRestoreAvailable or not (constants.IS_CHINA and vehicle.rentalIsActive)
            rentalTermSlots.append({b'itemId': (-1), 
               b'label': (backport.text(R.strings.hangar.buyVehicleWindow.restore())), 
               b'price': (getItemPricesVO(ItemPrice(vehicle.restorePrice, vehicle.restorePrice))), 
               b'enabled': enabled, 
               b'selected': (self.__selectedRentID <= _NOT_RENT_IDX), 
               b'isEnoughStatuses': isEnoughStatuses})
        rentPackages = vehicle.rentPackages
        currentSeasonRent = vehicle.currentSeasonRent
        isSeasonRented = currentSeasonRent is not None
        for rentPackageIdx, rentPackage in enumerate(rentPackages):
            rentID = rentPackage[b'rentID']
            rentType, packageID = parseRentID(rentID)
            if rentType == constants.RentType.TIME_RENT:
                days = packageID
                standardRentDays = STORE.getRentTermDays(days)
                if standardRentDays is not None:
                    label = standardRentDays
                else:
                    label = i18n.makeString(STORE.RENTALTERMSELECTIONPOPOVER_TERMSLOTANY, days=days)
                inMaxRentTime = isWithinMaxRentTime(vehicle.maxRentDuration, vehicle.rentLeftTime, days)
                enabled = not isSeasonRented and inMaxRentTime
            elif rentType in (constants.RentType.SEASON_RENT, constants.RentType.SEASON_CYCLE_RENT):
                seasonType = rentPackage[b'seasonType']
                label = i18n.makeString(_SEASON_RENT_TERMS[seasonType][rentType])
                if rentType == constants.RentType.SEASON_RENT:
                    enabled = not isSeasonRented or isSeasonRented and currentSeasonRent.duration == SeasonRentDuration.SEASON_CYCLE
                else:
                    enabled = not isSeasonRented
            else:
                raise SoftException((b'Unsupported rental type [{}]!').format(rentType))
            price = ItemPrice(rentPackage[b'rentPrice'], rentPackage[b'defaultRentPrice'])
            rentalTermSlots.append({b'itemId': rentPackageIdx, 
               b'label': label, 
               b'price': (getItemPricesVO(price)), 
               b'enabled': enabled, 
               b'selected': (self.__selectedRentID == rentID), 
               b'isEnoughStatuses': isEnoughStatuses})

        if not isRestoreAvailable:
            enabled = not vehicle.isDisabledForBuy and not vehicle.isHidden
            rentalTermSlots.append({b'itemId': _NOT_RENT_IDX, 
               b'label': (i18n.makeString(STORE.RENTALTERMSELECTIONPOPOVER_TERMSLOTUNLIM)), 
               b'price': (getItemPricesVO(vehicle.buyPrices.itemPrice)), 
               b'enabled': enabled, 
               b'selected': (self.__selectedRentID <= _NOT_RENT_IDX), 
               b'isEnoughStatuses': isEnoughStatuses})
        return {b'titleLabel': (text_styles.highTitle(STORE.RENTALTERMSELECTIONPOPOVER_TITLELABEL)), 
           b'rentalTermSlots': rentalTermSlots}
