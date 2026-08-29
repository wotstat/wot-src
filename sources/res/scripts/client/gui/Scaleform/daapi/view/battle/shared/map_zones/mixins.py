from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class MapZonesListener(object):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def startListen(self):
        mapZones = self._sessionProvider.shared.mapZones
        if mapZones:
            mapZones.onMarkerToZoneAdded += self._onMarkerToZoneAdded
            mapZones.onMarkerFromZoneRemoved += self._onMarkerFromZoneRemoved
            mapZones.onMarkerProgressUpdated += self._onMarkerProgressUpdated
            mapZones.onZoneTransformed += self._onZoneTransformed
            mapZones.onTransformedZoneRemoved += self._onTransformedZoneRemoved
        return

    def stopListen(self):
        mapZones = self._sessionProvider.shared.mapZones
        if mapZones:
            mapZones.onMarkerToZoneAdded -= self._onMarkerToZoneAdded
            mapZones.onMarkerFromZoneRemoved -= self._onMarkerFromZoneRemoved
            mapZones.onMarkerProgressUpdated -= self._onMarkerProgressUpdated
            mapZones.onZoneTransformed -= self._onZoneTransformed
            mapZones.onTransformedZoneRemoved -= self._onTransformedZoneRemoved
        return

    def _onMarkerToZoneAdded(self, zoneMarker, matrix):
        return

    def _onMarkerFromZoneRemoved(self, zoneMarker):
        return

    def _onMarkerProgressUpdated(self, zoneMarker):
        return

    def _onZoneTransformed(self, zone):
        return

    def _onTransformedZoneRemoved(self, zone):
        return
