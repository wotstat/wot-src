__revision__ = b'$Id$'
import os, re, string, sys
from distutils.errors import DistutilsPlatformError
PREFIX = os.path.normpath(sys.prefix)
EXEC_PREFIX = os.path.normpath(sys.exec_prefix)
if sys.executable:
    project_base = os.path.dirname(os.path.abspath(sys.executable))
else:
    project_base = os.getcwd()
if os.name == b'nt' and b'pcbuild' in project_base[-8:].lower():
    project_base = os.path.abspath(os.path.join(project_base, os.path.pardir))
if os.name == b'nt' and b'\\pc\\v' in project_base[-10:].lower():
    project_base = os.path.abspath(os.path.join(project_base, os.path.pardir, os.path.pardir))
if os.name == b'nt' and b'\\pcbuild\\amd64' in project_base[-14:].lower():
    project_base = os.path.abspath(os.path.join(project_base, os.path.pardir, os.path.pardir))
if b'_PYTHON_PROJECT_BASE' in os.environ:
    project_base = os.path.normpath(os.environ[b'_PYTHON_PROJECT_BASE'])

def _python_build():
    for fn in (b'Setup.dist', b'Setup.local'):
        if os.path.isfile(os.path.join(project_base, b'Modules', fn)):
            return True

    return False


python_build = _python_build()

def get_python_version():
    return sys.version[:3]


def get_python_inc(plat_specific=0, prefix=None):
    if prefix is None:
        prefix = plat_specific and EXEC_PREFIX or PREFIX
    if os.name == b'posix':
        if python_build:
            if sys.executable:
                buildir = os.path.dirname(sys.executable)
            else:
                buildir = os.getcwd()
            if plat_specific:
                inc_dir = buildir
            else:
                srcdir = os.path.abspath(os.path.join(buildir, get_config_var(b'srcdir')))
                inc_dir = os.path.join(srcdir, b'Include')
            return inc_dir
        return os.path.join(prefix, b'include', b'python' + get_python_version())
    else:
        if os.name == b'nt':
            return os.path.join(prefix, b'include')
        if os.name == b'os2':
            return os.path.join(prefix, b'Include')
        raise DistutilsPlatformError(b"I don't know where Python installs its C header files on platform '%s'" % os.name)
        return


def get_python_lib(plat_specific=0, standard_lib=0, prefix=None):
    if prefix is None:
        prefix = plat_specific and EXEC_PREFIX or PREFIX
    if os.name == b'posix':
        libpython = os.path.join(prefix, b'lib', b'python' + get_python_version())
        if standard_lib:
            return libpython
        return os.path.join(libpython, b'site-packages')
    elif os.name == b'nt':
        if standard_lib:
            return os.path.join(prefix, b'Lib')
        else:
            if get_python_version() < b'2.2':
                return prefix
            return os.path.join(prefix, b'Lib', b'site-packages')

    elif os.name == b'os2':
        if standard_lib:
            return os.path.join(prefix, b'Lib')
        else:
            return os.path.join(prefix, b'Lib', b'site-packages')

    else:
        raise DistutilsPlatformError(b"I don't know where Python installs its library on platform '%s'" % os.name)
    return


def customize_compiler(compiler):
    global _config_vars
    if compiler.compiler_type == b'unix':
        if sys.platform == b'darwin':
            if not get_config_var(b'CUSTOMIZED_OSX_COMPILER'):
                import _osx_support
                _osx_support.customize_compiler(_config_vars)
                _config_vars[b'CUSTOMIZED_OSX_COMPILER'] = b'True'
        cc, cxx, cflags, ccshared, ldshared, so_ext, ar, ar_flags = get_config_vars(b'CC', b'CXX', b'CFLAGS', b'CCSHARED', b'LDSHARED', b'SO', b'AR', b'ARFLAGS')
        if b'CC' in os.environ:
            newcc = os.environ[b'CC']
            if sys.platform == b'darwin' and b'LDSHARED' not in os.environ and ldshared.startswith(cc):
                ldshared = newcc + ldshared[len(cc):]
            cc = newcc
        if b'CXX' in os.environ:
            cxx = os.environ[b'CXX']
        if b'LDSHARED' in os.environ:
            ldshared = os.environ[b'LDSHARED']
        if b'CPP' in os.environ:
            cpp = os.environ[b'CPP']
        else:
            cpp = cc + b' -E'
        if b'LDFLAGS' in os.environ:
            ldshared = ldshared + b' ' + os.environ[b'LDFLAGS']
        if b'CFLAGS' in os.environ:
            cflags = cflags + b' ' + os.environ[b'CFLAGS']
            ldshared = ldshared + b' ' + os.environ[b'CFLAGS']
        if b'CPPFLAGS' in os.environ:
            cpp = cpp + b' ' + os.environ[b'CPPFLAGS']
            cflags = cflags + b' ' + os.environ[b'CPPFLAGS']
            ldshared = ldshared + b' ' + os.environ[b'CPPFLAGS']
        if b'AR' in os.environ:
            ar = os.environ[b'AR']
        if b'ARFLAGS' in os.environ:
            archiver = ar + b' ' + os.environ[b'ARFLAGS']
        else:
            archiver = ar + b' ' + ar_flags
        cc_cmd = cc + b' ' + cflags
        compiler.set_executables(preprocessor=cpp, compiler=cc_cmd, compiler_so=cc_cmd + b' ' + ccshared, compiler_cxx=cxx, linker_so=ldshared, linker_exe=cc, archiver=archiver)
        compiler.shared_lib_extension = so_ext
    return


