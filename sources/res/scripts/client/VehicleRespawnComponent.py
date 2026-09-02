import Event, BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleRespawnComponent(DynamicScriptComponent):
    onSetSpawnTime = Event.Event()

    def _onAvatarReady(self):
        BigWorld.player().inputHandler.onPostmortemKillerVisionExit += self.showSelector
        return

    def onDestroy(self):
        BigWorld.player().inputHandler.onPostmortemKillerVisionExit -= self.showSelector
        super(VehicleRespawnComponent, self).onDestroy()
        return

    def chooseSpawnGroup(self, groupName):
        self.cell.chooseSpawnGroup(groupName)
        return

    def set_spawnTime(self, prev):
        self.onSetSpawnTime(self.entity.id, self.spawnTime)
        return

    def showSelector(self):
        if not self.spawnTime:
            return
        self.entity.guiSessionProvider.dynamic.teleport.showSpawnPoints(self.__createSpawnPoints(), self.groupName)
        return

    def updateSelector(self):
        if not self.spawnTime:
            return
        self.entity.guiSessionProvider.dynamic.teleport.updateSpawnPoints(self.__createSpawnPoints(), self.groupName)
        return

    def __createSpawnPoints(self):
        points = [{b'guid': (point[b'name']), b'position': (point[b'position'].x, point[b'position'].y)} for point in self.spawnGroups]
        return points
