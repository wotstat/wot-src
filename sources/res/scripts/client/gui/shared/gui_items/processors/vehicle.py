import logging
from itertools import chain
import BigWorld, AccountCommands
from constants import RentType, SEASON_NAME_BY_TYPE, CLIENT_COMMAND_SOURCES
from AccountCommands import VEHICLE_SETTINGS_FLAG
from gui.impl import backport
from gui.impl.gen import R
from nation_change.nation_change_helpers import getMainVehicleInNationGroup, hasNationGroup, getNationGroupID
from gui.shared.gui_items.processors.messages.items_processor_messages import ItemBuyProcessorMessage, BattleAbilitiesApplyProcessorMessage, LayoutApplyProcessorMessage, BattleBoostersApplyProcessorMessage, OptDevicesApplyProcessorMessage, ConsumablesApplyProcessorMessage, ShellsApplyProcessorMessage
from gui.shared.gui_items.vehicle_equipment import EMPTY_ITEM
from gui.veh_post_progression.messages import makeVehiclePostProgressionUnlockMsg, makeAllPairsDiscardMsg
from items import EQUIPMENT_TYPES
from items.components.c11n_constants import SeasonType
from adisp import adisp_process, adisp_async
from gui import SystemMessages, g_tankActiveCamouflage
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE, CURRENCY_TO_SM_TYPE
from gui.shared.formatters import formatPrice, text_styles, getStyle, getBWFormatter
from gui.shared.formatters import icons
from gui.shared.formatters.time_formatters import formatTime, getTimeLeftInfo
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import getCrewCount
from gui.shared.gui_items.processors import ItemProcessor, Processor, makeI18nSuccess, makeI18nError, plugins as proc_plugs, makeSuccess
from gui.shared.money import Money, MONEY_UNDEFINED, Currency, ZERO_MONEY
from gui.shared.utils.requesters.recycle_bin_requester import VehicleRestoreInfo
from helpers import time_utils, dependency
from gui.shared.gui_items.gui_item_economics import ItemPrice, getVehicleBattleBoostersLayoutPrice, getVehicleConsumablesLayoutPrice, getVehicleOptionalDevicesLayoutPrice, getVehicleShellsLayoutPrice
from helpers.i18n import makeString
from skeletons.gui.game_control import IRestoreController, ITradeInController, IEpicBattleMetaGameController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from rent_common import parseRentID
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
_SEASON_RENT_DURATION_KEY = {(RentType.SEASON_RENT): b'season', 
   (RentType.SEASON_CYCLE_RENT): b'cycle'}

def getCrewAndShellsSumPrice(result, vehicle, crewType, buyShells):
    if crewType != -1:
        tankmenCount = len(vehicle.crew)
        itemsCache = dependency.instance(IItemsCache)
        tankmanCost = itemsCache.items.shop.getTankmanCostWithGoodyDiscount(vehicle.level)[crewType]
        result += Money(**tankmanCost) * tankmenCount
    if buyShells:
        for shell in vehicle.gun.defaultAmmo:
            result += shell.buyPrices.itemPrice.price * shell.count

    return result


def getCustomizationItemSellCountForVehicle(item, vehicleIntCD):
    installedCount = item.installedCount(vehicleIntCD)
    if not item.isProgressive:
        return installedCount
    inventoryCount = item.fullInventoryCount(vehicleIntCD)
    availableForSell = installedCount + inventoryCount - item.descriptor.progression.autoGrantCount
    return min(installedCount, availableForSell)


def showVehicleReceivedResultMessages(result):
    if result and result.userMsg:
        SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType, priority=result.msgPriority, messageData=result.msgData)
    if result is not None and result.auxData is not None:
        for m in result.auxData.get(b'additionalMessages', ()):
            if m.userMsg:
                SystemMessages.pushI18nMessage(m.userMsg, type=m.sysMsgType, priority=m.msgPriority, messageData=m.msgData)

    return


class VehicleReceiveProcessor(ItemProcessor):
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, vehicle, buyShell=False, crewType=-1):
        self.item = vehicle
        self.buyShell = buyShell
        self.buyCrew = crewType != -1
        self.crewType = crewType
        self.price = self._getPrice()
        super(VehicleReceiveProcessor, self).__init__(vehicle, self._getPluginsList())
        return

    def _getPluginsList(self):
        raise NotImplementedError
        return

    def _getPrice(self):
        raise NotImplementedError
        return

    def _getSysMsgType(self):
        raise NotImplementedError
        return

    def _getActualVehicle(self):
        return self.__itemsCache.items.getItemByCD(self.item.intCD)


class VehicleBuyer(VehicleReceiveProcessor):

    def __init__(self, vehicle, buySlot, buyShell=False, crewType=-1, showNotEnoughSlotMsg=True):
        self.buySlot = buySlot
        self.showNotEnoughSlotMsg = showNotEnoughSlotMsg
        super(VehicleBuyer, self).__init__(vehicle, buyShell=buyShell, crewType=crewType)
        return

    def _getPluginsList(self):
        return (
         proc_plugs.MoneyValidator(self.price),
         proc_plugs.VehicleSlotsConfirmator(self.showNotEnoughSlotMsg and not self.buySlot),
         proc_plugs.VehicleFreeLimitConfirmator(self.item, self.crewType),
         proc_plugs.CollectibleVehiclesValidator(self.item.intCD))

    def _getPrice(self):
        return getCrewAndShellsSumPrice(self.item.buyPrices.itemPrice.price, self.item, self.crewType, self.buyShell)

    @dependency.replace_none_kwargs(itemsCache=IItemsCache)
    def _errorHandler(self, code, errStr=b'', ctx=None, itemsCache=None):
        if not errStr:
            errStr = b'server_error' if code != AccountCommands.RES_CENTER_DISCONNECTED else b'server_error_centerDown'
        msg = (b'vehicle_buy/{}').format(errStr)
        slotsEnough = itemsCache.items.inventory.getFreeSlots(itemsCache.items.stats.vehicleSlots) > 0
        if not self.showNotEnoughSlotMsg and not slotsEnough:
            errStr = b'slot_error'
        return makeI18nError(sysMsgKey=msg, defaultSysMsgKey=b'vehicle_buy/server_error', auxData={b'errStr': errStr}, vehName=self.item.userName)

    def _successHandler(self, code, ctx=None):
        return makeI18nSuccess(sysMsgKey=b'vehicle_buy/success', vehName=self.item.userName, price=formatPrice(self.price, useStyle=True), type=self._getSysMsgType(), auxData={b'additionalMessages': [makeVehiclePostProgressionUnlockMsg(self._getActualVehicle())]})

    def _getSysMsgType(self):
        mainCurrency = self.item.buyPrices.itemPrice.getCurrency(byWeight=False)
        allCurrencies = self.price.getSetCurrencies(byWeight=True)
        if mainCurrency == Currency.CREDITS and Currency.GOLD in allCurrencies:
            return SM_TYPE.PurchaseForGoldAndCredits
        return CURRENCY_TO_SM_TYPE.get(mainCurrency, SM_TYPE.Information)

    def _request(self, callback):
        _logger.debug(b'Make request to buy vehicle: %s, %s, %s, %s', self.item, self.crewType, self.buyShell, self.price)
        BigWorld.player().shop.buyVehicle(self.item.nationID, self.item.innationID, self.buyShell, self.buyCrew, self.crewType, -1, (lambda code: self._response(code, callback)))
        return


