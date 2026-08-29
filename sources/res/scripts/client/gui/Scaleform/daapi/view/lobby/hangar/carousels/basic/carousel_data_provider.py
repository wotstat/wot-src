import typing, BigWorld
from account_helpers.telecom_rentals import TelecomRentals
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform import MENU
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import getStatusStrings
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from telecom_rentals_common import ROSTER_EXPIRATION_TOKEN_NAME, PARTNERSHIP_TOKEN_NAME
if typing.TYPE_CHECKING:
    from typing import Set, Dict

class _FRONT_SUPPLY_ITEMS(object):
    RENT_TANK = 0
    ALL = (RENT_TANK,)


class _SUPPLY_ITEMS(object):
    BUY_TANK = 0
    RESTORE_TANK = 1
    BUY_SLOT = 2
    ALL = (BUY_TANK, RESTORE_TANK, BUY_SLOT)


class HangarCarouselDataProvider(CarouselDataProvider):
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)

    def __init__(self, carouselFilter, itemsCache):
        super(HangarCarouselDataProvider, self).__init__(carouselFilter, itemsCache)
        self._serverSettings = self._lobbyContext.getServerSettings()
        self._setBaseCriteria()
        self._frontSupplyItems = []
        self._telecomRentalsVehicles = []
        self._supplyItems = []
        self._emptySlotsCount = 0
        self._restorableVehiclesCount = 0
        self._telecomRentals = None
        return

    def _populate(self):
        self._wotPlusCtrl.onDataChanged += self._onWotPlusDataChanged
        self._telecomRentals = BigWorld.player().telecomRentals
        self._telecomRentals.onPendingRentChanged += self._onTelecomPendingRentChanged
        g_clientUpdateManager.addCallback(b'tokens', self._onTelecomRentalsChanged)
        super(HangarCarouselDataProvider, self)._populate()
        return

    def _dispose(self):
        self._wotPlusCtrl.onDataChanged -= self._onWotPlusDataChanged
        self._telecomRentals.onPendingRentChanged -= self._onTelecomPendingRentChanged
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        super(HangarCarouselDataProvider, self)._dispose()
        return

    def _onWotPlusDataChanged(self, diff):
        if b'exclusiveVehicle' in diff:
            self.buildList()
        return

    def _onTelecomRentalsChanged(self, diff):
        if PARTNERSHIP_TOKEN_NAME in diff or ROSTER_EXPIRATION_TOKEN_NAME in diff:
            self.buildList()
        return

    def _onTelecomPendingRentChanged(self, vehCD):
        if vehCD is not None:
            self.buildList()
        return

    @property
    def collection(self):
        return self._vehicleItems + self._supplyItems + self._frontSupplyItems

    def getCurrentVehiclesCount(self):
        frontItems = len(self._getFrontAdditionalItemsIndexes())
        backItems = len(self._getAdditionalItemsIndexes())
        return len(self._filteredIndices) - backItems - frontItems

    def updateVehicles(self, vehiclesCDs=None, filterCriteria=None, forceUpdate=False):
        rentalVehicles = self._telecomRentalsVehicles
        changeInRentals = set(vehiclesCDs or ()).issubset(rentalVehicles)
        filterCriteria = filterCriteria or REQ_CRITERIA.EMPTY
        if vehiclesCDs:
            filterCriteria |= REQ_CRITERIA.IN_CD_LIST(vehiclesCDs)
        criteria = self._baseCriteria | filterCriteria | REQ_CRITERIA.VEHICLE.ACTIVE_IN_NATION_GROUP | REQ_CRITERIA.VEHICLE.TELECOM_RENT
        newRentalsVehicles = self._itemsCache.items.getVehicles(criteria).viewkeys()
        isVehicleRemoved = not set(vehiclesCDs or ()).issubset(newRentalsVehicles)
        isVehicleAdded = not set(vehiclesCDs or ()).issubset(rentalVehicles)
        if changeInRentals or isVehicleRemoved or isVehicleAdded:
            telecomPendingVehCD = self._telecomRentals.getRentsPending()
            telecomPendingVehCD = telecomPendingVehCD.intersection(newRentalsVehicles)
            if isVehicleAdded and telecomPendingVehCD:
                self._telecomRentals.resetRentsPending(telecomPendingVehCD)
            self.buildList()
            return
        super(HangarCarouselDataProvider, self).updateVehicles(vehiclesCDs, filterCriteria, forceUpdate)
        return

    def updateSupplies(self):
        self._supplyItems = []
        self._buildSupplyItems()
        self.flashObject.invalidateItems(self._getSupplyIndices(), self._supplyItems)
        self.applyFilter()
        return

    def clear(self):
        super(HangarCarouselDataProvider, self).clear()
        self._supplyItems = []
        self._frontSupplyItems = []
        return

    def _setBaseCriteria(self):
        self._baseCriteria = REQ_CRITERIA.INVENTORY
        self._baseCriteria |= ~REQ_CRITERIA.VEHICLE.MODE_HIDDEN
        self._baseCriteria |= ~REQ_CRITERIA.VEHICLE.BATTLE_ROYALE
        self._baseCriteria |= ~REQ_CRITERIA.VEHICLE.HIDDEN_IN_HANGAR
        return

    def _buildTelecomRentalVehicleItems(self):
        self._telecomRentalsVehicles = []
        rentPromotionCriteria = REQ_CRITERIA.VEHICLE.TELECOM_RENT | self._baseCriteria
        oldVehLen = len(self._vehicles)
        self._addVehicleItemsByCriteria(rentPromotionCriteria)
        totalRentVehicles = len(self._vehicles) - oldVehLen
        if totalRentVehicles > 0:
            self._telecomRentalsVehicles = [veh.intCD for veh in self._vehicles[-totalRentVehicles:]]
        return

    def _buildRentPromitionVehicleItems(self):
        rentPromotionCriteria = REQ_CRITERIA.VEHICLE.RENT_PROMOTION | ~self._baseCriteria
        self._addVehicleItemsByCriteria(rentPromotionCriteria)
        return

    def _buildVehicleItems(self):
        super(HangarCarouselDataProvider, self)._buildVehicleItems()
        self._buildTelecomRentalVehicleItems()
        self._buildRentPromitionVehicleItems()
        self._buildSupplyItems()
        self._buildFrontSupplyItems()
        return

    def _getFrontAdditionalItemsIndexes(self):
        frontIndices = self._getFrontIndices()
        pruneIndices = set()
        if not self._isTelecomRentalsEnabled() or self._telecomRentals.getAvailableRentCount() == 0:
            pruneIndices.add(_FRONT_SUPPLY_ITEMS.RENT_TANK)
        return [suppIdx for suppIdx in frontIndices if frontIndices.index(suppIdx) not in pruneIndices]

    def _getAdditionalItemsIndexes(self):
        supplyIndices = self._getSupplyIndices()
        restoreEnabled = self._serverSettings.isVehicleRestoreEnabled()
        storageEnabled = self._serverSettings.isStorageEnabled()
        pruneIndices = set()
        if not self._emptySlotsCount:
            pruneIndices.add(_SUPPLY_ITEMS.BUY_TANK)
        if self._restorableVehiclesCount == 0 or not restoreEnabled or not storageEnabled:
            pruneIndices.add(_SUPPLY_ITEMS.RESTORE_TANK)
        return [suppIdx for suppIdx in supplyIndices if supplyIndices.index(suppIdx) not in pruneIndices]

    def _buildSupplyItems(self):
        self._supplyItems = []
        items = self._itemsCache.items
        inventory = self._itemsCache.items.inventory
        slots = items.stats.vehicleSlots
        slotPrice = items.shop.getVehicleSlotsPrice(slots)
        defaultSlotPrice = items.shop.defaults.getVehicleSlotsPrice(slots)
        self._emptySlotsCount = inventory.getFreeSlots(slots)
        restoreVehsCriteria = REQ_CRITERIA.IN_CD_LIST(items.recycleBin.getVehiclesIntCDs()) | REQ_CRITERIA.VEHICLE.IS_RESTORE_POSSIBLE | ~REQ_CRITERIA.INVENTORY ^ REQ_CRITERIA.VEHICLE.TELECOM_RENT
        self._restorableVehiclesCount = len(items.getVehicles(restoreVehsCriteria))
        if slotPrice != defaultSlotPrice:
            discount = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, b'slotsPrices', True, slotPrice, defaultSlotPrice)
        else:
            discount = None
        smallBuySlotString, buySlotString = getStatusStrings(b'buySlot')
        smallBuyTankString, buyTankString = getStatusStrings(b'buyTank')
        smallRestoreTankString, restoreTankString = getStatusStrings(b'restoreTank')
        smallRestoreTankCountString, restoreTankCountString = getStatusStrings(b'restoreTankCount', style=text_styles.main, ctx={b'count': (self._restorableVehiclesCount)})
        smallEmptySlotsString, emptySlotsString = getStatusStrings(b'buyTankEmptyCount', style=text_styles.main, ctx={b'count': (self._emptySlotsCount)})
        self._supplyItems.append({b'buyTank': True, 
           b'smallInfoText': (text_styles.concatStylesToMultiLine(smallBuyTankString, smallEmptySlotsString)), 
           b'infoText': (text_styles.concatStylesToMultiLine(buyTankString, emptySlotsString)), 
           b'icon': (RES_ICONS.MAPS_ICONS_LIBRARY_TANKITEM_BUY_TANK), 
           b'tooltip': (TOOLTIPS.TANKS_CAROUSEL_BUY_VEHICLE_NEW)})
        self._supplyItems.append({b'restoreTank': True, 
           b'smallInfoText': (text_styles.concatStylesToMultiLine(smallRestoreTankString, smallRestoreTankCountString)), 
           b'infoText': (text_styles.concatStylesToMultiLine(restoreTankString, restoreTankCountString)), 
           b'icon': (RES_ICONS.MAPS_ICONS_LIBRARY_TANKITEM_BUY_TANK), 
           b'tooltip': (TOOLTIPS.TANKS_CAROUSEL_RESTORE_VEHICLE)})
        slotPriceCurrency = slotPrice.getCurrency()
        buySlotVO = {b'buySlot': True, 
           b'slotPrice': (slotPrice.get(slotPriceCurrency, 0)), 
           b'slotPriceCurrency': slotPriceCurrency, 
           b'icon': (RES_ICONS.MAPS_ICONS_LIBRARY_TANKITEM_BUY_SLOT), 
           b'infoText': buySlotString, 
           b'smallInfoText': smallBuySlotString, 
           b'hasSale': (discount is not None), 
           b'tooltip': (TOOLTIPS.TANKS_CAROUSEL_BUY_SLOT)}
        if discount is not None:
            buySlotVO.update({b'slotPriceActionData': discount})
        self._supplyItems.append(buySlotVO)
        return

    def _buildFrontSupplyItems(self):
        self._frontSupplyItems = []
        if self._isTelecomRentalsEnabled() and not self._telecomRentals.getAvailableRentCount() == 0:
            text = MENU.TANKCAROUSEL_WOTPLUSSELECTIONAVAILABLE
            if self._telecomRentals.getRentsPending():
                text = MENU.TANKCAROUSEL_WOTPLUSSELECTIONPENDING
            self._frontSupplyItems.append({b'isWotPlusSlot': True, 
               b'infoText': (text_styles.vehicleStatusInfoText(text)), 
               b'infoHoverText': (text_styles.vehicleStatusInfoText(text)), 
               b'smallInfoText': (text_styles.vehicleStatusSimpleText(text)), 
               b'icon': (RES_ICONS.MAPS_ICONS_LIBRARY_TANKITEM_BUY_TANK), 
               b'extraImage': (RES_ICONS.MAPS_ICONS_LIBRARY_RENT_ICO_BIG), 
               b'tooltip': (TOOLTIPS.TANKS_CAROUSEL_WOT_PLUS_SLOT)})
        return

    @staticmethod
    def _isSuitableForQueue(vehicle):
        return vehicle.getCustomState() != Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE

    def _getFrontIndices(self):
        previousItemsCount = len(self._vehicles) + len(_SUPPLY_ITEMS.ALL)
        return [previousItemsCount + idx for idx in _FRONT_SUPPLY_ITEMS.ALL]

    def _getSupplyIndices(self):
        return [len(self._vehicles) + idx for idx in _SUPPLY_ITEMS.ALL]

    def _isTelecomRentalsEnabled(self):
        hasTelecomRentalsActive = self._telecomRentals.isActive()
        isRentalEnabled = self._serverSettings.isTelecomRentalsEnabled()
        return hasTelecomRentalsActive and isRentalEnabled


class BCCarouselDataProvider(CarouselDataProvider):

    @property
    def collection(self):
        return self._vehicleItems

    def updateSupplies(self):
        return

    def _buildVehicleItems(self):
        super(BCCarouselDataProvider, self)._buildVehicleItems()
        for vehicleItem in self._vehicleItems:
            vehicleItem[b'infoText'] = b''
            vehicleItem[b'smallInfoText'] = b''

        return

    def setShowStats(self, showVehicleStats):
        return

    def selectVehicle(self, idx):
        self._selectedIdx = idx
        realIdx = self._filteredIndices[idx]
        return self._vehicles[realIdx].invID

    def _buildVehicle(self, vehicle):
        vehicle.dailyXPFactor = 1
        return super(BCCarouselDataProvider, self)._buildVehicle(vehicle)
