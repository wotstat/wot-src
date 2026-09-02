import logging
from collections import namedtuple
from adisp import adisp_process
from constants import GameSeasonType, RentType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import makeBrowserParams
from gui.Scaleform.daapi.view.lobby.store.browser import shop_helpers as helpers
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.game_control.links import URLMacros
from gui.impl.gen import R
from gui.shared import events, g_eventBus
from gui.shared.economics import getGUIPrice
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import ITradeInController
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)
_ProductInfo = namedtuple(b'_ProductInfo', (b'price', b'href', b'method'))
SHOP_RENT_TYPE_MAP = {(RentType.NO_RENT): b'none', 
   (RentType.TIME_RENT): b'time', 
   (RentType.BATTLES_RENT): b'battles', 
   (RentType.WINS_RENT): b'wins', 
   (RentType.SEASON_RENT): b'season', 
   (RentType.SEASON_CYCLE_RENT): b'cycle'}
SHOP_RENT_SEASON_TYPE_MAP = {(GameSeasonType.NONE): b'none', 
   (GameSeasonType.RANKED): b'ranked', 
   (GameSeasonType.EPIC): b'frontline'}

class _GoldPurchaseReason(object):
    VEHICLE = b'vehicle'
    RENT = b'rent'
    XP = b'experience'
    SLOT = b'slot'
    BERTH = b'barracks'
    CREW = b'crew'
    EQUIPMENT = b'equipment'
    CUSTOMIZATION = b'customization'
    BUNDLE = b'bundle'
    BATTLE_PASS = b'battle_pass'
    BATTLE_PASS_LEVELS = b'battle_pass_levels'
    PERSONAL_RESERVES = b'personal_reserves'
    LOOTBOX_REROLL = b'loot_box_re_roll'


class Source(object):
    EXTERNAL = b'external'


class Origin(object):
    STORAGE = b'storage'
    HERO_TANK = b'hero_tank'
    ADVENT_CALENDAR = b'advent_calendar'
    BATTLE_BOOSTERS = b'battle_boosters'
    CONSUMABLES = b'consumables'
    WITHOUT_NAME = b'without_name'
    HANGAR_TOP_MENU = b'hangar_top_menu'
    HANGAR_BONS_SCREEN = b'hangar_bons_screen'
    SHOP = b'shop'
    VEHICLE_PREVIEW = b'vehicle_preview'
    MISSIONS = b'missions'


def _getParams(reason, price, itemId=None):
    params = {b'reason': reason, 
       b'goldPrice': price, 
       b'source': (Source.EXTERNAL)}
    if itemId is not None:
        params[b'itemId'] = itemId
    return params


def _makeBuyItemUrl(categoryUrl, itemId=None):
    if itemId:
        return (b'{}/items/$PARAMS(web2client_{})').format(categoryUrl, itemId)
    return categoryUrl


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def canBuyGoldForItemThroughWeb(itemID, itemsCache=None):
    item = itemsCache.items.getItemByCD(itemID)
    if item.itemTypeID == GUI_ITEM_TYPE.VEHICLE:
        return canBuyGoldForVehicleThroughWeb(item)
    return False


@dependency.replace_none_kwargs(itemsCache=IItemsCache, tradeIn=ITradeInController)
def canBuyGoldForVehicleThroughWeb(vehicle, itemsCache=None, tradeIn=None):
    if vehicle.isUnlocked:
        money = itemsCache.items.stats.money
        money = tradeIn.addTradeInPriceIfNeeded(vehicle, money)
        exchangeRate = itemsCache.items.shop.exchangeRate
        price = getGUIPrice(vehicle, money, exchangeRate)
        currency = price.getCurrency(byWeight=True)
        mayObtainForMoney = vehicle.mayObtainWithMoneyExchange(money, exchangeRate)
        isBuyingAvailable = not vehicle.isHidden or vehicle.isRentable or vehicle.isRestorePossible()
        if currency == Currency.GOLD:
            if not mayObtainForMoney:
                if isBuyingAvailable:
                    return True
    return False


def showBuyPersonalReservesOverlay(itemId, source=None, origin=None):
    showBuyItemWebView(helpers.getBuyPersonalReservesUrl(), itemId, source, origin)
    return


def showBuyCreditsBattleBoosterOverlay(itemId, source=None, origin=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE):
    showBuyItemWebView(helpers.getBuyCreditsBattleBoostersUrl(), itemId, source, origin, alias)
    return


def showBuyBonBattleBoosterOverlay(itemId, source=None, origin=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE):
    showBuyItemWebView(helpers.getBuyBonBattleBoostersUrl(), itemId, source, origin, alias)
    return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def showBattleBoosterOverlay(itemId, source=None, origin=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE, itemsCache=None):
    item = itemsCache.items.getItemByCD(itemId)
    if item.getBuyPrice().price.isCurrencyDefined(Currency.CRYSTAL):
        showBuyMethod = showBuyBonBattleBoosterOverlay
    else:
        showBuyMethod = showBuyCreditsBattleBoosterOverlay
    showBuyMethod(itemId, source, origin, alias)
    return


