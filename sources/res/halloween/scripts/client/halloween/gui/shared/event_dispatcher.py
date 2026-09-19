from __future__ import absolute_import
import typing
from CurrentVehicle import HeroTankPreviewAppearance
from frameworks.wulf import WindowLayer
from BWUtil import AsyncReturn
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.dialogs.dialogs import showSingleDialog
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE, g_eventBus, events
from gui.shared.event_dispatcher import showShop, _getModuleInfoViewName, showBrowserOverlayView, findAndLoadWindow
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from halloween.gui.halloween_account_settings import AccountSettingsKeys, getSettings
from halloween.gui.impl.lobby.dialogs.story_choice_dialog import StoryChoiceDialog
from halloween.gui.impl.lobby.tank_setup.dialogs.confirm_dialog import HWTankSetupConfirmDialog
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency
from gui.impl.pub.notification_commands import WindowNotificationCommand, EventNotificationCommand, NotificationEvent
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.impl import INotificationWindowController
from wg_async import wg_await, wg_async
if typing.TYPE_CHECKING:
    from typing import Optional, Callable

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def _getUrl(urlName=None, url=None, lobbyContext=None):
    hostUrl = lobbyContext.getServerSettings().shop.hostUrl
    if url:
        return hostUrl + url
    else:
        return hostUrl + (b'' if urlName is None else GUI_SETTINGS.lookup(b'hwShop').get(urlName))


def getLoadedViewByLayoutID(layoutID):
    uiLoader = dependency.instance(IGuiLoader)
    if uiLoader and uiLoader.windowsManager:
        return uiLoader.windowsManager.getViewByLayoutID(layoutID)
    else:
        return


def isViewLoaded(layoutID):
    uiLoader = dependency.instance(IGuiLoader)
    if not uiLoader or not uiLoader.windowsManager or uiLoader.windowsManager.getViewByLayoutID(layoutID):
        return True
    return False


def isViewLoadedWrap(layoutID):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if isViewLoaded(layoutID=layoutID):
                return None
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator


def showHangar():
    from halloween.gui.impl.lobby.states import HalloweenHangarState
    HalloweenHangarState.goTo()
    return


def isHangarLoaded():
    return isViewLoaded(R.views.halloween.mono.lobby.hangar())


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def showMetaIntroView(forceOpen=True, parent=None, hwCtrl=None):
    if not hwCtrl.isInfoMetaEnabled():
        return
    from halloween.gui.impl.lobby.meta_intro_view import MetaIntroWindow
    layoutID = R.views.halloween.mono.lobby.meta_intro()
    isShowed = getSettings(AccountSettingsKeys.META_INTRO_VIEW_SHOWED)
    if isViewLoaded(layoutID) or isShowed and not forceOpen:
        return
    wnd = MetaIntroWindow(parent)
    wnd.load()
    return


def showVehiclePreview(**kwargs):
    kwargs.update({b'isHiddenMenu': True})
    from halloween.gui.impl.lobby.states import HalloweenVehiclePreviewState
    HalloweenVehiclePreviewState.goTo(ctx=kwargs)
    return


def showHeroTankPreview(vehTypeCompDescr, previewAlias=VIEW_ALIAS.LOBBY_HANGAR, previousBackAlias=None, previewBackCb=None, hangarVehicleCD=None, backOutfit=None, backBtnLabel=b'', isHiddenMenu=True, isKingReward=False):
    ctx = {b'itemCD': vehTypeCompDescr, 
       b'previewAlias': previewAlias, 
       b'previewAppearance': (HeroTankPreviewAppearance()), 
       b'isHeroTank': True, 
       b'previousBackAlias': previousBackAlias, 
       b'previewBackCb': previewBackCb, 
       b'hangarVehicleCD': hangarVehicleCD, 
       b'backOutfit': backOutfit, 
       b'backBtnLabel': backBtnLabel, 
       b'isHiddenMenu': isHiddenMenu, 
       b'isKingReward': isKingReward}
    from halloween.gui.impl.lobby.states import HalloweenHeroTankPreviewState
    HalloweenHeroTankPreviewState.goTo(ctx=ctx)
    return


