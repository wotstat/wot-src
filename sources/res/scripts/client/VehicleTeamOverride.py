from gui.battle_control import avatar_getter
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleTeamOverride(DynamicScriptComponent):

    def __init__(self):
        super(VehicleTeamOverride, self).__init__()
        self.__originalTeam = None
        return

    def onDestroy(self):
        self.__updateVehicleTeam(self.__originalTeam)
        super(VehicleTeamOverride, self).onDestroy()
        return

    def _onAvatarReady(self):
        self.__originalTeam = self.__getCurrentTeam()
        self.__updateVehicleTeam(self.newTeam)
        return

    def __getVehicleInfo(self):
        arena = avatar_getter.getArena()
        vInfo = arena.vehicles.get(self.entity.id) if arena else {}
        return vInfo or {}

    def __getCurrentTeam(self):
        vInfo = self.__getVehicleInfo()
        return vInfo.get(b'team')

    def __updateVehicleTeam(self, team):
        vInfo = self.__getVehicleInfo()
        if not team or vInfo.get(b'team') == team:
            return
        vInfo[b'team'] = team
        arena = avatar_getter.getArena()
        arena.onVehicleUpdated(self.entity.id)
        arena.onTeamKiller(self.entity.id, False)
        return
