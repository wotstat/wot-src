__revision__ = b'$Id$'
from distutils.core import Command

class install_headers(Command):
    description = b'install C/C++ header files'
    user_options = [
     (b'install-dir=', b'd', b'directory to install header files to'),
     (b'force', b'f', b'force installation (overwrite existing files)')]
    boolean_options = [
     b'force']

    def initialize_options(self):
        self.install_dir = None
        self.force = 0
        self.outfiles = []
        return

    def finalize_options(self):
        self.set_undefined_options(b'install', (b'install_headers', b'install_dir'), (b'force', b'force'))
        return

    def run(self):
        headers = self.distribution.headers
        if not headers:
            return
        self.mkpath(self.install_dir)
        for header in headers:
            out, _ = self.copy_file(header, self.install_dir)
            self.outfiles.append(out)

        return

    def get_inputs(self):
        return self.distribution.headers or []

    def get_outputs(self):
        return self.outfiles