class VehicleRenter(VehicleReceiveProcessor):

    def __init__(self, vehicle, rentID, buyShell=False, crewType=-1):
        self.rentPackageID = rentID
        self.rentPrice = self.__getRentPrice(rentID, vehicle)
        self.rentPackage = vehicle.getRentPackage(rentID)
        super(VehicleRenter, self).__init__(vehicle, buyShell, crewType)
        return

    def _getPluginsList(self):
        return (
         proc_plugs.MoneyValidator(self.price),
         proc_plugs.VehicleFreeLimitConfirmator(self.item, self.crewType))

    def _getPrice(self):
        return getCrewAndShellsSumPrice(self.rentPrice, self.item, self.crewType, self.buyShell)

    def _errorHandler(self, code, errStr=b'', ctx=None):
        if not errStr:
            msg = b'vehicle_rent/server_error' if code != AccountCommands.RES_CENTER_DISCONNECTED else b'vehicle_rent/server_error_centerDown'
        else:
            msg = (b'vehicle_rent/{}').format(errStr)
        return makeI18nError(sysMsgKey=msg, defaultSysMsgKey=b'vehicle_rent/server_error', vehName=self.item.userName)

    def _successHandler(self, code, ctx=None):
        rentType, packageID = parseRentID(self.rentPackageID)
        if rentType == RentType.TIME_RENT:
            rentPackageName = makeString(SYSTEM_MESSAGES.VEHICLE_RENT_TIMERENT, days=packageID)
        elif rentType in (RentType.SEASON_CYCLE_RENT, RentType.SEASON_RENT):
            seasonName = SEASON_NAME_BY_TYPE[self.rentPackage[b'seasonType']]
            durationKey = _SEASON_RENT_DURATION_KEY.get(rentType)
            rentPackageName = makeString((b'#system_messages:vehicle_rent/{}/{}').format(seasonName, durationKey))
        else:
            raise SoftException((b'Unknown rent type [{}]!').format(rentType))
        if not self.item.isDisabledForBuy and not self.item.isHidden:
            buyOption = makeString(SYSTEM_MESSAGES.VEHICLE_RENT_BUYOPTION)
        else:
            buyOption = b''
        return makeI18nSuccess(b'vehicle_rent/success', vehName=self.item.userName, rentPackageName=rentPackageName, price=formatPrice(self.price), type=self._getSysMsgType(), buyOption=buyOption)

    def _request(self, callback):
        _logger.debug(b'Make request to rent vehicle: %s, %s, %s, %s', self.item, self.crewType, self.buyShell, self.price)
        BigWorld.player().shop.buyVehicle(self.item.nationID, self.item.innationID, self.buyShell, self.buyCrew, self.crewType, self.rentPackageID, (lambda code: self._response(code, callback, ctx={b'rentID': (self.rentPackageID)})))
        return

    def _getSysMsgType(self):
        return CURRENCY_TO_SM_TYPE.get(self.rentPrice.getCurrency(byWeight=False), SM_TYPE.Information)

    def __getRentPrice(self, rentID, vehicle):
        for package in vehicle.rentPackages:
            if package[b'rentID'] == rentID:
                return package[b'rentPrice']

        return MONEY_UNDEFINED


class VehicleRestoreProcessor(VehicleBuyer):

    def _getPrice(self):
        return getCrewAndShellsSumPrice(self.item.restorePrice, self.item, self.crewType, self.buyShell)

    def _errorHandler(self, code, errStr=b'', ctx=None, itemsCache=None):
        if not errStr:
            msg = b'vehicle_restore/server_error' if code != AccountCommands.RES_CENTER_DISCONNECTED else b'vehicle_restore/server_error_centerDown'
        else:
            msg = (b'vehicle_restore/{}').format(errStr)
        return makeI18nError(sysMsgKey=msg, defaultSysMsgKey=b'vehicle_restore/server_error', vehName=self.item.userName)

    def _successHandler(self, code, ctx=None):
        return makeI18nSuccess(sysMsgKey=b'vehicle_restore/success', vehName=self.item.userName, price=formatPrice(self.price), type=self._getSysMsgType(), auxData={b'additionalMessages': [makeVehiclePostProgressionUnlockMsg(self._getActualVehicle())]})

    def _getSysMsgType(self):
        return SM_TYPE.Restore

    def _getPluginsList(self):
        return (
         proc_plugs.MoneyValidator(self.price),
         proc_plugs.VehicleSlotsConfirmator(not self.buySlot),
         proc_plugs.IsLongDisconnectedFromCenter())

    def _request(self, callback):
        _logger.debug(b'Make request to restore vehicle: %s, %s, %s, %s', self.item, self.crewType, self.buyShell, self.price)
        BigWorld.player().shop.buyVehicle(self.item.nationID, self.item.innationID, self.buyShell, self.buyCrew, self.crewType, -1, (lambda code: self._response(code, callback)))
        return


