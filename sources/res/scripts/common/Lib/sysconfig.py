import sys, os
from os.path import pardir, realpath
_INSTALL_SCHEMES = {b'posix_prefix': {b'stdlib': b'{base}/lib/python{py_version_short}', 
                     b'platstdlib': b'{platbase}/lib/python{py_version_short}', 
                     b'purelib': b'{base}/lib/python{py_version_short}/site-packages', 
                     b'platlib': b'{platbase}/lib/python{py_version_short}/site-packages', 
                     b'include': b'{base}/include/python{py_version_short}', 
                     b'platinclude': b'{platbase}/include/python{py_version_short}', 
                     b'scripts': b'{base}/bin', 
                     b'data': b'{base}'}, 
   b'posix_home': {b'stdlib': b'{base}/lib/python', 
                   b'platstdlib': b'{base}/lib/python', 
                   b'purelib': b'{base}/lib/python', 
                   b'platlib': b'{base}/lib/python', 
                   b'include': b'{base}/include/python', 
                   b'platinclude': b'{base}/include/python', 
                   b'scripts': b'{base}/bin', 
                   b'data': b'{base}'}, 
   b'nt': {b'stdlib': b'{base}/Lib', 
           b'platstdlib': b'{base}/Lib', 
           b'purelib': b'{base}/Lib/site-packages', 
           b'platlib': b'{base}/Lib/site-packages', 
           b'include': b'{base}/Include', 
           b'platinclude': b'{base}/Include', 
           b'scripts': b'{base}/Scripts', 
           b'data': b'{base}'}, 
   b'os2': {b'stdlib': b'{base}/Lib', 
            b'platstdlib': b'{base}/Lib', 
            b'purelib': b'{base}/Lib/site-packages', 
            b'platlib': b'{base}/Lib/site-packages', 
            b'include': b'{base}/Include', 
            b'platinclude': b'{base}/Include', 
            b'scripts': b'{base}/Scripts', 
            b'data': b'{base}'}, 
   b'os2_home': {b'stdlib': b'{userbase}/lib/python{py_version_short}', 
                 b'platstdlib': b'{userbase}/lib/python{py_version_short}', 
                 b'purelib': b'{userbase}/lib/python{py_version_short}/site-packages', 
                 b'platlib': b'{userbase}/lib/python{py_version_short}/site-packages', 
                 b'include': b'{userbase}/include/python{py_version_short}', 
                 b'scripts': b'{userbase}/bin', 
                 b'data': b'{userbase}'}, 
   b'nt_user': {b'stdlib': b'{userbase}/Python{py_version_nodot}', 
                b'platstdlib': b'{userbase}/Python{py_version_nodot}', 
                b'purelib': b'{userbase}/Python{py_version_nodot}/site-packages', 
                b'platlib': b'{userbase}/Python{py_version_nodot}/site-packages', 
                b'include': b'{userbase}/Python{py_version_nodot}/Include', 
                b'scripts': b'{userbase}/Scripts', 
                b'data': b'{userbase}'}, 
   b'posix_user': {b'stdlib': b'{userbase}/lib/python{py_version_short}', 
                   b'platstdlib': b'{userbase}/lib/python{py_version_short}', 
                   b'purelib': b'{userbase}/lib/python{py_version_short}/site-packages', 
                   b'platlib': b'{userbase}/lib/python{py_version_short}/site-packages', 
                   b'include': b'{userbase}/include/python{py_version_short}', 
                   b'scripts': b'{userbase}/bin', 
                   b'data': b'{userbase}'}, 
   b'osx_framework_user': {b'stdlib': b'{userbase}/lib/python', 
                           b'platstdlib': b'{userbase}/lib/python', 
                           b'purelib': b'{userbase}/lib/python/site-packages', 
                           b'platlib': b'{userbase}/lib/python/site-packages', 
                           b'include': b'{userbase}/include', 
                           b'scripts': b'{userbase}/bin', 
                           b'data': b'{userbase}'}}
_SCHEME_KEYS = (b'stdlib', b'platstdlib', b'purelib', b'platlib', b'include', b'scripts', b'data')
_PY_VERSION = sys.version.split()[0]
_PY_VERSION_SHORT = sys.version[:3]
_PY_VERSION_SHORT_NO_DOT = _PY_VERSION[0] + _PY_VERSION[2]
_PREFIX = os.path.normpath(sys.prefix)
_EXEC_PREFIX = os.path.normpath(sys.exec_prefix)
_CONFIG_VARS = None
_USER_BASE = None

