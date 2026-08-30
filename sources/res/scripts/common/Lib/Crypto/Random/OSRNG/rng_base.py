__revision__ = b'$Id$'
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *

class BaseRNG(object):

    def __init__(self):
        self.closed = False
        self._selftest()
        return

    def __del__(self):
        self.close()
        return

    def _selftest(self):
        data = self.read(16)
        if len(data) != 16:
            raise AssertionError(b'read truncated')
        data2 = self.read(16)
        if data == data2:
            raise AssertionError(b'OS RNG returned duplicate data')
        return

    def __enter__(self):
        return

    def __exit__(self):
        self.close()
        return

    def close(self):
        if not self.closed:
            self._close()
        self.closed = True
        return

    def flush(self):
        return

    def read(self, N=-1):
        if self.closed:
            raise ValueError(b'I/O operation on closed file')
        if not isinstance(N, (long, int)):
            raise TypeError(b'an integer is required')
        if N < 0:
            raise ValueError(b'cannot read to end of infinite stream')
        elif N == 0:
            return b''
        data = self._read(N)
        if len(data) != N:
            raise AssertionError(b'%s produced truncated output (requested %d, got %d)' % (self.name, N, len(data)))
        return data

    def _close(self):
        raise NotImplementedError(b'child class must implement this')
        return

    def _read(self, N):
        raise NotImplementedError(b'child class must implement this')
        return