class VehicleTradeInProcessorBase(VehicleBuyer):

    def __init__(self, vehicleToBuy, vehicleToTradeOff, buySlot, buyShell=False, crewType=-1):
        self.itemToTradeOff = vehicleToTradeOff
        super(VehicleTradeInProcessorBase, self).__init__(vehicleToBuy, buySlot, buyShell=buyShell, crewType=crewType)
        return

    def _getPluginsList(self):
        nationGroupVehs = self.itemToTradeOff.getAllNationGroupVehs(self.itemsCache.items)
        barracksBerthsNeeded = getCrewCount(nationGroupVehs)
        return (
         proc_plugs.VehicleValidator(self.itemToTradeOff, setAll=True),
         proc_plugs.VehicleSellValidator(self.itemToTradeOff),
         proc_plugs.MoneyValidator(self.price),
         proc_plugs.BarracksSlotsValidator(barracksBerthsNeeded))

    def _successHandler(self, code, ctx=None):
        return makeI18nSuccess(sysMsgKey=b'vehicle_trade_in/success', vehName=self.item.userName, tradeOffVehName=self.itemToTradeOff.userName, price=formatPrice(self.price), type=self._getSysMsgType())

    def _getSysMsgType(self):
        return CURRENCY_TO_SM_TYPE.get(self.item.buyPrices.itemPrice.getCurrency(byWeight=False), SM_TYPE.Information)

    def _errorHandler(self, code, errStr=b'', ctx=None, itemsCache=None):
        if not errStr:
            msg = b'vehicle_trade_in/server_error' if code != AccountCommands.RES_CENTER_DISCONNECTED else b'vehicle_trade_in/server_error_centerDown'
        else:
            msg = (b'vehicle_trade_in/{}').format(errStr)
        return makeI18nError(sysMsgKey=msg, defaultSysMsgKey=b'vehicle_trade_in/server_error', vehName=self.item.userName, tradeOffVehName=self.itemToTradeOff.userName)

    def _request(self, callback):
        _logger.debug(b'Make request to trade-in vehicle: %s, %s, %s, %s, %s, %s', self.item, self.itemToTradeOff, self.buyShell, self.buyCrew, self.crewType, self.price)
        self._getBuyingFunc()(self.itemToTradeOff.invID, self.item.nationID, self.item.innationID, self.buyShell, self.buyCrew, self.crewType, (lambda code: self._response(code, callback)))
        return

    def _getBuyingFunc(self):
        raise NotImplementedError
        return


class VehicleTradeInProcessor(VehicleTradeInProcessorBase):
    __tradeIn = dependency.descriptor(ITradeInController)

    def _getPrice(self):
        price = self.__tradeIn.getTradeInPrice(self.item).price
        return getCrewAndShellsSumPrice(price, self.item, self.crewType, self.buyShell)

    def _getBuyingFunc(self):
        return BigWorld.player().shop.tradeInVehicle

    def _getPluginsList(self):
        return super(VehicleTradeInProcessor, self)._getPluginsList() + (
         proc_plugs.VehicleTradeInValidator(self.item, self.itemToTradeOff),)


class VehicleSlotBuyer(Processor):

    def __init__(self, showConfirm=True, showWarning=True):
        self.__hasDiscounts = bool(self.itemsCache.items.shop.personalSlotDiscounts)
        self.__frozenSlotPrice = None
        slotCost = self.__getSlotPrice()
        currency = slotCost.getCurrency()
        if self.__hasDiscounts and not slotCost:
            confirmationType = b'freeSlotConfirmation'
            ctx = {}
        else:
            confirmationType = b'buySlotConfirmation'
            img = RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2
            if currency == Currency.CREDITS:
                img = RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2
            style = getStyle(currency) if currency in Currency.ALL else text_styles.credits
            ctx = {b'goldCost': (text_styles.concatStylesWithSpace(style(backport.getIntegralFormat(abs(slotCost.get(currency)))), icons.makeImageTag(img)))}
        super(VehicleSlotBuyer, self).__init__((
         proc_plugs.MessageInformator((b'buySlotNotEnough/{}').format(currency), activeHandler=(lambda : not proc_plugs.MoneyValidator(slotCost).validate().success), isEnabled=showWarning),
         proc_plugs.MessageConfirmator(confirmationType, isEnabled=showConfirm, ctx=ctx),
         proc_plugs.MoneyValidator(slotCost)))
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return makeI18nError(sysMsgKey=(b'vehicle_slot_buy/{}').format(errStr), defaultSysMsgKey=b'vehicle_slot_buy/server_error')

    def _successHandler(self, code, ctx=None):
        price = self.__getSlotPrice()
        msgType = SM_TYPE.FinancialTransactionWithGold
        if price.getCurrency() == Currency.CREDITS:
            msgType = SM_TYPE.FinancialTransactionWithCredits
        return makeI18nSuccess(sysMsgKey=b'vehicle_slot_buy/success', money=formatPrice(price), type=msgType)

    def _request(self, callback):
        _logger.debug(b'Attempt to request server for buying vehicle slot')
        BigWorld.player().stats.buySlot((lambda code: self._response(code, callback)))
        return

    def __getSlotPrice(self):
        if self.__frozenSlotPrice is not None:
            return self.__frozenSlotPrice
        else:
            price = self.itemsCache.items.shop.getVehicleSlotsPrice(self.itemsCache.items.stats.vehicleSlots)
            if self.__hasDiscounts:
                self.__frozenSlotPrice = price
            return price


