import logging, typing
from PlayerEvents import g_playerEvents
from constants import PremiumConfigs, PREMIUM_TYPE
from frameworks.wulf import ViewFlags, ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getWotPlusShopUrl, getBuyPremiumUrl
from gui.game_control.wot_plus.utils import getMaxGoldReserveCapacityFromAllTiers
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserve_model import CurrencyEnum
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserves_view_model import CurrencyReservesViewModel
from gui.impl.lobby.premacc.premacc_helpers import PiggyBankConstants, getDeltaTimeHelper
from gui.impl.pub import ViewImpl
from gui.shared.event_dispatcher import showWotPlusInfoPage, showTankPremiumAboutPage, showShop
from helpers import dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER
from skeletons.gui.game_control import IGameSessionController, IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from uilogging.wot_plus.loggers import WotPlusReservesLogger
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource, ReservesKeys
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
        g_playerEvents.onConfigModelUpdated += self._onConfigModelUpdated
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
        g_playerEvents.onConfigModelUpdated -= self._onConfigModelUpdated
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
        storage = self._wotPlusCtrl.getSettingsStorage()
        with self.viewModel.goldReserve.transaction() as goldReserve:
            goldReserve.setIsEnabled(storage.isGoldReserveFeatureEnabled())
            goldReserve.setIsActive(storage.isGoldReserveFeatureAvailable())
            goldReserve.setCurrency(CurrencyEnum.GOLD)
            goldReserve.setAmount(self._wotPlusCtrl.getGoldReserve())
            goldReserve.setMaxCapacity(getMaxGoldReserveCapacityFromAllTiers())
        return

    def _onServerSettingsChange(self, diff):
        if PremiumConfigs.PIGGYBANK in diff:
            self._updateCreditReserve()
            self._updateTimeToOpen()
        return

    def _onConfigModelUpdated(self, gpKey):
        if renewableSubscriptionsConfigSchema.gpKey == gpKey:
            self._updateGoldReserve()
        return

    def _onWotPlusDataChanged(self, data):
        if RS_TIER in data or b'piggyBank' in data:
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
        showShop(getWotPlusShopUrl())
        return

    def _onCreditReserveInfoButtonClick(self):
        self._wotPlusUILogger.logClickEvent(ReservesKeys.CREDITS_INFO)
        showTankPremiumAboutPage()
        return

    def _onCreditReserveActionButtonClick(self):
        self._wotPlusUILogger.logClickEvent(ReservesKeys.CREDITS_ACTIVATE)
        showShop(getBuyPremiumUrl())
        return