def _safe_realpath(path):
    try:
        return realpath(path)
    except OSError:
        return path

    return


if sys.executable:
    _PROJECT_BASE = os.path.dirname(_safe_realpath(sys.executable))
else:
    _PROJECT_BASE = _safe_realpath(os.getcwd())
if os.name == b'nt' and b'pcbuild' in _PROJECT_BASE[-8:].lower():
    _PROJECT_BASE = _safe_realpath(os.path.join(_PROJECT_BASE, pardir))
if os.name == b'nt' and b'\\pc\\v' in _PROJECT_BASE[-10:].lower():
    _PROJECT_BASE = _safe_realpath(os.path.join(_PROJECT_BASE, pardir, pardir))
if os.name == b'nt' and os.path.basename(os.path.dirname(os.path.dirname(_PROJECT_BASE))).lower() == b'pc' and os.path.basename(os.path.dirname(_PROJECT_BASE)).lower() == b'vs9.0':
    _PROJECT_BASE = _safe_realpath(os.path.join(_PROJECT_BASE, pardir, pardir, pardir))
if os.name == b'nt' and b'\\pcbuild\\amd64' in _PROJECT_BASE[-14:].lower():
    _PROJECT_BASE = _safe_realpath(os.path.join(_PROJECT_BASE, pardir, pardir))
if b'_PYTHON_PROJECT_BASE' in os.environ:
    _PROJECT_BASE = os.path.normpath(os.path.abspath(b'.'))

def is_python_build():
    for fn in (b'Setup.dist', b'Setup.local'):
        if os.path.isfile(os.path.join(_PROJECT_BASE, b'Modules', fn)):
            return True

    return False


_PYTHON_BUILD = is_python_build()
if _PYTHON_BUILD:
    for scheme in (b'posix_prefix', b'posix_home'):
        _INSTALL_SCHEMES[scheme][b'include'] = b'{projectbase}/Include'
        _INSTALL_SCHEMES[scheme][b'platinclude'] = b'{srcdir}'

def _subst_vars(s, local_vars):
    try:
        return s.format(**local_vars)
    except KeyError:
        try:
            return s.format(**os.environ)
        except KeyError as var:
            raise AttributeError(b'{%s}' % var)

    return


def _extend_dict(target_dict, other_dict):
    target_keys = target_dict.keys()
    for key, value in other_dict.items():
        if key in target_keys:
            continue
        target_dict[key] = value

    return


def _expand_vars(scheme, vars):
    res = {}
    if vars is None:
        vars = {}
    _extend_dict(vars, get_config_vars())
    for key, value in _INSTALL_SCHEMES[scheme].items():
        if os.name in (b'posix', b'nt'):
            value = os.path.expanduser(value)
        res[key] = os.path.normpath(_subst_vars(value, vars))

    return res


def _get_default_scheme():
    if os.name == b'posix':
        return b'posix_prefix'
    return os.name


def _getuserbase():
    env_base = os.environ.get(b'PYTHONUSERBASE', None)

    def joinuser(*args):
        return os.path.expanduser(os.path.join(*args))

    if os.name == b'nt':
        base = os.environ.get(b'APPDATA') or b'~'
        if env_base:
            return env_base
        return joinuser(base, b'Python')
    else:
        if sys.platform == b'darwin':
            framework = get_config_var(b'PYTHONFRAMEWORK')
            if framework:
                if env_base:
                    return env_base
                return joinuser(b'~', b'Library', framework, b'%d.%d' % sys.version_info[:2])
        if env_base:
            return env_base
        return joinuser(b'~', b'.local')


def _parse_makefile(filename, vars=None):
    import re
    _variable_rx = re.compile(b'([a-zA-Z][a-zA-Z0-9_]+)\\s*=\\s*(.*)')
    _findvar1_rx = re.compile(b'\\$\\(([A-Za-z][A-Za-z0-9_]*)\\)')
    _findvar2_rx = re.compile(b'\\${([A-Za-z][A-Za-z0-9_]*)}')
    if vars is None:
        vars = {}
    done = {}
    notdone = {}
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith(b'#') or line.strip() == b'':
            continue
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

    for k, v in done.items():
        if isinstance(v, str):
            done[k] = v.strip()

    vars.update(done)
    return vars


