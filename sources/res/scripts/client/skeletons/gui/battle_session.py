from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from typing import Any, Iterable, Optional
    from ClientArena import ClientArena
    from avatar_components.AvatarObserver import ObservedVehicleData
    from gui.armor_flashlight.interfaces import IArmorFlashlightBattleController
    from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO
    from gui.battle_control.arena_info.interfaces import IAppearanceCacheController, IArenaVehiclesController, IBattleSpamController, IMapZonesController, IOverrideSettingsController, IPointsOfInterestController, IPrebattleSetupController, IProgressionController, IRadarController, ISpawnController, IVehicleCountController, IVSEHUDSettingsController, IW2GTBattleController
    from gui.battle_control.controllers.consumables.ammo_ctrl import AmmoController
    from gui.battle_control.controllers.consumables.equipment_ctrl import EquipmentsController
    from gui.battle_control.controllers.msgs_ctrl import BattleMessagesController
    from gui.battle_control.controllers.spotting_indicators_ctrl import ISpottingIndicatorsController
    from gui.battle_control.controllers.vehicle_passenger import IVehiclePassengerController
    from gui.battle_control.controllers.vehicle_state_ctrl import VehicleStateController
    from gui.battle_control.controllers.vehicles_tracking import IVehiclesTrackingController
    from Vehicle import Vehicle

class ISharedControllersLocator(object):
    __slots__ = ()

    @property
    def ammo(self):
        raise NotImplementedError
        return

    @property
    def equipments(self):
        raise NotImplementedError
        return

    @property
    def optionalDevices(self):
        raise NotImplementedError
        return

    @property
    def prebattleSetups(self):
        raise NotImplementedError
        return

    @property
    def vehicleState(self):
        raise NotImplementedError
        return

    @property
    def vehiclePassenger(self):
        raise NotImplementedError
        return

    @property
    def vehiclesTracking(self):
        raise NotImplementedError
        return

    @property
    def hitDirection(self):
        raise NotImplementedError
        return

    @property
    def arenaLoad(self):
        raise NotImplementedError
        return

    @property
    def arenaPeriod(self):
        raise NotImplementedError
        return

    @property
    def feedback(self):
        raise NotImplementedError
        return

    @property
    def chatCommands(self):
        raise NotImplementedError
        return

    @property
    def messages(self):
        raise NotImplementedError
        return

    @property
    def drrScale(self):
        raise NotImplementedError
        return

    @property
    def privateStats(self):
        raise NotImplementedError
        return

    @property
    def crosshair(self):
        raise NotImplementedError
        return

    @property
    def personalEfficiencyCtrl(self):
        raise NotImplementedError
        return

    @property
    def anonymizerFakesCtrl(self):
        raise NotImplementedError
        return

    @property
    def viewPoints(self):
        raise NotImplementedError
        return

    @property
    def questProgress(self):
        raise NotImplementedError
        return

    @property
    def calloutCtrl(self):
        raise NotImplementedError
        return

    @property
    def spectator(self):
        raise NotImplementedError
        return

    @property
    def areaMarker(self):
        return NotImplementedError

    @property
    def arenaBorder(self):
        raise NotImplementedError
        return

    @property
    def deathzones(self):
        raise NotImplementedError
        return

    @property
    def ingameHelp(self):
        raise NotImplementedError
        return

    @property
    def mapZones(self):
        raise NotImplementedError
        return

    @property
    def killCamCtrl(self):
        raise NotImplementedError
        return

    @property
    def aimingSounds(self):
        raise NotImplementedError
        return

    @property
    def autoShootCtrl(self):
        raise NotImplementedError
        return

    @property
    def battleSpamCtrl(self):
        raise NotImplementedError
        return

    @property
    def armorFlashlight(self):
        raise NotImplementedError
        return

    @property
    def spottingIndicatorsCtrl(self):
        raise NotImplementedError
        return


