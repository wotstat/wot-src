import weakref
from Event import Event
from soft_exception import SoftException

class AbstractLock(object):

    def __init__(self):
        super(AbstractLock, self).__init__()
        self.onLocked = Event()
        self.onUnlocked = Event()
        return

    def dispose(self):
        self.onLocked.clear()
        self.onUnlocked.clear()
        return

    def getID(self):
        raise NotImplementedError
        return

    def lock(self):
        raise NotImplementedError
        return

    def unlock(self):
        raise NotImplementedError
        return

    def isLocked(self):
        raise NotImplementedError
        return

    def tryLock(self):
        raise NotImplementedError
        return


class _LockProxy(AbstractLock):

    def __init__(self, lockID):
        super(_LockProxy, self).__init__()
        self.__id = lockID
        self.__isLocked = False
        self.__counter = 0
        return

    def getID(self):
        return self.__id

    def increment(self):
        self.__counter += 1
        return self.__counter

    def decrement(self):
        self.__counter -= 1
        return self.__counter

    def lock(self):
        if not self.tryLock():
            raise SoftException(b'Lock is already locked!')
        return

    def unlock(self):
        if self.__isLocked:
            self.__isLocked = False
            self.onUnlocked()
        return

    def isLocked(self):
        return self.__isLocked

    def tryLock(self):
        if self.__isLocked:
            return False
        self.__isLocked = True
        self.onLocked()
        return True


class _LockStorage(object):

    def __init__(self):
        super(_LockStorage, self).__init__()
        self.__locks = {}
        return

    def create(self, lockID):
        if lockID in self.__locks:
            m = self.__locks[lockID]
        else:
            m = _LockProxy(lockID)
            self.__locks[lockID] = m
        m.increment()
        return m

    def delete(self, lockID):
        if lockID in self.__locks:
            m = self.__locks[lockID]
            counter = m.decrement()
            if counter == 0:
                lock = self.__locks.pop(lockID)
                lock.dispose()
        return

    def isExist(self, lockID):
        return lockID in self.__locks


_g_lockStorage = _LockStorage()

class Lock(AbstractLock):

    def __init__(self, lockID):
        super(Lock, self).__init__()
        self.__isLocked = False
        self.__proxy = _g_lockStorage.create(lockID)
        self.__proxy.onLocked += weakref.proxy(self.onLocked)
        self.__proxy.onUnlocked += weakref.proxy(self.onUnlocked)
        return

    def __del__(self):
        self.dispose()
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dispose()
        return

    def dispose(self):
        super(Lock, self).dispose()
        if self.__proxy is not None:
            self.__proxy.onLocked -= weakref.proxy(self.onLocked)
            self.__proxy.onUnlocked -= weakref.proxy(self.onUnlocked)
            self.unlock()
            _g_lockStorage.delete(self.__proxy.getID())
            self.__proxy = None
        return

    def getID(self):
        return self.__proxy.getID()

    def lock(self):
        if not self.__isLocked:
            try:
                self.__isLocked = True
                self.__proxy.lock()
            except SoftException as e:
                self.__isLocked = False
                raise e

        return

    def unlock(self):
        if self.__isLocked:
            self.__isLocked = False
            self.__proxy.unlock()
        return

    def isLocked(self):
        return self.__proxy.isLocked()

    def isOwner(self):
        return self.__isLocked

    def tryLock(self):
        if not self.__isLocked and not self.__proxy.isLocked():
            self.__isLocked = True
            self.__proxy.lock()
        return self.__isLocked


def synchronized(lockID):

    def decorator(func):

        def wrapper(*args, **kwargs):
            rv = None
            with Lock(lockID) as lock:
                if lock.tryLock():
                    rv = func(*args, **kwargs)
            return rv

        return wrapper

    return decorator
