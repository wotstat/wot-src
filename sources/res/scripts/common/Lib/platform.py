__copyright__ = b'\n    Copyright (c) 1999-2000, Marc-Andre Lemburg; mailto:mal@lemburg.com\n    Copyright (c) 2000-2010, eGenix.com Software GmbH; mailto:info@egenix.com\n\n    Permission to use, copy, modify, and distribute this software and its\n    documentation for any purpose and without fee or royalty is hereby granted,\n    provided that the above copyright notice appear in all copies and that\n    both that copyright notice and this permission notice appear in\n    supporting documentation or portions thereof, including modifications,\n    that you make.\n\n    EGENIX.COM SOFTWARE GMBH DISCLAIMS ALL WARRANTIES WITH REGARD TO\n    THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND\n    FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,\n    INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING\n    FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,\n    NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION\n    WITH THE USE OR PERFORMANCE OF THIS SOFTWARE !\n\n'
__version__ = b'1.0.7'
import sys, string, os, re
try:
    DEV_NULL = os.devnull
except AttributeError:
    if sys.platform in (b'dos', b'win32', b'win16', b'os2'):
        DEV_NULL = b'NUL'
    else:
        DEV_NULL = b'/dev/null'

_libc_search = re.compile(b'(__libc_init)|(GLIBC_([0-9.]+))|(libc(_\\w+)?\\.so(?:\\.(\\d[0-9.]*))?)')

def libc_ver(executable=sys.executable, lib=b'', version=b'', chunksize=2048):
    if hasattr(os.path, b'realpath'):
        executable = os.path.realpath(executable)
    f = open(executable, b'rb')
    binary = f.read(chunksize)
    pos = 0
    while 1:
        m = _libc_search.search(binary, pos)
        if not m:
            binary = f.read(chunksize)
            if not binary:
                break
            pos = 0
            continue
        libcinit, glibc, glibcversion, so, threads, soversion = m.groups()
        if libcinit and not lib:
            lib = b'libc'
        elif glibc:
            if lib != b'glibc':
                lib = b'glibc'
                version = glibcversion
            elif glibcversion > version:
                version = glibcversion
        elif so:
            if lib != b'glibc':
                lib = b'libc'
                if soversion and soversion > version:
                    version = soversion
                if threads and version[-len(threads):] != threads:
                    version = version + threads
        pos = m.end()

    f.close()
    return (lib, version)


def _dist_try_harder(distname, version, id):
    if os.path.exists(b'/var/adm/inst-log/info'):
        info = open(b'/var/adm/inst-log/info').readlines()
        distname = b'SuSE'
        for line in info:
            tv = string.split(line)
            if len(tv) == 2:
                tag, value = tv
            else:
                continue
            if tag == b'MIN_DIST_VERSION':
                version = string.strip(value)
            elif tag == b'DIST_IDENT':
                values = string.split(value, b'-')
                id = values[2]

        return (
         distname, version, id)
    if os.path.exists(b'/etc/.installed'):
        info = open(b'/etc/.installed').readlines()
        for line in info:
            pkg = string.split(line, b'-')
            if len(pkg) >= 2 and pkg[0] == b'OpenLinux':
                return (
                 b'OpenLinux', pkg[1], id)

    if os.path.isdir(b'/usr/lib/setup'):
        verfiles = os.listdir(b'/usr/lib/setup')
        for n in range(len(verfiles) - 1, -1, -1):
            if verfiles[n][:14] != b'slack-version-':
                del verfiles[n]

        if verfiles:
            verfiles.sort()
            distname = b'slackware'
            version = verfiles[-1][14:]
            return (
             distname, version, id)
    return (
     distname, version, id)


_release_filename = re.compile(b'(\\w+)[-_](release|version)')
_lsb_release_version = re.compile(b'(.+) release ([\\d.]+)[^(]*(?:\\((.+)\\))?')
_release_version = re.compile(b'([^0-9]+)(?: release )?([\\d.]+)[^(]*(?:\\((.+)\\))?')
_supported_dists = (b'SuSE', b'debian', b'fedora', b'redhat', b'centos', b'mandrake', b'mandriva', b'rocks', b'slackware', b'yellowdog', b'gentoo', b'UnitedLinux', b'turbolinux')

