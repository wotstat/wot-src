import operator
from abc import ABCMeta, abstractmethod
from collections import defaultdict, namedtuple
import typing, constants, nations
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_WARNING
from gui.server_events import formatters
from gui.shared.economics import getActionPrc
from gui.shared.gui_items import GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES
from gui.shared.money import Currency, MONEY_UNDEFINED
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from items import vehicles, ITEM_TYPE_NAMES
from rent_common import makeRentID
from shared_utils import BoundMethodWeakref as bwr, CONST_CONTAINER
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.shared import IItemsCache
_VEH_TYPE_IDX = 1
_VEH_TYPE_NAME = ITEM_TYPE_NAMES[_VEH_TYPE_IDX]
_DT = formatters.DISCOUNT_TYPE
_MULTIPLIER = b'Multiplier'
_COMMON_CRITERIA = ~REQ_CRITERIA.HIDDEN

class ACTION_MODIFIER_TYPE(CONST_CONTAINER):
    DISCOUNT = 1
    SELLING = 2
    RENT = 3
    AVAILABILITY = 4


class ACTION_SECTION_TYPE(CONST_CONTAINER):
    ECONOMICS = 1
    ALL = 2
    ITEM = 3
    CUSTOMIZATION = 4
    BOOSTER = 5
    ALL_BOOSTERS = 6


_ActionDiscountValue = namedtuple(b'_ActionDiscountValue', b'discountName, discountValue, discountType')

class _ParamContext(object):
    __slots__ = (b'__name', b'__value', b'__currency', b'__isMultiplier')

    def __init__(self, name, value, currency=None, isMultiplier=False):
        self.__name = name
        self.__value = value
        self.__currency = currency
        self.__isMultiplier = isMultiplier
        return

    def __repr__(self):
        params = [
         b'name = %s' % self.__name,
         b'value = %s' % self.__value]
        if self.hasCurrency():
            params.append(b'currency = %s' % self.__currency)
        if self.__isMultiplier:
            params.append(b'multiplier')
        return b'_ParamContext(%s)' % (b', ').join(params)

    def getName(self):
        return self.__name

    def getValue(self):
        return self.__value

    def getCurrency(self):
        return self.__currency

    def hasCurrency(self):
        return self.__currency is not None

    def isMultiplier(self):
        return self.__isMultiplier


def _getDiscountByValue(value, default):
    return int(default - value)


def _getPercentDiscountByValue(value, default):
    return getActionPrc(value, default)


def _getDiscountByMultiplier(mult, default):
    return int(default - default * float(mult))


def _getPercentDiscountByMultiplier(mult, default):
    price = int(round(float(mult) * default))
    return getActionPrc(price, default)


def _prepareVehData(vehsList, discounts=None):
    discounts = discounts or {}
    result = []
    for v in vehsList:
        discount, discountType = discounts.get(v, (None, None))
        result.append((v, (True, discount, discountType)))

    return result


class ActionModifier(object):

    def __init__(self, name, params, modType, section=ACTION_SECTION_TYPE.ECONOMICS, itemType=None):
        self._name = name
        self._params = params
        self._type = modType
        self._itemType = itemType
        self._section = section
        self.__extParams = []
        self.__cachedValue = None
        return

    def getName(self):
        return self._name

    def getParamName(self):
        return self.getName()

    def getParamValue(self):
        return

    def getParams(self):
        return self._params

    def getType(self):
        return self._type

    def getItemType(self):
        return self._itemType

    def getSection(self):
        return self._section

    def getValues(self, action):
        return {}

    def parse(self):
        if not self.__cachedValue:
            self.__cachedValue = self._parse()
            for p in self.__extParams:
                self.__cachedValue.update(p)

        return self.__cachedValue

    def packDiscounts(self, sorting=True):
        return {}

    def update(self, modifier):
        p = modifier.parse()
        if p is not None:
            self.__extParams.append(p)
        return

    def splitModifiers(self):
        return [
         self]

    def _parse(self):
        return

    def _calcDiscountValue(self, value, default):
        return _getPercentDiscountByValue(float(value), default)

    @abstractmethod
    def getDefaultParamValue(self):
        return

    def getDefaultDiscountType(self):
        return _DT.PERCENT

    @classmethod
    def _calculateDiscount(cls, paramName, discountVal, defaultVal, discountType, discountValueCalculator=None):
        if isinstance(discountVal, tuple):
            discountVal = discountVal[1]
        if not type(float):
            discountVal = float(discountVal)
        calculator = discountValueCalculator or cls._calcDiscountValue
        value = calculator(discountVal, defaultVal)
        return _ActionDiscountValue(discountValue=value, discountType=discountType)


class _DiscountsListAction(ActionModifier):
    __meta__ = ABCMeta
    DEFAULT_PRICE_MULT = 1.0

    @abstractmethod
    def _getParamName(self, idx):
        return

    @abstractmethod
    def _getParamPattern(self):
        return b''

    @abstractmethod
    def _getMultName(self, idx):
        return

    @abstractmethod
    def _makeResultItem(self, paramValue):
        return

    def _parse(self):
        result = {}
        namePattern = self._getParamPattern()
        if namePattern:
            patternLen = len(namePattern)
            for paramName in self._params:
                if paramName.startswith(namePattern):
                    try:
                        idx = int(paramName[patternLen:])
                    except ValueError:
                        return result

                    item = self._makeResultItem(self._params[paramName])
                    if item is not None:
                        result[item] = float(self._params.get(self._getMultName(idx), self.DEFAULT_PRICE_MULT))

        return result

    def getValues(self, action):
        result = {}
        for veh, value in self.parse().iteritems():
            result[veh.intCD] = [(value, action.getID())]

        return result

    def getDefaultParamValue(self):
        return self.DEFAULT_PRICE_MULT

    def getDefaultDiscountType(self):
        return _DT.MULTIPLIER


class _PriceOpAbstract(object):
    __meta__ = ABCMeta
    itemsCache = dependency.descriptor(IItemsCache)

    @abstractmethod
    def _getDiscountParams(self, item, value):
        return (0, b'')


