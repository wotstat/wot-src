from distutils import log
__revision__ = b'$Id$'
import sys, os, string
from types import *
from distutils.core import Command
from distutils.debug import DEBUG
from distutils.sysconfig import get_config_vars
from distutils.errors import DistutilsPlatformError
from distutils.file_util import write_file
from distutils.util import convert_path, subst_vars, change_root
from distutils.util import get_platform
from distutils.errors import DistutilsOptionError
from site import USER_BASE
from site import USER_SITE
if sys.version < b'2.2':
    WINDOWS_SCHEME = {b'purelib': b'$base', b'platlib': b'$base', 
       b'headers': b'$base/Include/$dist_name', 
       b'scripts': b'$base/Scripts', 
       b'data': b'$base'}
else:
    WINDOWS_SCHEME = {b'purelib': b'$base/Lib/site-packages', b'platlib': b'$base/Lib/site-packages', 
       b'headers': b'$base/Include/$dist_name', 
       b'scripts': b'$base/Scripts', 
       b'data': b'$base'}
INSTALL_SCHEMES = {b'unix_prefix': {b'purelib': b'$base/lib/python$py_version_short/site-packages', 
                    b'platlib': b'$platbase/lib/python$py_version_short/site-packages', 
                    b'headers': b'$base/include/python$py_version_short/$dist_name', 
                    b'scripts': b'$base/bin', 
                    b'data': b'$base'}, 
   b'unix_home': {b'purelib': b'$base/lib/python', 
                  b'platlib': b'$base/lib/python', 
                  b'headers': b'$base/include/python/$dist_name', 
                  b'scripts': b'$base/bin', 
                  b'data': b'$base'}, 
   b'unix_user': {b'purelib': b'$usersite', 
                  b'platlib': b'$usersite', 
                  b'headers': b'$userbase/include/python$py_version_short/$dist_name', 
                  b'scripts': b'$userbase/bin', 
                  b'data': b'$userbase'}, 
   b'nt': WINDOWS_SCHEME, 
   b'nt_user': {b'purelib': b'$usersite', 
                b'platlib': b'$usersite', 
                b'headers': b'$userbase/Python$py_version_nodot/Include/$dist_name', 
                b'scripts': b'$userbase/Scripts', 
                b'data': b'$userbase'}, 
   b'os2': {b'purelib': b'$base/Lib/site-packages', 
            b'platlib': b'$base/Lib/site-packages', 
            b'headers': b'$base/Include/$dist_name', 
            b'scripts': b'$base/Scripts', 
            b'data': b'$base'}, 
   b'os2_home': {b'purelib': b'$usersite', 
                 b'platlib': b'$usersite', 
                 b'headers': b'$userbase/include/python$py_version_short/$dist_name', 
                 b'scripts': b'$userbase/bin', 
                 b'data': b'$userbase'}}
SCHEME_KEYS = (b'purelib', b'platlib', b'headers', b'scripts', b'data')

