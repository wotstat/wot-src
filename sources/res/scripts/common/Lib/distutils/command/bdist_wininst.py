__revision__ = b'$Id$'
import sys, os, string
from sysconfig import get_python_version
from distutils.core import Command
from distutils.dir_util import remove_tree
from distutils.errors import DistutilsOptionError, DistutilsPlatformError
from distutils import log
from distutils.util import get_platform

class bdist_wininst(Command):
    description = b'create an executable installer for MS Windows'
    user_options = [
     (b'bdist-dir=', None, b'temporary directory for creating the distribution'),
     (
      b'plat-name=', b'p',
      b'platform name to embed in generated filenames (default: %s)' % get_platform()),
     (
      b'keep-temp', b'k',
      b'keep the pseudo-installation tree around after ' + b'creating the distribution archive'),
     (
      b'target-version=', None,
      b'require a specific python version' + b' on the target system'),
     (b'no-target-compile', b'c', b'do not compile .py to .pyc on the target system'),
     (b'no-target-optimize', b'o', b'do not compile .py to .pyo (optimized) on the target system'),
     (b'dist-dir=', b'd', b'directory to put final built distributions in'),
     (b'bitmap=', b'b', b'bitmap to use for the installer instead of python-powered logo'),
     (b'title=', b't', b'title to display on the installer background instead of default'),
     (b'skip-build', None, b'skip rebuilding everything (for testing/debugging)'),
     (b'install-script=', None, b'basename of installation script to be run after installation or before deinstallation'),
     (b'pre-install-script=', None, b'Fully qualified filename of a script to be run before any files are installed.  This script need not be in the distribution'),
     (b'user-access-control=', None, b"specify Vista's UAC handling - 'none'/default=no handling, 'auto'=use UAC if target Python installed for all users, 'force'=always use UAC")]
    boolean_options = [
     b'keep-temp', b'no-target-compile', b'no-target-optimize',
     b'skip-build']

    def initialize_options(self):
        self.bdist_dir = None
        self.plat_name = None
        self.keep_temp = 0
        self.no_target_compile = 0
        self.no_target_optimize = 0
        self.target_version = None
        self.dist_dir = None
        self.bitmap = None
        self.title = None
        self.skip_build = None
        self.install_script = None
        self.pre_install_script = None
        self.user_access_control = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'bdist', (b'skip_build', b'skip_build'))
        if self.bdist_dir is None:
            if self.skip_build and self.plat_name:
                bdist = self.distribution.get_command_obj(b'bdist')
                bdist.plat_name = self.plat_name
            bdist_base = self.get_finalized_command(b'bdist').bdist_base
            self.bdist_dir = os.path.join(bdist_base, b'wininst')
        if not self.target_version:
            self.target_version = b''
        if not self.skip_build and self.distribution.has_ext_modules():
            short_version = get_python_version()
            if self.target_version and self.target_version != short_version:
                raise DistutilsOptionError, b"target version can only be %s, or the '--skip-build' option must be specified" % (
                 short_version,)
            self.target_version = short_version
        self.set_undefined_options(b'bdist', (b'dist_dir', b'dist_dir'), (b'plat_name', b'plat_name'))
        if self.install_script:
            for script in self.distribution.scripts:
                if self.install_script == os.path.basename(script):
                    break
            else:
                raise DistutilsOptionError, b"install_script '%s' not found in scripts" % self.install_script

        return

    def run(self):
        if sys.platform != b'win32' and (self.distribution.has_ext_modules() or self.distribution.has_c_libraries()):
            raise DistutilsPlatformError(b'distribution contains extensions and/or C libraries; must be compiled on a Windows 32 platform')
        if not self.skip_build:
            self.run_command(b'build')
        install = self.reinitialize_command(b'install', reinit_subcommands=1)
        install.root = self.bdist_dir
        install.skip_build = self.skip_build
        install.warn_dir = 0
        install.plat_name = self.plat_name
        install_lib = self.reinitialize_command(b'install_lib')
        install_lib.compile = 0
        install_lib.optimize = 0
        if self.distribution.has_ext_modules():
            target_version = self.target_version
            if not target_version:
                target_version = sys.version[0:3]
            plat_specifier = b'.%s-%s' % (self.plat_name, target_version)
            build = self.get_finalized_command(b'build')
            build.build_lib = os.path.join(build.build_base, b'lib' + plat_specifier)
        for key in (b'purelib', b'platlib', b'headers', b'scripts', b'data'):
            value = string.upper(key)
            if key == b'headers':
                value = value + b'/Include/$dist_name'
            setattr(install, b'install_' + key, value)

        log.info(b'installing to %s', self.bdist_dir)
        install.ensure_finalized()
        sys.path.insert(0, os.path.join(self.bdist_dir, b'PURELIB'))
        install.run()
        del sys.path[0]
        from tempfile import mktemp
        archive_basename = mktemp()
        fullname = self.distribution.get_fullname()
        arcname = self.make_archive(archive_basename, b'zip', root_dir=self.bdist_dir)
        self.create_exe(arcname, fullname, self.bitmap)
        if self.distribution.has_ext_modules():
            pyversion = get_python_version()
        else:
            pyversion = b'any'
        self.distribution.dist_files.append((b'bdist_wininst', pyversion,
         self.get_installer_filename(fullname)))
        log.debug(b"removing temporary file '%s'", arcname)
        os.remove(arcname)
        if not self.keep_temp:
            remove_tree(self.bdist_dir, dry_run=self.dry_run)
        return

    def get_inidata(self):
        lines = []
        metadata = self.distribution.metadata
        lines.append(b'[metadata]')
        info = (metadata.long_description or b'') + b'\n'

        def escape(s):
            return string.replace(s, b'\n', b'\\n')

        for name in [5, 6, 7, 8, 
         9, 10, 11, 12]:
            data = getattr(metadata, name, b'')
            if data:
                info = info + b'\n    %s: %s' % (
                 string.capitalize(name), escape(data))
                lines.append(b'%s=%s' % (name, escape(data)))

        lines.append(b'\n[Setup]')
        if self.install_script:
            lines.append(b'install_script=%s' % self.install_script)
        lines.append(b'info=%s' % escape(info))
        lines.append(b'target_compile=%d' % (not self.no_target_compile))
        lines.append(b'target_optimize=%d' % (not self.no_target_optimize))
        if self.target_version:
            lines.append(b'target_version=%s' % self.target_version)
        if self.user_access_control:
            lines.append(b'user_access_control=%s' % self.user_access_control)
        title = self.title or self.distribution.get_fullname()
        lines.append(b'title=%s' % escape(title))
        import time, distutils
        build_info = b'Built %s with distutils-%s' % (
         time.ctime(time.time()), distutils.__version__)
        lines.append(b'build_info=%s' % build_info)
        return string.join(lines, b'\n')

    def create_exe(self, arcname, fullname, bitmap=None):
        import struct
        self.mkpath(self.dist_dir)
        cfgdata = self.get_inidata()
        installer_name = self.get_installer_filename(fullname)
        self.announce(b'creating %s' % installer_name)
        if bitmap:
            bitmapdata = open(bitmap, b'rb').read()
            bitmaplen = len(bitmapdata)
        else:
            bitmaplen = 0
        file = open(installer_name, b'wb')
        file.write(self.get_exe_bytes())
        if bitmap:
            file.write(bitmapdata)
        try:
            unicode
        except NameError:
            pass

        if isinstance(cfgdata, unicode):
            cfgdata = cfgdata.encode(b'mbcs')
        cfgdata = cfgdata + b'\x00'
        if self.pre_install_script:
            script_data = open(self.pre_install_script, b'r').read()
            cfgdata = cfgdata + script_data + b'\n\x00'
        else:
            cfgdata = cfgdata + b'\x00'
        file.write(cfgdata)
        header = struct.pack(b'<iii', 305419899, len(cfgdata), bitmaplen)
        file.write(header)
        file.write(open(arcname, b'rb').read())
        return

    def get_installer_filename(self, fullname):
        if self.target_version:
            installer_name = os.path.join(self.dist_dir, b'%s.%s-py%s.exe' % (
             fullname, self.plat_name, self.target_version))
        else:
            installer_name = os.path.join(self.dist_dir, b'%s.%s.exe' % (fullname, self.plat_name))
        return installer_name

    def get_exe_bytes(self):
        from distutils.msvccompiler import get_build_version
        cur_version = get_python_version()
        if self.target_version and self.target_version != cur_version:
            if self.target_version > cur_version:
                bv = get_build_version()
            elif self.target_version < b'2.4':
                bv = 6.0
            else:
                bv = 7.1
        else:
            bv = get_build_version()
        directory = os.path.dirname(__file__)
        if self.plat_name != b'win32' and self.plat_name[:3] == b'win':
            sfix = self.plat_name[3:]
        else:
            sfix = b''
        filename = os.path.join(directory, b'wininst-%.1f%s.exe' % (bv, sfix))
        f = open(filename, b'rb')
        try:
            return f.read()
        finally:
            f.close()

        return
