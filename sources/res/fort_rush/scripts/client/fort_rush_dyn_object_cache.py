from __future__ import absolute_import
import typing, CGF
from dyn_objects_cache import DynObjectsBase

class _FortRushDynObjects(DynObjectsBase):

    def __init__(self):
        super(_FortRushDynObjects, self).__init__()
        self.__prefabPaths = []
        return

    def init(self, dataSection):
        if self._initialized:
            return
        self.__prefabPaths = [value.asString for key, value in dataSection[b'prefabs'].items() if key == b'path' and value.asString]
        if self.__prefabPaths:
            CGF.cachePrefabs(self.__prefabPaths)
        super(_FortRushDynObjects, self).init(dataSection)
        return

    def clear(self):
        if self.__prefabPaths:
            CGF.removePrefabsFromCache(list(self.__prefabPaths))
            del self.__prefabPaths[:]
        self._initialized = False
        super(_FortRushDynObjects, self).clear()
        return

    def destroy(self):
        self.clear()
        super(_FortRushDynObjects, self).destroy()
        return
