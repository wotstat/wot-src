__revision__ = b'$Id$'
import os, subprocess, sys, re
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CompileError, LibError, LinkError
from distutils.ccompiler import CCompiler, gen_lib_options
from distutils import log
from distutils.util import get_platform
import _winreg
RegOpenKeyEx = _winreg.OpenKeyEx
RegEnumKey = _winreg.EnumKey
RegEnumValue = _winreg.EnumValue
RegError = _winreg.error
HKEYS = (
 _winreg.HKEY_USERS,
 _winreg.HKEY_CURRENT_USER,
 _winreg.HKEY_LOCAL_MACHINE,
 _winreg.HKEY_CLASSES_ROOT)
NATIVE_WIN64 = sys.platform == b'win32' and sys.maxsize > 4294967296L
if NATIVE_WIN64:
    VS_BASE = b'Software\\Wow6432Node\\Microsoft\\VisualStudio\\%0.1f'
    VSEXPRESS_BASE = b'Software\\Wow6432Node\\Microsoft\\VCExpress\\%0.1f'
    WINSDK_BASE = b'Software\\Wow6432Node\\Microsoft\\Microsoft SDKs\\Windows'
    NET_BASE = b'Software\\Wow6432Node\\Microsoft\\.NETFramework'
else:
    VS_BASE = b'Software\\Microsoft\\VisualStudio\\%0.1f'
    VSEXPRESS_BASE = b'Software\\Microsoft\\VCExpress\\%0.1f'
    WINSDK_BASE = b'Software\\Microsoft\\Microsoft SDKs\\Windows'
    NET_BASE = b'Software\\Microsoft\\.NETFramework'
PLAT_TO_VCVARS = {b'win32': b'x86', 
   b'win-amd64': b'amd64', 
   b'win-ia64': b'ia64'}

class Reg:

    def get_value(cls, path, key):
        for base in HKEYS:
            d = cls.read_values(base, path)
            if d and key in d:
                return d[key]

        raise KeyError(key)
        return

    get_value = classmethod(get_value)

    def read_keys(cls, base, key):
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return

        L = []
        i = 0
        while True:
            try:
                k = RegEnumKey(handle, i)
            except RegError:
                break

            L.append(k)
            i += 1

        return L

    read_keys = classmethod(read_keys)

    def read_values(cls, base, key):
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return

        d = {}
        i = 0
        while True:
            try:
                name, value, type = RegEnumValue(handle, i)
            except RegError:
                break

            name = name.lower()
            d[cls.convert_mbcs(name)] = cls.convert_mbcs(value)
            i += 1

        return d

    read_values = classmethod(read_values)

    def convert_mbcs(s):
        dec = getattr(s, b'decode', None)
        if dec is not None:
            try:
                s = dec(b'mbcs')
            except UnicodeError:
                pass

        return s

    convert_mbcs = staticmethod(convert_mbcs)


class MacroExpander:

    def __init__(self, version):
        self.macros = {}
        self.vsbase = VS_BASE % version
        self.load_macros(version)
        return

    def set_macro(self, macro, path, key):
        self.macros[b'$(%s)' % macro] = Reg.get_value(path, key)
        return

    def load_macros(self, version):
        self.set_macro(b'VCInstallDir', self.vsbase + b'\\Setup\\VC', b'productdir')
        self.set_macro(b'VSInstallDir', self.vsbase + b'\\Setup\\VS', b'productdir')
        self.set_macro(b'FrameworkDir', NET_BASE, b'installroot')
        try:
            if version >= 8.0:
                self.set_macro(b'FrameworkSDKDir', NET_BASE, b'sdkinstallrootv2.0')
            else:
                raise KeyError(b'sdkinstallrootv2.0')
        except KeyError:
            raise DistutilsPlatformError(b'Python was built with Visual Studio 2008;\nextensions must be built with a compiler than can generate compatible binaries.\nVisual Studio 2008 was not found on this system. If you have Cygwin installed,\nyou can try compiling with MingW32, by passing "-c mingw32" to setup.py.')

        if version >= 9.0:
            self.set_macro(b'FrameworkVersion', self.vsbase, b'clr version')
            self.set_macro(b'WindowsSdkDir', WINSDK_BASE, b'currentinstallfolder')
        else:
            p = b'Software\\Microsoft\\NET Framework Setup\\Product'
            for base in HKEYS:
                try:
                    h = RegOpenKeyEx(base, p)
                except RegError:
                    continue

                key = RegEnumKey(h, 0)
                d = Reg.get_value(base, b'%s\\%s' % (p, key))
                self.macros[b'$(FrameworkVersion)'] = d[b'version']

        return

    def sub(self, s):
        for k, v in self.macros.items():
            s = s.replace(k, v)

        return s


