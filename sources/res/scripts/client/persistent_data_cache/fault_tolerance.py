import typing
from persistent_data_cache_common.common import getLogger
from helpers import base64_utils
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
    from persistent_data_cache_common.types import TPDCVersion
_logger = getLogger(b'FaultTolerance')
_PREFS_NAME = b'pdcFaultTolerance'
_VERSION_KEY = b'version'
_FAILED_TO_LOAD_COUNT_KEY = b'failedToLoadCount'
_FAILED_TO_SAVE_COUNT_KEY = b'failedToSaveCount'
_FAILED_TO_LOAD_COUNT_LIMIT = 5
_FAILED_TO_SAVE_COUNT_LIMIT = 5

def _loadData(version, userPrefs):
    data, modified = {}, False
    if userPrefs.has_key(_PREFS_NAME):
        unpacked = base64_utils.unpack(userPrefs[_PREFS_NAME].asString, default=None)
        if isinstance(unpacked, dict):
            _logger.debug(b'Data has been loaded from preferences.')
            prefVersion = unpacked.pop(_VERSION_KEY, None)
            if prefVersion is None or prefVersion != version:
                modified, unpacked = True, {}
                _logger.debug(b'Version of preferences changed. <%s> != <%s>.', prefVersion, version)
            data = unpacked
        else:
            _logger.warning(b'Failed to load data from preferences.')
            modified = True
    return (
     data, modified)


class FaultTolerance(object):
    __slots__ = (b'_userPrefs', b'_data', b'_version', b'_modified')

    def __init__(self, version, userPrefs):
        self._version = version
        self._userPrefs = userPrefs
        self._data, self._modified = _loadData(self._version, self._userPrefs)
        _logger.debug(b'Initialized. <version==%s, modified=%s, data=%s>.', self._version, self._modified, self._data)
        return

    def isLimitsReached(self):
        failedToLoadCount = self._data.get(_FAILED_TO_LOAD_COUNT_KEY, 0)
        failedToSaveCount = self._data.get(_FAILED_TO_SAVE_COUNT_KEY, 0)
        return failedToLoadCount >= _FAILED_TO_LOAD_COUNT_LIMIT or failedToSaveCount >= _FAILED_TO_SAVE_COUNT_LIMIT

    def increaseFailedToLoadCount(self, error):
        self._increaseCount(_FAILED_TO_LOAD_COUNT_KEY)
        return

    def resetFailedToLoadCount(self):
        self._resetCount(_FAILED_TO_LOAD_COUNT_KEY)
        return

    def increaseFailedToSaveCount(self, error):
        self._increaseCount(_FAILED_TO_SAVE_COUNT_KEY)
        return

    def resetFailedToSaveCount(self):
        self._resetCount(_FAILED_TO_SAVE_COUNT_KEY)
        return

    def fini(self):
        if self._modified and self._userPrefs is not None:
            if self._data:
                data = {_VERSION_KEY: (self._version)}
                data.update(self._data)
                packed = base64_utils.pack(data)
                if packed is not None:
                    self._userPrefs.write(_PREFS_NAME, packed)
                    _logger.debug(b'Data has been saved. <%s>.', data)
                else:
                    _logger.error(b'Data has not been saved.')
            else:
                _logger.debug(b'Nothing to save.')
                if self._userPrefs.has_key(_PREFS_NAME):
                    self._userPrefs.deleteSection(_PREFS_NAME)
        self._userPrefs = None
        self._modified = False
        _logger.debug(b'Finalized.')
        return

    def _resetCount(self, key):
        if key in self._data:
            self._data.pop(key, None)
            self._modified = True
            _logger.debug(b'Count <%s> value has been deleted.', key)
        return

    def _increaseCount(self, key):
        count = self._data.get(key, 0) + 1
        self._data[key] = count
        self._modified = True
        _logger.debug(b'Count <%s> value changed to <%s>.', key, count)
        return


_g_faultTolerance = None

def init(version, userPrefs):
    global _g_faultTolerance
    if _g_faultTolerance is not None:
        _logger.error(b'Already initialized.')
        return _g_faultTolerance
    else:
        _g_faultTolerance = FaultTolerance(version, userPrefs)
        return _g_faultTolerance


def fini():
    global _g_faultTolerance
    if _g_faultTolerance is None:
        _logger.debug(b'Not initialized.')
        return
    else:
        _g_faultTolerance.fini()
        _g_faultTolerance = None
        return
