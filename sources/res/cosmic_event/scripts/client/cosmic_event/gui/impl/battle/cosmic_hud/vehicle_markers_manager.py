import functools, logging, typing, BigWorld
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.vehicle_marker_model import VehicleMarkerModel
from gui.Scaleform.daapi.view.battle.shared.markers2d import plugins, vehicle_plugins
from gui.Scaleform.daapi.view.battle.shared.markers2d.settings import CommonMarkerType
from shared_utils import safeCancelCallback
from helpers import time_utils
if typing.TYPE_CHECKING:
    from typing import Dict
    from frameworks.wulf import Array
_logger = logging.getLogger(__name__)

class VehicleMarkersManager(plugins.IMarkersManager):
    _pluginClass = vehicle_plugins.VehicleMarkerPlugin

    def __init__(self, markersArray, markersCtrl):
        self._plugins = []
        self.__playerNameToMarker = {}
        self.__lootTimers = {}
        self._markers = markersArray
        self._markersCtrl = markersCtrl
        return

    def start(self):
        plugin = self._pluginClass(self)
        self._plugins.append(plugin)
        for p in self._plugins:
            p.init()
            p.start()

        _logger.debug(b'VehicleMarkersManager: start')
        return

    def stop(self):
        for p in self._plugins:
            p.stop()
            p.fini()

        self._plugins = []
        self.__playerNameToMarker = {}
        for markerModel in self._markers:
            self._markersCtrl.remove(markerModel.proxy)

        for timerID in self.__lootTimers.values():
            safeCancelCallback(timerID)

        self.__lootTimers = {}
        _logger.debug(b'VehicleMarkersManager: stop')
        return

    def createMarker(self, symbol, matrixProvider=None, active=True, markerType=CommonMarkerType.VEHICLE):
        _logger.debug(b'VehicleMarkersManager invoked: createMarker %s', symbol)
        markerModel = VehicleMarkerModel()
        self._markers.addViewModel(markerModel)
        return len(self._markers) - 1

    def invokeMarker(self, markerID, *signature):
        _logger.debug(b'VehicleMarkersManager invoked: invokeMarker (%s)', str(signature))
        if signature[0] == b'setVehicleInfo':
            playerFullname = signature[6]
            self._markers[markerID].setPlayerName(playerFullname)
            self.__playerNameToMarker[playerFullname] = self._markers[markerID]
        return

    def setMarkerMatrix(self, markerID, matrix):
        _logger.debug(b'VehicleMarkersManager invoked: setMarkerMatrix')
        self._markersCtrl.add(self._markers[markerID].proxy, matrix)
        return

    def setMarkerActive(self, markerID, active):
        return

    def setMarkerLocationOffset(self, markerID, minY, maxY, distForMinY, maxBoost, boostStart):
        return

    def setMarkerRenderInfo(self, markerID, minScale, offset, innerOffset, cullDistance, boundsMinScale):
        return

    def setMarkerBoundCheckEnabled(self, markerID, enable):
        return

    def setMarkerObjectInFocus(self, markerID, isInFocus):
        return

    def destroyMarker(self, markerID):
        return

    def setMarkerSticky(self, markerID, isSticky):
        return

    def _createCanvas(self, arenaVisitor):
        return

    def _setupPlugins(self, arenaVisitor):
        return

    def setResearchingState(self, playerName, state):
        marker = self.__playerNameToMarker.get(playerName)
        if not marker:
            return
        marker.setIsLootResearching(state)
        return

    def setTimeRemained(self, playerName, timeRemained):
        marker = self.__playerNameToMarker.get(playerName)
        if not marker:
            return
        marker.setLootTimer(timeRemained)
        timerID = BigWorld.callback(time_utils.ONE_SECOND, functools.partial(self.onTimerTick, marker, playerName, timeRemained))
        self.__lootTimers[playerName] = timerID
        return

    def onTimerTick(self, marker, playerName, timeRemained):
        timerID = self.__lootTimers.pop(playerName)
        if timerID is None:
            _logger.error(b'Timer for playerName %s not found! but onTimerTick has called', playerName)
            return
        else:
            timeRemained -= 1
            if timeRemained <= 0 or not marker.getIsLootResearching():
                return
            marker.setLootTimer(timeRemained)
            timerID = BigWorld.callback(time_utils.ONE_SECOND, functools.partial(self.onTimerTick, marker, playerName, timeRemained))
            self.__lootTimers[playerName] = timerID
            return
