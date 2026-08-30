from __future__ import generators
import dis, imp, marshal, os, sys, types, struct
if hasattr(sys.__stdout__, b'newlines'):
    READ_MODE = b'U'
else:
    READ_MODE = b'r'
LOAD_CONST = dis.opmap[b'LOAD_CONST']
IMPORT_NAME = dis.opmap[b'IMPORT_NAME']
STORE_NAME = dis.opmap[b'STORE_NAME']
STORE_GLOBAL = dis.opmap[b'STORE_GLOBAL']
STORE_OPS = (STORE_NAME, STORE_GLOBAL)
HAVE_ARGUMENT = dis.HAVE_ARGUMENT
EXTENDED_ARG = dis.EXTENDED_ARG

def _unpack_opargs(code):
    extended_arg = 0
    n = len(code)
    i = 0
    while i < n:
        op = ord(code[i])
        offset = i
        i = i + 1
        arg = None
        if op >= HAVE_ARGUMENT:
            arg = ord(code[i]) + ord(code[i + 1]) * 256 + extended_arg
            extended_arg = 0
            i = i + 2
            if op == EXTENDED_ARG:
                extended_arg = arg * 65536
        yield (
         offset, op, arg)

    return


packagePathMap = {}

def AddPackagePath(packagename, path):
    paths = packagePathMap.get(packagename, [])
    paths.append(path)
    packagePathMap[packagename] = paths
    return


replacePackageMap = {}

def ReplacePackage(oldname, newname):
    replacePackageMap[oldname] = newname
    return


class Module():

    def __init__(self, name, file=None, path=None):
        self.__name__ = name
        self.__file__ = file
        self.__path__ = path
        self.__code__ = None
        self.globalnames = {}
        self.starimports = {}
        return

    def __repr__(self):
        s = b'Module(%r' % (self.__name__,)
        if self.__file__ is not None:
            s = s + b', %r' % (self.__file__,)
        if self.__path__ is not None:
            s = s + b', %r' % (self.__path__,)
        s = s + b')'
        return s


