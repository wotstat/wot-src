import BigWorld
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from cosmic_event.gui.shared.events import Teleport

class CosmicVehicleTeleportAbilityComponent(BigWorld.DynamicScriptComponent):

    def set_teleportPosition(self, prev):
        self.__sendEvent(Teleport.PREPARED, {b'position': (self.teleportPosition)})
        return

    def set_teleportGlimpseFrom(self, _):
        self.__sendEvent(Teleport.ACTIVATED, {b'go': (self.teleportGlimpseFrom)})
        return

    def set_teleportGlimpseTo(self, _):
        self.__sendEvent(Teleport.ACTIVATED, {b'go': (self.teleportGlimpseTo)})
        return

    def onDestroy(self):
        self.__sendEvent(Teleport.EXHAUSTED, {b'go': (self.entity.entityGameObject)})
        return

    def __sendEvent(self, event, ctx):
        g_eventBus.handleEvent(Teleport(event, ctx=ctx), scope=EVENT_BUS_SCOPE.BATTLE)
        return
