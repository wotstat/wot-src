from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class DeathZoneEvent(HasCtxEvent):
    UPDATE_DEATH_ZONE = b'deathZone/update'


class AirDropEvent(HasCtxEvent):
    AIR_DROP_SPAWNED = b'onAirDropSpawned'
    AIR_DROP_LANDED = b'onAirDropLanded'
    AIR_DROP_ENTERED = b'onAirDropEntered'
    AIR_DROP_LEFT = b'onAirDropLeft'
    AIR_DROP_NXT_SPAWNED = b'onAirDropNxtSpawned'


class LootEvent(HasCtxEvent):
    LOOT_PICKED_UP = b'onLootPickedUp'