class VehicleSeller(ItemProcessor):
    __restore = dependency.descriptor(IRestoreController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __slots__ = (b'vehicle', b'nationGroupVehs', b'shells', b'eqs', b'optDevs', b'gainMoney', b'spendMoney', b'inventory', b'customizationItems', b'boosters', b'itemsForDemountKit', b'itemsFreeToDemount', b'isCrewDismiss', b'isDismantlingForMoney', b'isRemovedAfterRent', b'usedDemountKitsCount', b'__hasPairModification')

    def __init__(self, vehicle, shells=None, eqs=None, optDevs=None, inventory=None, customizationItems=None, boosters=None, isCrewDismiss=False, itemsForDemountKit=None, itemsForFreeDemount=None):
        shells = shells or []
        eqs = eqs or []
        boosters = boosters or []
        optDevs = optDevs or []
        inventory = inventory or []
        customizationItems = customizationItems or []
        itemsForDemountKit = itemsForDemountKit or []
        itemsForFreeDemount = itemsForFreeDemount or []
        nationGroupVehs = vehicle.getAllNationGroupVehs(self.itemsCache.items)
        self.vehicle = vehicle
        self.nationGroupVehs = nationGroupVehs
        self.shells = shells
        self.eqs = eqs
        self.optDevs = optDevs
        self.gainMoney, self.spendMoney = self.__getGainSpendMoney(vehicle, nationGroupVehs, shells, eqs, boosters, optDevs, inventory, customizationItems, itemsForDemountKit, itemsForFreeDemount)
        self.inventory = set(m.intCD for m in inventory)
        self.customizationItems = set(customizationItems)
        self.boosters = boosters
        self.itemsForDemountKit = itemsForDemountKit
        self.itemsFreeToDemount = itemsForFreeDemount
        barracksBerthsNeeded = getCrewCount(nationGroupVehs)
        bufferOverflowCtx = {}
        isBufferOverflowed = False
        self.__compensationAmount = ItemPrice(Money(), Money())
        if isCrewDismiss:
            tankmenGoingToBuffer, deletedTankmen = self.__restore.getTankmenDeletedBySelling(*nationGroupVehs)
            countOfDeleted = len(deletedTankmen)
            if countOfDeleted > 0:
                isBufferOverflowed = True
                bufferOverflowCtx[b'deleted'] = deletedTankmen[-1]
                bufferOverflowCtx[b'dismissed'] = tankmenGoingToBuffer[-1]
                if countOfDeleted > 1:
                    bufferOverflowCtx[b'multiple'] = True
                    bufferOverflowCtx[b'extraCount'] = countOfDeleted - 1
        plugins = [
         proc_plugs.VehicleValidator(vehicle, False, prop={b'isBroken': True, b'isLocked': True}),
         proc_plugs.VehicleSellValidator(vehicle),
         proc_plugs.MoneyValidator(self.spendMoney - self.gainMoney),
         proc_plugs.VehicleSellsLeftValidator(vehicle, not (vehicle.isRented and vehicle.rentalIsOver)),
         proc_plugs.BarracksSlotsValidator(barracksBerthsNeeded, isEnabled=not isCrewDismiss),
         proc_plugs.BufferOverflowConfirmator(bufferOverflowCtx, isEnabled=isBufferOverflowed),
         proc_plugs.BattleBoosterValidator(boosters),
         proc_plugs.DismountForDemountKitValidator(vehicle, itemsForDemountKit),
         proc_plugs.FreeToDemountValidator(itemsForFreeDemount),
         _getUniqueVehicleSellConfirmator(vehicle)]
        super(VehicleSeller, self).__init__(vehicle, plugins)
        self.isCrewDismiss = isCrewDismiss
        self.usedDemountKitsCount = len(itemsForDemountKit)
        self.isDismantlingForMoney = bool(self.spendMoney) or self.usedDemountKitsCount
        self.isRemovedAfterRent = vehicle.isRented
        self.__hasPairModification = any(step.action.getPurchasedID() is not None for step in vehicle.postProgression.iterUnorderedSteps() if step.action.isMultiAction())
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        localKey = b'vehicle_sell/{}'
        defaultKey = b'vehicle_sell/server_error'
        if self.isRemovedAfterRent:
            localKey = b'vehicle_remove/{}'
            defaultKey = b'vehicle_remove/server_error'
        return makeI18nError(sysMsgKey=localKey.format(errStr), defaultSysMsgKey=defaultKey, vehName=self.vehicle.userName)

    def _successHandler(self, code, ctx=None):
        restoreInfo = b''
        sellForGold = self.vehicle.getSellPrice(preferred=True).getCurrency(byWeight=True) == Currency.GOLD
        if self.vehicle.isPremium and not self.vehicle.isUnique and not self.vehicle.isUnrecoverable and self.__lobbyContext.getServerSettings().isVehicleRestoreEnabled() and not sellForGold:
            timeKey, formattedTime = getTimeLeftInfo(self.itemsCache.items.shop.vehiclesRestoreConfig.restoreDuration)
            if timeKey == b'inf':
                restoreInfo = backport.text(R.strings.system_messages.vehicle.restoreDuration.unlimited())
            else:
                restoreInfo = backport.text(R.strings.system_messages.vehicle.restoreDuration.dyn(timeKey, R.invalid)(), time=formattedTime)
        additionalMsgs = []
        if self.__hasPairModification:
            additionalMsgs.append(makeAllPairsDiscardMsg(self.vehicle.userName))
        g_tankActiveCamouflage[self.vehicle.intCD] = SeasonType.UNDEFINED
        msgCtx = {b'vehName': (self.vehicle.userName)}
        if self.usedDemountKitsCount:
            msgCtx[b'countDK'] = self.usedDemountKitsCount
        if self.isDismantlingForMoney:
            msgCtx[b'gainMoney'] = self.__formatPrice(self.gainMoney)
            msgCtx[b'spendMoney'] = self.__formatPrice(self.spendMoney, isReceived=False)
        else:
            msgCtx[b'money'] = self.__formatPrice(self.gainMoney)
        if not self.isRemovedAfterRent:
            msgCtx[b'restoreInfo'] = restoreInfo
        sysMsgR = R.strings.system_messages.dyn(b'vehicle_remove' if self.isRemovedAfterRent else b'vehicle_sell', R.invalid)
        if sysMsgR:
            sysMsgR = sysMsgR.dyn(b'success_dismantling' if self.isDismantlingForMoney else b'success', R.invalid)
        if self.isRemovedAfterRent:
            smType = SM_TYPE.Remove
        elif sellForGold:
            smType = SM_TYPE.SellingForGold
        else:
            smType = SM_TYPE.Selling
        return makeSuccess(userMsg=backport.text(sysMsgR(), **msgCtx), msgType=smType, auxData=additionalMsgs)

    def _request(self, callback):
        saleData = self.__splitDataByVehicle()
        _logger.debug(b'Make server request: %s, %s, %s, %s, %s, %s, %s, %s, %s', self.nationGroupVehs, bool(self.shells), bool(self.eqs), bool(self.boosters), bool(self.inventory), bool(self.optDevs), self.isDismantlingForMoney, self.isCrewDismiss, saleData)
        BigWorld.player().inventory.sellVehicle(saleData, (lambda code, errStr=b'': self._response(code, callback, errStr=errStr)))
        return

    def __getGainSpendMoney(self, currentVehicle, vehicles, vehShells, vehEqs, boosters, optDevicesToSell, inventory, customizationItems, itemsForDemountKit, itemsForFreeDemount):
        moneyGain = currentVehicle.sellPrices.itemPrice.price
        for shell in vehShells:
            moneyGain += shell.sellPrices.itemPrice.price * shell.count

        for module in vehEqs + optDevicesToSell + boosters:
            moneyGain += module.sellPrices.itemPrice.price

        for module in inventory:
            moneyGain += module.sellPrices.itemPrice.price * module.inventoryCount

        for module in customizationItems:
            getCount = getCustomizationItemSellCountForVehicle
            moneyGain += module.sellPrices.itemPrice.price * reduce((lambda acc, veh: acc + getCount(module, veh.intCD)), vehicles, 0)

        dismantlingToInventoryDevices = getDismantlingForMoneyToInventoryDevices(optDevicesToSell, (itemsForDemountKit + itemsForFreeDemount), *vehicles)
        moneySpend = calculateSpendMoney(self.itemsCache.items, dismantlingToInventoryDevices)
        return (moneyGain, moneySpend)

    def __accumulatePrice(self, result, price, count=1):
        result += price * count
        return result

    def __splitInventory(self):
        result = {}
        for vehicle in self.nationGroupVehs:
            vehInv = self.itemsCache.items.getItems(criteria=REQ_CRITERIA.VEHICLE.SUITABLE([
             vehicle], (GUI_ITEM_TYPE.SHELL,) + GUI_ITEM_TYPE.VEHICLE_MODULES) | REQ_CRITERIA.INVENTORY).values()
            result[vehicle.invID] = set(m.intCD for m in vehInv) & self.inventory

        full = reduce((lambda acc, inv: acc | inv), result.itervalues())
        unique = reduce((lambda acc, inv: acc ^ inv), result.itervalues())
        difference = full - unique
        for key in result.iterkeys():
            result[key] -= difference

        result[self.vehicle.invID].update(difference)
        return result

    def __splitDataByVehicle(self):
        result = []
        itemsFromInventory = self.__splitInventory()
        for vehicle in self.nationGroupVehs:
            itemsFromVehicle = set()
            seenCustItems = set()
            itemsForDemountKit = set()
            itemsFreeToDemount = set()
            customizationItems = []
            for shell in list(self.shells):
                if shell.isInSetup(vehicle) and shell.intCD not in itemsFromVehicle:
                    itemsFromVehicle.add(shell.intCD)
                    self.shells.remove(shell)

            for booster in self.boosters:
                if booster.isInSetup(vehicle) and booster.intCD not in itemsFromVehicle:
                    itemsFromVehicle.add(booster.intCD)
                    self.boosters.remove(booster)

            for eq in list(self.eqs):
                if eq.isInSetup(vehicle) and eq.intCD not in itemsFromVehicle:
                    itemsFromVehicle.add(eq.intCD)
                    self.eqs.remove(eq)

            for od in list(self.optDevs):
                if od.isInSetup(vehicle) and od.intCD not in itemsFromVehicle:
                    itemsFromVehicle.add(od.intCD)
                    self.optDevs.remove(od)

            for ci in list(self.customizationItems):
                installedCount = getCustomizationItemSellCountForVehicle(ci, vehicle.intCD)
                if installedCount > 0 and ci.intCD not in seenCustItems:
                    customizationItems.append(ci.intCD)
                    customizationItems.append(installedCount)
                    seenCustItems.add(ci.intCD)
                    self.customizationItems.remove(ci)

            for od in list(self.itemsForDemountKit):
                if od.isInSetup(vehicle) and od.intCD not in itemsForDemountKit and od.intCD not in itemsFromVehicle:
                    itemsForDemountKit.add(od.intCD)
                    self.itemsForDemountKit.remove(od)

            for od in list(self.itemsFreeToDemount):
                if od.isInSetup(vehicle) and od.intCD not in itemsFreeToDemount and od.intCD not in itemsFromVehicle:
                    itemsFreeToDemount.add(od.intCD)
                    self.itemsFreeToDemount.remove(od)

            result.append((vehicle.invID, self.isCrewDismiss, list(itemsFromVehicle),
             list(itemsFromInventory[vehicle.invID]), customizationItems, list(itemsForDemountKit),
             list(itemsFreeToDemount)))

        return result

    @staticmethod
    def getCurrencyString(currencyCode, isReceived=True):
        if currencyCode not in Currency.ALL:
            return backport.text(R.strings.messenger.platformCurrencyMsg.dyn(b'received' if isReceived else b'debited').dyn(currencyCode)())
        return backport.text(R.strings.messenger.serviceChannelMessages.currencyUpdate.dyn(b'received' if isReceived else b'debited').dyn(currencyCode)())

    def __formatPrice(self, price, isReceived=True):
        separator = b',\n'
        bullet = u'\u2022 '
        cSpace = b': '
        items = []
        if self.usedDemountKitsCount and not isReceived:
            items.append(backport.text(R.strings.system_messages.vehicle_sell.currencyUpdate.debited.demount_kit(), countDK=self.usedDemountKitsCount))
        currencies = [c for c in Currency.ALL if price.get(c) is not None]
        for c in currencies:
            value = price.get(c, 0)
            if value == 0:
                continue
            formatter = getBWFormatter(c)
            cFormatted = formatter(value)
            styler = getStyle(c)
            cFormatted = styler(cFormatted)
            cIdentifier = self.getCurrencyString(c, isReceived)
            items.append((b'').join((
             cIdentifier, cSpace, cFormatted)))

        if not items:
            return b''
        else:
            result = separator.join((b'{} {}').format(bullet, item) for item in items) if items else b''
            return result


def getDismantlingForMoneyToInventoryDevices(optDevicesToSell, itemsForDemountKit, *vehicles):
    result = []
    itemsForDk = [dev.intCD for dev in itemsForDemountKit]
    for dev in getDismantlingToInventoryDevices(optDevicesToSell, *vehicles):
        if dev.intCD in itemsForDk:
            itemsForDk.remove(dev.intCD)
        else:
            result.append(dev)

    return result


def getDismantlingToInventoryDevices(optDevicesToSell, *vehicles):
    result = []
    optDevicesToSell = [dev.intCD for dev in optDevicesToSell]
    for vehicle in vehicles:
        vehDevices = vehicle.optDevices.setupLayouts.getUniqueItems() if vehicle is not None else []
        for dev in vehDevices:
            if dev and not dev.isRemovable:
                if dev.intCD in optDevicesToSell:
                    optDevicesToSell.remove(dev.intCD)
                else:
                    result.append(dev)

    return result


def calculateSpendMoney(items, dismantlingToInventoryDevices):
    moneySpend = MONEY_UNDEFINED
    for dev in dismantlingToInventoryDevices:
        moneySpend += dev.getRemovalPrice(items).price

    return moneySpend


class VehicleSettingsProcessor(ItemProcessor):

    def __init__(self, vehicle, setting, value, plugins=None, source=CLIENT_COMMAND_SOURCES.UNDEFINED):
        self._setting = setting
        self._value = value
        self._source = source
        super(VehicleSettingsProcessor, self).__init__(vehicle, plugins or [])
        return

    def _request(self, callback):
        _logger.debug(b'Make server request for changing vehicle settings: %s, %s, %s', self.item, self._setting, bool(self._value))
        BigWorld.player().inventory.changeVehicleSetting(self.item.invID, self._setting, bool(self._value), self._source, (lambda code: self._response(code, callback)))
        return


class VehicleFavoriteProcessor(VehicleSettingsProcessor):

    def __init__(self, vehicle, value):
        super(VehicleFavoriteProcessor, self).__init__(vehicle, VEHICLE_SETTINGS_FLAG.GROUP_0, value)
        return


class VehicleAutoRepairProcessor(VehicleSettingsProcessor):

    def __init__(self, vehicle, value):
        super(VehicleAutoRepairProcessor, self).__init__(vehicle, VEHICLE_SETTINGS_FLAG.AUTO_REPAIR, value)
        return


class VehicleAutoLoadProcessor(VehicleSettingsProcessor):

    def __init__(self, vehicle, value):
        super(VehicleAutoLoadProcessor, self).__init__(vehicle, VEHICLE_SETTINGS_FLAG.AUTO_LOAD, value)
        return


class VehicleAutoEquipProcessor(VehicleSettingsProcessor):

    def __init__(self, vehicle, value):
        super(VehicleAutoEquipProcessor, self).__init__(vehicle, VEHICLE_SETTINGS_FLAG.AUTO_EQUIP, value)
        return


class VehicleAutoBattleBoosterEquipProcessor(VehicleSettingsProcessor):

    def __init__(self, vehicle, value, settings=VEHICLE_SETTINGS_FLAG.AUTO_EQUIP_BOOSTER | VEHICLE_SETTINGS_FLAG.AUTO_EQUIP_BOOSTER_SOFT):
        super(VehicleAutoBattleBoosterEquipProcessor, self).__init__(vehicle, settings, value)
        return


class VehicleAutoStyleEquipProcessor(VehicleSettingsProcessor):

    def __init__(self, vehicle, value, source):
        super(VehicleAutoStyleEquipProcessor, self).__init__(vehicle, VEHICLE_SETTINGS_FLAG.AUTO_RENT_CUSTOMIZATION, value, source=source)
        return


class VehicleRepairer(ItemProcessor):

    def __init__(self, vehicle):
        self._repairCost = Money(credits=vehicle.repairCost)
        super(VehicleRepairer, self).__init__(vehicle, (
         proc_plugs.MoneyValidator(self._repairCost),))
        return

    def _request(self, callback):
        BigWorld.player().inventory.repair(self.item.invID, (lambda code: self._response(code, callback)))
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        needed = Money(credits=self._repairCost.credits - self.itemsCache.items.stats.credits)
        return makeI18nError(sysMsgKey=(b'vehicle_repair/{}').format(errStr), defaultSysMsgKey=b'vehicle_repair/server_error', vehName=self.item.userName, needed=formatPrice(needed))

    def _successHandler(self, code, ctx=None):
        return makeI18nSuccess(sysMsgKey=b'vehicle_repair/success', vehName=self.item.userName, money=formatPrice(self._repairCost), type=SM_TYPE.Repair)


@adisp_async
@adisp_process
def tryToLoadDefaultShellsLayout(vehicle, callback=None):
    defaultLayout = []
    for shell in vehicle.shells.layout.getItems():
        if shell.count > shell.inventoryCount:
            SystemMessages.pushI18nMessage(b'#system_messages:charge/inventory_error', vehicle=vehicle.userName, type=SystemMessages.SM_TYPE.Warning)
            yield lambda callback: callback(None)
            break
        defaultLayout.extend(shell.defaultLayoutValue)
    else:
        result = yield BuyAndInstallShellsProcessor(vehicle).request()
        if result and result.auxData:
            for m in result.auxData:
                SystemMessages.pushI18nMessage(m.userMsg, type=m.sysMsgType)

        if result and result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
        if callback is not None:
            callback(True)
            return

    if callback is not None:
        callback(False)
    return


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext, itemsCache=IItemsCache)
def _getUniqueVehicleSellConfirmator(vehicle, lobbyContext=None, itemsCache=None):
    info = vehicle.restoreInfo
    if info is None and itemsCache and hasNationGroup(vehicle.intCD):
        mainVehTypeCD = getMainVehicleInNationGroup(getNationGroupID(vehicle.intCD))
        restoreData = itemsCache.items.recycleBin.vehiclesBuffer.get(mainVehTypeCD)
        if restoreData:
            restoreType, changedAt = restoreData
            restoreCfg = itemsCache.items.shop.vehiclesRestoreConfig
            info = VehicleRestoreInfo(restoreType, changedAt, restoreCfg.restoreDuration, restoreCfg.restoreCooldown)
    sellForGold = vehicle.getSellPrice(preferred=True).getCurrency(byWeight=True) == Currency.GOLD
    if lobbyContext is not None and lobbyContext.getServerSettings().isVehicleRestoreEnabled() and not sellForGold and not vehicle.isUnrecoverable:
        if info is not None and vehicle.isPurchased and info.isInCooldown():
            return proc_plugs.MessageConfirmator(b'vehicleSell/restoreCooldown', ctx={b'cooldown': (formatTime(info.getRestoreCooldownTimeLeft(), time_utils.ONE_DAY))}, isEnabled=vehicle.isUnique)
        if vehicle.isPurchased:
            return proc_plugs.MessageConfirmator(b'vehicleSell/restoreUnlimited', isEnabled=vehicle.isUnique)
    if vehicle.isCrewLocked:
        dialogI18n = b'vehicleSell/unique/crewLocked'
    else:
        dialogI18n = b'vehicleSell/unique'
    return proc_plugs.MessageConfirmator(dialogI18n, isEnabled=vehicle.isUnique)


