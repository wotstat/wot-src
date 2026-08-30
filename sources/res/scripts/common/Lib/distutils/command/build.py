__revision__ = b'$Id$'
import sys, os
from distutils.util import get_platform
from distutils.core import Command
from distutils.errors import DistutilsOptionError

def show_compilers():
    from distutils.ccompiler import show_compilers
    show_compilers()
    return


class build(Command):
    description = b'build everything needed to install'
    user_options = [
     (b'build-base=', b'b', b'base directory for build library'),
     (b'build-purelib=', None, b'build directory for platform-neutral distributions'),
     (b'build-platlib=', None, b'build directory for platform-specific distributions'),
     (
      b'build-lib=', None,
      b'build directory for all distribution (defaults to either ' + b'build-purelib or build-platlib'),
     (b'build-scripts=', None, b'build directory for scripts'),
     (b'build-temp=', b't', b'temporary build directory'),
     (
      b'plat-name=', b'p',
      b'platform name to build for, if supported (default: %s)' % get_platform()),
     (b'compiler=', b'c', b'specify the compiler type'),
     (b'debug', b'g', b'compile extensions and libraries with debugging information'),
     (b'force', b'f', b'forcibly build everything (ignore file timestamps)'),
     (b'executable=', b'e', b'specify final destination interpreter path (build.py)')]
    boolean_options = [
     b'debug', b'force']
    help_options = [
     (
      b'help-compiler', None,
      b'list available compilers', show_compilers)]

    def initialize_options(self):
        self.build_base = b'build'
        self.build_purelib = None
        self.build_platlib = None
        self.build_lib = None
        self.build_temp = None
        self.build_scripts = None
        self.compiler = None
        self.plat_name = None
        self.debug = None
        self.force = 0
        self.executable = None
        return

    def finalize_options(self):
        if self.plat_name is None:
            self.plat_name = get_platform()
        elif os.name != b'nt':
            raise DistutilsOptionError(b"--plat-name only supported on Windows (try using './configure --help' on your platform)")
        plat_specifier = b'.%s-%s' % (self.plat_name, sys.version[0:3])
        if hasattr(sys, b'gettotalrefcount'):
            plat_specifier += b'-pydebug'
        if self.build_purelib is None:
            self.build_purelib = os.path.join(self.build_base, b'lib')
        if self.build_platlib is None:
            self.build_platlib = os.path.join(self.build_base, b'lib' + plat_specifier)
        if self.build_lib is None:
            if self.distribution.ext_modules:
                self.build_lib = self.build_platlib
            else:
                self.build_lib = self.build_purelib
        if self.build_temp is None:
            self.build_temp = os.path.join(self.build_base, b'temp' + plat_specifier)
        if self.build_scripts is None:
            self.build_scripts = os.path.join(self.build_base, b'scripts-' + sys.version[0:3])
        if self.executable is None and sys.executable:
            self.executable = os.path.normpath(sys.executable)
        return

    def run(self):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        return

    def has_pure_modules(self):
        return self.distribution.has_pure_modules()

    def has_c_libraries(self):
        return self.distribution.has_c_libraries()

    def has_ext_modules(self):
        return self.distribution.has_ext_modules()

    def has_scripts(self):
        return self.distribution.has_scripts()

    sub_commands = [
     (
      b'build_py', has_pure_modules),
     (
      b'build_clib', has_c_libraries),
     (
      b'build_ext', has_ext_modules),
     (
      b'build_scripts', has_scripts)]
