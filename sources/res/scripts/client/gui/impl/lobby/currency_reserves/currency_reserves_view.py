import logging, typing
from constants import PremiumConfigs, PREMIUM_TYPE, RENEWABLE_SUBSCRIPTION_CONFIG
from frameworks.wulf import ViewFlags, ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getWotPlusShopUrl, getBuyPremiumUrl
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserve_model import CurrencyEnum
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserves_view_model import CurrencyReservesViewModel
from gui.impl.lobby.premacc.premacc_helpers import PiggyBankConstants, getDeltaTimeHelper
from gui.impl.pub import ViewImpl
from gui.shared.event_dispatcher import showWotPlusInfoPage, showTankPremiumAboutPage, showShop, showSteamRedirectWotPlus
from helpers import dependency
from skeletons.gui.game_control import IGameSessionController, IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource, ReservesKeys
from uilogging.wot_plus.loggers import WotPlusReservesLogger
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from typing import Dict, Any

class CurrencyReservesView(ViewImpl):
    _itemsCache = dependency.descriptor(IItemsCache)
    _gameSession = dependency.descriptor(IGameSessionController)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)
    __slots__ = (b'_creditReserveInfo', b'_creditReserveConfig', b'_serverSettings', b'_wotPlusUILogger')

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_TOP_SUB_VIEW
        settings.model = CurrencyReservesViewModel()
        self._creditReserveInfo = self._itemsCache.items.stats.piggyBank
        self._creditReserveConfig = self._lobbyContext.getServerSettings().getPiggyBankConfig()
        self._serverSettings = self._lobbyContext.getServerSettings()
        self._wotPlusUILogger = WotPlusReservesLogger()
        super(CurrencyReservesView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(CurrencyReservesView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        self.viewModel.onClose += self._onClose
        self._gameSession.onPremiumNotify += self._onPremiumNotify
        self._lobbyContext.getServerSettings().onServerSettingsChange += self._onServerSettingsChange
        self._wotPlusCtrl.onDataChanged += self._onWotPlusDataChanged
        self.viewModel.goldReserve.onInfoButtonClick += self._onGoldReserveInfoButtonClick
        self.viewModel.goldReserve.onActionButtonClick += self._onGoldReserveActionButtonClick
        self.viewModel.creditReserve.onInfoButtonClick += self._onCreditReserveInfoButtonClick
        self.viewModel.creditReserve.onActionButtonClick += self._onCreditReserveActionButtonClick
        g_clientUpdateManager.addCallbacks({(PiggyBankConstants.PIGGY_BANK): (self._onPiggyBankChanged)})
        self._wotPlusUILogger.onViewInitialize()
        return

    def _finalize(self):
        self.viewModel.onClose -= self._onClose
        self._gameSession.onPremiumNotify -= self._onPremiumNotify
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self._onServerSettingsChange
        self._wotPlusCtrl.onDataChanged -= self._onWotPlusDataChanged
        self.viewModel.goldReserve.onInfoButtonClick -= self._onGoldReserveInfoButtonClick
        self.viewModel.goldReserve.onActionButtonClick -= self._onGoldReserveActionButtonClick
        self.viewModel.creditReserve.onInfoButtonClick -= self._onCreditReserveInfoButtonClick
        self.viewModel.creditReserve.onActionButtonClick -= self._onCreditReserveActionButtonClick
        g_clientUpdateManager.removeObjectCallbacks(self)
        self._wotPlusUILogger.onViewFinalize()
        return

    def _onPremiumNotify(self, *args):
        self._updateCreditReserve()
        return

    def _onLoading(self, highlightedComponentId=-1, makeTopView=False):
        logging.debug(b'CurrencyReserves::_onLoading')
        self._updateGoldReserve()
        self._updateCreditReserve()
        self._updateTimeToOpen()
        return

    def _onPiggyBankChanged(self, *args):
        self._updateCreditReserve()
        self._updateTimeToOpen()
        return

    def _updateTimeToOpen(self):
        timeToOpen = getDeltaTimeHelper(self._creditReserveConfig, self._creditReserveInfo)
        self.viewModel.setTimeToOpen(timeToOpen)
        return

    def _updateCreditReserve(self):
        with self.viewModel.creditReserve.transaction() as creditReserve:
            creditReserve.setIsEnabled(self._creditReserveConfig.get(b'enabled'))
            creditReserve.setIsActive(self._isPremiumPlusActive())
            creditReserve.setCurrency(CurrencyEnum.CREDITS)
            creditReserve.setAmount(self._creditReserveInfo.get(b'credits', 0))
            creditReserve.setMaxCapacity(self._creditReserveConfig.get(b'creditsThreshold', 0))
        return

    def _updateGoldReserve(self):
        with self.viewModel.goldReserve.transaction() as goldReserve:
            goldReserve.setIsEnabled(self._serverSettings.isRenewableSubGoldReserveEnabled())
            goldReserve.setIsActive(self._wotPlusCtrl.isEnabled())
            goldReserve.setCurrency(CurrencyEnum.GOLD)
            goldReserve.setAmount(self._wotPlusCtrl.getGoldReserve())
            goldReserve.setMaxCapacity(self._serverSettings.getRenewableSubMaxGoldReserveCapacity())
        return

    def _onServerSettingsChange(self, diff):
        if RENEWABLE_SUBSCRIPTION_CONFIG in diff:
            self._updateGoldReserve()
        if PremiumConfigs.PIGGYBANK in diff:
            self._updateCreditReserve()
            self._updateTimeToOpen()
        return

    def _onWotPlusDataChanged(self, data):
        if b'isEnabled' in data or b'piggyBank' in data:
            self._updateGoldReserve()
        return

    def _onClose(self):
        self._wotPlusUILogger.logCloseEvent()
        self.destroyWindow()
        return

    def _isPremiumPlusActive(self):
        return self._itemsCache.items.stats.isActivePremium(PREMIUM_TYPE.PLUS)

    def _onGoldReserveInfoButtonClick(self):
        showWotPlusInfoPage(WotPlusInfoPageSource.GOLD_RESERVES, includeSubscriptionInfo=True)
        return

    def _onGoldReserveActionButtonClick(self):
        self._wotPlusUILogger.logClickEvent(ReservesKeys.GOLD_ACTIVATE)
        if self._wotPlusCtrl.isWotPlusEnabled():
            showShop(getWotPlusShopUrl())
        else:
            showSteamRedirectWotPlus()
        return

    def _onCreditReserveInfoButtonClick(self):
        self._wotPlusUILogger.logClickEvent(ReservesKeys.CREDITS_INFO)
        showTankPremiumAboutPage()
        return

    def _onCreditReserveActionButtonClick(self):
        self._wotPlusUILogger.logClickEvent(ReservesKeys.CREDITS_ACTIVATE)
        showShop(getBuyPremiumUrl())
        return
