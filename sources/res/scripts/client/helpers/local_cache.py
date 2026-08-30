import base64, shelve
from collections import defaultdict
from contextlib import contextmanager
import os, cPickle
from threading import Lock, Thread
import types, zlib, BigWorld, Event
from debug_utils import LOG_WARNING, LOG_CURRENT_EXCEPTION, LOG_ERROR
from soft_exception import SoftException
from external_strings_utils import unicode_from_utf8

class CacheIO(object):

    def clear(self):
        return

    def read(self, src):
        return src

    def write(self, dst):
        return dst


class RedirectIO(CacheIO):

    def __init__(self, redirect=None):
        super(CacheIO, self).__init__()
        self._redirect = redirect or CacheIO()
        return

    def clear(self):
        if self._redirect is not None:
            self._redirect.clear()
        return

    def read(self, src):
        result = self._doRead(src)
        if not result:
            return result
        return self._redirect.read(result)

    def write(self, dst):
        result = self._redirect.write(dst)
        if not result:
            return result
        return self._doWrite(result)

    def _doRead(self, src):
        raise NotImplementedError
        return

    def _doWrite(self, dst):
        raise NotImplementedError
        return


@contextmanager
def _open_file(fileName, mode=b'r'):
    try:
        fd = open(fileName, mode)
    except IOError as error:
        LOG_CURRENT_EXCEPTION()
        yield (None, error)
    else:
        try:
            try:
                yield (
                 fd, None)
            except Exception:
                LOG_CURRENT_EXCEPTION()

        finally:
            fd.close()

    return


class _FileIO(RedirectIO):
    __internal = {}

    def __init__(self, filePath, redirect=None):
        super(_FileIO, self).__init__(redirect)
        self._filePath = filePath
        return

    def _doRead(self, src):
        if not self._filePath:
            return
        else:
            if self._filePath in _FileIO.__internal:
                LOG_WARNING(b'Gets cache from internal property', self._filePath)
                return _FileIO.__internal[self._filePath]
            if not os.path.isfile(self._filePath):
                return
            with _open_file(self._filePath, b'rb') as fd, error:
                if fd:
                    src = fd.read()
                else:
                    LOG_WARNING(b'Can not read cache', self._filePath, error)
                    src = None
            return src

    def _doWrite(self, dst):
        if not self._filePath:
            return
        else:
            with _open_file(self._filePath, b'wb') as fd, error:
                if fd:
                    fd.write(dst)
                else:
                    LOG_WARNING(b'Can not write cache', self._filePath, error)
                    _FileIO.__internal[self._filePath] = dst
            return fd


class _ShelveIO(RedirectIO):

    def __init__(self, filePath):
        super(_ShelveIO, self).__init__()
        self._filePath = filePath
        self._db = None
        return

    def clear(self):
        if self._db is not None:
            self._db.close()
            self._db = None
        return

    def write(self, dst):
        self._doWrite(dst)
        return

    def _doRead(self, src):
        if not self._filePath:
            return
        else:
            try:
                self._db = src = shelve.open(self._filePath, flag=b'c', writeback=True)
            except Exception as error:
                LOG_WARNING(b'Can not read cache', self._filePath, error)
                src = None

            return src

    def _doWrite(self, _):
        if not self._filePath:
            return
        else:
            try:
                self._db.sync()
            except Exception as error:
                LOG_WARNING(b'Can not write cache', self._filePath, error)

            return


_ioMutexes = defaultdict(Lock)

def _readWorker(uniqueID, io, callback):
    with _ioMutexes[uniqueID]:
        src = io.read(b'')
        callback(src)
    return


def _writeWorker(uniqueID, io, dst):
    with _ioMutexes[uniqueID]:
        io.write(dst)
    return


class _AsyncIO(RedirectIO):

    def __init__(self, uniqueID, redirect=None):
        super(_AsyncIO, self).__init__(redirect)
        self._uniqueID = uniqueID
        self.onRead = Event.Event()
        return

    def clear(self):
        self.onRead.clear()
        super(_AsyncIO, self).clear()
        return

    def read(self, src):
        t = Thread(target=_readWorker, args=(self._uniqueID, self._redirect, self.onRead))
        t.start()
        return b''

    def write(self, dst):
        t = Thread(target=_writeWorker, args=(self._uniqueID, self._redirect, dst))
        t.start()
        return b''

    def _doWrite(self, dst):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _doRead(self, src):
        raise SoftException(b'This method should not be reached in this context')
        return


