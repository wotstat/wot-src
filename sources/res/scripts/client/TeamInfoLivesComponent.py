import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent

class TeamInfoLivesComponent(DynamicScriptComponent):
    onTeamLivesUpdated = Event.Event()

    def onEnterWorld(self, *args):
        self.onTeamLivesUpdated()
        return

    def set_teamLives(self, prev):
        self.onTeamLivesUpdated()
        return

    def getLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get(b'lives', 0)

    def getLockedLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get(b'lockedLives', 0)

    def getUsedLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get(b'usedLives', 0)

    def getVehicleLives(self, vehicleID):
        for vl in self.teamLives:
            if vl[b'vehicleID'] == vehicleID:
                return dict(vl)

        return {}
