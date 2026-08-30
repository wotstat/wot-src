from __future__ import absolute_import, print_function
import os, traceback, sys, pydoc, fnmatch, logging, BigWorld, BWLogging, BWUtil, ResMgr, bwdeprecations
from bwdebug import NOTICE_MSG
try:
    import builtins
except ImportError:
    import __builtin__ as builtins

DEFAULT_ENCODING = b'utf-8'
PLATFORM_SUFFIX = BWUtil.getPlatformSuffix()

class _Helper(object):

    def __repr__(self):
        return b'Type help() for interactive help, or help(object) for help about object.'

    def __call__(self, *args, **kwds):
        return pydoc.help(*args, **kwds)


def set_helper():
    builtins.help = _Helper()
    return


def set_default_encoding():
    if hasattr(sys, b'setdefaultencoding'):
        sys.setdefaultencoding(DEFAULT_ENCODING)
        del sys.setdefaultencoding
        configLog = logging.getLogger(b'Config')
        configLog.info(b'Default encoding set to %s', sys.getdefaultencoding())
    return


def resMgrListDir(path, fnpat=None):
    dir = ResMgr.openSection(path)
    if dir is None:
        return
    else:
        if not fnpat:
            return dir.keys()
        return [n for n in dir.keys() if fnmatch.fnmatch(n, fnpat)]


def resMgrDirExists(path):
    return ResMgr.openSection(path) is not None


def getsitepackages():
    sitepackages = []
    seen = set()
    from soft_exception import SoftException
    if not PLATFORM_SUFFIX:
        raise SoftException(b'Unable to determine platform suffix')
    for prefix in sys.path:
        if not prefix or prefix in seen:
            continue
        seen.add(prefix)
        if prefix.endswith(b'scripts/server_common'):
            fullPath = os.path.join(prefix, b'site-packages') + b'/' + PLATFORM_SUFFIX
            sitepackages.append(fullPath)
        else:
            sitepackages.append(os.path.join(prefix, b'site-packages'))

    return sitepackages


def _init_pathinfo():
    return set(sys.path)


def addpackage(sitedir, name, known_paths):
    if known_paths is None:
        _init_pathinfo()
        reset = 1
    else:
        reset = 0
    fullname = os.path.join(sitedir, name)
    try:
        f = builtins.open(fullname, b'rU', encoding=b'utf-8')
    except IOError as error:
        print(b'ioerror', error, fullname, file=sys.stderr)
        return

    with f:
        resolveToAbs = False
        for n, line in enumerate(f):
            if line.startswith(b'#'):
                continue
            if line.startswith(b'@'):
                resolveToAbs = True
                continue
            try:
                if line.startswith((b'import ', b'import\t')):
                    exec line
                    continue
                line = line.rstrip()
                relativeDir = os.path.join(sitedir, line)
                if resolveToAbs:
                    dir = ResMgr.resolveToAbsolutePath(relativeDir)
                else:
                    dir = relativeDir
                if dir not in known_paths and resMgrDirExists(relativeDir):
                    sys.path.append(dir)
                    known_paths.add(dir)
            except Exception:
                print((b'Error processing line {:d} of {}:\n').format(n + 1, fullname), file=sys.stderr)
                for record in traceback.format_exception(*sys.exc_info()):
                    for sLine in record.splitlines():
                        print(b'  ' + sLine, file=sys.stderr)

                print(b'\nRemainder of file ignored', file=sys.stderr)
                break

    if reset:
        known_paths = None
    return known_paths


def addsitedir(sitedir, known_paths=None):
    if known_paths is None:
        known_paths = _init_pathinfo()
        reset = 1
    else:
        reset = 0
    if sitedir not in known_paths:
        sys.path.append(sitedir)
    names = resMgrListDir(sitedir, b'*.pth')
    if names is None or len(names) == 0:
        return
    for name in sorted(names):
        addpackage(sitedir, name, known_paths)

    if reset:
        known_paths = None
    return known_paths


def addsitepackages(known_paths):
    for sitedir in getsitepackages():
        if resMgrDirExists(sitedir):
            addsitedir(sitedir, known_paths)

    return known_paths


def setup_paths():
    known_paths = set(sys.path)
    addsitepackages(known_paths)
    sys.path = [p.replace(b'\\', b'/') for p in sys.path]
    return


@BWUtil.if_only_component(b'base', b'service', b'cell', b'database')
def set_twisted_reactor():
    import BWTwistedReactor, twisted.internet.default
    twisted.internet.default = BWTwistedReactor
    return


def set_builtin_open_patch():
    BWUtil.monkeyPatchOpen(full_replace=BigWorld.component in (b'client', b'bot'))
    return


@BWUtil.if_only_component(b'client', b'bot')
def revert_builtin_open_patch():
    BWUtil.revertPatchedOpen()
    return


@BWUtil.if_only_not_component(b'client', b'bot')
def patch_future_builtins_open():
    BWUtil.monkeyPatchFutureOpen()
    return


@BWUtil.if_only_not_component(b'process_defs')
def set_threading_bootstrap():
    import threading
    orig_bootstrap = threading.Thread._Thread__bootstrap

    def hooked_bootstrap(self):
        BigWorld.__onThreadStart(self.name)
        orig_bootstrap(self)
        BigWorld.__onThreadEnd()
        return

    threading.Thread._Thread__bootstrap = hooked_bootstrap
    return


def main():
    BWLogging.init()
    set_builtin_open_patch()
    set_threading_bootstrap()
    set_helper()
    set_default_encoding()
    setup_paths()
    revert_builtin_open_patch()
    patch_future_builtins_open()
    set_twisted_reactor()
    import bwpydevd
    bwpydevd.startDebug(isStartUp=True)
    return


main()
try:
    import BWAutoImport
except ImportError as e:
    NOTICE_MSG(b'bw_site.py failed to import BWAutoImport: %s\n' % (e,))
