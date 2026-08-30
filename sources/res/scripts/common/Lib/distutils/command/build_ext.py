__revision__ = b'$Id$'
import sys, os, string, re
from types import *
from site import USER_BASE, USER_SITE
from distutils.core import Command
from distutils.errors import *
from distutils.sysconfig import customize_compiler, get_python_version
from distutils.dep_util import newer_group
from distutils.extension import Extension
from distutils.util import get_platform
from distutils import log
if os.name == b'nt':
    from distutils.msvccompiler import get_build_version
    MSVC_VERSION = int(get_build_version())
extension_name_re = re.compile(b'^[a-zA-Z_][a-zA-Z_0-9]*(\\.[a-zA-Z_][a-zA-Z_0-9]*)*$')

def show_compilers():
    from distutils.ccompiler import show_compilers
    show_compilers()
    return


class build_ext(Command):
    description = b'build C/C++ extensions (compile/link to build directory)'
    sep_by = b" (separated by '%s')" % os.pathsep
    user_options = [
     (b'build-lib=', b'b', b'directory for compiled extension modules'),
     (b'build-temp=', b't', b'directory for temporary files (build by-products)'),
     (
      b'plat-name=', b'p',
      b'platform name to cross-compile for, if supported (default: %s)' % get_platform()),
     (
      b'inplace', b'i',
      b'ignore build-lib and put compiled extensions into the source ' + b'directory alongside your pure Python modules'),
     (
      b'include-dirs=', b'I',
      b'list of directories to search for header files' + sep_by),
     (b'define=', b'D', b'C preprocessor macros to define'),
     (b'undef=', b'U', b'C preprocessor macros to undefine'),
     (b'libraries=', b'l', b'external C libraries to link with'),
     (
      b'library-dirs=', b'L',
      b'directories to search for external C libraries' + sep_by),
     (b'rpath=', b'R', b'directories to search for shared C libraries at runtime'),
     (b'link-objects=', b'O', b'extra explicit link objects to include in the link'),
     (b'debug', b'g', b'compile/link with debugging information'),
     (b'force', b'f', b'forcibly build everything (ignore file timestamps)'),
     (b'compiler=', b'c', b'specify the compiler type'),
     (b'swig-cpp', None, b'make SWIG create C++ files (default is C)'),
     (b'swig-opts=', None, b'list of SWIG command line options'),
     (b'swig=', None, b'path to the SWIG executable'),
     (b'user', None, b'add user include, library and rpath')]
    boolean_options = [
     11, 36, 39, 45, 51]
    help_options = [
     (
      b'help-compiler', None,
      b'list available compilers', show_compilers)]

    def initialize_options(self):
        self.extensions = None
        self.build_lib = None
        self.plat_name = None
        self.build_temp = None
        self.inplace = 0
        self.package = None
        self.include_dirs = None
        self.define = None
        self.undef = None
        self.libraries = None
        self.library_dirs = None
        self.rpath = None
        self.link_objects = None
        self.debug = None
        self.force = None
        self.compiler = None
        self.swig = None
        self.swig_cpp = None
        self.swig_opts = None
        self.user = None
        return

    def finalize_options(self):
        from distutils import sysconfig
        self.set_undefined_options(b'build', (b'build_lib', b'build_lib'), (b'build_temp', b'build_temp'), (b'compiler', b'compiler'), (b'debug', b'debug'), (b'force', b'force'), (b'plat_name', b'plat_name'))
        if self.package is None:
            self.package = self.distribution.ext_package
        self.extensions = self.distribution.ext_modules
        py_include = sysconfig.get_python_inc()
        plat_py_include = sysconfig.get_python_inc(plat_specific=1)
        if self.include_dirs is None:
            self.include_dirs = self.distribution.include_dirs or []
        if isinstance(self.include_dirs, str):
            self.include_dirs = self.include_dirs.split(os.pathsep)
        self.include_dirs.append(py_include)
        if plat_py_include != py_include:
            self.include_dirs.append(plat_py_include)
        self.ensure_string_list(b'libraries')
        self.ensure_string_list(b'link_objects')
        if self.libraries is None:
            self.libraries = []
        if self.library_dirs is None:
            self.library_dirs = []
        elif type(self.library_dirs) is StringType:
            self.library_dirs = string.split(self.library_dirs, os.pathsep)
        if self.rpath is None:
            self.rpath = []
        elif type(self.rpath) is StringType:
            self.rpath = string.split(self.rpath, os.pathsep)
        if os.name == b'nt':
            self.library_dirs.append(os.path.join(sys.exec_prefix, b'libs'))
            if self.debug:
                self.build_temp = os.path.join(self.build_temp, b'Debug')
            else:
                self.build_temp = os.path.join(self.build_temp, b'Release')
            self.include_dirs.append(os.path.join(sys.exec_prefix, b'PC'))
            if MSVC_VERSION == 9:
                if self.plat_name == b'win32':
                    suffix = b''
                else:
                    suffix = self.plat_name[4:]
                for d in ((b'PCbuild',), (b'PC', b'VS9.0')):
                    new_lib = os.path.join(sys.exec_prefix, *d)
                    if suffix:
                        new_lib = os.path.join(new_lib, suffix)
                    self.library_dirs.append(new_lib)

            elif MSVC_VERSION == 8:
                self.library_dirs.append(os.path.join(sys.exec_prefix, b'PC', b'VS8.0'))
            elif MSVC_VERSION == 7:
                self.library_dirs.append(os.path.join(sys.exec_prefix, b'PC', b'VS7.1'))
            else:
                self.library_dirs.append(os.path.join(sys.exec_prefix, b'PC', b'VC6'))
        if os.name == b'os2':
            self.library_dirs.append(os.path.join(sys.exec_prefix, b'Config'))
        if sys.platform[:6] == b'cygwin' or sys.platform[:6] == b'atheos':
            if sys.executable.startswith(os.path.join(sys.exec_prefix, b'bin')):
                self.library_dirs.append(os.path.join(sys.prefix, b'lib', b'python' + get_python_version(), b'config'))
            else:
                self.library_dirs.append(b'.')
        if sysconfig.get_config_var(b'Py_ENABLE_SHARED'):
            if not sysconfig.python_build:
                self.library_dirs.append(sysconfig.get_config_var(b'LIBDIR'))
            else:
                self.library_dirs.append(b'.')
        if self.define:
            defines = self.define.split(b',')
            self.define = map((lambda symbol: (symbol, b'1')), defines)
        if self.undef:
            self.undef = self.undef.split(b',')
        if self.swig_opts is None:
            self.swig_opts = []
        else:
            self.swig_opts = self.swig_opts.split(b' ')
        if self.user:
            user_include = os.path.join(USER_BASE, b'include')
            user_lib = os.path.join(USER_BASE, b'lib')
            if os.path.isdir(user_include):
                self.include_dirs.append(user_include)
            if os.path.isdir(user_lib):
                self.library_dirs.append(user_lib)
                self.rpath.append(user_lib)
        return

    def run(self):
        from distutils.ccompiler import new_compiler
        if not self.extensions:
            return
        else:
            if self.distribution.has_c_libraries():
                build_clib = self.get_finalized_command(b'build_clib')
                self.libraries.extend(build_clib.get_library_names() or [])
                self.library_dirs.append(build_clib.build_clib)
            self.compiler = new_compiler(compiler=self.compiler, verbose=self.verbose, dry_run=self.dry_run, force=self.force)
            customize_compiler(self.compiler)
            if os.name == b'nt' and self.plat_name != get_platform():
                self.compiler.initialize(self.plat_name)
            if self.include_dirs is not None:
                self.compiler.set_include_dirs(self.include_dirs)
            if self.define is not None:
                for name, value in self.define:
                    self.compiler.define_macro(name, value)

            if self.undef is not None:
                for macro in self.undef:
                    self.compiler.undefine_macro(macro)

            if self.libraries is not None:
                self.compiler.set_libraries(self.libraries)
            if self.library_dirs is not None:
                self.compiler.set_library_dirs(self.library_dirs)
            if self.rpath is not None:
                self.compiler.set_runtime_library_dirs(self.rpath)
            if self.link_objects is not None:
                self.compiler.set_link_objects(self.link_objects)
            self.build_extensions()
            return

    def check_extensions_list(self, extensions):
        if not isinstance(extensions, list):
            raise DistutilsSetupError, b"'ext_modules' option must be a list of Extension instances"
        for i, ext in enumerate(extensions):
            if isinstance(ext, Extension):
                continue
            if not isinstance(ext, tuple) or len(ext) != 2:
                raise DistutilsSetupError, b"each element of 'ext_modules' option must be an Extension instance or 2-tuple"
            ext_name, build_info = ext
            log.warn(b"old-style (ext_name, build_info) tuple found in ext_modules for extension '%s' -- please convert to Extension instance" % ext_name)
            if not (isinstance(ext_name, str) and extension_name_re.match(ext_name)):
                raise DistutilsSetupError, b"first element of each tuple in 'ext_modules' must be the extension name (a string)"
            if not isinstance(build_info, dict):
                raise DistutilsSetupError, b"second element of each tuple in 'ext_modules' must be a dictionary (build info)"
            ext = Extension(ext_name, build_info[b'sources'])
            for key in (b'include_dirs', b'library_dirs', b'libraries', b'extra_objects', b'extra_compile_args', b'extra_link_args'):
                val = build_info.get(key)
                if val is not None:
                    setattr(ext, key, val)

            ext.runtime_library_dirs = build_info.get(b'rpath')
            if b'def_file' in build_info:
                log.warn(b"'def_file' element of build info dict no longer supported")
            macros = build_info.get(b'macros')
            if macros:
                ext.define_macros = []
                ext.undef_macros = []
                for macro in macros:
                    if not (isinstance(macro, tuple) and len(macro) in (1, 2)):
                        raise DistutilsSetupError, b"'macros' element of build info dict must be 1- or 2-tuple"
                    if len(macro) == 1:
                        ext.undef_macros.append(macro[0])
                    elif len(macro) == 2:
                        ext.define_macros.append(macro)

            extensions[i] = ext

        return

    def get_source_files(self):
        self.check_extensions_list(self.extensions)
        filenames = []
        for ext in self.extensions:
            filenames.extend(ext.sources)

        return filenames

    def get_outputs(self):
        self.check_extensions_list(self.extensions)
        outputs = []
        for ext in self.extensions:
            outputs.append(self.get_ext_fullpath(ext.name))

        return outputs

    def build_extensions(self):
        self.check_extensions_list(self.extensions)
        for ext in self.extensions:
            self.build_extension(ext)

        return

    def build_extension(self, ext):
        sources = ext.sources
        if sources is None or type(sources) not in (ListType, TupleType):
            raise DistutilsSetupError, (b"in 'ext_modules' option (extension '%s'), " + b"'sources' must be present and must be " + b'a list of source filenames') % ext.name
        sources = list(sources)
        ext_path = self.get_ext_fullpath(ext.name)
        depends = sources + ext.depends
        if not (self.force or newer_group(depends, ext_path, b'newer')):
            log.debug(b"skipping '%s' extension (up-to-date)", ext.name)
            return
        else:
            log.info(b"building '%s' extension", ext.name)
            sources = self.swig_sources(sources, ext)
            extra_args = ext.extra_compile_args or []
            macros = ext.define_macros[:]
            for undef in ext.undef_macros:
                macros.append((undef,))

            objects = self.compiler.compile(sources, output_dir=self.build_temp, macros=macros, include_dirs=ext.include_dirs, debug=self.debug, extra_postargs=extra_args, depends=ext.depends)
            self._built_objects = objects[:]
            if ext.extra_objects:
                objects.extend(ext.extra_objects)
            extra_args = ext.extra_link_args or []
            language = ext.language or self.compiler.detect_language(sources)
            self.compiler.link_shared_object(objects, ext_path, libraries=self.get_libraries(ext), library_dirs=ext.library_dirs, runtime_library_dirs=ext.runtime_library_dirs, extra_postargs=extra_args, export_symbols=self.get_export_symbols(ext), debug=self.debug, build_temp=self.build_temp, target_lang=language)
            return

    def swig_sources(self, sources, extension):
        new_sources = []
        swig_sources = []
        swig_targets = {}
        if self.swig_cpp:
            log.warn(b'--swig-cpp is deprecated - use --swig-opts=-c++')
        if self.swig_cpp or b'-c++' in self.swig_opts or b'-c++' in extension.swig_opts:
            target_ext = b'.cpp'
        else:
            target_ext = b'.c'
        for source in sources:
            base, ext = os.path.splitext(source)
            if ext == b'.i':
                new_sources.append(base + b'_wrap' + target_ext)
                swig_sources.append(source)
                swig_targets[source] = new_sources[-1]
            else:
                new_sources.append(source)

        if not swig_sources:
            return new_sources
        swig = self.swig or self.find_swig()
        swig_cmd = [swig, b'-python']
        swig_cmd.extend(self.swig_opts)
        if self.swig_cpp:
            swig_cmd.append(b'-c++')
        if not self.swig_opts:
            for o in extension.swig_opts:
                swig_cmd.append(o)

        for source in swig_sources:
            target = swig_targets[source]
            log.info(b'swigging %s to %s', source, target)
            self.spawn(swig_cmd + [b'-o', target, source])

        return new_sources

    def find_swig(self):
        if os.name == b'posix':
            return b'swig'
        if os.name == b'nt':
            for vers in (b'1.3', b'1.2', b'1.1'):
                fn = os.path.join(b'c:\\swig%s' % vers, b'swig.exe')
                if os.path.isfile(fn):
                    return fn
            else:
                return b'swig.exe'

        elif os.name == b'os2':
            return b'swig.exe'
        raise DistutilsPlatformError, b"I don't know how to find (much less run) SWIG on platform '%s'" % os.name
        return

    def get_ext_fullpath(self, ext_name):
        all_dots = string.maketrans(b'/' + os.sep, b'..')
        ext_name = ext_name.translate(all_dots)
        fullname = self.get_ext_fullname(ext_name)
        modpath = fullname.split(b'.')
        filename = self.get_ext_filename(ext_name)
        filename = os.path.split(filename)[-1]
        if not self.inplace:
            filename = os.path.join(*(modpath[:-1] + [filename]))
            return os.path.join(self.build_lib, filename)
        package = (b'.').join(modpath[0:-1])
        build_py = self.get_finalized_command(b'build_py')
        package_dir = os.path.abspath(build_py.get_package_dir(package))
        return os.path.join(package_dir, filename)

    def get_ext_fullname(self, ext_name):
        if self.package is None:
            return ext_name
        else:
            return self.package + b'.' + ext_name
            return

    def get_ext_filename(self, ext_name):
        from distutils.sysconfig import get_config_var
        ext_path = string.split(ext_name, b'.')
        if os.name == b'os2':
            ext_path[len(ext_path) - 1] = ext_path[len(ext_path) - 1][:8]
        so_ext = get_config_var(b'SO')
        if os.name == b'nt' and self.debug:
            return os.path.join(*ext_path) + b'_d' + so_ext
        return os.path.join(*ext_path) + so_ext

    def get_export_symbols(self, ext):
        initfunc_name = b'init' + ext.name.split(b'.')[-1]
        if initfunc_name not in ext.export_symbols:
            ext.export_symbols.append(initfunc_name)
        return ext.export_symbols

    def get_libraries(self, ext):
        if sys.platform == b'win32':
            from distutils.msvccompiler import MSVCCompiler
            if not isinstance(self.compiler, MSVCCompiler):
                template = b'python%d%d'
                if self.debug:
                    template = template + b'_d'
                pythonlib = template % (
                 sys.hexversion >> 24, sys.hexversion >> 16 & 255)
                return ext.libraries + [pythonlib]
            return ext.libraries
        else:
            if sys.platform == b'os2emx':
                template = b'python%d%d'
                pythonlib = template % (
                 sys.hexversion >> 24, sys.hexversion >> 16 & 255)
                return ext.libraries + [pythonlib]
            else:
                if sys.platform[:6] == b'cygwin':
                    template = b'python%d.%d'
                    pythonlib = template % (
                     sys.hexversion >> 24, sys.hexversion >> 16 & 255)
                    return ext.libraries + [pythonlib]
                if sys.platform[:6] == b'atheos':
                    from distutils import sysconfig
                    template = b'python%d.%d'
                    pythonlib = template % (
                     sys.hexversion >> 24, sys.hexversion >> 16 & 255)
                    extra = []
                    for lib in sysconfig.get_config_var(b'SHLIBS').split():
                        if lib.startswith(b'-l'):
                            extra.append(lib[2:])
                        else:
                            extra.append(lib)

                    return ext.libraries + [pythonlib, b'm'] + extra
                if sys.platform == b'darwin':
                    return ext.libraries
                if sys.platform[:3] == b'aix':
                    return ext.libraries
                from distutils import sysconfig
                if sysconfig.get_config_var(b'Py_ENABLE_SHARED'):
                    template = b'python%d.%d'
                    pythonlib = template % (
                     sys.hexversion >> 24, sys.hexversion >> 16 & 255)
                    return ext.libraries + [pythonlib]
                return ext.libraries

        return