def _parse_release_file(firstline):
    version = b''
    id = b''
    m = _lsb_release_version.match(firstline)
    if m is not None:
        return tuple(m.groups())
    else:
        m = _release_version.match(firstline)
        if m is not None:
            return tuple(m.groups())
        l = string.split(string.strip(firstline))
        if l:
            version = l[0]
            if len(l) > 1:
                id = l[1]
        return (
         b'', version, id)


def linux_distribution(distname=b'', version=b'', id=b'', supported_dists=_supported_dists, full_distribution_name=1):
    try:
        etc = os.listdir(b'/etc')
    except os.error:
        return (
         distname, version, id)

    etc.sort()
    for file in etc:
        m = _release_filename.match(file)
        if m is not None:
            _distname, dummy = m.groups()
            if _distname in supported_dists:
                distname = _distname
                break
    else:
        return _dist_try_harder(distname, version, id)

    f = open(b'/etc/' + file, b'r')
    firstline = f.readline()
    f.close()
    _distname, _version, _id = _parse_release_file(firstline)
    if _distname and full_distribution_name:
        distname = _distname
    if _version:
        version = _version
    if _id:
        id = _id
    return (
     distname, version, id)


def dist(distname=b'', version=b'', id=b'', supported_dists=_supported_dists):
    return linux_distribution(distname, version, id, supported_dists=supported_dists, full_distribution_name=0)


class _popen:
    tmpfile = b''
    pipe = None
    bufsize = None
    mode = b'r'

    def __init__(self, cmd, mode=b'r', bufsize=None):
        if mode != b'r':
            raise ValueError, b'popen()-emulation only supports read mode'
        import tempfile
        self.tmpfile = tmpfile = tempfile.mktemp()
        os.system(cmd + b' > %s' % tmpfile)
        self.pipe = open(tmpfile, b'rb')
        self.bufsize = bufsize
        self.mode = mode
        return

    def read(self):
        return self.pipe.read()

    def readlines(self):
        if self.bufsize is not None:
            return self.pipe.readlines()
        else:
            return

    def close(self, remove=os.unlink, error=os.error):
        if self.pipe:
            rc = self.pipe.close()
        else:
            rc = 255
        if self.tmpfile:
            try:
                remove(self.tmpfile)
            except error:
                pass

        return rc

    __del__ = close


def popen(cmd, mode=b'r', bufsize=None):
    popen = None
    if os.environ.get(b'OS', b'') == b'Windows_NT':
        try:
            import win32pipe
        except ImportError:
            pass
        else:
            popen = win32pipe.popen

    if popen is None:
        if hasattr(os, b'popen'):
            popen = os.popen
            if sys.platform == b'win32':
                try:
                    popen(b'')
                except os.error:
                    popen = _popen

        else:
            popen = _popen
    if bufsize is None:
        return popen(cmd, mode)
    else:
        return popen(cmd, mode, bufsize)
        return


def _norm_version(version, build=b''):
    l = string.split(version, b'.')
    if build:
        l.append(build)
    try:
        ints = map(int, l)
    except ValueError:
        strings = l
    else:
        strings = map(str, ints)

    version = string.join(strings[:3], b'.')
    return version


_ver_output = re.compile(b'(?:([\\w ]+) ([\\w.]+) .*\\[.* ([\\d.]+)\\])')

def _syscmd_ver(system=b'', release=b'', version=b'', supported_platforms=(b'win32', b'win16', b'dos', b'os2')):
    if sys.platform not in supported_platforms:
        return (system, release, version)
    else:
        for cmd in (b'ver', b'command /c ver', b'cmd /c ver'):
            try:
                pipe = popen(cmd)
                info = pipe.read()
                if pipe.close():
                    raise os.error, b'command failed'
            except os.error as why:
                continue
            except IOError as why:
                continue
            else:
                break

        else:
            return (
             system, release, version)

        info = string.strip(info)
        m = _ver_output.match(info)
        if m is not None:
            system, release, version = m.groups()
            if release[-1] == b'.':
                release = release[:-1]
            if version[-1] == b'.':
                version = version[:-1]
            version = _norm_version(version)
        return (
         system, release, version)


