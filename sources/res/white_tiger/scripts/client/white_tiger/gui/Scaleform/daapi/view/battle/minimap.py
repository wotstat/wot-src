from __future__ import absolute_import
from future.utils import viewitems
import BattleReplay
from Math import Matrix
import typing
from white_tiger_common.wt_constants import WT_VEHICLE_TAGS
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.common import EntriesPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import ArenaVehiclesPlugin, AreaMarkerEntriesPlugin
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin
from chat_commands_consts import INVALID_MARKER_ID
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapPingPlugin
from white_tiger.gui.white_tiger_gui_constants import MINIMAP_CONTAINER_NAME, BATTLE_CTRL_ID
from white_tiger.gui.shared.events import WhiteTigerEvent
if typing.TYPE_CHECKING:
    from white_tiger.gui.battle_control.controllers.teleport_spawn_ctrl import TeleportSpawnController

class WhiteTigerSettingsPlugin(GlobalSettingsPlugin):

    def start(self):
        super(WhiteTigerSettingsPlugin, self).start()
        g_eventBus.addListener(WhiteTigerEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.addListener(WhiteTigerEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        return

    def stop(self):
        g_eventBus.removeListener(WhiteTigerEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.removeListener(WhiteTigerEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
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
        if not BattleReplay.g_replayCtrl.isPlaying:
            setup[b'pinging'] = WhiteTigerMinimapPingPlugin
        return setup

    def _populate(self):
        super(WhiteTigerMinimapComponent, self)._populate()
        g_eventBus.addListener(WhiteTigerEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.addListener(WhiteTigerEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        return

    def _dispose(self):
        g_eventBus.removeListener(WhiteTigerEvent.HIDE_SPAWN_POINTS, self.__onHideSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
        g_eventBus.removeListener(WhiteTigerEvent.SHOW_SPAWN_POINTS, self.__onShowSpawnPoints, EVENT_BUS_SCOPE.GLOBAL)
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
        if avp is not None:
            avp.hideMinimapHP()
        return

    def __onHideSpawnPoints(self, _):
        self.__isActiveSpawnPoints = False
        return


class SpawnPointsPlugin(EntriesPlugin):
    __slots__ = (b'_points',)
    _SPAWN_POINT_ENTRY = b'WhiteTigerDeploymentPointMinimapEntryUI'

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
        return self.sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.WT_BATTLE_GUI_CTRL)

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
        for pointGuid, position in viewitems(self._points):
            matrix = Matrix()
            matrix.setTranslate(position)
            self._addEntryEx(pointGuid, self._SPAWN_POINT_ENTRY, MINIMAP_CONTAINER_NAME.WT_DEPLOY, matrix, active=True)
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

    def _setVehicleInfo(self, vehicleID, entry, vInfo, guiProps, isSpotted=False):
        vehicleType = vInfo.vehicleType
        classTag = vehicleType.classTag
        name = vehicleType.shortNameWithPrefix
        if WT_VEHICLE_TAGS.BOSS in vehicleType.tags:
            classTag = b'wtboss'
        if WT_VEHICLE_TAGS.PRIORITY_BOSS in vehicleType.tags:
            classTag = b'wtSpecialBoss'
        if WT_VEHICLE_TAGS.MINIBOSS in vehicleType.tags:
            classTag = b'miniboss'
        if classTag is not None:
            entry.setVehicleInfo(not guiProps.isFriend, guiProps.name(), classTag, vInfo.isAlive())
            animation = self._ArenaVehiclesPlugin__getSpottedAnimation(entry, isSpotted)
            if animation:
                self._ArenaVehiclesPlugin__playSpottedSound(entry)
            self._invoke(entry.getID(), b'setVehicleInfo', vehicleID, classTag, name, guiProps.name(), animation)
        return

    def hideMinimapHP(self):
        self.setShowMinimapHP(False)
        return


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

    def getMarkerIdFormEntityID(self, entityID):
        for entityIDEntry, dictEntityID in viewitems(self.__entityMap):
            if dictEntityID == entityID:
                return entityIDEntry

        return INVALID_MARKER_ID


class WhiteTigerMinimapPingPlugin(ClassicMinimapPingPlugin):

    def hideHintPanel(self, instantHide=False):
        self.__isHintPanelEnabled = False
        if instantHide:
            self.parentObj.as_disableHintPanelS()
        return
