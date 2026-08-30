__revision__ = b'$Id$'
import os, sys, copy
from distutils.ccompiler import gen_preprocess_options, gen_lib_options
from distutils.unixccompiler import UnixCCompiler
from distutils.file_util import write_file
from distutils.errors import DistutilsExecError, CompileError, UnknownFileError
from distutils import log

class EMXCCompiler(UnixCCompiler):
    compiler_type = b'emx'
    obj_extension = b'.obj'
    static_lib_extension = b'.lib'
    shared_lib_extension = b'.dll'
    static_lib_format = b'%s%s'
    shared_lib_format = b'%s%s'
    res_extension = b'.res'
    exe_extension = b'.exe'

    def __init__(self, verbose=0, dry_run=0, force=0):
        UnixCCompiler.__init__(self, verbose, dry_run, force)
        status, details = check_config_h()
        self.debug_print(b"Python's GCC status: %s (details: %s)" % (
         status, details))
        if status is not CONFIG_H_OK:
            self.warn(b"Python's pyconfig.h doesn't seem to support your compiler.  " + b'Reason: %s.' % details + b'Compiling may fail because of undefined preprocessor macros.')
        self.gcc_version, self.ld_version = get_versions()
        self.debug_print(self.compiler_type + b': gcc %s, ld %s\n' % (
         self.gcc_version,
         self.ld_version))
        self.set_executables(compiler=b'gcc -Zomf -Zmt -O3 -fomit-frame-pointer -mprobe -Wall', compiler_so=b'gcc -Zomf -Zmt -O3 -fomit-frame-pointer -mprobe -Wall', linker_exe=b'gcc -Zomf -Zmt -Zcrtdll', linker_so=b'gcc -Zomf -Zmt -Zcrtdll -Zdll')
        self.dll_libraries = [
         b'gcc']
        return

    def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
        if ext == b'.rc':
            try:
                self.spawn([b'rc', b'-r', src])
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
        if export_symbols is not None and target_desc != self.EXECUTABLE:
            temp_dir = os.path.dirname(objects[0])
            dll_name, dll_extension = os.path.splitext(os.path.basename(output_filename))
            def_file = os.path.join(temp_dir, dll_name + b'.def')
            contents = [
             b'LIBRARY %s INITINSTANCE TERMINSTANCE' % os.path.splitext(os.path.basename(output_filename))[0],
             b'DATA MULTIPLE NONSHARED',
             b'EXPORTS']
            for sym in export_symbols:
                contents.append(b'  "%s"' % sym)

            self.execute(write_file, (def_file, contents), b'writing %s' % def_file)
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
            if ext not in self.src_extensions + [b'.rc']:
                raise UnknownFileError, b"unknown file type '%s' (from '%s')" % (
                 ext, src_name)
            if strip_dir:
                base = os.path.basename(base)
            if ext == b'.rc':
                obj_names.append(os.path.join(output_dir, base + self.res_extension))
            else:
                obj_names.append(os.path.join(output_dir, base + self.obj_extension))

        return obj_names

    def find_library_file(self, dirs, lib, debug=0):
        shortlib = b'%s.lib' % lib
        longlib = b'lib%s.lib' % lib
        try:
            emx_dirs = os.environ[b'LIBRARY_PATH'].split(b';')
        except KeyError:
            emx_dirs = []

        for dir in dirs + emx_dirs:
            shortlibp = os.path.join(dir, shortlib)
            longlibp = os.path.join(dir, longlib)
            if os.path.exists(shortlibp):
                return shortlibp
            if os.path.exists(longlibp):
                return longlibp

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
    from distutils.version import StrictVersion
    from distutils.spawn import find_executable
    import re
    gcc_exe = find_executable(b'gcc')
    if gcc_exe:
        out = os.popen(gcc_exe + b' -dumpversion', b'r')
        try:
            out_string = out.read()
        finally:
            out.close()

        result = re.search(b'(\\d+\\.\\d+\\.\\d+)', out_string)
        if result:
            gcc_version = StrictVersion(result.group(1))
        else:
            gcc_version = None
    else:
        gcc_version = None
    ld_version = None
    return (gcc_version, ld_version)