def _win32_getvalue(key, name, default=b''):
    try:
        from win32api import RegQueryValueEx
    except ImportError:
        import _winreg
        RegQueryValueEx = _winreg.QueryValueEx

    try:
        return RegQueryValueEx(key, name)
    except:
        return default

    return


def win32_ver(release=b'', version=b'', csd=b'', ptype=b''):
    try:
        import win32api
        from win32api import RegQueryValueEx, RegOpenKeyEx, RegCloseKey, GetVersionEx
        from win32con import HKEY_LOCAL_MACHINE, VER_PLATFORM_WIN32_NT, VER_PLATFORM_WIN32_WINDOWS, VER_NT_WORKSTATION
    except ImportError:
        try:
            sys.getwindowsversion
        except AttributeError:
            return (
             release, version, csd, ptype)

        import _winreg
        GetVersionEx = sys.getwindowsversion
        RegQueryValueEx = _winreg.QueryValueEx
        RegOpenKeyEx = _winreg.OpenKeyEx
        RegCloseKey = _winreg.CloseKey
        HKEY_LOCAL_MACHINE = _winreg.HKEY_LOCAL_MACHINE
        VER_PLATFORM_WIN32_WINDOWS = 1
        VER_PLATFORM_WIN32_NT = 2
        VER_NT_WORKSTATION = 1
        VER_NT_SERVER = 3
        REG_SZ = 1

    winver = GetVersionEx()
    maj, min, buildno, plat, csd = winver
    version = b'%i.%i.%i' % (maj, min, buildno & 65535)
    if hasattr(winver, b'service_pack'):
        if winver.service_pack != b'':
            csd = b'SP%s' % winver.service_pack_major
    elif csd[:13] == b'Service Pack ':
        csd = b'SP' + csd[13:]
    if plat == VER_PLATFORM_WIN32_WINDOWS:
        regkey = b'SOFTWARE\\Microsoft\\Windows\\CurrentVersion'
        if maj == 4:
            if min == 0:
                release = b'95'
            elif min == 10:
                release = b'98'
            elif min == 90:
                release = b'Me'
            else:
                release = b'postMe'
        elif maj == 5:
            release = b'2000'
    elif plat == VER_PLATFORM_WIN32_NT:
        regkey = b'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'
        if maj <= 4:
            release = b'NT'
        elif maj == 5:
            if min == 0:
                release = b'2000'
            elif min == 1:
                release = b'XP'
            elif min == 2:
                release = b'2003Server'
            else:
                release = b'post2003'
        elif maj == 6:
            if hasattr(winver, b'product_type'):
                product_type = winver.product_type
            else:
                product_type = VER_NT_WORKSTATION
                try:
                    key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, regkey)
                    name, type = RegQueryValueEx(key, b'ProductName')
                    if type == REG_SZ and name.find(b'Server') != -1:
                        product_type = VER_NT_SERVER
                except WindowsError:
                    pass

            if min == 0:
                if product_type == VER_NT_WORKSTATION:
                    release = b'Vista'
                else:
                    release = b'2008Server'
            elif min == 1:
                if product_type == VER_NT_WORKSTATION:
                    release = b'7'
                else:
                    release = b'2008ServerR2'
            elif min == 2:
                if product_type == VER_NT_WORKSTATION:
                    release = b'8'
                else:
                    release = b'2012Server'
            else:
                release = b'post2012Server'
    elif not release:
        release = b'%i.%i' % (maj, min)
    return (
     release, version, csd, ptype)
    try:
        keyCurVer = RegOpenKeyEx(HKEY_LOCAL_MACHINE, regkey)
        RegQueryValueEx(keyCurVer, b'SystemRoot')
    except:
        return (
         release, version, csd, ptype)

    build = _win32_getvalue(keyCurVer, b'CurrentBuildNumber', (b'', 1))[0]
    ptype = _win32_getvalue(keyCurVer, b'CurrentType', (
     ptype, 1))[0]
    version = _norm_version(version, build)
    RegCloseKey(keyCurVer)
    return (release, version, csd, ptype)


