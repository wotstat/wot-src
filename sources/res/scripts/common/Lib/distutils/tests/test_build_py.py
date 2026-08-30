import os, sys, StringIO, unittest
from distutils.command.build_py import build_py
from distutils.core import Distribution
from distutils.errors import DistutilsFileError
from distutils.tests import support
from test.test_support import run_unittest

class BuildPyTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_package_data(self):
        sources = self.mkdtemp()
        f = open(os.path.join(sources, b'__init__.py'), b'w')
        try:
            f.write(b'# Pretend this is a package.')
        finally:
            f.close()

        f = open(os.path.join(sources, b'README.txt'), b'w')
        try:
            f.write(b'Info about this package')
        finally:
            f.close()

        destination = self.mkdtemp()
        dist = Distribution({b'packages': [b'pkg'], b'package_dir': {b'pkg': sources}})
        dist.script_name = os.path.join(sources, b'setup.py')
        dist.command_obj[b'build'] = support.DummyCommand(force=0, build_lib=destination)
        dist.packages = [b'pkg']
        dist.package_data = {b'pkg': [b'README.txt']}
        dist.package_dir = {b'pkg': sources}
        cmd = build_py(dist)
        cmd.compile = 1
        cmd.ensure_finalized()
        self.assertEqual(cmd.package_data, dist.package_data)
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 3)
        pkgdest = os.path.join(destination, b'pkg')
        files = os.listdir(pkgdest)
        self.assertIn(b'__init__.py', files)
        self.assertIn(b'README.txt', files)
        if sys.dont_write_bytecode:
            self.assertNotIn(b'__init__.pyc', files)
        else:
            self.assertIn(b'__init__.pyc', files)
        return

    def test_empty_package_dir(self):
        cwd = os.getcwd()
        sources = self.mkdtemp()
        open(os.path.join(sources, b'__init__.py'), b'w').close()
        testdir = os.path.join(sources, b'doc')
        os.mkdir(testdir)
        open(os.path.join(testdir, b'testfile'), b'w').close()
        os.chdir(sources)
        old_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()
        try:
            dist = Distribution({b'packages': [b'pkg'], b'package_dir': {b'pkg': b''}, b'package_data': {b'pkg': [b'doc/*']}})
            dist.script_name = os.path.join(sources, b'setup.py')
            dist.script_args = [b'build']
            dist.parse_command_line()
            try:
                dist.run_commands()
            except DistutilsFileError:
                self.fail(b"failed package_data test when package_dir is ''")

        finally:
            os.chdir(cwd)
            sys.stdout = old_stdout

        return

    def test_dir_in_package_data(self):
        sources = self.mkdtemp()
        pkg_dir = os.path.join(sources, b'pkg')
        os.mkdir(pkg_dir)
        open(os.path.join(pkg_dir, b'__init__.py'), b'w').close()
        docdir = os.path.join(pkg_dir, b'doc')
        os.mkdir(docdir)
        open(os.path.join(docdir, b'testfile'), b'w').close()
        os.mkdir(os.path.join(docdir, b'otherdir'))
        os.chdir(sources)
        dist = Distribution({b'packages': [b'pkg'], b'package_data': {b'pkg': [b'doc/*']}})
        dist.script_name = os.path.join(sources, b'setup.py')
        dist.script_args = [b'build']
        dist.parse_command_line()
        try:
            dist.run_commands()
        except DistutilsFileError:
            self.fail(b'failed package_data when data dir includes a dir')

        return

    def test_dont_write_bytecode(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_py(dist)
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
    return unittest.makeSuite(BuildPyTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
