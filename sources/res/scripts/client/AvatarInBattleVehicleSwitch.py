from __future__ import absolute_import
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from helpers import dependency
from script_component.ScriptComponent import ScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class AvatarInBattleVehicleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def set_vehicleSpawnList(self, _):
        if self._isAvatarReady:
            self.__updateAllVehsList()
        return

    def set_spawnInfoForVehicle(self, _):
        if self._isAvatarReady:
            self.__updateCurrentVehicle()
        return

    def confirmSelection(self):
        self.cell.confirmVehicleSelection()
        return

    def chooseVehicle(self, newCD):
        self.cell.chooseVehicle(newCD)
        return

    def switchSetup(self, vehTypeCD, groupId, layoutIdx):
        if groupId in self.spawnInfoForVehicle[b'vehDisabledSetupSwitches']:
            return
        self.cell.switchSetup(vehTypeCD, groupId, layoutIdx)
        return

    def _onAvatarReady(self):
        self.__updateAllVehsList()
        if self.spawnInfoForVehicle:
            self.__updateCurrentVehicle()
        return

    def __updateAllVehsList(self):
        self.__sessionProvider.dynamic.prebattleSetup.setAvailableVehicles(self.vehicleSpawnList)
        return

    def __updateCurrentVehicle(self):
        self.__sessionProvider.dynamic.prebattleSetup.updateVehicleInfo(self.spawnInfoForVehicle)
        return
