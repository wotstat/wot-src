from math import ceil
from typing import Tuple, Any, Union, Dict
from goodies.GoodieResources import Gold, Credits
from items import ITEM_TYPES, vehicles, artefacts
from items.artefacts import OPT_DEV_TYPE_TAG
DEFAULT_ZERO_BERTH = 0

class PRICE_TYPE:
    DEFAULT = (0,)
    PROMO = (1,)
    PERSONAL = (2,)


removalCosts = {(OPT_DEV_TYPE_TAG.DELUXE): b'paidDeluxeRemovalCost', 
   (OPT_DEV_TYPE_TAG.TROPHY_BASIC): b'paidTrophyBasicRemovalCost', 
   (OPT_DEV_TYPE_TAG.TROPHY_UPGRADED): b'paidTrophyUpgradedRemovalCost', 
   (OPT_DEV_TYPE_TAG.MODERNIZED1): b'paidModernized1RemovalCost', 
   (OPT_DEV_TYPE_TAG.MODERNIZED2): b'paidModernized2RemovalCost', 
   (OPT_DEV_TYPE_TAG.MODERNIZED3): b'paidModernized3RemovalCost'}

def getItemPrice(item, gameParams, goodies=None, goodieTarget=None):
    priceType = PRICE_TYPE.DEFAULT
    actualPrice = gameParams[b'items'][b'itemPrices'][item]
    defaultPrice = gameParams[b'defaults'].get(b'items', {}).get(b'itemPrices', {}).get(item, None)
    if not defaultPrice:
        defaultPrice = actualPrice
    else:
        priceType = PRICE_TYPE.PROMO
    if (actualPrice[0] == 0 or actualPrice[1] == 0) and goodies and goodieTarget:
        personalDiscounts = goodies.test(goodieTarget, {Credits(defaultPrice[0]), Gold(defaultPrice[1])})
        for _, discount in personalDiscounts.iteritems():
            if isinstance(discount, Gold) and discount.value <= actualPrice[1]:
                actualPrice = (
                 0, discount.value)
                priceType = PRICE_TYPE.PERSONAL
            elif isinstance(discount, Credits) and discount.value <= actualPrice[0]:
                actualPrice = (
                 discount.value, 0)
                priceType = PRICE_TYPE.PERSONAL

    return (
     defaultPrice, actualPrice, priceType)


def getComponentSellPrice(gameParams, compDescr, defaultPrice=False):
    sellPriceFactor = gameParams[b'sellPriceFactor']
    itemTypeID = vehicles.parseIntCompactDescr(compDescr)[0]
    buyPrice = gameParams[b'items'][b'itemPrices'].getPrices(compDescr)
    if defaultPrice:
        itemPrices = gameParams[b'defaults'].get(b'items', {}).get(b'itemPrices', {})
        if itemPrices and compDescr in itemPrices:
            buyPrice = itemPrices.getPrices(compDescr)
    if itemTypeID in (ITEM_TYPES.shell, ITEM_TYPES.equipment):
        exchangeRate = gameParams[b'economics'][b'exchangeRateForShellsAndEqs']
    else:
        exchangeRate = gameParams[b'economics'][b'exchangeRate']
    price = buyPrice.get(b'credits', 0) + buyPrice.get(b'gold', 0) * exchangeRate
    crystalPrice = buyPrice.get(b'crystal', 0)
    if crystalPrice:
        crystalExchangeRate = gameParams[b'economics'][b'crystalExchangeRate']
        price += crystalExchangeRate * crystalPrice
    return {b'credits': (int(ceil(sellPriceFactor * price))), 
       b'equipCoin': (buyPrice.get(b'equipCoin', 0))}


def getOptionalDeviceRemovalCost(gameParams, optDevCompDescr):
    device = vehicles.getItemByCompactDescr(optDevCompDescr)
    if device.removable:
        return {}
    for tag in OPT_DEV_TYPE_TAG.ALL.intersection(device.tags):
        return gameParams[b'economics'][removalCosts[tag]]

    return gameParams[b'economics'][b'paidRemovalCost']


def getNextSlotPrice(slots, slotsPrices):
    addSlotNumber = slots - slotsPrices[0]
    if addSlotNumber < 0:
        if len(slotsPrices[1]):
            return (slotsPrices[1][0][0], 0)
        return (b'credits', 0)
    if addSlotNumber < len(slotsPrices[1]):
        return slotsPrices[1][addSlotNumber]
    return slotsPrices[1][-1]


def getBerthPackCount(berthsInPack, selectedCount):
    return int(round(float(selectedCount) / berthsInPack))


def getNextBerthPackPrice(currentBerthsCount, berthsPrices, selectedCount=None):
    initialBerths, berthsInPack, packsCost = berthsPrices
    costCurrency, costValues = packsCost
    costValue = costValues[-1]
    selectedCount = selectedCount if selectedCount is not None else berthsInPack
    countPacks = getBerthPackCount(berthsInPack, selectedCount)
    countFreePacks = max((initialBerths - currentBerthsCount) / berthsInPack, DEFAULT_ZERO_BERTH)
    return (costCurrency, max((countPacks - countFreePacks) * costValue, DEFAULT_ZERO_BERTH))
