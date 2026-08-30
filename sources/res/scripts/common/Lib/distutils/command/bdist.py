__revision__ = b'$Id$'
import os
from distutils.util import get_platform
from distutils.core import Command
from distutils.errors import DistutilsPlatformError, DistutilsOptionError

def show_formats():
    from distutils.fancy_getopt import FancyGetopt
    formats = []
    for format in bdist.format_commands:
        formats.append((b'formats=' + format, None,
         bdist.format_command[format][1]))

    pretty_printer = FancyGetopt(formats)
    pretty_printer.print_help(b'List of available distribution formats:')
    return


class bdist(Command):
    description = b'create a built (binary) distribution'
    user_options = [
     (b'bdist-base=', b'b', b'temporary directory for creating built distributions'),
     (
      b'plat-name=', b'p',
      b'platform name to embed in generated filenames (default: %s)' % get_platform()),
     (b'formats=', None, b'formats for distribution (comma-separated list)'),
     (b'dist-dir=', b'd', b'directory to put final built distributions in [default: dist]'),
     (b'skip-build', None, b'skip rebuilding everything (for testing/debugging)'),
     (b'owner=', b'u', b'Owner name used when creating a tar file [default: current user]'),
     (b'group=', b'g', b'Group name used when creating a tar file [default: current group]')]
    boolean_options = [
     b'skip-build']
    help_options = [
     (
      b'help-formats', None,
      b'lists available distribution formats', show_formats)]
    no_format_option = (b'bdist_rpm',)
    default_format = {b'posix': b'gztar', b'nt': b'zip', 
       b'os2': b'zip'}
    format_commands = [
     28, 23, 29, 30, 31, 
     32, 25, 33]
    format_command = {b'rpm': (b'bdist_rpm', b'RPM distribution'), b'gztar': (b'bdist_dumb', b"gzip'ed tar file"), 
       b'bztar': (b'bdist_dumb', b"bzip2'ed tar file"), 
       b'ztar': (b'bdist_dumb', b'compressed tar file'), 
       b'tar': (b'bdist_dumb', b'tar file'), 
       b'wininst': (b'bdist_wininst', b'Windows executable installer'), 
       b'zip': (b'bdist_dumb', b'ZIP file'), 
       b'msi': (b'bdist_msi', b'Microsoft Installer')}

    def initialize_options(self):
        self.bdist_base = None
        self.plat_name = None
        self.formats = None
        self.dist_dir = None
        self.skip_build = 0
        self.group = None
        self.owner = None
        return

    def finalize_options(self):
        if self.plat_name is None:
            if self.skip_build:
                self.plat_name = get_platform()
            else:
                self.plat_name = self.get_finalized_command(b'build').plat_name
        if self.bdist_base is None:
            build_base = self.get_finalized_command(b'build').build_base
            self.bdist_base = os.path.join(build_base, b'bdist.' + self.plat_name)
        self.ensure_string_list(b'formats')
        if self.formats is None:
            try:
                self.formats = [
                 self.default_format[os.name]]
            except KeyError:
                raise DistutilsPlatformError, b"don't know how to create built distributions " + b'on platform %s' % os.name

        if self.dist_dir is None:
            self.dist_dir = b'dist'
        return

    def run(self):
        commands = []
        for format in self.formats:
            try:
                commands.append(self.format_command[format][0])
            except KeyError:
                raise DistutilsOptionError, b"invalid format '%s'" % format

        for i in range(len(self.formats)):
            cmd_name = commands[i]
            sub_cmd = self.reinitialize_command(cmd_name)
            if cmd_name not in self.no_format_option:
                sub_cmd.format = self.formats[i]
            if cmd_name == b'bdist_dumb':
                sub_cmd.owner = self.owner
                sub_cmd.group = self.group
            if cmd_name in commands[i + 1:]:
                sub_cmd.keep_temp = 1
            self.run_command(cmd_name)

        return