def _mac_ver_lookup(selectors, default=None):
    from gestalt import gestalt
    import MacOS
    l = []
    append = l.append
    for selector in selectors:
        try:
            append(gestalt(selector))
        except (RuntimeError, MacOS.Error):
            append(default)

    return l


def _bcd2str(bcd):
    return hex(bcd)[2:]


def _mac_ver_gestalt():
    try:
        import gestalt, MacOS
    except ImportError:
        return

    sysv, sysa = _mac_ver_lookup((b'sysv', b'sysa'))
    if sysv:
        major = (sysv & 65280) >> 8
        minor = (sysv & 240) >> 4
        patch = sysv & 15
        if (
         major, minor) >= (10, 4):
            major, minor, patch = _mac_ver_lookup((b'sys1', b'sys2', b'sys3'))
            release = b'%i.%i.%i' % (major, minor, patch)
        else:
            release = b'%s.%i.%i' % (_bcd2str(major), minor, patch)
    if sysa:
        machine = {1: b'68k', 2: b'PowerPC', 10: b'i386'}.get(sysa, b'')
    versioninfo = (b'', b'', b'')
    return (release, versioninfo, machine)


def _mac_ver_xml():
    fn = b'/System/Library/CoreServices/SystemVersion.plist'
    if not os.path.exists(fn):
        return
    else:
        try:
            import plistlib
        except ImportError:
            return

        pl = plistlib.readPlist(fn)
        release = pl[b'ProductVersion']
        versioninfo = (b'', b'', b'')
        machine = os.uname()[4]
        if machine in (b'ppc', b'Power Macintosh'):
            machine = b'PowerPC'
        return (release, versioninfo, machine)


def mac_ver(release=b'', versioninfo=(b'', b'', b''), machine=b''):
    info = _mac_ver_xml()
    if info is not None:
        return info
    else:
        info = _mac_ver_gestalt()
        if info is not None:
            return info
        return (
         release, versioninfo, machine)


def _java_getprop(name, default):
    from java.lang import System
    try:
        value = System.getProperty(name)
        if value is None:
            return default
        return value
    except AttributeError:
        return default

    return


def java_ver(release=b'', vendor=b'', vminfo=(b'', b'', b''), osinfo=(b'', b'', b'')):
    try:
        import java.lang
    except ImportError:
        return (
         release, vendor, vminfo, osinfo)

    vendor = _java_getprop(b'java.vendor', vendor)
    release = _java_getprop(b'java.version', release)
    vm_name, vm_release, vm_vendor = vminfo
    vm_name = _java_getprop(b'java.vm.name', vm_name)
    vm_vendor = _java_getprop(b'java.vm.vendor', vm_vendor)
    vm_release = _java_getprop(b'java.vm.version', vm_release)
    vminfo = (vm_name, vm_release, vm_vendor)
    os_name, os_version, os_arch = osinfo
    os_arch = _java_getprop(b'java.os.arch', os_arch)
    os_name = _java_getprop(b'java.os.name', os_name)
    os_version = _java_getprop(b'java.os.version', os_version)
    osinfo = (os_name, os_version, os_arch)
    return (
     release, vendor, vminfo, osinfo)


