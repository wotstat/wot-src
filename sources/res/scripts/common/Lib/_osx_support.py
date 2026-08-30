import os, re, sys
__all__ = [
 b'compiler_fixup',
 b'customize_config_vars',
 b'customize_compiler',
 b'get_platform_osx']
_UNIVERSAL_CONFIG_VARS = (b'CFLAGS', b'LDFLAGS', b'CPPFLAGS', b'BASECFLAGS', b'BLDSHARED', b'LDSHARED', b'CC', b'CXX', b'PY_CFLAGS', b'PY_LDFLAGS', b'PY_CPPFLAGS', b'PY_CORE_CFLAGS')
_COMPILER_CONFIG_VARS = (b'BLDSHARED', b'LDSHARED', b'CC', b'CXX')
_INITPRE = b'_OSX_SUPPORT_INITIAL_'

def _find_executable(executable, path=None):
    if path is None:
        path = os.environ[b'PATH']
    paths = path.split(os.pathsep)
    base, ext = os.path.splitext(executable)
    if (sys.platform == b'win32' or os.name == b'os2') and ext != b'.exe':
        executable = executable + b'.exe'
    if not os.path.isfile(executable):
        for p in paths:
            f = os.path.join(p, executable)
            if os.path.isfile(f):
                return f

        return
    return executable
    return


def _read_output(commandstring):
    import contextlib
    try:
        import tempfile
        fp = tempfile.NamedTemporaryFile()
    except ImportError:
        fp = open(b'/tmp/_osx_support.%s' % (
         os.getpid(),), b'w+b')

    with contextlib.closing(fp) as fp:
        cmd = b"%s 2>/dev/null >'%s'" % (commandstring, fp.name)
        if not os.system(cmd):
            return fp.read().strip()
        return
    return


def _find_build_tool(toolname):
    return _find_executable(toolname) or _read_output(b'/usr/bin/xcrun -find %s' % (toolname,)) or b''


_SYSTEM_VERSION = None

def _get_system_version():
    global _SYSTEM_VERSION
    if _SYSTEM_VERSION is None:
        _SYSTEM_VERSION = b''
        try:
            f = open(b'/System/Library/CoreServices/SystemVersion.plist')
        except IOError:
            pass
        else:
            try:
                m = re.search(b'<key>ProductUserVisibleVersion</key>\\s*<string>(.*?)</string>', f.read())
            finally:
                f.close()

            if m is not None:
                _SYSTEM_VERSION = (b'.').join(m.group(1).split(b'.')[:2])
    return _SYSTEM_VERSION


def _remove_original_values(_config_vars):
    for k in list(_config_vars):
        if k.startswith(_INITPRE):
            del _config_vars[k]

    return


def _save_modified_value(_config_vars, cv, newvalue):
    oldvalue = _config_vars.get(cv, b'')
    if oldvalue != newvalue and _INITPRE + cv not in _config_vars:
        _config_vars[_INITPRE + cv] = oldvalue
    _config_vars[cv] = newvalue
    return


def _supports_universal_builds():
    osx_version = _get_system_version()
    if osx_version:
        try:
            osx_version = tuple(int(i) for i in osx_version.split(b'.'))
        except ValueError:
            osx_version = b''

    if osx_version:
        return bool(osx_version >= (10, 4))
    return False


def _find_appropriate_compiler(_config_vars):
    if b'CC' in os.environ:
        return _config_vars
    cc = oldcc = _config_vars[b'CC'].split()[0]
    if not _find_executable(cc):
        cc = _find_build_tool(b'clang')
    elif os.path.basename(cc).startswith(b'gcc'):
        data = _read_output(b"'%s' --version" % (
         cc.replace(b"'", b'\'"\'"\''),))
        if data and b'llvm-gcc' in data:
            cc = _find_build_tool(b'clang')
    if not cc:
        raise SystemError(b'Cannot locate working compiler')
    if cc != oldcc:
        for cv in _COMPILER_CONFIG_VARS:
            if cv in _config_vars and cv not in os.environ:
                cv_split = _config_vars[cv].split()
                cv_split[0] = cc if cv != b'CXX' else cc + b'++'
                _save_modified_value(_config_vars, cv, (b' ').join(cv_split))

    return _config_vars


def _remove_universal_flags(_config_vars):
    for cv in _UNIVERSAL_CONFIG_VARS:
        if cv in _config_vars and cv not in os.environ:
            flags = _config_vars[cv]
            flags = re.sub(b'-arch\\s+\\w+\\s', b' ', flags)
            flags = re.sub(b'-isysroot [^ \t]*', b' ', flags)
            _save_modified_value(_config_vars, cv, flags)

    return _config_vars


def _remove_unsupported_archs(_config_vars):
    if b'CC' in os.environ:
        return _config_vars
    else:
        if re.search(b'-arch\\s+ppc', _config_vars[b'CFLAGS']) is not None:
            status = os.system(b"echo 'int main{};' | '%s' -c -arch ppc -x c -o /dev/null /dev/null 2>/dev/null" % (
             _config_vars[b'CC'].replace(b"'", b'\'"\'"\''),))
            if status:
                for cv in _UNIVERSAL_CONFIG_VARS:
                    if cv in _config_vars and cv not in os.environ:
                        flags = _config_vars[cv]
                        flags = re.sub(b'-arch\\s+ppc\\w*\\s', b' ', flags)
                        _save_modified_value(_config_vars, cv, flags)

        return _config_vars


