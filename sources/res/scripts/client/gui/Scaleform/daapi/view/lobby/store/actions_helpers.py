from __future__ import absolute_import, division
import operator, time
from collections import namedtuple
from future.utils import viewitems, viewvalues
import constants, nations
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.event_items import ActionData
from gui.server_events.events_helpers import EventInfoModel
from gui.server_events.formatters import formatStrDiscount, formatPercentValue, formatMultiplierValue, formatGoldPriceNormalCard, formatCreditPriceNormalCard, DECORATION_SIZES, formatGoldPrice, formatGoldPriceBig, formatCreditPrice, formatCreditPriceBig, formatVehicleLevel, DISCOUNT_TYPE
from gui.shared.formatters import icons
from gui.server_events import settings as quest_settings
from helpers import i18n, dependency, time_utils
from skeletons.gui.game_control import IMarathonEventsController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.gui_items import GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import getTypeBigIconPath, getTypeSmallIconPath
from gui.shared.money import MONEY_UNDEFINED, Currency, Money
from gui.shared.tooltips.common import CURRENCY_SETTINGS, _getCurrencySetting
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES
from gui.shared.tooltips import formatters, contexts
from gui.shared.tooltips.vehicle import CommonStatsBlockConstructor
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms
from gui.shared.items_parameters import formatters as param_formatter, params_helper
_DT = DISCOUNT_TYPE
_VEHICLE_NATION_ICON_PATH = b'../maps/icons/filters/nations/%s.png'
_MAX_ITEMS_IN_TABLE = 3
_PRIORITY_FOR_FUTURE_ACTION = 4
_MULTIPLIER = b'Multiplier'
_ALL = b'All'
_PREMIUM_PACKET = b'premiumPacket'
_gold_bonus_list = (
 b'berthsPrices', b'premiumPacket1Cost',
 b'premiumPacket3Cost', b'premiumPacket7Cost',
 b'premiumPacket14Cost', b'premiumPacket30Cost',
 b'premiumPacket90Cost', b'premiumPacket180Cost',
 b'premiumPacket360Cost')

