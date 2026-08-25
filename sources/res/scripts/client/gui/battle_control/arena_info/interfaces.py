from __future__ import absolute_import
import typing
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE
from gui.battle_control.controllers.interfaces import IBattleController
from gui.battle_control.view_components import ViewComponentsController
if typing.TYPE_CHECKING:
    from typing import Optional, Sequence, Tuple, Any, List, Dict, Callable
    from Math import Matrix
    from EmptyEntity import EmptyEntity
    from cgf_components.zone_components import ZoneMarker, RandomEventZoneUINotification, WeatherZoneUINotification
    from common_tank_structure import VehicleAppearanceCacheInfo
    from gui.battle_control.arena_info.arena_dp import ArenaDataProvider
    from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO
    from gui.battle_control.controllers.vse_hud_settings_ctrl.vse_hud_settings_ctrl import SettingsTypes, ItemSettingsTypes
    from gui.shared.gui_items.Vehicle import Vehicle
    from items.vehicles import VehicleDescr
    from points_of_interest.components import PoiStateComponent
    from pve_battle_hud import WidgetType
    from UIComponents import MinimapChangerComponent
    from vehicle_systems.CompoundAppearance import CompoundAppearance

class IArenaController(IBattleController):
    __slots__ = (b'__weakref__',)

    def getControllerID(self):
        return

    def getCtrlScope(self):
        raise NotImplementedError(b'Routine "getCtrlScope" must be implemented')
        return

    def startControl(self, battleCtx, arenaVisitor):
        return

    def stopControl(self):
        return


