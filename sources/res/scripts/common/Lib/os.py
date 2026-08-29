import sys, errno
_names = sys.builtin_module_names
__all__ = [
 2, 3, 4, 5, 6, 7, 8, 
 9, 10, 11, 12, 
 13, 14, 15]

def _get_exports_list(module):
    try:
        return list(module.__all__)
    except AttributeError:
        return [n for n in dir(module) if n[0] != b'_']

    return


if b'posix' in _names:
    name = b'posix'
    linesep = b'\n'
    from posix import *
    try:
        from posix import _exit
    except ImportError:
        pass

    import posixpath as path, posix
    __all__.extend(_get_exports_list(posix))
    del posix
elif b'nt' in _names:
    name = b'nt'
    linesep = b'\r\n'
    from nt import *
    try:
        from nt import _exit
    except ImportError:
        pass

    import ntpath as path, nt
    __all__.extend(_get_exports_list(nt))
    del nt
elif b'os2' in _names:
    name = b'os2'
    linesep = b'\r\n'
    from os2 import *
    try:
        from os2 import _exit
    except ImportError:
        pass

    if sys.version.find(b'EMX GCC') == -1:
        import ntpath as path
    else:
        import os2emxpath as path
        from _emx_link import link
    import os2
    __all__.extend(_get_exports_list(os2))
    del os2
elif b'ce' in _names:
    name = b'ce'
    linesep = b'\r\n'
    from ce import *
    try:
        from ce import _exit
    except ImportError:
        pass

    import ntpath as path, ce
    __all__.extend(_get_exports_list(ce))
    del ce
elif b'riscos' in _names:
    name = b'riscos'
    linesep = b'\n'
    from riscos import *
    try:
        from riscos import _exit
    except ImportError:
        pass

    import riscospath as path, riscos
    __all__.extend(_get_exports_list(riscos))
    del riscos
else:
    raise ImportError, b'no os specific module found'
sys.modules[b'os.path'] = path
from os.path import curdir, pardir, sep, pathsep, defpath, extsep, altsep, devnull
del _names
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

def makedirs(name, mode=511):
    head, tail = path.split(name)
    if not tail:
        head, tail = path.split(head)
    if head and tail and not path.exists(head):
        try:
            makedirs(head, mode)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        if tail == curdir:
            return
    mkdir(name, mode)
    return


def removedirs(name):
    rmdir(name)
    head, tail = path.split(name)
    if not tail:
        head, tail = path.split(head)
    while head and tail:
        try:
            rmdir(head)
        except error:
            break

        head, tail = path.split(head)

    return


def renames(old, new):
    head, tail = path.split(new)
    if head and tail and not path.exists(head):
        makedirs(head)
    rename(old, new)
    head, tail = path.split(old)
    if head and tail:
        try:
            removedirs(head)
        except error:
            pass

    return


__all__.extend([b'makedirs', b'removedirs', b'renames'])

