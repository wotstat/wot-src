import typing, BigWorld
from Math import Matrix
from WTTeamInfoComponent import WTCloneInfoEvent
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.common import EntriesPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import ArenaVehiclesPlugin, AreaMarkerEntriesPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.settings import CONTAINER_NAME
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin
from chat_commands_consts import INVALID_MARKER_ID, MarkerType
from wt_settings import g_wt_config
if typing.TYPE_CHECKING:
    from white_tiger.gui.battle_control.controllers.wt_teleport_spawn_ctrl import WTTeleportSpawnController

class WhiteTigerSettingsPlugin(GlobalSettingsPlugin):

    def start(self):
        super(WhiteTigerSettingsPlugin, self).start()
        g_eventBus.addListener(events.GameEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.addListener(events.GameEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        return

    def stop(self):
        g_eventBus.removeListener(events.GameEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.removeListener(events.GameEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        super(WhiteTigerSettingsPlugin, self).stop()
        return

    def __onShowSpawnPoints(self, _):
        if self._parentObj is not None:
            self._parentObj.as_setVisibleS(True)
        return

    def __onHideSpawnPoints(self, _):
        if self._parentObj is not None:
            self._parentObj.as_setVisibleS(self._isVisible)
        return


class WhiteTigerMinimapComponent(ClassicMinimapComponent):

    def __init__(self):
        super(WhiteTigerMinimapComponent, self).__init__()
        self.__isActiveSpawnPoints = False
        return

    def _setupPlugins(self, arenaVisitor):
        setup = super(WhiteTigerMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup[b'spawn_points'] = SpawnPointsPlugin
        setup[b'vehicles'] = WhiteTigerArenaVehiclesPlugin
        setup[b'settings'] = WhiteTigerSettingsPlugin
        setup[b'area_markers'] = WhiteTigerBaseAreaMarkerEntriesPlugin
        return setup

    def _populate(self):
        super(WhiteTigerMinimapComponent, self)._populate()
        g_eventBus.addListener(events.GameEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.addListener(events.GameEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        return

    def _dispose(self):
        g_eventBus.removeListener(events.GameEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.removeListener(events.GameEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        super(WhiteTigerMinimapComponent, self)._dispose()
        return

    def isModalViewShown(self):
        if self.__isActiveSpawnPoints:
            return True
        return super(WhiteTigerMinimapComponent, self).isModalViewShown()

    def __onShowSpawnPoints(self, _):
        self.__isActiveSpawnPoints = True
        mpp = self.getPlugin(b'pinging')
        if mpp is not None:
            mpp.hideHintPanel(instantHide=True)
        avp = self.getPlugin(b'vehicles')
        avp.hideMinimapHP()
        return

    def __onHideSpawnPoints(self, _):
        self.__isActiveSpawnPoints = False
        return


class SpawnPointsPlugin(EntriesPlugin):
    __slots__ = (b'_points',)
    _SPAWN_POINT_ENTRY = b'WTDeploymentPointMinimapEntryUI'

    def __init__(self, parent, clazz=None):
        super(SpawnPointsPlugin, self).__init__(parent, clazz)
        self._points = {}
        return

    def start(self):
        super(SpawnPointsPlugin, self).start()
        spawnCtrl = self._spawnCtrl
        if spawnCtrl:
            spawnCtrl.onShowSpawnPoints += self._onShowSpawnPoints
            spawnCtrl.onCloseSpawnPoints += self._onCloseSpawnPoints
            spawnCtrl.onChooseSpawnPoint += self._onChooseSpawnPoint
        return

    def stop(self):
        spawnCtrl = self._spawnCtrl
        if spawnCtrl:
            spawnCtrl.onShowSpawnPoints -= self._onShowSpawnPoints
            spawnCtrl.onCloseSpawnPoints -= self._onCloseSpawnPoints
            spawnCtrl.onChooseSpawnPoint -= self._onChooseSpawnPoint
        super(SpawnPointsPlugin, self).stop()
        return

    @property
    def _spawnCtrl(self):
        return self.sessionProvider.dynamic.teleport

    def _onShowSpawnPoints(self, points, pointGuid):
        self._removeMarkers()
        self._setPoints(points)
        self._addMarkers()
        self._choosePoint(pointGuid)
        return

    def _onCloseSpawnPoints(self):
        self._removeMarkers()
        return

    def _onChooseSpawnPoint(self, pointGuid):
        self._choosePoint(pointGuid)
        return

    def _setPoints(self, points):
        self._points = {point[b'guid']: (point[b'position'][0], 0, point[b'position'][1]) for point in points}
        return

    def _addMarkers(self):
        for pointGuid, position in self._points.iteritems():
            matrix = Matrix()
            matrix.setTranslate(position)
            self._addEntryEx(pointGuid, self._SPAWN_POINT_ENTRY, CONTAINER_NAME.WT_DEPLOY, matrix, active=True)
            self._invokeEx(pointGuid, b'setId', pointGuid)

        return

    def _removeMarkers(self):
        for pointGuid in self._points:
            self._delEntryEx(pointGuid)

        self._points = {}
        return

    def _choosePoint(self, chosenGuid):
        for pointGuid in self._points:
            self._invokeEx(pointGuid, b'setIsSelected', pointGuid == chosenGuid)

        return


class WhiteTigerArenaVehiclesPlugin(ArenaVehiclesPlugin):

    def __init__(self, parent, clazz=None):
        super(WhiteTigerArenaVehiclesPlugin, self).__init__(parent, clazz)
        self.__cloneVehicleIDs = set()
        return

    def start(self):
        super(WhiteTigerArenaVehiclesPlugin, self).start()
        g_eventBus.addListener(WTCloneInfoEvent.CLONE_VEHICLE_INFOS_UPDATED, self.__onCloneVehicleIDsUpdated, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def stop(self):
        g_eventBus.removeListener(WTCloneInfoEvent.CLONE_VEHICLE_INFOS_UPDATED, self.__onCloneVehicleIDsUpdated, scope=EVENT_BUS_SCOPE.BATTLE)
        self.__cloneVehicleIDs = set()
        super(WhiteTigerArenaVehiclesPlugin, self).stop()
        return

    def _setVehicleInfo(self, vehicleID, entry, vInfo, guiProps, isSpotted=False):
        vehicleType = vInfo.vehicleType
        classTag = vehicleType.classTag
        name = vehicleType.shortNameWithPrefix
        if g_wt_config.isAnyTypeBoss(vehicleType.compactDescr):
            classTag = b'boss'
        if self.__isCloneVehicle(vehicleID):
            classTag = b'clone'
        if classTag is not None:
            entry.setVehicleInfo(not guiProps.isFriend, guiProps.name(), classTag, vInfo.isAlive())
            animation = self._ArenaVehiclesPlugin__getSpottedAnimation(entry, isSpotted)
            if animation:
                self._ArenaVehiclesPlugin__playSpottedSound(entry)
            self._invoke(entry.getID(), b'setVehicleInfo', vehicleID, classTag, name, guiProps.name(), animation)
        return

    def __onCloneVehicleIDsUpdated(self, _):
        teamInfo = BigWorld.player().arena.teamInfo
        wtCloneInfo = getattr(teamInfo, b'wtTeamInfoComponent', None)
        if wtCloneInfo is None:
            return
        else:
            newIDs = set()
            for vehInfo in wtCloneInfo.cloneVehicleInfos:
                vid = vehInfo[b'vehicleId']
                newIDs.add(vid)

            self.__cloneVehicleIDs = newIDs
            arenaDP = self.sessionProvider.getArenaDP()
            getProps = arenaDP.getPlayerGuiProps
            for vehicleID in newIDs:
                if vehicleID not in self._entries:
                    continue
                vInfo = arenaDP.getVehicleInfo(vehicleID)
                entry = self._entries[vehicleID]
                self._setVehicleInfo(vehicleID, entry, vInfo, getProps(vehicleID, vInfo.team), isSpotted=True)

            return

    def __isCloneVehicle(self, vehicleID):
        return vehicleID in self.__cloneVehicleIDs


class WhiteTigerBaseAreaMarkerEntriesPlugin(AreaMarkerEntriesPlugin):
    __slots__ = (b'__entityMap',)

    def __init__(self, parentObj):
        super(WhiteTigerBaseAreaMarkerEntriesPlugin, self).__init__(parentObj)
        self.__entityMap = {}
        return

    def createMarker(self, uniqueID, symbol, container, matrix, active):
        model = self._addEntryEx(uniqueID, symbol, container, matrix=matrix, active=active)
        if model is not None:
            return True
        else:
            return False

    def deleteMarker(self, uniqueID):
        self._delEntryEx(uniqueID)
        return

    def setMatrix(self, uniqueID, matrix):
        self._setMatrixEx(uniqueID, matrix)
        return

    def update(self, *args, **kwargs):
        super(WhiteTigerBaseAreaMarkerEntriesPlugin, self).update()
        return

    def invoke(self, uniqueID, name, *args):
        self._invokeEx(uniqueID, name, *args)
        return

    def setActive(self, uniqueID, isActive):
        self._setActiveEx(uniqueID, isActive)
        return

    def mapCustomEntityID(self, uniqueID, entityID):
        self.__entityMap[uniqueID] = entityID
        return

    def deleteCustomEntityID(self, uniqueID):
        if uniqueID in self.__entityMap:
            self.__entityMap.pop(uniqueID)
        return

    def getMarkerIdFromEntityID(self, entityID, markerType):
        for entityIDEntry in self.__entityMap:
            if self.__entityMap[entityIDEntry] == entityID and markerType == MarkerType.BASE_MARKER_TYPE:
                return entityIDEntry

        return INVALID_MARKER_ID
