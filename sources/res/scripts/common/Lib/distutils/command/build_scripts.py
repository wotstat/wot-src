__revision__ = b'$Id$'
import os, re
from stat import ST_MODE
from distutils.core import Command
from distutils.dep_util import newer
from distutils.util import convert_path
from distutils import log
first_line_re = re.compile(b'^#!.*python[0-9.]*([ \t].*)?$')

class build_scripts(Command):
    description = b'"build" scripts (copy and fixup #! line)'
    user_options = [
     (b'build-dir=', b'd', b'directory to "build" (copy) to'),
     (b'force', b'f', b'forcibly build everything (ignore file timestamps'),
     (b'executable=', b'e', b'specify final destination interpreter path')]
    boolean_options = [
     b'force']

    def initialize_options(self):
        self.build_dir = None
        self.scripts = None
        self.force = None
        self.executable = None
        self.outfiles = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'build', (b'build_scripts', b'build_dir'), (b'force', b'force'), (b'executable', b'executable'))
        self.scripts = self.distribution.scripts
        return

    def get_source_files(self):
        return self.scripts

    def run(self):
        if not self.scripts:
            return
        self.copy_scripts()
        return

    def copy_scripts(self):
        _sysconfig = __import__(b'sysconfig')
        self.mkpath(self.build_dir)
        outfiles = []
        for script in self.scripts:
            adjust = 0
            script = convert_path(script)
            outfile = os.path.join(self.build_dir, os.path.basename(script))
            outfiles.append(outfile)
            if not self.force and not newer(script, outfile):
                log.debug(b'not copying %s (up-to-date)', script)
                continue
            try:
                f = open(script, b'r')
            except IOError:
                if not self.dry_run:
                    raise
                f = None
            else:
                first_line = f.readline()
                if not first_line:
                    self.warn(b'%s is an empty file (skipping)' % script)
                    continue
                match = first_line_re.match(first_line)
                if match:
                    adjust = 1
                    post_interp = match.group(1) or b''
                if adjust:
                    log.info(b'copying and adjusting %s -> %s', script, self.build_dir)
                    if not self.dry_run:
                        outf = open(outfile, b'w')
                        if not _sysconfig.is_python_build():
                            outf.write(b'#!%s%s\n' % (
                             self.executable,
                             post_interp))
                        else:
                            outf.write(b'#!%s%s\n' % (
                             os.path.join(_sysconfig.get_config_var(b'BINDIR'), b'python%s%s' % (_sysconfig.get_config_var(b'VERSION'),
                              _sysconfig.get_config_var(b'EXE'))),
                             post_interp))
                        outf.writelines(f.readlines())
                        outf.close()
                    if f:
                        f.close()
                elif f:
                    f.close()
                self.copy_file(script, outfile)

        if os.name == b'posix':
            for file in outfiles:
                if self.dry_run:
                    log.info(b'changing mode of %s', file)
                else:
                    oldmode = os.stat(file)[ST_MODE] & 4095
                    newmode = (oldmode | 365) & 4095
                    if newmode != oldmode:
                        log.info(b'changing mode of %s from %o to %o', file, oldmode, newmode)
                        os.chmod(file, newmode)

        return
