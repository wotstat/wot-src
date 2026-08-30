from __future__ import absolute_import
import typing, CGF
from dyn_objects_cache import DynObjectsBase

class _WhiteTigerDynObjects(DynObjectsBase):

    def __init__(self):
        super(_WhiteTigerDynObjects, self).__init__()
        self.__prefabPaths = []
        return

    def init(self, dataSection):
        if self._initialized:
            return
        self.__prefabPaths = [value.asString for key, value in dataSection[b'prefabs'].items() if key == b'path' and value.asString]
        if self.__prefabPaths:
            CGF.cachePrefabs(self.__prefabPaths)
        super(_WhiteTigerDynObjects, self).init(dataSection)
        return

    def destroy(self):
        super(_WhiteTigerDynObjects, self).clear()
        del self.__prefabPaths[:]
        return
