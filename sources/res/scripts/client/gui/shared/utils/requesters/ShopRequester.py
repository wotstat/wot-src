from __future__ import absolute_import
import logging, weakref
from builtins import map, range
from collections import namedtuple
from future.utils import iteritems, viewitems, viewvalues
import typing, BigWorld
from constants import WIN_XP_FACTOR_MODE, ARENA_BONUS_TYPE
from goodies.goodie_constants import GOODIE_VARIETY, GOODIE_TARGET_TYPE, GOODIE_RESOURCE_TYPE
from goodies.goodie_helpers import getPremiumCost, getPriceWithDiscount, GoodieData
from gui.shared.gui_items.gui_item_economics import ItemPrice
from gui.shared.money import Money, MONEY_UNDEFINED, Currency
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from items import ItemsPrices
from items.item_price import getNextSlotPrice, getNextBerthPackPrice
from post_progression_common import CUSTOM_ROLE_SLOT_CHANGE_PRICE
from post_progression_prices_common import getPostProgressionPrice
from skeletons.gui.shared.utils.requesters import IShopCommonStats, IShopRequester
if typing.TYPE_CHECKING:
    from typing import Tuple, Dict, Any
_logger = logging.getLogger(__name__)
_DEFAULT_EXCHANGE_RATE = 400
_DEFAULT_CRYSTAL_EXCHANGE_RATE = 200
_DEFAULT_SELL_PRICE_MODIF = 0.5
_DEFAULT_CLAN_CREATION_COST = 2500
_PREMIUM_CREW_IDX = 2
_VehiclesRestoreConfig = namedtuple(b'_VehiclesRestoreConfig', b'restoreDuration restoreCooldown restorePriceModif')
_TankmenRestoreConfig = namedtuple(b'_TankmenRestoreConfig', b'freeDuration billableDuration cost limit')
_TargetData = namedtuple(b'_TargetData', b'targetType, targetValue, limit')
_ResourceData = namedtuple(b'_ResourceData', b'resourceType, value, isPercentage')
_ConditionData = namedtuple(b'_ConditionData', b'conditionType, value')
_DEFAULT_SLOT_PRICE = (
 0, ([Currency.CREDITS, 300],))

class _NamedGoodieData(GoodieData):

    @staticmethod
    def __new__(cls, variety, target, enabled, lifetime, useby, counter, autostart, condition, resource, expireAfter, roundToEndOfGameDay):
        return GoodieData.__new__(cls, variety, _TargetData(*target) if target else None, enabled, lifetime, useby, counter, autostart, _ConditionData(*condition) if condition else None, _ResourceData(*resource) if resource else None, expireAfter if expireAfter else None, roundToEndOfGameDay if roundToEndOfGameDay else True)

    def getTargetValue(self):
        if self.target.targetType == GOODIE_TARGET_TYPE.ON_BUY_PREMIUM:
            return int(self.target.targetValue.split(b'_')[1])
        return self.target.targetValue


