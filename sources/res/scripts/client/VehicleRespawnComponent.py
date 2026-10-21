import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleRespawnComponent(DynamicScriptComponent):
    onSetSpawnTime = Event.Event()

    def chooseSpawnGroup(self, groupName):
        self.cell.chooseSpawnGroup(groupName)
        return

    def set_spawnTime(self, prev):
        self.onSetSpawnTime(self.entity.id, self.spawnTime)
        return