def showBuyEquipmentOverlay(itemId, source=None, origin=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE):
    showBuyItemWebView(helpers.getBuyEquipmentUrl(), itemId, source, origin, alias)
    return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def showBuyOptionalDeviceOverlay(itemId, source=None, origin=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE, itemsCache=None):
    item = itemsCache.items.getItemByCD(itemId)
    if item.getBuyPrice().price.isCurrencyDefined(Currency.CRYSTAL):
        showBuyItemWebView(helpers.getBonsDevicesUrl(), itemId, source, origin, alias)
    else:
        showBuyItemWebView(helpers.getBuyOptionalDevicesUrl(), itemId, source, origin, alias)
    return


def showTradeOffOverlay(parent=None):
    _showBlurredWebOverlay(helpers.getTradeOffOverlayUrl(), None, parent, isClientCloseControl=True)
    return


def showBuyGoldForVehicleWebOverlay(fullPrice, intCD, parent=None):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.VEHICLE, fullPrice, intCD), parent)
    return


def showBuyGoldForRentWebOverlay(fullPrice, intCD):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.RENT, fullPrice, intCD))
    return


def showBuyGoldForXpWebOverlay(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.XP, fullPrice))
    return


def showBuyGoldForSlot(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.SLOT, fullPrice))
    return


def showBuyGoldForBerth(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.BERTH, fullPrice))
    return


def showBuyGoldForCrew(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.CREW, fullPrice))
    return


def showBuyGoldForEquipment(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.EQUIPMENT, fullPrice))
    return


def showBuyGoldForCustomization(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.CUSTOMIZATION, fullPrice))
    return


def showBuyGoldForBattlePass(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.BATTLE_PASS, fullPrice))
    return


def showBuyGoldForBattlePassLevels(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.BATTLE_PASS_LEVELS, fullPrice))
    return


def showBuyGoldForPersonalReserves(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.PERSONAL_RESERVES, fullPrice))
    return


def showBuyGoldForReroll(fullPrice):
    showBuyGoldWebOverlay(_getParams(_GoldPurchaseReason.LOOTBOX_REROLL, fullPrice))
    return


def showBuyGoldForBundle(fullPrice, params=None):
    params = dict(params) or {}
    params.update(_getParams(_GoldPurchaseReason.BUNDLE, fullPrice))
    showBuyGoldWebOverlay(params)
    return


def showBlueprintsExchangeOverlay(url=None, parent=None):
    url = yield URLMacros().parse(url or helpers.getBlueprintsExchangeUrl())
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BLUEPRINTS_EXCHANGE_VIEW, parent=parent), ctx={b'url': url}), EVENT_BUS_SCOPE.LOBBY)
    return


@adisp_process
def _showBlurredWebOverlay(url, params=None, parent=None, isClientCloseControl=False):
    url = yield URLMacros().parse(url, params)
    ctx = {b'url': url, 
       b'allowRightClick': False}
    if isClientCloseControl:
        ctx.update(helpers.getClientControlledCloseCtx())
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.WEB_VIEW_TRANSPARENT, parent=parent), ctx=ctx), EVENT_BUS_SCOPE.LOBBY)
    return


@adisp_process
def showBuyItemWebView(url, itemId, source=None, origin=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE):
    url = yield URLMacros().parse(url)
    params = {}
    if source:
        params[b'source'] = source
    if origin:
        params[b'origin'] = origin
    url = yield URLMacros().parse(url=_makeBuyItemUrl(url, itemId), params=params)
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(alias), ctx={b'url': url}), EVENT_BUS_SCOPE.LOBBY)
    return


@adisp_process
def showBuyGoldWebOverlay(params=None, parent=None):
    url = helpers.getBuyMoreGoldUrl()
    if url:
        url = yield URLMacros().parse(url, params=params)
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.OVERLAY_WEB_STORE, parent=parent), ctx={b'url': url}), EVENT_BUS_SCOPE.LOBBY)
    return


def showIngameShop(url, origin=None):
    from gui.shared.event_dispatcher import showShop
    params = {}
    if origin:
        params[b'origin'] = origin
    showShop(url, params=params)
    return


@adisp_process
def showBuyLootboxOverlay(parent=None, alias=VIEW_ALIAS.OVERLAY_WEB_STORE):
    url = helpers.getBuyLootboxesUrl()
    if url:
        url = yield URLMacros().parse(url)
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(alias, parent=parent), ctx={b'url': url}), EVENT_BUS_SCOPE.LOBBY)
    return


def showBuyProductOverlay(params=None):
    _showOverlayWebStoreDefault(helpers.getBuyProductUrl(), params)
    return


def showRentProductOverlay(params=None):
    _showOverlayWebStoreDefault(helpers.getBuyProductUrl(), params)
    return


@adisp_process
def _showOverlayWebStoreDefault(url, params=None):
    if url:
        url = yield URLMacros().parse(url, params=params)
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.OVERLAY_WEB_STORE), ctx={b'url': url, 
           b'browserParams': (makeBrowserParams(R.strings.waiting.updating(), True, True, 0.5))}), EVENT_BUS_SCOPE.LOBBY)
    return