class IArenaLoadController(IArenaController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.LOAD

    def spaceLoadStarted(self):
        return

    def spaceLoadCompleted(self):
        return

    def updateSpaceLoadProgress(self, progress):
        return

    def arenaLoadCompleted(self):
        return


class IContactsController(IArenaController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.CONTACTS

    def invalidateUsersTags(self):
        return

    def invalidateUserTags(self, user):
        return


class IArenaVehiclesController(IArenaLoadController, IContactsController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.VEHICLES | _SCOPE.LOAD | _SCOPE.CONTACTS

    def invalidateArenaInfo(self):
        return

    def invalidateVehiclesInfo(self, arenaDP):
        return

    def invalidateVehiclesStats(self, arenaDP):
        return

    def updateVehiclesStats(self, updated, arenaDP):
        return

    def addVehicleInfo(self, vo, arenaDP):
        return

    def updateVehiclesInfo(self, updated, arenaDP):
        return

    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        return

    def invalidatePlayerStatus(self, flags, vInfoVO, arenaDP):
        return

    def invalidateFogOfWarHiddenVehiclesFlag(self, flag):
        return

    def invalidateFogOfWarEnabledFlag(self, flag):
        return

    def updateTriggeredChatCommands(self, chatCommands, arenaDP):
        return

    def updatePriorityChatCommand(self, vehicleID, chatCommand, durationMS):
        return


class ITeamsBasesController(IArenaController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.TEAMS_BASES

    def invalidateTeamBasePoints(self, baseTeam, baseID, points, timeLeft, invadersCnt, capturingStopped):
        return

    def invalidateTeamBaseCaptured(self, baseTeam, baseID):
        return

    def removeTeamsBases(self):
        return


class IArenaPeriodController(IArenaController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.PERIOD

    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        return

    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        return


class IPersonalInvitationsController(IArenaController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.INVITATIONS

    def invalidateInvitationsStatuses(self, vos, arenaDP):
        return


class IVehiclesAndPersonalInvitationsController(IArenaVehiclesController, IPersonalInvitationsController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.VEHICLES | _SCOPE.INVITATIONS | _SCOPE.CONTACTS


class IVehiclesAndPositionsController(IArenaVehiclesController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.VEHICLES | _SCOPE.POSITIONS

    def updatePositions(self, iterator):
        return


class IBattleFieldController(IArenaVehiclesController):
    __slots__ = ()

    def setVehicleHealth(self, vehicleID, newHealth):
        return

    def setVehicleData(self, data):
        return

    def setVehicleVisible(self, vehicleID, health):
        return

    def stopVehicleVisual(self, vehicleID):
        return

    def getAliveVehicles(self):
        return


class IProgressionController(IArenaLoadController):
    __slots__ = ()
    onVehicleUpgradeStarted = None
    onVehicleUpgradeFinished = None

    def getCurrentVehicle(self):
        raise NotImplementedError
        return

    def getCurrentVehicleLevel(self):
        raise NotImplementedError
        return

    def updateXP(self, xp, observedVehicleID):
        raise NotImplementedError
        return

    def mayInstallModule(self, moduleItem):
        raise NotImplementedError
        return

    def mayInstallModuleOnVehicle(self, moduleItem, vehicle):
        raise NotImplementedError
        return

    def updateVehicleXP(self):
        return

    def vehicleVisualChangingStarted(self, vehicleID):
        return

    def vehicleVisualChangingFinished(self, vehicleID):
        return

    def addRuntimeView(self, view):
        return

    def removeRuntimeView(self, view):
        return

    def vehicleUpgradeRequest(self, intCD, moduleItem):
        return

    def vehicleUpgradeResponse(self, intCD, successfullyProcessed):
        return

    def isModuleSelected(self, intCD):
        return

    def getModule(self, intCD):
        raise NotImplementedError
        return

    def getInstalledOnVehicleAnalogByIntCD(self, intCD):
        raise NotImplementedError
        return

    def getWindowCtrl(self):
        raise NotImplementedError
        return

    def updateVehicleReadinessTime(self, cooldownTime, reason):
        raise NotImplementedError
        return

    def isVehicleReady(self):
        raise NotImplementedError
        return

    def setAverageBattleLevel(self, level):
        raise NotImplementedError
        return

    @property
    def maxLevel(self):
        raise NotImplementedError
        return


class IContactsAndPersonalInvitationsController(IContactsController, IPersonalInvitationsController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.CONTACTS | _SCOPE.INVITATIONS


class IViewPointsController(IArenaLoadController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.LOAD | _SCOPE.VIEW_POINTS

    def updateViewPoints(self, viewPoints):
        return

    def updateAttachedVehicle(self, vehicleID):
        return


class IAnonymizerFakesController(IArenaVehiclesController):
    __slots__ = ()

    def getCtrlScope(self):
        return _SCOPE.VEHICLES

    def addBattleFriend(self, avatarSessionID):
        raise NotImplementedError
        return

    def removeBattleFriend(self, avatarSessionID):
        raise NotImplementedError
        return

    def addBattleIgnored(self, avatarSessionID):
        raise NotImplementedError
        return

    def removeBattleIgnored(self, avatarSessionID):
        raise NotImplementedError
        return

    def mute(self, avatarSessionID, name):
        raise NotImplementedError
        return

    def unmute(self, avatarSessionID):
        raise NotImplementedError
        return

    def addTmpIgnored(self, avatarSessionID, name):
        raise NotImplementedError
        return

    def removeTmpIgnored(self, avatarSessionID):
        raise NotImplementedError
        return


class IRadarController(object):

    def activateRadar(self):
        raise NotImplementedError
        return

    def updateRadarReadinessTime(self, radarReadinessTime):
        raise NotImplementedError
        return

    def updateRadarReadiness(self, isReady):
        raise NotImplementedError
        return

    def addRuntimeView(self, view):
        raise NotImplementedError
        return

    def removeRuntimeView(self, view):
        raise NotImplementedError
        return


class ISpawnController(object):

    def showSpawnPoints(self, points):
        raise NotImplementedError
        return


class IVehicleCountController(IArenaVehiclesController, ViewComponentsController):

    def updateAttachedVehicle(self, vehicleID):
        raise NotImplementedError
        return

    def updateLives(self, lives):
        raise NotImplementedError
        return


class IPrebattleSetupsController(IArenaPeriodController, IArenaLoadController, ViewComponentsController):

    def getPrebattleSetupsVehicle(self):
        raise NotImplementedError
        return

    def getPrebattleVehicleID(self):
        raise NotImplementedError
        return

    def getCtrlScope(self):
        return _SCOPE.PERIOD | _SCOPE.LOAD

    def isArenaLoaded(self):
        raise NotImplementedError
        return

    def isSelectionStarted(self):
        raise NotImplementedError
        return

    def stopSelection(self):
        raise NotImplementedError
        return

    def setPlayerVehicle(self, vehicleID, vehDescr):
        raise NotImplementedError
        return

    def setCrew(self, vehicleID, crew):
        raise NotImplementedError
        return

    def setDynSlotType(self, vehicleID, dynSlotTypeID):
        raise NotImplementedError
        return

    def setEnhancements(self, vehicleID, enhancements):
        raise NotImplementedError
        return

    def setPostProgression(self, vehicleID, itemCDs):
        raise NotImplementedError
        return

    def setDisabledSwitches(self, vehicleID, groupIDs):
        raise NotImplementedError
        return

    def setRespawnReloadFactor(self, vehicleID, reloadFactor):
        raise NotImplementedError
        return

    def setSetups(self, vehicleID, setups):
        raise NotImplementedError
        return

    def setSetupsIndexes(self, vehicleID, setupsIndexes):
        raise NotImplementedError
        return

    def setSiegeState(self, vehicleID, siegeState):
        raise NotImplementedError
        return

    def setVehicleAttrs(self, vehicleID, attrs):
        raise NotImplementedError
        return

    def onCurrentShellUpdate(self, vehicleID):
        raise NotImplementedError
        return

    def switchLayout(self, groupID, layoutIdx):
        raise NotImplementedError
        return

    def getSlotItem(self, group, layout, slotId):
        raise NotImplementedError
        return


class IAppearanceCacheController(IArenaVehiclesController):

    def getAppearance(self, vId, vInfo, callback=None, strCD=None, needLoad=True):
        raise NotImplementedError
        return

    def reloadAppearance(self, vId, vInfo, callback=None, strCD=None, oldStrCD=None):
        raise NotImplementedError
        return


class IPointsOfInterestController(IBattleController):
    onPoiEquipmentUsed = None
    onPoiCaptured = None
    onPoiInvaderDestroyed = None

    @staticmethod
    def getPoiState(poiID):
        raise NotImplementedError
        return

    @staticmethod
    def getPoiEntity(poiID):
        raise NotImplementedError
        return

    def getVehicleCapturingPoiGO(self, poiName, entityGameObject, vehicleID, spaceID):
        raise NotImplementedError
        return


class IPrebattleSetupController(IArenaLoadController, IArenaPeriodController, ViewComponentsController):
    onVehiclesListUpdated = None
    onVehicleChanged = None
    onBattleStarted = None
    onSelectionConfirmed = None
    onTeammateSelectionStatuses = None

    def getCtrlScope(self):
        return _SCOPE.PERIOD | _SCOPE.LOAD

    def confirmVehicleSelection(self):
        raise NotImplementedError
        return

    def isSelectionConfirmed(self):
        raise NotImplementedError
        return

    def chooseVehicle(self, newCD):
        raise NotImplementedError
        return

    def setAvailableVehicles(self, vehiclesList):
        raise NotImplementedError
        return

    @staticmethod
    def getVehiclesList():
        raise NotImplementedError
        return

    def updateVehicleInfo(self, vehicleInfo):
        raise NotImplementedError
        return

    @staticmethod
    def getCurrentVehicleInfo():
        raise NotImplementedError
        return

    def updateSpawnPoints(self, spawnPoints):
        raise NotImplementedError
        return

    def updateConfirmationStatuses(self, newStatuses):
        raise NotImplementedError
        return

    def getCurrentGUIVehicle(self):
        raise NotImplementedError
        return

    def switchPrebattleSetup(self, groupID, layoutIdx):
        raise NotImplementedError
        return

    def isVehicleStateIndicatorAllowed(self):
        raise NotImplementedError
        return


class IBRVOIPController(IArenaLoadController):
    __slots__ = ()

    @property
    def isVoipSupported(self):
        raise NotImplementedError
        return

    @property
    def isVoipEnabled(self):
        raise NotImplementedError
        return

    @property
    def isJoined(self):
        raise NotImplementedError
        return

    @property
    def isTeamVoipEnabled(self):
        raise NotImplementedError
        return

    def toggleChannelConnection(self):
        raise NotImplementedError
        return


class IMapZonesController(IBattleController):
    onMarkerToZoneAdded = None
    onMarkerFromZoneRemoved = None
    onMarkerProgressUpdated = None
    onZoneTransformed = None
    onTransformedZoneRemoved = None

    def addMarkerToZone(self, zoneMarkerAccess, matrix):
        raise NotImplementedError
        return

    def removeMarkerFromZone(self, zoneMarker):
        raise NotImplementedError
        return

    def addTransformedZone(self, zoneAccess):
        raise NotImplementedError
        return

    def removeTransformedZone(self, zone):
        raise NotImplementedError
        return

    def enterRandomEventZone(self, zone):
        raise NotImplementedError
        return

    def exitRandomEventZone(self, zone):
        raise NotImplementedError
        return

    def removeRandomEventZone(self, zone):
        raise NotImplementedError
        return

    def enterWeatherZone(self, zone):
        raise NotImplementedError
        return

    def exitWeatherZone(self, zone):
        raise NotImplementedError
        return

    def removeWeatherZone(self, zone):
        raise NotImplementedError
        return

    def getZoneMarkers(self):
        raise NotImplementedError
        return

    def getTransformedZones(self):
        raise NotImplementedError
        return


class IOverrideSettingsController(IArenaController):
    __slots__ = ()

    @property
    def defaultTab(self):
        raise NotImplementedError
        return

    @property
    def disabledTabs(self):
        raise NotImplementedError
        return

    def getCtrlScope(self):
        return _SCOPE.OVERRIDE_SETTINGS


class IAimingSoundsCtrl(IBattleController):

    def startControl(self, *_):
        return

    def stopControl(self):
        return

    def updateDispersion(self, shotFactor, multFactor, aimingFactor, idealFactor, dualAccMultFactor, dualAccFactor, idealDualAccFactor, hasDualAcc):
        raise NotImplementedError
        return


class IVSEHUDSettingsController(IBattleController):
    __slots__ = ()
    onSettingsChanged = None
    onItemSettingsChanged = None

    def setSettings(self, settingsID, settings):
        raise NotImplementedError
        return

    def getSettings(self, settingsID):
        raise NotImplementedError
        return

    def setItemSettings(self, settingsID, itemID, settings):
        raise NotImplementedError
        return

    def getItemSettings(self, settingsID, itemID):
        raise NotImplementedError
        return


class IAutoShootController(IBattleController):

    def startControl(self, *_):
        return

    def isBurstActive(self):
        raise NotImplementedError
        return

    def processShootCmd(self):
        raise NotImplementedError
        return


class IBattleSpamController(IBattleController):

    def filterAllyHitMessage(self, targetID):
        raise NotImplementedError
        return

    def filterAutoShootTracerSound(self, attackerID):
        raise NotImplementedError
        return

    def filterFullscreenEffects(self, attackerID):
        raise NotImplementedError
        return

    def filterMarkersHitState(self, targetID, stateKey):
        raise NotImplementedError
        return


class INitroController(IBattleController):

    def startControl(self, *_):
        raise NotImplementedError
        return

    def processNitroCmd(self):
        raise NotImplementedError
        return


class IW2GTBattleController(IArenaPeriodController, IArenaVehiclesController):
    onStageChanged = None

    def getCtrlScope(self):
        return _SCOPE.LOAD | _SCOPE.VEHICLES | _SCOPE.PERIOD

    @property
    def isActive(self):
        raise NotImplementedError
        return

    def isArenaSuitable(self, arena):
        raise NotImplementedError
        return