class IDynamicControllersLocator(object):
    __slots__ = ()

    def getControllerByID(self, ctrlID):
        raise NotImplementedError
        return

    @property
    def debug(self):
        raise NotImplementedError
        return

    @property
    def teamBases(self):
        raise NotImplementedError
        return

    @property
    def repair(self):
        raise NotImplementedError
        return

    @property
    def progressTimer(self):
        raise NotImplementedError
        return

    @property
    def maps(self):
        raise NotImplementedError
        return

    @property
    def missions(self):
        raise NotImplementedError
        return

    @property
    def respawn(self):
        raise NotImplementedError
        return

    @property
    def dynSquads(self):
        raise NotImplementedError
        return

    @property
    def battleField(self):
        raise NotImplementedError
        return

    @property
    def progression(self):
        raise NotImplementedError
        return

    @property
    def radar(self):
        raise NotImplementedError
        return

    @property
    def spawn(self):
        raise NotImplementedError
        return

    @property
    def deathScreen(self):
        raise NotImplementedError
        return

    @property
    def vehicleCount(self):
        raise NotImplementedError
        return

    @property
    def battleHints(self):
        raise NotImplementedError
        return

    @property
    def dogTags(self):
        raise NotImplementedError
        return

    @property
    def battleNotifier(self):
        raise NotImplementedError
        return

    @property
    def soundPlayers(self):
        raise NotImplementedError
        return

    @property
    def gameNotifications(self):
        raise NotImplementedError
        return

    @property
    def appearanceCache(self):
        raise NotImplementedError
        return

    @property
    def pointsOfInterest(self):
        raise NotImplementedError
        return

    @property
    def prebattleSetup(self):
        raise NotImplementedError
        return

    @property
    def overrideSettingsController(self):
        raise NotImplementedError
        return

    @property
    def vseHUDSettings(self):
        raise NotImplementedError
        return

    @property
    def commendationsMessagesController(self):
        raise NotImplementedError
        return

    @property
    def shotsResultSound(self):
        raise NotImplementedError
        return

    @property
    def w2GTBattleController(self):
        raise NotImplementedError
        return

    @property
    def prebattleHighlightsController(self):
        raise NotImplementedError
        return


class ISquadInvitationsHandler(object):
    __slots__ = ()

    def clear(self):
        raise NotImplementedError
        return

    def send(self, sessionID):
        raise NotImplementedError
        return

    def accept(self, sessionID):
        raise NotImplementedError
        return

    def reject(self, sessionID):
        raise NotImplementedError
        return


class IClientArenaVisitor(object):
    __slots__ = ()

    def clear(self):
        raise NotImplementedError
        return

    @property
    def gui(self):
        raise NotImplementedError
        return

    @property
    def bonus(self):
        raise NotImplementedError
        return

    @property
    def type(self):
        raise NotImplementedError
        return

    @property
    def extra(self):
        raise NotImplementedError
        return

    @property
    def vehicles(self):
        raise NotImplementedError
        return

    @property
    def modifiers(self):
        raise NotImplementedError
        return

    def getComponentSystem(self):
        raise NotImplementedError
        return

    def isArenaInWaiting(self):
        raise NotImplementedError
        return

    def hasRage(self):
        raise NotImplementedError
        return

    def hasRespawns(self):
        raise NotImplementedError
        return

    def hasHealthBar(self):
        raise NotImplementedError
        return

    def hasPlayerGroups(self):
        raise NotImplementedError
        return

    def isSoloTeam(self, team):
        raise NotImplementedError
        return

    def getArenaIcon(self, subdir=b''):
        raise NotImplementedError
        return

    def getTeamSpawnPoints(self, team):
        raise NotImplementedError
        return

    def getTeamSpawnPointsIterator(self, team):
        raise NotImplementedError
        return

    def getVisibilityMinRadius(self):
        raise NotImplementedError
        return

    def getVisibilityMaxRadius(self):
        raise NotImplementedError
        return

    def getVehicleCircularAoiRadius(self):
        raise NotImplementedError
        return

    def getArenaSubscription(self):
        raise NotImplementedError
        return

    def getRoundLength(self):
        raise NotImplementedError
        return

    def isBattleEndWarningEnabled(self):
        raise NotImplementedError
        return

    def getArenaUniqueID(self):
        raise NotImplementedError
        return

    def getArenaGuiType(self):
        raise NotImplementedError
        return

    def getArenaBonusType(self):
        raise NotImplementedError
        return

    def getArenaType(self):
        raise NotImplementedError
        return

    def getArenaPeriod(self):
        raise NotImplementedError
        return

    def getArenaPeriodEndTime(self):
        raise NotImplementedError
        return

    def getArenaPeriodLength(self):
        raise NotImplementedError
        return

    def getArenaPeriodAdditionalInfo(self):
        raise NotImplementedError
        return

    def getArenaPositions(self):
        raise NotImplementedError
        return

    def getArenaExtraData(self):
        raise NotImplementedError
        return

    def getArenaModifiers(self):
        raise NotImplementedError
        return

    def getArenaVehicles(self):
        raise NotImplementedError
        return

    def getArenaStatistics(self):
        raise NotImplementedError
        return

    def isArenaFogOfWarEnabled(self):
        raise NotImplementedError
        return

    def hasGameEndMessage(self):
        raise NotImplementedError
        return

    def hasDogTag(self):
        raise NotImplementedError
        return

    def hasW2gtTag(self):
        raise NotImplementedError
        return

    def hasDynSquads(self):
        raise NotImplementedError
        return

    def hasBattleNotifier(self):
        raise NotImplementedError
        return

    def hasPointsOfInterest(self):
        raise NotImplementedError
        return

    def hasCommendationsMessages(self):
        raise NotImplementedError
        return

    def hasLiveTags(self):
        raise NotImplementedError
        return

    def isEnableExternalRespawn(self):
        raise NotImplementedError
        return

    def isArenaLeaveAllowed(self):
        raise NotImplementedError
        return


