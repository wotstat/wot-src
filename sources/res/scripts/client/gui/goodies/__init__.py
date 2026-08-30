from gui.goodies.booster_state_provider import BoosterStateProvider
from gui.goodies.storage_novelty import StorageNovelty
from gui.goodies.goodies_cache import GoodiesCache
from skeletons.gui.storage_novelty import IStorageNovelty
from skeletons.gui.goodies import IGoodiesCache, IBoostersStateProvider
from helpers.dependency import DependencyManager
__all__ = (b'getGoodiesCacheConfig', b'getStorageNoveltyConfig')

def getGoodiesCacheConfig(manager):
    cache = GoodiesCache()
    cache.init()
    provider = BoosterStateProvider()
    manager.addInstance(IGoodiesCache, cache, finalizer=b'fini')
    manager.addInstance(IBoostersStateProvider, provider, finalizer=b'fini')
    return


def getStorageNoveltyConfig(manager):

    def _create():
        instance = StorageNovelty()
        instance.init()
        return instance

    manager.addRuntime(IStorageNovelty, _create, finalizer=b'fini')
    return