class SetEnhancementProcessor(Processor):

    def __init__(self, slot, enhancementID, vehicle):
        super(SetEnhancementProcessor, self).__init__(plugins=[proc_plugs.VehicleValidator(vehicle)])
        self.vehicleInvID = vehicle.invID
        self.slot = slot
        self.enhancementID = enhancementID
        return

    def _request(self, callback):
        BigWorld.player().setEnhancement(self.vehicleInvID, self.slot, self.enhancementID, (lambda code, errStr: self._response(code, callback, errStr=errStr)))
        return


class DismountEnhancementProcessor(Processor):

    def __init__(self, slot, vehicle):
        super(DismountEnhancementProcessor, self).__init__(plugins=[proc_plugs.VehicleValidator(vehicle)])
        self.vehicleInvID = vehicle.invID
        self.slot = slot
        return

    def _request(self, callback):
        BigWorld.player().dismountEnhancement(self.vehicleInvID, self.slot, (lambda code, errStr, ext: self._response(code, callback, errStr=errStr, ctx=ext)))
        return


class OptDevicesInstaller(Processor):

    def __init__(self, vehicle):
        super(OptDevicesInstaller, self).__init__()
        self.__buyItems = [item for item in vehicle.optDevices.layout.getItems() if not item.isInInventory and not vehicle.optDevices.setupLayouts.isInSetup(item)]
        self.__price = getVehicleOptionalDevicesLayoutPrice(vehicle).price
        self._vehicle = vehicle
        self.__devices = vehicle.optDevices.layout.getIntCDs()
        self._setupPlugins()
        return

    def _setupPlugins(self):
        self.addPlugins((
         proc_plugs.VehicleValidator(self._vehicle),
         proc_plugs.MoneyValidator(self.__price, byCurrencyError=False),
         proc_plugs.OptionalDevicesInstallValidator(self._vehicle)))
        return

    def _request(self, callback):
        BigWorld.player().inventory.equipOptDevsSequence(self._vehicle.invID, self.__devices, (lambda code, errStr: self._response(code, callback, errStr)))
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return OptDevicesApplyProcessorMessage().makeErrorMsg(errStr)

    def _successHandler(self, code, ctx=None):
        buyMessages = [ItemBuyProcessorMessage(item, 1).makeSuccessMsg() for item in self.__buyItems]
        return makeSuccess(auxData=buyMessages)


