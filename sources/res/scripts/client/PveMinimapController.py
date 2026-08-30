from __future__ import absolute_import
from constants import PVE_MINIMAP_DEFAULT_ZOOM, PVE_MINIMAP_DEFAULT_BORDERS
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from script_component.DynamicScriptComponent import DynamicScriptComponent

class PveMinimapController(DynamicScriptComponent):

    def set_minimapData(self, prev):
        if self.minimapData.zoomLevel != prev.zoomLevel:
            self._sendZoomUpdated()
        elif self.minimapData.minimapBorders != prev.minimapBorders:
            self._sendMinimapBorders()
        return

    def _onAvatarReady(self):
        if self.minimapData.zoomLevel != PVE_MINIMAP_DEFAULT_ZOOM:
            self._sendZoomUpdated()
        elif self.minimapData.minimapBorders != PVE_MINIMAP_DEFAULT_BORDERS:
            self._sendMinimapBorders()
        return

    def _sendZoomUpdated(self):
        g_eventBus.handleEvent(events.ScalableBattleMinimapEvent(events.ScalableBattleMinimapEvent.ZOOM_UPDATED, {b'zoomLevel': (self.minimapData.zoomLevel)}), EVENT_BUS_SCOPE.BATTLE)
        return

    def _sendMinimapBorders(self):
        g_eventBus.handleEvent(events.ScalableBattleMinimapEvent(events.ScalableBattleMinimapEvent.BORDERS_UPDATED, {b'minimapBorders': (self.minimapData.minimapBorders)}), EVENT_BUS_SCOPE.BATTLE)
        return