class install(Command):
    description = b'install everything from build directory'
    user_options = [
     (b'prefix=', None, b'installation prefix'),
     (b'exec-prefix=', None, b'(Unix only) prefix for platform-specific files'),
     (b'home=', None, b'(Unix only) home directory to install under'),
     (
      b'user', None,
      b"install in user site-package '%s'" % USER_SITE),
     (b'install-base=', None, b'base installation directory (instead of --prefix or --home)'),
     (
      b'install-platbase=', None,
      b'base installation directory for platform-specific files ' + b'(instead of --exec-prefix or --home)'),
     (b'root=', None, b'install everything relative to this alternate root directory'),
     (b'install-purelib=', None, b'installation directory for pure Python module distributions'),
     (b'install-platlib=', None, b'installation directory for non-pure module distributions'),
     (
      b'install-lib=', None,
      b'installation directory for all module distributions ' + b'(overrides --install-purelib and --install-platlib)'),
     (b'install-headers=', None, b'installation directory for C/C++ headers'),
     (b'install-scripts=', None, b'installation directory for Python scripts'),
     (b'install-data=', None, b'installation directory for data files'),
     (b'compile', b'c', b'compile .py to .pyc [default]'),
     (b'no-compile', None, b"don't compile .py files"),
     (b'optimize=', b'O', b'also compile with optimization: -O1 for "python -O", -O2 for "python -OO", and -O0 to disable [default: -O0]'),
     (b'force', b'f', b'force installation (overwrite any existing files)'),
     (b'skip-build', None, b'skip rebuilding everything (for testing/debugging)'),
     (b'record=', None, b'filename in which to record list of installed files')]
    boolean_options = [
     b'compile', b'force', b'skip-build', b'user']
    negative_opt = {b'no-compile': b'compile'}

    def initialize_options(self):
        self.prefix = None
        self.exec_prefix = None
        self.home = None
        self.user = 0
        self.install_base = None
        self.install_platbase = None
        self.root = None
        self.install_purelib = None
        self.install_platlib = None
        self.install_headers = None
        self.install_lib = None
        self.install_scripts = None
        self.install_data = None
        self.install_userbase = USER_BASE
        self.install_usersite = USER_SITE
        self.compile = None
        self.optimize = None
        self.extra_path = None
        self.install_path_file = 1
        self.force = 0
        self.skip_build = 0
        self.warn_dir = 1
        self.build_base = None
        self.build_lib = None
        self.record = None
        return

    def finalize_options(self):
        if (self.prefix or self.exec_prefix or self.home) and (self.install_base or self.install_platbase):
            raise DistutilsOptionError, b'must supply either prefix/exec-prefix/home or ' + b'install-base/install-platbase -- not both'
        if self.home and (self.prefix or self.exec_prefix):
            raise DistutilsOptionError, b'must supply either home or prefix/exec-prefix -- not both'
        if self.user and (self.prefix or self.exec_prefix or self.home or self.install_base or self.install_platbase):
            raise DistutilsOptionError(b"can't combine user with prefix, exec_prefix/home, or install_(plat)base")
        if os.name != b'posix':
            if self.exec_prefix:
                self.warn(b'exec-prefix option ignored on this platform')
                self.exec_prefix = None
        self.dump_dirs(b'pre-finalize_{unix,other}')
        if os.name == b'posix':
            self.finalize_unix()
        else:
            self.finalize_other()
        self.dump_dirs(b'post-finalize_{unix,other}()')
        py_version = string.split(sys.version)[0]
        prefix, exec_prefix = get_config_vars(b'prefix', b'exec_prefix')
        self.config_vars = {b'dist_name': (self.distribution.get_name()), b'dist_version': (self.distribution.get_version()), 
           b'dist_fullname': (self.distribution.get_fullname()), 
           b'py_version': py_version, 
           b'py_version_short': (py_version[0:3]), 
           b'py_version_nodot': (py_version[0] + py_version[2]), 
           b'sys_prefix': prefix, 
           b'prefix': prefix, 
           b'sys_exec_prefix': exec_prefix, 
           b'exec_prefix': exec_prefix, 
           b'userbase': (self.install_userbase), 
           b'usersite': (self.install_usersite)}
        self.expand_basedirs()
        self.dump_dirs(b'post-expand_basedirs()')
        self.config_vars[b'base'] = self.install_base
        self.config_vars[b'platbase'] = self.install_platbase
        if DEBUG:
            from pprint import pprint
            print b'config vars:'
            pprint(self.config_vars)
        self.expand_dirs()
        self.dump_dirs(b'post-expand_dirs()')
        if self.user:
            self.create_home_path()
        if self.install_lib is None:
            if self.distribution.ext_modules:
                self.install_lib = self.install_platlib
            else:
                self.install_lib = self.install_purelib
        self.convert_paths(b'lib', b'purelib', b'platlib', b'scripts', b'data', b'headers', b'userbase', b'usersite')
        self.handle_extra_path()
        self.install_libbase = self.install_lib
        self.install_lib = os.path.join(self.install_lib, self.extra_dirs)
        if self.root is not None:
            self.change_roots(b'libbase', b'lib', b'purelib', b'platlib', b'scripts', b'data', b'headers')
        self.dump_dirs(b'after prepending root')
        self.set_undefined_options(b'build', (b'build_base', b'build_base'), (b'build_lib', b'build_lib'))
        return

    def dump_dirs(self, msg):
        if DEBUG:
            from distutils.fancy_getopt import longopt_xlate
            print msg + b':'
            for opt in self.user_options:
                opt_name = opt[0]
                if opt_name[-1] == b'=':
                    opt_name = opt_name[0:-1]
                if opt_name in self.negative_opt:
                    opt_name = string.translate(self.negative_opt[opt_name], longopt_xlate)
                    val = not getattr(self, opt_name)
                else:
                    opt_name = string.translate(opt_name, longopt_xlate)
                    val = getattr(self, opt_name)
                print b'  %s: %s' % (opt_name, val)

        return

    def finalize_unix(self):
        if self.install_base is not None or self.install_platbase is not None:
            if self.install_lib is None and self.install_purelib is None and self.install_platlib is None or self.install_headers is None or self.install_scripts is None or self.install_data is None:
                raise DistutilsOptionError, b'install-base or install-platbase supplied, but installation scheme is incomplete'
            return
        if self.user:
            if self.install_userbase is None:
                raise DistutilsPlatformError(b'User base directory is not specified')
            self.install_base = self.install_platbase = self.install_userbase
            self.select_scheme(b'unix_user')
        elif self.home is not None:
            self.install_base = self.install_platbase = self.home
            self.select_scheme(b'unix_home')
        else:
            if self.prefix is None:
                if self.exec_prefix is not None:
                    raise DistutilsOptionError, b'must not supply exec-prefix without prefix'
                self.prefix = os.path.normpath(sys.prefix)
                self.exec_prefix = os.path.normpath(sys.exec_prefix)
            elif self.exec_prefix is None:
                self.exec_prefix = self.prefix
            self.install_base = self.prefix
            self.install_platbase = self.exec_prefix
            self.select_scheme(b'unix_prefix')
        return

    def finalize_other(self):
        if self.user:
            if self.install_userbase is None:
                raise DistutilsPlatformError(b'User base directory is not specified')
            self.install_base = self.install_platbase = self.install_userbase
            self.select_scheme(os.name + b'_user')
        elif self.home is not None:
            self.install_base = self.install_platbase = self.home
            self.select_scheme(b'unix_home')
        elif self.prefix is None:
            self.prefix = os.path.normpath(sys.prefix)
        self.install_base = self.install_platbase = self.prefix
        try:
            self.select_scheme(os.name)
        except KeyError:
            raise DistutilsPlatformError, b"I don't know how to install stuff on '%s'" % os.name

        return

    def select_scheme(self, name):
        scheme = INSTALL_SCHEMES[name]
        for key in SCHEME_KEYS:
            attrname = b'install_' + key
            if getattr(self, attrname) is None:
                setattr(self, attrname, scheme[key])

        return

    def _expand_attrs(self, attrs):
        for attr in attrs:
            val = getattr(self, attr)
            if val is not None:
                if os.name == b'posix' or os.name == b'nt':
                    val = os.path.expanduser(val)
                val = subst_vars(val, self.config_vars)
                setattr(self, attr, val)

        return

    def expand_basedirs(self):
        self._expand_attrs([b'install_base',
         b'install_platbase',
         b'root'])
        return

    def expand_dirs(self):
        self._expand_attrs([1, 
         2, 
         3, 
         4, 
         5, 
         6])
        return

    def convert_paths(self, *names):
        for name in names:
            attr = b'install_' + name
            setattr(self, attr, convert_path(getattr(self, attr)))

        return

    def handle_extra_path(self):
        if self.extra_path is None:
            self.extra_path = self.distribution.extra_path
        if self.extra_path is not None:
            if type(self.extra_path) is StringType:
                self.extra_path = string.split(self.extra_path, b',')
            if len(self.extra_path) == 1:
                path_file = extra_dirs = self.extra_path[0]
            elif len(self.extra_path) == 2:
                path_file, extra_dirs = self.extra_path
            else:
                raise DistutilsOptionError, b"'extra_path' option must be a list, tuple, or comma-separated string with 1 or 2 elements"
            extra_dirs = convert_path(extra_dirs)
        else:
            path_file = None
            extra_dirs = b''
        self.path_file = path_file
        self.extra_dirs = extra_dirs
        return

    def change_roots(self, *names):
        for name in names:
            attr = b'install_' + name
            setattr(self, attr, change_root(self.root, getattr(self, attr)))

        return

    def create_home_path(self):
        if not self.user:
            return
        home = convert_path(os.path.expanduser(b'~'))
        for name, path in self.config_vars.iteritems():
            if path.startswith(home) and not os.path.isdir(path):
                self.debug_print(b"os.makedirs('%s', 0700)" % path)
                os.makedirs(path, 448)

        return

    def run(self):
        if not self.skip_build:
            self.run_command(b'build')
            build_plat = self.distribution.get_command_obj(b'build').plat_name
            if self.warn_dir and build_plat != get_platform():
                raise DistutilsPlatformError(b"Can't install when cross-compiling")
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        if self.path_file:
            self.create_path_file()
        if self.record:
            outputs = self.get_outputs()
            if self.root:
                root_len = len(self.root)
                for counter in xrange(len(outputs)):
                    outputs[counter] = outputs[counter][root_len:]

            self.execute(write_file, (
             self.record, outputs), b"writing list of installed files to '%s'" % self.record)
        sys_path = map(os.path.normpath, sys.path)
        sys_path = map(os.path.normcase, sys_path)
        install_lib = os.path.normcase(os.path.normpath(self.install_lib))
        if self.warn_dir and not (self.path_file and self.install_path_file) and install_lib not in sys_path:
            log.debug(b"modules installed to '%s', which is not in Python's module search path (sys.path) -- you'll have to change the search path yourself", self.install_lib)
        return

    def create_path_file(self):
        filename = os.path.join(self.install_libbase, self.path_file + b'.pth')
        if self.install_path_file:
            self.execute(write_file, (
             filename, [self.extra_dirs]), b'creating %s' % filename)
        else:
            self.warn(b"path file '%s' not created" % filename)
        return

    def get_outputs(self):
        outputs = []
        for cmd_name in self.get_sub_commands():
            cmd = self.get_finalized_command(cmd_name)
            for filename in cmd.get_outputs():
                if filename not in outputs:
                    outputs.append(filename)

        if self.path_file and self.install_path_file:
            outputs.append(os.path.join(self.install_libbase, self.path_file + b'.pth'))
        return outputs

    def get_inputs(self):
        inputs = []
        for cmd_name in self.get_sub_commands():
            cmd = self.get_finalized_command(cmd_name)
            inputs.extend(cmd.get_inputs())

        return inputs

    def has_lib(self):
        return self.distribution.has_pure_modules() or self.distribution.has_ext_modules()

    def has_headers(self):
        return self.distribution.has_headers()

    def has_scripts(self):
        return self.distribution.has_scripts()

    def has_data(self):
        return self.distribution.has_data_files()

    sub_commands = [
     (
      b'install_lib', has_lib),
     (
      b'install_headers', has_headers),
     (
      b'install_scripts', has_scripts),
     (
      b'install_data', has_data),
     (
      b'install_egg_info',
      (lambda self: True))]
