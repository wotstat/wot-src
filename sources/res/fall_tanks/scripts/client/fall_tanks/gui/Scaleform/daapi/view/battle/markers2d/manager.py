from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.markers2d import plugins, MarkersManager
from fall_tanks.gui.Scaleform.daapi.view.battle.markers2d.vehicle_plugins import FallTanksSettingsPlugin, FallTanksVehicleMarkerPlugin

class FallTanksMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF = b'fall_tanks|fallTanksBattleVehicleMarkersApp.swf'

    def _setupPlugins(self, arenaVisitor):
        setup = {b'settings': FallTanksSettingsPlugin, 
           b'eventBus': (plugins.EventBusPlugin), 
           b'controlMode': (plugins.ControlModePlugin), 
           b'vehiclesTargets': (plugins.VehicleMarkerTargetPlugin), 
           b'vehicles': FallTanksVehicleMarkerPlugin}
        return setup