class ShopCommonStats(IShopCommonStats):

    def getValue(self, key, defaultValue=None):
        raise NotImplementedError
        return

    def getPrices(self):
        try:
            return self.getItemsData()[b'itemPrices']
        except KeyError:
            return ItemsPrices()

        return

    def getBoosterPrices(self):
        try:
            return self.getGoodiesData()[b'prices']
        except KeyError:
            return {}

        return

    def getHiddens(self):
        try:
            return self.getItemsData()[b'notInShopItems']
        except KeyError:
            return set()

        return

    def getHiddenBoosters(self):
        try:
            return self.getGoodiesData()[b'notInShop']
        except KeyError:
            return set()

        return

    def getNotToBuyVehicles(self):
        try:
            return self.getItemsData()[b'vehiclesNotToBuy']
        except KeyError:
            return set()

        return

    def getVehicleRentPrices(self):
        try:
            return self.getItemsData()[b'vehiclesRentPrices']
        except KeyError:
            return {}

        return

    def getVehiclesForGold(self):
        try:
            return self.getItemsData()[b'vehiclesToSellForGold']
        except KeyError:
            return set()

        return

    def getVehiclesSellPriceFactors(self):
        try:
            return self.getItemsData()[b'vehicleSellPriceFactors']
        except KeyError:
            return {}

        return

    def getItemPrice(self, intCD):
        prices = self.getPrices()
        if intCD in prices:
            return Money(**prices.getPrices(intCD))
        return MONEY_UNDEFINED

    def getBoosterPricesTuple(self, boosterID):
        return self.getBoosterPrices().get(boosterID, tuple())

    def getOperationPrices(self):
        try:
            return self.getItemsData()[b'operationPrices']
        except KeyError:
            return {}

        return

    def getItem(self, intCD):
        return (
         self.getItemPrice(intCD), intCD in self.getHiddens())

    def getAchievementReward(self, achievement, arenaType=ARENA_BONUS_TYPE.REGULAR):
        return

    @property
    def revision(self):
        return self.getValue(b'rev', 0)

    @property
    def paidRemovalCost(self):
        cost = self.getValue(b'paidRemovalCost', {})
        return cost.get(Currency.GOLD, 10)

    @property
    def paidDeluxeRemovalCost(self):
        cost = self.getValue(b'paidDeluxeRemovalCost', {(Currency.CRYSTAL): 100})
        return Money(**cost)

    @property
    def paidTrophyBasicRemovalCost(self):
        cost = self.getValue(b'paidTrophyBasicRemovalCost', {(Currency.GOLD): 10})
        return Money(**cost)

    @property
    def paidTrophyUpgradedRemovalCost(self):
        cost = self.getValue(b'paidTrophyUpgradedRemovalCost', {(Currency.GOLD): 10})
        return Money(**cost)

    def getPaidModernizedRemovalCost(self, level):
        cost = self.getValue(self._getModernizedKey(level), {(Currency.EQUIP_COIN): 10})
        return Money(**cost)

    @property
    def exchangeRate(self):
        return self.getValue(b'exchangeRate', _DEFAULT_EXCHANGE_RATE)

    @property
    def clanCreationCost(self):
        return self.getValue(b'clanCreationCost', _DEFAULT_CLAN_CREATION_COST)

    @property
    def crystalExchangeRate(self):
        return self.getValue(b'crystalExchangeRate', _DEFAULT_CRYSTAL_EXCHANGE_RATE)

    @property
    def exchangeRateForShellsAndEqs(self):
        return self.getValue(b'exchangeRateForShellsAndEqs', _DEFAULT_EXCHANGE_RATE)

    @property
    def sellPriceModif(self):
        return self.getValue(b'sellPriceModif', _DEFAULT_SELL_PRICE_MODIF)

    @property
    def vehiclesRestoreConfig(self):
        config = self.__getRestoreConfig().get(b'vehicles', {})
        return _VehiclesRestoreConfig(config.get(b'premiumDuration', 0), config.get(b'actionCooldown', 0), config.get(b'sellToRestoreFactor', 1.1))

    @property
    def tankmenRestoreConfig(self):
        config = self.__getRestoreConfig().get(b'tankmen', {})
        return _TankmenRestoreConfig(config.get(b'freeDuration', 0), config.get(b'creditsDuration', 0), Money(credits=config.get(b'creditsCost', 0)), config.get(b'limit', 100))

    def sellPriceModifiers(self, compDescr):
        sellPriceModif = self.sellPriceModif
        sellPriceFactors = self.getVehiclesSellPriceFactors()
        if compDescr in sellPriceFactors:
            modifiers = sellPriceFactors[compDescr]
        else:
            modifiers = sellPriceModif
        rate = self.defaults.exchangeRate if hasattr(self, b'defaults') else self.exchangeRate
        return (
         self.revision,
         rate,
         self.exchangeRateForShellsAndEqs,
         sellPriceModif,
         modifiers,
         compDescr in self.getVehiclesForGold())

    @property
    def slotsPrices(self):
        return self.getValue(b'slotsPrices', _DEFAULT_SLOT_PRICE)

    def getVehicleSlotsPrice(self, currentSlotsCount):
        price = getNextSlotPrice(currentSlotsCount, self.slotsPrices)
        return Money.makeFrom(price[0], price[1])

    @property
    def dropSkillsCost(self):
        return self.getValue(b'dropSkillsCost', {})

    @property
    def dailyXPFactor(self):
        return self.getValue(b'dailyXPFactor', 2)

    @property
    def winXPFactorMode(self):
        return self.getValue(b'winXPFactorMode', WIN_XP_FACTOR_MODE.DAILY)

    @property
    def berthsPrices(self):
        return self.getValue(b'berthsPrices', (0, 1, [300]))

    def getBattlePassCost(self):
        return Money(**self.getValue(b'battlePassCost', defaultValue={(Currency.GOLD): 6500}))

    def getBattlePassLevelCost(self):
        return Money(**self.getValue(b'battlePassLevelCost', defaultValue={(Currency.GOLD): 250}))

    def getTankmanBerthPrice(self, berthsCount):
        prices = self.berthsPrices
        goldCost = getNextBerthPackPrice(berthsCount, prices)
        return (Money(gold=goldCost), prices[1])

    @property
    def isEnabledBuyingGoldShellsForCredits(self):
        return self.getValue(b'isEnabledBuyingGoldShellsForCredits', False)

    @property
    def isEnabledBuyingGoldEqsForCredits(self):
        return self.getValue(b'isEnabledBuyingGoldEqsForCredits', False)

    @property
    def tankmanCost(self):
        return self.getValue(b'tankmanCost', tuple())

    @property
    def changeRoleCost(self):
        return self.getValue(b'changeRoleCost', 600)

    @property
    def tankman(self):
        return self.getValue(b'tankman', {})

    @property
    def freeXPConversion(self):
        return self.getValue(b'freeXPConversion', (25, 1))

    @property
    def freeXPToTManXPRate(self):
        return self.getValue(b'freeXPToTManXPRate', 10)

    def getItemsData(self):
        return self.getValue(b'items', {})

    def getGoodiesData(self):
        return self.getValue(b'goodies', {})

    def getVehCamouflagePriceFactor(self, typeCompDescr):
        return self.getItemsData().get(b'vehicleCamouflagePriceFactors', {}).get(typeCompDescr)

    def getEmblemsGroupPriceFactors(self):
        return self.getItemsData().get(b'playerEmblemGroupPriceFactors', {})

    def getEmblemsGroupHiddens(self):
        return self.getItemsData().get(b'notInShopPlayerEmblemGroups', set())

    def getInscriptionsGroupPriceFactors(self, nationID):
        return self.getItemsData().get(b'inscriptionGroupPriceFactors', [])[nationID]

    def getInscriptionsGroupHiddens(self, nationID):
        return self.getItemsData().get(b'notInShopInscriptionGroups', [])[nationID]

    def getCamouflagesPriceFactors(self, nationID):
        return self.getItemsData().get(b'camouflagePriceFactors', [])[nationID]

    def getCamouflagesHiddens(self, nationID):
        return self.getItemsData().get(b'notInShopCamouflages', [])[nationID]

    def getNotInShopProgressionLvlItems(self):
        return self.getItemsData().get(b'notInShopProgressionLvlItems', {})

    @property
    def premiumCost(self):
        return self.getValue(b'premiumCost', {})

    @property
    def goodies(self):
        return self.getGoodiesData().get(b'goodies', {})

    def getGoodieByID(self, discountID):
        return self.goodies.get(discountID, None)

    def getGoodiesByVariety(self, variety):
        return {goodieID: item for goodieID, item in iteritems(self.goodies) if item.variety == variety}

    @property
    def boosters(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.BOOSTER)

    @property
    def discounts(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.DISCOUNT)

    @property
    def demountKits(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.DEMOUNT_KIT)

    @property
    def recertificationForms(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.RECERTIFICATION_FORM)

    @property
    def mentoringLicenses(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.MENTORING_LICENSE)

    def getPremiumPacketCost(self, days):
        return self.premiumCost.get(days)

    @property
    def camouflageCost(self):
        return self.getValue(b'camouflageCost', {})

    def getCamouflageCost(self, days=0):
        return self.camouflageCost.get(days)

    @property
    def playerInscriptionCost(self):
        return self.getValue(b'playerInscriptionCost', {})

    def getInscriptionCost(self, days=0):
        return self.playerInscriptionCost.get(days)

    @property
    def playerEmblemCost(self):
        return self.getValue(b'playerEmblemCost', {})

    def getEmblemCost(self, days=0):
        return self.playerEmblemCost.get(days)

    def _getModernizedKey(self, level):
        return (b'').join((b'paidModernized', str(level), b'RemovalCost'))

    def __getRestoreConfig(self):
        return self.getValue(b'restore_config', {})


