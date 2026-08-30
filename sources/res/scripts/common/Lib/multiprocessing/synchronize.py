__all__ = [
 0, 1, 2, 3, 4, 5]
import threading, os, sys
from time import time as _time, sleep as _sleep
import _multiprocessing
from multiprocessing.process import current_process
from multiprocessing.util import Finalize, register_after_fork, debug
from multiprocessing.forking import assert_spawning, Popen
try:
    from _multiprocessing import SemLock
except ImportError:
    raise ImportError(b'This platform lacks a functioning sem_open' + b' implementation, therefore, the required' + b' synchronization primitives needed will not' + b' function, see issue 3770.')

RECURSIVE_MUTEX, SEMAPHORE = range(2)
SEM_VALUE_MAX = _multiprocessing.SemLock.SEM_VALUE_MAX

class SemLock(object):

    def __init__(self, kind, value, maxvalue):
        sl = self._semlock = _multiprocessing.SemLock(kind, value, maxvalue)
        debug(b'created semlock with handle %s' % sl.handle)
        self._make_methods()
        if sys.platform != b'win32':

            def _after_fork(obj):
                obj._semlock._after_fork()
                return

            register_after_fork(self, _after_fork)
        return

    def _make_methods(self):
        self.acquire = self._semlock.acquire
        self.release = self._semlock.release
        return

    def __enter__(self):
        return self._semlock.__enter__()

    def __exit__(self, *args):
        return self._semlock.__exit__(*args)

    def __getstate__(self):
        assert_spawning(self)
        sl = self._semlock
        return (Popen.duplicate_for_child(sl.handle), sl.kind, sl.maxvalue)

    def __setstate__(self, state):
        self._semlock = _multiprocessing.SemLock._rebuild(*state)
        debug(b'recreated blocker with handle %r' % state[0])
        self._make_methods()
        return


class Semaphore(SemLock):

    def __init__(self, value=1):
        SemLock.__init__(self, SEMAPHORE, value, SEM_VALUE_MAX)
        return

    def get_value(self):
        return self._semlock._get_value()

    def __repr__(self):
        try:
            value = self._semlock._get_value()
        except Exception:
            value = b'unknown'

        return b'<Semaphore(value=%s)>' % value


class BoundedSemaphore(Semaphore):

    def __init__(self, value=1):
        SemLock.__init__(self, SEMAPHORE, value, value)
        return

    def __repr__(self):
        try:
            value = self._semlock._get_value()
        except Exception:
            value = b'unknown'

        return b'<BoundedSemaphore(value=%s, maxvalue=%s)>' % (
         value, self._semlock.maxvalue)


class Lock(SemLock):

    def __init__(self):
        SemLock.__init__(self, SEMAPHORE, 1, 1)
        return

    def __repr__(self):
        try:
            if self._semlock._is_mine():
                name = current_process().name
                if threading.current_thread().name != b'MainThread':
                    name += b'|' + threading.current_thread().name
            elif self._semlock._get_value() == 1:
                name = b'None'
            elif self._semlock._count() > 0:
                name = b'SomeOtherThread'
            else:
                name = b'SomeOtherProcess'
        except Exception:
            name = b'unknown'

        return b'<Lock(owner=%s)>' % name


class RLock(SemLock):

    def __init__(self):
        SemLock.__init__(self, RECURSIVE_MUTEX, 1, 1)
        return

    def __repr__(self):
        try:
            if self._semlock._is_mine():
                name = current_process().name
                if threading.current_thread().name != b'MainThread':
                    name += b'|' + threading.current_thread().name
                count = self._semlock._count()
            elif self._semlock._get_value() == 1:
                name, count = (b'None', 0)
            elif self._semlock._count() > 0:
                name, count = (b'SomeOtherThread', b'nonzero')
            else:
                name, count = (b'SomeOtherProcess', b'nonzero')
        except Exception:
            name, count = (b'unknown', b'unknown')

        return b'<RLock(%s, %s)>' % (name, count)


class Condition(object):

    def __init__(self, lock=None):
        self._lock = lock or RLock()
        self._sleeping_count = Semaphore(0)
        self._woken_count = Semaphore(0)
        self._wait_semaphore = Semaphore(0)
        self._make_methods()
        return

    def __getstate__(self):
        assert_spawning(self)
        return (self._lock, self._sleeping_count,
         self._woken_count, self._wait_semaphore)

    def __setstate__(self, state):
        self._lock, self._sleeping_count, self._woken_count, self._wait_semaphore = state
        self._make_methods()
        return

    def __enter__(self):
        return self._lock.__enter__()

    def __exit__(self, *args):
        return self._lock.__exit__(*args)

    def _make_methods(self):
        self.acquire = self._lock.acquire
        self.release = self._lock.release
        return

    def __repr__(self):
        try:
            num_waiters = self._sleeping_count._semlock._get_value() - self._woken_count._semlock._get_value()
        except Exception:
            num_waiters = b'unknown'

        return b'<Condition(%s, %s)>' % (self._lock, num_waiters)

    def wait(self, timeout=None):
        self._sleeping_count.release()
        count = self._lock._semlock._count()
        for i in xrange(count):
            self._lock.release()

        try:
            self._wait_semaphore.acquire(True, timeout)
        finally:
            self._woken_count.release()
            for i in xrange(count):
                self._lock.acquire()

        return

    def notify(self):
        while self._woken_count.acquire(False):
            res = self._sleeping_count.acquire(False)

        if self._sleeping_count.acquire(False):
            self._wait_semaphore.release()
            self._woken_count.acquire()
            self._wait_semaphore.acquire(False)
        return

    def notify_all(self):
        while self._woken_count.acquire(False):
            res = self._sleeping_count.acquire(False)

        sleepers = 0
        while self._sleeping_count.acquire(False):
            self._wait_semaphore.release()
            sleepers += 1

        if sleepers:
            for i in xrange(sleepers):
                self._woken_count.acquire()

            while self._wait_semaphore.acquire(False):
                pass

        return


class Event(object):

    def __init__(self):
        self._cond = Condition(Lock())
        self._flag = Semaphore(0)
        return

    def is_set(self):
        self._cond.acquire()
        try:
            if self._flag.acquire(False):
                self._flag.release()
                return True
            else:
                return False

        finally:
            self._cond.release()

        return

    def set(self):
        self._cond.acquire()
        try:
            self._flag.acquire(False)
            self._flag.release()
            self._cond.notify_all()
        finally:
            self._cond.release()

        return

    def clear(self):
        self._cond.acquire()
        try:
            self._flag.acquire(False)
        finally:
            self._cond.release()

        return

    def wait(self, timeout=None):
        self._cond.acquire()
        try:
            if self._flag.acquire(False):
                self._flag.release()
            else:
                self._cond.wait(timeout)
            if self._flag.acquire(False):
                self._flag.release()
                return True
            return False
        finally:
            self._cond.release()

        return
