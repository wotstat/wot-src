from items.item_price import getComponentSellPrice, getOptionalDeviceRemovalCost

class RESTORE_VEHICLE_TYPE:
    PREMIUM = 0
    ACTION = 1


class RESTORE_OPT_DEV_REASON:
    SELL_FROM_VEHICLE = 0
    SELL_FROM_DEPOT = 1
    DESTROYED = 2
    ALL = (
     SELL_FROM_VEHICLE, SELL_FROM_DEPOT, DESTROYED)


def getVehicleRestorePrice(defaultBuyPrice, exchangeRate, sellPriceFactor, sellToRestoreFactor):
    credits = defaultBuyPrice[0] + defaultBuyPrice[1] * exchangeRate
    return (int(credits * sellPriceFactor * sellToRestoreFactor), 0)


def getVehicleRestorePriceShort(vehTypeCompDescr, gameParams):
    if b'defaults' in gameParams and b'items' in gameParams[b'defaults'] and b'itemPrices' in gameParams[b'defaults'][b'items'] and vehTypeCompDescr in gameParams[b'defaults'][b'items'][b'itemPrices']:
        defaultBuyPrice = gameParams[b'defaults'][b'items'][b'itemPrices'][vehTypeCompDescr]
    else:
        defaultBuyPrice = gameParams[b'items'][b'itemPrices'][vehTypeCompDescr]
    exchangeRate = gameParams[b'economics'][b'exchangeRate']
    sellPriceFactor = gameParams[b'sellPriceFactor']
    sellToRestore = gameParams[b'restore_config'][b'vehicles'][b'sellToRestoreFactor']
    return getVehicleRestorePrice(defaultBuyPrice, exchangeRate, sellPriceFactor, sellToRestore)


def getOptionalDeviceRestorePriceShort(optionalDeviceCD, reason, count, isModernized, gameParams):
    itemPrice = gameParams[b'items'][b'itemPrices'].getPrices(optionalDeviceCD)
    itemPrices = gameParams[b'defaults'].get(b'items', {}).get(b'itemPrices', {})
    if itemPrices and optionalDeviceCD in itemPrices:
        itemPrice = itemPrices.getPrices(optionalDeviceCD)
    sellPrice = getComponentSellPrice(gameParams, optionalDeviceCD, defaultPrice=True)
    removalCost = getOptionalDeviceRemovalCost(gameParams, optionalDeviceCD)
    restoreCost = gameParams[b'economics'][b'paidRemovalCost']
    return getOptionalDeviceRestorePrice(reason, count, isModernized, itemPrice, sellPrice, removalCost, restoreCost)


def getOptionalDeviceRestorePrice(reason, count, isModernized, itemPrice, sellPrice, removalCost, restoreCost):

    def updatePrice(currentPrice, priceToUpdate):
        for currency, amount in priceToUpdate.iteritems():
            currentPrice[currency] += amount

        return

    restorePrice = {b'credits': 0, b'gold': 0, 
       b'equipCoin': 0, 
       b'crystal': 0}
    if reason == RESTORE_OPT_DEV_REASON.SELL_FROM_DEPOT:
        updatePrice(restorePrice, sellPrice)
        updatePrice(restorePrice, restoreCost)
    elif reason == RESTORE_OPT_DEV_REASON.DESTROYED:
        if isModernized:
            updatePrice(restorePrice, itemPrice)
        updatePrice(restorePrice, removalCost)
    elif reason == RESTORE_OPT_DEV_REASON.SELL_FROM_VEHICLE:
        updatePrice(restorePrice, sellPrice)
        updatePrice(restorePrice, removalCost)
    restorePrice = {currency: amount * count for currency, amount in restorePrice.iteritems()}
    return restorePrice
