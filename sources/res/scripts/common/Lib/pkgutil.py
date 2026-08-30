import os, sys, imp, os.path
from types import ModuleType
__all__ = [
 3, 4, 5, 6, 
 7, 8, 9, 
 10, 11, 12, 13]

def read_code(stream):
    import marshal
    magic = stream.read(4)
    if magic != imp.get_magic():
        return
    else:
        stream.read(4)
        return marshal.load(stream)


def simplegeneric(func):
    registry = {}

    def wrapper(*args, **kw):
        ob = args[0]
        try:
            cls = ob.__class__
        except AttributeError:
            cls = type(ob)

        try:
            mro = cls.__mro__
        except AttributeError:
            try:

                class cls(cls, object):
                    pass

                mro = cls.__mro__[1:]
            except TypeError:
                mro = (
                 object,)

        for t in mro:
            if t in registry:
                return registry[t](*args, **kw)
        else:
            return func(*args, **kw)

        return

    try:
        wrapper.__name__ = func.__name__
    except (TypeError, AttributeError):
        pass

    def register(typ, func=None):
        if func is None:
            return (lambda f: register(typ, f))
        else:
            registry[typ] = func
            return func

    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    wrapper.register = register
    return wrapper


def walk_packages(path=None, prefix=b'', onerror=None):

    def seen(p, m={}):
        if p in m:
            return True
        m[p] = True
        return

    for importer, name, ispkg in iter_modules(path, prefix):
        yield (
         importer, name, ispkg)
        if ispkg:
            try:
                __import__(name)
            except ImportError:
                if onerror is not None:
                    onerror(name)
            except Exception:
                if onerror is not None:
                    onerror(name)
                else:
                    raise

            path = getattr(sys.modules[name], b'__path__', None) or []
            path = [p for p in path if not seen(p)]
            for item in walk_packages(path, name + b'.', onerror):
                yield item

    return


def iter_modules(path=None, prefix=b''):
    if path is None:
        importers = iter_importers()
    else:
        importers = map(get_importer, path)
    yielded = {}
    for i in importers:
        for name, ispkg in iter_importer_modules(i, prefix):
            if name not in yielded:
                yielded[name] = 1
                yield (i, name, ispkg)

    return


def iter_importer_modules(importer, prefix=b''):
    if not hasattr(importer, b'iter_modules'):
        return []
    return importer.iter_modules(prefix)


iter_importer_modules = simplegeneric(iter_importer_modules)

class ImpImporter:

    def __init__(self, path=None):
        self.path = path
        return

    def find_module(self, fullname, path=None):
        subname = fullname.split(b'.')[-1]
        if subname != fullname and self.path is None:
            return
        else:
            if self.path is None:
                path = None
            else:
                path = [
                 os.path.realpath(self.path)]
            try:
                file, filename, etc = imp.find_module(subname, path)
            except ImportError:
                return

            return ImpLoader(fullname, file, filename, etc)

    def iter_modules(self, prefix=b''):
        if self.path is None or not os.path.isdir(self.path):
            return
        yielded = {}
        import inspect
        try:
            filenames = os.listdir(self.path)
        except OSError:
            filenames = []

        filenames.sort()
        for fn in filenames:
            modname = inspect.getmodulename(fn)
            if modname == b'__init__' or modname in yielded:
                continue
            path = os.path.join(self.path, fn)
            ispkg = False
            if not modname and os.path.isdir(path) and b'.' not in fn:
                modname = fn
                try:
                    dircontents = os.listdir(path)
                except OSError:
                    dircontents = []

                for fn in dircontents:
                    subname = inspect.getmodulename(fn)
                    if subname == b'__init__':
                        ispkg = True
                        break
                else:
                    continue

            if modname and b'.' not in modname:
                yielded[modname] = 1
                yield (prefix + modname, ispkg)

        return


class ImpLoader:
    code = source = None

    def __init__(self, fullname, file, filename, etc):
        self.file = file
        self.filename = filename
        self.fullname = fullname
        self.etc = etc
        return

    def load_module(self, fullname):
        self._reopen()
        try:
            mod = imp.load_module(fullname, self.file, self.filename, self.etc)
        finally:
            if self.file:
                self.file.close()

        return mod

    def get_data(self, pathname):
        with open(pathname, b'rb') as file:
            return file.read()
        return

    def _reopen(self):
        if self.file and self.file.closed:
            mod_type = self.etc[2]
            if mod_type == imp.PY_SOURCE:
                self.file = open(self.filename, b'rU')
            elif mod_type in (imp.PY_COMPILED, imp.C_EXTENSION):
                self.file = open(self.filename, b'rb')
        return

    def _fix_name(self, fullname):
        if fullname is None:
            fullname = self.fullname
        elif fullname != self.fullname:
            raise ImportError(b'Loader for module %s cannot handle module %s' % (
             self.fullname, fullname))
        return fullname

    def is_package(self, fullname):
        fullname = self._fix_name(fullname)
        return self.etc[2] == imp.PKG_DIRECTORY

    def get_code(self, fullname=None):
        fullname = self._fix_name(fullname)
        if self.code is None:
            mod_type = self.etc[2]
            if mod_type == imp.PY_SOURCE:
                source = self.get_source(fullname)
                self.code = compile(source, self.filename, b'exec')
            elif mod_type == imp.PY_COMPILED:
                self._reopen()
                try:
                    self.code = read_code(self.file)
                finally:
                    self.file.close()

            elif mod_type == imp.PKG_DIRECTORY:
                self.code = self._get_delegate().get_code()
        return self.code

    def get_source(self, fullname=None):
        fullname = self._fix_name(fullname)
        if self.source is None:
            mod_type = self.etc[2]
            if mod_type == imp.PY_SOURCE:
                self._reopen()
                try:
                    self.source = self.file.read()
                finally:
                    self.file.close()

            elif mod_type == imp.PY_COMPILED:
                if os.path.exists(self.filename[:-1]):
                    f = open(self.filename[:-1], b'rU')
                    self.source = f.read()
                    f.close()
            elif mod_type == imp.PKG_DIRECTORY:
                self.source = self._get_delegate().get_source()
        return self.source

    def _get_delegate(self):
        return ImpImporter(self.filename).find_module(b'__init__')

    def get_filename(self, fullname=None):
        fullname = self._fix_name(fullname)
        mod_type = self.etc[2]
        if self.etc[2] == imp.PKG_DIRECTORY:
            return self._get_delegate().get_filename()
        else:
            if self.etc[2] in (imp.PY_SOURCE, imp.PY_COMPILED, imp.C_EXTENSION):
                return self.filename
            return


