import os, subprocess, sys
if os.name == b'nt':

    def _get_build_version():
        prefix = b'MSC v.'
        i = sys.version.find(prefix)
        if i == -1:
            return 6
        else:
            i = i + len(prefix)
            s, rest = sys.version[i:].split(b' ', 1)
            majorVersion = int(s[:-2]) - 6
            minorVersion = int(s[2:3]) / 10.0
            if majorVersion == 6:
                minorVersion = 0
            if majorVersion >= 6:
                return majorVersion + minorVersion
            return


    def find_msvcrt():
        version = _get_build_version()
        if version is None:
            return
        else:
            if version <= 6:
                clibname = b'msvcrt'
            else:
                clibname = b'msvcr%d' % (version * 10)
            import imp
            if imp.get_suffixes()[0][0] == b'_d.pyd':
                clibname += b'd'
            return clibname + b'.dll'


    def find_library(name):
        if name in (b'c', b'm'):
            return find_msvcrt()
        else:
            for directory in os.environ[b'PATH'].split(os.pathsep):
                fname = os.path.join(directory, name)
                if os.path.isfile(fname):
                    return fname
                if fname.lower().endswith(b'.dll'):
                    continue
                fname = fname + b'.dll'
                if os.path.isfile(fname):
                    return fname

            return


if os.name == b'ce':

    def find_library(name):
        return name


if os.name == b'posix' and sys.platform == b'darwin':
    from ctypes.macholib.dyld import dyld_find as _dyld_find

    def find_library(name):
        possible = [
         b'lib%s.dylib' % name,
         b'%s.dylib' % name,
         b'%s.framework/%s' % (name, name)]
        for name in possible:
            try:
                return _dyld_find(name)
            except ValueError:
                continue

        return


