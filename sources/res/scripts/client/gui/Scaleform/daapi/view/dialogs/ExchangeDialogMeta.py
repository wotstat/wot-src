import math, operator, Event
from adisp import adisp_async, adisp_process
from gui import DialogsInterface
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.Scaleform.daapi.view.lobby.exchange.detailed_exchange_xp_dialog import ExchangeDetailedXPDialogMeta
from gui.techtree.settings import UnlockStats
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.genConsts.CONFIRM_EXCHANGE_DIALOG_TYPES import CONFIRM_EXCHANGE_DIALOG_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES
from gui.Scaleform.genConsts.TEXT_MANAGER_STYLES import TEXT_MANAGER_STYLES
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.managers.ColorSchemeManager import ColorSchemeManager
from gui.impl import backport
from gui.shared import events
from gui.shared.formatters import icons, text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.processors import makeError
from gui.shared.gui_items.processors.common import GoldToCreditsExchanger
from gui.shared.money import Currency, Money
from gui.shared.utils import decorators
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import i18n, dependency
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache
STEP_SIZE = 1
I18N_NEEDGOLDTEXT_KEY = b'{0:>s}/needGoldText'
I18N_NEEDITEMSTEXT_KEY = b'{0:>s}/needItemsText'
I18N_GOLDNOTENOUGHTEXT_KEY = b'{0:>s}/goldNotEnoughText'
I18N_EXCHANGENONEEDTEXT_KEY = b'{0:>s}/exchangeNoNeedText'
I18N_NEEDITEMSSTEPPERTITLE_KEY = b'{0:>s}/needItemsStepperTitle'
TEXT_COLOR_ID_XP = b'textColorXp'
TEXT_COLOR_ID_CREDITS = b'textColorCredits'

class InfoItemBase(object):

    @property
    def itemTypeName(self):
        raise NotImplementedError()
        return

    @property
    def userName(self):
        raise NotImplementedError()
        return

    @property
    def itemTypeID(self):
        raise NotImplementedError()
        return

    def getExtraIconInfo(self):
        raise NotImplementedError()
        return

    def getGUIEmblemID(self):
        raise NotImplementedError()
        return


class _ExchangeSubmitterBase(object):

    def __init__(self, exchangeItem):
        self._exchangeItem = exchangeItem
        return

    @property
    def type(self):
        return self._getType()

    @property
    def infoItem(self):
        return self._getInfoItem()

    @property
    def exchangeRate(self):
        return self._getExchangeRate()

    @property
    def defaultExchangeRate(self):
        return self._getDefaultExchangeRate()

    @property
    def resourceToExchange(self):
        return self._getResourceToExchange()

    @property
    def currencyIconStr(self):
        return self._getCurrencyIconStr()

    @property
    def currencyIconPath(self):
        return self._getCurrencyIconPath()

    @property
    def currencyFormat(self):
        return self._getCurrencyFormat()

    @property
    def colorScheme(self):
        return self._getColorScheme()

    @property
    def rateToColorScheme(self):
        return self._getRateToColorScheme()

    @property
    def exchangeRateItemsIcon(self):
        return self._getExchangeRateItemsIcon()

    @property
    def maxExchangeValue(self):
        return self._getMaxExchangeValue()

    @property
    def itemCD(self):
        return self._exchangeItem.itemCD

    def destroy(self):
        return

    def submit(self, gold, valueToExchange, callback=None):
        raise NotImplementedError()
        return

    def _getType(self):
        raise NotImplementedError()
        return

    def _getInfoItem(self):
        raise NotImplementedError()
        return

    def _getExchangeRate(self):
        raise NotImplementedError()
        return

    def _getDefaultExchangeRate(self):
        raise NotImplementedError()
        return

    def _getResourceToExchange(self):
        raise NotImplementedError()
        return

    def _getCurrencyIconStr(self):
        raise NotImplementedError()
        return

    def _getCurrencyIconPath(self):
        raise NotImplementedError()
        return

    def _getCurrencyFormat(self):
        raise NotImplementedError()
        return

    def _getColorScheme(self):
        raise NotImplementedError()
        return

    def _getRateToColorScheme(self):
        raise NotImplementedError()
        return

    def _getExchangeRateItemsIcon(self):
        raise NotImplementedError()
        return

    def _getMaxExchangeValue(self):
        raise NotImplementedError()
        return


