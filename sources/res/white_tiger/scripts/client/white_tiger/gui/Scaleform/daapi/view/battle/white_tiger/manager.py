from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
from gui.shared.gui_items.marker_items import MarkerParamsFactory, MarkerItem
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask as FLAG
from gui.Scaleform.daapi.view.battle.shared.minimap.settings import CONTAINER_NAME
from white_tiger.gui.Scaleform.daapi.view.battle.white_tiger import markers as WhiteTigerMarkers
from white_tiger.gui.Scaleform.daapi.view.battle.white_tiger.plugins import WhiteTigerVehicleMarkerPlugin, WhiteTigerEventBusPlugin, WhiteTigerBaseAreaMarkerPlugin
WT_MARKERS = {(MarkerItem.ANOMALY): {(FLAG.MINIMAP_MARKER): [
                                                {b'clazz': (WhiteTigerMarkers.AnomalyMarkerComponent), 
                                                   b'symbol': b'WTAnomalyMinimapEntryUI', 
                                                   b'container': (CONTAINER_NAME.ICONS), 
                                                   b'onlyTranslation': True}]}, 
   (MarkerItem.GEN_ON): {(FLAG.MARKER_2D): [
                                          {b'symbol': (WhiteTigerVehicleMarkerPlugin.WT_GENERATOR_MARKER), 
                                             b'clazz': (WhiteTigerMarkers.World2DGeneratorMarkerComponentOn), 
                                             b'alpha': 1, 
                                             b'isSticky': True}], 
                         (FLAG.MINIMAP_MARKER): [
                                               {b'clazz': (WhiteTigerMarkers.MinimapGeneratorMarkerComponentOn), 
                                                  b'symbol': b'WTGeneratorMinimapEntryUI', 
                                                  b'container': (CONTAINER_NAME.ICONS), 
                                                  b'onlyTranslation': True, 
                                                  b'alpha': 1}]}, 
   (MarkerItem.GEN_OFF): {(FLAG.MARKER_2D): [
                                           {b'symbol': (WhiteTigerVehicleMarkerPlugin.WT_GENERATOR_MARKER), 
                                              b'clazz': (WhiteTigerMarkers.World2DGeneratorMarkerComponentOff), 
                                              b'alpha': 0.5, 
                                              b'isSticky': True}], 
                          (FLAG.MINIMAP_MARKER): [
                                                {b'clazz': (WhiteTigerMarkers.MinimapGeneratorMarkerComponentOff), 
                                                   b'symbol': b'WTGeneratorMinimapEntryUI', 
                                                   b'container': (CONTAINER_NAME.ICONS), 
                                                   b'onlyTranslation': True, 
                                                   b'alpha': 0.5}]}, 
   (MarkerItem.DOME): {b'offset': (0, 20, 0), 
                       (FLAG.MARKER_2D): [
                                        {b'symbol': (WhiteTigerVehicleMarkerPlugin.WT_DOME_MARKER), 
                                           b'clazz': (WhiteTigerMarkers.World2DIndexedMarkerComponent), 
                                           b'isSticky': False}]}}

class WhiteTigerMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF = b'white_tiger|white_tiger_battle_vehicle_markers.swf'

    def _setupPlugins(self, arenaVisitor):
        setup = super(WhiteTigerMarkersManager, self)._setupPlugins(arenaVisitor)
        setup[b'vehicles'] = WhiteTigerVehicleMarkerPlugin
        setup[b'eventBus'] = WhiteTigerEventBusPlugin
        setup[b'area_markers'] = WhiteTigerBaseAreaMarkerPlugin
        return setup

    def startPlugins(self):
        super(WhiteTigerMarkersManager, self).startPlugins()
        MarkerParamsFactory.MARKER_DATA.update(WT_MARKERS)
        return
