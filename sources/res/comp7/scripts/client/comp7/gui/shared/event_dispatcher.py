import logging, typing
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews
from frameworks.wulf import Window
from gui.Scaleform.daapi.view.lobby.vehicle_preview.configurable_vehicle_preview import OptionalBlocks
from gui.impl.gen import R
from gui.impl.pub.notification_commands import WindowNotificationCommand
from gui.server_events.events_dispatcher import ifPrbNavigationEnabled
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller, IHangarSpaceSwitchController, IIngameTournamentController
from skeletons.gui.impl import IGuiLoader, INotificationWindowController
if typing.TYPE_CHECKING:
    from enum import Enum
_logger = logging.getLogger(__name__)

def showComp7PrimeTimeWindow():
    from comp7.gui.impl.lobby.hangar.states import Comp7PrimeTimeState
    Comp7PrimeTimeState.goTo()
    return


def showComp7MetaRootTab(tabId=None, **params):
    from comp7.gui.impl.lobby.hangar import states
    if tabId == MetaRootViews.PROGRESSION or tabId is None:
        states.Comp7MetaProgressionState.goTo(**params)
    elif tabId == MetaRootViews.RANKREWARDS:
        states.Comp7MetaRankRewardsState.goTo(**params)
    elif tabId == MetaRootViews.YEARLYREWARDS:
        states.Comp7MetaYearlyRewardsState.goTo(**params)
    elif tabId == MetaRootViews.WEEKLYQUESTS:
        states.Comp7MetaWeeklyQuestsState.goTo(**params)
    elif tabId == MetaRootViews.SHOP:
        states.Comp7MetaShopState.goTo(**params)
    elif tabId == MetaRootViews.LEADERBOARD:
        states.Comp7MetaLeaderboardState.goTo(**params)
    elif tabId == MetaRootViews.YEARLYSTATISTICS:
        states.Comp7MetaYearlyStatisticsState.goTo(**params)
    return


def showComp7NoVehiclesScreen():
    from comp7.gui.impl.lobby.hangar.states import Comp7NoVehiclesState
    Comp7NoVehiclesState.goTo()
    return


def showComp7IntroScreen():
    from comp7.gui.impl.lobby.hangar.states import Comp7IntroState
    Comp7IntroState.goTo()
    return


def showComp7WCIScreen():
    from comp7.gui.impl.lobby.hangar.states import Comp7WCIState
    Comp7WCIState.goTo()
    return


def showComp7OLSScreen():
    from comp7.gui.impl.lobby.hangar.states import Comp7OLSState
    Comp7OLSState.goTo()
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showComp7WhatsNewScreen(notificationMgr=None):
    from comp7.gui.impl.lobby.whats_new_view import WhatsNewViewWindow
    notificationMgr.append(WindowNotificationCommand(WhatsNewViewWindow()))
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showComp7RanksRewardsScreen(quest, notificationMgr=None):
    from comp7.gui.impl.lobby.rewards_screen import RanksRewardsWindow
    window = RanksRewardsWindow(quest=quest)
    notificationMgr.append(WindowNotificationCommand(window))
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showComp7TokensRewardsScreen(quest, notificationMgr=None):
    from comp7.gui.impl.lobby.rewards_screen import TokensRewardsWindow
    window = TokensRewardsWindow(quest=quest)
    notificationMgr.append(WindowNotificationCommand(window))
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showComp7QualificationRewardsScreen(quests, notificationMgr=None):
    from comp7.gui.impl.lobby.rewards_screen import QualificationRewardsWindow
    window = QualificationRewardsWindow(quests=quests)
    notificationMgr.append(WindowNotificationCommand(window))
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController, comp7Ctrl=IComp7Controller)
def showComp7YearlyRewardsScreen(bonuses, showSeasonResults=True, notificationMgr=None, comp7Ctrl=None):
    from comp7.gui.impl.lobby.rewards_screen import YearlyRewardsWindow
    comp7Ctrl.tryToShowSeasonStatistics()
    window = YearlyRewardsWindow(bonuses=bonuses, showSeasonResults=showSeasonResults)
    notificationMgr.append(WindowNotificationCommand(window))
    return


def showComp7YearlyRewardsSelectionWindow(category=None):
    from comp7.gui.impl.lobby.rewards_selection_screen import Comp7RewardsSelectionWindow, Comp7SelectableRewardType
    window = Comp7RewardsSelectionWindow(Comp7SelectableRewardType.YEARLY, category)
    window.load()
    return


def showComp7WeeklyQuestsRewardsSelectionWindow(category=None):
    from comp7.gui.impl.lobby.rewards_selection_screen import Comp7RewardsSelectionWindow, Comp7SelectableRewardType
    window = Comp7RewardsSelectionWindow(Comp7SelectableRewardType.WEEKLY_QUESTS, category)
    window.load()
    return


def showComp7AllRewardsSelectionWindow():
    from comp7.gui.impl.lobby.rewards_selection_screen import Comp7RewardsSelectionWindow
    window = Comp7RewardsSelectionWindow()
    window.load()
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showComp7SelectedRewardsScreen(bonuses, notificationMgr=None):
    from comp7.gui.impl.lobby.rewards_screen import SelectedRewardsWindow
    window = SelectedRewardsWindow(bonuses=bonuses)
    notificationMgr.append(WindowNotificationCommand(window))
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController, comp7Ctrl=IComp7Controller)
def showComp7SeasonStatisticsScreen(seasonNumber=None, force=False, notificationMgr=None, comp7Ctrl=None):
    from comp7.gui.impl.lobby.season_statistics import SeasonStatisticsWindow
    if not seasonNumber:
        seasonInfo = comp7Ctrl.getPreviousSeason()
        if not seasonInfo:
            _logger.error(b'Could not show Season Statistic view, no season info.')
            return
        seasonNumber = comp7Ctrl.getPreviousSeason().getNumber()
    window = SeasonStatisticsWindow(seasonNumber=seasonNumber, saveViewing=not force)
    if force:
        window.load()
    else:
        notificationMgr.append(WindowNotificationCommand(window))
    return


