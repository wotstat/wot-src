import WWISE
from account_helpers.AccountSettings import AccountSettings, EarlyAccess
from frameworks.wulf import ViewFlags, WindowFlags, WindowLayer
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import HeaderMenuVisibilityState
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams
from gui.impl.gen import R
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shop import showBuyGoldWebOverlay, Source
from gui.sounds.filters import StatesGroup, States
from helpers import dependency
from skeletons.gui.game_control import IEarlyAccessController

def updateVisibilityHangarHeaderMenu(isVisible=False):
    state = (isVisible or HeaderMenuVisibilityState).NOTHING if 1 else HeaderMenuVisibilityState.ALL
    g_eventBus.handleEvent(events.LobbyHeaderMenuEvent(events.LobbyHeaderMenuEvent.TOGGLE_VISIBILITY, ctx={b'state': state}), EVENT_BUS_SCOPE.LOBBY)
    return


@dependency.replace_none_kwargs(earlyAccessCtrl=IEarlyAccessController)
def showEarlyAccessInfoPage(parent=None, closeCallback=None, earlyAccessCtrl=None):
    from gui.impl.lobby.common.browser_view import BrowserView, makeSettings
    from web.web_client_api import webApiCollection, ui, sound, request

    def closeCallbackWrapper(*args, **kwargs):
        if closeCallback:
            closeCallback(*args, **kwargs)
        WWISE.WW_setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_OFF)
        return

    WWISE.WW_setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_ON)
    webHandlers = webApiCollection(request.RequestWebApi, ui.OpenWindowWebApi, ui.CloseWindowWebApi, ui.OpenTabWebApi, ui.UtilWebApi, sound.SoundWebApi, sound.HangarSoundWebApi)
    window = LobbyWindow(content=BrowserView(R.views.lobby.common.BrowserView(), makeSettings(url=earlyAccessCtrl.getInfoPageLink(), viewFlags=ViewFlags.LOBBY_TOP_SUB_VIEW, returnClb=closeCallbackWrapper, restoreBackground=True, webHandlers=webHandlers)), wndFlags=WindowFlags.WINDOW, parent=parent, layer=WindowLayer.TOP_SUB_VIEW)
    window.load()
    return


def showBuyTokensWindow(parent=None, desiredVehCD=None, backCallback=None):
    from gui.impl.lobby.early_access.early_access_buy_view import EarlyAccessBuyViewWindow
    window = EarlyAccessBuyViewWindow(parent=parent, desiredVehCD=desiredVehCD, backCallback=backCallback)
    window.load()
    return


def showEarlyAccessRewardsView(bonuses):
    from gui.impl.lobby.early_access.early_access_rewards_view import EarlyAccessRewardsViewWindow
    window = EarlyAccessRewardsViewWindow(bonuses)
    window.load()
    return


def checkIntroSeen(isNextVehicleView=False):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if not AccountSettings.getEarlyAccess(EarlyAccess.INTRO_SEEN):
                showIntroView(isNextVehicleView)
            else:
                return func(*args, **kwargs)
            return

        return wrapper

    return decorator


@checkIntroSeen(isNextVehicleView=True)
def showEarlyAccessVehicleView(isFromTechTree=False, selectedVehicleCD=None):
    from gui.impl.lobby.early_access.early_access_vehicle_view import EarlyAccessVehicleView
    g_eventBus.handleEvent(events.LoadGuiImplViewEvent(GuiImplViewLoadParams(R.views.lobby.early_access.EarlyAccessVehicleView(), EarlyAccessVehicleView, ScopeTemplates.LOBBY_SUB_SCOPE), isFromTechTree=isFromTechTree, selectedVehicleCD=selectedVehicleCD), scope=EVENT_BUS_SCOPE.LOBBY)
    return


@checkIntroSeen(isNextVehicleView=False)
def showEarlyAccessQuestsView(isFromTechTree=False):
    from gui.impl.lobby.early_access.early_access_quests_view import EarlyAccessQuestsView
    g_eventBus.handleEvent(events.LoadGuiImplViewEvent(GuiImplViewLoadParams(R.views.lobby.early_access.EarlyAccessQuestsView(), EarlyAccessQuestsView, ScopeTemplates.LOBBY_SUB_SCOPE), isFromTechTree=isFromTechTree), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def showIntroView(isNextVehicleView=True):
    from gui.impl.lobby.early_access.early_access_intro_view import EarlyAccessIntroViewWindow
    window = EarlyAccessIntroViewWindow(isNextVehicleView)
    window.load()
    return


def showBuyGoldForEarlyAccess(goldAmount):
    params = {b'reason': b'', 
       b'goldPrice': goldAmount, 
       b'source': (Source.EXTERNAL)}
    showBuyGoldWebOverlay(params)
    return
