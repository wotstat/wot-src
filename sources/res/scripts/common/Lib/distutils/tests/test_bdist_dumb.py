import os, sys, zipfile, unittest
from test.test_support import run_unittest
try:
    import zlib
except ImportError:
    zlib = None

from distutils.core import Distribution
from distutils.command.bdist_dumb import bdist_dumb
from distutils.tests import support
SETUP_PY = b"from distutils.core import setup\nimport foo\n\nsetup(name='foo', version='0.1', py_modules=['foo'],\n      url='xxx', author='xxx', author_email='xxx')\n\n"

class BuildDumbTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def setUp(self):
        super(BuildDumbTestCase, self).setUp()
        self.old_location = os.getcwd()
        self.old_sys_argv = (sys.argv, sys.argv[:])
        return

    def tearDown(self):
        os.chdir(self.old_location)
        sys.argv = self.old_sys_argv[0]
        sys.argv[:] = self.old_sys_argv[1]
        super(BuildDumbTestCase, self).tearDown()
        return

    @unittest.skipUnless(zlib, b'requires zlib')
    def test_simple_built(self):
        tmp_dir = self.mkdtemp()
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
        cmd = bdist_dumb(dist)
        cmd.format = b'zip'
        cmd.ensure_finalized()
        cmd.run()
        dist_created = os.listdir(os.path.join(pkg_dir, b'dist'))
        base = b'%s.%s.zip' % (dist.get_fullname(), cmd.plat_name)
        if os.name == b'os2':
            base = base.replace(b':', b'-')
        self.assertEqual(dist_created, [base])
        fp = zipfile.ZipFile(os.path.join(b'dist', base))
        try:
            contents = fp.namelist()
        finally:
            fp.close()

        contents = sorted(filter(None, map(os.path.basename, contents)))
        wanted = [b'foo-0.1-py%s.%s.egg-info' % sys.version_info[:2], b'foo.py']
        if not sys.dont_write_bytecode:
            wanted.append(b'foo.pyc')
        self.assertEqual(contents, sorted(wanted))
        return

    def test_finalize_options(self):
        pkg_dir, dist = self.create_dist()
        os.chdir(pkg_dir)
        cmd = bdist_dumb(dist)
        self.assertEqual(cmd.bdist_dir, None)
        cmd.finalize_options()
        base = cmd.get_finalized_command(b'bdist').bdist_base
        self.assertEqual(cmd.bdist_dir, os.path.join(base, b'dumb'))
        default = cmd.default_format[os.name]
        self.assertEqual(cmd.format, default)
        return


def test_suite():
    return unittest.makeSuite(BuildDumbTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