class ShopRequester(AbstractSyncDataRequester, ShopCommonStats, IShopRequester):

    def __init__(self, goodies):
        super(ShopRequester, self).__init__()
        self.defaults = DefaultShopRequester({}, self)
        self._goodies = weakref.proxy(goodies)
        return

    def clear(self):
        self.defaults.clear()
        super(ShopRequester, self).clear()
        return

    def getValue(self, key, defaultValue=None):
        return self.getCacheValue(key, defaultValue)

    def _response(self, resID, invData, callback=None):
        if invData is not None:
            self.defaults.update(invData.get(b'defaults'))
        super(ShopRequester, self)._response(resID, invData, callback)
        return

    def _requestCache(self, callback=None):
        BigWorld.player().shop.getCache((lambda resID, value, rev: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        data = dict(data)
        if b'goodies' in data:
            goodies = data[b'goodies'].get(b'goodies', {})
            formattedGoodies = {}
            for goodieID, goodieData in viewitems(goodies):
                formattedGoodies[goodieID] = _NamedGoodieData(*goodieData)

            data[b'goodies'][b'goodies'] = formattedGoodies
        return data

    def getPremiumCostWithDiscount(self, premiumPacketDiscounts=None):
        discounts = premiumPacketDiscounts or self.personalPremiumPacketsDiscounts
        premiumCostWithDiscount = self.premiumCost.copy()
        for discount in viewvalues(discounts):
            premiumCostWithDiscount[discount.getTargetValue()] = getPremiumCost(self.premiumCost, discount)

        return premiumCostWithDiscount

    def isActionOnPremium(self):
        premiumCost = self.premiumCost
        defaultPremiumCost = self.defaults.premiumCost
        for days, price in viewitems(premiumCost):
            if defaultPremiumCost[days] != price:
                return True

        return False

    def getPetCostWithDiscount(self, petPrice):
        petGoodies = self.personalPetDiscounts
        if petGoodies:
            bestGoody = self.bestGoody(petGoodies)
            currency = petPrice.getCurrency()
            return Money.makeFrom(currency, getPriceWithDiscount(petPrice.get(petPrice.getCurrency(), 0), bestGoody.resource))
        return petPrice

    def getVehicleSlotsPrice(self, currentSlotsCount):
        price = super(ShopRequester, self).getVehicleSlotsPrice(currentSlotsCount)
        slotGoodies = self.personalSlotDiscounts
        if slotGoodies:
            bestGoody = self.bestGoody(slotGoodies)
            currency = price.getCurrency()
            return Money.makeFrom(currency, getPriceWithDiscount(price.get(price.getCurrency(), 0), bestGoody.resource))
        return price

    def getVehicleSlotsItemPrice(self, currentSlotsCount):
        defPrice = self.defaults.getVehicleSlotsPrice(currentSlotsCount)
        price = self.getVehicleSlotsPrice(currentSlotsCount)
        currency = price.getCurrency()
        slotGoodies = self.personalSlotDiscounts
        if slotGoodies:
            bestGoody = self.bestGoody(slotGoodies)
            price = Money.makeFrom(currency, getPriceWithDiscount(price.get(currency, 0), bestGoody.resource))
        return ItemPrice(price=price, defPrice=defPrice)

    def getTankmanCostItemPrices(self, vehLevel):
        result = []
        defaultCost = self.defaults.tankmanCost
        countItems = len(defaultCost)
        tankmanCostWithGoodyDiscount = self.getTankmanCostWithGoodyDiscount(vehLevel)
        if countItems == len(tankmanCostWithGoodyDiscount):
            for idx in range(countItems):
                commanderLevelsPrices = {}
                commanderLevelsDefPrices = {}
                for currency in Currency.ALL:
                    defPriceCurrency = defaultCost[idx].get(currency, None)
                    if defPriceCurrency:
                        if idx == _PREMIUM_CREW_IDX and BigWorld.player().freePremiumCrew.get(vehLevel):
                            commanderLevelsPrices[currency] = 0
                        else:
                            commanderLevelsPrices[currency] = tankmanCostWithGoodyDiscount[idx].get(currency, None)
                        commanderLevelsDefPrices[currency] = defPriceCurrency

                price = Money(**commanderLevelsPrices)
                defPrice = Money(**commanderLevelsDefPrices)
                itemPrice = ItemPrice(price=price, defPrice=defPrice)
                result.append(itemPrice)

        else:
            _logger.error(b'len(self.tankmanCost) must be equal to len(self.getTankmanCostWithGoodyDiscount(vehLevel))')
        return result

    def getTankmanCostWithGoodyDiscount(self, vehLevel):
        prices = self.tankmanCost[:]
        tankmanGoodies = self.personalTankmanDiscounts
        if BigWorld.player().freePremiumCrew.get(vehLevel):
            premiumPrice = prices[_PREMIUM_CREW_IDX].copy()
            prices = prices[:_PREMIUM_CREW_IDX] + (premiumPrice,)
            premiumPrice[Currency.GOLD] = 0
        if tankmanGoodies:
            bestGoody = self.bestGoody(tankmanGoodies)
            return self.__applyGoodyToStudyCost(prices, bestGoody)
        return prices

    @property
    def personalPremiumPacketsDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_PREMIUM)

    @property
    def personalSlotDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_SLOT)

    @property
    def personalPetDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_PET)

    @property
    def personalTankmanDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_GOLD_TANKMEN)

    @property
    def personalVehicleDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_VEHICLE)

    def getVehicleDiscountDescriptions(self):
        return self.__getDiscountsDescriptionsByTarget(GOODIE_TARGET_TYPE.ON_BUY_VEHICLE)

    def getPersonalVehicleDiscountPrice(self, typeCompDescr):
        defaultPrice = self.defaults.getItemPrice(typeCompDescr)
        currency = defaultPrice.getCurrency()
        personalVehicleDiscountPrice = None
        for discount in viewvalues(self.personalVehicleDiscounts):
            if discount.getTargetValue() == typeCompDescr:
                discountPrice = self.__getPriceWithDiscount(defaultPrice, discount.resource)
                if discountPrice.isDefined() and (personalVehicleDiscountPrice is None or discountPrice.get(currency) < personalVehicleDiscountPrice.get(currency)):
                    personalVehicleDiscountPrice = discountPrice

        return personalVehicleDiscountPrice

    def bestGoody(self, goodies):
        if goodies:
            return sorted(viewvalues(goodies), key=(lambda goody: goody.resource[1]))[-1]
        else:
            return

    def customRoleSlotChangeCost(self, vehType, isRaw=False):
        cost = getPostProgressionPrice(CUSTOM_ROLE_SLOT_CHANGE_PRICE, vehType, self._data)
        if isRaw:
            return cost
        return Money(**cost)

    def __getDiscountsDescriptionsByTarget(self, targetType):
        return {discountID: item for discountID, item in viewitems(self.discounts) if item.target.targetType == targetType and item.enabled}

    def __applyGoodyToStudyCost(self, prices, goody):

        def convert(price):
            newPrice = price.copy()
            if price[b'isPremium']:
                newPrice[Currency.GOLD] = getPriceWithDiscount(price[Currency.GOLD], goody.resource)
            return newPrice

        return tuple(map(convert, prices))

    def __personalDiscountsByTarget(self, targetType):
        discounts = self.__getDiscountsDescriptionsByTarget(targetType)
        return {discountID: item for discountID, item in viewitems(discounts) if discountID in self._goodies.goodies}

    @staticmethod
    def __getPriceWithDiscount(price, resourceData):
        resourceType, _, _ = resourceData
        if resourceType == GOODIE_RESOURCE_TYPE.CREDITS:
            return Money(credits=getPriceWithDiscount(price.credits, resourceData))
        if resourceType == GOODIE_RESOURCE_TYPE.GOLD:
            return Money(gold=getPriceWithDiscount(price.gold, resourceData))
        return MONEY_UNDEFINED