class ActionInfo(EventInfoModel):

    def __init__(self, event, actionData):
        super(ActionInfo, self).__init__(event)
        self.discount = actionData.discountObj
        self.priority = actionData.priority
        self.uiDecoration = actionData.uiDecoration
        self._compositionType = None
        self._id = b''
        self._maxDiscount = None
        self._packedDiscounts = None
        return

    @property
    def visualPriority(self):
        return self.priority

    @visualPriority.setter
    def visualPriority(self, value):
        self.priority = value
        return

    def getID(self):
        if not self._id:
            self._id = (b'/').join((self.event.getID(), self.discount.getName(), self.discount.getParamName()))
        return self._id

    def isAvailable(self):
        return (
         True, None)

    def isCompleted(self):
        return False

    def isOutOfDate(self):
        return False

    def getStartTime(self):
        return self.event.getStartTime()

    def getFinishTime(self):
        return self.event.getFinishTime()

    def getExactStartTime(self):
        return self.event.getData().get(b'startTime', time.time())

    def getExactFinishTime(self):
        return self.event.getData().get(b'finishTime', time.time())

    def getTitle(self):
        return self.event.getUserName()

    def getIsNew(self):
        return quest_settings.isNewCommonEvent(self)

    def getAutoDescription(self, useBigIco=False, forNormalCard=False):
        discountValue = self._getAutoDescriptionData(useBigIco)
        return self._getShortDescription(self.discount.getParamName(), discount=discountValue)

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        discount = self._getAdditionalDescriptionData(useBigIco)
        return self._getFullDescription(self.discount.getParamName(), discount, forHeroCard=forHeroCard)

    def getComingSoonDescription(self):
        return

    def getTooltipInfo(self):
        return self.event.getDescription()

    def isDiscountVisible(self):
        discount = self._getMaxDiscount()
        if discount:
            if discount.discountType == _DT.MULTIPLIER:
                return not (discount.discountValue == 0 or discount.discountValue == 1)
            return discount.discountValue > 0
        return False

    def getDiscount(self):
        discount = self._getMaxDiscount()
        if discount:
            return formatStrDiscount(discount)
        return b''

    def getBattleQuestsInfo(self):
        linkedQuests = self.event.linkedQuests
        if linkedQuests:
            return i18n.makeString(QUESTS.ACTION_LABEL_BATTLEQUESTS, count=len(linkedQuests))
        return b''

    def getLinkBtnLabel(self):
        return

    def getActionBtnLabel(self):
        return self._getButtonName(self.discount.getParamName())

    def getPicture(self):
        picture = getDecoration(self.uiDecoration)
        if picture:
            return {b'isWeb': True, 
               b'src': picture}
        paramName = self.discount.getParamName()
        if paramName.endswith(_MULTIPLIER):
            paramName = paramName[:-len(_MULTIPLIER)]
        return {b'isWeb': False, 
           b'src': (_PARAM_TO_IMG_DICT.get(paramName, b''))}

    def getTriggerChainID(self):
        raise NotImplementedError
        return

    def getTableData(self):
        return []

    def getActionTime(self):
        return {b'id': (self.getID()), 
           b'isTimeOver': (not self.event.isAvailable()[0]), 
           b'timeLeft': (self._getActiveTimeDateText()), 
           b'isShowTimeIco': (self._showTimerIco())}

    def setComposition(self, compositionType):
        self._compositionType = compositionType
        return

    def getMaxDiscountValue(self):
        maxDiscount = self._getMaxDiscount()
        if maxDiscount is not None:
            return maxDiscount.discountValue
        else:
            return 0

    def getExtraData(self):
        return

    def _showTimerIco(self):
        return self.event.getFinishTimeLeft() <= time_utils.ONE_DAY

    def _getActiveTimeDateText(self):
        timeStr = self._getActiveDateTimeString()
        return text_styles.stats(timeStr)

    def _getAutoDescription(self, stepName):
        formatter = (b'auto/{}').format(self.__modifyName(stepName))
        return i18n.makeString(QUESTS.getActionDescription(formatter))

    def _getFullDescription(self, stepName, discount=None, forHeroCard=False):
        modifiedStepName = self.__modifyName(stepName)
        locKey = None
        if forHeroCard:
            locKey = QUESTS.getActionDescription((b'hero/full/{}').format(modifiedStepName))
        if locKey is None:
            locKey = QUESTS.getActionDescription((b'full/{}').format(modifiedStepName))
        return i18n.makeString(locKey, discount=discount)

    def _getShortDescription(self, stepName, **kwargs):
        formatter = (b'short/{}').format(self.__modifyName(stepName))
        return i18n.makeString(QUESTS.getActionDescription(formatter), **kwargs)

    @classmethod
    def _getButtonName(cls, stepName):
        formatter = (b'button/{}').format(stepName)
        return i18n.makeString(QUESTS.getActionDescription(formatter))

    @classmethod
    def _formatPriceIcon(cls, item, useBigIco, forNormalCard=False):
        if hasattr(item, b'buyPrices'):
            sellGold = item.buyPrices.itemPrice.price.gold
            sellCredits = item.buyPrices.itemPrice.price.credits
            if sellGold:
                if forNormalCard:
                    return formatGoldPriceNormalCard(sellGold)
                if useBigIco:
                    return formatGoldPriceBig(sellGold)
                return formatGoldPrice(sellGold)
            if sellCredits:
                if forNormalCard:
                    return formatCreditPriceNormalCard(sellCredits)
                if useBigIco:
                    return formatCreditPriceBig(sellCredits)
                return formatCreditPrice(sellCredits)
        return b''

    @classmethod
    def _formatRentPriceIcon(cls, item, useBigIco, forNormalCard=False):
        if hasattr(item, b'minRentPrice'):
            rentPrice = item.minRentPrice.toDict()
            if rentPrice[Currency.GOLD]:
                if forNormalCard:
                    return formatGoldPriceNormalCard(rentPrice[Currency.GOLD])
                if useBigIco:
                    return formatGoldPriceBig(rentPrice[Currency.GOLD])
                return formatGoldPrice(rentPrice[Currency.GOLD])
            if rentPrice[Currency.CREDITS]:
                if forNormalCard:
                    return formatCreditPriceNormalCard(rentPrice[Currency.CREDITS])
                if useBigIco:
                    return formatCreditPriceBig(rentPrice[Currency.CREDITS])
                return formatCreditPrice(rentPrice[Currency.CREDITS])
        return b''

    def _getPackedDiscounts(self, sorting=False):
        if not self._packedDiscounts:
            self._packedDiscounts = {}
            for key, discount in viewitems(self.discount.packDiscounts(sorting=sorting)):
                if discount.discountType == _DT.MULTIPLIER and not (discount.discountValue == 0 or discount.discountValue == 1):
                    self._packedDiscounts[key] = discount
                elif discount.discountValue > 0:
                    self._packedDiscounts[key] = discount

        return self._packedDiscounts

    def _getMaxDiscount(self):
        if not self._maxDiscount:
            discounts = self._getPackedDiscounts(sorting=False)
            if discounts:
                self._maxDiscount = max(discounts.values(), key=operator.itemgetter(1))
        return self._maxDiscount

    def _getAutoDescriptionData(self, useBigIco=False):
        return self._getAdditionalDescriptionData(useBigIco)

    def _getAdditionalDescriptionData(self, useBigIco=False):
        discount = self._getMaxDiscount()
        if discount:
            return formatPercentValue(discount.discountValue)
        else:
            return

    def _formatFinishTime(self):
        return (b' ').join((text_styles.main(i18n.makeString(QUESTS.ACTION_TIME_FINISH)),
         backport.getShortDateFormat(self.getFinishTime())))

    def _getActiveDateTimeString(self):
        if self.event.getFinishTimeLeft() <= time_utils.ONE_DAY:
            gmtime = time.gmtime(self.event.getFinishTimeLeft())
            if gmtime.tm_hour > 0:
                fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLFINISH_LONGFORMAT)
            else:
                fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLFINISH_SHORTFORMAT)
            fmt %= {b'hours': (time.strftime(b'%H', gmtime)), 
               b'min': (time.strftime(b'%M', gmtime))}
            return (b' ').join((text_styles.main(i18n.makeString(QUESTS.ACTION_TIME_LEFT)), fmt))
        return self._formatFinishTime()

    def __modifyName(self, stepName):
        return self._compositionType or stepName