def get_makefile_filename():
    if _PYTHON_BUILD:
        return os.path.join(_PROJECT_BASE, b'Makefile')
    return os.path.join(get_path(b'platstdlib'), b'config', b'Makefile')


_get_makefile_filename = get_makefile_filename

def _generate_posix_vars():
    import pprint
    vars = {}
    makefile = get_makefile_filename()
    try:
        _parse_makefile(makefile, vars)
    except IOError as e:
        msg = b'invalid Python installation: unable to open %s' % makefile
        if hasattr(e, b'strerror'):
            msg = msg + b' (%s)' % e.strerror
        raise IOError(msg)

    config_h = get_config_h_filename()
    try:
        with open(config_h) as f:
            parse_config_h(f, vars)
    except IOError as e:
        msg = b'invalid Python installation: unable to open %s' % config_h
        if hasattr(e, b'strerror'):
            msg = msg + b' (%s)' % e.strerror
        raise IOError(msg)

    if _PYTHON_BUILD:
        vars[b'LDSHARED'] = vars[b'BLDSHARED']
    name = b'_sysconfigdata'
    if b'darwin' in sys.platform:
        import imp
        module = imp.new_module(name)
        module.build_time_vars = vars
        sys.modules[name] = module
    pybuilddir = b'build/lib.%s-%s' % (get_platform(), sys.version[:3])
    if hasattr(sys, b'gettotalrefcount'):
        pybuilddir += b'-pydebug'
    try:
        os.makedirs(pybuilddir)
    except OSError:
        pass

    destfile = os.path.join(pybuilddir, name + b'.py')
    with open(destfile, b'wb') as f:
        f.write(b'# system configuration generated and used by the sysconfig module\n')
        f.write(b'build_time_vars = ')
        pprint.pprint(vars, stream=f)
    with open(b'pybuilddir.txt', b'w') as f:
        f.write(pybuilddir)
    return


def _init_posix(vars):
    from _sysconfigdata import build_time_vars
    vars.update(build_time_vars)
    return


def _init_non_posix(vars):
    vars[b'LIBDEST'] = get_path(b'stdlib')
    vars[b'BINLIBDEST'] = get_path(b'platstdlib')
    vars[b'INCLUDEPY'] = get_path(b'include')
    vars[b'SO'] = b'.pyd'
    vars[b'EXE'] = b'.exe'
    vars[b'VERSION'] = _PY_VERSION_SHORT_NO_DOT
    vars[b'BINDIR'] = os.path.dirname(_safe_realpath(sys.executable))
    return


def parse_config_h(fp, vars=None):
    import re
    if vars is None:
        vars = {}
    define_rx = re.compile(b'#define ([A-Z][A-Za-z0-9_]+) (.*)\n')
    undef_rx = re.compile(b'/[*] #undef ([A-Z][A-Za-z0-9_]+) [*]/\n')
    while True:
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

            vars[n] = v
        else:
            m = undef_rx.match(line)
            if m:
                vars[m.group(1)] = 0

    return vars


def get_config_h_filename():
    if _PYTHON_BUILD:
        if os.name == b'nt':
            inc_dir = os.path.join(_PROJECT_BASE, b'PC')
        else:
            inc_dir = _PROJECT_BASE
    else:
        inc_dir = get_path(b'platinclude')
    return os.path.join(inc_dir, b'pyconfig.h')


def get_scheme_names():
    schemes = _INSTALL_SCHEMES.keys()
    schemes.sort()
    return tuple(schemes)


def get_path_names():
    return _SCHEME_KEYS


def get_paths(scheme=_get_default_scheme(), vars=None, expand=True):
    if expand:
        return _expand_vars(scheme, vars)
    else:
        return _INSTALL_SCHEMES[scheme]

    return


def get_path(name, scheme=_get_default_scheme(), vars=None, expand=True):
    return get_paths(scheme, vars, expand)[name]


