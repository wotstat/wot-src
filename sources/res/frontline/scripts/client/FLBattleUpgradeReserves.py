import BigWorld
from ReservesEvents import randomReservesEvents

class FLBattleUpgradeReserves(BigWorld.DynamicScriptComponent):

    def onEnterWorld(self, *args):
        return

    def onLeaveWorld(self, *args):
        return

    def set_upgradeReadinessTime(self, _):
        vehicle = self.entity
        if vehicle.id == BigWorld.player().playerVehicleID:
            randomReservesEvents.onUpdate(self.upgradeReadinessTime.totalTime, self.upgradeReadinessTime.reason)
        return