def showRewardPathView():
    from halloween.gui.impl.lobby.states import RewardPathState
    RewardPathState.goTo()
    return


@dependency.replace_none_kwargs(notificationsMgr=INotificationWindowController)
def showPromoWindowView(forceOpen=False, notificationsMgr=None):
    from halloween.gui.impl.lobby.promo_window_view import PromoWindow
    layoutID = R.views.halloween.mono.lobby.promo()
    isShowed = getSettings(AccountSettingsKeys.PROMO_SCREEN_SHOWED)
    if isViewLoaded(layoutID=layoutID) or isShowed and not forceOpen:
        return
    window = PromoWindow(layoutID)
    notificationsMgr.append(WindowNotificationCommand(window))
    return


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showBestiaryWindow(enemyIntCD=None, useQueue=False, notificationMgr=None):
    from halloween.gui.impl.lobby.bestiary.states import HWBestiaryOverviewState
    if useQueue:
        notificationMgr.append(EventNotificationCommand(NotificationEvent((lambda : HWBestiaryOverviewState.goTo(vehIntCD=enemyIntCD)))))
    else:
        HWBestiaryOverviewState.goTo(vehIntCD=enemyIntCD)
    return


def showDifficultyView(level, useQueue=False):
    from halloween.gui.impl.lobby.difficulty_window_view import DifficultyWindow
    layoutID = R.views.halloween.mono.lobby.difficulty_congrat()
    findAndLoadWindow(useQueue, DifficultyWindow, layoutID, level)
    return


def showComparisonWindow():
    from halloween.gui.impl.lobby.comparison_window_view import ComparisonWindow
    layoutID = R.views.halloween.mono.lobby.comparison()
    if isViewLoaded(layoutID=layoutID):
        return
    wnd = ComparisonWindow(layoutID)
    wnd.load()
    return


def showStoryChoiceWindow():
    from halloween.gui.impl.lobby.story_choice import StoryChoiceWindow
    layoutID = R.views.halloween.mono.lobby.story_choice()
    findAndLoadWindow(True, StoryChoiceWindow, layoutID)
    return


def showAwardCongratsWindow(choiceID=b'option_1'):
    from halloween.gui.impl.lobby.award_congrats_view import AwardCongratsViewWindow
    layoutID = R.views.halloween.mono.lobby.award_congrats_screen()
    if isViewLoaded(layoutID=layoutID):
        return
    wnd = AwardCongratsViewWindow(layoutID, choiceID)
    wnd.load()
    return


def showAnomaliesWindow():
    from halloween.gui.impl.lobby.states import AnomaliesState
    AnomaliesState.goTo()
    return


def showKingRewardCongratsView(artefactID, useQueue=False):
    from halloween.gui.impl.lobby.king_reward_congrats_view import KingRewardCongratsWindow
    layoutID = R.views.halloween.mono.lobby.king_reward_congrat()
    findAndLoadWindow(useQueue, KingRewardCongratsWindow, layoutID, artefactID)
    return


def showCrewSelectionWindow():
    from halloween.gui.impl.lobby.crew_showcase_view import CrewShowcaseWindow
    wnd = CrewShowcaseWindow()
    wnd.load()
    return


def showDecryptWindowView(artefactID, useQueue=False, isReward=False, disableOutro=False, disableLastArtefact=False):
    from halloween.gui.impl.lobby.decrypt_view import DecryptWindow
    findAndLoadWindow(useQueue, DecryptWindow, artefactID, isReward, disableOutro, disableLastArtefact)
    return


def showAttachmentRewardView(element, isFirstEntry, useQueue=True):
    from halloween.gui.impl.lobby.attachment_reward_view import AttachmentRewardWindow
    findAndLoadWindow(useQueue, AttachmentRewardWindow, element, isFirstEntry)
    return


