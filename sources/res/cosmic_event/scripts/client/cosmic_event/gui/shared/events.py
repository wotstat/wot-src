from gui.shared.events import HasCtxEvent

class ArtifactScanningEvent(HasCtxEvent):
    VEHICLES_IN_ZONE_CHANGED = b'artifact/vehiclesInZoneChanged'
    ANNOUNCEMENT_CREATED = b'artifact/announced'
    ARTIFACT_SCANNING_READY = b'artifact/scanningReady'
    ARTIFACT_DESTROYED = b'artifact/destroyed'


class LootEvent(HasCtxEvent):
    PREPARING = b'loot/preparing'
    SPAWNED = b'loot/spawned'
    PICKED_UP = b'loot/pickedUp'
    DESTROYED = b'loot/destroyed'


class CosmicVehicleEvent(HasCtxEvent):
    START_LOOT_RESEARCHING = b'cosmicVehicle/startLootResearching'
    STOP_LOOT_RESEARCHING = b'cosmicVehicle/stopLootResearching'
    LOOT_RESEARCHING_DONE = b'cosmicVehicle/lootResearchingDone'
    LOOT_TRANSFER = b'cosmicVehicle/lootTransfer'
    START_TELEPORT = b'cosmicVehicle/startTeleport'
    TELEPORT_PREPARED = b'cosmicVehicle/teleportPrepared'


class MeteoriteZoneEvent(HasCtxEvent):
    STATE_CHANGED = b'zone/stateChanged'
    DEACTIVATE = b'zone/deactivate'
    VEHICLE_DAMAGE = b'zone/damage'
    LOOT_PREPARING = b'zone/lootPreparing'


class MineEvent(HasCtxEvent):
    APPEAR = b'mine/appear'
    EXPLODE = b'mine/explode'


class Teleport(HasCtxEvent):
    ACTIVATED = b'teleport/activate'
    PREPARED = b'teleport/prepared'
    EXHAUSTED = b'teleport/exhausted'
