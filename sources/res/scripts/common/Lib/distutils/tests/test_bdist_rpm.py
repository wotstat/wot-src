import unittest, sys, os, tempfile, shutil
from test.test_support import run_unittest
try:
    import zlib
except ImportError:
    zlib = None

from distutils.core import Distribution
from distutils.command.bdist_rpm import bdist_rpm
from distutils.tests import support
from distutils.spawn import find_executable
from distutils import spawn
from distutils.errors import DistutilsExecError
SETUP_PY = b"from distutils.core import setup\nimport foo\n\nsetup(name='foo', version='0.1', py_modules=['foo'],\n      url='xxx', author='xxx', author_email='xxx')\n\n"

class BuildRpmTestCase(support.TempdirManager, support.EnvironGuard, support.LoggingSilencer, unittest.TestCase):

    def setUp(self):
        super(BuildRpmTestCase, self).setUp()
        self.old_location = os.getcwd()
        self.old_sys_argv = (sys.argv, sys.argv[:])
        return

    def tearDown(self):
        os.chdir(self.old_location)
        sys.argv = self.old_sys_argv[0]
        sys.argv[:] = self.old_sys_argv[1]
        super(BuildRpmTestCase, self).tearDown()
        return

    @unittest.skipUnless(sys.platform.startswith(b'linux'), b'spurious sdtout/stderr output under Mac OS X')
    @unittest.skipUnless(zlib, b'requires zlib')
    @unittest.skipIf(find_executable(b'rpm') is None, b'the rpm command is not found')
    @unittest.skipIf(find_executable(b'rpmbuild') is None, b'the rpmbuild command is not found')
    def test_quiet(self):
        tmp_dir = self.mkdtemp()
        os.environ[b'HOME'] = tmp_dir
        pkg_dir = os.path.join(tmp_dir, b'foo')
        os.mkdir(pkg_dir)
        self.write_file((pkg_dir, b'setup.py'), SETUP_PY)
        self.write_file((pkg_dir, b'foo.py'), b'#')
        self.write_file((pkg_dir, b'MANIFEST.in'), b'include foo.py')
        self.write_file((pkg_dir, b'README'), b'')
        dist = Distribution({b'name': b'foo', b'version': b'0.1', b'py_modules': [
                         b'foo'], 
           b'url': b'xxx', 
           b'author': b'xxx', b'author_email': b'xxx'})
        dist.script_name = b'setup.py'
        os.chdir(pkg_dir)
        sys.argv = [
         b'setup.py']
        cmd = bdist_rpm(dist)
        cmd.fix_python = True
        cmd.quiet = 1
        cmd.ensure_finalized()
        cmd.run()
        dist_created = os.listdir(os.path.join(pkg_dir, b'dist'))
        self.assertIn(b'foo-0.1-1.noarch.rpm', dist_created)
        self.assertIn((b'bdist_rpm', b'any', b'dist/foo-0.1-1.src.rpm'), dist.dist_files)
        self.assertIn((b'bdist_rpm', b'any', b'dist/foo-0.1-1.noarch.rpm'), dist.dist_files)
        return

    @unittest.skipUnless(sys.platform.startswith(b'linux'), b'spurious sdtout/stderr output under Mac OS X')
    @unittest.skipUnless(zlib, b'requires zlib')
    @unittest.skipIf(find_executable(b'rpm') is None, b'the rpm command is not found')
    @unittest.skipIf(find_executable(b'rpmbuild') is None, b'the rpmbuild command is not found')
    def test_no_optimize_flag(self):
        tmp_dir = self.mkdtemp()
        os.environ[b'HOME'] = tmp_dir
        pkg_dir = os.path.join(tmp_dir, b'foo')
        os.mkdir(pkg_dir)
        self.write_file((pkg_dir, b'setup.py'), SETUP_PY)
        self.write_file((pkg_dir, b'foo.py'), b'#')
        self.write_file((pkg_dir, b'MANIFEST.in'), b'include foo.py')
        self.write_file((pkg_dir, b'README'), b'')
        dist = Distribution({b'name': b'foo', b'version': b'0.1', b'py_modules': [
                         b'foo'], 
           b'url': b'xxx', 
           b'author': b'xxx', b'author_email': b'xxx'})
        dist.script_name = b'setup.py'
        os.chdir(pkg_dir)
        sys.argv = [
         b'setup.py']
        cmd = bdist_rpm(dist)
        cmd.fix_python = True
        cmd.quiet = 1
        cmd.ensure_finalized()
        cmd.run()
        dist_created = os.listdir(os.path.join(pkg_dir, b'dist'))
        self.assertIn(b'foo-0.1-1.noarch.rpm', dist_created)
        self.assertIn((b'bdist_rpm', b'any', b'dist/foo-0.1-1.src.rpm'), dist.dist_files)
        self.assertIn((b'bdist_rpm', b'any', b'dist/foo-0.1-1.noarch.rpm'), dist.dist_files)
        os.remove(os.path.join(pkg_dir, b'dist', b'foo-0.1-1.noarch.rpm'))
        return


def test_suite():
    return unittest.makeSuite(BuildRpmTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
