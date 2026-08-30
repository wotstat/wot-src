import logging
from enum import IntEnum
import Event
from PlayerEvents import g_playerEvents
from constants import ARENA_PERIOD
from debug_utils import LOG_ERROR, LOG_WARNING
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.app_loader.decorators import sf_battle
from gui.battle_control import avatar_getter
from gui.battle_control.view_components import ViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID, VEHICLE_VIEW_STATE
from gui.battle_control.arena_info.interfaces import ISpawnController
from helpers import dependency, uniprof
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class SpawnType(IntEnum):
    DEFAULT = 1
    TELEPORT = 2


class ISpawnListener(object):

    def setSpawnPoints(self, points, pointId=None):
        return

    def showSpawnPoints(self):
        return

    def closeSpawnPoints(self):
        return

    def updatePoint(self, vehicleId, pointId, prevPointId):
        return

    def updateCloseTime(self, timeLeft, state):
        return

    def onSelectPoint(self, pointId):
        return

    def setSpawnType(self, spawnType):
        return


class WTTeleportSpawnController(ViewComponentsController, ISpawnController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(WTTeleportSpawnController, self).__init__()
        self.__ingameMenu = None
        self.__isSpawnPointsVisible = False
        self.__eManager = Event.EventManager()
        self.onShowSpawnPoints = Event.Event(self.__eManager)
        self.onCloseSpawnPoints = Event.Event(self.__eManager)
        self.onChooseSpawnPoint = Event.Event(self.__eManager)
        self._equipment = None
        self.onTeamLivesUpdated = Event.Event(self.__eManager)
        self.onTeamRespawnInfoUpdated = Event.Event(self.__eManager)
        self.onTeamLivesSetted = Event.Event(self.__eManager)
        return

    def setEquipment(self, equipment):
        self._equipment = equipment
        return

    def cancelEquipment(self):
        if self._equipment:
            self._equipment.deactivate()
        return

    @property
    def isSpawnPointsVisible(self):
        return self.__isSpawnPointsVisible

    def getControllerID(self):
        return BATTLE_CTRL_ID.TELEPORT_CTRL

    def startControl(self, *args):
        self.__subscribeListeners()
        return

    def stopControl(self):
        self.__unsubscribeListeners()
        if self._app and self._app.containerManager:
            self._app.containerManager.onViewAddedToContainer -= self.__onViewAddedToContainer
        self.__eManager.clear()
        self.__eManager = None
        return

    def setViewComponents(self, *components):
        self._viewComponents.extend(components)
        return

    def movingToRespawn(self):
        self.closeSpawnPoints()
        return

    def showSpawnPoints(self, points, pointGuid=None):
        uniprof.enterToRegion(b'avatar.control_mode.teleport_spawn_ctrl')
        if self._app and self._app.containerManager:
            self._app.containerManager.onViewAddedToContainer += self.__onViewAddedToContainer
        else:
            _logger.warning(b'App reference is still None!')
        self.__isSpawnPointsVisible = True
        for viewComponent in self._viewComponents:
            viewComponent.setSpawnType(SpawnType.TELEPORT if self._equipment else SpawnType.DEFAULT)
            viewComponent.setSpawnPoints(points, pointGuid)
            viewComponent.showSpawnPoints()

        self.onShowSpawnPoints(points, pointGuid)
        return

    def updateSpawnPoints(self, points, pointGuid=None):
        for viewComponent in self._viewComponents:
            viewComponent.setSpawnPoints(points, pointGuid)

        self.onShowSpawnPoints(points, pointGuid)
        return

    def closeSpawnPoints(self):
        uniprof.exitFromRegion(b'avatar.control_mode.teleport_spawn_ctrl')
        if self._app and self._app.containerManager:
            self._app.containerManager.onViewAddedToContainer -= self.__onViewAddedToContainer
        self.__isSpawnPointsVisible = False
        for viewComponent in self._viewComponents:
            viewComponent.closeSpawnPoints()

        self.onCloseSpawnPoints()
        return

    def chooseSpawnKeyPoint(self, pointId):
        for viewComponent in self._viewComponents:
            viewComponent.onSelectPoint(pointId)

        if self._equipment:
            self._equipment.apply(pointId)
            self.closeSpawnPoints()
            return
        else:
            avatar_getter.getPlayerVehicle().cell.VehicleRespawnComponent.chooseSpawnGroup(pointId)
            self._equipment = None
            self.onChooseSpawnPoint(pointId)
            return

    def addRuntimeView(self, view):
        if view in self._viewComponents:
            LOG_ERROR((b'View is already added! {}').format(view))
        elif self.__isSpawnPointsVisible:
            view.showSpawnPoints()
        self._viewComponents.append(view)
        return

    def removeRuntimeView(self, view):
        if view in self._viewComponents:
            self._viewComponents.remove(view)
        else:
            LOG_WARNING((b'View has not been found! {}').format(view))
        return

    @sf_battle
    def _app(self):
        return

    def __subscribeListeners(self):
        g_playerEvents.onArenaPeriodChange += self.__onArenaPeriodChange
        vehStateCtrl = self.__sessionProvider.shared.vehicleState
        if vehStateCtrl is not None:
            vehStateCtrl.onVehicleStateUpdated += self.__onVehicleStateUpdated
        return

    def __unsubscribeListeners(self):
        g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChange
        vehStateCtrl = self.__sessionProvider.shared.vehicleState
        if vehStateCtrl is not None:
            vehStateCtrl.onVehicleStateUpdated -= self.__onVehicleStateUpdated
        return

    def __onViewAddedToContainer(self, _, pyEntity):
        if pyEntity.alias == VIEW_ALIAS.INGAME_MENU:
            self.__ingameMenu = pyEntity
            self.__ingameMenu.onDispose += self.__onIngameMenuDisposed
        return

    def __onIngameMenuDisposed(self, _):
        if self.__isSpawnPointsVisible:
            for viewComponent in self._viewComponents:
                viewComponent.showSpawnPoints()

        if self.__ingameMenu:
            self.__ingameMenu.onDispose -= self.__onIngameMenuDisposed
            self.__ingameMenu = None
        return

    def __onArenaPeriodChange(self, period, *_):
        if period == ARENA_PERIOD.AFTERBATTLE:
            self.closeSpawnPoints()
        return

    def __onVehicleStateUpdated(self, state, *_):
        if state in (VEHICLE_VIEW_STATE.DESTROYED, VEHICLE_VIEW_STATE.CREW_DEACTIVATED):
            self.closeSpawnPoints()
        return
