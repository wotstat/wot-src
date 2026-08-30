__revision__ = b'$Id$'
import os
from sysconfig import get_python_version
from distutils.util import get_platform
from distutils.core import Command
from distutils.dir_util import remove_tree, ensure_relative
from distutils.errors import DistutilsPlatformError
from distutils import log

class bdist_dumb(Command):
    description = b'create a "dumb" built distribution'
    user_options = [
     (b'bdist-dir=', b'd', b'temporary directory for creating the distribution'),
     (
      b'plat-name=', b'p',
      b'platform name to embed in generated filenames (default: %s)' % get_platform()),
     (b'format=', b'f', b'archive format to create (tar, ztar, gztar, zip)'),
     (
      b'keep-temp', b'k',
      b'keep the pseudo-installation tree around after ' + b'creating the distribution archive'),
     (b'dist-dir=', b'd', b'directory to put final built distributions in'),
     (b'skip-build', None, b'skip rebuilding everything (for testing/debugging)'),
     (b'relative', None, b'build the archive using relative paths (default: false)'),
     (b'owner=', b'u', b'Owner name used when creating a tar file [default: current user]'),
     (b'group=', b'g', b'Group name used when creating a tar file [default: current group]')]
    boolean_options = [
     b'keep-temp', b'skip-build', b'relative']
    default_format = {b'posix': b'gztar', b'nt': b'zip', 
       b'os2': b'zip'}

    def initialize_options(self):
        self.bdist_dir = None
        self.plat_name = None
        self.format = None
        self.keep_temp = 0
        self.dist_dir = None
        self.skip_build = None
        self.relative = 0
        self.owner = None
        self.group = None
        return

    def finalize_options(self):
        if self.bdist_dir is None:
            bdist_base = self.get_finalized_command(b'bdist').bdist_base
            self.bdist_dir = os.path.join(bdist_base, b'dumb')
        if self.format is None:
            try:
                self.format = self.default_format[os.name]
            except KeyError:
                raise DistutilsPlatformError, (b"don't know how to create dumb built distributions " + b'on platform %s') % os.name

        self.set_undefined_options(b'bdist', (b'dist_dir', b'dist_dir'), (b'plat_name', b'plat_name'), (b'skip_build', b'skip_build'))
        return

    def run(self):
        if not self.skip_build:
            self.run_command(b'build')
        install = self.reinitialize_command(b'install', reinit_subcommands=1)
        install.root = self.bdist_dir
        install.skip_build = self.skip_build
        install.warn_dir = 0
        log.info(b'installing to %s' % self.bdist_dir)
        self.run_command(b'install')
        archive_basename = b'%s.%s' % (self.distribution.get_fullname(),
         self.plat_name)
        if os.name == b'os2':
            archive_basename = archive_basename.replace(b':', b'-')
        pseudoinstall_root = os.path.join(self.dist_dir, archive_basename)
        if not self.relative:
            archive_root = self.bdist_dir
        elif self.distribution.has_ext_modules() and install.install_base != install.install_platbase:
            raise DistutilsPlatformError, b"can't make a dumb built distribution where base and platbase are different (%s, %s)" % (
             repr(install.install_base),
             repr(install.install_platbase))
        else:
            archive_root = os.path.join(self.bdist_dir, ensure_relative(install.install_base))
        filename = self.make_archive(pseudoinstall_root, self.format, root_dir=archive_root, owner=self.owner, group=self.group)
        if self.distribution.has_ext_modules():
            pyversion = get_python_version()
        else:
            pyversion = b'any'
        self.distribution.dist_files.append((b'bdist_dumb', pyversion,
         filename))
        if not self.keep_temp:
            remove_tree(self.bdist_dir, dry_run=self.dry_run)
        return