class EconomicsActionsInfo(ActionInfo):

    def getTriggerChainID(self):
        if b'winXPFactorMode' in self.discount.getParamName():
            return b'winXPFactorMode'
        return self.discount.getParamName()

    def getDiscount(self):
        paramName = self.discount.getParamName()
        if b'winXPFactorMode' in paramName:
            discount = self.__handleWinXPFactorMode()
        else:
            discounts = self._getPackedDiscounts()
            discount = discounts.get(paramName) if discounts else None
        if discount:
            return formatStrDiscount(discount)
        else:
            return b''

    def getActionBtnLabel(self):
        discountParamName = self.discount.getParamName()
        if discountParamName in (b'clanCreationCost',):
            return b''
        if _PREMIUM_PACKET in discountParamName:
            isPremium = getEconomicalStatsDict().get(b'isPremium', False)
            if isPremium:
                return self._getButtonName((b'{}/continue').format(_PREMIUM_PACKET))
            return self._getButtonName((b'{}/new').format(_PREMIUM_PACKET))
        return super(EconomicsActionsInfo, self).getActionBtnLabel()

    def getLinkBtnLabel(self):
        if self.discount.getParamName() == b'clanCreationCost':
            return self._getButtonName(self.discount.getParamName())
        return b''

    def _getAutoDescriptionData(self, useBigIco=False):
        paramName = self.discount.getParamName()
        if b'exchangeRate' in paramName:
            discountValue = self.__getExchangeRateBonusIco(useBigIco)
        elif paramName in (b'freeXPConversionDiscrecity', b'freeXPToTManXPRate'):
            discount = self._getMaxDiscount()
            discountValue = formatMultiplierValue(discount.discountValue)
        else:
            discountValue = self._getAdditionalDescriptionData(useBigIco)
        return discountValue

    def _getAdditionalDescriptionData(self, useBigIco=False):
        paramName = self.discount.getParamName()
        if paramName.endswith(_MULTIPLIER):
            paramName = paramName[:-len(_MULTIPLIER)]
        if b'winXPFactorMode' in paramName:
            discountValue = getEconomicalStatsDict().get(b'dailyXPFactor', None)
        elif b'exchangeRate' in paramName:
            discountValue = self.__getExchangeRateBonusIco()
        else:
            discountValue = getEconomicalStatsDict().get(paramName, None)
        if paramName in _gold_bonus_list:
            if useBigIco:
                discountValue = formatGoldPriceBig(discountValue)
            else:
                discountValue = formatGoldPrice(discountValue)
        if not discountValue:
            discount = self._getMaxDiscount()
            discountValue = formatPercentValue(discount.discountValue) if discount else None
        return discountValue

    def isDiscountVisible(self):
        paramName = self.discount.getParamName()
        if b'winXPFactorMode' in paramName:
            discount = self.__handleWinXPFactorMode()
        else:
            discount = self._getMaxDiscount()
        if discount:
            if discount.discountType == _DT.MULTIPLIER:
                return not (discount.discountValue == 0 or discount.discountValue == 1)
            return discount.discountValue > 0
        return False

    def __handleWinXPFactorMode(self):
        return self.discount.handlerWinXPFactorMode()

    def __getExchangeRateBonusIco(self, useBigIco=False):
        credit = getEconomicalStatsDict().get(b'exchangeRate')
        if useBigIco:
            goldIcon = formatGoldPriceBig(1)
            creditsIcon = formatCreditPriceBig(credit)
        else:
            goldIcon = formatGoldPrice(1)
            creditsIcon = formatCreditPrice(credit)
        return i18n.makeString(QUESTS.ACTION_EXCHANGERATE_GOLD2CREDIT, gold=goldIcon, credits=creditsIcon)


