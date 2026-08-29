import typing
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import makeBrowserParams
from helpers import dependency
from helpers.http.url_formatters import addParamsToUrlQuery
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def _getUrl(urlName=None, lobbyContext=None):
    hostUrl = lobbyContext.getServerSettings().shop.hostUrl
    return hostUrl + (b'' if urlName is None else GUI_SETTINGS.shop.get(urlName))


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isSubscriptionEnabled(itemsCache=None):
    return itemsCache.items.stats.isSubscriptionEnabled


def getShopURL():
    return _getUrl()


def getShopRootUrl():
    return _getUrl(b'shopRootUrl')


def getBuyMoreGoldUrl():
    return _getUrl(b'buyMoreGoldUrl')


def getBuyGoldUrl():
    return _getUrl(b'buyGoldUrl')


def getBuyFeaturedUrl():
    return _getUrl(b'buyFeatured')


def getBuyPremiumUrl():
    return _getUrl(b'buyPremiumUrl')


def getBuyPersonalReservesUrl():
    return _getUrl(b'buyBoosters')


def getBuyCreditsBattleBoostersUrl():
    return _getUrl(b'buyCreditsBattleBoosters')


def getBuyBonBattleBoostersUrl():
    return _getUrl(b'buyBonBattleBoosters')


def getBuyEquipmentUrl():
    return _getUrl(b'buyEquipment')


def getBuyOptionalDevicesUrl():
    return _getUrl(b'buyOptionalDevices')


def getBuyVehiclesUrl():
    return _getUrl(b'buyVehiclesUrl')


def getBuyProductUrl():
    return _getUrl(b'buyProduct')


def getBonsUrl():
    return _getUrl(b'bonsUrl')


def getBonsDevicesUrl():
    return _getUrl(b'bonsDevicesUrl')


def getBonsVehiclesUrl():
    return _getUrl(b'bonsVehiclesUrl')


def getBonsInstructionsUrl():
    return _getUrl(b'bonsInstructionsUrl')


def getTradeInVehiclesUrl():
    return _getUrl(b'tradeIn')


def getTradeOffOverlayUrl():
    return _getUrl(b'tradeOffOverlay')


def getPremiumVehiclesUrl():
    return _getUrl(b'premiumVehicles')


def getBuyBattlePassUrl():
    return _getUrl(b'buyBattlePass')


def getBattlePassCoinProductsUrl():
    return _getUrl(b'bpcoinProducts')


def getBattlePassPointsProductsUrl():
    return _getUrl(b'bpProducts')


def getBuyCollectibleVehiclesUrl():
    return _getUrl(b'buyCollectibleVehicle')


def getBlueprintsExchangeUrl():
    return _getUrl(b'blueprintsExchange')


def getPlayerSeniorityAwardsUrl():
    return _getUrl(b'seniorityAwardsProducts')


def getSplitPageUrl(params):
    url = _getUrl(b'splitUrl')
    return addParamsToUrlQuery(url, params, True)


def getRentVehicleUrl():
    return _getUrl(b'rentVehicle')


def getTelecomRentVehicleUrl():
    return _getUrl(b'telecomTankRental')


def getWotPlusShopUrl():
    return _getUrl(b'buyWotPlus')


def getIntegratedAuctionUrl():
    return _getUrl(b'integratedAuction')


def getBlackMarketUrl():
    return _getUrl(b'blackMarket')


def getShowcaseUrl():
    return _getUrl(b'showcase')


def getClientControlledCloseCtx():
    return {b'browserParams': (makeBrowserParams(isCloseBtnVisible=True)), 
       b'forcedSkipEscape': True}


def getSteelHunterProductsUrl():
    return _getUrl(b'shProducts')


def getCosmic2024ShopUrl():
    return _getUrl(urlName=b'cosm24Shop')


def getComp7ProductsUrl():
    return _getUrl(b'comp7Products')
