import logging, plugins
from gui.Scaleform.daapi.view.battle.epic.minimap import EpicMinimapComponent
_logger = logging.getLogger(__name__)
_RADAR_PLUGIN = b'radar'
_VEHICLES_PLUGIN = b'vehicles'

class BattleRoyaleMinimapComponent(EpicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(BattleRoyaleMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup[b'personal'] = plugins.BattleRoyalePersonalEntriesPlugin
        setup[b'deathZones'] = plugins.DeathZonesPlugin
        setup[_RADAR_PLUGIN] = plugins.BattleRoyaleRadarPlugin
        setup[b'airdrop'] = plugins.AirDropPlugin
        setup[_VEHICLES_PLUGIN] = plugins.BattleRoyaleVehiclePlugin
        setup[b'pinging'] = plugins.BattleRoyalMinimapPingPlugin
        setup[b'area'] = plugins.BattleRoyalStaticMarkerPlugin
        return setup

    def _populate(self):
        super(BattleRoyaleMinimapComponent, self)._populate()
        radarPlugin = self.getPlugin(_RADAR_PLUGIN)
        if radarPlugin:
            vehiclesPlugin = self.getPlugin(_VEHICLES_PLUGIN)
            if vehiclesPlugin:
                vehiclesPlugin.setRadarPlugin(radarPlugin)
                return
            _logger.error(b'Vehicles plugin has not been found!')
        else:
            _logger.error(b'Radar plugin has not been found!')
        _logger.error(b'Vehicles markers can not be initialized properly!')
        return
