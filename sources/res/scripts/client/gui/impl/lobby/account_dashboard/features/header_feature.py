import logging, typing, BigWorld
from WeakMethod import WeakMethodProxy
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.clans.settings import getClanRoleName
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.account_completion.tooltips.hangar_tooltip_view import HangarTooltipView
from gui.impl.lobby.account_dashboard.features.base import FeatureItem
from gui.impl.lobby.tooltips.clans import ClanShortInfoTooltipContent
from gui.impl.pub.dialog_window import DialogButtons
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.platform.base.statuses.constants import StatusTypes
from gui.shared import event_dispatcher
from gui.shared.event_dispatcher import showSteamConfirmEmailOverlay, showSteamAddEmailOverlay
from gui.shared.view_helpers.emblems import EmblemSize, getClanEmblemURL
from helpers import dependency
from skeletons.gui.game_control import IBadgesController, ISteamCompletionController, IPlatoonController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.web import IWebController
from wg_async import wg_async, wg_await
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.account_dashboard.header_model import HeaderModel
    from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus
_logger = logging.getLogger(__name__)

class HeaderFeature(FeatureItem):
    __itemsCache = dependency.descriptor(IItemsCache)
    __webCtrl = dependency.descriptor(IWebController)
    __badgesController = dependency.descriptor(IBadgesController)
    __wgnpSteamAccCtrl = dependency.descriptor(IWGNPSteamAccRequestController)
    __steamRegistrationCtrl = dependency.descriptor(ISteamCompletionController)
    __platoonCtrl = dependency.descriptor(IPlatoonController)

    def __init__(self, viewModel):
        super(HeaderFeature, self).__init__(viewModel)
        self.__notConfirmedEmail = b''
        self.__isDestroyed = False
        self.__confirmationWindow = None
        self._tooltipModelFactories = {(R.views.lobby.tooltips.clans.ClanShortInfoTooltipContent()): ClanShortInfoTooltipContent, 
           (R.views.lobby.account_completion.tooltips.HangarTooltip()): (WeakMethodProxy(self.__createHangarTooltipView))}
        return

    def initialize(self, *args, **kwargs):
        super(HeaderFeature, self).initialize(*args, **kwargs)
        self._viewModel.header.onShowBadges += self.__onShowBadges
        self._viewModel.header.onAccountInfoButtonClick += self.__onAccountInfoButtonClick
        self.__badgesController.onUpdated += self.__onBadgesChanged
        g_clientUpdateManager.addCallbacks({b'stats.clanInfo': (self.__onClanInfoChanged), 
           b'cache.activeOrders': (self.__onClanInfoChanged)})
        self.__wgnpSteamAccCtrl.statusEvents.subscribe(StatusTypes.CONFIRMED, self._setEmailConfirmed)
        self.__wgnpSteamAccCtrl.statusEvents.subscribe(StatusTypes.ADDED, self._setEmailActionNeeded)
        self.__wgnpSteamAccCtrl.statusEvents.subscribe(StatusTypes.ADD_NEEDED, self._setEmailActionNeeded)
        return

    def finalize(self):
        self.__isDestroyed = True
        self._viewModel.header.onShowBadges -= self.__onShowBadges
        self._viewModel.header.onAccountInfoButtonClick -= self.__onAccountInfoButtonClick
        self.__badgesController.onUpdated -= self.__onBadgesChanged
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__wgnpSteamAccCtrl.statusEvents.unsubscribe(StatusTypes.CONFIRMED, self._setEmailConfirmed)
        self.__wgnpSteamAccCtrl.statusEvents.unsubscribe(StatusTypes.ADDED, self._setEmailActionNeeded)
        self.__wgnpSteamAccCtrl.statusEvents.unsubscribe(StatusTypes.ADD_NEEDED, self._setEmailActionNeeded)
        if self.__confirmationWindow is not None:
            self.__confirmationWindow.stopWaiting(DialogButtons.CANCEL)
            self.__confirmationWindow = None
        super(HeaderFeature, self).finalize()
        return

    def createToolTipContent(self, event, contentID):
        if contentID in self._tooltipModelFactories:
            return self._tooltipModelFactories[contentID]()
        return

    def _fillModel(self, model):
        submodel = model.header
        submodel.setUserName(BigWorld.player().name)
        submodel.setIsTeamKiller(self.__itemsCache.items.stats.isTeamKiller)
        self._updateClanInfo(model=model)
        self._updateBadges(model=model)
        submodel.setIsEmailPending(False)
        submodel.setEmailButtonLabel(R.invalid())
        if self.__steamRegistrationCtrl.isSteamAccount:
            self.__askEmailStatus()
        return

    @replaceNoneKwargsModel
    def _setEmailConfirmed(self, status=None, model=None):
        submodel = model.header
        submodel.setEmailButtonLabel(R.invalid())
        submodel.setIsEmailPending(False)
        self.__notConfirmedEmail = b''
        _logger.debug(b'User email confirmed.')
        return

    @replaceNoneKwargsModel
    def _setEmailActionNeeded(self, status=None, model=None):
        submodel = model.header
        submodel.setIsEmailPending(True)
        self.__notConfirmedEmail = status.email if status else b''
        if self.__notConfirmedEmail:
            submodel.setEmailButtonLabel(R.strings.badge.badgesPage.accountCompletion.button.confirmEmail())
        else:
            submodel.setEmailButtonLabel(R.strings.badge.badgesPage.accountCompletion.button.provideEmail())
        _logger.debug(b'User email: %s action needed.', self.__notConfirmedEmail)
        return

    @replaceNoneKwargsModel
    def _updateClanInfo(self, model=None):
        submodel = model.header
        clanProfile = self.__webCtrl.getAccountProfile()
        isInClan = clanProfile.isInClan()
        submodel.setIsInClan(isInClan)
        if isInClan:
            submodel.setClanAbbrev(clanProfile.getClanAbbrev())
            submodel.setRoleInClan(getClanRoleName(clanProfile.getRole()) or b'')
            submodel.setClanDescription(clanProfile.getClanFullName())
            clanIcon = getClanEmblemURL(clanProfile.getClanDbID(), EmblemSize.SIZE_32)
            submodel.setClanIcon(clanIcon if clanIcon is not None else b'')
        return

    @replaceNoneKwargsModel
    def _updateBadges(self, model=None):
        submodel = model.header
        self.__setBadge(submodel.setBadgeID, self.__badgesController.getPrefix())
        self.__setBadge(submodel.setSuffixBadgeID, self.__badgesController.getSuffix())
        return

    def __createHangarTooltipView(self):
        _logger.debug(b'Show not confirmed email: %s tooltip.', self.__notConfirmedEmail)
        return HangarTooltipView(self.__notConfirmedEmail)

    def __onClanInfoChanged(self, _):
        self._updateClanInfo()
        return

    def __onBadgesChanged(self):
        self._updateBadges()
        return

    @staticmethod
    def __setBadge(setter, badge):
        setter(badge.getIconPostfix() if badge is not None and badge.isSelected else b'')
        return

    @staticmethod
    def __onShowBadges():
        event_dispatcher.showBadges(backViewName=backport.text(R.strings.badge.badgesPage.header.backBtn.descrLabel()))
        return

    def __onAccountInfoButtonClick(self):
        if self.__steamRegistrationCtrl.isSteamAccount:
            self.__onEmailButtonClicked()
        return

    def __onEmailButtonClicked(self):
        label = self._viewModel.header.getEmailButtonLabel()
        if label == R.strings.badge.badgesPage.accountCompletion.button.confirmEmail():
            _logger.debug(b'Show email confirmation overlay with email=%s.', self.__notConfirmedEmail)
            showSteamConfirmEmailOverlay(email=self.__notConfirmedEmail)
        elif label == R.strings.badge.badgesPage.accountCompletion.button.provideEmail():
            _logger.debug(b'Show add email overlay.')
            showSteamAddEmailOverlay()
        else:
            _logger.warning(b'Unknown email button label: %s. Action skipped.', label)
        return

    @wg_async
    def __askEmailStatus(self):
        if not self.__steamRegistrationCtrl.isSteamAccount:
            _logger.debug(b'Account completion disabled.')
            return
        _logger.debug(b'Sending email status request.')
        status = yield wg_await(self.__wgnpSteamAccCtrl.getEmailStatus())
        if status.isUndefined or self.__isDestroyed:
            _logger.warning(b'Can not get account email status.')
            return
        if status.typeIs(StatusTypes.ADD_NEEDED):
            self._setEmailActionNeeded()
        elif status.typeIs(StatusTypes.ADDED):
            self._setEmailActionNeeded(status=status)
        else:
            self._setEmailConfirmed()
        return
