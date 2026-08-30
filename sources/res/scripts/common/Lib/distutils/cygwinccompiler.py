__revision__ = b'$Id$'
import os, sys, copy
from distutils.ccompiler import gen_preprocess_options, gen_lib_options
from distutils.unixccompiler import UnixCCompiler
from distutils.file_util import write_file
from distutils.errors import DistutilsExecError, CompileError, UnknownFileError
from distutils import log

def get_msvcr():
    msc_pos = sys.version.find(b'MSC v.')
    if msc_pos != -1:
        msc_ver = sys.version[msc_pos + 6:msc_pos + 10]
        if msc_ver == b'1300':
            return [
             b'msvcr70']
        if msc_ver == b'1310':
            return [
             b'msvcr71']
        if msc_ver == b'1400':
            return [
             b'msvcr80']
        if msc_ver == b'1500':
            return [
             b'msvcr90']
        raise ValueError(b'Unknown MS Compiler version %s ' % msc_ver)
    return


class CygwinCCompiler(UnixCCompiler):
    compiler_type = b'cygwin'
    obj_extension = b'.o'
    static_lib_extension = b'.a'
    shared_lib_extension = b'.dll'
    static_lib_format = b'lib%s%s'
    shared_lib_format = b'%s%s'
    exe_extension = b'.exe'

    def __init__(self, verbose=0, dry_run=0, force=0):
        UnixCCompiler.__init__(self, verbose, dry_run, force)
        status, details = check_config_h()
        self.debug_print(b"Python's GCC status: %s (details: %s)" % (
         status, details))
        if status is not CONFIG_H_OK:
            self.warn(b"Python's pyconfig.h doesn't seem to support your compiler. Reason: %s. Compiling may fail because of undefined preprocessor macros." % details)
        self.gcc_version, self.ld_version, self.dllwrap_version = get_versions()
        self.debug_print(self.compiler_type + b': gcc %s, ld %s, dllwrap %s\n' % (
         self.gcc_version,
         self.ld_version,
         self.dllwrap_version))
        if self.ld_version >= b'2.10.90':
            self.linker_dll = b'gcc'
        else:
            self.linker_dll = b'dllwrap'
        if self.ld_version >= b'2.13':
            shared_option = b'-shared'
        else:
            shared_option = b'-mdll -static'
        self.set_executables(compiler=b'gcc -mcygwin -O -Wall', compiler_so=b'gcc -mcygwin -mdll -O -Wall', compiler_cxx=b'g++ -mcygwin -O -Wall', linker_exe=b'gcc -mcygwin', linker_so=b'%s -mcygwin %s' % (
         self.linker_dll, shared_option))
        if self.gcc_version == b'2.91.57':
            self.dll_libraries = [
             b'msvcrt']
            self.warn(b'Consider upgrading to a newer version of gcc')
        else:
            self.dll_libraries = get_msvcr()
        return

    def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
        if ext == b'.rc' or ext == b'.res':
            try:
                self.spawn([3, 4, src, 5, obj])
            except DistutilsExecError as msg:
                raise CompileError, msg

        else:
            try:
                self.spawn(self.compiler_so + cc_args + [src, b'-o', obj] + extra_postargs)
            except DistutilsExecError as msg:
                raise CompileError, msg

        return

    def link(self, target_desc, objects, output_filename, output_dir=None, libraries=None, library_dirs=None, runtime_library_dirs=None, export_symbols=None, debug=0, extra_preargs=None, extra_postargs=None, build_temp=None, target_lang=None):
        extra_preargs = copy.copy(extra_preargs or [])
        libraries = copy.copy(libraries or [])
        objects = copy.copy(objects or [])
        libraries.extend(self.dll_libraries)
        if export_symbols is not None and (target_desc != self.EXECUTABLE or self.linker_dll == b'gcc'):
            temp_dir = os.path.dirname(objects[0])
            dll_name, dll_extension = os.path.splitext(os.path.basename(output_filename))
            def_file = os.path.join(temp_dir, dll_name + b'.def')
            lib_file = os.path.join(temp_dir, b'lib' + dll_name + b'.a')
            contents = [
             b'LIBRARY %s' % os.path.basename(output_filename),
             b'EXPORTS']
            for sym in export_symbols:
                contents.append(sym)

            self.execute(write_file, (def_file, contents), b'writing %s' % def_file)
            if self.linker_dll == b'dllwrap':
                extra_preargs.extend([b'--output-lib', lib_file])
                extra_preargs.extend([b'--def', def_file])
            else:
                objects.append(def_file)
        if not debug:
            extra_preargs.append(b'-s')
        UnixCCompiler.link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, None, debug, extra_preargs, extra_postargs, build_temp, target_lang)
        return

    def object_filenames(self, source_filenames, strip_dir=0, output_dir=b''):
        if output_dir is None:
            output_dir = b''
        obj_names = []
        for src_name in source_filenames:
            base, ext = os.path.splitext(os.path.normcase(src_name))
            if ext not in self.src_extensions + [b'.rc', b'.res']:
                raise UnknownFileError, b"unknown file type '%s' (from '%s')" % (
                 ext, src_name)
            if strip_dir:
                base = os.path.basename(base)
            if ext == b'.res' or ext == b'.rc':
                obj_names.append(os.path.join(output_dir, base + ext + self.obj_extension))
            else:
                obj_names.append(os.path.join(output_dir, base + self.obj_extension))

        return obj_names