def system_alias(system, release, version):
    if system == b'Rhapsody':
        return (
         b'MacOS X Server', system + release, version)
    if system == b'SunOS':
        if release < b'5':
            return (
             system, release, version)
        l = string.split(release, b'.')
        if l:
            try:
                major = int(l[0])
            except ValueError:
                pass
            else:
                major = major - 3
                l[0] = str(major)
                release = string.join(l, b'.')

        if release < b'6':
            system = b'Solaris'
        else:
            system = b'Solaris'
    elif system == b'IRIX64':
        system = b'IRIX'
        if version:
            version = version + b' (64bit)'
        else:
            version = b'64bit'
    elif system in (b'win32', b'win16'):
        system = b'Windows'
    return (system, release, version)


def _platform(*args):
    platform = string.join(map(string.strip, filter(len, args)), b'-')
    replace = string.replace
    platform = replace(platform, b' ', b'_')
    platform = replace(platform, b'/', b'-')
    platform = replace(platform, b'\\', b'-')
    platform = replace(platform, b':', b'-')
    platform = replace(platform, b';', b'-')
    platform = replace(platform, b'"', b'-')
    platform = replace(platform, b'(', b'-')
    platform = replace(platform, b')', b'-')
    platform = replace(platform, b'unknown', b'')
    while 1:
        cleaned = replace(platform, b'--', b'-')
        if cleaned == platform:
            break
        platform = cleaned

    while platform[-1] == b'-':
        platform = platform[:-1]

    return platform


def _node(default=b''):
    try:
        import socket
    except ImportError:
        return default

    try:
        return socket.gethostname()
    except socket.error:
        return default

    return


if not hasattr(os.path, b'abspath'):

    def _abspath(path, isabs=os.path.isabs, join=os.path.join, getcwd=os.getcwd, normpath=os.path.normpath):
        if not isabs(path):
            path = join(getcwd(), path)
        return normpath(path)


else:
    _abspath = os.path.abspath

def _follow_symlinks(filepath):
    filepath = _abspath(filepath)
    while os.path.islink(filepath):
        filepath = os.path.normpath(os.path.join(os.path.dirname(filepath), os.readlink(filepath)))

    return filepath


def _syscmd_uname(option, default=b''):
    if sys.platform in (b'dos', b'win32', b'win16', b'os2'):
        return default
    else:
        try:
            f = os.popen(b'uname %s 2> %s' % (option, DEV_NULL))
        except (AttributeError, os.error):
            return default

        output = string.strip(f.read())
        rc = f.close()
        if not output or rc:
            return default
        return output

    return