def get_build_version():
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


def normalize_and_reduce_paths(paths):
    reduced_paths = []
    for p in paths:
        np = os.path.normpath(p)
        if np not in reduced_paths:
            reduced_paths.append(np)

    return reduced_paths


def removeDuplicates(variable):
    oldList = variable.split(os.pathsep)
    newList = []
    for i in oldList:
        if i not in newList:
            newList.append(i)

    newVariable = os.pathsep.join(newList)
    return newVariable


def find_vcvarsall(version):
    vsbase = VS_BASE % version
    try:
        productdir = Reg.get_value(b'%s\\Setup\\VC' % vsbase, b'productdir')
    except KeyError:
        productdir = None

    if productdir is None:
        vsbase = VSEXPRESS_BASE % version
        try:
            productdir = Reg.get_value(b'%s\\Setup\\VC' % vsbase, b'productdir')
        except KeyError:
            productdir = None
            log.debug(b'Unable to find productdir in registry')

    if not productdir or not os.path.isdir(productdir):
        toolskey = b'VS%0.f0COMNTOOLS' % version
        toolsdir = os.environ.get(toolskey, None)
        if toolsdir and os.path.isdir(toolsdir):
            productdir = os.path.join(toolsdir, os.pardir, os.pardir, b'VC')
            productdir = os.path.abspath(productdir)
            if not os.path.isdir(productdir):
                log.debug(b'%s is not a valid directory' % productdir)
                return
        else:
            log.debug(b'Env var %s is not set or invalid' % toolskey)
    if not productdir:
        log.debug(b'No productdir found')
        return
    else:
        vcvarsall = os.path.join(productdir, b'vcvarsall.bat')
        if os.path.isfile(vcvarsall):
            return vcvarsall
        log.debug(b'Unable to find vcvarsall.bat')
        return