class PickleIO(RedirectIO):

    def _doRead(self, src):
        try:
            return cPickle.loads(src)
        except cPickle.PickleError as error:
            LOG_WARNING(b'Can not unpickle cache', error)
            return
        except EOFError as error:
            LOG_WARNING(b'Data is broken', error)
            return

        return

    def _doWrite(self, dst):
        try:
            return cPickle.dumps(dst, -1)
        except cPickle.PickleError as error:
            LOG_WARNING(b'Can not pickle cache', error)
            return

        return


class ZipIO(RedirectIO):

    def _doRead(self, src):
        try:
            return zlib.decompress(src)
        except zlib.error as error:
            LOG_WARNING(b'Can not decompress cache', error)
            return

        return

    def _doWrite(self, dst):
        try:
            return zlib.compress(dst)
        except zlib.error as error:
            LOG_WARNING(b'Can not compress cache', error)
            return

        return


class CryptIO(RedirectIO):

    def _doRead(self, src):
        return BigWorld.ucpdata(src)

    def _doWrite(self, dst):
        return BigWorld.cpdata(dst)


def makeFileLocalCachePath(space, tags, fileFormat=b'.dat'):
    p = os.path
    prefsFilePath = unicode_from_utf8(BigWorld.getPreferencesFilePath())[1]
    dirPath = p.join(p.dirname(prefsFilePath), space)
    try:
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
    except Exception:
        LOG_WARNING(b'Error while creating directory', dirPath, tags)
        return b''

    tagsType = type(tags)
    if tagsType is types.TupleType:
        fileName = (b';').join(map(str, tags))
    elif tagsType in types.StringTypes:
        fileName = tags
    else:
        LOG_ERROR(b'Type of tags can be string, unicode or tuple', tagsType, tags)
        return b''
    if fileFormat:
        fileFormat = (b'.{0:>s}').format(fileFormat)
    else:
        fileFormat = b''
    return p.join(dirPath, (b'{0:>s}{1:>s}').format(base64.b32encode(fileName), fileFormat))


class FileLocalCache(object):
    __internal = {}
    __slots__ = (b'_io', b'_ioEnabled', b'onRead')

    def __init__(self, space, tags, io=None, async=False):
        super(FileLocalCache, self).__init__()
        filePath = makeFileLocalCachePath(space, tags)
        self._ioEnabled = True
        if io:
            self._io = _FileIO(filePath, io)
        else:
            self._io = _FileIO(filePath, PickleIO())
        if async:
            self._io = _AsyncIO(filePath, redirect=self._io)
            self._io.onRead += self._onRead
        self.onRead = Event.Event()
        return

    def clear(self):
        if self._ioEnabled:
            self._io.clear()
        self.onRead.clear()
        return

    def read(self):
        if self._ioEnabled:
            self._onRead(self._io.read(None))
        return

    def write(self):
        if self._ioEnabled:
            self._io.write(self._getCache())
        return

    def _onRead(self, src):
        if src:
            self._setCache(src)
            BigWorld.callback(0, self.onRead)
        return

    def _getCache(self):
        raise NotImplementedError
        return

    def _setCache(self, data):
        raise NotImplementedError
        return


class ShelfLocalCache(object):
    __slots__ = (b'_io', b'_cache', b'_autoflush', b'onRead', b'__flushCbID')

    def __init__(self, space, tags, autoflush=0):
        super(ShelfLocalCache, self).__init__()
        filePath = makeFileLocalCachePath(space, tags, fileFormat=b'')
        self._io = _AsyncIO(filePath, redirect=_ShelveIO(filePath))
        self._io.onRead += self._onRead
        self._cache = None
        self._autoflush = autoflush
        self.__flushCbID = None
        if autoflush > 0:
            self.__loadFlushCb()
        self.onRead = Event.Event()
        return

    def clear(self):
        self.__clearFlushCb()
        self._cache = None
        self._io.clear()
        self.onRead.clear()
        return

    def read(self):
        self._io.read(None)
        return

    def write(self):
        self._io.write(None)
        return

    def _doWrite(self, dst):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _doRead(self, src):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _onRead(self, src):
        if src is not None:
            self._cache = src
            BigWorld.callback(0, self.onRead)
        return

    def __doFlush(self):
        self.write()
        self.__loadFlushCb()
        return

    def __loadFlushCb(self):
        self.__clearFlushCb()
        if self.__flushCbID is None:
            self.__flushCbID = BigWorld.callback(self._autoflush, self.__doFlush)
        return

    def __clearFlushCb(self):
        if self.__flushCbID is not None:
            BigWorld.cancelCallback(self.__flushCbID)
            self.__flushCbID = None
        return