def _syscmd_file(target, default=b''):
    import subprocess
    if sys.platform in (b'dos', b'win32', b'win16', b'os2'):
        return default
    else:
        target = _follow_symlinks(target)
        try:
            proc = subprocess.Popen([b'file', target], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except (AttributeError, os.error):
            return default

        output = proc.communicate()[0]
        rc = proc.wait()
        if not output or rc:
            return default
        return output

    return


_default_architecture = {b'win32': (b'', b'WindowsPE'), 
   b'win16': (b'', b'Windows'), 
   b'dos': (b'', b'MSDOS')}
_architecture_split = re.compile(b'[\\s,]').split

def architecture(executable=sys.executable, bits=b'', linkage=b''):
    if not bits:
        import struct
        try:
            size = struct.calcsize(b'P')
        except struct.error:
            size = struct.calcsize(b'l')

        bits = str(size * 8) + b'bit'
    if executable:
        output = _syscmd_file(executable, b'')
    else:
        output = b''
    if not output and executable == sys.executable:
        if sys.platform in _default_architecture:
            b, l = _default_architecture[sys.platform]
            if b:
                bits = b
            if l:
                linkage = l
        return (
         bits, linkage)
    fileout = _architecture_split(output)[1:]
    if b'executable' not in fileout:
        return (
         bits, linkage)
    if b'32-bit' in fileout:
        bits = b'32bit'
    elif b'N32' in fileout:
        bits = b'n32bit'
    elif b'64-bit' in fileout:
        bits = b'64bit'
    if b'ELF' in fileout:
        linkage = b'ELF'
    elif b'PE' in fileout:
        if b'Windows' in fileout:
            linkage = b'WindowsPE'
        else:
            linkage = b'PE'
    elif b'COFF' in fileout:
        linkage = b'COFF'
    elif b'MS-DOS' in fileout:
        linkage = b'MSDOS'
    return (
     bits, linkage)


_uname_cache = None

def uname():
    global _uname_cache
    no_os_uname = 0
    if _uname_cache is not None:
        return _uname_cache
    else:
        processor = b''
        try:
            system, node, release, version, machine = os.uname()
        except AttributeError:
            no_os_uname = 1

        if no_os_uname or not filter(None, (system, node, release, version, machine)):
            if no_os_uname:
                system = sys.platform
                release = b''
                version = b''
                node = _node()
                machine = b''
            use_syscmd_ver = 1
            if system == b'win32':
                release, version, csd, ptype = win32_ver()
                if release and version:
                    use_syscmd_ver = 0
                if not machine:
                    if b'PROCESSOR_ARCHITEW6432' in os.environ:
                        machine = os.environ.get(b'PROCESSOR_ARCHITEW6432', b'')
                    else:
                        machine = os.environ.get(b'PROCESSOR_ARCHITECTURE', b'')
                if not processor:
                    processor = os.environ.get(b'PROCESSOR_IDENTIFIER', machine)
            if use_syscmd_ver:
                system, release, version = _syscmd_ver(system)
                if system == b'Microsoft Windows':
                    system = b'Windows'
                elif system == b'Microsoft' and release == b'Windows':
                    system = b'Windows'
                    if b'6.0' == version[:3]:
                        release = b'Vista'
                    else:
                        release = b''
            if system in (b'win32', b'win16'):
                if not version:
                    if system == b'win32':
                        version = b'32bit'
                    else:
                        version = b'16bit'
                system = b'Windows'
            elif system[:4] == b'java':
                release, vendor, vminfo, osinfo = java_ver()
                system = b'Java'
                version = string.join(vminfo, b', ')
                if not version:
                    version = vendor
        if system == b'OpenVMS':
            if not release or release == b'0':
                release = version
                version = b''
            try:
                import vms_lib
            except ImportError:
                pass
            else:
                csid, cpu_number = vms_lib.getsyi(b'SYI$_CPU', 0)
                if cpu_number >= 128:
                    processor = b'Alpha'
                else:
                    processor = b'VAX'

        if not processor:
            processor = _syscmd_uname(b'-p', b'')
        if system == b'unknown':
            system = b''
        if node == b'unknown':
            node = b''
        if release == b'unknown':
            release = b''
        if version == b'unknown':
            version = b''
        if machine == b'unknown':
            machine = b''
        if processor == b'unknown':
            processor = b''
        if system == b'Microsoft' and release == b'Windows':
            system = b'Windows'
            release = b'Vista'
        _uname_cache = (system, node, release, version, machine, processor)
        return _uname_cache


def system():
    return uname()[0]


def node():
    return uname()[1]


def release():
    return uname()[2]


def version():
    return uname()[3]


def machine():
    return uname()[4]


def processor():
    return uname()[5]


_sys_version_parser = re.compile(b'([\\w.+]+)\\s*\\(#?([^,]+),\\s*([\\w ]+),\\s*([\\w :]+)\\)\\s*\\[([^\\]]+)\\]?')
_ironpython_sys_version_parser = re.compile(b'IronPython\\s*([\\d\\.]+)(?: \\(([\\d\\.]+)\\))? on (.NET [\\d\\.]+)')
_ironpython26_sys_version_parser = re.compile(b'([\\d.]+)\\s*\\(IronPython\\s*[\\d.]+\\s*\\(([\\d.]+)\\) on ([\\w.]+ [\\d.]+(?: \\(\\d+-bit\\))?)\\)')
_pypy_sys_version_parser = re.compile(b'([\\w.+]+)\\s*\\(#?([^,]+),\\s*([\\w ]+),\\s*([\\w :]+)\\)\\s*\\[PyPy [^\\]]+\\]?')
_sys_version_cache = {}

def _sys_version(sys_version=None):
    if sys_version is None:
        sys_version = sys.version
    result = _sys_version_cache.get(sys_version, None)
    if result is not None:
        return result
    else:
        if b'IronPython' in sys_version:
            name = b'IronPython'
            if sys_version.startswith(b'IronPython'):
                match = _ironpython_sys_version_parser.match(sys_version)
            else:
                match = _ironpython26_sys_version_parser.match(sys_version)
            if match is None:
                raise ValueError(b'failed to parse IronPython sys.version: %s' % repr(sys_version))
            version, alt_version, compiler = match.groups()
            buildno = b''
            builddate = b''
        elif sys.platform.startswith(b'java'):
            name = b'Jython'
            match = _sys_version_parser.match(sys_version)
            if match is None:
                raise ValueError(b'failed to parse Jython sys.version: %s' % repr(sys_version))
            version, buildno, builddate, buildtime, _ = match.groups()
            compiler = sys.platform
        elif b'PyPy' in sys_version:
            name = b'PyPy'
            match = _pypy_sys_version_parser.match(sys_version)
            if match is None:
                raise ValueError(b'failed to parse PyPy sys.version: %s' % repr(sys_version))
            version, buildno, builddate, buildtime = match.groups()
            compiler = b''
        else:
            match = _sys_version_parser.match(sys_version)
            if match is None:
                raise ValueError(b'failed to parse CPython sys.version: %s' % repr(sys_version))
            version, buildno, builddate, buildtime, compiler = match.groups()
            name = b'CPython'
            builddate = builddate + b' ' + buildtime
        if hasattr(sys, b'subversion'):
            _, branch, revision = sys.subversion
        else:
            branch = b''
            revision = b''
        l = string.split(version, b'.')
        if len(l) == 2:
            l.append(b'0')
            version = string.join(l, b'.')
        result = (
         name, version, branch, revision, buildno, builddate, compiler)
        _sys_version_cache[sys_version] = result
        return result


def python_implementation():
    return _sys_version()[0]


def python_version():
    return _sys_version()[1]


def python_version_tuple():
    return tuple(string.split(_sys_version()[1], b'.'))


def python_branch():
    return _sys_version()[2]


def python_revision():
    return _sys_version()[3]


def python_build():
    return _sys_version()[4:6]


def python_compiler():
    return _sys_version()[6]


_platform_cache = {}

def platform(aliased=0, terse=0):
    result = _platform_cache.get((aliased, terse), None)
    if result is not None:
        return result
    else:
        system, node, release, version, machine, processor = uname()
        if machine == processor:
            processor = b''
        if aliased:
            system, release, version = system_alias(system, release, version)
        if system == b'Windows':
            rel, vers, csd, ptype = win32_ver(version)
            if terse:
                platform = _platform(system, release)
            else:
                platform = _platform(system, release, version, csd)
        elif system in (b'Linux',):
            distname, distversion, distid = dist(b'')
            if distname and not terse:
                platform = _platform(system, release, machine, processor, b'with', distname, distversion, distid)
            else:
                libcname, libcversion = libc_ver(sys.executable)
                platform = _platform(system, release, machine, processor, b'with', libcname + libcversion)
        elif system == b'Java':
            r, v, vminfo, (os_name, os_version, os_arch) = java_ver()
            if terse or not os_name:
                platform = _platform(system, release, version)
            else:
                platform = _platform(system, release, version, b'on', os_name, os_version, os_arch)
        elif system == b'MacOS':
            if terse:
                platform = _platform(system, release)
            else:
                platform = _platform(system, release, machine)
        elif terse:
            platform = _platform(system, release)
        else:
            bits, linkage = architecture(sys.executable)
            platform = _platform(system, release, machine, processor, bits, linkage)
        _platform_cache[(aliased, terse)] = platform
        return platform


if __name__ == b'__main__':
    terse = b'terse' in sys.argv or b'--terse' in sys.argv
    aliased = b'nonaliased' not in sys.argv and b'--nonaliased' not in sys.argv
    print platform(aliased, terse)
    sys.exit(0)