class _ExchangeDialogMeta(I18nConfirmDialogMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    wallet = dependency.descriptor(IWalletController)

    def __init__(self, submitterParams, key):
        self.__submitter = self._getSubmitterType()(submitterParams)
        self.onInvalidate = Event.Event()
        self.onCloseDialog = Event.Event()
        self.colorManager = ColorSchemeManager()
        super(_ExchangeDialogMeta, self).__init__(key, scope=ScopeTemplates.LOBBY_SUB_SCOPE)
        self.wallet.onWalletStatusChanged += self._onStatsChanged
        return

    def destroy(self):
        self.wallet.onWalletStatusChanged -= self._onStatsChanged
        self.onInvalidate.clear()
        self.onCloseDialog.clear()
        self.__submitter.destroy()
        return

    @adisp_async
    @adisp_process
    def submit(self, gold, valueToExchange, callback=None):
        submitter = self._getSubmitter()
        result = yield submitter.submit(gold, valueToExchange)
        if callback is not None:
            callback(result)
        return

    def getType(self):
        submitter = self._getSubmitter()
        return submitter.type

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_EXCHANGE_DIALOG

    def getExchangeRate(self):
        submitter = self._getSubmitter()
        return submitter.exchangeRate

    def getTypeCompDescr(self):
        submitter = self._getSubmitter()
        return submitter.itemCD

    def makeVO(self):
        submitter = self._getSubmitter()
        item = submitter.infoItem
        resToExchange = submitter.resourceToExchange
        state, stateMsg = self._getState(resToExchange)
        return {b'title': (self.getTitle()), 
           b'exchangeBtnText': (self.getButtonLabels()[0][b'label']), 
           b'cancelBtnText': (self.getButtonLabels()[1][b'label']), 
           b'state': state, 
           b'lockExchangeMessage': stateMsg, 
           b'iconExtraInfo': (item.getExtraIconInfo()), 
           b'iconModuleType': (item.itemTypeName), 
           b'icon': (self._getItemIcon(item)), 
           b'iconType': (self._getItemIconType(item)), 
           b'itemName': (text_styles.middleTitle(item.userName)), 
           b'needItemsText': (self._getResourceToExchangeTxt(resToExchange)), 
           b'needGoldText': (self._getGoldToExchangeTxt(resToExchange)), 
           b'exchangeBlockData': (self._getExchangeBlockData(resToExchange))}

    def _getSubmitterType(self):
        raise NotImplementedError()
        return

    def _getSubmitter(self):
        return self.__submitter

    def _onStatsChanged(self, *args):
        self.onInvalidate()
        return

    def _getRGB(self, colorId):
        return self.colorManager.getColorScheme(colorId).get(b'rgb')

    def _makeString(self, key, ctx=None):
        ctx = ctx or {}
        i18nKey = key.format(self._key)
        return super(_ExchangeDialogMeta, self)._makeString(i18nKey, ctx)

    def _getExchangeBlockData(self, resToExchange):
        submitter = self._getSubmitter()
        goldStepperTitleStr = i18n.makeString(DIALOGS.CONFIRMEXCHANGEDIALOG_GOLDITEMSSTEPPERTITLE)
        goldStepperTitleFmt = text_styles.main(goldStepperTitleStr)
        needItemsStepperTitle = text_styles.main(self._makeString(I18N_NEEDITEMSSTEPPERTITLE_KEY))
        return {b'goldStepperTitle': goldStepperTitleFmt, 
           b'needItemsIcon': (submitter.currencyIconPath), 
           b'needItemsStepperTitle': needItemsStepperTitle, 
           b'goldIcon': (RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2), 
           b'defaultExchangeRate': (submitter.defaultExchangeRate), 
           b'exchangeRate': (submitter.exchangeRate), 
           b'defaultGoldValue': (self._getGoldToExchange(resToExchange)), 
           b'goldStepSize': STEP_SIZE, 
           b'maxGoldValue': (submitter.maxExchangeValue), 
           b'goldTextColorId': (TEXT_MANAGER_STYLES.GOLD_TEXT), 
           b'itemsTextColorId': (submitter.colorScheme), 
           b'exchangeHeaderData': {b'labelText': (MENU.EXCHANGE_RATE), 
                                   b'rateFromIcon': (ICON_TEXT_FRAMES.GOLD), 
                                   b'rateToIcon': (submitter.exchangeRateItemsIcon), 
                                   b'rateFromTextColor': (self._getRGB(TEXT_COLOR_ID_XP)), 
                                   b'rateToTextColor': (self._getRGB(submitter.rateToColorScheme))}}

    def _getState(self, resToExchange):
        if resToExchange <= 0:
            return (
             CONFIRM_EXCHANGE_DIALOG_TYPES.EXCHANGE_NOT_NEEED_STATE,
             text_styles.success(self._makeString(I18N_EXCHANGENONEEDTEXT_KEY)))
        if not self._isEnoughGold(resToExchange):
            goldToExchange = self._getGoldToExchange(resToExchange)
            fmtGold = (b'').join((text_styles.gold(backport.getGoldFormat(goldToExchange)), icons.gold()))
            return (
             CONFIRM_EXCHANGE_DIALOG_TYPES.NOT_ENOUGH_GOLD_STATE,
             text_styles.error(self._makeString(I18N_GOLDNOTENOUGHTEXT_KEY, {b'gold': fmtGold})))
        return (
         CONFIRM_EXCHANGE_DIALOG_TYPES.NORMAL_STATE, b'')

    def _isEnoughGold(self, resToExchange):
        return self._getGoldToExchange(resToExchange) <= self.itemsCache.items.stats.gold

    def _getResourceToExchangeTxt(self, resToExchange):
        if resToExchange > 0:
            resource = backport.getIntegralFormat(resToExchange)
            submitter = self._getSubmitter()
            resStr = submitter.currencyFormat(resource) + submitter.currencyIconStr
            return text_styles.error(self._makeString(I18N_NEEDITEMSTEXT_KEY, {b'value': resStr}))
        return b''

    def _getGoldToExchangeTxt(self, resToExchange):
        if resToExchange > 0:
            goldToExchange = self._getGoldToExchange(resToExchange)
            fmtGold = (b'').join((text_styles.gold(backport.getGoldFormat(goldToExchange)), icons.gold()))
            return text_styles.main(self._makeString(I18N_NEEDGOLDTEXT_KEY, {b'gold': fmtGold}))
        return b''

    def _getGoldToExchange(self, resToExchange):
        if resToExchange > 0:
            submitter = self._getSubmitter()
            return int(math.ceil(float(resToExchange) / submitter.exchangeRate))
        return 0

    def _getItemIconType(self, item):
        if item.itemTypeID == GUI_ITEM_TYPE.VEHICLE:
            return CONFIRM_EXCHANGE_DIALOG_TYPES.VEHICLE_ICON
        return CONFIRM_EXCHANGE_DIALOG_TYPES.MODULE_ICON

    def _getItemIcon(self, item):
        if item.itemTypeID == GUI_ITEM_TYPE.VEHICLE:
            icon = item.type
            if item.isElite:
                icon += b'_elite'
            return icon
        return item.getGUIEmblemID()
        return


class _ExchangeItem(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, cd, count=1):
        super(_ExchangeItem, self).__init__()
        self._cd = cd
        self._count = count
        return

    @property
    def itemCD(self):
        return self._cd

    @property
    def count(self):
        return self._count

    @property
    def infoItem(self):
        return self._getInfoItem()

    def doAction(self, action, resultType):
        raise NotImplementedError
        return

    def _getInfoItem(self):
        raise NotImplementedError
        return


class _SingleExchangeItem(_ExchangeItem):

    def doAction(self, action, resultType):
        return action(self._cd)

    def _getInfoItem(self):
        item = self.itemsCache.items.getItemByCD(self._cd)
        return item


class _MultipleExchangeItem(_ExchangeItem):

    def __init__(self, itemsCDs, infoItem):
        super(_MultipleExchangeItem, self).__init__(itemsCDs)
        self.__infoItem = infoItem
        return

    def doAction(self, action, resultType):
        return sum([action(itemCD) for itemCD in self._cd], resultType())

    def _getInfoItem(self):
        return self.__infoItem


class _WebProductInfoItem(InfoItemBase):

    def __init__(self, name):
        self.__name = name
        return

    @property
    def itemTypeName(self):
        return b''

    @property
    def itemTypeID(self):
        return

    @property
    def userName(self):
        return self.__name

    def getExtraIconInfo(self):
        return

    def getGUIEmblemID(self):
        return b'notFound'


class _WebProductExchangeItem(_ExchangeItem):

    def __init__(self, price, count, infoItem):
        super(_WebProductExchangeItem, self).__init__(None, count)
        self.__infoItem = infoItem
        self.__price = price
        return

    @property
    def price(self):
        return self.__price

    def _getInfoItem(self):
        return self.__infoItem

    def doAction(self, action, resultType):
        return


class _SlotInfoItem(InfoItemBase):

    def __init__(self, name):
        self.__name = name
        return

    @property
    def itemTypeName(self):
        return b''

    @property
    def itemTypeID(self):
        return

    @property
    def userName(self):
        return self.__name

    def getExtraIconInfo(self):
        return

    def getGUIEmblemID(self):
        return b'slots'


class _BerthsInfoItem(InfoItemBase):

    def __init__(self, name):
        self.__name = name
        return

    @property
    def itemTypeName(self):
        return b''

    @property
    def itemTypeID(self):
        return

    @property
    def userName(self):
        return self.__name

    def getExtraIconInfo(self):
        return

    def getGUIEmblemID(self):
        return b'crew'


class _SlotExchangeItem(_ExchangeItem):

    def __init__(self, price, count, infoItem):
        super(_SlotExchangeItem, self).__init__(None, count)
        self.__infoItem = infoItem
        self.__price = price
        return

    @property
    def price(self):
        return self.__price

    def _getInfoItem(self):
        return self.__infoItem

    def doAction(self, action, resultType):
        return


class _BerthsExchangeItem(_ExchangeItem):

    def __init__(self, price, infoItem):
        super(_BerthsExchangeItem, self).__init__(None)
        self.__infoItem = infoItem
        self.__price = price
        return

    @property
    def price(self):
        return self.__price

    def _getInfoItem(self):
        return self.__infoItem

    def doAction(self, action, resultType):
        return


class _ExchangeCreditsSubmitter(_ExchangeSubmitterBase):
    itemsCache = dependency.descriptor(IItemsCache)

    @adisp_async
    @decorators.adisp_process(b'transferMoney')
    def submit(self, gold, valueToExchange, callback=None):
        result = yield GoldToCreditsExchanger(gold).request()
        if callback is not None:
            callback(result)
        return

    def _getType(self):
        return CONFIRM_EXCHANGE_DIALOG_TYPES.TYPE_CREDITS_EXCHANGE

    def _getInfoItem(self):
        return self._exchangeItem.infoItem

    def _getExchangeRate(self):
        return self.itemsCache.items.shop.exchangeRate

    def _getDefaultExchangeRate(self):
        return self.itemsCache.items.shop.defaults.exchangeRate

    def _getResourceToExchange(self):

        def _getPrice(itemCD):
            item = self.itemsCache.items.getItemByCD(itemCD)
            return item.buyPrices.itemPrice.price

        price = self._exchangeItem.doAction(_getPrice, Money)
        return price.get(Currency.CREDITS, 0) * self._exchangeItem.count - self.itemsCache.items.stats.credits

    def _getCurrencyIconStr(self):
        return icons.credits()

    def _getCurrencyIconPath(self):
        return RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2

    def _getCurrencyFormat(self):
        return text_styles.credits

    def _getColorScheme(self):
        return TEXT_MANAGER_STYLES.CREDITS_TEXT

    def _getRateToColorScheme(self):
        return TEXT_COLOR_ID_CREDITS

    def _getExchangeRateItemsIcon(self):
        return ICON_TEXT_FRAMES.CREDITS

    def _getMaxExchangeValue(self):
        return self.itemsCache.items.stats.actualGold


class _ExchangeCreditsSubscriber(object):

    def __init__(self):
        super(_ExchangeCreditsSubscriber, self).__init__()
        g_clientUpdateManager.addMoneyCallback(self._onStatsChanged)
        g_clientUpdateManager.addCallback(b'shop.exchangeRate', self._onStatsChanged)
        return

    def destroy(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def _onStatsChanged(self, *args):
        raise NotImplementedError()
        return


class ExchangeCreditsSingleItemMeta(_ExchangeDialogMeta, _ExchangeCreditsSubscriber):

    def __init__(self, itemCD, installVehicle=None, key=b'confirmExchangeDialog/exchangeCredits', count=1):
        super(ExchangeCreditsSingleItemMeta, self).__init__(_SingleExchangeItem(itemCD, count=count), key=key)
        submitter = self._getSubmitter()
        item = self.itemsCache.items.getItemByCD(submitter.itemCD)
        self.__installVehicleCD = installVehicle
        self.__isInstalled = False
        if item and item.itemTypeID != GUI_ITEM_TYPE.VEHICLE and self.__installVehicleCD:
            vehicle = self.itemsCache.items.getItemByCD(self.__installVehicleCD)
            self.__isInstalled = item.isInstalled(vehicle)
        self.__inventoryCount = 0
        if item:
            self.__inventoryCount = item.inventoryCount
        g_clientUpdateManager.addCallback(b'inventory.1', self.__checkInventory)
        return

    def destroy(self):
        self.__inventoryCount = None
        self.__installVehicleCD = None
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(ExchangeCreditsSingleItemMeta, self).destroy()
        return

    def _getSubmitterType(self):
        return _ExchangeCreditsSubmitter

    def __checkInventory(self, *args):
        submitter = self._getSubmitter()
        item = self.itemsCache.items.getItemByCD(submitter.itemCD)
        if item is not None:
            if item.itemTypeID == GUI_ITEM_TYPE.VEHICLE and item.isInInventory or item.inventoryCount > self.__inventoryCount:
                self.onCloseDialog()
            elif self.__installVehicleCD:
                vehicle = self.itemsCache.items.getItemByCD(self.__installVehicleCD)
                if not self.__isInstalled and item.isInstalled(vehicle):
                    self.onCloseDialog()
        return


class ExchangeCreditsSingleItemModalMeta(ExchangeCreditsSingleItemMeta):

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_EXCHANGE_DIALOG_MODAL


class ExchangeCreditsMultiItemsMeta(_ExchangeDialogMeta, _ExchangeCreditsSubscriber):

    def __init__(self, itemsCDs, infoItem, key=b'confirmExchangeDialog/exchangeCredits'):
        super(ExchangeCreditsMultiItemsMeta, self).__init__(_MultipleExchangeItem(itemsCDs, infoItem), key)
        return

    def _getSubmitterType(self):
        return _ExchangeCreditsSubmitter


class _ExchangeCreditsForSlotSubmitter(_ExchangeCreditsSubmitter):

    def _getResourceToExchange(self):
        return self._exchangeItem.count * self._exchangeItem.price - self.itemsCache.items.stats.credits


class ExchangeCreditsForSlotMeta(_ExchangeDialogMeta, _ExchangeCreditsSubscriber):

    def __init__(self, name, count, price, key=b'confirmExchangeDialog/exchangeCredits'):
        infoItem = _SlotInfoItem(name)
        super(ExchangeCreditsForSlotMeta, self).__init__(_SlotExchangeItem(price, count, infoItem), key)
        return

    def _getSubmitterType(self):
        return _ExchangeCreditsForSlotSubmitter


class ExchangeCreditsForBerthsMeta(_ExchangeDialogMeta, _ExchangeCreditsSubscriber):

    def __init__(self, name, price, key=b'confirmExchangeDialog/exchangeCredits'):
        infoItem = _BerthsInfoItem(name)
        super(ExchangeCreditsForBerthsMeta, self).__init__(_BerthsExchangeItem(price, infoItem), key)
        return

    def _getSubmitterType(self):
        return _ExchangeCreditsForSlotSubmitter

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_EXCHANGE_BERTHS_DIALOG


class _WebProductCreditsExchangeSubmitter(_ExchangeCreditsSubmitter):

    def _getResourceToExchange(self):
        return self._exchangeItem.count * self._exchangeItem.price - self.itemsCache.items.stats.credits


class ExchangeCreditsWebProductMeta(_ExchangeDialogMeta, _ExchangeCreditsSubscriber):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, name, count, price, key=b'confirmExchangeDialog/exchangeCredits'):
        infoItem = _WebProductInfoItem(name)
        super(ExchangeCreditsWebProductMeta, self).__init__(_WebProductExchangeItem(price, count, infoItem), key)
        return

    def _getItemIconType(self, item):
        return CONFIRM_EXCHANGE_DIALOG_TYPES.PLATFORM_PACK_ICON

    def _getSubmitterType(self):
        return _WebProductCreditsExchangeSubmitter


class _RestoreExchangeCreditsSubmitter(_ExchangeCreditsSubmitter):

    def _getResourceToExchange(self):

        def _getRestorePrice(itemCD):
            item = self.itemsCache.items.getItemByCD(itemCD)
            return item.restorePrice.getSignValue(Currency.CREDITS)

        credit = self._exchangeItem.doAction(_getRestorePrice, Money)
        return credit - self.itemsCache.items.stats.credits


class RestoreExchangeCreditsMeta(ExchangeCreditsSingleItemMeta):

    def __init__(self, itemCD, key=b'confirmExchangeDialog/restoreExchangeCredits'):
        super(RestoreExchangeCreditsMeta, self).__init__(itemCD, key=key)
        return

    def _getSubmitterType(self):
        return _RestoreExchangeCreditsSubmitter


class _ExchangeXpSubmitter(_ExchangeSubmitterBase):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, submitterParams):
        exchangeItem, parentCD, xpCost = submitterParams
        super(_ExchangeXpSubmitter, self).__init__(exchangeItem)
        self._parentCD = parentCD
        self._xpCost = xpCost
        return

    def destroy(self):
        self._parentCD = None
        self._xpCost = None
        return

    @adisp_async
    @adisp_process
    def submit(self, gold, xpToExchange, callback=None):
        isOk, result, xpExchanged = yield DialogsInterface.showDialog(ExchangeDetailedXPDialogMeta(xpToExchange))
        if xpExchanged < xpToExchange:
            result = makeError(auxData=[result])
        if callback is not None:
            callback(result if isOk else None)
        return

    def _getType(self):
        return CONFIRM_EXCHANGE_DIALOG_TYPES.TYPE_XP_EXCHANGE

    def _getInfoItem(self):
        return self._exchangeItem.infoItem

    def _getExchangeRate(self):
        return self.itemsCache.items.shop.freeXPConversion[0]

    def _getDefaultExchangeRate(self):
        return self.itemsCache.items.shop.defaults.freeXPConversion[0]

    def _getResourceToExchange(self):

        def _getUnlockState(itemCD):
            item = self.itemsCache.items.getItemByCD(itemCD)
            return item.isUnlocked

        unlockState = self._exchangeItem.doAction(_getUnlockState, bool)
        if unlockState:
            return 0
        stats = self.itemsCache.items.stats
        unlockStats = UnlockStats(stats.unlocks, stats.vehiclesXPs, stats.freeXP)
        return self._xpCost - unlockStats.getVehTotalXP(self._parentCD)

    def _getCurrencyIconStr(self):
        return icons.freeXP()

    def _getCurrencyIconPath(self):
        return RES_ICONS.MAPS_ICONS_LIBRARY_ELITEXPICON_2

    def _getCurrencyFormat(self):
        return text_styles.expText

    def _getColorScheme(self):
        return TEXT_MANAGER_STYLES.STATS_TEXT

    def _getRateToColorScheme(self):
        return TEXT_COLOR_ID_XP

    def _getExchangeRateItemsIcon(self):
        return ICON_TEXT_FRAMES.ELITE_XP

    def _getMaxExchangeValue(self):
        eliteVehicles = self.itemsCache.items.getVehicles(REQ_CRITERIA.VEHICLE.FULLY_ELITE).values()
        result = sum(map(operator.attrgetter(b'xp'), eliteVehicles))
        return min(int(result / self.exchangeRate), self.itemsCache.items.stats.actualGold)


class ExchangeXpMeta(_ExchangeDialogMeta):

    def __init__(self, itemCD, parentCD, xpCost):
        super(ExchangeXpMeta, self).__init__((_SingleExchangeItem(itemCD), parentCD, xpCost), key=b'confirmExchangeDialog/exchangeXp')
        g_clientUpdateManager.addCurrencyCallback(Currency.GOLD, self._onStatsChanged)
        g_clientUpdateManager.addCallbacks({b'shop.freeXPConversion': (self._onStatsChanged), 
           b'inventory.1': (self._onStatsChanged), 
           b'stats.vehTypeXP': (self._onStatsChanged), 
           b'stats.freeXP': (self._onStatsChanged), 
           b'stats.unlocks': (self.__checkUnlocks)})
        return

    def destroy(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(ExchangeXpMeta, self).destroy()
        return

    def _getSubmitterType(self):
        return _ExchangeXpSubmitter

    def __checkUnlocks(self, *args):
        submitter = self._getSubmitter()
        item = self.itemsCache.items.getItemByCD(submitter.itemCD)
        if item is not None and item.isUnlocked:
            self.onCloseDialog()
        return
