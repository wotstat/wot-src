import os, sys, shutil, tempfile, unittest, sysconfig
from copy import deepcopy
import warnings
from distutils import log
from distutils.log import DEBUG, INFO, WARN, ERROR, FATAL
from distutils.core import Distribution

def capture_warnings(func):

    def _capture_warnings(*args, **kw):
        with warnings.catch_warnings():
            warnings.simplefilter(b'ignore')
            return func(*args, **kw)
        return

    return _capture_warnings


class LoggingSilencer(object):

    def setUp(self):
        super(LoggingSilencer, self).setUp()
        self.threshold = log.set_threshold(log.FATAL)
        self._old_log = log.Log._log
        log.Log._log = self._log
        self.logs = []
        return

    def tearDown(self):
        log.set_threshold(self.threshold)
        log.Log._log = self._old_log
        super(LoggingSilencer, self).tearDown()
        return

    def _log(self, level, msg, args):
        if level not in (DEBUG, INFO, WARN, ERROR, FATAL):
            raise ValueError(b'%s wrong log level' % str(level))
        self.logs.append((level, msg, args))
        return

    def get_logs(self, *levels):

        def _format(msg, args):
            if len(args) == 0:
                return msg
            return msg % args

        return [_format(msg, args) for level, msg, args in self.logs if level in levels]

    def clear_logs(self):
        self.logs = []
        return


class TempdirManager(object):

    def setUp(self):
        super(TempdirManager, self).setUp()
        self.old_cwd = os.getcwd()
        self.tempdirs = []
        return

    def tearDown(self):
        os.chdir(self.old_cwd)
        super(TempdirManager, self).tearDown()
        while self.tempdirs:
            d = self.tempdirs.pop()
            shutil.rmtree(d, os.name in (b'nt', b'cygwin'))

        return

    def mkdtemp(self):
        d = tempfile.mkdtemp()
        self.tempdirs.append(d)
        return d

    def write_file(self, path, content=b'xxx'):
        if isinstance(path, (list, tuple)):
            path = os.path.join(*path)
        f = open(path, b'w')
        try:
            f.write(content)
        finally:
            f.close()

        return

    def create_dist(self, pkg_name=b'foo', **kw):
        tmp_dir = self.mkdtemp()
        pkg_dir = os.path.join(tmp_dir, pkg_name)
        os.mkdir(pkg_dir)
        dist = Distribution(attrs=kw)
        return (
         pkg_dir, dist)


class DummyCommand:

    def __init__(self, **kwargs):
        for kw, val in kwargs.items():
            setattr(self, kw, val)

        return

    def ensure_finalized(self):
        return


class EnvironGuard(object):

    def setUp(self):
        super(EnvironGuard, self).setUp()
        self.old_environ = deepcopy(os.environ)
        return

    def tearDown(self):
        for key, value in self.old_environ.items():
            if os.environ.get(key) != value:
                os.environ[key] = value

        for key in os.environ.keys():
            if key not in self.old_environ:
                del os.environ[key]

        super(EnvironGuard, self).tearDown()
        return


def copy_xxmodule_c(directory):
    filename = _get_xxmodule_path()
    if filename is None:
        raise unittest.SkipTest(b'cannot find xxmodule.c (test must run in the python build dir)')
    shutil.copy(filename, directory)
    return


def _get_xxmodule_path():
    srcdir = sysconfig.get_config_var(b'srcdir')
    candidates = [
     os.path.join(os.path.dirname(__file__), b'xxmodule.c'),
     os.path.join(srcdir, b'Modules', b'xxmodule.c'),
     os.path.join(srcdir, b'..', b'..', b'..', b'Modules', b'xxmodule.c')]
    for path in candidates:
        if os.path.exists(path):
            return path

    return


def fixup_build_ext(cmd):
    if os.name == b'nt':
        cmd.debug = sys.executable.endswith(b'_d.exe')
    elif sysconfig.get_config_var(b'Py_ENABLE_SHARED'):
        runshared = sysconfig.get_config_var(b'RUNSHARED')
        if runshared is None:
            cmd.library_dirs = [
             b'.']
        elif sys.platform == b'darwin':
            cmd.library_dirs = []
        else:
            name, equals, value = runshared.partition(b'=')
            cmd.library_dirs = [d for d in value.split(os.pathsep) if d]
    return