class VehPriceActionInfo(ActionInfo):
    _DEFAULT_MARGIN_AFTER_BLOCK = 10
    _DEFAULT_MARGIN_AFTER_SEPARATOR = 17

    def getTriggerChainID(self):
        return b'vehicleBuyPrice'

    def getAutoDescription(self, useBigIco=False, forNormalCard=False):
        vehs = self._getAdditionalDescriptionData(useBigIco, forNormalCard=forNormalCard)
        vehsLen = len(vehs)
        if vehsLen > 1:
            discValue = formatPercentValue(vehs[0][b'discount'])
            paramKey = b'two' if vehsLen == 2 else b'more'
            vehicles = (b', ').join((vehs[0][b'title'], vehs[1][b'title']))
        elif vehsLen == 1:
            discValue = vehs[0][b'price']
            paramKey = b'one'
            vehicles = vehs[0][b'title']
        else:
            return b''
        values = {b'vehicles': vehicles, 
           b'discount': discValue}
        paramName = (b'/').join((self.getTriggerChainID(), paramKey))
        return self._getShortDescription(paramName, **values)

    def getActionBtnLabel(self):
        return self._getButtonName(self.getTriggerChainID())

    def getPicture(self):
        picture = getDecoration(self.uiDecoration)
        if picture:
            return {b'isWeb': True, 
               b'src': picture}
        return {b'isWeb': False, 
           b'src': (_PARAM_TO_IMG_DICT.get(self.getTriggerChainID(), b''))}

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        vehiclesCount = len(self._getPackedDiscounts())
        if vehiclesCount > _MAX_ITEMS_IN_TABLE:
            return i18n.makeString(QUESTS.ACTION_DISCOUNT_MORE, deviceName=i18n.makeString(QUESTS.ACTION_MORE_TYPE_VEHICLES), count=vehiclesCount - _MAX_ITEMS_IN_TABLE)
        return b''

    def getTableData(self):
        result = []
        for item in self._sortVehicles():
            veh = item.discountName
            item = {b'icon': (_VEHICLE_NATION_ICON_PATH % nations.NAMES[veh.nationID]), 
               b'additionalIcon': (getTypeSmallIconPath(veh.type, veh.isPremium or veh.isElite)), 
               b'title': ((b' ').join((i18n.makeString(TOOLTIPS.level(veh.level)), veh.shortUserName))), 
               b'discount': (formatStrDiscount(item)), 
               b'price': (self._getPrice(veh, False))}
            result.append(item)

        return result

    def getExtraData(self):
        items = self._getAdditionalDescriptionData(useBigIco=True, addVehInfo=True)
        if len(items) == 1:
            return self.__getCardWithTTCForVehicle(items[0])
        else:
            return

    def _getAdditionalDescriptionData(self, useBigIco=False, addVehInfo=False, forNormalCard=False):
        result = []
        for item in self._sortVehicles():
            veh = item.discountName
            level = formatVehicleLevel(i18n.makeString(TOOLTIPS.level(veh.level)))
            item = {b'title': ((b' ').join((level, veh.shortUserName))), 
               b'discount': (item.discountValue), 
               b'price': (self._getPrice(veh, useBigIco, forNormalCard))}
            if addVehInfo:
                item.update({b'veh': veh})
            result.append(item)

        return result

    def _getPrice(self, veh, useBigIco, forNormalCard=False):
        return self._formatPriceIcon(veh, useBigIco, forNormalCard)

    def _sortVehicles(self):
        discountItems = self._getPackedDiscounts()
        return sorted(sorted(discountItems.values(), key=self._sortByNameFunc), key=self._sortByVehicleParams, reverse=True)[:3]

    @staticmethod
    def _sortByNameFunc(item):
        return item.discountName.shortUserName

    @staticmethod
    def _sortByVehicleParams(item):
        veh = item.discountName
        dscnt = item.discountValue
        return (dscnt, (veh.buyPrices.itemPrice.price.gold, veh.buyPrices.itemPrice.price.credits), veh.level)

    def _getPriceBlock(self, vehicle, configuration, valueWidth):
        block = []
        buyPrice = configuration.buyPrice
        if buyPrice:
            itemPrice = vehicle.buyPrices.itemPrice
            price = itemPrice.price
            actionPrc = itemPrice.getActionPrc()
            defaultPrice = itemPrice.defPrice
            currency = price.getCurrency()
            buyPriceValue = price.get(currency)
            oldPriceValue = defaultPrice.get(currency)
            block.append(self._makePriceBlock(oldPriceValue, CURRENCY_SETTINGS.getBuySetting(currency), percent=0, valueWidth=valueWidth))
            block.append(self._makePriceBlock(buyPriceValue, CURRENCY_SETTINGS.getBuySetting(currency), percent=actionPrc, valueWidth=valueWidth))
        return [
         formatters.packBuildUpBlockData(block, gap=2, padding=formatters.packPadding(top=-2))]

    def _makePriceBlock(self, price, currencySetting, percent=0, valueWidth=-1):
        _int = backport.getIntegralFormat
        hasAction = percent != 0
        settings = _getCurrencySetting(currencySetting)
        if settings is None:
            return
        else:
            valueFormatted = settings.textStyle(_int(price))
            if hasAction:
                settingsFrame = settings.frame
                if settingsFrame in Currency.ALL:
                    newPrice = MONEY_UNDEFINED.replace(settingsFrame, price)
                else:
                    newPrice = Money(credits=price)
                return formatters.packActionTextParameterBlockData(name=text_styles.main(_ms(TOOLTIPS.ACTIONPRICE_BUYPRICE_ACTIONPRICE, value=text_styles.expText(percent))), value=valueFormatted, icon=_getCurrencySetting(currencySetting).frame, padding=formatters.packPadding(left=20, bottom=-20), currency=newPrice.getCurrency(), valueWidth=valueWidth)
            return formatters.packTextParameterWithIconBlockData(name=text_styles.main(self._getDefaultPriceLabelConst()), value=valueFormatted, icon=settings.frame, valueWidth=valueWidth)

    def _getDefaultPriceLabelConst(self):
        return TOOLTIPS.ACTIONPRICE_BUYPRICE_DEFAULTPRICE

    def __getCardWithTTCForVehicle(self, vehItemDict):
        result = {}
        items = []
        context = contexts.ToolTipContext(None)
        statsConfig = context.getStatsConfiguration(vehItemDict[b'veh'])
        leftPadding = 20
        rightPadding = 20
        blockTopPadding = -4
        leftRightPadding = formatters.packPadding(left=leftPadding, right=rightPadding)
        blockPadding = formatters.packPadding(left=leftPadding, right=rightPadding, top=blockTopPadding)
        valueWidth = 75
        textGap = -2
        items.append(formatters.packBuildUpBlockData(self.__getHeaderBlock(vehItemDict), padding=leftRightPadding))
        items.append(formatters.packBuildUpBlockData(self._getPriceBlock(vehItemDict[b'veh'], statsConfig, valueWidth), gap=textGap, padding=blockPadding))
        items.append(formatters.packBuildUpBlockData(self.__getCommonStatsBlock(vehItemDict[b'veh']), gap=textGap, padding=blockPadding))
        result.update({b'blocksData': items, 
           b'marginAfterBlock': (self._DEFAULT_MARGIN_AFTER_BLOCK), 
           b'marginAfterSeparator': (self._DEFAULT_MARGIN_AFTER_SEPARATOR), 
           b'width': 600, 
           b'highlightType': (SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT)})
        return result

    def __getHeaderBlock(self, vehItemDict):
        block = []
        icon = getTypeBigIconPath(vehItemDict[b'veh'].type, vehItemDict[b'veh'].isElite)
        paramName = (b'/').join((self.getTriggerChainID(), b'one'))
        values = {b'vehicles': (vehItemDict[b'title']), 
           b'discount': (vehItemDict[b'price'])}
        titleDescr = text_styles.superPromoTitle(self._getShortDescription(paramName, **values))
        block.append(formatters.packImageTextBlockData(title=titleDescr, img=icon, imgPadding=formatters.packPadding(left=10, top=-15), txtGap=-6, txtOffset=84, padding=formatters.packPadding(top=15, bottom=-17)))
        return block

    def __getCommonStatsBlock(self, vehicle):
        block = []
        params = CommonStatsBlockConstructor.PARAMS
        paramsDict = params_helper.getParameters(vehicle)
        comparator = params_helper.similarCrewComparator(vehicle)
        for paramName in params.get(vehicle.type, ()):
            if paramName in paramsDict:
                paramInfo = comparator.getExtendedData(paramName)
                fmtValue = param_formatter.colorizedFormatParameter(paramInfo, None)
                if fmtValue is not None:
                    block.append(formatters.packTextParameterBlockData(name=param_formatter.formatVehicleParamName(paramName), value=fmtValue, valueWidth=80, padding=formatters.packPadding(left=-1)))

        return block