class BuyAndInstallConsumablesProcessor(Processor):

    def __init__(self, vehicle):
        super(BuyAndInstallConsumablesProcessor, self).__init__()
        self._vehicle = vehicle
        self._setupPlugins()
        return

    def _setupPlugins(self):
        self.addPlugins((
         proc_plugs.VehicleValidator(self._vehicle),
         proc_plugs.MoneyValidator(getVehicleConsumablesLayoutPrice(self._vehicle).price, byCurrencyError=False),
         proc_plugs.ConsumablesInstallValidator(self._vehicle)))
        return

    def _request(self, callback):
        BigWorld.player().inventory.setAndFillLayouts(self._vehicle.invID, None, self.__getLayoutRaw(), EQUIPMENT_TYPES.regular, (lambda code, errStr, ext: self._response(code, callback, errStr=errStr, ctx=ext)))
        return

    def _successHandler(self, code, ctx=None):
        additionalMessages = []
        if ctx:
            additionalMessages = [ItemBuyProcessorMessage(self.itemsCache.items.getItemByCD(cd), count, Money.makeFromMoneyTuple(price)).makeSuccessMsg() for cd, price, count in ctx.get(b'eqs', [])]
        return makeSuccess(auxData=additionalMessages)

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return ConsumablesApplyProcessorMessage(self._vehicle).makeErrorMsg(errStr)

    def __getLayoutRaw(self):
        layout = [item.defaultLayoutValue if item is not None else (0, 0) for item in self._vehicle.consumables.layout]
        currentBoosters = [item.defaultLayoutValue if item is not None else (0, 0) for item in self._vehicle.battleBoosters.installed]
        layout.extend(currentBoosters)
        return [v for v in chain.from_iterable(layout)]


