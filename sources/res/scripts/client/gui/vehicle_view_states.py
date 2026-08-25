from __future__ import absolute_import
from gui.prb_control import prbDispatcherProperty
from gui.shared.system_factory import registerVehicleViewState, collectVehicleViewStates
from shared_utils import findFirst

class IVehicleViewState(object):
    __slots__ = ()

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        raise NotImplementedError
        return

    def isLocked(self):
        raise NotImplementedError
        return

    def isEliteShown(self):
        raise NotImplementedError
        return

    def isLevelShown(self):
        raise NotImplementedError
        return

    def isRoleShown(self):
        raise NotImplementedError
        return

    def isUIShown(self):
        raise NotImplementedError
        return

    def isCrewOpsEnabled(self):
        raise NotImplementedError
        return

    def isMaintenanceEnabled(self):
        raise NotImplementedError
        return

    def isMaintenanceVisible(self):
        raise NotImplementedError
        return

    def isCustomizationEnabled(self):
        raise NotImplementedError
        return

    def isCustomizationVisible(self):
        raise NotImplementedError
        return

    def isOnlyForEventBattles(self):
        raise NotImplementedError
        return

    def isOptionalDevicesOpsEnabled(self):
        raise NotImplementedError
        return

    def getCustomizationTooltip(self):
        raise NotImplementedError
        return

    def isEasyTankEquipEnabled(self):
        raise NotImplementedError
        return

    def isEasyTankEquipVisible(self):
        raise NotImplementedError
        return


class NoPresentViewState(IVehicleViewState):

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return False

    def isLocked(self):
        return False

    def isEliteShown(self):
        return False

    def isLevelShown(self):
        return False

    def isRoleShown(self):
        return False

    def isUIShown(self):
        return False

    def isCrewOpsEnabled(self):
        return False

    def isMaintenanceEnabled(self):
        return False

    def isMaintenanceVisible(self):
        return False

    def isCustomizationEnabled(self):
        return False

    def isCustomizationVisible(self):
        return False

    def isOnlyForEventBattles(self):
        return False

    def isOptionalDevicesOpsEnabled(self):
        return False

    def getCustomizationTooltip(self):
        return b''

    def isEasyTankEquipEnabled(self):
        return False

    def isEasyTankEquipVisible(self):
        return False


class SelectedViewState(IVehicleViewState):
    __slots__ = (b'_locked', b'_isInHangar', b'_isBroken', b'_isDisabledInRent', b'_isOnlyForEventBattles', b'_isOutfitLocked', b'_isCustomizationEnabled', b'_isEliteShown', b'_isLevelShown', b'_isRoleShown', b'_isMaintenanceVisible', b'_isCustomizationVisible', b'_isEasyTankEquipEnabled', b'_isEasyTankEquipVisible')

    def __init__(self, vehicle):
        super(SelectedViewState, self).__init__()
        self._isEliteShown = self._isLevelShown = self._isRoleShown = True
        self._isMaintenanceVisible = self._isCustomizationVisible = True
        self._isEasyTankEquipVisible = True
        self._resolveVehicleState(vehicle)
        self._resolvePrbState()
        return

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return True

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def getCustomizationTooltip(self):
        return b''

    def isLocked(self):
        return self._locked

    def isEliteShown(self):
        return self._isEliteShown

    def isLevelShown(self):
        return self._isLevelShown

    def isRoleShown(self):
        return self._isRoleShown

    def isUIShown(self):
        return True

    def isCrewOpsEnabled(self):
        return not self._locked

    def isMaintenanceEnabled(self):
        return not self._locked and self._isInHangar

    def isMaintenanceVisible(self):
        return self._isMaintenanceVisible

    def isCustomizationEnabled(self):
        return self._isCustomizationEnabled

    def isCustomizationVisible(self):
        return self._isCustomizationVisible

    def isOnlyForEventBattles(self):
        return self._isOnlyForEventBattles

    def isOptionalDevicesOpsEnabled(self):
        return self.isMaintenanceEnabled() and not self._isBroken

    def isOutfitLocked(self):
        return self._isOutfitLocked

    def isEasyTankEquipEnabled(self):
        return self._isEasyTankEquipEnabled

    def isEasyTankEquipVisible(self):
        return self._isEasyTankEquipVisible

    def _resolveVehicleState(self, vehicle):
        self._isInHangar = vehicle.isInHangar() and not vehicle.isDisabled()
        self._isBroken = vehicle.isBroken()
        self._isDisabledInRent = vehicle.isDisabledInRent()
        self._isOnlyForEventBattles = vehicle.isOnlyForEventBattles()
        self._isOutfitLocked = vehicle.isOutfitLocked()
        self._isCustomizationEnabled = vehicle.isCustomizationEnabled()
        self._isEasyTankEquipEnabled = vehicle.isEasyTankEquipEnabled()
        return

    def _resolvePrbState(self):
        self._locked = False
        if self.prbDispatcher is not None:
            permission = self.prbDispatcher.getGUIPermissions()
            if permission is not None:
                self._locked = not permission.canChangeVehicle()
        return


class PremiumIGRViewState(SelectedViewState):
    __slots__ = (b'_isDisabledInPremIGR',)

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return vehicle.isPremiumIGR()

    def isMaintenanceEnabled(self):
        return super(PremiumIGRViewState, self).isMaintenanceEnabled() and not self._isDisabledInPremIGR

    def isCustomizationEnabled(self):
        return super(PremiumIGRViewState, self).isCustomizationEnabled() and not self._isDisabledInPremIGR

    def _resolveVehicleState(self, vehicle):
        super(PremiumIGRViewState, self)._resolveVehicleState(vehicle)
        self._isDisabledInPremIGR = False
        dossier = vehicle.getDossier()
        if dossier is None or not dossier.getTotalStats().getBattlesCount():
            self._isDisabledInPremIGR |= vehicle.isDisabledInPremIGR()
        return


registerVehicleViewState(PremiumIGRViewState)

class WoTPlusVehicleViewState(SelectedViewState):

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return vehicle.isWotPlus()


registerVehicleViewState(WoTPlusVehicleViewState)

def createState4CurrentVehicle(vehicle):
    if vehicle.isPresent():
        viewStates = collectVehicleViewStates()
        state = findFirst((lambda s: s.isSuitableVehicle(vehicle)), viewStates, SelectedViewState)(vehicle)
    else:
        state = NoPresentViewState()
    return state
