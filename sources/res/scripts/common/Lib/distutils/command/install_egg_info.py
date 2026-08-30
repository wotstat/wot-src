from distutils.cmd import Command
from distutils import log, dir_util
import os, sys, re

class install_egg_info(Command):
    description = b"Install package's PKG-INFO metadata as an .egg-info file"
    user_options = [
     (b'install-dir=', b'd', b'directory to install to')]

    def initialize_options(self):
        self.install_dir = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'install_lib', (b'install_dir', b'install_dir'))
        basename = b'%s-%s-py%s.egg-info' % (
         to_filename(safe_name(self.distribution.get_name())),
         to_filename(safe_version(self.distribution.get_version())),
         sys.version[:3])
        self.target = os.path.join(self.install_dir, basename)
        self.outputs = [self.target]
        return

    def run(self):
        target = self.target
        if os.path.isdir(target) and not os.path.islink(target):
            dir_util.remove_tree(target, dry_run=self.dry_run)
        elif os.path.exists(target):
            self.execute(os.unlink, (self.target,), b'Removing ' + target)
        elif not os.path.isdir(self.install_dir):
            self.execute(os.makedirs, (self.install_dir,), b'Creating ' + self.install_dir)
        log.info(b'Writing %s', target)
        if not self.dry_run:
            f = open(target, b'w')
            self.distribution.metadata.write_pkg_file(f)
            f.close()
        return

    def get_outputs(self):
        return self.outputs


def safe_name(name):
    return re.sub(b'[^A-Za-z0-9.]+', b'-', name)


def safe_version(version):
    version = version.replace(b' ', b'.')
    return re.sub(b'[^A-Za-z0-9.]+', b'-', version)


def to_filename(name):
    return name.replace(b'-', b'_')