elif os.name == b'posix':
    import re, tempfile, errno

    def _findLib_gcc(name):
        expr = b'[^\\(\\)\\s]*lib%s\\.[^\\(\\)\\s]*' % re.escape(name)
        cmd = b'if type gcc >/dev/null 2>&1; then CC=gcc; elif type cc >/dev/null 2>&1; then CC=cc;else exit; fi;LANG=C LC_ALL=C $CC -Wl,-t -o "$2" 2>&1 -l"$1"'
        temp = tempfile.NamedTemporaryFile()
        try:
            proc = subprocess.Popen((cmd, b'_findLib_gcc', name, temp.name), shell=True, stdout=subprocess.PIPE)
            trace, _ = proc.communicate()
        finally:
            try:
                temp.close()
            except OSError as e:
                if e.errno != errno.ENOENT:
                    raise

        res = re.search(expr, trace)
        if not res:
            return
        else:
            return res.group(0)


    if sys.platform == b'sunos5':

        def _get_soname(f):
            if not f:
                return
            else:
                null = open(os.devnull, b'wb')
                try:
                    with null:
                        proc = subprocess.Popen((b'/usr/ccs/bin/dump', b'-Lpv', f), stdout=subprocess.PIPE, stderr=null)
                except OSError:
                    return

                data, _ = proc.communicate()
                res = re.search(b'\\[.*\\]\\sSONAME\\s+([^\\s]+)', data)
                if not res:
                    return
                return res.group(1)


    else:

        def _get_soname(f):
            if not f:
                return None
            else:
                cmd = b'if ! type objdump >/dev/null 2>&1; then exit; fi;objdump -p -j .dynamic 2>/dev/null "$1"'
                proc = subprocess.Popen((cmd, b'_get_soname', f), shell=True, stdout=subprocess.PIPE)
                dump, _ = proc.communicate()
                res = re.search(b'\\sSONAME\\s+([^\\s]+)', dump)
                if not res:
                    return None
                return res.group(1)


    if sys.platform.startswith(b'freebsd') or sys.platform.startswith(b'openbsd') or sys.platform.startswith(b'dragonfly'):

        def _num_version(libname):
            parts = libname.split(b'.')
            nums = []
            try:
                while parts:
                    nums.insert(0, int(parts.pop()))

            except ValueError:
                pass

            return nums or [sys.maxint]


        def find_library(name):
            ename = re.escape(name)
            expr = b':-l%s\\.\\S+ => \\S*/(lib%s\\.\\S+)' % (ename, ename)
            null = open(os.devnull, b'wb')
            try:
                with null:
                    proc = subprocess.Popen((b'/sbin/ldconfig', b'-r'), stdout=subprocess.PIPE, stderr=null)
            except OSError:
                data = b''
            else:
                data, _ = proc.communicate()

            res = re.findall(expr, data)
            if not res:
                return _get_soname(_findLib_gcc(name))
            res.sort(key=_num_version)
            return res[-1]


    elif sys.platform == b'sunos5':

        def _findLib_crle(name, is64):
            if not os.path.exists(b'/usr/bin/crle'):
                return
            else:
                env = dict(os.environ)
                env[b'LC_ALL'] = b'C'
                if is64:
                    args = (b'/usr/bin/crle', b'-64')
                else:
                    args = (b'/usr/bin/crle',)
                paths = None
                null = open(os.devnull, b'wb')
                try:
                    with null:
                        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=null, env=env)
                except OSError:
                    return

                try:
                    for line in proc.stdout:
                        line = line.strip()
                        if line.startswith(b'Default Library Path (ELF):'):
                            paths = line.split()[4]

                finally:
                    proc.stdout.close()
                    proc.wait()

                if not paths:
                    return
                for dir in paths.split(b':'):
                    libfile = os.path.join(dir, b'lib%s.so' % name)
                    if os.path.exists(libfile):
                        return libfile

                return


        def find_library(name, is64=False):
            return _get_soname(_findLib_crle(name, is64) or _findLib_gcc(name))


    else:

        def _findSoname_ldconfig(name):
            import struct
            if struct.calcsize(b'l') == 4:
                machine = os.uname()[4] + b'-32'
            else:
                machine = os.uname()[4] + b'-64'
            mach_map = {b'x86_64-64': b'libc6,x86-64', b'ppc64-64': b'libc6,64bit', 
               b'sparc64-64': b'libc6,64bit', 
               b's390x-64': b'libc6,64bit', 
               b'ia64-64': b'libc6,IA-64'}
            abi_type = mach_map.get(machine, b'libc6')
            expr = b'\\s+(lib%s\\.[^\\s]+)\\s+\\(%s' % (re.escape(name), abi_type)
            env = dict(os.environ)
            env[b'LC_ALL'] = b'C'
            env[b'LANG'] = b'C'
            null = open(os.devnull, b'wb')
            try:
                with null:
                    p = subprocess.Popen([b'/sbin/ldconfig', b'-p'], stderr=null, stdout=subprocess.PIPE, env=env)
            except OSError:
                return

            data, _ = p.communicate()
            res = re.search(expr, data)
            if not res:
                return
            else:
                return res.group(1)


        def find_library(name):
            return _findSoname_ldconfig(name) or _get_soname(_findLib_gcc(name))


def test():
    from ctypes import cdll
    if os.name == b'nt':
        print cdll.msvcrt
        print cdll.load(b'msvcrt')
        print find_library(b'msvcrt')
    if os.name == b'posix':
        print find_library(b'm')
        print find_library(b'c')
        print find_library(b'bz2')
        if sys.platform == b'darwin':
            print cdll.LoadLibrary(b'libm.dylib')
            print cdll.LoadLibrary(b'libcrypto.dylib')
            print cdll.LoadLibrary(b'libSystem.dylib')
            print cdll.LoadLibrary(b'System.framework/System')
        else:
            print cdll.LoadLibrary(b'libm.so')
            print cdll.LoadLibrary(b'libcrypt.so')
            print find_library(b'crypt')
    return


if __name__ == b'__main__':
    test()
