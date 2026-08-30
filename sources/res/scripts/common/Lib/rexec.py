from warnings import warnpy3k
warnpy3k(b'the rexec module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import sys, __builtin__, os, ihooks, imp
__all__ = [
 b'RExec']

class FileBase():
    ok_file_methods = (b'fileno', b'flush', b'isatty', b'read', b'readline', b'readlines', b'seek', b'tell', b'write', b'writelines', b'xreadlines', b'__iter__')


class FileWrapper(FileBase):

    def __init__(self, f):
        for m in self.ok_file_methods:
            if not hasattr(self, m) and hasattr(f, m):
                setattr(self, m, getattr(f, m))

        return

    def close(self):
        self.flush()
        return


TEMPLATE = b'\ndef %s(self, *args):\n        return getattr(self.mod, self.name).%s(*args)\n'

class FileDelegate(FileBase):

    def __init__(self, mod, name):
        self.mod = mod
        self.name = name
        return

    for m in FileBase.ok_file_methods + (b'close',):
        exec TEMPLATE % (m, m)


class RHooks(ihooks.Hooks):

    def __init__(self, *args):
        verbose = 0
        rexec = None
        if args and type(args[-1]) == type(0):
            verbose = args[-1]
            args = args[:-1]
        if args and hasattr(args[0], b'__class__'):
            rexec = args[0]
            args = args[1:]
        if args:
            raise TypeError, b'too many arguments'
        ihooks.Hooks.__init__(self, verbose)
        self.rexec = rexec
        return

    def set_rexec(self, rexec):
        self.rexec = rexec
        return

    def get_suffixes(self):
        return self.rexec.get_suffixes()

    def is_builtin(self, name):
        return self.rexec.is_builtin(name)

    def init_builtin(self, name):
        m = __import__(name)
        return self.rexec.copy_except(m, ())

    def init_frozen(self, name):
        raise SystemError, b"don't use this"
        return

    def load_source(self, *args):
        raise SystemError, b"don't use this"
        return

    def load_compiled(self, *args):
        raise SystemError, b"don't use this"
        return

    def load_package(self, *args):
        raise SystemError, b"don't use this"
        return

    def load_dynamic(self, name, filename, file):
        return self.rexec.load_dynamic(name, filename, file)

    def add_module(self, name):
        return self.rexec.add_module(name)

    def modules_dict(self):
        return self.rexec.modules

    def default_path(self):
        return self.rexec.modules[b'sys'].path


RModuleLoader = ihooks.FancyModuleLoader
RModuleImporter = ihooks.ModuleImporter

class RExec(ihooks._Verbose):
    ok_path = tuple(sys.path)
    ok_builtin_modules = (b'audioop', b'array', b'binascii', b'cmath', b'errno', b'imageop', b'marshal', b'math', b'md5', b'operator', b'parser', b'select', b'sha', b'_sre', b'strop', b'struct', b'time', b'_weakref')
    ok_posix_names = (b'error', b'fstat', b'listdir', b'lstat', b'readlink', b'stat', b'times', b'uname', b'getpid', b'getppid', b'getcwd', b'getuid', b'getgid', b'geteuid', b'getegid')
    ok_sys_names = (b'byteorder', b'copyright', b'exit', b'getdefaultencoding', b'getrefcount', b'hexversion', b'maxint', b'maxunicode', b'platform', b'ps1', b'ps2', b'version', b'version_info')
    nok_builtin_names = (b'open', b'file', b'reload', b'__import__')
    ok_file_types = (
     imp.C_EXTENSION, imp.PY_SOURCE)

    def __init__(self, hooks=None, verbose=0):
        raise RuntimeError, b'This code is not secure in Python 2.2 and later'
        ihooks._Verbose.__init__(self, verbose)
        self.hooks = hooks or RHooks(verbose)
        self.hooks.set_rexec(self)
        self.modules = {}
        self.ok_dynamic_modules = self.ok_builtin_modules
        list = []
        for mname in self.ok_builtin_modules:
            if mname in sys.builtin_module_names:
                list.append(mname)

        self.ok_builtin_modules = tuple(list)
        self.set_trusted_path()
        self.make_builtin()
        self.make_initial_modules()
        self.make_sys()
        self.loader = RModuleLoader(self.hooks, verbose)
        self.importer = RModuleImporter(self.loader, verbose)
        return

    def set_trusted_path(self):
        self.trusted_path = filter(os.path.isabs, sys.path)
        return

    def load_dynamic(self, name, filename, file):
        if name not in self.ok_dynamic_modules:
            raise ImportError, b'untrusted dynamic module: %s' % name
        if name in sys.modules:
            src = sys.modules[name]
        else:
            src = imp.load_dynamic(name, filename, file)
        dst = self.copy_except(src, [])
        return dst

    def make_initial_modules(self):
        self.make_main()
        self.make_osname()
        return

    def get_suffixes(self):
        return [item for item in imp.get_suffixes() if item[2] in self.ok_file_types]

    def is_builtin(self, mname):
        return mname in self.ok_builtin_modules

    def make_builtin(self):
        m = self.copy_except(__builtin__, self.nok_builtin_names)
        m.__import__ = self.r_import
        m.reload = self.r_reload
        m.open = m.file = self.r_open
        return

    def make_main(self):
        self.add_module(b'__main__')
        return

    def make_osname(self):
        osname = os.name
        src = __import__(osname)
        dst = self.copy_only(src, self.ok_posix_names)
        dst.environ = e = {}
        for key, value in os.environ.items():
            e[key] = value

        return

    def make_sys(self):
        m = self.copy_only(sys, self.ok_sys_names)
        m.modules = self.modules
        m.argv = [b'RESTRICTED']
        m.path = map(None, self.ok_path)
        m.exc_info = self.r_exc_info
        m = self.modules[b'sys']
        l = self.modules.keys() + list(self.ok_builtin_modules)
        l.sort()
        m.builtin_module_names = tuple(l)
        return

    def copy_except(self, src, exceptions):
        dst = self.copy_none(src)
        for name in dir(src):
            setattr(dst, name, getattr(src, name))

        for name in exceptions:
            try:
                delattr(dst, name)
            except AttributeError:
                pass

        return dst

    def copy_only(self, src, names):
        dst = self.copy_none(src)
        for name in names:
            try:
                value = getattr(src, name)
            except AttributeError:
                continue

            setattr(dst, name, value)

        return dst

    def copy_none(self, src):
        m = self.add_module(src.__name__)
        m.__doc__ = src.__doc__
        return m

    def add_module(self, mname):
        m = self.modules.get(mname)
        if m is None:
            self.modules[mname] = m = self.hooks.new_module(mname)
        m.__builtins__ = self.modules[b'__builtin__']
        return m

    def r_exec(self, code):
        m = self.add_module(b'__main__')
        exec code in m.__dict__
        return

    def r_eval(self, code):
        m = self.add_module(b'__main__')
        return eval(code, m.__dict__)

    def r_execfile(self, file):
        m = self.add_module(b'__main__')
        execfile(file, m.__dict__)
        return

    def r_import(self, mname, globals={}, locals={}, fromlist=[]):
        return self.importer.import_module(mname, globals, locals, fromlist)

    def r_reload(self, m):
        return self.importer.reload(m)

    def r_unload(self, m):
        return self.importer.unload(m)

    def make_delegate_files(self):
        s = self.modules[b'sys']
        self.delegate_stdin = FileDelegate(s, b'stdin')
        self.delegate_stdout = FileDelegate(s, b'stdout')
        self.delegate_stderr = FileDelegate(s, b'stderr')
        self.restricted_stdin = FileWrapper(sys.stdin)
        self.restricted_stdout = FileWrapper(sys.stdout)
        self.restricted_stderr = FileWrapper(sys.stderr)
        return

    def set_files(self):
        if not hasattr(self, b'save_stdin'):
            self.save_files()
        if not hasattr(self, b'delegate_stdin'):
            self.make_delegate_files()
        s = self.modules[b'sys']
        s.stdin = self.restricted_stdin
        s.stdout = self.restricted_stdout
        s.stderr = self.restricted_stderr
        sys.stdin = self.delegate_stdin
        sys.stdout = self.delegate_stdout
        sys.stderr = self.delegate_stderr
        return

    def reset_files(self):
        self.restore_files()
        s = self.modules[b'sys']
        self.restricted_stdin = s.stdin
        self.restricted_stdout = s.stdout
        self.restricted_stderr = s.stderr
        return

    def save_files(self):
        self.save_stdin = sys.stdin
        self.save_stdout = sys.stdout
        self.save_stderr = sys.stderr
        return

    def restore_files(self):
        sys.stdin = self.save_stdin
        sys.stdout = self.save_stdout
        sys.stderr = self.save_stderr
        return

    def s_apply(self, func, args=(), kw={}):
        self.save_files()
        try:
            self.set_files()
            r = func(*args, **kw)
        finally:
            self.restore_files()

        return r

    def s_exec(self, *args):
        return self.s_apply(self.r_exec, args)

    def s_eval(self, *args):
        return self.s_apply(self.r_eval, args)

    def s_execfile(self, *args):
        return self.s_apply(self.r_execfile, args)

    def s_import(self, *args):
        return self.s_apply(self.r_import, args)

    def s_reload(self, *args):
        return self.s_apply(self.r_reload, args)

    def s_unload(self, *args):
        return self.s_apply(self.r_unload, args)

    def r_open(self, file, mode=b'r', buf=-1):
        mode = str(mode)
        if mode not in (b'r', b'rb'):
            raise IOError, b"can't open files for writing in restricted mode"
        return open(file, mode, buf)

    def r_exc_info(self):
        ty, va, tr = sys.exc_info()
        tr = None
        return (ty, va, tr)


def test():
    import getopt, traceback
    opts, args = getopt.getopt(sys.argv[1:], b'vt:')
    verbose = 0
    trusted = []
    for o, a in opts:
        if o == b'-v':
            verbose = verbose + 1
        if o == b'-t':
            trusted.append(a)

    r = RExec(verbose=verbose)
    if trusted:
        r.ok_builtin_modules = r.ok_builtin_modules + tuple(trusted)
    if args:
        r.modules[b'sys'].argv = args
        r.modules[b'sys'].path.insert(0, os.path.dirname(args[0]))
    else:
        r.modules[b'sys'].path.insert(0, b'')
    fp = sys.stdin
    if args and args[0] != b'-':
        try:
            fp = open(args[0])
        except IOError as msg:
            print b"%s: can't open file %r" % (sys.argv[0], args[0])
            return 1

    if fp.isatty():
        try:
            import readline
        except ImportError:
            pass

        import code

        class RestrictedConsole(code.InteractiveConsole):

            def runcode(self, co):
                self.locals[b'__builtins__'] = r.modules[b'__builtin__']
                r.s_apply(code.InteractiveConsole.runcode, (self, co))
                return

        try:
            RestrictedConsole(r.modules[b'__main__'].__dict__).interact()
        except SystemExit as n:
            return n

    else:
        text = fp.read()
        fp.close()
        c = compile(text, fp.name, b'exec')
        try:
            r.s_exec(c)
        except SystemExit as n:
            return n
        except:
            traceback.print_exc()
            return 1

    return


if __name__ == b'__main__':
    sys.exit(test())
