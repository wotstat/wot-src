enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print b'WARNING: WWISE support is not enabled.'
    enabled = False