class IBattleClientCache(object):

    def getRecord(self, recordClass):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def save(self):
        raise NotImplementedError
        return

    def load(self):
        raise NotImplementedError
        return


class IArenaDataProvider(object):
    __slots__ = ()

    def clearInfo(self):
        raise NotImplementedError
        return

    def clearStats(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def defaultInfo(self):
        raise NotImplementedError
        return

    def buildVehiclesData(self, vehicles):
        raise NotImplementedError
        return

    def buildStatsData(self, stats):
        raise NotImplementedError
        return

    def addVehicleInfo(self, vehicleID, vInfo):
        raise NotImplementedError
        return

    def updateVehicleInfo(self, vID, vInfo):
        raise NotImplementedError
        return

    def updateVehicleStatus(self, vID, vInfo):
        raise NotImplementedError
        return

    def updatePlayerStatus(self, vID, vInfo):
        raise NotImplementedError
        return

    def updateVehicleStats(self, vID, vStats):
        raise NotImplementedError
        return

    def updateVehicleInteractiveStats(self, iStats):
        raise NotImplementedError
        return

    def updateGameModeSpecificStats(self, vehicleID, isStatic, stats):
        raise NotImplementedError
        return

    def updateInvitationStatus(self, avatarSessionID, include, exclude=0):
        raise NotImplementedError
        return

    def updateChatCommandState(self, vID, chatCommandState):
        raise NotImplementedError
        return

    def isRequiredDataExists(self):
        raise NotImplementedError
        return

    def getTeamsOnArena(self):
        raise NotImplementedError
        return

    def getAllyTeams(self):
        raise NotImplementedError
        return

    def getEnemyTeams(self):
        raise NotImplementedError
        return

    def isEnemyTeam(self, team):
        raise NotImplementedError
        return

    def isAllyTeam(self, team):
        raise NotImplementedError
        return

    def isMultipleTeams(self):
        raise NotImplementedError
        return

    def getMultiTeamsType(self):
        raise NotImplementedError
        return

    def getMultiTeamsIndexes(self):
        raise NotImplementedError
        return

    def getTeamIDsIterator(self):
        raise NotImplementedError
        return

    def getNumberOfTeam(self, enemy=False):
        raise NotImplementedError
        return

    def getPersonalDescription(self):
        raise NotImplementedError
        return

    def getPlayerVehicleID(self, forceUpdate=False):
        raise NotImplementedError
        return

    def getVehicleInfo(self, vID=None):
        raise NotImplementedError
        return

    def getVehicleStats(self, vID=None):
        raise NotImplementedError
        return

    def getVehiclesCountInPrebattle(self, team, prebattleID):
        raise NotImplementedError
        return

    def getSquadSizes(self):
        raise NotImplementedError
        return

    def getPlayerGuiProps(self, vID, team):
        raise NotImplementedError
        return

    def isSquadMan(self, vID, prebattleID=None):
        raise NotImplementedError
        return

    def isTeamKiller(self, vID):
        raise NotImplementedError
        return

    def isObserver(self, vID):
        raise NotImplementedError
        return

    def isPlayerObserver(self):
        raise NotImplementedError
        return

    def getVehIDByAccDBID(self, accDBID):
        raise NotImplementedError
        return

    def getVehIDBySessionID(self, avatarSessionID):
        raise NotImplementedError
        return

    def getSessionIDByVehID(self, vehID):
        raise NotImplementedError
        return

    def getVehiclesInfoIterator(self):
        raise NotImplementedError
        return

    def getAllyVehiclesInfoIterator(self):
        raise NotImplementedError
        return

    def getVehiclesStatsIterator(self):
        raise NotImplementedError
        return

    def getVehiclesItemsGenerator(self):
        raise NotImplementedError
        return

    def getActiveVehiclesGenerator(self):
        raise NotImplementedError
        return

    def getAlliesVehiclesNumber(self):
        raise NotImplementedError
        return

    def getEnemiesVehiclesNumber(self):
        raise NotImplementedError
        return

    def isAlly(self, vehicleID):
        raise NotImplementedError
        return

    def getReservesModifier(self):
        raise NotImplementedError
        return

    def getWinStatus(self, team):
        raise NotImplementedError
        return


class IBattleContext(object):

    def start(self, arenaDP):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def getArenaDP(self):
        raise NotImplementedError
        return

    def getVehIDBySessionID(self, avatarSessionID):
        raise NotImplementedError
        return

    def getSessionIDByVehID(self, vehID):
        raise NotImplementedError
        return

    def setPlayerFullNameFormatter(self, formatter):
        raise NotImplementedError
        return

    def getVehicleInfo(self, vID=None, avatarSessionID=None):
        raise NotImplementedError
        return

    def getPlayerName(self, vID=None, avatarSessionID=None):
        raise NotImplementedError
        return

    def resetPlayerFullNameFormatter(self):
        raise NotImplementedError
        return

    def createPlayerFullNameFormatter(self, showVehShortName=True, showClan=True, showRegion=True):
        raise NotImplementedError
        return

    def getPlayerFullNameParts(self, vID=None, avatarSessionID=None, pName=None, showVehShortName=True, showClan=True, showRegion=True):
        raise NotImplementedError
        return

    def getPlayerFullName(self, vID=None, avatarSessionID=None, pName=None, showVehShortName=True, showClan=True, showRegion=True):
        raise NotImplementedError
        return

    def isSquadMan(self, vID=None, avatarSessionID=None, prebattleID=None):
        raise NotImplementedError
        return

    def isTeamKiller(self, vID=None, avatarSessionID=None):
        raise NotImplementedError
        return

    def isObserver(self, vID):
        raise NotImplementedError
        return

    def isPlayerObserver(self):
        raise NotImplementedError
        return

    def isInTeam(self, teamIdx, vID=None, avatarSessionID=None):
        raise NotImplementedError
        return

    def isAlly(self, vID=None, avatarSessionID=None):
        raise NotImplementedError
        return

    def isEnemy(self, vID=None, avatarSessionID=None):
        raise NotImplementedError
        return

    def isCurrentPlayer(self, vID):
        raise NotImplementedError
        return

    def getPlayerGuiProps(self, vID, team):
        raise NotImplementedError
        return

    def getArenaTypeName(self, isInBattle=True):
        raise NotImplementedError
        return

    def getArenaDescriptionString(self, isInBattle=True):
        raise NotImplementedError
        return

    def getArenaWinString(self, isInBattle=True):
        raise NotImplementedError
        return

    def getArenaFrameLabel(self):
        raise NotImplementedError
        return

    def getBattleTypeIconPathBig(self):
        raise NotImplementedError
        return

    def getBattleTypeIconPathSmall(self):
        raise NotImplementedError
        return

    def getGuiEventType(self):
        raise NotImplementedError
        return

    def isInvitationEnabled(self):
        raise NotImplementedError
        return

    def hasSquadRestrictions(self):
        raise NotImplementedError
        return

    def getSelectedQuestIDs(self):
        raise NotImplementedError
        return

    def getSelectedQuestInfo(self):
        raise NotImplementedError
        return

    def getTeamName(self, enemy=False):
        raise NotImplementedError
        return

    def getArenaSmallIcon(self):
        raise NotImplementedError
        return

    def getArenaScreenIcon(self):
        raise NotImplementedError
        return

    def getArenaRespawnIcon(self):
        raise NotImplementedError
        return

    def setLastArenaWinStatus(self, winStatus):
        raise NotImplementedError
        return

    def extractLastArenaWinStatus(self):
        raise NotImplementedError
        return


class IBattleSessionProvider(object):
    __slots__ = (b'onBattleSessionStart', b'onBattleSessionStop', b'onUpdateObservedVehicleData')

    @property
    def shared(self):
        raise NotImplementedError
        return

    @property
    def dynamic(self):
        raise NotImplementedError
        return

    @property
    def arenaVisitor(self):
        raise NotImplementedError
        return

    @property
    def invitations(self):
        raise NotImplementedError
        return

    @property
    def battleCache(self):
        return

    @property
    def isReplayPlaying(self):
        raise NotImplementedError
        return

    def getCtx(self):
        raise NotImplementedError
        return

    def sendRequest(self, ctx, callback, allowDelay=None):
        raise NotImplementedError
        return

    def setPlayerVehicle(self, vID, vDesc):
        raise NotImplementedError
        return

    def switchVehicle(self, vehicleID):
        raise NotImplementedError
        return

    def getArenaDP(self):
        raise NotImplementedError
        return

    def addArenaCtrl(self, controller):
        raise NotImplementedError
        return

    def removeArenaCtrl(self, controller):
        raise NotImplementedError
        return

    def registerViewComponentsCtrl(self, controller):
        raise NotImplementedError
        return

    def registerViewComponents(self, *data):
        raise NotImplementedError
        return

    def addViewComponent(self, componentID, component, **kwargs):
        raise NotImplementedError
        return

    def removeViewComponent(self, componentID):
        raise NotImplementedError
        return

    def getExitResult(self):
        raise NotImplementedError
        return

    @staticmethod
    def exit():
        raise NotImplementedError
        return

    def start(self, setup):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def switchToPostmortem(self, noRespawnPossible=True, respawnAvailable=False):
        raise NotImplementedError
        return

    def updateVehicleQuickShellChanger(self, isActive):
        raise NotImplementedError
        return

    def movingToRespawnBase(self, vehicle=None):
        raise NotImplementedError
        return

    def invalidateVehicleState(self, state, value, vehicleID=0):
        raise NotImplementedError
        return

    def setVehicleHealth(self, isPlayerVehicle, vehicleID, newHealth, attackerID, attackReasonID):
        raise NotImplementedError
        return

    def repairPointAction(self, repairPointIndex, action, nextActionTime):
        raise NotImplementedError
        return

    def updateAvatarPrivateStats(self, stats):
        raise NotImplementedError
        return

    def addHitDirection(self, hitDirYaw, attackerID, damage, isBlocked, critFlags, isHighExplosive, damagedID, attackReasonID):
        raise NotImplementedError
        return

    def startVehicleVisual(self, vProxy, isImmediate=False):
        raise NotImplementedError
        return

    def stopVehicleVisual(self, vehicleID, isPlayerVehicle):
        raise NotImplementedError
        return

    def handleShortcutChatCommand(self, key):
        raise NotImplementedError
        return

    def handleContexChatCommand(self, key):
        raise NotImplementedError
        return

    def updateVehicleEffects(self, vehicle):
        raise NotImplementedError
        return

    def updateObservedVehicleData(self, vID, extraData):
        raise NotImplementedError
        return
