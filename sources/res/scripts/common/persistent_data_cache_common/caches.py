from __future__ import absolute_import
import os, enum, typing
from persistent_data_cache_common import cached_data
from persistent_data_cache_common.common import getLogger, MeasureExecutionTime, DEFAULT_SAVING_TIMEOUT
from soft_exception import SoftException
from wg_async import wg_async, wg_await, forwardAsFuture, AsyncReturn, TimeoutError, BrokenPromiseError
if typing.TYPE_CHECKING:
    from persistent_data_cache_common.types import TData, TPDCVersion
    from persistent_data_cache_common.configs import BasePDCConfig
    from persistent_data_cache_common.data_providers import PDProvider
    from persistent_data_cache_common.events import DefaultPDCEventsDispatcher

class _SavingPDCStates(enum.IntEnum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    CANCELED = 3


class SavingCacheCanceledException(SoftException):
    pass


class SavingCacheFailedException(SoftException):
    pass


class BasePDCache(object):
    __slots__ = (b'_events', b'_logger', b'_config', b'_cachedData', b'_destroyed', b'_savingState')

    def __init__(self, config, eventsDispatcher):
        self._logger = getLogger(self.__class__.__name__)
        self._config = config
        self._cachedData = None
        self._destroyed = False
        self._savingState = _SavingPDCStates.NOT_STARTED
        self._events = eventsDispatcher
        self._logger.debug(b'Initialized with <%s>.', self._config)
        return

    def destroy(self):
        self._destroyed = True
        self.unload()
        self._savingState = _SavingPDCStates.CANCELED
        self._config = None
        self._events = None
        self._logger.debug(b'Destroyed.')
        return

    def unload(self):
        self._cachedData = None
        self._logger.debug(b'Unloaded.')
        return

    def load(self, dataProvider):
        if self._destroyed:
            raise SoftException((b'Cannot load {}. Cache already destroyed.').format(dataProvider.name))
        data = self._getCachedData().get(dataProvider.name)
        self._logger.debug(b'Data has%s been loaded from <%s>.', b' not' if data is None else b'', dataProvider.name)
        return data

    @wg_async
    def save(self, dataProviders, timeout=DEFAULT_SAVING_TIMEOUT):
        if self._savingState != _SavingPDCStates.NOT_STARTED:
            self._logger.error(b'Data wont be saved. Cache has been destroyed|saving|failed previously.')
            raise AsyncReturn(False)
        self._savingState = _SavingPDCStates.IN_PROGRESS
        result = False
        try:
            try:
                self._events.onCacheDataSavingStarted()
                yield wg_await(self._save(dataProviders), timeout=timeout)
                self._events.onCachedDataSaved()
                result = True
            except SavingCacheCanceledException:
                self._logger.debug(b'Saving canceled.')
            except BrokenPromiseError:
                self._logger.debug(b'Destroyed while waiting for saving result.')
            except SavingCacheFailedException as error:
                self._logger.error(b'Saving failed with <%s>.', error)
                self._events.onFailedToSaveCachedData(str(error))
            except TimeoutError:
                error = (b'Saving data timeout <{}>.').format(timeout)
                self._logger.error(error)
                self._events.onFailedToSaveCachedData(error)

        finally:
            self._savingState = _SavingPDCStates.CANCELED

        raise AsyncReturn(result)
        return

    @wg_async
    def _save(self, dataProviders):
        cacheFilePath = self._config.cacheFilePath
        version = self._config.version
        dataProviders = list(dataProviders)
        with MeasureExecutionTime(b'cache.file.deleted').start():
            yield wg_await(forwardAsFuture(self._tryToDeleteCacheFile(cacheFilePath)))
        if self._savingState != _SavingPDCStates.IN_PROGRESS:
            self._logger.debug(b'[Save] Canceled after delete.')
            raise SavingCacheCanceledException()
        cachedData = cached_data.CreatedData(version=version)
        packTiming = MeasureExecutionTime(b'cache.part.packed')
        for dataProvider in dataProviders:
            with packTiming.start(dataProvider.name):
                serialized, error = yield wg_await(forwardAsFuture(self._tryToSerializeData(dataProvider)))
            if serialized is None or error:
                raise SavingCacheFailedException(error)
            if self._savingState != _SavingPDCStates.IN_PROGRESS:
                self._logger.debug(b'[Save] Canceled after serialize <%s>.', dataProvider.name)
                raise SavingCacheCanceledException()
            cachedData.add(dataProvider, serialized)

        with MeasureExecutionTime(b'cache.file.saved').start():
            error = yield wg_await(forwardAsFuture(self._tryToSaveCachedData(cacheFilePath, cachedData)))
        if error:
            raise SavingCacheFailedException(error)
        raise AsyncReturn(None)
        return

    def _getCachedData(self):
        if self._cachedData is None:
            self._cachedData = self._tryToLoadCachedData(self._config.cacheFilePath, self._config.version)
        return self._cachedData

    @MeasureExecutionTime(b'cache.loaded')
    def _tryToLoadCachedData(self, filePath, version):
        try:
            if not self._isFileExist(filePath):
                self._logger.debug(b'Cache file does not exist: <%s>.', filePath)
                return {}
            else:
                cachedData = MeasureExecutionTime(b'cache.file.loaded')(self._loadCachedData)(filePath)
                if cachedData.version != version:
                    self._logger.debug(b'Cache version mismatch: %s != %s.', cachedData.version, version)
                    return {}
                data = cachedData.deserialize(onDataDeserialized=self._events.onDataDeserialized)
                self._events.onCachedDataLoaded()
                return data

        except Exception as error:
            self._logger.exception(b'Failed to load cache file <%s>.', filePath)
            self._events.onFailedToLoadCachedData(str(error))
            return {}

        return

    def _tryToSerializeData(self, dataProvider):
        try:
            data = dataProvider.get()
            if data is None:
                self._logger.error(b'Data for <%s> wont be serialized. No data created.', dataProvider.name)
                return (None, b'')
            return (dataProvider.serialize(data), b'')
        except Exception as error:
            self._logger.exception(b'Cannot serialize data for <%s>.', dataProvider.name)
            return (None, str(error))

        return

    def _tryToSaveCachedData(self, filePath, cachedData):
        try:
            if cachedData.isEmpty():
                self._logger.debug(b'Cannot save cached data to <%s>. Data is empty.', filePath)
            else:
                self._saveCachedData(filePath, cachedData)
            return b''
        except Exception as error:
            self._logger.exception(b'Cannot save cached data to <%s>.', filePath)
            return str(error)

        return

    def _tryToDeleteCacheFile(self, filePath):
        try:
            if not self._isFileExist(filePath):
                return True
            else:
                self._deleteFile(filePath)
                self._logger.debug(b'Cache file <%s> deleted.', filePath)
                return True

        except Exception:
            self._logger.exception(b'Cannot delete cache file <%s>.', filePath)
            return False

        return

    def _loadCachedData(self, filePath):
        raise NotImplementedError
        return

    def _saveCachedData(self, filePath, cachedData):
        raise NotImplementedError
        return

    def _isFileExist(self, filePath):
        raise NotImplementedError
        return

    def _deleteFile(self, filePath):
        raise NotImplementedError
        return


class DefaultPDCache(BasePDCache):
    __slots__ = ()

    def _loadCachedData(self, filePath):
        with open(filePath, b'rb') as cf:
            return cached_data.loads(cf.read())
        return

    def _saveCachedData(self, filePath, cachedData):
        data = cached_data.dumps(cachedData)
        dirPath = os.path.dirname(filePath)
        if not os.path.exists(dirPath):
            self._logger.debug(b'Creating cache dir by path <%s>.', dirPath)
            os.makedirs(dirPath)
        with open(filePath, b'wb') as cf:
            cf.write(data)
        return

    def _isFileExist(self, filePath):
        return os.path.isfile(filePath)

    def _deleteFile(self, filePath):
        os.remove(filePath)
        return
