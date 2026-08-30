from messenger import error
from helpers.ro_property import ROPropertyMeta
from messenger.storage.ChannelsStorage import ChannelsStorage
from messenger.storage.shown_messages_storage import ShownMessagesStorage
from messenger.storage.local_cache import StorageLocalCache, SimpleCachedStorage
from messenger.storage.PlayerCtxStorage import PlayerCtxStorage
from messenger.storage.UsersStorage import UsersStorage
_STORAGE = {b'channels': (ChannelsStorage()), 
   b'users': (UsersStorage()), 
   b'playerCtx': (PlayerCtxStorage()), 
   b'shownMessages': (ShownMessagesStorage())}
_DYN_STORAGE = {}

class storage_getter(object):

    def __init__(self, name):
        super(storage_getter, self).__init__()
        if name not in _STORAGE:
            raise error((b'Storage "{0:>s}" not found').format(name))
        self.__name = name
        return

    def __call__(self, *args):
        return _STORAGE[self.__name]


class dyn_storage_getter(object):

    def __init__(self, name):
        super(dyn_storage_getter, self).__init__()
        self.__name = name
        return

    def __call__(self, *args):

        def _getStorage(_self):
            global _DYN_STORAGE
            if self.__name not in _DYN_STORAGE:
                raise error((b'Dyn storage "{0:>s}" not found').format(self.__name))
            return _DYN_STORAGE[self.__name]

        return property(_getStorage)


def addDynStorage(name, storage):
    if name not in _DYN_STORAGE:
        _DYN_STORAGE[name] = storage
    else:
        raise error((b'Storage "{0:>s}" is exists').format(name))
    return


def clearDynStorage(name):
    if name in _DYN_STORAGE:
        storage = _DYN_STORAGE.pop(name, None)
        if storage:
            storage.clear()
    return


class StorageDecorator(object):
    __metaclass__ = ROPropertyMeta
    __readonly__ = _STORAGE

    def __repr__(self):
        return (b'StorageDecorator(id=0x{0:08X}, ro={1!r:s})').format(id(self), self.__readonly__.keys())

    def __init__(self):
        super(StorageDecorator, self).__init__()
        self.__storageCache = None
        return

    def restoreFromCache(self):
        if self.__storageCache:
            return
        from gui.shared.utils import getPlayerDatabaseID, getPlayerName
        self.__storageCache = StorageLocalCache((
         getPlayerDatabaseID(), getPlayerName(), b'storage'))
        self.__storageCache.onRead += self.__onRead
        self.__storageCache.read()
        return

    def init(self):
        for _, storage in self.__readonly__.iteritems():
            storage.init()

        return

    def switch(self, scope):
        for _, storage in self.__readonly__.iteritems():
            storage.switch(scope)

        return

    def clear(self):
        if self.__storageCache:
            for name, storage in self.__readonly__.iteritems():
                record = storage.makeRecordInCache()
                if record:
                    self.__storageCache.addRecord(name, record)

            self.__storageCache.write()
            self.__storageCache.clear()
            self.__storageCache = None
        for storage in self.__readonly__.itervalues():
            storage.clear()

        return

    def __onRead(self):
        if not self.__storageCache:
            return
        for name, storage in self.__readonly__.iteritems():
            storage.restoreFromCache(self.__storageCache.popRecord(name))

        return
