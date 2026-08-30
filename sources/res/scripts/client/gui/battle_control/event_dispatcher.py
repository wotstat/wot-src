from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.battle_control.avatar_getter import isVehicleAlive
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent, LoadViewEvent
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
_SCOPE = EVENT_BUS_SCOPE.BATTLE

def _makeKeyCtx(key=0, isDown=False):
    return {b'key': key, 
       b'isDown': isDown}


@dependency.replace_none_kwargs(appLoader=IAppLoader)
def _killHelpView(appLoader=None):
    battleApp = appLoader.getDefBattleApp()
    if battleApp is None:
        return False
    else:
        for alias in (VIEW_ALIAS.INGAME_HELP, VIEW_ALIAS.INGAME_DETAILS_HELP):
            view = battleApp.containerManager.getViewByKey(ViewKey(alias))
            if view is not None:
                view.destroy()
                return True

        return False


def showExtendedInfo(isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.SHOW_EXTENDED_INFO, _makeKeyCtx(isDown=isDown)), scope=_SCOPE)
    return


def choiceConsumable(key):
    g_eventBus.handleEvent(GameEvent(GameEvent.CHOICE_CONSUMABLE, _makeKeyCtx(key=key)), scope=_SCOPE)
    return


def changeAmmunitionSetup(key):
    g_eventBus.handleEvent(GameEvent(GameEvent.CHANGE_AMMUNITION_SETUP, _makeKeyCtx(key=key)), scope=_SCOPE)
    return


def toggleHelp():
    if _killHelpView():
        return
    g_eventBus.handleEvent(LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.INGAME_HELP)), scope=_SCOPE)
    return


def toggleHelpDetailed(ctx):
    if _killHelpView():
        return
    g_eventBus.handleEvent(LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.INGAME_DETAILS_HELP), ctx=ctx), scope=_SCOPE)
    return


def setMinimapCmd(key):
    g_eventBus.handleEvent(GameEvent(GameEvent.MINIMAP_CMD, _makeKeyCtx(key=key)), scope=_SCOPE)
    return


def setRadialMenuCmd(key, isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.RADIAL_MENU_CMD, _makeKeyCtx(key=key, isDown=isDown)), scope=_SCOPE)
    return


def setRespondToCalloutCmd(key, isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.RESPOND_TO_CALLOUT, _makeKeyCtx(key=key, isDown=isDown)), scope=_SCOPE)
    return


def toggleGUIVisibility():
    g_eventBus.handleEvent(GameEvent(GameEvent.TOGGLE_GUI), scope=_SCOPE)
    return


def setPlayingTimeOnArena(playingTime):
    g_eventBus.handleEvent(GameEvent(GameEvent.PLAYING_TIME_ON_ARENA, {b'time': playingTime}), scope=_SCOPE)
    return


def showIngameMenu():
    g_eventBus.handleEvent(LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.INGAME_MENU)), scope=_SCOPE)
    return


def showBattleVehicleConfigurator():
    if isVehicleAlive():
        g_eventBus.handleEvent(LoadViewEvent(SFViewLoadParams(BATTLE_VIEW_ALIASES.BATTLE_VEHICLE_CONFIGURATOR)), scope=_SCOPE)
    return


def hideBattleVehicleConfigurator():
    g_eventBus.handleEvent(GameEvent(GameEvent.HIDE_VEHICLE_UPGRADE), scope=_SCOPE)
    return


def toggleFullStats(isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.FULL_STATS, _makeKeyCtx(isDown=isDown)), scope=_SCOPE)
    return


def toggleEventStats(isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.EVENT_STATS, _makeKeyCtx(isDown=isDown)), scope=_SCOPE)
    return


def toggleFullStatsQuestProgress(isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.FULL_STATS_QUEST_PROGRESS, _makeKeyCtx(isDown=isDown)), scope=_SCOPE)
    return


def toggleFullStatsPersonalReserves(isDown):
    g_eventBus.handleEvent(GameEvent(GameEvent.FULL_STATS_PERSONAL_RESERVES, _makeKeyCtx(isDown=isDown)), scope=_SCOPE)
    return


def toggleVoipChannelEnabled(arenaBonusType=None):
    event = GameEvent(GameEvent.TOGGLE_VOIP_CHANNEL_ENABLED, {b'arenaBonusType': arenaBonusType})
    g_eventBus.handleEvent(event, scope=_SCOPE)
    return


def setNextPlayerPanelMode():
    g_eventBus.handleEvent(GameEvent(GameEvent.NEXT_PLAYERS_PANEL_MODE), scope=_SCOPE)
    return


def toggleMarkers2DVisibility():
    g_eventBus.handleEvent(GameEvent(GameEvent.MARKERS_2D_VISIBILITY), scope=_SCOPE)
    return


def toggleCrosshairVisibility():
    g_eventBus.handleEvent(GameEvent(GameEvent.CROSSHAIR_VISIBILITY), scope=_SCOPE)
    return


def toggleGunMarkerVisibility():
    g_eventBus.handleEvent(GameEvent(GameEvent.GUN_MARKER_VISIBILITY), scope=_SCOPE)
    return


def overrideCrosshairView(newMode):
    g_eventBus.handleEvent(GameEvent(GameEvent.CROSSHAIR_VIEW, {b'ctrlMode': newMode}), scope=_SCOPE)
    return


def changeTargetVehicle(vehicleID):
    g_eventBus.handleEvent(GameEvent(GameEvent.ON_TARGET_VEHICLE_CHANGED, {b'vehicleID': vehicleID}), scope=_SCOPE)
    return


def chargeReleased(keyDown=False):
    g_eventBus.handleEvent(GameEvent(GameEvent.CHARGE_RELEASED, {b'keyDown': keyDown}), scope=_SCOPE)
    return


def destroyTimersPanelShown(shown=None):
    g_eventBus.handleEvent(GameEvent(GameEvent.DESTROY_TIMERS_PANEL, {b'shown': shown}), scope=_SCOPE)
    return


def dualGunPreCharge():
    g_eventBus.handleEvent(GameEvent(GameEvent.PRE_CHARGE), scope=_SCOPE)
    return


def controlModeChange(mode):
    g_eventBus.handleEvent(GameEvent(GameEvent.CONTROL_MODE_CHANGE, {b'mode': mode}), scope=_SCOPE)
    return


def sniperCameraTransition(transitionTime, currentGunIndex):
    g_eventBus.handleEvent(GameEvent(GameEvent.SNIPER_CAMERA_TRANSITION, {b'transitionTime': transitionTime, 
       b'currentGunIndex': currentGunIndex}), scope=_SCOPE)
    return


def showCommanderCamHint(show):
    g_eventBus.handleEvent(GameEvent(GameEvent.COMMANDER_HINT, {b'show': show}), scope=_SCOPE)
    return


def togglePiercingDebugPanel():
    g_eventBus.handleEvent(GameEvent(GameEvent.TOGGLE_DEBUG_PIERCING_PANEL), scope=_SCOPE)
    return


def activateBattleContextHint():
    g_eventBus.handleEvent(GameEvent(GameEvent.BATTLE_CONTEXT_HINT_ACTIVATED), scope=_SCOPE)
    return