def showComp7PurchaseDialog(productCode, parent=None):
    from comp7.gui.impl.lobby.dialogs.purchase_dialog import PurchaseDialogWindow
    if not PurchaseDialogWindow.getInstances():
        PurchaseDialogWindow(productCode, parent).load()
    return


@dependency.replace_none_kwargs(comp7Ctrl=IComp7Controller, spaceSwitchController=IHangarSpaceSwitchController)
def showComp7ShopPage(comp7Ctrl=None, spaceSwitchController=None):
    from comp7.gui.prb_control.entities import comp7_prb_helpers
    if not comp7Ctrl.isModePrbActive():
        spaceSwitchController.onSpaceUpdated += checkSpaceAndShowShop
        comp7_prb_helpers.selectComp7()
        return
    showComp7MetaRootTab(tabId=MetaRootViews.SHOP)
    return


@dependency.replace_none_kwargs(comp7Ctrl=IComp7Controller, spaceSwitchController=IHangarSpaceSwitchController)
def checkSpaceAndShowShop(comp7Ctrl, spaceSwitchController):
    if not comp7Ctrl.isModePrbActive():
        return
    spaceSwitchController.onSpaceUpdated -= checkSpaceAndShowShop
    showComp7MetaRootTab(tabId=MetaRootViews.SHOP)
    return


@ifPrbNavigationEnabled
@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showComp7BanWindow(arenaTypeID, time, duration, penalty, isQualification, notificationMgr=None, force=False):
    from comp7.gui.impl.lobby.hangar.notifications.punishment_notification_view import Comp7BanNotificationWindow
    wnd = Comp7BanNotificationWindow(arenaTypeID, time, duration, penalty, isQualification)
    if force:
        wnd.load()
    else:
        notificationMgr.append(WindowNotificationCommand(wnd))
    return


def showComp7InfoPage():
    from comp7.gui.comp7_constants import SELECTOR_BATTLE_TYPES
    from frameworks.wulf import WindowLayer
    from gui import GUI_SETTINGS
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    from gui.impl.lobby.mode_selector.items.base_item import getInfoPageKey
    from gui.shared.event_dispatcher import showBrowserOverlayView
    url = GUI_SETTINGS.lookup(getInfoPageKey(SELECTOR_BATTLE_TYPES.COMP7))
    showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))
    return


def showTournamentInfoPage(infoPageKey):
    from frameworks.wulf import WindowLayer
    from gui import GUI_SETTINGS
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    from gui.shared.event_dispatcher import showBrowserOverlayView
    url = GUI_SETTINGS.lookup(infoPageKey)
    showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))
    return


def showWciInfoPage():
    from comp7.gui.comp7_constants import INFO_PAGE_WCI
    showTournamentInfoPage(INFO_PAGE_WCI)
    return


def showOlsInfoPage():
    from comp7.gui.comp7_constants import INFO_PAGE_OLS
    showTournamentInfoPage(INFO_PAGE_OLS)
    return


def showComp7StylePreview(vehCD, style, **kwargs):
    from comp7.gui.impl.lobby.hangar.states import Comp7StylePreviewState
    kwargs.update({b'itemCD': vehCD, 
       b'style': style, 
       b'showBackButton': False})
    params = {b'ctx': kwargs}
    Comp7StylePreviewState.goTo(**params)
    return


def showComp7VehiclePreview(vehCD, **kwargs):
    from comp7.gui.impl.lobby.hangar.states import Comp7VehiclePreviewState
    kwargs.update({b'itemCD': vehCD, 
       b'showBackButton': False, 
       b'showCloseButton': False, 
       b'hiddenBlocks': (
                       OptionalBlocks.ALL,)})
    params = {b'ctx': kwargs}
    Comp7VehiclePreviewState.goTo(**params)
    return


@dependency.replace_none_kwargs(ingameTournamentController=IIngameTournamentController)
def showOlsOfferGiftsWindow(ingameTournamentController=None):
    from helpers.ingame_tournament_helper import IngameTournamentType
    ingameTournamentController.openOfferGifts(IngameTournamentType.OLS, overrideOnBackCallback=showComp7OLSScreen)
    return


def showComp7SeasonVehiclesStatisticsView(closeCallback=None, vehicleCD=None):
    from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
    from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS
    from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_PROFILE), ctx={b'selectedAlias': (VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE), 
       b'closeCallback': closeCallback, 
       b'battlesType': (PROFILE_DROPDOWN_KEYS.COMP7), 
       b'vehicleCD': vehicleCD}), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def showComp7VehicleBanWindow():
    from comp7.gui.impl.battle.vehicle_ban.ban_view import BanViewWindow
    uiLoader = dependency.instance(IGuiLoader)
    viewID = R.views.comp7.mono.battle.ban_view()
    if uiLoader.windowsManager.getViewByLayoutID(viewID) is None:
        window = BanViewWindow()
        window.load()
    return
