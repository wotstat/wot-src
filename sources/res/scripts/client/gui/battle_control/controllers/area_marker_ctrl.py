import logging, math
from functools import partial
import Math, math_utils, BigWorld
from helpers import dependency
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from shared_utils import findFirst
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_controller import BaseMarkerController
_logger = logging.getLogger(__name__)

def fetchEntityMatrix(entityID):
    entity = BigWorld.entities.get(entityID)
    if entity is None:
        return
    else:
        return entity.matrix


class AreaMarkersController(BaseMarkerController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(AreaMarkersController, self).__init__()
        self._battleCtx = None
        self._arenaVisitor = None
        self._vehiclesAreaMarkerHandler = VehiclesAreaMarkerHandler(self)
        return

    def startControl(self, battleCtx, arenaVisitor):
        self._battleCtx = battleCtx
        self._arenaVisitor = arenaVisitor
        self.init()
        return

    def stopControl(self):
        self._battleCtx = None
        self._arenaVisitor = None
        self._vehiclesAreaMarkerHandler.clear()
        self.stop()
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.AREA_MARKER

    def getPluginID(self):
        return b'area_markers'

    def spaceLoadCompleted(self):
        self.start()
        return

    def setVehiclesAreaMarkerParams(self, vehiclesAreaMarkerParams):
        handler = self._vehiclesAreaMarkerHandler
        handler.unpackVehiclesAreaMarkerParams(vehiclesAreaMarkerParams)
        handler.vehiclesAreaMarkerUpdate()
        return

    def _tickUpdate(self):
        super(AreaMarkersController, self)._tickUpdate()
        player = BigWorld.player()
        if player is None:
            return
        else:
            vehicle = player.getVehicleAttached()
            observableVehiclePosition = vehicle.position if vehicle else None
            for marker in self._markers.itervalues():
                if marker.isEmpty():
                    continue
                distanceToArea = marker.getDistanceToArea(observableVehiclePosition)
                if not self._isMarkerActuallyVisibleImpl(marker, distanceToArea):
                    marker.setVisible(False)
                    continue
                marker.setVisible(self._globalVisibility)
                marker.update(int(math.ceil(max(0, distanceToArea))))

            return

    def removeAllMarkersAtPoint(self):
        markersIDs = self.allMarkersID
        vehiclesMarkersIDs = self._vehiclesAreaMarkerHandler.getVehiclesMarkersIDs()
        removeList = set(markersIDs) - set(vehiclesMarkersIDs)
        for markerID in removeList:
            self.removeMarker(markerID)

        return

    def isMarkerActuallyVisible(self, marker):
        player = BigWorld.player()
        if player is None:
            return False
        else:
            vehicle = player.getVehicleAttached()
            observableVehiclePosition = vehicle.position if vehicle else None
            distanceToArea = marker.getDistanceToArea(observableVehiclePosition)
            return self._isMarkerActuallyVisibleImpl(marker, distanceToArea)

    def _isMarkerActuallyVisibleImpl(self, marker, distanceToArea):
        conditionDistance = marker.disappearingRadius
        if conditionDistance <= 0:
            return True
        else:
            isHidden = distanceToArea is None or (conditionDistance < distanceToArea if marker.reverseDisappearing else conditionDistance > distanceToArea)
            return not isHidden


class VehiclesAreaMarkerHandler(object):
    _TELEPORT_DISTANCE = 5.0
    _TICK_UPDATE = 0.01

    def __init__(self, parent):
        super(VehiclesAreaMarkerHandler, self).__init__()
        self._parent = parent
        self._vehiclesAreaMarker = {b'ID': {}, b'matrix': {}, b'lastCheckTime': {}, b'prevData': {}}
        self._vehiclesAreaMarkerParams = {}
        self._vehiclesCallback = {}
        return

    def clear(self):
        for callbackID in self._vehiclesCallback.itervalues():
            if callbackID:
                BigWorld.cancelCallback(callbackID)

        self._vehiclesCallback.clear()
        self._parent = None
        self._vehiclesAreaMarker.clear()
        self._vehiclesAreaMarkerParams.clear()
        return

    def getVehiclesMarkersIDs(self):
        vehiclesID = self._vehiclesAreaMarker[b'ID']
        return [markerID for markerData in vehiclesID.itervalues() for markerID in markerData.itervalues()]

    def vehiclesAreaMarkerUpdate(self):
        player = BigWorld.player()
        playerVehicleID = player.playerVehicleID if player else None
        if playerVehicleID is None:
            return
        else:
            markerIDs = self._vehiclesAreaMarker.get(b'ID')
            for vehicleID, params in self._vehiclesAreaMarkerParams.iteritems():
                if vehicleID == playerVehicleID:
                    continue
                markersData = params[b'markersData']
                for markerData in markersData:
                    vehMarkerList = markerIDs.get(vehicleID)
                    serverID = markerData[b'markerID']
                    if vehMarkerList is None:
                        self.__addVehicleMarker(markerData, vehicleID, params)
                        self._vehiclesCallback[vehicleID] = BigWorld.callback(self._TICK_UPDATE, partial(self.__updateVehicleMarker, vehicleID, params))
                    elif serverID not in vehMarkerList:
                        self.__addVehicleMarker(markerData, vehicleID, params, False)
                    markerID = markerIDs[vehicleID][serverID]
                    self.__updateVisibility(markerID, markerData[b'visibility'])

            return

    def unpackVehiclesAreaMarkerParams(self, params):
        for marker in params:
            vehicleID = marker[b'vehicleID']
            if vehicleID in self._vehiclesAreaMarkerParams:
                continue
            self._vehiclesAreaMarkerParams[vehicleID] = marker

        removeVehicleList = []
        removeMarkerList = []
        markerIDs = self._vehiclesAreaMarker[b'ID']
        for vehicleID in self._vehiclesAreaMarkerParams.iterkeys():
            marker = findFirst((lambda item: item[b'vehicleID'] == vehicleID), params)
            if marker is None:
                removeVehicleList.append(vehicleID)
            elif vehicleID in markerIDs:
                serverIDs = [data[b'markerID'] for data in marker[b'markersData']]
                clientIDs = markerIDs[vehicleID].keys()
                removeMarkerList.extend([(vehicleID, ID) for ID in clientIDs if ID not in serverIDs])

        for vehicleID in removeVehicleList:
            self.__removeAllVehicleMarkers(vehicleID)

        for vehicleID, markerID in removeMarkerList:
            self.__removeVehicleMarkerByID(vehicleID, markerID)

        return

    def __addVehicleMarker(self, markerData, vehicleID, params, createMatrix=True):
        vehicle = BigWorld.entities.get(vehicleID)
        vehiclesMatrix = self._vehiclesAreaMarker[b'matrix']
        positionData = params[b'positionData']
        position = positionData[b'position']
        ypr = positionData[b'ypr']
        parent = self._parent
        if createMatrix:
            vehiclePrevData = self._vehiclesAreaMarker[b'prevData']
            lastCheckTime = self._vehiclesAreaMarker[b'lastCheckTime']
            if vehicle:
                vehiclesMatrix.update({vehicleID: {b'matrix': (vehicle.matrix), b'inAoI': True}})
            else:
                vehiclesMatrix.update({vehicleID: {b'matrix': (math_utils.createRTMatrix(ypr, position)), 
                               b'inAoI': False}})
            vehiclePrevData.update({vehicleID: {b'position': position, b'ypr': (Math.Vector3(ypr))}})
            lastCheckTime.update({vehicleID: (BigWorld.time())})
        marker = parent.createMarker(vehiclesMatrix[vehicleID][b'matrix'], markerData[b'markerType'])
        markerID = parent.addMarker(marker)
        self._vehiclesAreaMarker[b'ID'].setdefault(vehicleID, {}).update({(markerData[b'markerID']): markerID})
        return

    def __removeAllVehicleMarkers(self, vehicleID):
        if vehicleID in self._vehiclesCallback:
            callbackID = self._vehiclesCallback[vehicleID]
            if callbackID:
                BigWorld.cancelCallback(callbackID)
            del self._vehiclesCallback[vehicleID]
        vehiclesAreaMarker = self._vehiclesAreaMarker
        markerIDs = vehiclesAreaMarker[b'ID']
        if vehicleID in markerIDs:
            for markerID in markerIDs[vehicleID].itervalues():
                self._parent.removeMarker(markerID)

        for dictData in vehiclesAreaMarker.itervalues():
            if vehicleID in dictData:
                del dictData[vehicleID]

        if vehicleID in self._vehiclesAreaMarkerParams:
            del self._vehiclesAreaMarkerParams[vehicleID]
        return

    def __removeVehicleMarkerByID(self, vehicleID, serverID):
        markerIDs = self._vehiclesAreaMarker[b'ID']
        if vehicleID in markerIDs:
            count = len(markerIDs[vehicleID])
            if count > 1:
                markerID = markerIDs[vehicleID][serverID]
                self._parent.removeMarker(markerID)
                del markerIDs[vehicleID][serverID]
            else:
                self.__removeAllVehicleMarkers(vehicleID)
        return

    def __updateVehicleMarker(self, vehicleID, params):
        self._vehiclesCallback[vehicleID] = None
        markerIDs = self._vehiclesAreaMarker[b'ID']
        if vehicleID not in markerIDs:
            return
        else:
            vehicle = BigWorld.entities.get(vehicleID)
            vehiclesMatrix = self._vehiclesAreaMarker[b'matrix']
            markerIDs = markerIDs[vehicleID].values()
            prevDataByVehID = self._vehiclesAreaMarker[b'prevData'][vehicleID]
            lastCheckTime = self._vehiclesAreaMarker[b'lastCheckTime']
            if vehicle:
                matrix = vehicle.matrix
                if not vehiclesMatrix[vehicleID][b'inAoI']:
                    vehiclesMatrix.update({vehicleID: {b'matrix': matrix, b'inAoI': True}})
                    for markerID in markerIDs:
                        self._parent.setMarkerMatrix(markerID, matrix)

            else:
                positionData = params[b'positionData']
                position = positionData[b'position']
                ypr = positionData[b'ypr']
                if vehiclesMatrix[vehicleID][b'inAoI']:
                    vehiclesMatrix.update({vehicleID: {b'matrix': (math_utils.createRTMatrix(ypr, position)), 
                                   b'inAoI': False}})
                    for markerID in markerIDs:
                        self._parent.setMarkerMatrix(markerID, vehiclesMatrix[vehicleID][b'matrix'])

                else:
                    matrix = vehiclesMatrix[vehicleID][b'matrix']
                    if (prevDataByVehID[b'position'] - position).length < self._TELEPORT_DISTANCE:
                        dt = BigWorld.time() - lastCheckTime[vehicleID]
                        position = matrix.translation + positionData[b'velocity'] * dt
                    if prevDataByVehID[b'position'] != ypr:
                        matrix.setRotateYPR(ypr)
                        prevDataByVehID[b'ypr'] = ypr
                    matrix.translation = position
                prevDataByVehID[b'position'] = position
                lastCheckTime[vehicleID] = BigWorld.time()
            self._vehiclesCallback[vehicleID] = BigWorld.callback(self._TICK_UPDATE, partial(self.__updateVehicleMarker, vehicleID, params))
            return

    def __updateVisibility(self, markerID, visibility):
        parent = self._parent
        if visibility:
            parent.showMarkersById(markerID)
        else:
            parent.hideMarkersById(markerID)
        return