class VehRentActionInfo(VehPriceActionInfo):

    def getTriggerChainID(self):
        return b'vehicleRentPrice'

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        return self._getFullDescription(self.getTriggerChainID(), forHeroCard=forHeroCard)

    def getTableData(self):
        return

    def _getPrice(self, veh, useBigIco, forNormalCard=False):
        return self._formatRentPriceIcon(veh, useBigIco)

    def _calcDiscountValue(self, value, default):
        discount = float(value) / default * 100
        return int(discount)

    def _getPriceBlock(self, vehicle, configuration, valueWidth):
        block = []
        if vehicle.isRentAvailable and vehicle.isRentable:
            buyPrice = vehicle.buyPrices
            rentPackages = vehicle.rentPackages
            if buyPrice and rentPackages:
                itemPrice = vehicle.buyPrices.itemPrice
                price = itemPrice.price
                currency = price.getCurrency()
                buyPriceValue = price.get(currency)
                if vehicle.isDisabledForBuy is not True:
                    block.append(self._makePriceBlock(buyPriceValue, CURRENCY_SETTINGS.getBuySetting(currency), percent=itemPrice.getActionPrc(), valueWidth=valueWidth))
                for rent in rentPackages:
                    defaultPrice = rent.get(b'defaultRentPrice')
                    defaultPriceValue = defaultPrice.get(defaultPrice.getCurrency())
                    days = rent.get(b'days')
                    rentPrice = rent.get(b'rentPrice')
                    currency = rentPrice.getCurrency()
                    rentPriceValue = rentPrice.get(currency)
                    block.append(self.__makeRentBlock(rentPriceValue, CURRENCY_SETTINGS.getBuySetting(currency), days, percent=self._calcDiscountValue(rentPriceValue, defaultPriceValue)))

        return [formatters.packBuildUpBlockData(block, gap=2, padding=formatters.packPadding(top=-2))]

    @staticmethod
    def _sortByVehicleParams(item):
        veh = item.discountName
        dscnt = item.discountValue
        return (dscnt, (veh.minRentPrice.gold, veh.minRentPrice.credits), veh.level)

    def _getDefaultPriceLabelConst(self):
        return TOOLTIPS.ACTIONPRICE_RENTPRICE_DEFAULTPRICE

    def __makeRentBlock(self, price, currencySetting, days, percent=0):
        _int = backport.getIntegralFormat
        settings = _getCurrencySetting(currencySetting)
        if settings is None:
            return
        else:
            valueFormatted = settings.textStyle(_int(price))
            settingsFrame = settings.frame
            if settingsFrame in Currency.ALL:
                newPrice = MONEY_UNDEFINED.replace(settingsFrame, price)
            else:
                newPrice = Money(credits=price)
            if days == 1:
                text = text_styles.main(_ms(TOOLTIPS.ACTIONPRICE_RENTPRICE_1DAY, value=text_styles.expText(percent)))
            elif days == 3:
                text = text_styles.main(_ms(TOOLTIPS.ACTIONPRICE_RENTPRICE_3DAY, value=text_styles.expText(percent)))
            else:
                text = text_styles.main(_ms(TOOLTIPS.ACTIONPRICE_RENTPRICE_DAYS, days=days, value=text_styles.expText(percent)))
            return formatters.packActionTextParameterBlockData(name=text, value=valueFormatted, icon=_getCurrencySetting(currencySetting).frame, padding=formatters.packPadding(left=20, bottom=-20), currency=newPrice.getCurrency())


class EquipmentActionInfo(ActionInfo):

    def getTriggerChainID(self):
        return b'equipmentPrice'

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        equipCount = len(self._getPackedDiscounts())
        if equipCount > _MAX_ITEMS_IN_TABLE:
            return i18n.makeString(QUESTS.ACTION_DISCOUNT_MORE, deviceName=i18n.makeString(QUESTS.ACTION_MORE_TYPE_EQUIPMENT), count=equipCount - _MAX_ITEMS_IN_TABLE)
        return b''

    def getTableData(self):
        items = self._getPackedDiscounts()
        res = []
        for data in viewvalues(items):
            equip = data.discountName
            item = {b'icon': b'', 
               b'additionalIcon': b'', 
               b'title': ((b' ').join((icons.makeImageTag(equip.icon, vSpace=-3), equip.userName))), 
               b'discount': (formatStrDiscount(data)), 
               b'price': (self._formatPriceIcon(equip, False))}
            res.append(item)

        return res[:3]


class OptDeviceActionInfo(ActionInfo):

    def getTriggerChainID(self):
        return b'optionalDevicePrice'

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        optDeviceCount = len(self._getPackedDiscounts())
        if optDeviceCount > _MAX_ITEMS_IN_TABLE:
            return i18n.makeString(QUESTS.ACTION_DISCOUNT_MORE, deviceName=i18n.makeString(QUESTS.ACTION_MORE_TYPE_OPTIONALDEVICES), count=optDeviceCount - _MAX_ITEMS_IN_TABLE)
        return b''

    def getTableData(self):
        items = self._getPackedDiscounts()
        res = []
        for data in viewvalues(items):
            optDevice = data.discountName
            item = {b'icon': b'', 
               b'additionalIcon': b'', 
               b'title': ((b' ').join((icons.makeImageTag(optDevice.icon, vSpace=-3), optDevice.userName))), 
               b'discount': (formatStrDiscount(data)), 
               b'price': (self._formatPriceIcon(optDevice, False))}
            res.append(item)

        return sorted(res, key=(lambda x: x[b'discount']), reverse=True)[:3]


