__revision__ = b'$Id$'
import sys, os, string, re
from distutils.errors import DistutilsPlatformError
from distutils.dep_util import newer
from distutils.spawn import spawn
from distutils import log
from distutils.errors import DistutilsByteCompileError

def get_platform():
    if os.name == b'nt':
        prefix = b' bit ('
        i = string.find(sys.version, prefix)
        if i == -1:
            return sys.platform
        j = string.find(sys.version, b')', i)
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
    osname = string.lower(osname)
    osname = string.replace(osname, b'/', b'')
    machine = string.replace(machine, b' ', b'_')
    machine = string.replace(machine, b'/', b'-')
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
        import _osx_support, distutils.sysconfig
        osname, release, machine = _osx_support.get_platform_osx(distutils.sysconfig.get_config_vars(), osname, release, machine)
    return b'%s-%s-%s' % (osname, release, machine)


def convert_path(pathname):
    if os.sep == b'/':
        return pathname
    if not pathname:
        return pathname
    if pathname[0] == b'/':
        raise ValueError, b"path '%s' cannot be absolute" % pathname
    if pathname[-1] == b'/':
        raise ValueError, b"path '%s' cannot end with '/'" % pathname
    paths = string.split(pathname, b'/')
    while b'.' in paths:
        paths.remove(b'.')

    if not paths:
        return os.curdir
    return os.path.join(*paths)


def change_root(new_root, pathname):
    if os.name == b'posix':
        if not os.path.isabs(pathname):
            return os.path.join(new_root, pathname)
        else:
            return os.path.join(new_root, pathname[1:])

    elif os.name == b'nt':
        drive, path = os.path.splitdrive(pathname)
        if path[0] == b'\\':
            path = path[1:]
        return os.path.join(new_root, path)
    if os.name == b'os2':
        drive, path = os.path.splitdrive(pathname)
        if path[0] == os.sep:
            path = path[1:]
        return os.path.join(new_root, path)
    raise DistutilsPlatformError, b"nothing known about platform '%s'" % os.name
    return


_environ_checked = 0

def check_environ():
    global _environ_checked
    if _environ_checked:
        return
    if os.name == b'posix' and b'HOME' not in os.environ:
        try:
            import pwd
            os.environ[b'HOME'] = pwd.getpwuid(os.getuid())[5]
        except (ImportError, KeyError):
            pass

    if b'PLAT' not in os.environ:
        os.environ[b'PLAT'] = get_platform()
    _environ_checked = 1
    return


def subst_vars(s, local_vars):
    check_environ()

    def _subst(match, local_vars=local_vars):
        var_name = match.group(1)
        if var_name in local_vars:
            return str(local_vars[var_name])
        else:
            return os.environ[var_name]

        return

    try:
        return re.sub(b'\\$([a-zA-Z_][a-zA-Z_0-9]*)', _subst, s)
    except KeyError as var:
        raise ValueError, b"invalid variable '$%s'" % var

    return


def grok_environment_error(exc, prefix=b'error: '):
    return prefix + str(exc)


_wordchars_re = _squote_re = _dquote_re = None

def _init_regex():
    global _dquote_re
    global _squote_re
    global _wordchars_re
    _wordchars_re = re.compile(b'[^\\\\\\\'\\"%s ]*' % string.whitespace)
    _squote_re = re.compile(b"'(?:[^'\\\\]|\\\\.)*'")
    _dquote_re = re.compile(b'"(?:[^"\\\\]|\\\\.)*"')
    return


def split_quoted(s):
    if _wordchars_re is None:
        _init_regex()
    s = string.strip(s)
    words = []
    pos = 0
    while s:
        m = _wordchars_re.match(s, pos)
        end = m.end()
        if end == len(s):
            words.append(s[:end])
            break
        if s[end] in string.whitespace:
            words.append(s[:end])
            s = string.lstrip(s[end:])
            pos = 0
        elif s[end] == b'\\':
            s = s[:end] + s[end + 1:]
            pos = end + 1
        else:
            if s[end] == b"'":
                m = _squote_re.match(s, end)
            elif s[end] == b'"':
                m = _dquote_re.match(s, end)
            else:
                raise RuntimeError, b"this can't happen (bad char '%c')" % s[end]
            if m is None:
                raise ValueError, b'bad string (mismatched %s quotes?)' % s[end]
            beg, end = m.span()
            s = s[:beg] + s[beg + 1:end - 1] + s[end:]
            pos = m.end() - 2
        if pos >= len(s):
            words.append(s)
            break

    return words


def execute(func, args, msg=None, verbose=0, dry_run=0):
    if msg is None:
        msg = b'%s%r' % (func.__name__, args)
        if msg[-2:] == b',)':
            msg = msg[0:-2] + b')'
    log.info(msg)
    if not dry_run:
        func(*args)
    return


def strtobool(val):
    val = string.lower(val)
    if val in (b'y', b'yes', b't', b'true', b'on', b'1'):
        return 1
    if val in (b'n', b'no', b'f', b'false', b'off', b'0'):
        return 0
    raise ValueError, b'invalid truth value %r' % (val,)
    return


def byte_compile(py_files, optimize=0, force=0, prefix=None, base_dir=None, verbose=1, dry_run=0, direct=None):
    if sys.dont_write_bytecode:
        raise DistutilsByteCompileError(b'byte-compiling is disabled.')
    if direct is None:
        direct = __debug__ and optimize == 0
    if not direct:
        try:
            from tempfile import mkstemp
            script_fd, script_name = mkstemp(b'.py')
        except ImportError:
            from tempfile import mktemp
            script_fd, script_name = None, mktemp(b'.py')

        log.info(b"writing byte-compilation script '%s'", script_name)
        if not dry_run:
            if script_fd is not None:
                script = os.fdopen(script_fd, b'w')
            else:
                script = open(script_name, b'w')
            script.write(b'from distutils.util import byte_compile\nfiles = [\n')
            script.write(string.join(map(repr, py_files), b',\n') + b']\n')
            script.write(b'\nbyte_compile(files, optimize=%r, force=%r,\n             prefix=%r, base_dir=%r,\n             verbose=%r, dry_run=0,\n             direct=1)\n' % (optimize, force, prefix, base_dir, verbose))
            script.close()
        cmd = [sys.executable, script_name]
        if optimize == 1:
            cmd.insert(1, b'-O')
        elif optimize == 2:
            cmd.insert(1, b'-OO')
        spawn(cmd, dry_run=dry_run)
        execute(os.remove, (script_name,), b'removing %s' % script_name, dry_run=dry_run)
    else:
        from py_compile import compile
        for file in py_files:
            if file[-3:] != b'.py':
                continue
            cfile = file + (__debug__ and b'c' or b'o')
            dfile = file
            if prefix:
                if file[:len(prefix)] != prefix:
                    raise ValueError, b"invalid prefix: filename %r doesn't start with %r" % (
                     file, prefix)
                dfile = dfile[len(prefix):]
            if base_dir:
                dfile = os.path.join(base_dir, dfile)
            cfile_base = os.path.basename(cfile)
            if direct:
                if force or newer(file, cfile):
                    log.info(b'byte-compiling %s to %s', file, cfile_base)
                    if not dry_run:
                        compile(file, cfile, dfile)
                else:
                    log.debug(b'skipping byte-compilation of %s to %s', file, cfile_base)

    return


def rfc822_escape(header):
    lines = string.split(header, b'\n')
    header = string.join(lines, b'\n' + b'        ')
    return header
