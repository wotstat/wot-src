from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.vehicle_view_states import SelectedViewState

class FunRandomVehicleViewState(SelectedViewState, FunSubModesWatcher):

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return cls._funRandomCtrl.isOnlyFunRandomVehicle(vehicle.item)

    def setCustomizationVisible(self, customizationVisible):
        self._isCustomizationVisible = customizationVisible
        return

    def setEliteShown(self, eliteShown):
        self._isEliteShown = eliteShown
        return

    def setLevelShown(self, levelShown):
        self._isLevelShown = levelShown
        return

    def setMaintenanceVisible(self, maintenanceVisible):
        self._isMaintenanceVisible = maintenanceVisible
        return

    def setRoleShown(self, roleShown):
        self._isRoleShown = roleShown
        return

    def _resolveVehicleState(self, vehicle):
        super(FunRandomVehicleViewState, self)._resolveVehicleState(vehicle)
        self.__resolveStateByCurrentSubMode(vehicle)
        return

    @hasDesiredSubMode()
    def __resolveStateByCurrentSubMode(self, vehicle):
        self.getDesiredSubMode().resolveVehicleViewState(self, vehicle)
        return
