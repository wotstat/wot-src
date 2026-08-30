from __future__ import absolute_import
import io, os, platform, sys
from functools import partial
import BigWorld, ResMgr
from bwdebug import TRACE_MSG
try:
    import builtins
except ImportError:
    import __builtin__ as builtins

try:
    _unicode = unicode
    _basestring = basestring
except NameError:
    _unicode = str
    _basestring = str

_PY2 = sys.version_info.major < 3

class _BuiltinsAccessor(object):

    def __init__(self, field_name):
        self._field_name = field_name
        self._original = None
        return

    @property
    def original(self):
        return self._original or self._get()

    def set(self, value):
        self._original = self._get()
        self._set(value)
        return

    def get(self):
        return self._get()

    def _set(self, value):
        raise NotImplementedError
        return

    def _get(self):
        raise NotImplementedError
        return

    def revert(self):
        if self._original:
            self.set(self._original)
            self._original = None
        return


class _ItemAccessor(_BuiltinsAccessor):

    def _set(self, value):
        builtins[self._field_name] = value
        return

    def _get(self):
        return builtins[self._field_name]


class _AttrAccessor(_BuiltinsAccessor):

    def _set(self, value):
        setattr(builtins, self._field_name, value)
        return

    def _get(self):
        return getattr(builtins, self._field_name)


try:
    _ = builtins[b'open']
    _open_accessor = _ItemAccessor(b'open')
except TypeError:
    _open_accessor = _AttrAccessor(b'open')

class _BwFile(object):

    def __init__(self, path):
        self._content = ResMgr.openSection(path).asBinary.split(b'\n')
        return

    def __enter__(self):
        return self._content

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def __iter__(self):
        return iter(self._content)


def bwResReplaceOpen(name, *args, **kwargs):
    return _BwFile(name)


def bwResRelativePatch(function, name, *args, **kwargs):
    try:
        absname = ResMgr.resolveToAbsolutePath(name)
    except Exception as e:
        raise IOError(2, (b'Error = {}; name = {}').format(str(e), name))

    absname = _unicode(absname)
    return function(absname, *args, **kwargs)


@partial
def bwResRelativeOpen(name, *args, **kwargs):
    if _PY2:
        kwargs.pop(b'encoding', None)
    return bwResRelativePatch(_open_accessor.original, name, *args, **kwargs)


@partial
def bwResRelativeIOOpen(name, *args, **kwargs):
    return bwResRelativePatch(io.open, name, *args, **kwargs)


def monkeyPatchOpen(full_replace=False):
    TRACE_MSG(b'BWUtil.monkeyPatchOpen: Patching open()', full_replace)
    if full_replace:
        new_open = bwResReplaceOpen
    else:
        new_open = bwResRelativeOpen
    _open_accessor.set(new_open)
    return


def monkeyPatchFutureOpen():
    TRACE_MSG(b'BWUtil.monkeyPatchFutureOpen: Patching future open()')
    try:
        from future import builtins as future_builtins
        future_builtins.open = bwResRelativeIOOpen
    except ImportError:
        TRACE_MSG(b'BWUtil.monkeyPatchFutureOpen: Patching aborted since no future library')

    return


def revertPatchedOpen():
    TRACE_MSG(b'BWUtil.revertPatchedOpen: Reverting open()')
    _open_accessor.revert()
    return


def extendPath(path, name):
    from pkgutil import extend_path
    path = extend_path(path, name)
    if not isinstance(path, list):
        return path
    pname = os.path.join(*name.split(b'.'))
    init_py = b'__init__' + os.extsep + b'py'
    path = path[:]
    for dir in sys.path:
        if not isinstance(dir, _basestring) or not ResMgr.isDir(dir):
            continue
        subdir = os.path.join(dir, pname)
        initfile = os.path.join(subdir, init_py)
        if subdir not in path and ResMgr.isFile(initfile):
            path.append(subdir)

    return path


def longDistroNameToShort(longDistroName):
    if longDistroName.startswith(b'Red Hat'):
        return b'rhel'
    if longDistroName.startswith(b'CentOS'):
        return b'CentOS'
    return longDistroName


SHORT_NAME_ENTERPRISE_LINUX = b'el'
ENTERPRISE_LINUX_DISTROS = [
 b'centos', b'rhel']
ALLOWED_DISTROS = ENTERPRISE_LINUX_DISTROS + [b'fedora']

def finaliseShortNameFromReleaseInfo(longDistroName, versionStr, releaseName):
    majorVerStr = versionStr
    if b'.' in versionStr:
        majorVerStr = versionStr[0:versionStr.index(b'.')]
    versionNum = int(majorVerStr)
    shortDistroName = longDistroNameToShort(longDistroName).lower()
    if shortDistroName not in ALLOWED_DISTROS:
        sys.stderr.write(b"Distribution '%s' is not supported\n" % shortDistroName)
        return None
    else:
        if shortDistroName in ENTERPRISE_LINUX_DISTROS:
            shortDistroName = SHORT_NAME_ENTERPRISE_LINUX
        return b'%s%d' % (shortDistroName, versionNum)


def findPlatformName():
    if platform.system() == b'Windows':
        return b'win64'
    else:
        try:
            platformData = platform.linux_distribution()
        except AttributeError:
            sys.stderr.write(b'Unable to detect linux distribution. An old version of Python may be present. BigWorld requires Python 2.7.\n')
            return

        return finaliseShortNameFromReleaseInfo(*platformData)
        return


def getPlatformArchitecutre():
    try:
        return platform.processor()
    except:
        sys.stderr.write(b'Unable to detect platform architecture')
        return

    return


def getPlatformSuffix():
    platformName = findPlatformName()
    if not platformName:
        return None
    else:
        platformArchitecture = getPlatformArchitecutre()
        if not platformArchitecture:
            return None
        platformSuffix = platformName
        if platformName == b'el9':
            platformSuffix += b'/' + platformArchitecture
        return platformSuffix


class AsyncReturn(StopIteration):
    __slots__ = (b'value',)

    def __init__(self, value):
        self.value = value
        return


def if_only_component(*components):

    def _real_decorator(func):

        def _wrapper(*args, **kwargs):
            if BigWorld.component in components:
                func(*args, **kwargs)
            return

        return _wrapper

    return _real_decorator


def if_only_not_component(*components):

    def _real_decorator(func):

        def _wrapper(*args, **kwargs):
            if BigWorld.component not in components:
                func(*args, **kwargs)
            return

        return _wrapper

    return _real_decorator
