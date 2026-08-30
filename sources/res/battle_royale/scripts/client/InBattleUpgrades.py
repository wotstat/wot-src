import BigWorld, CGF
from aih_constants import CTRL_MODE_NAME
from wotdecorators import noexcept

class UpgradeInProgressComponent(object):
    pass


class InBattleUpgrades(BigWorld.DynamicScriptComponent):

    def onEnterWorld(self, *args):
        return

    def onLeaveWorld(self, *args):
        return

    def upgradeVehicle(self, indCD):
        self.cell.upgradeVehicle(indCD)
        return

    def onVehicleUpgraded(self, newVehCompactDescr, newVehOutfitCompactDescr):
        vehicle = self.entity
        vehicle.isUpgrading = True
        queue = CGF.CommandQueue(vehicle.entityGameObject.spaceID)
        if vehicle.entityGameObject.hasComponent(UpgradeInProgressComponent):
            queue.removeComponent(vehicle.entityGameObject, UpgradeInProgressComponent)
        queue.createComponent(vehicle.entityGameObject, UpgradeInProgressComponent)
        self.__onVehicleUpgraded(vehicle, newVehCompactDescr, newVehOutfitCompactDescr)

        def removeUpgrageInProgressComponent():
            if vehicle and vehicle.entityGameObject:
                vehicle.entityGameObject.removeComponent(UpgradeInProgressComponent)
            return

        BigWorld.callback(0, removeUpgrageInProgressComponent)
        vehicle.isUpgrading = False
        return

    @noexcept
    def __onVehicleUpgraded(self, vehicle, newVehCompactDescr, newVehOutfitCompactDescr):
        vehicleID = vehicle.id
        if vehicle.isPlayerVehicle:
            inputHandler = BigWorld.player().inputHandler
            arcadeState = None
            if inputHandler.ctrlModeName == CTRL_MODE_NAME.ARCADE:
                arcadeState = inputHandler.ctrl.camera.cloneState()
            inputHandler.onControlModeChanged(CTRL_MODE_NAME.ARCADE, initialVehicleMatrix=vehicle.matrix, arcadeState=arcadeState)
        progressionCtrl = vehicle.guiSessionProvider.dynamic.progression
        if progressionCtrl is not None:
            progressionCtrl.vehicleVisualChangingStarted(vehicleID)
        vehicle.respawnVehicle(vehicleID, newVehCompactDescr, newVehOutfitCompactDescr)
        return

    def testClientMethod(self):
        return

    def set_upgradeReadinessTime(self, prev):
        vehicle = self.entity
        ctrl = vehicle.guiSessionProvider.dynamic.progression
        if ctrl is not None and vehicle.id == BigWorld.player().playerVehicleID:
            ctrl.updateVehicleReadinessTime(self.upgradeReadinessTime.totalTime, self.upgradeReadinessTime.reason)
        return


def onBattleRoyalePrerequisites(vehicle, oldTypeDescriptor, forceReloading):
    if b'battle_royale' not in vehicle.typeDescriptor.type.tags:
        return forceReloading
    if not oldTypeDescriptor:
        return True
    for moduleName in (b'gun', b'turret', b'chassis'):
        oldModule = getattr(oldTypeDescriptor, moduleName)
        newModule = getattr(vehicle.typeDescriptor, moduleName)
        if oldModule.id != newModule.id:
            forceReloading = True
            if moduleName == b'gun' and vehicle.id == BigWorld.player().getObservedVehicleID():
                player = BigWorld.player()
                if player.isObserver():
                    vehicle.guiSessionProvider.shared.ammo.clearAmmo()
                    vehicle.guiSessionProvider.shared.ammo.setGunSettings(vehicle.id, vehicle.typeDescriptor)
                player.gunRotator.switchActiveGun([0])

    if forceReloading:
        vehicle.isForceReloading = True
    return forceReloading
