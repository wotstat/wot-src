from __future__ import absolute_import
import typing, logging
from future.utils import viewitems
from adisp import adisp_async, adisp_process
from gui import GUI_SETTINGS
from gui.game_control.links import URLMacros
from gui.shared import g_eventBus
from gui.shared.events import OpenLinkEvent
from helpers import dependency
from skeletons.gui.game_control import IExternalLinksController
from gui.game_control.links_handlers import external
from skeletons.gui.login_manager import ILoginManager
if typing.TYPE_CHECKING:
    from gui.game_control.links_handlers.external import ILinksHandler
_logger = logging.getLogger(__name__)
_LISTENERS = {(OpenLinkEvent.SPECIFIED): b'_handleSpecifiedURL', 
   (OpenLinkEvent.PARSED): b'_handleParsedURL', 
   (OpenLinkEvent.REGISTRATION): b'_handleOpenRegistrationURL', 
   (OpenLinkEvent.RECOVERY_PASSWORD): b'_handleOpenRecoveryPasswordURL', 
   (OpenLinkEvent.PAYMENT): b'_handleOpenPaymentURL', 
   (OpenLinkEvent.SECURITY_SETTINGS): b'_handleSecuritySettingsURL', 
   (OpenLinkEvent.CLAN_RULES): b'_handleClanRulesURL', 
   (OpenLinkEvent.SUPPORT): b'_handleSupportURL', 
   (OpenLinkEvent.MIGRATION): b'_handleMigrationURL', 
   (OpenLinkEvent.FORT_DESC): b'_handleFortDescription', 
   (OpenLinkEvent.CLAN_SEARCH): b'_handleClanSearch', 
   (OpenLinkEvent.CLAN_CREATE): b'_handleClanCreate', 
   (OpenLinkEvent.INVIETES_MANAGEMENT): b'_handleInvitesManagementURL', 
   (OpenLinkEvent.GLOBAL_MAP_SUMMARY): b'_handleGmSummaryURL', 
   (OpenLinkEvent.GLOBAL_MAP_PROMO_SUMMARY): b'_handleGmPromoSummaryURL', 
   (OpenLinkEvent.GLOBAL_MAP_CAP): b'_handleGmCapURL', 
   (OpenLinkEvent.GLOBAL_MAP_PROMO): b'_handleGmPromoURL', 
   (OpenLinkEvent.PREM_SHOP): b'_handleOpenPremShopURL', 
   (OpenLinkEvent.FRONTLINE_CHANGES): b'_handleFrontlineChangesURL', 
   (OpenLinkEvent.TOKEN_SHOP): b'_handleTokenShopURL', 
   (OpenLinkEvent.WOT_PLUS_STEAM_SHOP): b'_handleWotPlusSteamShopURL', 
   (OpenLinkEvent.WOT_PLUS_SHOP): b'_handleWotPlusShopURL', 
   (OpenLinkEvent.STEAM_SUBSCRIPTION_MANAGEMENT): b'_handleSteamSubscriptionManagementURL', 
   (OpenLinkEvent.LOOT_BOXES_LIST): b'_handleLootBoxesListURL', 
   (OpenLinkEvent.REPORT_CONTENT): b'_handleReportContentURL', 
   (OpenLinkEvent.OPEN_BUNDLE_STEPS): b'_handleOpenBundleStepsURL'}

