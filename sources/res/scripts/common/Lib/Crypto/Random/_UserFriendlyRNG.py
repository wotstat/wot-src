__revision__ = b'$Id$'
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *
import os, threading, struct, time
from math import floor
from Crypto.Random import OSRNG
from Crypto.Random.Fortuna import FortunaAccumulator

class _EntropySource(object):

    def __init__(self, accumulator, src_num):
        self._fortuna = accumulator
        self._src_num = src_num
        self._pool_num = 0
        return

    def feed(self, data):
        self._fortuna.add_random_event(self._src_num, self._pool_num, data)
        self._pool_num = self._pool_num + 1 & 31
        return


class _EntropyCollector(object):

    def __init__(self, accumulator):
        self._osrng = OSRNG.new()
        self._osrng_es = _EntropySource(accumulator, 255)
        self._time_es = _EntropySource(accumulator, 254)
        self._clock_es = _EntropySource(accumulator, 253)
        return

    def reinit(self):
        for i in range(2):
            block = self._osrng.read(1024)
            for p in range(32):
                self._osrng_es.feed(block[p * 32:(p + 1) * 32])

            block = None

        self._osrng.flush()
        return

    def collect(self):
        self._osrng_es.feed(self._osrng.read(8))
        t = time.time()
        self._time_es.feed(struct.pack(b'@I', int(1073741824 * (t - floor(t)))))
        t = time.clock()
        self._clock_es.feed(struct.pack(b'@I', int(1073741824 * (t - floor(t)))))
        return


class _UserFriendlyRNG(object):

    def __init__(self):
        self.closed = False
        self._fa = FortunaAccumulator.FortunaAccumulator()
        self._ec = _EntropyCollector(self._fa)
        self.reinit()
        return

    def reinit(self):
        self._pid = os.getpid()
        self._ec.reinit()
        self._fa._forget_last_reseed()
        return

    def close(self):
        self.closed = True
        self._osrng = None
        self._fa = None
        return

    def flush(self):
        return

    def read(self, N):
        if self.closed:
            raise ValueError(b'I/O operation on closed file')
        if not isinstance(N, (long, int)):
            raise TypeError(b'an integer is required')
        if N < 0:
            raise ValueError(b'cannot read to end of infinite stream')
        self._ec.collect()
        retval = self._fa.random_data(N)
        self._check_pid()
        return retval

    def _check_pid(self):
        if os.getpid() != self._pid:
            raise AssertionError(b'PID check failed. RNG must be re-initialized after fork(). Hint: Try Random.atfork()')
        return


class _LockingUserFriendlyRNG(_UserFriendlyRNG):

    def __init__(self):
        self._lock = threading.Lock()
        _UserFriendlyRNG.__init__(self)
        return

    def close(self):
        self._lock.acquire()
        try:
            return _UserFriendlyRNG.close(self)
        finally:
            self._lock.release()

        return

    def reinit(self):
        self._lock.acquire()
        try:
            return _UserFriendlyRNG.reinit(self)
        finally:
            self._lock.release()

        return

    def read(self, bytes):
        self._lock.acquire()
        try:
            return _UserFriendlyRNG.read(self, bytes)
        finally:
            self._lock.release()

        return


class RNGFile(object):

    def __init__(self, singleton):
        self.closed = False
        self._singleton = singleton
        return

    def __enter__(self):
        return

    def __exit__(self):
        self.close()
        return

    def close(self):
        self.closed = True
        self._singleton = None
        return

    def read(self, bytes):
        if self.closed:
            raise ValueError(b'I/O operation on closed file')
        return self._singleton.read(bytes)

    def flush(self):
        if self.closed:
            raise ValueError(b'I/O operation on closed file')
        return


_singleton_lock = threading.Lock()
_singleton = None

def _get_singleton():
    global _singleton
    _singleton_lock.acquire()
    try:
        if _singleton is None:
            _singleton = _LockingUserFriendlyRNG()
        return _singleton
    finally:
        _singleton_lock.release()

    return


def new():
    return RNGFile(_get_singleton())


def reinit():
    _get_singleton().reinit()
    return


def get_random_bytes(n):
    return _get_singleton().read(n)
