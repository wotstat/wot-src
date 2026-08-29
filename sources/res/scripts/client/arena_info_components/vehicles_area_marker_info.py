class VehiclesAreaMarkerInfo(object):

    def onEnterWorld(self):
        self._setVehiclesAreaMarkerParams()
        return

    def onLeaveWorld(self):
        return

    def set_vehiclesAreaMarkerParams(self, _):
        self._setVehiclesAreaMarkerParams()
        return

    def _setVehiclesAreaMarkerParams(self):
        areaMarkerCtrl = self.sessionProvider.shared.areaMarker
        if self.vehiclesAreaMarkerParams is not None and areaMarkerCtrl:
            areaMarkerCtrl.setVehiclesAreaMarkerParams(self.vehiclesAreaMarkerParams)
        return