class _BuyPriceSet(_PriceOpAbstract):

    def _getDiscountParams(self, item, value):
        for currency in Currency.BY_WEIGHT:
            setValue = item.buyPrices.itemPrice.defPrice.get(currency)
            if setValue:
                return (_getPercentDiscountByValue(value, setValue), currency)

        return (_getPercentDiscountByValue(value, item.buyPrices.itemPrice.defPrice.credits), _DT.CREDITS)


class _RentPriceSet(_PriceOpAbstract):

    def _getRentDiscountParams(self, item, package, value):
        rentPackage = item.getRentPackage(package)
        if rentPackage:
            defaultGoldRentPrice = rentPackage.get(b'defaultRentPrice', MONEY_UNDEFINED).gold
            if defaultGoldRentPrice:
                return (_getPercentDiscountByValue(value, defaultGoldRentPrice), _DT.GOLD)
        return (
         _getPercentDiscountByValue(value, 0), _DT.CREDITS)


class _BuyPriceMul(_PriceOpAbstract):

    def _getDiscountParams(self, item, value):
        if item.buyPrices.itemPrice.defPrice.isSet(Currency.GOLD):
            return (_getPercentDiscountByMultiplier(value, item.buyPrices.itemPrice.defPrice.gold), _DT.GOLD)
        return (
         _getPercentDiscountByMultiplier(value, item.buyPrices.itemPrice.defPrice.getSignValue(Currency.CREDITS)),
         _DT.PERCENT)


class _RentPriceMul(_PriceOpAbstract):

    def _getDiscountParams(self, item, value):
        if item.rentPackages:
            defaultRentPrice = item.rentPackages[0].get(b'defaultRentPrice', MONEY_UNDEFINED)
            for currency in Currency.BY_WEIGHT:
                setValue = defaultRentPrice.get(currency)
                if setValue:
                    return (_getPercentDiscountByMultiplier(value, setValue), currency)

        return (
         _getPercentDiscountByMultiplier(value, 0), _DT.CREDITS)


class _SellPriceMul(_PriceOpAbstract):

    def _getDiscountParams(self, item, value):
        isForGold, value = value
        if item.buyPrices.itemPrice.price.isSet(Currency.GOLD):
            if isForGold:
                return (int(item.buyPrices.itemPrice.price.gold * float(value)), _DT.GOLD)
            creditsPrice = item.buyPrices.itemPrice.price.gold * self.itemsCache.items.shop.defaults.exchangeRate
            return (
             int(creditsPrice * float(value)), _DT.CREDITS)
        return (
         int(item.buyPrices.itemPrice.price.getSignValue(Currency.CREDITS) * float(value)), _DT.CREDITS)


class _ItemsPrice(_DiscountsListAction, _PriceOpAbstract):

    def __init__(self, name, params, modType=ACTION_MODIFIER_TYPE.DISCOUNT, section=ACTION_SECTION_TYPE.ITEM, itemType=None):
        super(_ItemsPrice, self).__init__(name, params, modType, section, itemType)
        return

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for item, value in items:
            dv, _ = self._getDiscountParams(item, value)
            result[item.intCD] = _ActionDiscountValue(discountName=item, discountValue=dv, discountType=_DT.PERCENT)

        return result

    def _getParamName(self, idx):
        return b'itemName%d' % idx

    def _getParamPattern(self):
        return b'itemName'

    def _getMultName(self, idx):
        return b'price%d' % idx


class _SplitByCurrency(ActionModifier):

    def __init__(self, name, params, modType=ACTION_MODIFIER_TYPE.DISCOUNT, section=ACTION_SECTION_TYPE.ITEM, itemType=None):
        super(_SplitByCurrency, self).__init__(name, params, modType, section, itemType)
        self._paramName = None
        return

    def splitModifiers(self):
        res = []
        for paramName, paramValue in self._params.iteritems():
            obj = self.__class__(self.getName(), {paramName: paramValue})
            obj.setParamName(paramName)
            res.append(obj)

        return res

    def setParamName(self, paramName):
        self._paramName = paramName
        return

    def getParamName(self):
        if self._itemType in GUI_ITEM_TYPE.ALL() and self._paramName is not None:
            itemName = GUI_ITEM_TYPE_NAMES[self._itemType]
            return (b'/').join((itemName, self._paramName))
        else:
            return self.getName()

    def getDefaultParamValue(self):
        return


class _ItemsPriceAll(ActionModifier):
    itemsCache = dependency.descriptor(IItemsCache)
    __meta__ = ABCMeta
    DEFAULT_PRICE_MULT = 1.0

    def __init__(self, name, params, modType=ACTION_MODIFIER_TYPE.DISCOUNT, section=ACTION_SECTION_TYPE.ALL, itemType=None):
        super(_ItemsPriceAll, self).__init__(name, params, modType, section, itemType)
        return

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for (_, item), value in items:
            result[item.intCD] = _ActionDiscountValue(discountName=item, discountValue=int(round((1 - float(value)) * 100)), discountType=_DT.PERCENT)

        return result

    def _parse(self):
        nation = self._params.get(self._getNationName())
        goldPriceMult = self._params.get(self._getGoldMultName())
        creditsPriceMult = self._params.get(self._getCreditsMultName())
        result = self._getConditionResult(nation, goldPriceMult, creditsPriceMult, self._getRequestCriteria())
        return result

    def _getRequestCriteria(self):
        return _COMMON_CRITERIA

    def _getConditionResult(self, nation, goldPriceMult, creditsPriceMult, criteria):
        result = {}
        for v in self.itemsCache.items.getItems(itemTypeID=self._itemType, criteria=criteria).itervalues():
            if v.buyPrices.itemPrice.price.isSet(Currency.GOLD) and goldPriceMult is not None:
                result[(nation, v)] = float(goldPriceMult)
            elif v.buyPrices.itemPrice.price.isSet(Currency.CREDITS) and creditsPriceMult is not None:
                result[(nation, v)] = float(creditsPriceMult)

        return result

    def _getGoldMultName(self):
        return b'goldPriceMultiplier'

    def _getCreditsMultName(self):
        return b'creditsPriceMultiplier'

    def _getNationName(self):
        return b'nation'

    def _packMultiplier(self, multName, multVal):
        return _ActionDiscountValue(discountName=multName, discountValue=int(round((1 - float(multVal)) * 100)), discountType=_DT.PERCENT)

    def getValues(self, action):
        result = defaultdict(list)
        parsedValue = self.parse()
        if parsedValue:
            for (nation, multType), value in parsedValue.iteritems():
                if nation is None:
                    nation = nations.NONE_INDEX
                else:
                    nation = nations.INDICES[nation]
                result[nation].append(((multType, value), action.getID()))

        return result


