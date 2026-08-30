import logging, weakref, BigWorld
from battle_royale.gui.battle_control.controllers.notification_manager import INotificationManagerListener
from debug_utils import LOG_ERROR, LOG_WARNING
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.app_loader.decorators import sf_battle
from gui.battle_control import avatar_getter
from gui.battle_control.view_components import ViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID, COUNTDOWN_STATE
from gui.battle_control.arena_info.interfaces import ISpawnController
from gui.shared.utils.scheduled_notifications import PeriodicNotifier
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class ISpawnListener(object):

    def setSpawnPoints(self, points):
        return

    def showSpawnPoints(self):
        return

    def closeSpawnPoints(self):
        return

    def updatePoint(self, vehicleId, pointId, prevPointId):
        return

    def updateCloseTime(self, timeLeft, state):
        return

    def updateRespawnTime(self, timeLeft):
        return

    def updateBlockToRessurecTime(self, blockTime):
        return

    def updateLives(self, livesLeft, prev):
        return

    def onSelectPoint(self, pointId):
        return


class SpawnController(ViewComponentsController, ISpawnController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, notificationManager):
        super(SpawnController, self).__init__()
        self.__ingameMenu = None
        self.__isSpawnPointsVisible = False
        self.__pointsByVehicle = {}
        self.__closeTime = 0
        self.__cdState = COUNTDOWN_STATE.WAIT
        self.__notifier = self.__createNotifier()
        self.notificationManager = weakref.ref(notificationManager)
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.SPAWN_CTRL

    def startControl(self, *args):
        return

    def stopControl(self):
        if self._app and self._app.containerManager:
            self._app.containerManager.onViewAddedToContainer -= self.__onViewAddedToContainer
        self.__notifier.stopNotification()
        self.__notifier.clear()
        self.__notifier = None
        self.notificationManager = None
        return

    def setViewComponents(self, *components):
        for component in components:
            if isinstance(component, INotificationManagerListener):
                component.addNotificationManager(self.notificationManager())

        self._viewComponents.extend(components)
        self.__updateCloseTime()
        return

    def showSpawnPoints(self, points):
        if self._app:
            self._app.containerManager.onViewAddedToContainer += self.__onViewAddedToContainer
        else:
            _logger.warning(b'App reference is still None!')
        self.__isSpawnPointsVisible = True
        for viewComponent in self._viewComponents:
            viewComponent.setSpawnPoints(points)
            viewComponent.showSpawnPoints()

        return

    def showRespawnPoints(self):
        if self.__isSpawnPointsVisible:
            return
        self.__isSpawnPointsVisible = True
        for viewComponent in self._viewComponents:
            viewComponent.showSpawnPoints()

        return

    def setupCloseTime(self, closeTime):
        self.__closeTime = closeTime
        self.__cdState = COUNTDOWN_STATE.START
        self.__notifier.startNotification()
        return

    def updateTeamSpawnKeyPoints(self, points):
        if not self.__isSpawnPointsVisible:
            return
        else:
            arenaDP = self.__sessionProvider.getArenaDP()
            for point in points:
                pointId = point[b'guid']
                vehicleId = point[b'vehID']
                if vehicleId == arenaDP.getPlayerVehicleID():
                    continue
                prevPoint = self.__pointsByVehicle.get(vehicleId, None)
                if prevPoint != pointId:
                    for viewComponent in self._viewComponents:
                        viewComponent.updatePoint(vehicleId, pointId, prevPoint)

                    self.__pointsByVehicle[vehicleId] = pointId

            return

    def updateRespawnTimer(self, respawnTime):
        for viewComponent in self._viewComponents:
            viewComponent.updateRespawnTime(respawnTime)

        return

    def updateBlockToRessurecTimer(self, blockTime):
        for viewComponent in self._viewComponents:
            viewComponent.updateBlockToRessurecTime(blockTime)

        return

    def updateLives(self, lives, prev):
        for viewComponent in self._viewComponents:
            viewComponent.updateLives(lives, prev)

        return

    def closeSpawnPoints(self):
        self.__closeSpawnPoints()
        return

    def chooseSpawnKeyPoint(self, pointId, isRespawn=False):
        for viewComponent in self._viewComponents:
            viewComponent.onSelectPoint(pointId)

        if not isRespawn:
            avatar_getter.getArena().teamInfo.spawnKeyPointTeamInfo.cell.chooseSpawnKeyPoint(pointId)
        return

    def placeVehicle(self):
        avatar_getter.getArena().teamInfo.spawnKeyPointTeamInfo.cell.placeVehicle()
        self.__closeSpawnPoints()
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

    @property
    def viewComponents(self):
        return self._viewComponents

    @sf_battle
    def _app(self):
        return

    def __updateCloseTime(self):
        for viewComponent in self._viewComponents:
            viewComponent.updateCloseTime(self._getDeltaTime(), self.__cdState)

        return

    def _getDeltaTime(self):
        return max(self.__closeTime - BigWorld.serverTime(), 0)

    def __createNotifier(self):
        return PeriodicNotifier(self._getDeltaTime, self.__updateCloseTime, (1,))

    def __closeSpawnPoints(self):
        if self._app:
            self._app.containerManager.onViewAddedToContainer -= self.__onViewAddedToContainer
        if self.__notifier:
            self.__notifier.stopNotification()
        self.__isSpawnPointsVisible = False
        for viewComponent in self._viewComponents:
            viewComponent.closeSpawnPoints()

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