def get_config_h_filename():
    if python_build:
        if os.name == b'nt':
            inc_dir = os.path.join(project_base, b'PC')
        else:
            inc_dir = project_base
    else:
        inc_dir = get_python_inc(plat_specific=1)
    if get_python_version() < b'2.2':
        config_h = b'config.h'
    else:
        config_h = b'pyconfig.h'
    return os.path.join(inc_dir, config_h)


def get_makefile_filename():
    if python_build:
        return os.path.join(project_base, b'Makefile')
    lib_dir = get_python_lib(plat_specific=1, standard_lib=1)
    return os.path.join(lib_dir, b'config', b'Makefile')


def parse_config_h(fp, g=None):
    if g is None:
        g = {}
    define_rx = re.compile(b'#define ([A-Z][A-Za-z0-9_]+) (.*)\n')
    undef_rx = re.compile(b'/[*] #undef ([A-Z][A-Za-z0-9_]+) [*]/\n')
    while 1:
        line = fp.readline()
        if not line:
            break
        m = define_rx.match(line)
        if m:
            n, v = m.group(1, 2)
            try:
                v = int(v)
            except ValueError:
                pass

            g[n] = v
        else:
            m = undef_rx.match(line)
            if m:
                g[m.group(1)] = 0

    return g


_variable_rx = re.compile(b'([a-zA-Z][a-zA-Z0-9_]+)\\s*=\\s*(.*)')
_findvar1_rx = re.compile(b'\\$\\(([A-Za-z][A-Za-z0-9_]*)\\)')
_findvar2_rx = re.compile(b'\\${([A-Za-z][A-Za-z0-9_]*)}')

def parse_makefile(fn, g=None):
    from distutils.text_file import TextFile
    fp = TextFile(fn, strip_comments=1, skip_blanks=1, join_lines=1)
    if g is None:
        g = {}
    done = {}
    notdone = {}
    while 1:
        line = fp.readline()
        if line is None:
            break
        m = _variable_rx.match(line)
        if m:
            n, v = m.group(1, 2)
            v = v.strip()
            tmpv = v.replace(b'$$', b'')
            if b'$' in tmpv:
                notdone[n] = v
            else:
                try:
                    v = int(v)
                except ValueError:
                    done[n] = v.replace(b'$$', b'$')
                else:
                    done[n] = v

    while notdone:
        for name in notdone.keys():
            value = notdone[name]
            m = _findvar1_rx.search(value) or _findvar2_rx.search(value)
            if m:
                n = m.group(1)
                found = True
                if n in done:
                    item = str(done[n])
                elif n in notdone:
                    found = False
                elif n in os.environ:
                    item = os.environ[n]
                else:
                    done[n] = item = b''
                if found:
                    after = value[m.end():]
                    value = value[:m.start()] + item + after
                    if b'$' in after:
                        notdone[name] = value
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            done[name] = value.strip()
                        else:
                            done[name] = value

                        del notdone[name]
            else:
                del notdone[name]

    fp.close()
    for k, v in done.items():
        if isinstance(v, str):
            done[k] = v.strip()

    g.update(done)
    return g


def expand_makefile_vars(s, vars):
    while 1:
        m = _findvar1_rx.search(s) or _findvar2_rx.search(s)
        if m:
            beg, end = m.span()
            s = s[0:beg] + vars.get(m.group(1)) + s[end:]
        else:
            break

    return s


_config_vars = None

def _init_posix():
    global _config_vars
    from _sysconfigdata import build_time_vars
    _config_vars = {}
    _config_vars.update(build_time_vars)
    return


def _init_nt():
    global _config_vars
    g = {}
    g[b'LIBDEST'] = get_python_lib(plat_specific=0, standard_lib=1)
    g[b'BINLIBDEST'] = get_python_lib(plat_specific=1, standard_lib=1)
    g[b'INCLUDEPY'] = get_python_inc(plat_specific=0)
    g[b'SO'] = b'.pyd'
    g[b'EXE'] = b'.exe'
    g[b'VERSION'] = get_python_version().replace(b'.', b'')
    g[b'BINDIR'] = os.path.dirname(os.path.abspath(sys.executable))
    _config_vars = g
    return


def _init_os2():
    global _config_vars
    g = {}
    g[b'LIBDEST'] = get_python_lib(plat_specific=0, standard_lib=1)
    g[b'BINLIBDEST'] = get_python_lib(plat_specific=1, standard_lib=1)
    g[b'INCLUDEPY'] = get_python_inc(plat_specific=0)
    g[b'SO'] = b'.pyd'
    g[b'EXE'] = b'.exe'
    _config_vars = g
    return


def get_config_vars(*args):
    global _config_vars
    if _config_vars is None:
        func = globals().get(b'_init_' + os.name)
        if func:
            func()
        else:
            _config_vars = {}
        _config_vars[b'prefix'] = PREFIX
        _config_vars[b'exec_prefix'] = EXEC_PREFIX
        if sys.platform == b'darwin':
            import _osx_support
            _osx_support.customize_config_vars(_config_vars)
    if args:
        vals = []
        for name in args:
            vals.append(_config_vars.get(name))

        return vals
    return _config_vars
    return


def get_config_var(name):
    return get_config_vars().get(name)