class _VehiclePrice(_ItemsPrice):

    def __init__(self, name, params, modType=ACTION_MODIFIER_TYPE.DISCOUNT, section=ACTION_SECTION_TYPE.ITEM):
        super(_VehiclePrice, self).__init__(name, params, modType, section, GUI_ITEM_TYPE.VEHICLE)
        return

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for v, value in items:
            dv, dt = self._getDiscountParams(v, value)
            dt = dt if self.getType() == ACTION_MODIFIER_TYPE.SELLING else _DT.PERCENT
            result[v.intCD] = _ActionDiscountValue(discountName=v, discountValue=dv, discountType=dt)

        return result

    def _makeResultItem(self, vehName):
        try:
            if b':' in vehName:
                vehIDs = vehicles.g_list.getIDsByName(vehName)
            else:
                vehIDs = vehicles.g_list.getIDsByVehName(vehName)
            vehTypeCompDescr = vehicles.makeIntCompactDescrByID(_VEH_TYPE_NAME, *vehIDs)
            return self.itemsCache.items.getItemByCD(vehTypeCompDescr)
        except Exception:
            LOG_ERROR(b'There is error while getting vehicle item', vehName)
            LOG_CURRENT_EXCEPTION()

        return

    def _getParamName(self, idx):
        return b'vehName%d' % idx

    def _getParamPattern(self):
        return b'vehName'


class _VehicleRentPrice(_VehiclePrice):

    def __init__(self, name, params, modType=ACTION_MODIFIER_TYPE.RENT, section=ACTION_SECTION_TYPE.ITEM):
        super(_VehicleRentPrice, self).__init__(name, params, modType=modType, section=section)
        return

    def packDiscounts(self, sorting=True):
        res = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for (vehicle, package), value in items:
            dv, _ = self._getDiscountParams(vehicle, value)
            res[(vehicle.intCD, package)] = _ActionDiscountValue(discountName=vehicle, discountValue=dv, discountType=_DT.PERCENT)

        return res

    def _parse(self):
        result = {}
        namePattern = self._getParamPattern()
        if namePattern:
            patternLen = len(namePattern)
            for paramName in self._params:
                if paramName.startswith(namePattern):
                    try:
                        idx = int(paramName[patternLen:])
                    except ValueError:
                        return result

                    item = self._makeResultItem(self._params[paramName])
                    if item is not None:
                        for rentPackage in item.rentPackages:
                            rentID = rentPackage[b'rentID']
                            result[(item, rentID)] = float(self._params.get(self._getMultName(idx), self.DEFAULT_PRICE_MULT))

        return result

    def getValues(self, action):
        result = {}
        for (vehicle, package), value in self.parse().iteritems():
            result[(vehicle.intCD, package)] = [(value, action.getID())]

        return result


class _EquipmentPrice(_ItemsPrice):

    def __init__(self, name, params):
        super(_EquipmentPrice, self).__init__(name, params, itemType=GUI_ITEM_TYPE.EQUIPMENT)
        return

    def _makeResultItem(self, eqName):
        try:
            vehCache = vehicles.g_cache
            idx = vehCache.equipmentIDs().get(eqName)
            if idx is not None:
                return self.itemsCache.items.getItemByCD(vehCache.equipments()[idx].compactDescr)
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return


class _OptDevicePrice(_ItemsPrice):

    def __init__(self, name, params):
        super(_OptDevicePrice, self).__init__(name, params, itemType=GUI_ITEM_TYPE.OPTIONALDEVICE)
        return

    def _makeResultItem(self, devName):
        try:
            vehCache = vehicles.g_cache
            idx = vehCache.optionalDeviceIDs().get(devName)
            if idx is not None:
                return self.itemsCache.items.getItemByCD(vehCache.optionalDevices()[idx].compactDescr)
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return


class _ShellPrice(_ItemsPrice):

    def __init__(self, name, params):
        super(_ShellPrice, self).__init__(name, params, itemType=GUI_ITEM_TYPE.SHELL)
        return

    def _getParamName(self, idx):
        return b'shellName%d' % idx

    def _getParamPattern(self):
        return b'shellName'

    def _makeResultItem(self, shellName):
        shellNation, shellName = shellName.split(b':')
        shellNation = nations.INDICES[shellNation]
        try:
            vehCache = vehicles.g_cache
            idx = vehCache.shellIDs(shellNation).get(shellName)
            if idx is not None:
                return self.itemsCache.items.getItemByCD(vehCache.shells(shellNation)[idx].compactDescr)
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return


_ECONOMICS_SET_EXCLUDE_IN_GUI = (
 b'dailyXPFactor', b'exchangeRateForShellsAndEqs')
_ECONOMICS_SET_EXCLUDE_IN_PARCING = (
 b'tradeInAllowedVehicleLevels',
 b'tradeInForbiddenVehicles',
 b'freeXPConversionDiscrecitydailyXPFactor')

