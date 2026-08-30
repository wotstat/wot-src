import BigWorld
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from typing import TYPE_CHECKING
from cosmic_event_common.cosmic_constants import LOOT_STATE
from cosmic_event.gui.shared.events import LootEvent
if TYPE_CHECKING:
    from gui.shared.events import HasCtxEvent
    from typing import Optional

class CosmicLoot(BigWorld.Entity):

    def onEnterWorld(self, *args):
        if self.state == LOOT_STATE.SPAWNED:
            self.__sendEvent(LootEvent.SPAWNED, {b'loot': self})
        elif self.state == LOOT_STATE.PREPARING:
            self.__sendEvent(LootEvent.PREPARING, {b'loot': self})
        return

    def onLeaveWorld(self, *args):
        self.__sendEvent(LootEvent.DESTROYED, {b'loot': self})
        return

    def set_state(self, _):
        if self.state == LOOT_STATE.SPAWNED:
            self.__sendEvent(LootEvent.SPAWNED, {b'loot': self})
        elif self.state == LOOT_STATE.PICKED_UP:
            self.__sendEvent(LootEvent.PICKED_UP, {b'loot': self})
        elif self.state == LOOT_STATE.PREPARING:
            self.__sendEvent(LootEvent.PREPARING, {b'loot': self})
        return

    def __sendEvent(self, event, ctx):
        g_eventBus.handleEvent(LootEvent(event, ctx=ctx), scope=EVENT_BUS_SCOPE.BATTLE)
        return
