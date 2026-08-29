import sys
absolute_import = sys.version_info[0] >= 3
if not absolute_import:
    if __name__.startswith(b'bsddb3.'):
        from _pybsddb import *
        from _pybsddb import __version__
    else:
        from _bsddb import *
        from _bsddb import __version__
elif __name__.startswith(b'bsddb3.'):
    exec b'from ._pybsddb import *'
    exec b'from ._pybsddb import __version__'
else:
    exec b'from ._bsddb import *'
    exec b'from ._bsddb import __version__'
