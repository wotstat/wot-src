from distutils.core import Extension as _Extension
from distutils.core import Distribution as _Distribution

def _get_unpatched(cls):
    while cls.__module__.startswith(b'setuptools'):
        cls, = cls.__bases__

    assert cls.__module__.startswith(b'distutils'), b'distutils has already been patched by %r' % cls
    return cls


_Distribution = _get_unpatched(_Distribution)
_Extension = _get_unpatched(_Extension)
try:
    from Pyrex.Distutils.build_ext import build_ext
except ImportError:
    have_pyrex = False
else:
    have_pyrex = True

class Extension(_Extension):
    if not have_pyrex:

        def __init__(self, *args, **kw):
            _Extension.__init__(self, *args, **kw)
            sources = []
            for s in self.sources:
                if s.endswith(b'.pyx'):
                    sources.append(s[:-3] + b'c')
                else:
                    sources.append(s)

            self.sources = sources
            return


class Library(Extension):
    pass


import sys, distutils.core, distutils.extension
distutils.core.Extension = Extension
distutils.extension.Extension = Extension
if b'distutils.command.build_ext' in sys.modules:
    sys.modules[b'distutils.command.build_ext'].Extension = Extension