class Mingw32CCompiler(CygwinCCompiler):
    compiler_type = b'mingw32'

    def __init__(self, verbose=0, dry_run=0, force=0):
        CygwinCCompiler.__init__(self, verbose, dry_run, force)
        if self.ld_version >= b'2.13':
            shared_option = b'-shared'
        else:
            shared_option = b'-mdll -static'
        if self.gcc_version <= b'2.91.57':
            entry_point = b'--entry _DllMain@12'
        else:
            entry_point = b''
        if self.gcc_version < b'4' or is_cygwingcc():
            no_cygwin = b' -mno-cygwin'
        else:
            no_cygwin = b''
        self.set_executables(compiler=b'gcc%s -O -Wall' % no_cygwin, compiler_so=b'gcc%s -mdll -O -Wall' % no_cygwin, compiler_cxx=b'g++%s -O -Wall' % no_cygwin, linker_exe=b'gcc%s' % no_cygwin, linker_so=b'%s%s %s %s' % (
         self.linker_dll, no_cygwin,
         shared_option, entry_point))
        self.dll_libraries = []
        self.dll_libraries = get_msvcr()
        return


CONFIG_H_OK = b'ok'
CONFIG_H_NOTOK = b'not ok'
CONFIG_H_UNCERTAIN = b'uncertain'

def check_config_h():
    from distutils import sysconfig
    import string
    if string.find(sys.version, b'GCC') >= 0:
        return (CONFIG_H_OK, b"sys.version mentions 'GCC'")
    else:
        fn = sysconfig.get_config_h_filename()
        try:
            f = open(fn)
            try:
                s = f.read()
            finally:
                f.close()

        except IOError as exc:
            return (CONFIG_H_UNCERTAIN,
             b"couldn't read '%s': %s" % (fn, exc.strerror))

        if string.find(s, b'__GNUC__') >= 0:
            return (CONFIG_H_OK, b"'%s' mentions '__GNUC__'" % fn)
        return (CONFIG_H_NOTOK, b"'%s' does not mention '__GNUC__'" % fn)

    return


def get_versions():
    from distutils.version import LooseVersion
    from distutils.spawn import find_executable
    import re
    gcc_exe = find_executable(b'gcc')
    if gcc_exe:
        out = os.popen(gcc_exe + b' -dumpversion', b'r')
        out_string = out.read()
        out.close()
        result = re.search(b'(\\d+\\.\\d+(\\.\\d+)*)', out_string)
        if result:
            gcc_version = LooseVersion(result.group(1))
        else:
            gcc_version = None
    else:
        gcc_version = None
    ld_exe = find_executable(b'ld')
    if ld_exe:
        out = os.popen(ld_exe + b' -v', b'r')
        out_string = out.read()
        out.close()
        result = re.search(b'(\\d+\\.\\d+(\\.\\d+)*)', out_string)
        if result:
            ld_version = LooseVersion(result.group(1))
        else:
            ld_version = None
    else:
        ld_version = None
    dllwrap_exe = find_executable(b'dllwrap')
    if dllwrap_exe:
        out = os.popen(dllwrap_exe + b' --version', b'r')
        out_string = out.read()
        out.close()
        result = re.search(b' (\\d+\\.\\d+(\\.\\d+)*)', out_string)
        if result:
            dllwrap_version = LooseVersion(result.group(1))
        else:
            dllwrap_version = None
    else:
        dllwrap_version = None
    return (
     gcc_version, ld_version, dllwrap_version)


def is_cygwingcc():
    out = os.popen(b'gcc -dumpmachine', b'r')
    out_string = out.read()
    out.close()
    return out_string.strip().endswith(b'cygwin')
