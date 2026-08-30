import logging
from math import ceil
from constants import PremiumConfigs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl
from gui.impl.gen import R
from gui.impl.lobby.premacc.piggybank_base import PiggyBankBaseView, PiggyBankConstants
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.impl.gen.view_models.views.lobby.premacc.piggybank_model import PiggybankModel
from frameworks.wulf import ViewFlags, ViewSettings
from gui.shared.event_dispatcher import showTankPremiumAboutPage, showShop
from gui.shared.utils.scheduled_notifications import TimerNotifier
from helpers import time_utils
_logger = logging.getLogger(__name__)

def _getBackBtnLabel():
    return R.strings.premacc.piggyBank.backBtnAddLabel()


class PiggyBankView(PiggyBankBaseView):
    _PERIOD = 7 * time_utils.ONE_DAY
    __slots__ = ()

    def __init__(self, layoutID=R.views.lobby.premacc.piggybank.Piggybank()):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_TOP_SUB_VIEW
        settings.model = PiggybankModel()
        super(PiggyBankView, self).__init__(settings)
        return

    def onPremAccProlong(self, _=None):
        showShop(getBuyPremiumUrl())
        return

    def onBackBtnClicked(self, _=None):
        self.destroyWindow()
        return

    def onGoToContentPage(self):
        showTankPremiumAboutPage()
        return

    def _createNotifier(self):
        return TimerNotifier(self._getDeltaTime, self._updateTimer)

    def _initialize(self, *args, **kwargs):
        super(PiggyBankView, self)._initialize(*args, **kwargs)
        with self.getViewModel().transaction() as model:
            model.setBackBtnLabel(_getBackBtnLabel())
            self._updatePercentDiscount(model=model)
            self._updateIsPremUsed(model=model)
            self._updatePeriodInDays(model=model)
            self._updatePiggyIsFull(model=model)
        return

    @replaceNoneKwargsModel
    def _updateIsPremUsed(self, credits_=None, model=None):
        credits_ = credits_ or self._data.get(b'credits', 0)
        isPremium = self._isTankPremiumActive()
        isPremUsed = isPremium or credits_ > 0
        model.setIsPremUsed(isPremUsed)
        return

    @replaceNoneKwargsModel
    def _updatePeriodInDays(self, model=None):
        period = self._config.get(b'cycleLength', self._PERIOD)
        periodInDays = ceil(period / time_utils.ONE_DAY)
        model.setPeriodInDays(periodInDays)
        return

    @replaceNoneKwargsModel
    def _updatePercentDiscount(self, model=None):
        percent = self.__toPercents(self._config.get(b'multiplier', 0))
        model.setPercentDiscount(percent)
        return

    @replaceNoneKwargsModel
    def _updatePiggyIsFull(self, credits_=None, model=None):
        creditsValue = credits_ or self._data.get(b'credits', 0)
        maxAmount = self._config.get(b'creditsThreshold', PiggyBankConstants.MAX_AMOUNT)
        model.setPiggyIsFull(creditsValue >= maxAmount)
        return

    def _updateCredits(self, credits_=None):
        super(PiggyBankView, self)._updateCredits(credits_)
        self._updatePiggyIsFull(credits_)
        self._updateIsPremUsed(credits_)
        return

    def _updatePrem(self, *args):
        super(PiggyBankView, self)._updatePrem()
        self._updateIsPremUsed()
        return

    def _onServerSettingsChange(self, diff):
        super(PiggyBankView, self)._onServerSettingsChange(diff)
        if PremiumConfigs.PIGGYBANK not in diff:
            return
        diffConfig = diff.get(PremiumConfigs.PIGGYBANK)
        if b'creditsThreshold' in diffConfig:
            self._updatePiggyIsFull()
        if b'cycleLength' in diffConfig:
            self._updatePeriodInDays()
        if b'multiplier' in diffConfig:
            self._updatePercentDiscount()
        return

    def _addListeners(self):
        super(PiggyBankView, self)._addListeners()
        self.viewModel.onPremAccProlong += self.onPremAccProlong
        self.viewModel.onBackBtnClicked += self.onBackBtnClicked
        self.viewModel.onGoToContentPage += self.onGoToContentPage
        return

    def _removeListeners(self):
        super(PiggyBankView, self)._removeListeners()
        self.viewModel.onPremAccProlong -= self.onPremAccProlong
        self.viewModel.onBackBtnClicked -= self.onBackBtnClicked
        self.viewModel.onGoToContentPage -= self.onGoToContentPage
        return

    @staticmethod
    def __toPercents(value):
        return int(value * 100)
