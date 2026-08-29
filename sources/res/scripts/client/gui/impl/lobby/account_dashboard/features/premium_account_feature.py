import typing
from constants import PREMIUM_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl
from gui.impl.lobby.account_dashboard.features.base import FeatureItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.event_dispatcher import showShop
from helpers import dependency, time_utils
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.account_dashboard.premium_account_model import PremiumAccountModel

class PremiumAccountFeature(FeatureItem):
    __slots__ = ()
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __gameSession = dependency.descriptor(IGameSessionController)

    def initialize(self, *args, **kwargs):
        super(PremiumAccountFeature, self).initialize(*args, **kwargs)
        self.__startListening()
        return

    def finalize(self):
        self.__stopListening()
        super(PremiumAccountFeature, self).finalize()
        return

    def _fillModel(self, model):
        self.__setPremBonusValues(model=model)
        self.__updatePremState(model=model)
        return

    def __startListening(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onSettingsChange
        self.__gameSession.onPremiumNotify += self.__onPremiumStatusChanged
        g_clientUpdateManager.addCallbacks({b'stats.dummySessionStats': (self.__onStatsChanged), 
           b'premium': (self.__onPremiumStatusChanged)})
        self._viewModel.premiumAccount.onClick += self.__onClick
        return

    def __stopListening(self):
        self._viewModel.premiumAccount.onClick -= self.__onClick
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onSettingsChange
        self.__gameSession.onPremiumNotify -= self.__onPremiumStatusChanged
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def __onSettingsChange(self, diff):
        if not {b'tankPremiumBonus', b'premSquad_config'} & set(diff.keys()):
            return
        self.__setPremBonusValues()
        return

    def __onStatsChanged(self, *_):
        self.__updatePremState()
        return

    def __onPremiumStatusChanged(self, *_):
        self.__updatePremState()
        return

    @replaceNoneKwargsModel
    def __setPremBonusValues(self, model=None):
        submodel = model.premiumAccount
        settings = self.__lobbyContext.getServerSettings()
        submodel.setXpBonus(self.__toPercents(settings.getPremiumXPBonus()))
        submodel.setCreditBonus(self.__toPercents(settings.getPremiumCreditsBonus()))
        submodel.setPlatoonBonus(self.__toPercents(settings.squadPremiumBonus.ownCredits))
        return

    @replaceNoneKwargsModel
    def __updatePremState(self, model=None):
        submodel = model.premiumAccount
        stats = self.__getStatsRequester().dummySessionStats
        base = stats.get(b'base', {})
        premium = stats.get(b'premium', {})
        submodel.setPlusPremiumSecondsLeft(self.__getTimeLeft(PREMIUM_TYPE.PLUS))
        submodel.setPremiumAccountCredits(premium.get(b'credits', 0))
        submodel.setPremiumAccountXp(premium.get(b'xp', 0))
        submodel.setBasicPremiumSecondsLeft(self.__getTimeLeft(PREMIUM_TYPE.BASIC))
        submodel.setStandardAccountCredits(base.get(b'credits', 0))
        submodel.setStandardAccountXp(base.get(b'xp', 0))
        return

    def __getTimeLeft(self, premType):
        expiryTime = self.__getStatsRequester().premiumInfo.get(premType, {}).get(b'expiryTime', 0)
        serverTime = time_utils.getCurrentLocalServerTimestamp()
        if expiryTime == 0 or expiryTime <= serverTime:
            return -1
        return expiryTime - serverTime

    def __getStatsRequester(self):
        return self.__itemsCache.items.stats

    @staticmethod
    def __toPercents(value):
        return int(round(value * 100))

    @staticmethod
    def __onClick():
        showShop(getBuyPremiumUrl())
        return
