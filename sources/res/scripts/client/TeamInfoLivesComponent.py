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

    def set_respawnInfo(self, prev):
        teleport = self.entity.sessionProvider.dynamic.teleport
        if teleport is None:
            return
        else:
            teleport.onTeamRespawnInfoUpdated(self.__getRespawnInfoIDs())
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

    def getRespawnInfo(self, vehicleID):
        for entry in self.respawnInfo:
            if entry[b'vehicleID'] != vehicleID:
                continue
            return (
             entry.spawnTime, entry.delay)

        return (0.0, 0.0)

    def __getRespawnInfoIDs(self):
        if self.respawnInfo is None:
            return []
        else:
            return [entry[b'vehicleID'] for entry in self.respawnInfo]
