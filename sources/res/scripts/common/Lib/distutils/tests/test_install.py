import os, sys, unittest, site
from test.test_support import captured_stdout, run_unittest
from distutils import sysconfig
from distutils.command.install import install
from distutils.command import install as install_module
from distutils.command.build_ext import build_ext
from distutils.command.install import INSTALL_SCHEMES
from distutils.core import Distribution
from distutils.errors import DistutilsOptionError
from distutils.extension import Extension
from distutils.tests import support

def _make_ext_name(modname):
    if os.name == b'nt' and sys.executable.endswith(b'_d.exe'):
        modname += b'_d'
    return modname + sysconfig.get_config_var(b'SO')


class InstallTestCase(support.TempdirManager, support.EnvironGuard, support.LoggingSilencer, unittest.TestCase):

    def test_home_installation_scheme(self):
        builddir = self.mkdtemp()
        destination = os.path.join(builddir, b'installation')
        dist = Distribution({b'name': b'foopkg'})
        dist.script_name = os.path.join(builddir, b'setup.py')
        dist.command_obj[b'build'] = support.DummyCommand(build_base=builddir, build_lib=os.path.join(builddir, b'lib'))
        cmd = install(dist)
        cmd.home = destination
        cmd.ensure_finalized()
        self.assertEqual(cmd.install_base, destination)
        self.assertEqual(cmd.install_platbase, destination)

        def check_path(got, expected):
            got = os.path.normpath(got)
            expected = os.path.normpath(expected)
            self.assertEqual(got, expected)
            return

        libdir = os.path.join(destination, b'lib', b'python')
        check_path(cmd.install_lib, libdir)
        check_path(cmd.install_platlib, libdir)
        check_path(cmd.install_purelib, libdir)
        check_path(cmd.install_headers, os.path.join(destination, b'include', b'python', b'foopkg'))
        check_path(cmd.install_scripts, os.path.join(destination, b'bin'))
        check_path(cmd.install_data, destination)
        return

    @unittest.skipIf(sys.version < b'2.6', b'site.USER_SITE was introduced in 2.6')
    def test_user_site(self):
        self.old_user_base = site.USER_BASE
        self.old_user_site = site.USER_SITE
        self.tmpdir = self.mkdtemp()
        self.user_base = os.path.join(self.tmpdir, b'B')
        self.user_site = os.path.join(self.tmpdir, b'S')
        site.USER_BASE = self.user_base
        site.USER_SITE = self.user_site
        install_module.USER_BASE = self.user_base
        install_module.USER_SITE = self.user_site

        def _expanduser(path):
            return self.tmpdir

        self.old_expand = os.path.expanduser
        os.path.expanduser = _expanduser

        def cleanup():
            site.USER_BASE = self.old_user_base
            site.USER_SITE = self.old_user_site
            install_module.USER_BASE = self.old_user_base
            install_module.USER_SITE = self.old_user_site
            os.path.expanduser = self.old_expand
            return

        self.addCleanup(cleanup)
        for key in (b'nt_user', b'unix_user', b'os2_home'):
            self.assertIn(key, INSTALL_SCHEMES)

        dist = Distribution({b'name': b'xx'})
        cmd = install(dist)
        options = [name for name, short, lable in cmd.user_options]
        self.assertIn(b'user', options)
        cmd.user = 1
        self.assertFalse(os.path.exists(self.user_base))
        self.assertFalse(os.path.exists(self.user_site))
        cmd.ensure_finalized()
        self.assertTrue(os.path.exists(self.user_base))
        self.assertTrue(os.path.exists(self.user_site))
        self.assertIn(b'userbase', cmd.config_vars)
        self.assertIn(b'usersite', cmd.config_vars)
        return

    def test_handle_extra_path(self):
        dist = Distribution({b'name': b'xx', b'extra_path': b'path,dirs'})
        cmd = install(dist)
        cmd.handle_extra_path()
        self.assertEqual(cmd.extra_path, [b'path', b'dirs'])
        self.assertEqual(cmd.extra_dirs, b'dirs')
        self.assertEqual(cmd.path_file, b'path')
        cmd.extra_path = [
         b'path']
        cmd.handle_extra_path()
        self.assertEqual(cmd.extra_path, [b'path'])
        self.assertEqual(cmd.extra_dirs, b'path')
        self.assertEqual(cmd.path_file, b'path')
        dist.extra_path = cmd.extra_path = None
        cmd.handle_extra_path()
        self.assertEqual(cmd.extra_path, None)
        self.assertEqual(cmd.extra_dirs, b'')
        self.assertEqual(cmd.path_file, None)
        cmd.extra_path = b'path,dirs,again'
        self.assertRaises(DistutilsOptionError, cmd.handle_extra_path)
        return

    def test_finalize_options(self):
        dist = Distribution({b'name': b'xx'})
        cmd = install(dist)
        cmd.prefix = b'prefix'
        cmd.install_base = b'base'
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)
        cmd.install_base = None
        cmd.home = b'home'
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)
        cmd.prefix = None
        cmd.user = b'user'
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)
        return

    def test_record(self):
        install_dir = self.mkdtemp()
        project_dir, dist = self.create_dist(py_modules=[b'hello'], scripts=[
         b'sayhi'])
        os.chdir(project_dir)
        self.write_file(b'hello.py', b"def main(): print 'o hai'")
        self.write_file(b'sayhi', b'from hello import main; main()')
        cmd = install(dist)
        dist.command_obj[b'install'] = cmd
        cmd.root = install_dir
        cmd.record = os.path.join(project_dir, b'filelist')
        cmd.ensure_finalized()
        cmd.run()
        f = open(cmd.record)
        try:
            content = f.read()
        finally:
            f.close()

        found = [os.path.basename(line) for line in content.splitlines()]
        expected = [b'hello.py', b'hello.pyc', b'sayhi',
         b'UNKNOWN-0.0.0-py%s.%s.egg-info' % sys.version_info[:2]]
        self.assertEqual(found, expected)
        return

    def test_record_extensions(self):
        install_dir = self.mkdtemp()
        project_dir, dist = self.create_dist(ext_modules=[
         Extension(b'xx', [b'xxmodule.c'])])
        os.chdir(project_dir)
        support.copy_xxmodule_c(project_dir)
        buildextcmd = build_ext(dist)
        support.fixup_build_ext(buildextcmd)
        buildextcmd.ensure_finalized()
        cmd = install(dist)
        dist.command_obj[b'install'] = cmd
        dist.command_obj[b'build_ext'] = buildextcmd
        cmd.root = install_dir
        cmd.record = os.path.join(project_dir, b'filelist')
        cmd.ensure_finalized()
        cmd.run()
        f = open(cmd.record)
        try:
            content = f.read()
        finally:
            f.close()

        found = [os.path.basename(line) for line in content.splitlines()]
        expected = [_make_ext_name(b'xx'),
         b'UNKNOWN-0.0.0-py%s.%s.egg-info' % sys.version_info[:2]]
        self.assertEqual(found, expected)
        return

    def test_debug_mode(self):
        old_logs_len = len(self.logs)
        install_module.DEBUG = True
        try:
            with captured_stdout():
                self.test_record()
        finally:
            install_module.DEBUG = False

        self.assertGreater(len(self.logs), old_logs_len)
        return


def test_suite():
    return unittest.makeSuite(InstallTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
