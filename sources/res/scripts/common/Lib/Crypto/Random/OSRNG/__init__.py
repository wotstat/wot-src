__revision__ = b'$Id$'
import os
if os.name == b'posix':
    from Crypto.Random.OSRNG.posix import new
elif os.name == b'nt':
    from Crypto.Random.OSRNG.nt import new
elif hasattr(os, b'urandom'):
    from Crypto.Random.OSRNG.fallback import new
else:
    raise ImportError(b'Not implemented')
