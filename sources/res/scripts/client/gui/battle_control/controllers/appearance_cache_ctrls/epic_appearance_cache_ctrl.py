from gui.battle_control.controllers.appearance_cache_ctrls import getWholeVehModels
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController
from items.vehicles import VehicleDescriptor

class EpicAppearanceCacheController(DefaultAppearanceCacheController):
    SUPPLY_VEHICLES = (b'germany:G00_Artilleriebunker', b'germany:G00_Feuerbunker', b'germany:G00_Startgestell', b'ussr:R00_Baloon')

    def arenaLoadCompleted(self):
        super(EpicAppearanceCacheController, self).arenaLoadCompleted()
        self._precacheExtraResources()
        return

    def _precacheExtraResources(self):
        for vehicleTypeName in self.SUPPLY_VEHICLES:
            descr = VehicleDescriptor(typeName=vehicleTypeName)
            self._appearanceCache.loadResources(descr.makeCompactDescr(), getWholeVehModels(descr))

        return