class BuyAndInstallShellsProcessor(Processor):

    def __init__(self, vehicle):
        super(BuyAndInstallShellsProcessor, self).__init__()
        self.__vehicle = vehicle
        self._setupPlugins()
        return

    def _setupPlugins(self):
        self.addPlugins((
         proc_plugs.VehicleValidator(self.__vehicle),
         proc_plugs.MoneyValidator(getVehicleShellsLayoutPrice(self.__vehicle).price, byCurrencyError=False),
         proc_plugs.ShellsInstallValidator(self.__vehicle)))
        return

    def _request(self, callback):
        BigWorld.player().inventory.setAndFillLayouts(self.__vehicle.invID, self.__getShellsRaw(), None, 0, (lambda code, errStr, ext: self._response(code, callback, errStr=errStr, ctx=ext)))
        return

    def _successHandler(self, code, ctx=None):
        additionalMessages = []
        totalPrice = ZERO_MONEY
        if ctx:
            for cd, price, count in ctx.get(b'shells', []):
                money = Money.makeFromMoneyTuple(price)
                additionalMessages.append(ItemBuyProcessorMessage(self.itemsCache.items.getItemByCD(cd), count, money).makeSuccessMsg())
                totalPrice += money

            if totalPrice:
                additionalMessages.append(ShellsApplyProcessorMessage(self.__vehicle, totalPrice).makeSuccessMsg())
        return makeSuccess(auxData=additionalMessages)

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return ShellsApplyProcessorMessage(self.__vehicle).makeErrorMsg(errStr)

    def __getShellsRaw(self):
        itemsIntAndCount = [item.defaultLayoutValue for item in self.__vehicle.shells.layout]
        return [v for v in chain.from_iterable(itemsIntAndCount)]


