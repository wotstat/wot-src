import logging
from adisp import adisp_process
from gui import DialogsInterface
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.clans.cache_providers.base_provider import IBaseProvider
from gui.clans.clan_helpers import isStrongholdsEnabled
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.notify_center.actions import OpenInternalBrowser
from gui.notify_center.proxy_data import ShowInBrowserItem
from helpers import dependency
from skeletons.gui.game_control import IBrowserController
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)

class ClientStrongholdProvider(IBaseProvider, IGlobalListener):
    lobbyContext = dependency.descriptor(ILobbyContext)
    browserCtrl = dependency.descriptor(IBrowserController)

    def __init__(self):
        super(ClientStrongholdProvider, self).__init__()
        self.__tabActive = False
        self.__entityActive = False
        self.__unitActive = False
        self.__browserID = None
        if self.prbEntity:
            self.__checkSwitch()
        return

    def start(self):
        self.startGlobalListening()
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        g_eventBus.addListener(events.StrongholdEvent.STRONGHOLD_ACTIVATED, self.__onStrongholdsActivate, EVENT_BUS_SCOPE.STRONGHOLD)
        g_eventBus.addListener(events.StrongholdEvent.STRONGHOLD_DEACTIVATED, self.__onStrongholdsDeactivate, EVENT_BUS_SCOPE.STRONGHOLD)
        g_eventBus.addListener(events.StrongholdEvent.STRONGHOLD_LOADED, self.__onStrogholdLoaded, EVENT_BUS_SCOPE.STRONGHOLD)
        from gui.Scaleform.daapi.view.lobby.strongholds.web_handlers import createStrongholdsWebHandlers
        ShowInBrowserItem.addWebHandler(b'stronghold', createStrongholdsWebHandlers())
        OpenInternalBrowser.addWebHandler(b'stronghold', createStrongholdsWebHandlers())
        return

    def stop(self, withClear=False):
        self.stopGlobalListening()
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        g_eventBus.removeListener(events.StrongholdEvent.STRONGHOLD_ACTIVATED, self.__onStrongholdsActivate, EVENT_BUS_SCOPE.STRONGHOLD)
        g_eventBus.removeListener(events.StrongholdEvent.STRONGHOLD_DEACTIVATED, self.__onStrongholdsDeactivate, EVENT_BUS_SCOPE.STRONGHOLD)
        g_eventBus.removeListener(events.StrongholdEvent.STRONGHOLD_LOADED, self.__onStrogholdLoaded, EVENT_BUS_SCOPE.STRONGHOLD)
        ShowInBrowserItem.removeWebHandler(b'stronghold')
        OpenInternalBrowser.removeWebHandler(b'stronghold')
        return

    def onPrbEntitySwitched(self):
        self.__checkSwitch()
        return

    def isTabActive(self):
        return self.__tabActive

    def loadUrl(self, url):
        browser = self.browserCtrl.getBrowser(self.__browserID)
        if browser is not None:
            browser.navigate(url)
        else:
            _logger.info(b'BrowserController has not browser with id: %s', self.__browserID)
        return

    def __onServerSettingChanged(self, diff):
        if b'strongholdSettings' in diff and b'isStrongholdsEnabled' in diff[b'strongholdSettings']:
            enabled = diff[b'strongholdSettings'][b'isStrongholdsEnabled']
            if not enabled:
                if self.__tabActive or self.__entityActive:
                    if self.__tabActive:
                        g_eventBus.handleEvent(g_entitiesFactories.makeLoadEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_HANGAR)), scope=EVENT_BUS_SCOPE.LOBBY)
                    if not self.__unitActive:
                        self.__leave()
                        self.__showPopupDlg()
        return

    @adisp_process
    def __leave(self):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction())
        return

    def __checkSwitch(self):
        entity = self.prbEntity
        flags = entity.getFunctionalFlags()
        entityActive = flags & FUNCTIONAL_FLAG.STRONGHOLD > 0
        unitActive = flags & FUNCTIONAL_FLAG.UNIT > 0 and entityActive
        switched = unitActive is not self.__unitActive
        if switched:
            isStrongholdsDisabled = not isStrongholdsEnabled()
            if isStrongholdsDisabled and self.__unitActive:
                self.__showPopupDlg()
        self.__entityActive = entityActive
        self.__unitActive = unitActive
        return

    def __onStrongholdsActivate(self, _):
        self.__tabActive = True
        return

    def __onStrongholdsDeactivate(self, _):
        self.__tabActive = False
        self.__browserID = None
        return

    def __onStrogholdLoaded(self, event):
        self.__browserID = event.ctx.get(b'browserID')
        return

    @adisp_process
    def __showPopupDlg(self):
        yield DialogsInterface.showI18nInfoDialog(b'fortDisabled')
        return
