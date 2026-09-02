from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
from white_tiger.gui.Scaleform.daapi.view.battle.markers2d.plugins import WhiteTigerBaseAreaMarkerPlugin, WhiteTigerVehicleMarkerPlugin

class WhiteTigerMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF = b'white_tiger|whiteTigerBattleMarkersApp.swf'

    def _setupPlugins(self, arenaVisitor):
        setup = super(WhiteTigerMarkersManager, self)._setupPlugins(arenaVisitor)
        setup[b'area_markers'] = WhiteTigerBaseAreaMarkerPlugin
        setup[b'vehicles'] = WhiteTigerVehicleMarkerPlugin
        return setup
