import BigWorld, cosmic_prefabs, typing
from PrefabsLoading import PrefabDataListLoader
from dyn_objects_cache import DynObjectsBase, _PointsOfInterestConfig
from vehicle_systems.stricted_loading import makeCallbackWeak
if typing.TYPE_CHECKING:
    from PrefabsLoading import PrefabData

class CosmicEventDynObjects(DynObjectsBase):

    def __init__(self):
        super(CosmicEventDynObjects, self).__init__()
        self.__pointsOfInterestConfig = None
        self.__cachedPrefabs = set()
        self.__resourcesCache = {}
        self.lootPrefabs = {}
        return

    def init(self, dataSection):
        super(CosmicEventDynObjects, self).init(dataSection)
        self.__pointsOfInterestConfig = _PointsOfInterestConfig({(10, 13): (cosmic_prefabs.Artifact.SMALL_HINT), 
           (17, 22): (cosmic_prefabs.Artifact.BIG_HINT)})
        self.__cachedPrefabs.update(set(self.__pointsOfInterestConfig.getPrefabs()))
        self.__collectLootPrefabs()
        self.__collectVehiclePrefabs()
        self.__collectArtifactPrefabs()
        self.__collectDebufPrefabs()
        self.__collectMeteoriteZonePrefabs()
        self.__collectMinePrefabs()
        self.__collectMarkerPrefabs()
        self.__collectOtherPrefabs()
        prefabsLoader = PrefabDataListLoader(b'CosmicPrefabs', list(self.__cachedPrefabs))
        BigWorld.loadResourceListBG((prefabsLoader,), makeCallbackWeak(self.__onResourcesLoaded))
        return

    def clear(self):
        self.__pointsOfInterestConfig = None
        if self.__cachedPrefabs:
            self.__cachedPrefabs.clear()
        self.__resourcesCache = {}
        super(CosmicEventDynObjects, self).clear()
        return

    def destroy(self):
        self.clear()
        super(CosmicEventDynObjects, self).destroy()
        return

    def getPointOfInterestConfig(self):
        return self.__pointsOfInterestConfig

    def __onResourcesLoaded(self, resourceRefs):
        self.__resourcesCache = resourceRefs[b'CosmicPrefabs']
        return

    def __collectLootPrefabs(self):
        prefabs = cosmic_prefabs.Loot.RANGE_LOOT
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectVehiclePrefabs(self):
        prefabs = cosmic_prefabs.Vehicle.RANGE
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectArtifactPrefabs(self):
        prefabs = cosmic_prefabs.Artifact.RANGE
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectDebufPrefabs(self):
        prefabs = cosmic_prefabs.Debuf.RANGE
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectMeteoriteZonePrefabs(self):
        prefabs = cosmic_prefabs.MeteoriteZone.RANGE
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectMinePrefabs(self):
        prefabs = cosmic_prefabs.Mine.RANGE
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectMarkerPrefabs(self):
        prefabs = cosmic_prefabs.Marker.RANGE
        self.__cachedPrefabs.update(prefabs)
        return

    def __collectOtherPrefabs(self):
        prefabs = (b'content/CGFPrefabs/cosmic_event/cosmic_event_artifact_gathering.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_artifact_idle.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_artifact_spawn_abilities.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_artifact_spawn_s_zone_01.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_overcharge.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_passive_shield_shockwave.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_power_shot_mode.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_respawn_protection.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_rocket_booster.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_shield.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_wave.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_sniper_mode.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_supernova.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_supernova_hint.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_teleport_in.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_teleport_out.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_event_zone_s.prefab', b'content/CGFPrefabs/cosmic_event/cosmic_vehicle_emissive.prefab')
        self.__cachedPrefabs.update(prefabs)
        return
