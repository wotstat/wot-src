__revision__ = b'$Id$'
import os, sys
from distutils.core import Command
from distutils.errors import DistutilsOptionError
if hasattr(os, b'extsep'):
    PYTHON_SOURCE_EXTENSION = os.extsep + b'py'
else:
    PYTHON_SOURCE_EXTENSION = b'.py'

class install_lib(Command):
    description = b'install all Python modules (extensions and pure Python)'
    user_options = [
     30, 
     31, 
     32, 
     33, 
     35, 
     36, 
     37]
    boolean_options = [
     b'force', b'compile', b'skip-build']
    negative_opt = {b'no-compile': b'compile'}

    def initialize_options(self):
        self.install_dir = None
        self.build_dir = None
        self.force = 0
        self.compile = None
        self.optimize = None
        self.skip_build = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'install', (b'build_lib', b'build_dir'), (b'install_lib', b'install_dir'), (b'force', b'force'), (b'compile', b'compile'), (b'optimize', b'optimize'), (b'skip_build', b'skip_build'))
        if self.compile is None:
            self.compile = 1
        if self.optimize is None:
            self.optimize = 0
        if not isinstance(self.optimize, int):
            try:
                self.optimize = int(self.optimize)
                assert not self.optimize not in (0, 1, 2)
            except (ValueError, AssertionError):
                raise DistutilsOptionError, b'optimize must be 0, 1, or 2'

        return

    def run(self):
        self.build()
        outfiles = self.install()
        if outfiles is not None and self.distribution.has_pure_modules():
            self.byte_compile(outfiles)
        return

    def build(self):
        if not self.skip_build:
            if self.distribution.has_pure_modules():
                self.run_command(b'build_py')
            if self.distribution.has_ext_modules():
                self.run_command(b'build_ext')
        return

    def install(self):
        if os.path.isdir(self.build_dir):
            outfiles = self.copy_tree(self.build_dir, self.install_dir)
        else:
            self.warn(b"'%s' does not exist -- no Python modules to install" % self.build_dir)
            return
        return outfiles

    def byte_compile(self, files):
        if sys.dont_write_bytecode:
            self.warn(b'byte-compiling is disabled, skipping.')
            return
        from distutils.util import byte_compile
        install_root = self.get_finalized_command(b'install').root
        if self.compile:
            byte_compile(files, optimize=0, force=self.force, prefix=install_root, dry_run=self.dry_run)
        if self.optimize > 0:
            byte_compile(files, optimize=self.optimize, force=self.force, prefix=install_root, verbose=self.verbose, dry_run=self.dry_run)
        return

    def _mutate_outputs(self, has_any, build_cmd, cmd_option, output_dir):
        if not has_any:
            return []
        build_cmd = self.get_finalized_command(build_cmd)
        build_files = build_cmd.get_outputs()
        build_dir = getattr(build_cmd, cmd_option)
        prefix_len = len(build_dir) + len(os.sep)
        outputs = []
        for file in build_files:
            outputs.append(os.path.join(output_dir, file[prefix_len:]))

        return outputs

    def _bytecode_filenames(self, py_filenames):
        bytecode_files = []
        for py_file in py_filenames:
            ext = os.path.splitext(os.path.normcase(py_file))[1]
            if ext != PYTHON_SOURCE_EXTENSION:
                continue
            if self.compile:
                bytecode_files.append(py_file + b'c')
            if self.optimize > 0:
                bytecode_files.append(py_file + b'o')

        return bytecode_files

    def get_outputs(self):
        pure_outputs = self._mutate_outputs(self.distribution.has_pure_modules(), b'build_py', b'build_lib', self.install_dir)
        if self.compile:
            bytecode_outputs = self._bytecode_filenames(pure_outputs)
        else:
            bytecode_outputs = []
        ext_outputs = self._mutate_outputs(self.distribution.has_ext_modules(), b'build_ext', b'build_lib', self.install_dir)
        return pure_outputs + bytecode_outputs + ext_outputs

    def get_inputs(self):
        inputs = []
        if self.distribution.has_pure_modules():
            build_py = self.get_finalized_command(b'build_py')
            inputs.extend(build_py.get_outputs())
        if self.distribution.has_ext_modules():
            build_ext = self.get_finalized_command(b'build_ext')
            inputs.extend(build_ext.get_outputs())
        return inputs