class DefaultShopRequester(ShopCommonStats):

    def __init__(self, cache, proxy):
        super(DefaultShopRequester, self).__init__()
        self.__cache = cache.copy()
        self.__proxy = weakref.proxy(proxy)
        return

    def clear(self):
        _logger.debug(b'Clearing shop defaults.')
        self.__cache.clear()
        return

    def update(self, cache):
        if cache is None:
            cache = {}
        self.clear()
        self.__cache = cache.copy()
        return

    def getValue(self, key, defaultValue=None):
        if key in self.__cache:
            return self.__cache[key]
        return defaultValue

    @property
    def revision(self):
        return self.__proxy.revision

    def getPrices(self):
        return self.getItemsData().get(b'itemPrices', self.__proxy.getPrices())

    def getBoosterPrices(self):
        return self.getGoodiesData().get(b'prices', self.__proxy.getBoosterPrices())

    def getHiddens(self):
        return self.getItemsData().get(b'notInShopItems', self.__proxy.getHiddens())

    def getHiddenBoosters(self):
        return self.getGoodiesData().get(b'notInShop', self.__proxy.getHiddenBoosters())

    def getNotToBuyVehicles(self):
        return self.getItemsData().get(b'vehiclesNotToBuy', self.__proxy.getNotToBuyVehicles())

    def getVehicleRentPrices(self):
        return self.getItemsData().get(b'vehiclesRentPrices', self.__proxy.getVehicleRentPrices())

    def getVehiclesForGold(self):
        return self.getItemsData().get(b'vehiclesToSellForGold', {})

    def getVehiclesSellPriceFactors(self):
        return self.getItemsData().get(b'vehicleSellPriceFactors', {})

    def getItemPrice(self, intCD):
        prices = self.getPrices()
        if intCD in prices:
            return Money(**prices.getPrices(intCD))
        return self.__proxy.getItemPrice(intCD)

    def getBoosterPricesTuple(self, boosterID):
        return self.getBoosterPrices().get(boosterID, self.__proxy.getBoosterPricesTuple(boosterID))

    def getOperationPrices(self):
        return self.getItemsData().get(b'operationPrices', self.__proxy.getOperationPrices())

    @property
    def paidRemovalCost(self):
        cost = self.getValue(b'paidRemovalCost')
        if cost is None:
            return self.__proxy.paidRemovalCost
        else:
            return cost.get(Currency.GOLD, 10)

    @property
    def paidDeluxeRemovalCost(self):
        cost = self.getValue(b'paidDeluxeRemovalCost')
        if cost is None:
            return self.__proxy.paidDeluxeRemovalCost
        else:
            return Money(**cost)

    def getPaidModernizedRemovalCost(self, level):
        return self.__proxy.getPaidModernizedRemovalCost(level)

    @property
    def paidTrophyBasicRemovalCost(self):
        cost = self.getValue(b'paidTrophyBasicRemovalCost')
        if cost is None:
            return self.__proxy.paidTrophyBasicRemovalCost
        else:
            return Money(**cost)

    @property
    def paidTrophyUpgradedRemovalCost(self):
        cost = self.getValue(b'paidTrophyUpgradedRemovalCost')
        if cost is None:
            return self.__proxy.paidTrophyUpgradedRemovalCost
        else:
            return Money(**cost)

    @property
    def exchangeRate(self):
        return self.getValue(b'exchangeRate', self.__proxy.exchangeRate)

    @property
    def clanCreationCost(self):
        return self.getValue(b'clanCreationCost', self.__proxy.clanCreationCost)

    @property
    def exchangeRateForShellsAndEqs(self):
        return self.getValue(b'exchangeRateForShellsAndEqs', self.__proxy.exchangeRateForShellsAndEqs)

    @property
    def sellPriceModif(self):
        return self.getValue(b'sellPriceModif', self.__proxy.sellPriceModif)

    @property
    def slotsPrices(self):
        return self.getValue(b'slotsPrices', self.__proxy.slotsPrices)

    @property
    def dropSkillsCost(self):
        value = self.__proxy.dropSkillsCost
        defaults = self.getValue(b'dropSkillsCost')
        if defaults is None:
            return value
        else:
            newValue = {}
            for k, v in value.items():
                mergedValue = v.copy()
                defaultValue = defaults.get(k, {})
                mergedValue.update(defaultValue)
                newValue[k] = mergedValue

            return newValue

    @property
    def dailyXPFactor(self):
        return self.getValue(b'dailyXPFactor', self.__proxy.dailyXPFactor)

    @property
    def winXPFactorMode(self):
        return self.getValue(b'winXPFactorMode', self.__proxy.winXPFactorMode)

    @property
    def berthsPrices(self):
        return self.getValue(b'berthsPrices', self.__proxy.berthsPrices)

    def getBattlePassCost(self):
        cost = self.getValue(b'battlePassCost')
        if cost is None:
            return self.__proxy.getBattlePassCost()
        else:
            return Money(**cost)

    def getBattlePassLevelCost(self):
        cost = self.getValue(b'battlePassLevelCost')
        if cost is None:
            return self.__proxy.getBattlePassLevelCost()
        else:
            return Money(**cost)

    @property
    def isEnabledBuyingGoldShellsForCredits(self):
        return self.getValue(b'isEnabledBuyingGoldShellsForCredits', self.__proxy.isEnabledBuyingGoldShellsForCredits)

    @property
    def isEnabledBuyingGoldEqsForCredits(self):
        return self.getValue(b'isEnabledBuyingGoldEqsForCredits', self.__proxy.isEnabledBuyingGoldEqsForCredits)

    @property
    def tankmanCost(self):
        value = self.__proxy.tankmanCost
        defaults = self.getValue(b'tankmanCost')
        if defaults is None:
            return value
        else:
            newValues = []
            for idx, cost in enumerate(value):
                default = defaults[idx] if len(defaults) > idx else {}
                newValue = cost.copy()
                newValue.update(default)
                newValues.append(newValue)

            return newValues

    @property
    def changeRoleCost(self):
        return self.getValue(b'changeRoleCost', self.__proxy.changeRoleCost)

    @property
    def tankman(self):
        return self.getValue(b'tankman', self.__proxy.tankman)

    @property
    def freeXPConversion(self):
        return self.getValue(b'freeXPConversion', self.__proxy.freeXPConversion)

    @property
    def freeXPToTManXPRate(self):
        return self.getValue(b'freeXPToTManXPRate', self.__proxy.freeXPToTManXPRate)

    def getItemsData(self):
        return self.getValue(b'items', self.__proxy.getItemsData())

    def getGoodiesData(self):
        return self.getValue(b'goodies', self.__proxy.getGoodiesData())

    def getVehCamouflagePriceFactor(self, typeCompDescr):
        value = self.getItemsData().get(b'vehicleCamouflagePriceFactors', {}).get(typeCompDescr)
        if value is None:
            return self.__proxy.getVehCamouflagePriceFactor(typeCompDescr)
        else:
            return value

    def getEmblemsGroupPriceFactors(self):
        return self.getItemsData().get(b'playerEmblemGroupPriceFactors', self.__proxy.getEmblemsGroupPriceFactors())

    def getEmblemsGroupHiddens(self):
        return self.getItemsData().get(b'notInShopPlayerEmblemGroups', self.__proxy.getEmblemsGroupHiddens())

    def getInscriptionsGroupPriceFactors(self, nationID):
        value = self.getItemsData().get(b'inscriptionGroupPriceFactors', [])
        if len(value) <= nationID:
            return self.__proxy.getInscriptionsGroupPriceFactors(nationID)
        return value[nationID]

    def getInscriptionsGroupHiddens(self, nationID):
        value = self.getItemsData().get(b'notInShopInscriptionGroups', [])
        if len(value) <= nationID:
            return self.__proxy.getInscriptionsGroupHiddens(nationID)
        return value[nationID]

    def getCamouflagesPriceFactors(self, nationID):
        value = self.getItemsData().get(b'camouflagePriceFactors', [])
        if len(value) <= nationID:
            return self.__proxy.getCamouflagesPriceFactors(nationID)
        return value[nationID]

    def getCamouflagesHiddens(self, nationID):
        value = self.getItemsData().get(b'notInShopCamouflages', [])
        if len(value) <= nationID:
            return self.__proxy.getCamouflagesHiddens(nationID)
        return value[nationID]

    @property
    def premiumCost(self):
        value = self.__proxy.premiumCost.copy()
        value.update(self.getValue(b'premiumCost', {}))
        return value

    @property
    def goodies(self):
        return self.getGoodiesData().get(b'goodies', self.__proxy.goodies)

    @property
    def camouflageCost(self):
        value = self.__proxy.camouflageCost.copy()
        value.update(self.getValue(b'camouflageCost', {}))
        return value

    @property
    def playerInscriptionCost(self):
        value = self.__proxy.playerInscriptionCost.copy()
        value.update(self.getValue(b'playerInscriptionCost', {}))
        return value

    @property
    def playerEmblemCost(self):
        value = self.__proxy.playerEmblemCost.copy()
        value.update(self.getValue(b'playerEmblemCost', {}))
        return value
