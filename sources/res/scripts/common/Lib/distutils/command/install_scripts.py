__revision__ = b'$Id$'
import os
from distutils.core import Command
from distutils import log
from stat import ST_MODE

class install_scripts(Command):
    description = b'install scripts (Python or otherwise)'
    user_options = [
     (b'install-dir=', b'd', b'directory to install scripts to'),
     (b'build-dir=', b'b', b'build directory (where to install from)'),
     (b'force', b'f', b'force installation (overwrite existing files)'),
     (b'skip-build', None, b'skip the build steps')]
    boolean_options = [
     b'force', b'skip-build']

    def initialize_options(self):
        self.install_dir = None
        self.force = 0
        self.build_dir = None
        self.skip_build = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'build', (b'build_scripts', b'build_dir'))
        self.set_undefined_options(b'install', (b'install_scripts', b'install_dir'), (b'force', b'force'), (b'skip_build', b'skip_build'))
        return

    def run(self):
        if not self.skip_build:
            self.run_command(b'build_scripts')
        self.outfiles = self.copy_tree(self.build_dir, self.install_dir)
        if os.name == b'posix':
            for file in self.get_outputs():
                if self.dry_run:
                    log.info(b'changing mode of %s', file)
                else:
                    mode = (os.stat(file)[ST_MODE] | 365) & 4095
                    log.info(b'changing mode of %s to %o', file, mode)
                    os.chmod(file, mode)

        return

    def get_inputs(self):
        return self.distribution.scripts or []

    def get_outputs(self):
        return self.outfiles or []