class ShellPriceActionInfo(ActionInfo):

    def getTriggerChainID(self):
        return b'shellsPrice'


class BoosterPriceActionInfo(ActionInfo):

    def getTriggerChainID(self):
        return b'goodiePrice'

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        boostersCount = len(self._getPackedDiscounts())
        if boostersCount > _MAX_ITEMS_IN_TABLE:
            return i18n.makeString(QUESTS.ACTION_DISCOUNT_MORE, deviceName=i18n.makeString(QUESTS.ACTION_MORE_TYPE_GOODIES), count=boostersCount - _MAX_ITEMS_IN_TABLE)
        return b''

    def getTableData(self):
        res = []
        for data in self.__sortBoosters():
            booster = data.discountName
            guiType = booster.boosterGuiType
            formatter = (b'booster/{}').format(guiType)
            busterName = i18n.makeString(QUESTS.getActionDescription(formatter))
            busterSmallIcon = RES_ICONS.getBusterSmallIcon(guiType)
            item = {b'icon': busterSmallIcon, 
               b'additionalIcon': b'', 
               b'title': busterName, 
               b'discount': (formatStrDiscount(data)), 
               b'price': (self._formatPriceIcon(booster, False))}
            res.append(item)

        return res

    def __sortBoosters(self):

        def __sortByNameFunc(item):
            return item.discountName.userName

        def __sortByParams(item):
            booster = item.discountName
            maxValues = booster.buyPrices.getMaxValuesAsMoney()
            discount = item.discountValue
            return (discount, tuple(maxValues.iterallitems(byWeight=True)))

        discountItems = self._getPackedDiscounts()
        return sorted(sorted(discountItems.values(), key=__sortByNameFunc), key=__sortByParams, reverse=True)[:3]


class C11nPriceGroupPriceActionInfo(ActionInfo):

    def getTriggerChainID(self):
        return b'c11nPrice'

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        itemsCount = len(self._getPackedDiscounts())
        if itemsCount > _MAX_ITEMS_IN_TABLE:
            return i18n.makeString(QUESTS.ACTION_DISCOUNT_MORE, deviceName=i18n.makeString(QUESTS.ACTION_MORE_TYPE_CUSTOMIZATIONS), count=itemsCount - _MAX_ITEMS_IN_TABLE)
        return b''

    def getTableData(self):
        items = self._getPackedDiscounts()
        res = []
        for data in viewvalues(items):
            c11n = data.discountName
            item = {b'icon': b'', 
               b'additionalIcon': b'', 
               b'title': ((b' ').join((c11n.userType, c11n.userName))), 
               b'discount': (formatStrDiscount(data)), 
               b'price': (self._formatPriceIcon(c11n, False))}
            res.append(item)

        return sorted(res, key=(lambda x: x[b'discount']), reverse=True)[:3]

    def getPicture(self):
        data = super(C11nPriceGroupPriceActionInfo, self).getPicture()
        if data.get(b'isWeb', False):
            return data
        paramName = self.discount.getParamName()
        if paramName.endswith(_ALL):
            itemTypeIDs = set(item.itemTypeID for _, item in self.discount.parse())
        else:
            itemTypeIDs = set(item.itemTypeID for item in self.discount.parse())
        if len(itemTypeIDs) == 1:
            paramName = GUI_ITEM_TYPE_NAMES[itemTypeIDs.pop()]
            image = RES_ICONS.getCustomActionImage(paramName)
        else:
            paramName = self.discount.getParamName()
            image = _PARAM_TO_IMG_DICT.get(paramName)
        return {b'isWeb': False, 
           b'src': image}


class ComingSoonActionInfo(ActionInfo):

    def __init__(self, info):
        self.__name = info[b'name']
        self.__startTime = info[b'startTime']
        self.__announceTime = info[b'announceTime']
        self.__params = info[b'params']
        super(ComingSoonActionInfo, self).__init__(object, ActionData(object, _PRIORITY_FOR_FUTURE_ACTION, 0))
        return

    def getID(self):
        return (b'/').join((self.__announceTime, self.__startTime, self._getParamName()))

    def getStartTime(self):
        return self.__startTime

    def getFinishTime(self):
        return

    def getActionTime(self):
        return {b'id': (self.getID()), 
           b'isTimeOver': False, 
           b'timeLeft': (self._getStartTime()), 
           b'isShowTimeIco': False}

    def getTriggerChainID(self):
        return

    def getPicture(self):
        picture = getDecoration(self.uiDecoration)
        if picture:
            return {b'isWeb': True, 
               b'src': picture}
        return {b'isWeb': False, 
           b'src': (_PARAM_TO_IMG_DICT.get(self._getParamName(), b''))}

    def getTitle(self):
        return i18n.makeString(QUESTS.ACTION_COMINGSOON_LABEL)

    def getIsNew(self):
        return False

    def getAutoDescription(self, useBigIco=False, forNormalCard=False):
        return

    def getAdditionalDescription(self, useBigIco=False, forHeroCard=False):
        return

    def getComingSoonDescription(self):
        return self._getAutoDescription(self._getParamName())

    def getTooltipInfo(self):
        return b''

    def getDiscount(self):
        return b''

    def getBattleQuestsInfo(self):
        return b''

    def getLinkBtnLabel(self):
        return

    def getActionBtnLabel(self):
        return

    def _getStartTime(self):
        startTimeStr = backport.getShortDateFormat(self.__startTime)
        if startTimeStr is not None:
            return text_styles.main(i18n.makeString(QUESTS.ACTION_COMINGSOON_TIME, startTime=startTimeStr))
        else:
            return b''

    def _getParamName(self):
        paramName = self.__name
        if b'Economics' in paramName:
            paramName = self.__params[0] if self.__params else b''
        for cur in Currency.ALL:
            if paramName.endswith(cur.capitalize()):
                paramName = paramName[:-len(cur)]

        if paramName.endswith(_MULTIPLIER):
            paramName = paramName[:-len(_MULTIPLIER)]
        return paramName


