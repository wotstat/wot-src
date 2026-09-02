import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import uniprof

class VehicleRemovalController(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onBecomePlayer(self):
        return

    def handleKey(self, isDown, key, mods):
        return

    def onBecomeNonPlayer(self):
        return

    @uniprof.regionDecorator(label=b'VehicleRemovalController.removeVehicle', scope=b'wrap')
    def removeVehicle(self, vehID):
        self.sessionProvider.shared.feedback.onVehicleMarkerRemoved(vehID)
        vehicle = BigWorld.entity(vehID)
        if vehicle is None:
            return
        else:
            vehicle.show(False)
            return