def _override_all_archs(_config_vars):
    if b'ARCHFLAGS' in os.environ:
        arch = os.environ[b'ARCHFLAGS']
        for cv in _UNIVERSAL_CONFIG_VARS:
            if cv in _config_vars and b'-arch' in _config_vars[cv]:
                flags = _config_vars[cv]
                flags = re.sub(b'-arch\\s+\\w+\\s', b' ', flags)
                flags = flags + b' ' + arch
                _save_modified_value(_config_vars, cv, flags)

    return _config_vars


def _check_for_unavailable_sdk(_config_vars):
    cflags = _config_vars.get(b'CFLAGS', b'')
    m = re.search(b'-isysroot\\s+(\\S+)', cflags)
    if m is not None:
        sdk = m.group(1)
        if not os.path.exists(sdk):
            for cv in _UNIVERSAL_CONFIG_VARS:
                if cv in _config_vars and cv not in os.environ:
                    flags = _config_vars[cv]
                    flags = re.sub(b'-isysroot\\s+\\S+(?:\\s|$)', b' ', flags)
                    _save_modified_value(_config_vars, cv, flags)

    return _config_vars


def compiler_fixup(compiler_so, cc_args):
    stripArch = stripSysroot = False
    compiler_so = list(compiler_so)
    if not _supports_universal_builds():
        stripArch = stripSysroot = True
    else:
        stripArch = b'-arch' in cc_args
        stripSysroot = b'-isysroot' in cc_args
    if stripArch or b'ARCHFLAGS' in os.environ:
        while True:
            try:
                index = compiler_so.index(b'-arch')
                del compiler_so[index:index + 2]
            except ValueError:
                break

    if b'ARCHFLAGS' in os.environ and not stripArch:
        compiler_so = compiler_so + os.environ[b'ARCHFLAGS'].split()
    if stripSysroot:
        while True:
            try:
                index = compiler_so.index(b'-isysroot')
                del compiler_so[index:index + 2]
            except ValueError:
                break

    sysroot = None
    if b'-isysroot' in cc_args:
        idx = cc_args.index(b'-isysroot')
        sysroot = cc_args[idx + 1]
    elif b'-isysroot' in compiler_so:
        idx = compiler_so.index(b'-isysroot')
        sysroot = compiler_so[idx + 1]
    if sysroot and not os.path.isdir(sysroot):
        from distutils import log
        log.warn(b"Compiling with an SDK that doesn't seem to exist: %s", sysroot)
        log.warn(b'Please check your Xcode installation')
    return compiler_so


def customize_config_vars(_config_vars):
    if not _supports_universal_builds():
        _remove_universal_flags(_config_vars)
    _override_all_archs(_config_vars)
    _check_for_unavailable_sdk(_config_vars)
    return _config_vars


def customize_compiler(_config_vars):
    _find_appropriate_compiler(_config_vars)
    _remove_unsupported_archs(_config_vars)
    _override_all_archs(_config_vars)
    return _config_vars


def get_platform_osx(_config_vars, osname, release, machine):
    macver = _config_vars.get(b'MACOSX_DEPLOYMENT_TARGET', b'')
    macrelease = _get_system_version() or macver
    macver = macver or macrelease
    if macver:
        release = macver
        osname = b'macosx'
        cflags = _config_vars.get(_INITPRE + b'CFLAGS', _config_vars.get(b'CFLAGS', b''))
        if macrelease:
            try:
                macrelease = tuple(int(i) for i in macrelease.split(b'.')[0:2])
            except ValueError:
                macrelease = (10, 0)

        else:
            macrelease = (10, 0)
        if macrelease >= (10, 4) and b'-arch' in cflags.strip():
            machine = b'fat'
            archs = re.findall(b'-arch\\s+(\\S+)', cflags)
            archs = tuple(sorted(set(archs)))
            if len(archs) == 1:
                machine = archs[0]
            elif archs == (b'i386', b'ppc'):
                machine = b'fat'
            elif archs == (b'i386', b'x86_64'):
                machine = b'intel'
            elif archs == (b'i386', b'ppc', b'x86_64'):
                machine = b'fat3'
            if archs == (b'ppc64', b'x86_64'):
                machine = b'fat64'
            elif archs == (b'i386', b'ppc', b'ppc64', b'x86_64'):
                machine = b'universal'
            else:
                raise ValueError(b"Don't know machine value for archs=%r" % (archs,))
        elif machine == b'i386':
            if sys.maxint >= 4294967296L:
                machine = b'x86_64'
        elif machine in (b'PowerPC', b'Power_Macintosh'):
            if sys.maxint >= 4294967296L:
                machine = b'ppc64'
            else:
                machine = b'ppc'
    return (
     osname, release, machine)