def walk(top, topdown=True, onerror=None, followlinks=False):
    islink, join, isdir = path.islink, path.join, path.isdir
    try:
        names = listdir(top)
    except error as err:
        if onerror is not None:
            onerror(err)
        return

    dirs, nondirs = [], []
    for name in names:
        if isdir(join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    if topdown:
        yield (
         top, dirs, nondirs)
    for name in dirs:
        new_path = join(top, name)
        if followlinks or not islink(new_path):
            for x in walk(new_path, topdown, onerror, followlinks):
                yield x

    if not topdown:
        yield (
         top, dirs, nondirs)
    return


__all__.append(b'walk')
try:
    environ
except NameError:
    environ = {}

def execl(file, *args):
    execv(file, args)
    return


def execle(file, *args):
    env = args[-1]
    execve(file, args[:-1], env)
    return


def execlp(file, *args):
    execvp(file, args)
    return


def execlpe(file, *args):
    env = args[-1]
    execvpe(file, args[:-1], env)
    return


def execvp(file, args):
    _execvpe(file, args)
    return


def execvpe(file, args, env):
    _execvpe(file, args, env)
    return


__all__.extend([49, 50, 51, 52, 53, 54])

def _execvpe(file, args, env=None):
    if env is not None:
        func = execve
        argrest = (args, env)
    else:
        func = execv
        argrest = (args,)
        env = environ
    head, tail = path.split(file)
    if head:
        func(file, *argrest)
        return
    else:
        if b'PATH' in env:
            envpath = env[b'PATH']
        else:
            envpath = defpath
        PATH = envpath.split(pathsep)
        saved_exc = None
        saved_tb = None
        for dir in PATH:
            fullname = path.join(dir, file)
            try:
                func(fullname, *argrest)
            except error as e:
                tb = sys.exc_info()[2]
                if e.errno != errno.ENOENT and e.errno != errno.ENOTDIR and saved_exc is None:
                    saved_exc = e
                    saved_tb = tb

        if saved_exc:
            raise error, saved_exc, saved_tb
        raise error, e, tb
        return


try:
    putenv
except NameError:
    pass
else:
    import UserDict
    if name in (b'os2', b'nt'):

        def unsetenv(key):
            putenv(key, b'')
            return


    if name == b'riscos':
        from riscosenviron import _Environ
    elif name in (b'os2', b'nt'):

        class _Environ(UserDict.IterableUserDict):

            def __init__(self, environ):
                UserDict.UserDict.__init__(self)
                data = self.data
                for k, v in environ.items():
                    data[k.upper()] = v

                return

            def __setitem__(self, key, item):
                putenv(key, item)
                self.data[key.upper()] = item
                return

            def __getitem__(self, key):
                return self.data[key.upper()]

            try:
                unsetenv
            except NameError:

                def __delitem__(self, key):
                    del self.data[key.upper()]
                    return

            else:

                def __delitem__(self, key):
                    unsetenv(key)
                    del self.data[key.upper()]
                    return

                def clear(self):
                    for key in self.data.keys():
                        unsetenv(key)
                        del self.data[key]

                    return

                def pop(self, key, *args):
                    unsetenv(key)
                    return self.data.pop(key.upper(), *args)

            def has_key(self, key):
                return key.upper() in self.data

            def __contains__(self, key):
                return key.upper() in self.data

            def get(self, key, failobj=None):
                return self.data.get(key.upper(), failobj)

            def update(self, dict=None, **kwargs):
                if dict:
                    try:
                        keys = dict.keys()
                    except AttributeError:
                        for k, v in dict:
                            self[k] = v

                    for k in keys:
                        self[k] = dict[k]

                if kwargs:
                    self.update(kwargs)
                return

            def copy(self):
                return dict(self)


    else:

        class _Environ(UserDict.IterableUserDict):

            def __init__(self, environ):
                UserDict.UserDict.__init__(self)
                self.data = environ
                return

            def __setitem__(self, key, item):
                putenv(key, item)
                self.data[key] = item
                return

            def update(self, dict=None, **kwargs):
                if dict:
                    try:
                        keys = dict.keys()
                    except AttributeError:
                        for k, v in dict:
                            self[k] = v

                    for k in keys:
                        self[k] = dict[k]

                if kwargs:
                    self.update(kwargs)
                return

            try:
                unsetenv
            except NameError:
                pass
            else:

                def __delitem__(self, key):
                    unsetenv(key)
                    del self.data[key]
                    return

                def clear(self):
                    for key in self.data.keys():
                        unsetenv(key)
                        del self.data[key]

                    return

                def pop(self, key, *args):
                    unsetenv(key)
                    return self.data.pop(key, *args)

            def copy(self):
                return dict(self)


    environ = _Environ(environ)

def getenv(key, default=None):
    return environ.get(key, default)


__all__.append(b'getenv')

def _exists(name):
    return name in globals()


if _exists(b'fork') and not _exists(b'spawnv') and _exists(b'execv'):
    P_WAIT = 0
    P_NOWAIT = P_NOWAITO = 1

    def _spawnvef(mode, file, args, env, func):
        pid = fork()
        if not pid:
            try:
                if env is None:
                    func(file, args)
                else:
                    func(file, args, env)
            except:
                _exit(127)

        elif mode == P_NOWAIT:
            return pid
        while 1:
            wpid, sts = waitpid(pid, 0)
            if WIFSTOPPED(sts):
                continue
            elif WIFSIGNALED(sts):
                return -WTERMSIG(sts)
            if WIFEXITED(sts):
                return WEXITSTATUS(sts)
            raise error, b'Not stopped, signaled or exited???'

        return


    def spawnv(mode, file, args):
        return _spawnvef(mode, file, args, None, execv)


    def spawnve(mode, file, args, env):
        return _spawnvef(mode, file, args, env, execve)


    def spawnvp(mode, file, args):
        return _spawnvef(mode, file, args, None, execvp)


    def spawnvpe(mode, file, args, env):
        return _spawnvef(mode, file, args, env, execvpe)


if _exists(b'spawnv'):

    def spawnl(mode, file, *args):
        return spawnv(mode, file, args)


    def spawnle(mode, file, *args):
        env = args[-1]
        return spawnve(mode, file, args[:-1], env)


    __all__.extend([b'spawnv', b'spawnve', b'spawnl', b'spawnle'])
if _exists(b'spawnvp'):

    def spawnlp(mode, file, *args):
        return spawnvp(mode, file, args)


    def spawnlpe(mode, file, *args):
        env = args[-1]
        return spawnvpe(mode, file, args[:-1], env)


    __all__.extend([b'spawnvp', b'spawnvpe', b'spawnlp', b'spawnlpe'])
if _exists(b'fork'):
    if not _exists(b'popen2'):

        def popen2(cmd, mode=b't', bufsize=-1):
            import warnings
            msg = b'os.popen2 is deprecated.  Use the subprocess module.'
            warnings.warn(msg, DeprecationWarning, stacklevel=2)
            import subprocess
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring), bufsize=bufsize, stdin=PIPE, stdout=PIPE, close_fds=True)
            return (p.stdin, p.stdout)


        __all__.append(b'popen2')
    if not _exists(b'popen3'):

        def popen3(cmd, mode=b't', bufsize=-1):
            import warnings
            msg = b'os.popen3 is deprecated.  Use the subprocess module.'
            warnings.warn(msg, DeprecationWarning, stacklevel=2)
            import subprocess
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring), bufsize=bufsize, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
            return (p.stdin, p.stdout, p.stderr)


        __all__.append(b'popen3')
    if not _exists(b'popen4'):

        def popen4(cmd, mode=b't', bufsize=-1):
            import warnings
            msg = b'os.popen4 is deprecated.  Use the subprocess module.'
            warnings.warn(msg, DeprecationWarning, stacklevel=2)
            import subprocess
            PIPE = subprocess.PIPE
            p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring), bufsize=bufsize, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
            return (p.stdin, p.stdout)


        __all__.append(b'popen4')
import copy_reg as _copy_reg

def _make_stat_result(tup, dict):
    return stat_result(tup, dict)


def _pickle_stat_result(sr):
    type, args = sr.__reduce__()
    return (_make_stat_result, args)


try:
    _copy_reg.pickle(stat_result, _pickle_stat_result, _make_stat_result)
except NameError:
    pass

def _make_statvfs_result(tup, dict):
    return statvfs_result(tup, dict)


def _pickle_statvfs_result(sr):
    type, args = sr.__reduce__()
    return (_make_statvfs_result, args)


try:
    _copy_reg.pickle(statvfs_result, _pickle_statvfs_result, _make_statvfs_result)
except NameError:
    pass
