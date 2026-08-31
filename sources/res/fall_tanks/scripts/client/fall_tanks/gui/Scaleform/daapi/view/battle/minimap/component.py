from __future__ import absolute_import
from constants import IS_DEVELOPMENT
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicTeleportPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import VehicleMechanicsCollectionMinimapPlugin
from fall_tanks.gui.Scaleform.daapi.view.battle.minimap.plugins import FallTanksGlobalSettingsPlugin, FallTanksPersonalEntriesPlugin, FallTanksArenaVehiclesPlugin

class FallTanksMinimapComponent(MinimapComponent):

    def hasMinimapGrid(self):
        return True

    def _setupPlugins(self, arenaVisitor):
        setup = {b'settings': FallTanksGlobalSettingsPlugin, 
           b'personal': FallTanksPersonalEntriesPlugin, 
           b'vehicles': FallTanksArenaVehiclesPlugin, 
           b'vehicleMechanics': VehicleMechanicsCollectionMinimapPlugin}
        if IS_DEVELOPMENT:
            setup[b'teleport'] = ClassicTeleportPlugin
        return setup
