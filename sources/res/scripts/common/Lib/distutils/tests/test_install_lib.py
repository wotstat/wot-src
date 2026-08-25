import os, sys, unittest
from distutils.command.install_lib import install_lib
from distutils.extension import Extension
from distutils.tests import support
from distutils.errors import DistutilsOptionError
from test.test_support import run_unittest

class InstallLibTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def test_finalize_options(self):
        pkg_dir, dist = self.create_dist()
        cmd = install_lib(dist)
        cmd.finalize_options()
        self.assertEqual(cmd.compile, 1)
        self.assertEqual(cmd.optimize, 0)
        cmd.optimize = b'foo'
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)
        cmd.optimize = b'4'
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)
        cmd.optimize = b'2'
        cmd.finalize_options()
        self.assertEqual(cmd.optimize, 2)
        return

    def _setup_byte_compile(self):
        pkg_dir, dist = self.create_dist()
        cmd = install_lib(dist)
        cmd.compile = cmd.optimize = 1
        f = os.path.join(pkg_dir, b'foo.py')
        self.write_file(f, b'# python file')
        cmd.byte_compile([f])
        return pkg_dir

    @unittest.skipIf(sys.dont_write_bytecode, b'byte-compile not enabled')
    def test_byte_compile(self):
        pkg_dir = self._setup_byte_compile()
        if sys.flags.optimize < 1:
            self.assertTrue(os.path.exists(os.path.join(pkg_dir, b'foo.pyc')))
        else:
            self.assertTrue(os.path.exists(os.path.join(pkg_dir, b'foo.pyo')))
        return

    def test_get_outputs(self):
        pkg_dir, dist = self.create_dist()
        cmd = install_lib(dist)
        cmd.compile = cmd.optimize = 1
        cmd.install_dir = pkg_dir
        f = os.path.join(pkg_dir, b'foo.py')
        self.write_file(f, b'# python file')
        cmd.distribution.py_modules = [pkg_dir]
        cmd.distribution.ext_modules = [Extension(b'foo', [b'xxx'])]
        cmd.distribution.packages = [pkg_dir]
        cmd.distribution.script_name = b'setup.py'
        self.assertGreaterEqual(len(cmd.get_outputs()), 2)
        return

    def test_get_inputs(self):
        pkg_dir, dist = self.create_dist()
        cmd = install_lib(dist)
        cmd.compile = cmd.optimize = 1
        cmd.install_dir = pkg_dir
        f = os.path.join(pkg_dir, b'foo.py')
        self.write_file(f, b'# python file')
        cmd.distribution.py_modules = [pkg_dir]
        cmd.distribution.ext_modules = [Extension(b'foo', [b'xxx'])]
        cmd.distribution.packages = [pkg_dir]
        cmd.distribution.script_name = b'setup.py'
        self.assertEqual(len(cmd.get_inputs()), 2)
        return

    def test_dont_write_bytecode(self):
        pkg_dir, dist = self.create_dist()
        cmd = install_lib(dist)
        cmd.compile = 1
        cmd.optimize = 1
        old_dont_write_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            cmd.byte_compile([])
        finally:
            sys.dont_write_bytecode = old_dont_write_bytecode

        self.assertIn(b'byte-compiling is disabled', self.logs[0][1])
        return


def test_suite():
    return unittest.makeSuite(InstallLibTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
