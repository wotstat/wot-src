from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class VehicleHealthBroadcastListenerComponent(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onEnterWorld(self, prereqs=None):
        return

    def onLeaveWorld(self):
        return

    def handleKey(self, isDown, key, mods):
        return

    def onBecomePlayer(self):
        return

    def onBecomeNonPlayer(self):
        return

    def onVehicleHealthChanged(self, vehicleID, newHealth, attackerID, attackReasonID):
        self.guiSessionProvider.setVehicleHealth(False, vehicleID, newHealth, attackerID, attackReasonID)
        return
