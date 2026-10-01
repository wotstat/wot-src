from account_helpers.settings_core.settings_constants import MARKERS
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import MarkersManager
from portal.gui.Scaleform.daapi.view.battle.portal_vehicle_marker_plugins import PortalVehicleMarkerPlugin
from portal.gui.Scaleform.daapi.view.battle.shared.markers.markers2d import Portal2DAreaMarkersPlugin, PortalControlPointsPlugin

class PortalMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF = b'portal|portalBattleVehicleMarkersApp.swf'
    PORTAL_MARKER_SETTINGS = {(MARKERS.ENEMY): {b'markerBaseVehicleName': 1, 
                         b'markerAltVehicleName': 1, 
                         b'markerBasePlayerName': 0, 
                         b'markerAltPlayerName': 0, 
                         b'markerBaseHpIndicator': 1, 
                         b'markerAltHpIndicator': 1, 
                         b'markerBaseDamage': 1, 
                         b'markerAltDamage': 1, 
                         b'markerBaseIcon': 1, 
                         b'markerAltIcon': 1, 
                         b'markerBaseAimMarker2D': 0, 
                         b'markerAltAimMarker2D': 0, 
                         b'markerBaseVehicleDist': 0, 
                         b'markerAltVehicleDist': 0, 
                         b'markerBaseLevel': 0, 
                         b'markerAltLevel': 0}, 
       (MARKERS.DEAD): {b'markerBaseVehicleName': 1, 
                        b'markerAltVehicleName': 1, 
                        b'markerBasePlayerName': 1, 
                        b'markerAltPlayerName': 1, 
                        b'markerBaseHpIndicator': 0, 
                        b'markerAltHpIndicator': 0, 
                        b'markerBaseDamage': 0, 
                        b'markerAltDamage': 0, 
                        b'markerBaseIcon': 1, 
                        b'markerAltIcon': 1, 
                        b'markerBaseAimMarker2D': 0, 
                        b'markerAltAimMarker2D': 0, 
                        b'markerBaseVehicleDist': 0, 
                        b'markerAltVehicleDist': 0, 
                        b'markerBaseLevel': 0, 
                        b'markerAltLevel': 0, 
                        b'markerBaseHp': 3, 
                        b'markerAltHp': 3}, 
       (MARKERS.ALLY): {b'markerBaseVehicleName': 1, 
                        b'markerAltVehicleName': 1, 
                        b'markerBasePlayerName': 1, 
                        b'markerAltPlayerName': 1, 
                        b'markerBaseHpIndicator': 1, 
                        b'markerAltHpIndicator': 1, 
                        b'markerBaseDamage': 1, 
                        b'markerAltDamage': 1, 
                        b'markerBaseIcon': 1, 
                        b'markerAltIcon': 1, 
                        b'markerBaseAimMarker2D': 0, 
                        b'markerAltAimMarker2D': 0, 
                        b'markerBaseVehicleDist': 0, 
                        b'markerAltVehicleDist': 0, 
                        b'markerBaseLevel': 0, 
                        b'markerAltLevel': 0}}

    def _setupPlugins(self, arenaVisitor):
        setup = super(PortalMarkersManager, self)._setupPlugins(arenaVisitor)
        setup[b'vehicles'] = PortalVehicleMarkerPlugin
        setup[b'portal_2d_markers'] = Portal2DAreaMarkersPlugin
        setup[b'teamAndControlPoints'] = PortalControlPointsPlugin
        return setup

    def setMarkerSettings(self, markerSettings, notify=False):
        portalMarkerSettings = self.PORTAL_MARKER_SETTINGS.copy()
        portalMarkerSettings[MARKERS.ENEMY][b'markerBaseHp'] = markerSettings[MARKERS.ENEMY][b'markerBaseHp']
        portalMarkerSettings[MARKERS.ENEMY][b'markerAltHp'] = markerSettings[MARKERS.ENEMY][b'markerAltHp']
        portalMarkerSettings[MARKERS.ALLY][b'markerBaseHp'] = markerSettings[MARKERS.ALLY][b'markerBaseHp']
        portalMarkerSettings[MARKERS.ALLY][b'markerAltHp'] = markerSettings[MARKERS.ALLY][b'markerAltHp']
        super(PortalMarkersManager, self).setMarkerSettings(portalMarkerSettings, notify)
        return