class ModuleFinder():

    def __init__(self, path=None, debug=0, excludes=[], replace_paths=[]):
        if path is None:
            path = sys.path
        self.path = path
        self.modules = {}
        self.badmodules = {}
        self.debug = debug
        self.indent = 0
        self.excludes = excludes
        self.replace_paths = replace_paths
        self.processed_paths = []
        return

    def msg(self, level, str, *args):
        if level <= self.debug:
            for i in range(self.indent):
                print b'   ',

            print str,
            for arg in args:
                print repr(arg),

            print
        return

    def msgin(self, *args):
        level = args[0]
        if level <= self.debug:
            self.indent = self.indent + 1
            self.msg(*args)
        return

    def msgout(self, *args):
        level = args[0]
        if level <= self.debug:
            self.indent = self.indent - 1
            self.msg(*args)
        return

    def run_script(self, pathname):
        self.msg(2, b'run_script', pathname)
        with open(pathname, READ_MODE) as fp:
            stuff = (
             b'', b'r', imp.PY_SOURCE)
            self.load_module(b'__main__', fp, pathname, stuff)
        return

    def load_file(self, pathname):
        dir, name = os.path.split(pathname)
        name, ext = os.path.splitext(name)
        with open(pathname, READ_MODE) as fp:
            stuff = (
             ext, b'r', imp.PY_SOURCE)
            self.load_module(name, fp, pathname, stuff)
        return

    def import_hook(self, name, caller=None, fromlist=None, level=-1):
        self.msg(3, b'import_hook', name, caller, fromlist, level)
        parent = self.determine_parent(caller, level=level)
        q, tail = self.find_head_package(parent, name)
        m = self.load_tail(q, tail)
        if not fromlist:
            return q
        else:
            if m.__path__:
                self.ensure_fromlist(m, fromlist)
            return

    def determine_parent(self, caller, level=-1):
        self.msgin(4, b'determine_parent', caller, level)
        if not caller or level == 0:
            self.msgout(4, b'determine_parent -> None')
            return
        else:
            pname = caller.__name__
            if level >= 1:
                if caller.__path__:
                    level -= 1
                if level == 0:
                    parent = self.modules[pname]
                    self.msgout(4, b'determine_parent ->', parent)
                    return parent
                if pname.count(b'.') < level:
                    raise ImportError, b'relative importpath too deep'
                pname = (b'.').join(pname.split(b'.')[:-level])
                parent = self.modules[pname]
                self.msgout(4, b'determine_parent ->', parent)
                return parent
            if caller.__path__:
                parent = self.modules[pname]
                self.msgout(4, b'determine_parent ->', parent)
                return parent
            if b'.' in pname:
                i = pname.rfind(b'.')
                pname = pname[:i]
                parent = self.modules[pname]
                self.msgout(4, b'determine_parent ->', parent)
                return parent
            self.msgout(4, b'determine_parent -> None')
            return

    def find_head_package(self, parent, name):
        self.msgin(4, b'find_head_package', parent, name)
        if b'.' in name:
            i = name.find(b'.')
            head = name[:i]
            tail = name[i + 1:]
        else:
            head = name
            tail = b''
        if parent:
            qname = b'%s.%s' % (parent.__name__, head)
        else:
            qname = head
        q = self.import_module(head, qname, parent)
        if q:
            self.msgout(4, b'find_head_package ->', (q, tail))
            return (
             q, tail)
        else:
            if parent:
                qname = head
                parent = None
                q = self.import_module(head, qname, parent)
                if q:
                    self.msgout(4, b'find_head_package ->', (q, tail))
                    return (
                     q, tail)
            self.msgout(4, b'raise ImportError: No module named', qname)
            raise ImportError, b'No module named ' + qname
            return

    def load_tail(self, q, tail):
        self.msgin(4, b'load_tail', q, tail)
        m = q
        while tail:
            i = tail.find(b'.')
            if i < 0:
                i = len(tail)
            head, tail = tail[:i], tail[i + 1:]
            mname = b'%s.%s' % (m.__name__, head)
            m = self.import_module(head, mname, m)
            if not m:
                self.msgout(4, b'raise ImportError: No module named', mname)
                raise ImportError, b'No module named ' + mname

        self.msgout(4, b'load_tail ->', m)
        return m

    def ensure_fromlist(self, m, fromlist, recursive=0):
        self.msg(4, b'ensure_fromlist', m, fromlist, recursive)
        for sub in fromlist:
            if sub == b'*':
                if not recursive:
                    all = self.find_all_submodules(m)
                    if all:
                        self.ensure_fromlist(m, all, 1)
            elif not hasattr(m, sub):
                subname = b'%s.%s' % (m.__name__, sub)
                submod = self.import_module(sub, subname, m)
                if not submod:
                    raise ImportError, b'No module named ' + subname

        return

    def find_all_submodules(self, m):
        if not m.__path__:
            return
        else:
            modules = {}
            suffixes = []
            for triple in imp.get_suffixes():
                suffixes.append(triple[0])

            for dir in m.__path__:
                try:
                    names = os.listdir(dir)
                except os.error:
                    self.msg(2, b"can't list directory", dir)
                    continue

                for name in names:
                    mod = None
                    for suff in suffixes:
                        n = len(suff)
                        if name[-n:] == suff:
                            mod = name[:-n]
                            break

                    if mod and mod != b'__init__':
                        modules[mod] = mod

            return modules.keys()

    def import_module(self, partname, fqname, parent):
        self.msgin(3, b'import_module', partname, fqname, parent)
        try:
            m = self.modules[fqname]
        except KeyError:
            pass
        else:
            self.msgout(3, b'import_module ->', m)
            return m

        if fqname in self.badmodules:
            self.msgout(3, b'import_module -> None')
            return
        else:
            if parent and parent.__path__ is None:
                self.msgout(3, b'import_module -> None')
                return
            try:
                fp, pathname, stuff = self.find_module(partname, parent and parent.__path__, parent)
            except ImportError:
                self.msgout(3, b'import_module ->', None)
                return

            try:
                m = self.load_module(fqname, fp, pathname, stuff)
            finally:
                if fp:
                    fp.close()

            if parent:
                setattr(parent, partname, m)
            self.msgout(3, b'import_module ->', m)
            return m

    def load_module(self, fqname, fp, pathname, file_info):
        suffix, mode, type = file_info
        self.msgin(2, b'load_module', fqname, fp and b'fp', pathname)
        if type == imp.PKG_DIRECTORY:
            m = self.load_package(fqname, pathname)
            self.msgout(2, b'load_module ->', m)
            return m
        else:
            if type == imp.PY_SOURCE:
                co = compile(fp.read() + b'\n', pathname, b'exec')
            elif type == imp.PY_COMPILED:
                if fp.read(4) != imp.get_magic():
                    self.msgout(2, b'raise ImportError: Bad magic number', pathname)
                    raise ImportError, b'Bad magic number in %s' % pathname
                fp.read(4)
                co = marshal.load(fp)
            else:
                co = None
            m = self.add_module(fqname)
            m.__file__ = pathname
            if co:
                if self.replace_paths:
                    co = self.replace_paths_in_code(co)
                m.__code__ = co
                self.scan_code(co, m)
            self.msgout(2, b'load_module ->', m)
            return m

    def _add_badmodule(self, name, caller):
        if name not in self.badmodules:
            self.badmodules[name] = {}
        if caller:
            self.badmodules[name][caller.__name__] = 1
        else:
            self.badmodules[name][b'-'] = 1
        return

    def _safe_import_hook(self, name, caller, fromlist, level=-1):
        if name in self.badmodules:
            self._add_badmodule(name, caller)
            return
        try:
            self.import_hook(name, caller, level=level)
        except ImportError as msg:
            self.msg(2, b'ImportError:', str(msg))
            self._add_badmodule(name, caller)

        if fromlist:
            for sub in fromlist:
                if sub in self.badmodules:
                    self._add_badmodule(sub, caller)
                    continue
                try:
                    self.import_hook(name, caller, [sub], level=level)
                except ImportError as msg:
                    self.msg(2, b'ImportError:', str(msg))
                    fullname = name + b'.' + sub
                    self._add_badmodule(fullname, caller)

        return

    def scan_opcodes(self, co, unpack=struct.unpack):
        code = co.co_code
        names = co.co_names
        consts = co.co_consts
        opargs = [(op, arg) for _, op, arg in _unpack_opargs(code) if op != EXTENDED_ARG]
        for i, (op, oparg) in enumerate(opargs):
            if c in STORE_OPS:
                yield (
                 b'store', (names[oparg],))
                continue
            if op == IMPORT_NAME and i >= 1 and opargs[i - 1][0] == LOAD_CONST:
                fromlist = consts[opargs[i - 1][1]]
                yield (b'import', (fromlist, names[oparg]))
                continue

        return

    def scan_opcodes_25(self, co):
        code = co.co_code
        names = co.co_names
        consts = co.co_consts
        opargs = [(op, arg) for _, op, arg in _unpack_opargs(code) if op != EXTENDED_ARG]
        for i, (op, oparg) in enumerate(opargs):
            if op in STORE_OPS:
                yield (
                 b'store', (names[oparg],))
                continue
            if op == IMPORT_NAME and i >= 2 and opargs[i - 1][0] == opargs[i - 2][0] == LOAD_CONST:
                level = consts[opargs[i - 2][1]]
                fromlist = consts[opargs[i - 1][1]]
                if level == -1:
                    yield (
                     b'import', (fromlist, names[oparg]))
                elif level == 0:
                    yield (
                     b'absolute_import', (fromlist, names[oparg]))
                else:
                    yield (
                     b'relative_import', (level, fromlist, names[oparg]))
                continue

        return

    def scan_code(self, co, m):
        code = co.co_code
        if sys.version_info >= (2, 5):
            scanner = self.scan_opcodes_25
        else:
            scanner = self.scan_opcodes
        for what, args in scanner(co):
            if what == b'store':
                name, = args
                m.globalnames[name] = 1
            elif what in (b'import', b'absolute_import'):
                fromlist, name = args
                have_star = 0
                if fromlist is not None:
                    if b'*' in fromlist:
                        have_star = 1
                    fromlist = [f for f in fromlist if f != b'*']
                if what == b'absolute_import':
                    level = 0
                else:
                    level = -1
                self._safe_import_hook(name, m, fromlist, level=level)
                if have_star:
                    mm = None
                    if m.__path__:
                        mm = self.modules.get(m.__name__ + b'.' + name)
                    if mm is None:
                        mm = self.modules.get(name)
                    if mm is not None:
                        m.globalnames.update(mm.globalnames)
                        m.starimports.update(mm.starimports)
                        if mm.__code__ is None:
                            m.starimports[name] = 1
                    else:
                        m.starimports[name] = 1
            elif what == b'relative_import':
                level, fromlist, name = args
                if name:
                    self._safe_import_hook(name, m, fromlist, level=level)
                else:
                    parent = self.determine_parent(m, level=level)
                    self._safe_import_hook(parent.__name__, None, fromlist, level=0)
            else:
                raise RuntimeError(what)

        for c in co.co_consts:
            if isinstance(c, type(co)):
                self.scan_code(c, m)

        return

    def load_package(self, fqname, pathname):
        self.msgin(2, b'load_package', fqname, pathname)
        newname = replacePackageMap.get(fqname)
        if newname:
            fqname = newname
        m = self.add_module(fqname)
        m.__file__ = pathname
        m.__path__ = [pathname]
        m.__path__ = m.__path__ + packagePathMap.get(fqname, [])
        fp, buf, stuff = self.find_module(b'__init__', m.__path__)
        self.load_module(fqname, fp, buf, stuff)
        self.msgout(2, b'load_package ->', m)
        if fp:
            fp.close()
        return m

    def add_module(self, fqname):
        if fqname in self.modules:
            return self.modules[fqname]
        self.modules[fqname] = m = Module(fqname)
        return m

    def find_module(self, name, path, parent=None):
        if parent is not None:
            fullname = parent.__name__ + b'.' + name
        else:
            fullname = name
        if fullname in self.excludes:
            self.msgout(3, b'find_module -> Excluded', fullname)
            raise ImportError, name
        if path is None:
            if name in sys.builtin_module_names:
                return (None, None, (b'', b'', imp.C_BUILTIN))
            path = self.path
        return imp.find_module(name, path)

    def report(self):
        print
        print b'  %-25s %s' % (b'Name', b'File')
        print b'  %-25s %s' % (b'----', b'----')
        keys = self.modules.keys()
        keys.sort()
        for key in keys:
            m = self.modules[key]
            if m.__path__:
                print b'P',
            else:
                print b'm',
            print b'%-25s' % key, m.__file__ or b''

        missing, maybe = self.any_missing_maybe()
        if missing:
            print
            print b'Missing modules:'
            for name in missing:
                mods = self.badmodules[name].keys()
                mods.sort()
                print b'?', name, b'imported from', (b', ').join(mods)

        if maybe:
            print
            print b'Submodules that appear to be missing, but could also be',
            print b'global names in the parent package:'
            for name in maybe:
                mods = self.badmodules[name].keys()
                mods.sort()
                print b'?', name, b'imported from', (b', ').join(mods)

        return

    def any_missing(self):
        missing, maybe = self.any_missing_maybe()
        return missing + maybe

    def any_missing_maybe(self):
        missing = []
        maybe = []
        for name in self.badmodules:
            if name in self.excludes:
                continue
            i = name.rfind(b'.')
            if i < 0:
                missing.append(name)
                continue
            subname = name[i + 1:]
            pkgname = name[:i]
            pkg = self.modules.get(pkgname)
            if pkg is not None:
                if pkgname in self.badmodules[name]:
                    missing.append(name)
                elif subname in pkg.globalnames:
                    pass
                elif pkg.starimports:
                    maybe.append(name)
                else:
                    missing.append(name)
            else:
                missing.append(name)

        missing.sort()
        maybe.sort()
        return (missing, maybe)

    def replace_paths_in_code(self, co):
        new_filename = original_filename = os.path.normpath(co.co_filename)
        for f, r in self.replace_paths:
            if original_filename.startswith(f):
                new_filename = r + original_filename[len(f):]
                break

        if self.debug and original_filename not in self.processed_paths:
            if new_filename != original_filename:
                self.msgout(2, b'co_filename %r changed to %r' % (
                 original_filename, new_filename))
            else:
                self.msgout(2, b'co_filename %r remains unchanged' % (
                 original_filename,))
            self.processed_paths.append(original_filename)
        consts = list(co.co_consts)
        for i in range(len(consts)):
            if isinstance(consts[i], type(co)):
                consts[i] = self.replace_paths_in_code(consts[i])

        return types.CodeType(co.co_argcount, co.co_nlocals, co.co_stacksize, co.co_flags, co.co_code, tuple(consts), co.co_names, co.co_varnames, new_filename, co.co_name, co.co_firstlineno, co.co_lnotab, co.co_freevars, co.co_cellvars)


def test():
    import getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'dmp:qx:')
    except getopt.error as msg:
        print msg
        return

    debug = 1
    domods = 0
    addpath = []
    exclude = []
    for o, a in opts:
        if o == b'-d':
            debug = debug + 1
        if o == b'-m':
            domods = 1
        if o == b'-p':
            addpath = addpath + a.split(os.pathsep)
        if o == b'-q':
            debug = 0
        if o == b'-x':
            exclude.append(a)

    if not args:
        script = b'hello.py'
    else:
        script = args[0]
    path = sys.path[:]
    path[0] = os.path.dirname(script)
    path = addpath + path
    if debug > 1:
        print b'path:'
        for item in path:
            print b'   ', repr(item)

    mf = ModuleFinder(path, debug, exclude)
    for arg in args[1:]:
        if arg == b'-m':
            domods = 1
            continue
        if domods:
            if arg[-2:] == b'.*':
                mf.import_hook(arg[:-2], None, [b'*'])
            else:
                mf.import_hook(arg)
        else:
            mf.load_file(arg)

    mf.run_script(script)
    mf.report()
    return mf


if __name__ == b'__main__':
    try:
        mf = test()
    except KeyboardInterrupt:
        print b'\n[interrupt]'
