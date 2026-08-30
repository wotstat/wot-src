import BigWorld, logging, typing
from dyn_objects_cache import DynObjectsBase
from PrefabsLoading import PrefabDataListLoader
from vehicle_systems.stricted_loading import makeCallbackWeak
if typing.TYPE_CHECKING:
    from PrefabsLoading import PrefabData
_logger = logging.getLogger(__name__)

class WTBattleDynObjects(DynObjectsBase):

    def __init__(self):
        super(WTBattleDynObjects, self).__init__()
        self.__resourcesCache = {}
        return

    def init(self, dataSection):
        if self._initialized:
            return
        self.__cachePrefabs(dataSection)
        super(WTBattleDynObjects, self).init(dataSection)
        return

    def destroy(self):
        self.clear()
        super(WTBattleDynObjects, self).destroy()
        return

    def clear(self):
        self.__resourcesCache = {}
        self.__resourcesCache = None
        self._initialized = False
        super(WTBattleDynObjects, self).clear()
        return

    def __cachePrefabs(self, dataSection):
        prefabsPaths = {value.asString for key, value in dataSection[b'WtPrefabs'].items() if key == b'path' and value.asString}
        if not prefabsPaths:
            _logger.warning(b'No valid prefab paths found in WtPrefabs/path entries; skipping preload')
            return
        prefabsLoader = PrefabDataListLoader(b'WtPrefabs', list(prefabsPaths))
        BigWorld.loadResourceListBG((prefabsLoader,), makeCallbackWeak(self.__onPrefabsLoaded))
        return

    def __onPrefabsLoaded(self, resourceRefs):
        self.__resourcesCache = resourceRefs[b'WtPrefabs']
        if self.__resourcesCache:
            _logger.info(b'WtPrefabs loaded successfully: %d items', len(resourceRefs[b'WtPrefabs']))
        return