class MarathonEventActionInfo(ActionInfo):
    _marathonsCtrl = dependency.descriptor(IMarathonEventsController)

    def __init__(self, event, actionData):
        super(MarathonEventActionInfo, self).__init__(event, actionData)
        prefix = self.__getPrefix(event)
        if prefix is not None:
            self._marathonEvent = self._marathonsCtrl.getMarathon(prefix)
        else:
            self._marathonEvent = self._marathonsCtrl.getPrimaryMarathon()
        return

    def getTitle(self):
        if self._marathonEvent:
            return i18n.makeString(self._marathonEvent.data.quests.titleSetProgress)
        return b''

    def getAutoDescription(self, useBigIco=False, forNormalCard=False):
        if self._marathonEvent is None:
            return b''
        else:
            values = {b'level': (formatVehicleLevel(i18n.makeString(TOOLTIPS.level(8))))}
            name = self.discount.getParamName()
            if name == b'set_MarathonAnnounce':
                return i18n.makeString(self._marathonEvent.data.quests.autoSetAnnounce, **values)
            if name == b'set_MarathonInProgress':
                return i18n.makeString(self._marathonEvent.data.quests.autoSetProgress, **values)
            return i18n.makeString(self._marathonEvent.data.quests.autoSetFinished, **values)

    def _getFullDescription(self, stepName, discount=None, forHeroCard=False):
        if self._marathonEvent is None:
            return b''
        else:
            if stepName == b'set_MarathonFinished':
                locKey = R.strings.quests.action.hero.full.dyn(stepName)()
                return backport.text(locKey, value=self._marathonEvent.getExtraTimeToBuy())
            return super(MarathonEventActionInfo, self)._getFullDescription(stepName, discount, forHeroCard)

    def getDiscount(self):
        _ActionDiscountValue = namedtuple(b'_ActionDiscountValue', b'discountName, discountValue, discountType')
        return formatStrDiscount(_ActionDiscountValue(discountValue=100, discountType=DISCOUNT_TYPE.PERCENT, discountName=b'marathon'))

    def getTriggerChainID(self):
        return b'showMarathon'

    def isDiscountVisible(self):
        return self._marathonEvent and not self._marathonEvent.isRewardObtained()

    def _getActiveDateTimeString(self):
        name = self.discount.getParamName()
        if name == b'set_MarathonAnnounce':
            timeStr = backport.getLongDateFormat(self.getFinishTime())
            if timeStr is not None and self._marathonEvent:
                return text_styles.main(i18n.makeString(self._marathonEvent.data.quests.announceTime, startTime=timeStr))
        elif name == b'set_MarathonInProgress':
            return super(MarathonEventActionInfo, self)._getActiveDateTimeString()
        return b''

    def _formatFinishTime(self):
        if self._marathonEvent is None:
            return b''
        else:
            return (b' ').join((text_styles.main(i18n.makeString(self._marathonEvent.data.quests.timeFinish)),
             backport.getLongDateFormat(self.getFinishTime())))

    def _showTimerIco(self):
        name = self.discount.getParamName()
        if name == b'set_MarathonFinished':
            return False
        return self.event.getFinishTimeLeft() <= time_utils.ONE_DAY

    def __getPrefix(self, event):
        modifier = next(iter(event.getModifiers()), None)
        if modifier is not None:
            return modifier.getParams().get(b'prefix', None)
        else:
            return


def getEconomicalStatsDict():
    itemsCache = dependency.instance(IItemsCache)
    shop = itemsCache.items.shop
    slotPrices = shop.slotsPrices[1]
    slotPricesValue = slotPrices[0][1]
    return {b'exchangeRate': (shop.exchangeRate), b'slotsPrices': slotPricesValue, 
       b'berthsPrices': (shop.berthsPrices[2][0]), 
       b'premiumPacket1Cost': (shop.getPremiumPacketCost(1)), 
       b'premiumPacket3Cost': (shop.getPremiumPacketCost(3)), 
       b'premiumPacket7Cost': (shop.getPremiumPacketCost(7)), 
       b'premiumPacket14Cost': (shop.getPremiumPacketCost(14)), 
       b'premiumPacket30Cost': (shop.getPremiumPacketCost(30)), 
       b'premiumPacket90Cost': (shop.getPremiumPacketCost(90)), 
       b'premiumPacket180Cost': (shop.getPremiumPacketCost(180)), 
       b'premiumPacket360Cost': (shop.getPremiumPacketCost(360)), 
       b'winXPFactorMode': (shop.winXPFactorMode), 
       b'freeXPToTManXPRate': (shop.freeXPToTManXPRate), 
       b'dailyXPFactor': (shop.dailyXPFactor), 
       b'freeXPConversionDiscrecity': (shop.freeXPConversion[0]), 
       b'isPremium': (itemsCache.items.stats.isPremium)}


def getDecoration(uiDecoration):
    eventsCache = dependency.instance(IEventsCache)
    prefetcher = eventsCache.prefetcher
    return prefetcher.getMissionDecoration(uiDecoration, DECORATION_SIZES.DISCOUNT)