try:
    import zipimport
    from zipimport import zipimporter

    def iter_zipimport_modules(importer, prefix=b''):
        dirlist = zipimport._zip_directory_cache[importer.archive].keys()
        dirlist.sort()
        _prefix = importer.prefix
        plen = len(_prefix)
        yielded = {}
        import inspect
        for fn in dirlist:
            if not fn.startswith(_prefix):
                continue
            fn = fn[plen:].split(os.sep)
            if len(fn) == 2 and fn[1].startswith(b'__init__.py'):
                if fn[0] not in yielded:
                    yielded[fn[0]] = 1
                    yield (fn[0], True)
            if len(fn) != 1:
                continue
            modname = inspect.getmodulename(fn[0])
            if modname == b'__init__':
                continue
            if modname and b'.' not in modname and modname not in yielded:
                yielded[modname] = 1
                yield (prefix + modname, False)

        return


    iter_importer_modules.register(zipimporter, iter_zipimport_modules)
except ImportError:
    pass

def get_importer(path_item):
    try:
        importer = sys.path_importer_cache[path_item]
    except KeyError:
        for path_hook in sys.path_hooks:
            try:
                importer = path_hook(path_item)
                break
            except ImportError:
                pass

        else:
            importer = None

        sys.path_importer_cache.setdefault(path_item, importer)

    if importer is None:
        try:
            importer = ImpImporter(path_item)
        except ImportError:
            importer = None

    return importer


def iter_importers(fullname=b''):
    if fullname.startswith(b'.'):
        raise ImportError(b'Relative module names not supported')
    if b'.' in fullname:
        pkg = (b'.').join(fullname.split(b'.')[:-1])
        if pkg not in sys.modules:
            __import__(pkg)
        path = getattr(sys.modules[pkg], b'__path__', None) or []
    else:
        for importer in sys.meta_path:
            yield importer

        path = sys.path
    for item in path:
        yield get_importer(item)

    if b'.' not in fullname:
        yield ImpImporter()
    return


def get_loader(module_or_name):
    if module_or_name in sys.modules:
        module_or_name = sys.modules[module_or_name]
    if isinstance(module_or_name, ModuleType):
        module = module_or_name
        loader = getattr(module, b'__loader__', None)
        if loader is not None:
            return loader
        fullname = module.__name__
    else:
        fullname = module_or_name
    return find_loader(fullname)


def find_loader(fullname):
    for importer in iter_importers(fullname):
        loader = importer.find_module(fullname)
        if loader is not None:
            return loader

    return


def extend_path(path, name):
    if not isinstance(path, list):
        return path
    pname = os.path.join(*name.split(b'.'))
    sname = os.extsep.join(name.split(b'.'))
    sname_pkg = sname + os.extsep + b'pkg'
    init_py = b'__init__' + os.extsep + b'py'
    path = path[:]
    for dir in sys.path:
        if not isinstance(dir, basestring) or not os.path.isdir(dir):
            continue
        subdir = os.path.join(dir, pname)
        initfile = os.path.join(subdir, init_py)
        if subdir not in path and os.path.isfile(initfile):
            path.append(subdir)
        pkgfile = os.path.join(dir, sname_pkg)
        if os.path.isfile(pkgfile):
            try:
                f = open(pkgfile)
            except IOError as msg:
                sys.stderr.write(b"Can't open %s: %s\n" % (
                 pkgfile, msg))
            else:
                for line in f:
                    line = line.rstrip(b'\n')
                    if not line or line.startswith(b'#'):
                        continue
                    path.append(line)

                f.close()

    return path


def get_data(package, resource):
    loader = get_loader(package)
    if loader is None or not hasattr(loader, b'get_data'):
        return
    mod = sys.modules.get(package) or loader.load_module(package)
    if mod is None or not hasattr(mod, b'__file__'):
        return
    parts = resource.split(b'/')
    parts.insert(0, os.path.dirname(mod.__file__))
    resource_name = os.path.join(*parts)
    return loader.get_data(resource_name)
