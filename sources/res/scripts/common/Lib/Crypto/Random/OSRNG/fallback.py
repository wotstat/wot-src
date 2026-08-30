__revision__ = b'$Id$'
__all__ = [b'PythonOSURandomRNG']
import os
from rng_base import BaseRNG

class PythonOSURandomRNG(BaseRNG):
    name = b'<os.urandom>'

    def __init__(self):
        self._read = os.urandom
        BaseRNG.__init__(self)
        return

    def _close(self):
        self._read = None
        return


def new(*args, **kwargs):
    return PythonOSURandomRNG(*args, **kwargs)
