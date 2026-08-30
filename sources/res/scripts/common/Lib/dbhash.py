import sys, warnings
warnings.warnpy3k(b'in 3.x, the dbhash module has been removed', stacklevel=2)
try:
    import bsddb
except ImportError:
    del sys.modules[__name__]
    raise

__all__ = [b'error', b'open']
error = bsddb.error

def open(file, flag=b'r', mode=438):
    return bsddb.hashopen(file, flag, mode)