class EconomicsSet(ActionModifier):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, name, params, paramName=b'', paramValue=b''):
        super(EconomicsSet, self).__init__(name, params, ACTION_MODIFIER_TYPE.DISCOUNT)
        self._paramName = paramName
        self._paramValue = paramValue
        self.__handlers = {b'premiumPacket1Cost': (bwr(self.handlerPremiumPacket1)), 
           b'premiumPacket3Cost': (bwr(self.handlerPremiumPacket3)), 
           b'premiumPacket7Cost': (bwr(self.handlerPremiumPacket7)), 
           b'premiumPacket14Cost': (bwr(self.handlerPremiumPacket14)), 
           b'premiumPacket30Cost': (bwr(self.handlerPremiumPacket30)), 
           b'premiumPacket90Cost': (bwr(self.handlerPremiumPacket90)), 
           b'premiumPacket180Cost': (bwr(self.handlerPremiumPacket180)), 
           b'premiumPacket360Cost': (bwr(self.handlerPremiumPacket360)), 
           b'freeXPConversionDiscrecity': (bwr(self.handlerFreeXPConversionDiscrecity)), 
           b'exchangeRate': (bwr(self.handlerExchangeRate)), 
           b'exchangeRateForShellsAndEqs': (bwr(self.handlerExchangeRateForShellsAndEqs)), 
           b'slotsPrices': (bwr(self.handlerSlotsPrices)), 
           b'creditsTankmanCost': (bwr(self.handlerCreditsTankmanCost)), 
           b'goldTankmanCost': (bwr(self.handlerGoldTankmanCost)), 
           b'changeRoleCost': (bwr(self.handlerChangeRoleCost)), 
           b'creditsDropSkillsCost': (bwr(self.handlerCreditsDropSkillsCost)), 
           b'goldDropSkillsCost': (bwr(self.handlerGoldDropSkillsCost)), 
           b'clanCreationCost': (bwr(self.handlerClanCreationCost)), 
           b'paidRemovalCost': (bwr(self.handlerPaidRemovalCost)), 
           b'paidDeluxeRemovalCost': (bwr(self.handlerPaidDeluxeRemovalCost)), 
           b'berthsPrices': (bwr(self.handlerBerthsPrices)), 
           b'freeXPToTManXPRate': (bwr(self.handlerFreeXPToTManXPRate)), 
           b'tradeInSellPriceFactor': (bwr(self.handlerTradeInSellPriceFactor))}
        return

    def getParamName(self):
        return self._makeParamCtx(self._paramName, self._paramValue).getName()

    def getParamValue(self):
        return self._paramValue

    def packDiscounts(self, sorting=True):
        data = self.parse()
        for sectionName, value in data.iteritems():
            paramCtx = self._makeParamCtx(sectionName, value)
            wrappedName = paramCtx.getName()
            if wrappedName in self.__handlers:
                try:
                    fResult = self.__handlers[wrappedName](paramCtx)
                    if fResult:
                        return {wrappedName: fResult}
                except Exception:
                    LOG_ERROR(b'Error while calculating economics discount', paramCtx)
                    LOG_CURRENT_EXCEPTION()

        return {}

    def splitModifiers(self):
        res = []
        for k, v in self._params.iteritems():
            if k not in _ECONOMICS_SET_EXCLUDE_IN_GUI:
                obj = self.__class__(self.getName(), {k: v}, paramName=k, paramValue=v)
                res.append(obj)

        return res

    def _parse(self):
        result = {}
        for k, v in self._params.iteritems():
            if k in _ECONOMICS_SET_EXCLUDE_IN_PARCING:
                continue
            try:
                result[k] = float(v)
            except ValueError as ex:
                LOG_WARNING(b'There is error while converting action set_Economics param', ex.message)

        return result

    def _makeParamCtx(self, name, value):
        if name == b'winXPFactorMode':
            newName = (b'/').join((name, self.getParamValue()))
            currency = None
        else:
            newName, currency = self._extractCurrency(name)
        return _ParamContext(newName, value, currency)

    @classmethod
    def _calcCustomizationDiscountValue(cls, value, default):
        return int(100 * _getDiscountByValue(int(value), default) / default)

    def handlerSlotsPrices(self, ctx):
        default = self.itemsCache.items.shop.defaults.getVehicleSlotsPrice(self.itemsCache.items.stats.vehicleSlots)
        return self._calculateDiscount(b'slotsPrices', ctx.getValue(), default.get(default.getCurrency(), 0), _DT.PERCENT)

    def handlerBerthsPrices(self, ctx):
        default, _ = self.itemsCache.items.shop.defaults.getTankmanBerthPrice(self.itemsCache.items.stats.tankmenBerthsCount)
        return self._calculateDiscount(b'berthsPrices', ctx.getValue(), default.gold, _DT.PERCENT)

    def handlerCreditsTankmanCost(self, ctx):
        tankmanCost = self.itemsCache.items.shop.defaults.tankmanCost
        if tankmanCost is not None:
            return self._calculateDiscount(b'creditsTankmanCost', ctx.getValue(), tankmanCost[1][Currency.CREDITS], _DT.PERCENT)
        else:
            return float(ctx.getValue())

    def handlerGoldTankmanCost(self, ctx):
        tankmanCost = self.itemsCache.items.shop.defaults.tankmanCost
        if tankmanCost is not None:
            return self._calculateDiscount(b'goldTankmanCost', ctx.getValue(), tankmanCost[2][Currency.GOLD], _DT.PERCENT)
        else:
            return float(ctx.getValue())

    def handlerChangeRoleCost(self, ctx):
        default = self.itemsCache.items.shop.defaults.changeRoleCost
        return self._calculateDiscount(b'changeRoleCost', ctx.getValue(), default, _DT.PERCENT)

    def handlerCreditsDropSkillsCost(self, ctx):
        dropSkillsCost = self.itemsCache.items.shop.defaults.dropSkillsCost
        if dropSkillsCost is not None:
            return self._calculateDiscount(b'creditsDropSkillsCost', ctx.getValue(), dropSkillsCost[1][Currency.CREDITS], _DT.PERCENT)
        else:
            return float(ctx.getValue())

    def handlerGoldDropSkillsCost(self, ctx):
        dropSkillsCost = self.itemsCache.items.shop.defaults.dropSkillsCost
        if dropSkillsCost is not None:
            return self._calculateDiscount(b'goldDropSkillsCost', ctx.getValue(), dropSkillsCost[2][Currency.GOLD], _DT.PERCENT)
        else:
            return float(ctx.getValue())

    def handlerExchangeRate(self, ctx):
        default = self.itemsCache.items.shop.defaults.exchangeRate
        shopValue = self.itemsCache.items.shop.exchangeRate
        return self._calculateDiscount(b'exchangeRate', shopValue, default, _DT.MULTIPLIER, discountValueCalculator=self._calculateModifier)

    def handlerExchangeRateForShellsAndEqs(self, ctx):
        default = self.itemsCache.items.shop.defaults.exchangeRateForShellsAndEqs
        return self._calculateDiscount(b'exchangeRateForShellsAndEqs', ctx.getValue(), default, _DT.PERCENT)

    def handlerPaidRemovalCost(self, ctx):
        default = self.itemsCache.items.shop.defaults.paidRemovalCost
        return self._calculateDiscount(b'paidRemovalCost', ctx.getValue(), default, _DT.PERCENT)

    def handlerPaidDeluxeRemovalCost(self, ctx):
        default = self.itemsCache.items.shop.defaults.paidDeluxeRemovalCost.get(ctx.getCurrency())
        return self._calculateDiscount(b'paidDeluxeRemovalCost', ctx.getValue(), default, _DT.PERCENT)

    def handlerClanCreationCost(self, ctx):
        default = self.itemsCache.items.shop.defaults.clanCreationCost
        return self._calculateDiscount(b'clanCreationCost', ctx.getValue(), default, _DT.PERCENT)

    def handlerFreeXPConversionDiscrecity(self, ctx):
        default = self.itemsCache.items.shop.defaults.freeXPConversion[0]
        shopValue = self.itemsCache.items.shop.freeXPConversion[0]
        return self._calculateDiscount(b'freeXPConversionDiscrecity', shopValue, default, _DT.MULTIPLIER, discountValueCalculator=self._calculateModifier)

    def handlerFreeXPToTManXPRate(self, ctx):
        default = self.itemsCache.items.shop.defaults.freeXPToTManXPRate
        shopValue = self.itemsCache.items.shop.freeXPToTManXPRate
        return self._calculateDiscount(b'freeXPToTManXPRate', shopValue, default, _DT.MULTIPLIER, discountValueCalculator=self._calculateModifier)

    def handlerPremiumPacket1(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(1)
        return self._calculateDiscount(b'premiumPacket1', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket3(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(3)
        return self._calculateDiscount(b'premiumPacket3', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket7(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(7)
        return self._calculateDiscount(b'premiumPacket7', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket14(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(14)
        return self._calculateDiscount(b'premiumPacket14', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket30(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(30)
        return self._calculateDiscount(b'premiumPacket30', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket90(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(90)
        return self._calculateDiscount(b'premiumPacket90', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket180(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(180)
        return self._calculateDiscount(b'premiumPacket180', ctx.getValue(), default, _DT.PERCENT)

    def handlerPremiumPacket360(self, ctx):
        default = self.itemsCache.items.shop.defaults.getPremiumPacketCost(360)
        return self._calculateDiscount(b'premiumPacket360', ctx.getValue(), default, _DT.PERCENT)

    def handlerTradeInSellPriceFactor(self, ctx):
        return self._calculateDiscount(b'tradeInSellPriceFactor', ctx.getValue(), 1, _DT.TRADE_IN_PERCENT, discountValueCalculator=(lambda v, _: int(v * 100)))

    def handlerWinXPFactorMode(self):
        winXpFactor = self.itemsCache.items.shop.winXPFactorMode
        if winXpFactor == constants.WIN_XP_FACTOR_MODE.DAILY:
            return None
        else:
            dailyFactor = self.itemsCache.items.shop.dailyXPFactor
            return _ActionDiscountValue(discountName=b'winXPFactorMode', discountValue=dailyFactor, discountType=_DT.MULTIPLIER)

    def _calculateDiscount(self, paramName, discountVal, defaultVal, discountType, discountValueCalculator=None):
        calculator = discountValueCalculator or self._calcDiscountValue
        value = calculator(discountVal, defaultVal)
        return _ActionDiscountValue(discountName=paramName, discountValue=value, discountType=discountType)

    def _calculateModifier(self, value, defaultValue):
        if value % defaultValue > 0:
            return round(float(value) / defaultValue, 2)
        return int(value / defaultValue)

    def getValues(self, action):
        result = defaultdict(dict)
        for key, value in self.parse().iteritems():
            result[key] = [
             (
              value, action.getID())]

        return result

    def _extractCurrency(self, name):
        for cur in Currency.ALL:
            if name.endswith(cur.capitalize()):
                return (name[:-len(cur)], cur)

        return (
         name, None)


class EconomicsMul(EconomicsSet):

    def _makeParamCtx(self, name, value):
        newName, currency = self._extractCurrency(name)
        isMult = False
        if name != b'exchangeRateForShellsAndEqs' and newName.endswith(_MULTIPLIER):
            newName = newName[:-len(_MULTIPLIER)]
            isMult = True
        return _ParamContext(newName, value, currency=currency, isMultiplier=isMult)

    def _calcDiscountValue(self, value, default):
        return _getPercentDiscountByMultiplier(value, default)

    def _calcCustomizationDiscountValue(self, value, default):
        return _getDiscountByMultiplier(float(value), 100)


class EquipmentPriceSet(_EquipmentPrice, _BuyPriceSet):
    pass


class EquipmentPriceMul(_EquipmentPrice, _BuyPriceMul):

    def _getMultName(self, idx):
        return b'priceMultiplier%d' % idx


class EquipmentPriceAll(_SplitByCurrency, _ItemsPriceAll):

    def __init__(self, name, params):
        super(EquipmentPriceAll, self).__init__(name, params, itemType=GUI_ITEM_TYPE.EQUIPMENT)
        return

    def _getRequestCriteria(self):
        return _COMMON_CRITERIA


class OptDevicePriceAll(_ItemsPriceAll, _BuyPriceMul):

    def __init__(self, name, params):
        super(OptDevicePriceAll, self).__init__(name, params, itemType=GUI_ITEM_TYPE.OPTIONALDEVICE)
        return

    def _getRequestCriteria(self):
        return _COMMON_CRITERIA


class OptDevicePriceSet(_OptDevicePrice, _BuyPriceSet):
    pass


class OptDevicePriceMul(_OptDevicePrice, _BuyPriceMul):

    def _getMultName(self, idx):
        return b'priceMultiplier%d' % idx


class ShellPriceAll(_SplitByCurrency, _ItemsPriceAll):

    def __init__(self, name, params):
        super(ShellPriceAll, self).__init__(name, params, itemType=GUI_ITEM_TYPE.SHELL)
        return

    def _getRequestCriteria(self):
        return _COMMON_CRITERIA


class ShellPriceNation(ShellPriceAll):

    def __init__(self, name, params, paramName=None):
        super(ShellPriceNation, self).__init__(name, params)
        self._paramName = paramName
        return

    def splitModifiers(self):
        class_ = self.__class__
        name = self.getName()
        nation = self._params.get(b'nation')
        res = [class_(name, {param: value, b'nation': nation} if nation else {param: value}, param) for param, value in self._params.iteritems() if param != b'nation']
        return res


class ShellPriceSet(_ShellPrice, _BuyPriceSet):
    pass


class ShellPriceMul(_ShellPrice, _BuyPriceMul):

    def _getMultName(self, idx):
        return b'priceMultiplier%d' % idx


class VehPriceAll(_ItemsPriceAll):

    def __init__(self, name, params):
        super(VehPriceAll, self).__init__(name, params, itemType=GUI_ITEM_TYPE.VEHICLE)
        return


class VehRentPriceAll(_ItemsPriceAll):

    def __init__(self, name, params, modType=ACTION_MODIFIER_TYPE.RENT, section=ACTION_SECTION_TYPE.ALL, itemType=GUI_ITEM_TYPE.VEHICLE):
        super(VehRentPriceAll, self).__init__(name, params, modType=modType, section=section, itemType=itemType)
        return


class VehPriceNation(_ItemsPriceAll):

    def __init__(self, name, params):
        super(VehPriceNation, self).__init__(name, params, itemType=GUI_ITEM_TYPE.VEHICLE)
        return


class VehRentPriceNation(_ItemsPriceAll):

    def __init__(self, name, params):
        super(VehRentPriceNation, self).__init__(name, params, itemType=GUI_ITEM_TYPE.VEHICLE, section=ACTION_SECTION_TYPE.ALL, modType=ACTION_MODIFIER_TYPE.RENT)
        return


class VehPriceSet(_VehiclePrice, _BuyPriceSet):
    pass


class VehRentPriceSet(_VehicleRentPrice, _RentPriceSet):
    MAX_RENT_PACKAGES_COUNT = 6

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for (vehicle, package), rentCost in items:
            dv, _ = self._getRentDiscountParams(vehicle, package, rentCost)
            result[vehicle.intCD] = _ActionDiscountValue(discountName=vehicle, discountValue=dv, discountType=_DT.PERCENT)

        return result

    def _getParamName(self, idx):
        return b'rentPacket%dDays' % idx

    def _getMultName(self, idx):
        return b'rentPacket%dCost' % idx

    def _parse(self):
        result = {}
        if b'vehName' in self._params:
            item = self._makeResultItem(self._params[b'vehName'])
            if item is not None:
                for idx in xrange(self.MAX_RENT_PACKAGES_COUNT):
                    paramName = self._getParamName(idx)
                    multName = self._getMultName(idx)
                    if paramName in self._params and multName in self._params:
                        rentID = makeRentID(constants.RentType.TIME_RENT, int(self._params.get(paramName, 0)))
                        result[(item, rentID)] = int(self._params.get(multName, 0))

            return result
        return


class VehPriceMul(_VehiclePrice, _BuyPriceMul):

    def _getMultName(self, idx):
        return b'priceMultiplier%d' % idx


class VehRentPriceMul(VehPriceMul, _VehicleRentPrice, _RentPriceMul):
    pass


class VehPriceCond(_VehiclePrice, _BuyPriceMul):
    DEFAULT_PRICE_MULT = 1.0

    def _getRequestCriteria(self):
        criteria = ~REQ_CRITERIA.SECRET | ~REQ_CRITERIA.HIDDEN
        if b'nation' in self._params:
            criteria |= REQ_CRITERIA.NATIONS([
             nations.INDICES[self._params[b'nation']]])
        if b'levelEqual' in self._params:
            criteria |= REQ_CRITERIA.VEHICLE.LEVELS([int(self._params[b'levelEqual'])])
        else:
            criteria |= REQ_CRITERIA.VEHICLE.LEVELS(range(int(self._params.get(b'levelMoreThan', 0)) + 1, int(self._params.get(b'levelLessThan', constants.MAX_VEHICLE_LEVEL + 1))))
        if b'vehClass' in self._params:
            criteria |= REQ_CRITERIA.VEHICLE.CLASSES([self._params[b'vehClass']])
        return criteria

    def _parse(self):
        result = {}
        try:
            goldPriceMult = self._params.get(b'goldPriceMultiplier')
            creditsPriceMult = self._params.get(b'creditsPriceMultiplier')
            result = self._getConditionResult(goldPriceMult, creditsPriceMult, self._getRequestCriteria())
        except Exception:
            LOG_ERROR(b'There is error while vehicles getting')
            LOG_CURRENT_EXCEPTION()

        return result

    def _getConditionResult(self, goldPriceMult, creditsPriceMult, criteria):
        result = {}
        for v in self.itemsCache.items.getVehicles(criteria).itervalues():
            if v.buyPrices.itemPrice.price.isSet(Currency.GOLD) and goldPriceMult is not None:
                result[v] = float(goldPriceMult)
            elif v.buyPrices.itemPrice.price.isSet(Currency.CREDITS) and creditsPriceMult is not None:
                result[v] = float(creditsPriceMult)

        return result


class VehRentPriceCond(VehPriceCond, _VehicleRentPrice, _RentPriceMul):

    def _getConditionResult(self, goldPriceMult, creditsPriceMult, criteria):
        result = {}
        for v in self.itemsCache.items.getVehicles(criteria).itervalues():
            for rentPackage in v.rentPackages:
                rentCost = rentPackage[b'rentPrice']
                rentID = rentPackage[b'rentID']
                if rentCost.isSet(Currency.GOLD) and goldPriceMult is not None:
                    result[(v, rentID)] = float(goldPriceMult)
                elif rentCost.isSet(Currency.CREDITS) and creditsPriceMult is not None:
                    result[(v, rentID)] = float(creditsPriceMult)

        return result


class VehSellPriceSet(_VehiclePrice, _SellPriceMul):
    DEFAULT_PRICE_MULT = 0.5

    def __init__(self, name, params):
        super(VehSellPriceSet, self).__init__(name, params, ACTION_MODIFIER_TYPE.SELLING)
        return

    def packDiscounts(self, sorting=True):
        results = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for vehicle, value in items:
            dv, dt = self._getDiscountParams(vehicle, value)
            results[vehicle.intCD] = _ActionDiscountValue(discountName=vehicle, discountValue=dv, discountType=dt)

        return results

    def _parse(self):
        isForGold = self._params.get(b'sellForGold', b'false') != b'false'
        result = {}
        for v, value in super(VehSellPriceSet, self)._parse().iteritems():
            result[v] = (isForGold, value)

        return result

    def _getMultName(self, idx):
        return b'sellPriceFactor'


class _BoosterPrice(_DiscountsListAction, _PriceOpAbstract):
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, name, params):
        super(_BoosterPrice, self).__init__(name, params, ACTION_MODIFIER_TYPE.DISCOUNT, ACTION_SECTION_TYPE.BOOSTER)
        return

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for item, value in items:
            dv, _ = self._getDiscountParams(item, value)
            result[item.boosterID] = _ActionDiscountValue(discountName=item, discountValue=dv, discountType=_DT.PERCENT)

        return result

    def getValues(self, action):
        result = {}
        for booster, value in self.parse().iteritems():
            result[booster.boosterID] = [(value, action.getID())]

        return result

    def _getParamName(self, idx):
        return b'goodieID%d' % idx

    def _getParamPattern(self):
        return b'goodieID'

    def _getMultName(self, idx):
        return b'price%d' % idx

    def _getRequestCriteria(self):
        criteria = _COMMON_CRITERIA | REQ_CRITERIA.BOOSTER.ENABLED
        return criteria

    def _makeResultItem(self, strBoosterID):
        try:
            if strBoosterID.isdigit():
                boosterID = int(strBoosterID)
            else:
                _, boosterIdPart = strBoosterID.split(b'_')
                boosterID = int(boosterIdPart)
            goodies = self.goodiesCache.getBoosters(criteria=self._getRequestCriteria())
            if boosterID in goodies:
                return goodies[boosterID]
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return


class BoosterPriceSet(_BoosterPrice, _BuyPriceSet):
    pass


class BoosterPriceMul(_BoosterPrice, _BuyPriceMul):

    def _getMultName(self, idx):
        return b'priceMultiplier%d' % idx


class BoostersPriceAll(_ItemsPriceAll):
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, name, params):
        super(BoostersPriceAll, self).__init__(name, params, ACTION_MODIFIER_TYPE.DISCOUNT, ACTION_SECTION_TYPE.ALL_BOOSTERS)
        return

    def _getRequestCriteria(self):
        criteria = _COMMON_CRITERIA | REQ_CRITERIA.BOOSTER.ENABLED
        return criteria

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for (_, booster), value in items:
            result[booster.boosterID] = _ActionDiscountValue(discountName=booster, discountValue=int(round((1 - float(value)) * 100)), discountType=_DT.PERCENT)

        return result

    def _getConditionResult(self, nation, goldPriceMult, creditsPriceMult, criteria):
        result = {}
        for booster in self.goodiesCache.getBoosters(criteria=criteria).itervalues():
            buyPrices = booster.buyPrices
            if buyPrices.hasPriceIn(Currency.GOLD) and goldPriceMult is not None:
                result[(nation, booster)] = float(goldPriceMult)
            elif buyPrices.hasPriceIn(Currency.CREDITS) and creditsPriceMult is not None:
                result[(nation, booster)] = float(creditsPriceMult)

        return result


class _C11nPrice(_ItemsPrice):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getParamName(self, idx):
        return b'name%d' % idx

    def _getParamPattern(self):
        return b'name'

    def _parse(self):
        result = {}
        namePattern = self._getParamPattern()
        if namePattern:
            patternLen = len(namePattern)
            criteria = _COMMON_CRITERIA
            items = self.itemsCache.items.getItems(itemTypeID=GUI_ITEM_TYPE.CUSTOMIZATIONS, criteria=criteria, nationID=nations.NONE_INDEX)
            for paramName in self._params:
                if paramName.startswith(namePattern):
                    try:
                        idx = int(paramName[patternLen:])
                    except ValueError:
                        return result

                    priceGroup = self._params[paramName]
                    criteria = REQ_CRITERIA.CUSTOMIZATION.PRICE_GROUP(priceGroup)
                    for item in filter(criteria, items.itervalues()):
                        result[item] = float(self._params.get(self._getMultName(idx), self.DEFAULT_PRICE_MULT))

        return result


class C11nPriceGroupPriceSet(_C11nPrice, _BuyPriceSet):
    pass


class C11nPriceGroupPriceMul(_C11nPrice, _BuyPriceMul):

    def _getMultName(self, idx):
        return b'priceFactorMultiplier%d' % idx


class C11nPriceGroupPriceByTagMul(C11nPriceGroupPriceMul):

    def _getParamName(self, idx):
        return b'tag%d' % idx

    def _getParamPattern(self):
        return b'tag'

    def _parse(self):
        result = {}
        namePattern = self._getParamPattern()
        if namePattern:
            patternLen = len(namePattern)
            criteria = _COMMON_CRITERIA
            items = self.itemsCache.items.getItems(itemTypeID=GUI_ITEM_TYPE.CUSTOMIZATIONS, criteria=criteria, nationID=nations.NONE_INDEX)
            for paramName in self._params:
                if paramName.startswith(namePattern):
                    try:
                        idx = int(paramName[patternLen:])
                    except ValueError:
                        return result

                    tag = self._params[paramName]
                    criteria = REQ_CRITERIA.CUSTOMIZATION.PRICE_GROUP_TAG(tag)
                    for item in filter(criteria, items.itervalues()):
                        result[item] = float(self._params.get(self._getMultName(idx), self.DEFAULT_PRICE_MULT))

        return result


class C11nPriceGroupPriceAll(_ItemsPriceAll):

    def __init__(self, name, params):
        super(C11nPriceGroupPriceAll, self).__init__(name, params, modType=ACTION_MODIFIER_TYPE.DISCOUNT, section=ACTION_SECTION_TYPE.CUSTOMIZATION, itemType=GUI_ITEM_TYPE.CUSTOMIZATIONS)
        return

    def packDiscounts(self, sorting=True):
        result = {}
        items = self.parse().iteritems()
        if sorting:
            items = sorted(items, key=operator.itemgetter(0))
        for (_, item), value in items:
            result[(item.itemTypeID, item.id)] = _ActionDiscountValue(discountName=item, discountValue=int(round((1 - float(value)) * 100)), discountType=_DT.PERCENT)

        return result


class MarathonEventModifier(ActionModifier):

    def __init__(self, name, params):
        super(MarathonEventModifier, self).__init__(name, params, modType=ACTION_MODIFIER_TYPE.DISCOUNT, section=ACTION_SECTION_TYPE.ALL, itemType=GUI_ITEM_TYPE.ACHIEVEMENT)
        return


class ReferralModifier(ActionModifier):

    def __init__(self, name, params):
        super(ReferralModifier, self).__init__(b'referralDisabled', params, modType=ACTION_MODIFIER_TYPE.AVAILABILITY)
        return


class EventStateModifier(ActionModifier):

    def __init__(self, name, params):
        super(EventStateModifier, self).__init__(name, params, modType=ACTION_MODIFIER_TYPE.AVAILABILITY)
        return

    def getState(self):
        return self.getParams().get(b'state')


class TradeInModifier(ActionModifier):

    def __init__(self, name, params):
        super(TradeInModifier, self).__init__(b'tradein', params, modType=ACTION_MODIFIER_TYPE.AVAILABILITY)
        return


class LobbyHeaderTabCounterModifier(ActionModifier):

    def __init__(self, _, params):
        super(LobbyHeaderTabCounterModifier, self).__init__(b'LobbyHeaderTabCounterModification', params, modType=ACTION_MODIFIER_TYPE.AVAILABILITY)
        return

    def getAlias(self):
        return self._params.get(b'alias', b'')

    def getCounterValue(self):
        return self._params.get(b'counterValue', b'')


_MODIFIERS = (
 (
  b'mul_EconomicsParams', EconomicsMul),
 (
  b'set_EconomicsParams', EconomicsSet),
 (
  b'mul_EconomicsPrices', EconomicsMul),
 (
  b'set_EconomicsPrices', EconomicsSet),
 (
  b'set_TradeIn', TradeInModifier),
 (
  b'cond_VehPrice', VehPriceCond),
 (
  b'mul_VehPrice', VehPriceMul),
 (
  b'set_VehPrice', VehPriceSet),
 (
  b'mul_VehPriceAll', VehPriceAll),
 (
  b'mul_VehPriceNation', VehPriceNation),
 (
  b'set_VehSellPrice', VehSellPriceSet),
 (
  b'cond_VehRentPrice', VehRentPriceCond),
 (
  b'mul_VehRentPrice', VehRentPriceMul),
 (
  b'set_VehRentPrice', VehRentPriceSet),
 (
  b'mul_VehRentPriceAll', VehRentPriceAll),
 (
  b'mul_VehRentPriceNation', VehRentPriceNation),
 (
  b'mul_EquipmentPriceAll', EquipmentPriceAll),
 (
  b'mul_EquipmentPrice', EquipmentPriceMul),
 (
  b'set_EquipmentPrice', EquipmentPriceSet),
 (
  b'mul_OptionalDevicePriceAll', OptDevicePriceAll),
 (
  b'mul_OptionalDevicePrice', OptDevicePriceMul),
 (
  b'set_OptionalDevicePrice', OptDevicePriceSet),
 (
  b'mul_ShellPriceAll', ShellPriceAll),
 (
  b'mul_ShellPriceNation', ShellPriceNation),
 (
  b'mul_ShellPrice', ShellPriceMul),
 (
  b'set_ShellPrice', ShellPriceSet),
 (
  b'set_PriceGroupPrice', C11nPriceGroupPriceSet),
 (
  b'mul_PriceGroupPrice', C11nPriceGroupPriceMul),
 (
  b'mul_PriceGroupPriceByTag', C11nPriceGroupPriceByTagMul),
 (
  b'mul_PriceGroupPriceAll', C11nPriceGroupPriceAll),
 (
  b'set_GoodiePrice', BoosterPriceSet),
 (
  b'mul_GoodiePrice', BoosterPriceMul),
 (
  b'mul_GoodiePriceAll', BoostersPriceAll),
 (
  b'set_MarathonAnnounce', MarathonEventModifier),
 (
  b'set_MarathonInProgress', MarathonEventModifier),
 (
  b'set_MarathonFinished', MarathonEventModifier),
 (
  b'ReferralProgramDisabled', ReferralModifier),
 (
  b'EventState', EventStateModifier),
 (
  b'LobbyHeaderTabCounterModification', LobbyHeaderTabCounterModifier))
_MODIFIERS_DICT = dict(_MODIFIERS)
_MODIFIERS_ORDER = dict((n, idx) for idx, (n, _) in enumerate(_MODIFIERS))

def compareModifiers(modName1, modName2):
    if modName1 not in _MODIFIERS_ORDER:
        return -1
    if modName2 not in _MODIFIERS_ORDER:
        return 1
    return _MODIFIERS_ORDER[modName1] - _MODIFIERS_ORDER[modName2]


_g_cache = {}

def _freeze(obj):
    if isinstance(obj, dict):
        return frozenset({key: _freeze(value) for key, value in obj.items()}.items())
    if isinstance(obj, list):
        return tuple([_freeze(value) for value in obj])
    return obj


def getModifierObj(name, params):
    key = (
     name, _freeze(params))
    if key in _g_cache:
        return _g_cache[key]
    else:
        modifier = None
        if name in _MODIFIERS_DICT:
            modifier = _MODIFIERS_DICT[name](name, params)
            _g_cache[key] = modifier
        return modifier


def clearModifiersCache():
    _g_cache.clear()
    return