class BuyAndInstallBattleBoostersProcessor(Processor):

    def __init__(self, vehicle):
        super(BuyAndInstallBattleBoostersProcessor, self).__init__()
        self.__vehicle = vehicle
        self.__boosters = self.__vehicle.battleBoosters.layout.getItems()
        self._setupPlugins()
        return

    def _setupPlugins(self):
        self.addPlugins((
         proc_plugs.VehicleValidator(self.__vehicle),
         proc_plugs.MoneyValidator(getVehicleBattleBoostersLayoutPrice(self.__vehicle).price, byCurrencyError=False),
         proc_plugs.BattleBoostersInstallValidator(self.__vehicle)))
        return

    def _request(self, callback):
        BigWorld.player().inventory.setAndFillLayouts(self.__vehicle.invID, None, self.__getLayoutRaw(), EQUIPMENT_TYPES.battleBoosters, (lambda code, errStr, ext: self._response(code, callback, errStr=errStr, ctx=ext)))
        return

    def _successHandler(self, code, ctx=None):
        return makeSuccess(auxData=[ItemBuyProcessorMessage(i, 1).makeSuccessMsg() for i in self.__boosters if not i.isInInventory and not self.__vehicle.battleBoosters.setupLayouts.isInOtherLayout(i)])

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return BattleBoostersApplyProcessorMessage().makeErrorMsg(errStr)

    def __getLayoutRaw(self):
        desiredBoosters = [item.defaultLayoutValue if item is not None else (0, 0) for item in self.__vehicle.battleBoosters.layout]
        layout = [item.defaultLayoutValue if item is not None else (0, 0) for item in self.__vehicle.consumables.installed]
        layout.extend(desiredBoosters)
        return [v for v in chain.from_iterable(layout)]


class AutoFillVehicleLayoutProcessor(Processor):

    def __init__(self, vehicle):
        super(AutoFillVehicleLayoutProcessor, self).__init__()
        self.__vehicle = vehicle
        self._setupPlugins()
        return

    def _setupPlugins(self):
        price = self.__getPrice()
        self.addPlugins((
         proc_plugs.VehicleValidator(self.__vehicle),
         proc_plugs.MoneyValidator(price),
         proc_plugs.ShellsInstallValidator(self.__vehicle),
         proc_plugs.ConsumablesInstallValidator(self.__vehicle)))
        return

    def _request(self, callback):
        BigWorld.player().inventory.setAndFillLayouts(self.__vehicle.invID, self.__getShellsRaw(), self.__getConsumablesRaw(), EQUIPMENT_TYPES.regular, (lambda code, errStr, ext: self._response(code, callback, errStr=errStr, ctx=ext)))
        return

    def _successHandler(self, code, ctx=None):
        additionalMessages = []
        totalPrice = ZERO_MONEY
        if ctx:
            for cd, price, count in ctx.get(b'shells', []):
                money = Money.makeFromMoneyTuple(price)
                additionalMessages.append(ItemBuyProcessorMessage(self.itemsCache.items.getItemByCD(cd), count, money).makeSuccessMsg())
                totalPrice += money

            if totalPrice:
                additionalMessages.append(LayoutApplyProcessorMessage(self.__vehicle, totalPrice).makeSuccessMsg())
            additionalMessages.extend([ItemBuyProcessorMessage(self.itemsCache.items.getItemByCD(cd), count, Money.makeFromMoneyTuple(price)).makeSuccessMsg() for cd, price, count in ctx.get(b'eqs', [])])
        return makeSuccess(auxData=additionalMessages)

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return LayoutApplyProcessorMessage(self.__vehicle).makeErrorMsg(errStr)

    def __getShellsRaw(self):
        itemsIntAndCount = [item.defaultLayoutValue for item in self.__vehicle.shells.layout]
        return [v for v in chain.from_iterable(itemsIntAndCount)]

    def __getConsumablesRaw(self):
        itemsIntAndCount = [item.defaultLayoutValue if item is not None else (0, 0) for item in self.__vehicle.consumables.layout]
        return [v for v in chain.from_iterable(itemsIntAndCount)]

    def __getPrice(self):
        return getVehicleShellsLayoutPrice(self.__vehicle).price + getVehicleConsumablesLayoutPrice(self.__vehicle).price


class InstallBattleAbilitiesProcessor(Processor):
    __epicMetaGameCtrl = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self, vehicle, classVehs=False):
        super(InstallBattleAbilitiesProcessor, self).__init__()
        self.__vehicle = vehicle
        self.__classVehs = classVehs
        self._setupPlugins()
        return

    def _setupPlugins(self):
        self.addPlugins((
         proc_plugs.VehicleValidator(self.__vehicle),
         proc_plugs.BattleAbilitiesValidator(self.__vehicle)))
        return

    def _request(self, callback):
        self.__epicMetaGameCtrl.changeEquippedSkills(self.__getCurrentSkills(), self.__vehicle.intCD, (lambda code, _: self._response(code, callback)), self.__classVehs)
        return

    def _successHandler(self, code, ctx=None):
        return makeSuccess()

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return BattleAbilitiesApplyProcessorMessage().makeErrorMsg(errStr)

    def __getCurrentSkills(self):
        skillToAbilitiesIds = {skillID: skillInfo.eqID for skillID, skillInfo in self.__epicMetaGameCtrl.getAllUnlockedSkillInfoBySkillId().iteritems()}
        currentSkills = [
         -1] * self.__epicMetaGameCtrl.getNumAbilitySlots(self.__vehicle.descriptor.type)
        for slotIdx, item in enumerate(self.__vehicle.battleAbilities.layout):
            for skillID, battleAbilitiesID in skillToAbilitiesIds.iteritems():
                if item != EMPTY_ITEM and item.innationID == battleAbilitiesID:
                    currentSkills[slotIdx] = skillID

        return currentSkills