def query_vcvarsall(version, arch=b'x86'):
    vcvarsall = find_vcvarsall(version)
    interesting = set((b'include', b'lib', b'libpath', b'path'))
    result = {}
    if vcvarsall is None:
        raise DistutilsPlatformError(b'Unable to find vcvarsall.bat')
    log.debug(b"Calling 'vcvarsall.bat %s' (version=%s)", arch, version)
    popen = subprocess.Popen(b'"%s" %s & set' % (vcvarsall, arch), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stdout, stderr = popen.communicate()
        if popen.wait() != 0:
            raise DistutilsPlatformError(stderr.decode(b'mbcs'))
        stdout = stdout.decode(b'mbcs')
        for line in stdout.split(b'\n'):
            line = Reg.convert_mbcs(line)
            if b'=' not in line:
                continue
            line = line.strip()
            key, value = line.split(b'=', 1)
            key = key.lower()
            if key in interesting:
                if value.endswith(os.pathsep):
                    value = value[:-1]
                result[key] = removeDuplicates(value)

    finally:
        popen.stdout.close()
        popen.stderr.close()

    if len(result) != len(interesting):
        raise ValueError(str(list(result.keys())))
    return result


VERSION = get_build_version()
if VERSION < 8.0:
    raise DistutilsPlatformError(b'VC %0.1f is not supported by this module' % VERSION)

class MSVCCompiler(CCompiler):
    compiler_type = b'msvc'
    executables = {}
    _c_extensions = [
     b'.c']
    _cpp_extensions = [b'.cc', b'.cpp', b'.cxx']
    _rc_extensions = [b'.rc']
    _mc_extensions = [b'.mc']
    src_extensions = _c_extensions + _cpp_extensions + _rc_extensions + _mc_extensions
    res_extension = b'.res'
    obj_extension = b'.obj'
    static_lib_extension = b'.lib'
    shared_lib_extension = b'.dll'
    static_lib_format = shared_lib_format = b'%s%s'
    exe_extension = b'.exe'

    def __init__(self, verbose=0, dry_run=0, force=0):
        CCompiler.__init__(self, verbose, dry_run, force)
        self.__version = VERSION
        self.__root = b'Software\\Microsoft\\VisualStudio'
        self.__paths = []
        self.plat_name = None
        self.__arch = None
        self.initialized = False
        return

    def initialize(self, plat_name=None):
        if plat_name is None:
            plat_name = get_platform()
        ok_plats = (b'win32', b'win-amd64', b'win-ia64')
        if plat_name not in ok_plats:
            raise DistutilsPlatformError(b'--plat-name must be one of %s' % (
             ok_plats,))
        if b'DISTUTILS_USE_SDK' in os.environ and b'MSSdk' in os.environ and self.find_exe(b'cl.exe'):
            self.cc = b'cl.exe'
            self.linker = b'link.exe'
            self.lib = b'lib.exe'
            self.rc = b'rc.exe'
            self.mc = b'mc.exe'
        else:
            if plat_name == get_platform() or plat_name == b'win32':
                plat_spec = PLAT_TO_VCVARS[plat_name]
            else:
                plat_spec = PLAT_TO_VCVARS[get_platform()] + b'_' + PLAT_TO_VCVARS[plat_name]
            vc_env = query_vcvarsall(VERSION, plat_spec)
            self.__paths = vc_env[b'path'].encode(b'mbcs').split(os.pathsep)
            os.environ[b'lib'] = vc_env[b'lib'].encode(b'mbcs')
            os.environ[b'include'] = vc_env[b'include'].encode(b'mbcs')
            if len(self.__paths) == 0:
                raise DistutilsPlatformError(b"Python was built with %s, and extensions need to be built with the same version of the compiler, but it isn't installed." % self.__product)
            self.cc = self.find_exe(b'cl.exe')
            self.linker = self.find_exe(b'link.exe')
            self.lib = self.find_exe(b'lib.exe')
            self.rc = self.find_exe(b'rc.exe')
            self.mc = self.find_exe(b'mc.exe')
        try:
            for p in os.environ[b'path'].split(b';'):
                self.__paths.append(p)

        except KeyError:
            pass

        self.__paths = normalize_and_reduce_paths(self.__paths)
        os.environ[b'path'] = (b';').join(self.__paths)
        self.preprocess_options = None
        if self.__arch == b'x86':
            self.compile_options = [
             21, 22, 23, 24, 
             25]
            self.compile_options_debug = [21, 26, 27, 24, 
             28, 29]
        else:
            self.compile_options = [
             21, 22, 23, 24, 30, 
             25]
            self.compile_options_debug = [21, 26, 27, 24, 30, 
             28, 29]
        self.ldflags_shared = [b'/DLL', b'/nologo', b'/INCREMENTAL:NO']
        if self.__version >= 7:
            self.ldflags_shared_debug = [b'/DLL', b'/nologo', b'/INCREMENTAL:no', b'/DEBUG']
        self.ldflags_static = [b'/nologo']
        self.initialized = True
        return

    def object_filenames(self, source_filenames, strip_dir=0, output_dir=b''):
        if output_dir is None:
            output_dir = b''
        obj_names = []
        for src_name in source_filenames:
            base, ext = os.path.splitext(src_name)
            base = os.path.splitdrive(base)[1]
            base = base[os.path.isabs(base):]
            if ext not in self.src_extensions:
                raise CompileError(b"Don't know how to compile %s" % src_name)
            if strip_dir:
                base = os.path.basename(base)
            if ext in self._rc_extensions:
                obj_names.append(os.path.join(output_dir, base + self.res_extension))
            elif ext in self._mc_extensions:
                obj_names.append(os.path.join(output_dir, base + self.res_extension))
            else:
                obj_names.append(os.path.join(output_dir, base + self.obj_extension))

        return obj_names

    def compile(self, sources, output_dir=None, macros=None, include_dirs=None, debug=0, extra_preargs=None, extra_postargs=None, depends=None):
        if not self.initialized:
            self.initialize()
        compile_info = self._setup_compile(output_dir, macros, include_dirs, sources, depends, extra_postargs)
        macros, objects, extra_postargs, pp_opts, build = compile_info
        compile_opts = extra_preargs or []
        compile_opts.append(b'/c')
        if debug:
            compile_opts.extend(self.compile_options_debug)
        else:
            compile_opts.extend(self.compile_options)
        for obj in objects:
            try:
                src, ext = build[obj]
            except KeyError:
                continue

            if debug:
                src = os.path.abspath(src)
            if ext in self._c_extensions:
                input_opt = b'/Tc' + src
            elif ext in self._cpp_extensions:
                input_opt = b'/Tp' + src
            elif ext in self._rc_extensions:
                input_opt = src
                output_opt = b'/fo' + obj
                try:
                    self.spawn([
                     self.rc] + pp_opts + [output_opt] + [input_opt])
                except DistutilsExecError as msg:
                    raise CompileError(msg)

                continue
            elif ext in self._mc_extensions:
                h_dir = os.path.dirname(src)
                rc_dir = os.path.dirname(obj)
                try:
                    self.spawn([
                     self.mc] + [b'-h', h_dir, b'-r', rc_dir] + [src])
                    base, _ = os.path.splitext(os.path.basename(src))
                    rc_file = os.path.join(rc_dir, base + b'.rc')
                    self.spawn([
                     self.rc] + [b'/fo' + obj] + [rc_file])
                except DistutilsExecError as msg:
                    raise CompileError(msg)

                continue
            else:
                raise CompileError(b"Don't know how to compile %s to %s" % (
                 src, obj))
            output_opt = b'/Fo' + obj
            try:
                self.spawn([
                 self.cc] + compile_opts + pp_opts + [input_opt, output_opt] + extra_postargs)
            except DistutilsExecError as msg:
                raise CompileError(msg)

        return objects

    def create_static_lib(self, objects, output_libname, output_dir=None, debug=0, target_lang=None):
        if not self.initialized:
            self.initialize()
        objects, output_dir = self._fix_object_args(objects, output_dir)
        output_filename = self.library_filename(output_libname, output_dir=output_dir)
        if self._need_link(objects, output_filename):
            lib_args = objects + [b'/OUT:' + output_filename]
            if debug:
                pass
            try:
                self.spawn([self.lib] + lib_args)
            except DistutilsExecError as msg:
                raise LibError(msg)

        else:
            log.debug(b'skipping %s (up-to-date)', output_filename)
        return

    def link(self, target_desc, objects, output_filename, output_dir=None, libraries=None, library_dirs=None, runtime_library_dirs=None, export_symbols=None, debug=0, extra_preargs=None, extra_postargs=None, build_temp=None, target_lang=None):
        if not self.initialized:
            self.initialize()
        objects, output_dir = self._fix_object_args(objects, output_dir)
        fixed_args = self._fix_lib_args(libraries, library_dirs, runtime_library_dirs)
        libraries, library_dirs, runtime_library_dirs = fixed_args
        if runtime_library_dirs:
            self.warn(b"I don't know what to do with 'runtime_library_dirs': " + str(runtime_library_dirs))
        lib_opts = gen_lib_options(self, library_dirs, runtime_library_dirs, libraries)
        if output_dir is not None:
            output_filename = os.path.join(output_dir, output_filename)
        if self._need_link(objects, output_filename):
            if target_desc == CCompiler.EXECUTABLE:
                if debug:
                    ldflags = self.ldflags_shared_debug[1:]
                else:
                    ldflags = self.ldflags_shared[1:]
            elif debug:
                ldflags = self.ldflags_shared_debug
            else:
                ldflags = self.ldflags_shared
            export_opts = []
            for sym in export_symbols or []:
                export_opts.append(b'/EXPORT:' + sym)

            ld_args = ldflags + lib_opts + export_opts + objects + [b'/OUT:' + output_filename]
            build_temp = os.path.dirname(objects[0])
            if export_symbols is not None:
                dll_name, dll_ext = os.path.splitext(os.path.basename(output_filename))
                implib_file = os.path.join(build_temp, self.library_filename(dll_name))
                ld_args.append(b'/IMPLIB:' + implib_file)
            self.manifest_setup_ldargs(output_filename, build_temp, ld_args)
            if extra_preargs:
                ld_args[:0] = extra_preargs
            if extra_postargs:
                ld_args.extend(extra_postargs)
            self.mkpath(os.path.dirname(output_filename))
            try:
                self.spawn([self.linker] + ld_args)
            except DistutilsExecError as msg:
                raise LinkError(msg)

            mfinfo = self.manifest_get_embed_info(target_desc, ld_args)
            if mfinfo is not None:
                mffilename, mfid = mfinfo
                out_arg = b'-outputresource:%s;%s' % (output_filename, mfid)
                try:
                    self.spawn([8, 9, 10, 
                     mffilename, 
                     out_arg])
                except DistutilsExecError as msg:
                    raise LinkError(msg)

        else:
            log.debug(b'skipping %s (up-to-date)', output_filename)
        return

    def manifest_setup_ldargs(self, output_filename, build_temp, ld_args):
        temp_manifest = os.path.join(build_temp, os.path.basename(output_filename) + b'.manifest')
        ld_args.append(b'/MANIFESTFILE:' + temp_manifest)
        return

    def manifest_get_embed_info(self, target_desc, ld_args):
        for arg in ld_args:
            if arg.startswith(b'/MANIFESTFILE:'):
                temp_manifest = arg.split(b':', 1)[1]
                break
        else:
            return

        if target_desc == CCompiler.EXECUTABLE:
            mfid = 1
        else:
            mfid = 2
            temp_manifest = self._remove_visual_c_ref(temp_manifest)
        if temp_manifest is None:
            return
        else:
            return (
             temp_manifest, mfid)

    def _remove_visual_c_ref(self, manifest_file):
        try:
            manifest_f = open(manifest_file)
            try:
                manifest_buf = manifest_f.read()
            finally:
                manifest_f.close()

            pattern = re.compile(b'<assemblyIdentity.*?name=("|\')Microsoft\\.VC\\d{2}\\.CRT("|\').*?(/>|</assemblyIdentity>)', re.DOTALL)
            manifest_buf = re.sub(pattern, b'', manifest_buf)
            pattern = b'<dependentAssembly>\\s*</dependentAssembly>'
            manifest_buf = re.sub(pattern, b'', manifest_buf)
            pattern = re.compile(b'<assemblyIdentity.*?name=(?:"|\')(.+?)(?:"|\').*?(?:/>|</assemblyIdentity>)', re.DOTALL)
            if re.search(pattern, manifest_buf) is None:
                return
            manifest_f = open(manifest_file, b'w')
            try:
                manifest_f.write(manifest_buf)
                return manifest_file
            finally:
                manifest_f.close()

        except IOError:
            pass

        return

    def library_dir_option(self, dir):
        return b'/LIBPATH:' + dir

    def runtime_library_dir_option(self, dir):
        raise DistutilsPlatformError(b"don't know how to set runtime library search path for MSVC++")
        return

    def library_option(self, lib):
        return self.library_filename(lib)

    def find_library_file(self, dirs, lib, debug=0):
        if debug:
            try_names = [
             lib + b'_d', lib]
        else:
            try_names = [
             lib]
        for dir in dirs:
            for name in try_names:
                libfile = os.path.join(dir, self.library_filename(name))
                if os.path.exists(libfile):
                    return libfile

        else:
            return

        return

    def find_exe(self, exe):
        for p in self.__paths:
            fn = os.path.join(os.path.abspath(p), exe)
            if os.path.isfile(fn):
                return fn

        for p in os.environ[b'Path'].split(b';'):
            fn = os.path.join(os.path.abspath(p), exe)
            if os.path.isfile(fn):
                return fn

        return exe