class ExternalLinksHandler(IExternalLinksController):
    __loginManager = dependency.descriptor(ILoginManager)

    def __init__(self):
        super(ExternalLinksHandler, self).__init__()
        self.__urlMacros = None
        self.__linksHandlers = None
        return

    def init(self):
        self.__urlMacros = URLMacros()
        addListener = g_eventBus.addListener
        for eventType, handlerName in viewitems(_LISTENERS):
            handler = getattr(self, handlerName, None)
            if not handler:
                _logger.error(b'Handler is not found %s %s', eventType, handlerName)
                continue
            if not callable(handler):
                _logger.error(b'Handler is invalid %s %s %r', eventType, handlerName, handler)
                continue
            addListener(eventType, handler)

        return

    def fini(self):
        if self.__urlMacros is not None:
            self.__urlMacros.clear()
            self.__urlMacros = None
        removeListener = g_eventBus.removeListener
        for eventType, handlerName in viewitems(_LISTENERS):
            handler = getattr(self, handlerName, None)
            if handler is not None:
                removeListener(eventType, handler)

        super(ExternalLinksHandler, self).fini()
        return

    def open(self, url):
        if not url:
            _logger.error(b'URL is empty %r', url)
            return
        handled = False
        for handler in self._getHandlers():
            handled = handler.handle(url)
            if handled:
                break

        if not handled:
            _logger.error(b'Cant handle external link: %s', url)
        return

    @adisp_async
    @adisp_process
    def getURL(self, name, params=None, callback=lambda *args: None):
        urlSettings = GUI_SETTINGS.lookup(name)
        if urlSettings:
            url = yield self.__urlMacros.parse(str(urlSettings), params)
        else:
            url = yield lambda callback: callback(b'')
        callback(url)
        return

    def externalAllowed(self, url):
        for handler in self._getHandlers():
            result = handler.checkHandle(url)
            if result.handled:
                return result.externalAllowed

        return False

    def _handleSpecifiedURL(self, event):
        self.open(event.url)
        return

    @adisp_process
    def __openParsedUrl(self, urlName, params=None):
        parsedUrl = yield self.getURL(urlName, params)
        self.open(parsedUrl)
        return

    def _handleParsedURL(self, event):
        self.__openParsedUrl(event.url)
        return

    def _handleOpenRegistrationURL(self, _):
        self.__openParsedUrl(b'registrationURL')
        return

    def _handleOpenRecoveryPasswordURL(self, _):
        self.__openParsedUrl(b'recoveryPswdURL')
        return

    def _handleOpenPaymentURL(self, _):
        self.__openParsedUrl(b'paymentURL')
        return

    def _handleSecuritySettingsURL(self, _):
        self.__openParsedUrl(b'securitySettingsURL')
        return

    def _handleClanRulesURL(self, _):
        self.__openParsedUrl(b'clanRulesURL')
        return

    def _handleSupportURL(self, _):
        self.__openParsedUrl(b'supportURL')
        return

    def _handleMigrationURL(self):
        self.__openParsedUrl(b'migrationURL')
        return

    def _handleFortDescription(self, _):
        self.__openParsedUrl(b'fortDescription')
        return

    def _handleClanSearch(self, _):
        self.__openParsedUrl(b'clanSearch')
        return

    def _handleClanCreate(self, _):
        self.__openParsedUrl(b'clanCreate')
        return

    def _handleInvitesManagementURL(self, _):
        self.__openParsedUrl(b'invitesManagementURL')
        return

    def _handleGmSummaryURL(self, _):
        self.__openParsedUrl(b'globalMapSummary')
        return

    def _handleGmPromoSummaryURL(self, _):
        self.__openParsedUrl(b'globalMapPromoSummary')
        return

    def _handleGmCapURL(self, _):
        self.__openParsedUrl(b'globalMapCap')
        return

    def _handleGmPromoURL(self, _):
        self.__openParsedUrl(b'globalMapPromo')
        return

    def _handleOpenPremShopURL(self, _):
        self.__openParsedUrl(b'premShopURL')
        return

    def _handleFrontlineChangesURL(self, _):
        self.__openParsedUrl(b'frontlineChangesURL')
        return

    def _handleTokenShopURL(self, event):
        self.__openParsedUrl(b'tokenShopURL', event.params)
        return

    def _handleWotPlusSteamShopURL(self, _):
        self.__openParsedUrl(b'wotPlusSteamURL')
        return

    def _handleWotPlusShopURL(self, _):
        self.__openParsedUrl(b'wotPlusShopURL')
        return

    def _handleSteamSubscriptionManagementURL(self, _):
        self.__openParsedUrl(b'steamSubscriptionManagementURL')
        return

    def _handleLootBoxesListURL(self, _):
        self.__openParsedUrl(b'lootBoxesListURL')
        return

    def _handleReportContentURL(self, _):
        self.__openParsedUrl(b'reportContentURL')
        return

    def _handleOpenBundleStepsURL(self, _):
        self.__openParsedUrl(b'openBundleStepsURL')
        return

    def _getHandlers(self):
        if not self.__linksHandlers:
            self.__linksHandlers = []
            if self.__loginManager.isWgcSteam:
                self.__linksHandlers.append(external.PremShopLinksHandler())
                self.__linksHandlers.append(external.AddPlatformTagLinksHandler())
                self.__linksHandlers.append(external.PremShopLinksForArgsUrlHandler())
                self.__linksHandlers.append(external.AddPlatformTagLinksToArgsUrlHandler())
            self.__linksHandlers.append(external.OpenBrowserHandler())
        return self.__linksHandlers