_PARAM_TO_IMG_DICT = {b'exchangeRate': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONVERT_GOLD), 
   b'paidRemovalCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_REMOVE_EQUIPMENT), 
   b'changeRoleCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CREW_CHANGE_MAIN_SKILL), 
   b'freeXPConversionDiscrecity': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONVERT_EXP), 
   b'slotsPrices': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SLOT), 
   b'berthsPrices': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PLACE_IN_BARRACKS), 
   b'goldTankmanCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CREW_EDUCATION), 
   b'creditsTankmanCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CREW_EDUCATION), 
   b'creditsDropSkillsCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CREW_SKILL_RESET), 
   b'goldDropSkillsCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CREW_SKILL_RESET), 
   b'premiumPacket1Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_1), 
   b'premiumPacket3Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_3), 
   b'premiumPacket7Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_7), 
   b'premiumPacket14Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_14), 
   b'premiumPacket30Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_30), 
   b'premiumPacket90Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_90), 
   b'premiumPacket180Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_180), 
   b'premiumPacket360Cost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_PREM_360), 
   b'winXPFactorMode/always': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_TANK_EXP), 
   b'winXPFactorMode/daily': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_TANK_EXP), 
   b'freeXPToTManXPRate': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CREW_EXP), 
   b'clanCreationCost': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CLAN), 
   b'vehicleBuyPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_VEHICLES), 
   b'vehicleRentPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_TANK_CLOCK), 
   b'equipment/goldPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONSUMABLES), 
   b'equipment/creditsPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONSUMABLES), 
   b'mul_EquipmentPriceAll': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONSUMABLES), 
   b'mul_EquipmentPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONSUMABLES), 
   b'set_EquipmentPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CONSUMABLES), 
   b'mul_OptionalDevicePriceAll': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_EQUIPMENT), 
   b'mul_OptionalDevicePrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_EQUIPMENT), 
   b'set_OptionalDevicePrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_EQUIPMENT), 
   b'shell/goldPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SHELLS), 
   b'shell/creditsPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SHELLS), 
   b'mul_ShellPriceAll': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SHELLS), 
   b'mul_ShellPriceNation': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SHELLS), 
   b'mul_ShellPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SHELLS), 
   b'set_ShellPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_SHELLS), 
   b'set_PriceGroupPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CUSTOM_MIXED), 
   b'mul_PriceGroupPrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CUSTOM_MIXED), 
   b'mul_PriceGroupPriceByTag': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CUSTOM_MIXED), 
   b'mul_PriceGroupPriceAll': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_CUSTOM_MIXED), 
   b'set_GoodiePrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_RESERVE), 
   b'mul_GoodiePrice': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_RESERVE), 
   b'mul_GoodiePriceAll': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_RESERVE), 
   b'tradeInSellPriceFactor': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_TRADE_IN), 
   b'set_MarathonAnnounce': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_MARATHON_ITALY), 
   b'set_MarathonInProgress': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_MARATHON_ITALY), 
   b'set_MarathonFinished': (RES_ICONS.MAPS_ICONS_ACTIONS_480X280_MARATHON_ITALY)}
_MODIFIERS_DICT = {b'mul_EconomicsParams': EconomicsActionsInfo, 
   b'set_EconomicsParams': EconomicsActionsInfo, 
   b'mul_EconomicsPrices': EconomicsActionsInfo, 
   b'set_EconomicsPrices': EconomicsActionsInfo, 
   b'set_VehPrice': VehPriceActionInfo, 
   b'mul_VehPriceNation': VehPriceActionInfo, 
   b'mul_VehPriceAll': VehPriceActionInfo, 
   b'cond_VehPrice': VehPriceActionInfo, 
   b'mul_VehPrice': VehPriceActionInfo, 
   b'set_VehRentPrice': VehRentActionInfo, 
   b'mul_VehRentPriceNation': VehRentActionInfo, 
   b'mul_VehRentPriceAll': VehRentActionInfo, 
   b'mul_VehRentPrice': VehRentActionInfo, 
   b'cond_VehRentPrice': VehRentActionInfo, 
   b'mul_EquipmentPriceAll': EquipmentActionInfo, 
   b'mul_EquipmentPrice': EquipmentActionInfo, 
   b'set_EquipmentPrice': EquipmentActionInfo, 
   b'mul_OptionalDevicePriceAll': OptDeviceActionInfo, 
   b'mul_OptionalDevicePrice': OptDeviceActionInfo, 
   b'set_OptionalDevicePrice': OptDeviceActionInfo, 
   b'mul_ShellPriceAll': ShellPriceActionInfo, 
   b'set_ShellPrice': ShellPriceActionInfo, 
   b'mul_ShellPriceNation': ShellPriceActionInfo, 
   b'mul_ShellPrice': ShellPriceActionInfo, 
   b'set_PriceGroupPrice': C11nPriceGroupPriceActionInfo, 
   b'mul_PriceGroupPrice': C11nPriceGroupPriceActionInfo, 
   b'mul_PriceGroupPriceByTag': C11nPriceGroupPriceActionInfo, 
   b'mul_PriceGroupPriceAll': C11nPriceGroupPriceActionInfo, 
   b'set_GoodiePrice': BoosterPriceActionInfo, 
   b'mul_GoodiePrice': BoosterPriceActionInfo, 
   b'mul_GoodiePriceAll': BoosterPriceActionInfo, 
   b'set_MarathonAnnounce': MarathonEventActionInfo, 
   b'set_MarathonInProgress': MarathonEventActionInfo, 
   b'set_MarathonFinished': MarathonEventActionInfo}

def getModifierObj(name, event, modifier):
    if name in _MODIFIERS_DICT:
        return _MODIFIERS_DICT[name](event, modifier)
    else:
        return


def getActionInfoData(event):
    if event.getType() == constants.EVENT_TYPE.ACTION:
        return _parseAction(event)
    return []


def getAnnouncedActionInfo(info):
    return ComingSoonActionInfo(info)


def _parseAction(event):
    modifiers = event.getActions()
    for modifierName, modifierData in viewitems(modifiers):
        for actionData in modifierData:
            modifier = getModifierObj(modifierName, event, actionData)
            if modifier is not None:
                yield modifier

    return
