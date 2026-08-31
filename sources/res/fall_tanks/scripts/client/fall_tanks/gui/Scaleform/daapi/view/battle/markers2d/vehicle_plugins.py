from __future__ import absolute_import
from account_helpers.settings_core.settings_constants import MARKERS
from gui.Scaleform.daapi.view.battle.shared.markers2d.plugins import SettingsPlugin
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import RespawnableVehicleMarkerPlugin
from fall_tanks.gui.battle_control.arena_info.arena_vos import FallTanksKeys
from fall_tanks.gui.fall_tanks_gui_constants import FALL_TANKS_GUI_PROPS_NAME
_MARKER_SETTINGS = (
 (
  b'markerBaseIcon', False),
 (
  b'markerBaseLevel', False),
 (
  b'markerBaseHpIndicator', False),
 (
  b'markerBaseDamage', False),
 (b'markerBaseHp', 3),
 (
  b'markerBaseVehicleName', True),
 (
  b'markerBasePlayerName', True),
 (
  b'markerAltIcon', False),
 (
  b'markerAltLevel', False),
 (
  b'markerAltHpIndicator', False),
 (
  b'markerAltDamage', False),
 (b'markerAltHp', 3),
 (
  b'markerAltVehicleName', True),
 (
  b'markerAltPlayerName', True))

class FallTanksSettingsPlugin(SettingsPlugin):
    __OVERRIDES = {(MARKERS.ALLY): _MARKER_SETTINGS, 
       (MARKERS.ENEMY): _MARKER_SETTINGS, 
       (MARKERS.DEAD): _MARKER_SETTINGS}

    def __init__(self, parentObj):
        super(FallTanksSettingsPlugin, self).__init__(parentObj)
        self._overrides = self.__OVERRIDES
        return


class FallTanksVehicleMarkerPlugin(RespawnableVehicleMarkerPlugin):
    __VEHICLE_MARKER_LINKAGE = b'FallTanksVehicleMarkerUI'

    def invalidateVehiclesStats(self, arenaDP):
        for vStats in (vStats for vStats in arenaDP.getVehiclesStatsIterator() if vStats.vehicleID in self._markers):
            self.__updatePlayerPosition(self._markers[vStats.vehicleID], vStats)

        return

    def updateVehiclesStats(self, updated, arenaDP):
        for vStats in (vStats for _, vStats in updated if vStats.vehicleID in self._markers):
            self.__updatePlayerPosition(self._markers[vStats.vehicleID], vStats)

        return

    def updateTargetDesignatorSpottedMarkerTimer(self, vehicleID, handle, ctrl):
        return

    def _getMarkerSymbol(self, vehicleID):
        return self.__VEHICLE_MARKER_LINKAGE

    def _getGuiPropsName(self, vInfo, guiProps):
        return FALL_TANKS_GUI_PROPS_NAME

    def _setVehicleInfo(self, marker, vInfo, guiProps, nameParts):
        super(FallTanksVehicleMarkerPlugin, self)._setVehicleInfo(marker, vInfo, guiProps, nameParts)
        vStats = self.sessionProvider.getArenaDP().getVehicleStats(vInfo.vehicleID)
        self.__updatePlayerPosition(marker, vStats)
        return

    def _needsMarker(self, vInfo):
        vehicleID = vInfo.vehicleID
        vStats = self.sessionProvider.getArenaDP().getVehicleStats(vehicleID)
        isLeaver = vStats.gameModeSpecific.getValue(FallTanksKeys.IS_LEAVER)
        return super(FallTanksVehicleMarkerPlugin, self)._needsMarker(vInfo) and not isLeaver

    def __updatePlayerPosition(self, marker, vStats):
        position = vStats.gameModeSpecific.getValue(FallTanksKeys.RACE_POSITION)
        self._invokeMarker(marker.getMarkerID(), b'setPlayerPosition', position)
        return
