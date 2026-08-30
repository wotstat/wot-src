from __future__ import absolute_import
import os, logging
from typing import Dict, Any
from helpers.local_cache import FileLocalCache
from gui.game_control.wotlda.constants import LAST_UPDATE_TIMESTAMP, SupportedWTRRange
_logger = logging.getLogger(__name__)

class WotldaCache(FileLocalCache):
    _CACHE_TYPE = b''

    def __init__(self):
        super(WotldaCache, self).__init__(b'wotlda_cache', (self._CACHE_TYPE, b'loadouts'), isAsync=True)
        self._filePath = self._buildLocalCachePath(b'wotlda_cache', (self._CACHE_TYPE, b'loadouts'))
        self._cache = {}
        return

    def update(self, data):
        self._setCache(data)
        self.write()
        return

    def clear(self):
        super(WotldaCache, self).clear()
        self.clearCache()
        return

    def getUpdatedAtTimestamp(self):
        return self._cache.get(LAST_UPDATE_TIMESTAMP, 0)

    def isCacheEmpty(self):
        return not bool(self._cache)

    def clearCache(self):
        self._cache.clear()
        return

    def getLoadout(self, vehicleID, *args, **kwargs):
        raise NotImplementedError
        return

    def deleteCacheFile(self):
        try:
            os.remove(self._filePath)
        except OSError:
            _logger.debug(b'Deleting [%s] file failed.', self._filePath)

        return

    def _getCache(self):
        return self._cache.copy()

    def _setCache(self, data):
        self._cache = data
        return


class EasyTankEquipCache(WotldaCache):
    _CACHE_TYPE = b'easy_tank_equip'

    def getLoadout(self, vehicleID, *args, **kwargs):
        return self._cache.get(str(vehicleID), {})


class EquipmentForSubscribersCache(WotldaCache):
    _CACHE_TYPE = b'subscription'

    def getLoadout(self, vehicleID, *args, **kwargs):
        loadoutType = kwargs.get(b'loadoutType')
        wtrRange = kwargs.get(b'wtrRange')
        return self._cache.get(loadoutType, {}).get(wtrRange, {}).get(str(vehicleID), {})


class CrewCache(WotldaCache):
    _CACHE_TYPE = b'crew'

    def getLoadout(self, vehicleID, *args, **kwargs):
        result = {}
        role = kwargs.get(b'role')
        allSkills = set()
        for range in SupportedWTRRange.allRanges():
            skills = self._cache.get(range.value, {}).get(str(vehicleID), {}).get(role, {})
            if skills:
                allSkills = skills.keys()
                break

        for range in SupportedWTRRange.allRanges():
            skills = self._cache.get(range.value, {}).get(str(vehicleID), {}).get(role, {})
            for skill in allSkills:
                result.setdefault(skill, []).append(skills.get(skill, 0))

        return result