def showTwitchConExchangeView(useQueue=True):
    from halloween.gui.impl.lobby.reward_selection_view import RewardSelectionWindow
    layoutID = R.views.halloween.mono.lobby.reward_selection()
    findAndLoadWindow(useQueue, RewardSelectionWindow, layoutID)
    return


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def showIntroVideo(hwCtrl=None):
    if not hwCtrl.isIntroVideoEnabled():
        return
    url = GUI_SETTINGS.lookup(b'hwIntroVideo')
    showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))
    return


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def showInfoPage(hwCtrl=None):
    if not hwCtrl.isInfoPageEnabled():
        return
    url = GUI_SETTINGS.lookup(b'infoPageHalloween')
    showBrowserOverlayView(url, HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_BROWSER, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))
    return


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController, notificationMgr=INotificationWindowController)
def showOutroVideo(useQueue=False, callbackOnClose=None, hwCtrl=None, notificationMgr=None):
    if not hwCtrl.isOutroVideoEnabled():
        return
    url = GUI_SETTINGS.lookup(b'hwOutroVideo')
    browserOverlayViewLambda = lambda : showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW), callbackOnClose=callbackOnClose)
    if useQueue:
        notificationMgr.append(EventNotificationCommand(NotificationEvent(browserOverlayViewLambda)))
    else:
        browserOverlayViewLambda()
    return


def showBattleResult(arenaUniqueId):
    from halloween.gui.impl.lobby.states import HalloweenBattleResultsState
    HalloweenBattleResultsState.goTo(arenaUniqueId=arenaUniqueId)
    return


def showHalloweenShopAll():
    showShop(_getUrl(b'hwShopAll'))
    return


def showHalloweenShopVehicle():
    showShop(_getUrl(b'hwShopVehicle'))
    return


def showHalloweenShopBundle(bundleUrl):
    showShop(_getUrl(url=bundleUrl))
    return


def showBundleWindow(**kwargs):
    from halloween.gui.impl.lobby.states import HalloweenExchangeScreenState
    HalloweenExchangeScreenState.goTo(**kwargs)
    return


@wg_async
def showHWTankSetupConfirmDialog(items, vehicle=None, startState=None, parent=None):
    from gui.impl.dialogs import dialogs
    result = yield wg_await(dialogs.showSingleDialogWithResultData(layoutID=R.views.lobby.tanksetup.dialogs.Confirm(), wrappedViewClass=HWTankSetupConfirmDialog, items=items, vehicle=vehicle, startState=startState, parent=parent))
    raise AsyncReturn(result)
    return


@wg_async
def showAbilitiesIncompleteConfirm(parent=None):
    from halloween.gui.impl.lobby.dialogs.abilities_incomplete_dialog import AbilitiesIncompleteDialog
    from gui.impl.dialogs import dialogs
    result = yield wg_await(dialogs.showSingleDialogWithResultData(layoutID=R.views.halloween.mono.lobby.dialogs.abilities_incomplete_confirm(), wrappedViewClass=AbilitiesIncompleteDialog, parent=parent))
    raise AsyncReturn(result)
    return


@wg_async
def showStoryChoiceDialog(choice):
    result = yield wg_await(showSingleDialog(layoutID=R.views.halloween.mono.lobby.dialogs.story_choice_confirm(), wrappedViewClass=StoryChoiceDialog, choice=choice))
    raise AsyncReturn(result)
    return


def showModuleInfo(itemCD, vehicleDescr):
    itemCD = int(itemCD)
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_MODULE_INFO, _getModuleInfoViewName(itemCD, vehicleDescr)), ctx={b'moduleCompactDescr': itemCD, 
       b'vehicleDescr': vehicleDescr}), EVENT_BUS_SCOPE.LOBBY)
    return


def closeViewsByID(layoutIDs):
    uiLoader = dependency.instance(IGuiLoader)
    if not uiLoader or not uiLoader.windowsManager:
        return
    for layoutID in layoutIDs:
        view = uiLoader.windowsManager.getViewByLayoutID(layoutID)
        if view:
            view.destroyWindow()

    return
