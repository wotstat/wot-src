from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform import getVehicleTypeAssetPath, getNationsAssetPath, NATION_ICON_PREFIX_131x31
from gui.Scaleform.daapi.view.meta.ExchangeXpWindowMeta import ExchangeXpWindowMeta
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shop import showBuyGoldForXpWebOverlay
from gui.shared.formatters import icons
from gui.shared.formatters.text_styles import builder
from gui.shared.gui_items.gui_item_economics import ItemPrice
from gui.shared.gui_items.processors.common import FreeXPExchanger
from gui.shared.money import Currency, Money
from gui.shared.utils.decorators import adisp_process
from helpers import i18n, dependency
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache
from gui.impl import backport

class ExchangeXPWindow(ExchangeXpWindowMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    wallet = dependency.descriptor(IWalletController)
    __slots__ = (b'__needXP',)

    def __init__(self, ctx=None, needXP=None):
        super(ExchangeXPWindow, self).__init__(ctx)
        self.__needXP = needXP or (ctx or {}).get(b'needXP', 0)
        return

    def _populate(self):
        super(ExchangeXPWindow, self)._populate()
        self.__xpForFree = self.itemsCache.items.shop.freeXPConversionLimit
        self.as_setPrimaryCurrencyS(self.itemsCache.items.stats.actualGold)
        self.__setRates()
        self.as_totalExperienceChangedS(self.itemsCache.items.stats.actualFreeXP)
        self.__prepareAndPassVehiclesData()
        self.as_setWalletStatusS(self.wallet.status, True)
        if self.__needXP > 0:
            self.as_setTargetXPS(self.__needXP)
        return

    def _subscribe(self):
        g_clientUpdateManager.addCurrencyCallback(Currency.GOLD, self._setGoldCallBack)
        g_clientUpdateManager.addCallbacks({b'shop.freeXPConversion': (self.__setXPConversationCallBack), 
           b'shop.goodies': (self.__discountChangedCallback), 
           b'goodies.4': (self.__discountChangedCallback), 
           b'inventory.1': (self.__vehiclesDataChangedCallBack), 
           b'stats.vehTypeXP': (self.__vehiclesDataChangedCallBack), 
           b'stats.freeXP': (self.__setFreeXPCallBack)})
        self.wallet.onWalletStatusChanged += self.__setWalletCallback
        self.itemsCache.onSyncCompleted += self.__setXPConversationCallBack
        return

    def __vehiclesDataChangedCallBack(self, _):
        self.__prepareAndPassVehiclesData()
        return

    def __setFreeXPCallBack(self, value):
        self.as_totalExperienceChangedS(value)
        return

    def __setXPConversationCallBack(self, *args):
        self.__setRates()
        return

    def __setWalletCallback(self, status):
        self.as_setPrimaryCurrencyS(self.itemsCache.items.stats.actualGold)
        self.as_totalExperienceChangedS(self.itemsCache.items.stats.actualFreeXP)
        self.as_setWalletStatusS(status, True)
        return

    def __prepareAndPassVehiclesData(self):
        values = []
        for vehicleCD in self.itemsCache.items.stats.eliteVehicles:
            try:
                vehicle = self.itemsCache.items.getItemByCD(vehicleCD)
                if not vehicle.xp or not vehicle.activeInNationGroup:
                    continue
                isBattleRoyaleVehicle = vehicle.isOnlyForBattleRoyaleBattles
                values.append({b'id': (vehicle.intCD), 
                   b'vehicleType': ((isBattleRoyaleVehicle or getVehicleTypeAssetPath)(vehicle.type) if 1 else None), 
                   b'vehicleName': (vehicle.shortUserName), 
                   b'xp': (vehicle.xp), 
                   b'xpStrValue': (backport.getIntegralFormat(vehicle.xp)), 
                   b'isSelectCandidate': (vehicle.isFullyElite), 
                   b'vehicleIco': (vehicle.iconSmall), 
                   b'nationIco': (getNationsAssetPath(vehicle.nationID, namePrefix=NATION_ICON_PREFIX_131x31))})
            except Exception:
                continue

        labelBuilder = builder().addStyledText(b'middleTitle', i18n.makeString(MENU.EXCHANGE_RATE))
        if self.__xpForFree is not None:
            labelBuilder.addStyledText(self.__getActionStyle(), i18n.makeString(MENU.EXCHANGEXP_AVAILABLE_FORFREE_LABEL))
            labelBuilder.addStyledText(b'expText', i18n.makeString(MENU.EXCHANGEXP_AVAILABLE_FORFREE_VALUE, icon=icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ELITEXPICON_2), forFree=backport.getNiceNumberFormat(self.__xpForFree)))
        exchangeHeaderData = {b'labelText': (labelBuilder.render()), 
           b'rateFromIcon': (ICON_TEXT_FRAMES.GOLD), 
           b'rateToIcon': (ICON_TEXT_FRAMES.ELITE_XP), 
           b'rateFromTextColor': (self.app.colorManager.getColorScheme(b'textColorGold').get(b'rgb')), 
           b'rateToTextColor': (self.app.colorManager.getColorScheme(b'textColorCredits').get(b'rgb'))}
        vehicleData = {b'isHaveElite': (bool(values)), 
           b'vehicleList': values, 
           b'tableHeader': (self._getTableHeader()), 
           b'xpForFree': (self.__xpForFree), 
           b'exchangeHeaderData': exchangeHeaderData}
        self.as_vehiclesDataChangedS(vehicleData)
        return

    def _getTableHeader(self):
        return [
         self._createTableBtnInfo(b'isSelectCandidate', 40, 2, DIALOGS.GATHERINGXPFORM_SORTBY_SELECTION, b'ascending', RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_OK),
         self._createTableBtnInfo(b'vehicleName', 179, 1, DIALOGS.GATHERINGXPFORM_SORTBY_VEHICLE, b'ascending', RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_TANK, sortType=b'string'),
         self._createTableBtnInfo(b'xp', 103, 0, DIALOGS.GATHERINGXPFORM_SORTBY_XP, b'descending', RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_XP)]

    def _createTableBtnInfo(self, btnID, buttonWidth, sortOrder, toolTip, defaultSortDirection, iconSource, sortType=b'numeric'):
        return {b'id': btnID, 
           b'buttonWidth': buttonWidth, 
           b'sortOrder': sortOrder, 
           b'toolTip': toolTip, 
           b'defaultSortDirection': defaultSortDirection, 
           b'iconSource': iconSource, 
           b'sortType': sortType, 
           b'ascendingIconSource': b'../maps/icons/buttons/tab_sort_button/ascendingSortArrow.png', 
           b'descendingIconSource': b'../maps/icons/buttons/tab_sort_button/descendingSortArrow.png', 
           b'buttonHeight': 30}

    @adisp_process(b'exchangeVehiclesXP')
    def exchange(self, data):
        exchangeXP = data.exchangeXp
        vehTypeCompDescrs = map(int, data.selectedVehicles)
        eliteVcls = self.itemsCache.items.stats.eliteVehicles
        xps = self.itemsCache.items.stats.vehiclesXPs
        commonXp = 0
        for vehicleCD in vehTypeCompDescrs:
            if vehicleCD in eliteVcls:
                commonXp += xps.get(vehicleCD, 0)

        xpToExchange = min(commonXp, exchangeXP)
        money = self.itemsCache.items.stats.money
        price = self.__getConversionPrice(xpToExchange).price
        if self.wallet.isAvailable and money.gold < price.gold:
            self._goToGoldBuy(price.gold)
        else:
            result = yield FreeXPExchanger(xpToExchange, vehTypeCompDescrs, freeConversion=self.__xpForFree).request()
            self._processResult(result, xpToExchange)
        return

    def onWindowClose(self):
        self.destroy()
        return

    def getSubmitButtonEnableState(self, selectedXPCount):
        return selectedXPCount > 0

    def _dispose(self):
        self.itemsCache.onSyncCompleted -= self.__setXPConversationCallBack
        self.wallet.onWalletStatusChanged -= self.__setWalletCallback
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(ExchangeXPWindow, self)._dispose()
        return

    def _processResult(self, result, _):
        if result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
        if result.success:
            self.destroy()
        return

    def _goToGoldBuy(self, gold):
        showBuyGoldForXpWebOverlay(gold)
        return

    def __discountChangedCallback(self, _):
        self.__setRates()
        newLimit = self.itemsCache.items.shop.freeXPConversionLimit
        if newLimit != self.__xpForFree:
            self.__xpForFree = newLimit
            self.__prepareAndPassVehiclesData()
        return

    def __setRates(self):
        rate = self.itemsCache.items.shop.freeXPConversionWithDiscount
        defaultRate = self.itemsCache.items.shop.defaults.freeXPConversion
        self.as_exchangeRateS({b'value': (defaultRate[0]), 
           b'actionValue': (rate[0]), 
           b'actionMode': (self.itemsCache.items.shop.isXPConversionActionActive)})
        return

    def __getConversionPrice(self, xp):

        def computeCost(xp, rate, cost):
            return round(cost * xp / rate)

        rate, cost = self.itemsCache.items.shop.freeXPConversionWithDiscount
        defRate, defCost = self.itemsCache.items.shop.defaults.freeXPConversion
        return ItemPrice(Money(gold=computeCost(xp, rate, cost)), Money(gold=computeCost(xp, defRate, defCost)))

    def __getActionStyle(self):
        rate = self.itemsCache.items.shop.defaults.freeXPConversion
        actionRate = self.itemsCache.items.shop.freeXPConversionWithDiscount
        if rate != actionRate and actionRate > 0:
            return b'statsText'
        return b'alertText'