def get_config_vars(*args):
    global _CONFIG_VARS
    import re
    if _CONFIG_VARS is None:
        _CONFIG_VARS = {}
        _CONFIG_VARS[b'prefix'] = _PREFIX
        _CONFIG_VARS[b'exec_prefix'] = _EXEC_PREFIX
        _CONFIG_VARS[b'py_version'] = _PY_VERSION
        _CONFIG_VARS[b'py_version_short'] = _PY_VERSION_SHORT
        _CONFIG_VARS[b'py_version_nodot'] = _PY_VERSION[0] + _PY_VERSION[2]
        _CONFIG_VARS[b'base'] = _PREFIX
        _CONFIG_VARS[b'platbase'] = _EXEC_PREFIX
        _CONFIG_VARS[b'projectbase'] = _PROJECT_BASE
        if os.name in (b'nt', b'os2'):
            _init_non_posix(_CONFIG_VARS)
        if os.name == b'posix':
            _init_posix(_CONFIG_VARS)
        _CONFIG_VARS[b'userbase'] = _getuserbase()
        if b'srcdir' not in _CONFIG_VARS:
            _CONFIG_VARS[b'srcdir'] = _PROJECT_BASE
        if _PYTHON_BUILD and os.name == b'posix':
            base = _PROJECT_BASE
            try:
                cwd = os.getcwd()
            except OSError:
                cwd = None

            if not os.path.isabs(_CONFIG_VARS[b'srcdir']) and base != cwd:
                srcdir = os.path.join(base, _CONFIG_VARS[b'srcdir'])
                _CONFIG_VARS[b'srcdir'] = os.path.normpath(srcdir)
        if sys.platform == b'darwin':
            import _osx_support
            _osx_support.customize_config_vars(_CONFIG_VARS)
    if args:
        vals = []
        for name in args:
            vals.append(_CONFIG_VARS.get(name))

        return vals
    return _CONFIG_VARS
    return


def get_config_var(name):
    return get_config_vars().get(name)


def get_platform():
    import re
    if os.name == b'nt':
        prefix = b' bit ('
        i = sys.version.find(prefix)
        if i == -1:
            return sys.platform
        j = sys.version.find(b')', i)
        look = sys.version[i + len(prefix):j].lower()
        if look == b'amd64':
            return b'win-amd64'
        if look == b'itanium':
            return b'win-ia64'
        return sys.platform
    if b'_PYTHON_HOST_PLATFORM' in os.environ:
        return os.environ[b'_PYTHON_HOST_PLATFORM']
    if os.name != b'posix' or not hasattr(os, b'uname'):
        return sys.platform
    osname, host, release, version, machine = os.uname()
    osname = osname.lower().replace(b'/', b'')
    machine = machine.replace(b' ', b'_')
    machine = machine.replace(b'/', b'-')
    if osname[:5] == b'linux':
        return b'%s-%s' % (osname, machine)
    if osname[:5] == b'sunos':
        if release[0] >= b'5':
            osname = b'solaris'
            release = b'%d.%s' % (int(release[0]) - 3, release[2:])
            bitness = {2147483647: b'32bit', 9223372036854775807L: b'64bit'}
            machine += b'.%s' % bitness[sys.maxint]
    elif osname[:4] == b'irix':
        return b'%s-%s' % (osname, release)
    if osname[:3] == b'aix':
        return b'%s-%s.%s' % (osname, version, release)
    if osname[:6] == b'cygwin':
        osname = b'cygwin'
        rel_re = re.compile(b'[\\d.]+')
        m = rel_re.match(release)
        if m:
            release = m.group()
    elif osname[:6] == b'darwin':
        import _osx_support
        osname, release, machine = _osx_support.get_platform_osx(get_config_vars(), osname, release, machine)
    return b'%s-%s-%s' % (osname, release, machine)


def get_python_version():
    return _PY_VERSION_SHORT


def _print_dict(title, data):
    for index, (key, value) in enumerate(sorted(data.items())):
        if index == 0:
            print b'%s: ' % title
        print b'\t%s = "%s"' % (key, value)

    return


def _main():
    if b'--generate-posix-vars' in sys.argv:
        _generate_posix_vars()
        return
    print b'Platform: "%s"' % get_platform()
    print b'Python version: "%s"' % get_python_version()
    print b'Current installation scheme: "%s"' % _get_default_scheme()
    print
    _print_dict(b'Paths', get_paths())
    print
    _print_dict(b'Variables', get_config_vars())
    return


if __name__ == b'__main__':
    _main()
