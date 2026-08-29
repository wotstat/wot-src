import os, sys, unittest
from test.test_support import EnvironmentVarGuard, run_unittest
from distutils import sysconfig
from distutils.unixccompiler import UnixCCompiler

class UnixCCompilerTestCase(unittest.TestCase):

    def setUp(self):
        self._backup_platform = sys.platform
        self._backup_get_config_var = sysconfig.get_config_var

        class CompilerWrapper(UnixCCompiler):

            def rpath_foo(self):
                return self.runtime_library_dir_option(b'/foo')

        self.cc = CompilerWrapper()
        return

    def tearDown(self):
        sys.platform = self._backup_platform
        sysconfig.get_config_var = self._backup_get_config_var
        return

    @unittest.skipIf(sys.platform == b'win32', b"can't test on Windows")
    def test_runtime_libdir_option(self):
        sys.platform = b'darwin'
        self.assertEqual(self.cc.rpath_foo(), b'-L/foo')
        sys.platform = b'hp-ux'
        old_gcv = sysconfig.get_config_var

        def gcv(v):
            return b'xxx'

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), [b'+s', b'-L/foo'])

        def gcv(v):
            return b'gcc'

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), [b'-Wl,+s', b'-L/foo'])

        def gcv(v):
            return b'g++'

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), [b'-Wl,+s', b'-L/foo'])
        sysconfig.get_config_var = old_gcv
        sys.platform = b'irix646'
        self.assertEqual(self.cc.rpath_foo(), [b'-rpath', b'/foo'])
        sys.platform = b'osf1V5'
        self.assertEqual(self.cc.rpath_foo(), [b'-rpath', b'/foo'])
        sys.platform = b'bar'

        def gcv(v):
            if v == b'CC':
                return b'gcc'
            if v == b'GNULD':
                return b'yes'
            return

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), b'-Wl,-R/foo')
        sys.platform = b'bar'

        def gcv(v):
            if v == b'CC':
                return b'gcc'
            if v == b'GNULD':
                return b'no'
            return

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), b'-Wl,-R/foo')
        sys.platform = b'bar'

        def gcv(v):
            if v == b'CC':
                return b'x86_64-pc-linux-gnu-gcc-4.4.2'
            if v == b'GNULD':
                return b'yes'
            return

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), b'-Wl,-R/foo')
        sys.platform = b'bar'

        def gcv(v):
            if v == b'CC':
                return b'cc'
            if v == b'GNULD':
                return b'yes'
            return

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), b'-R/foo')
        sys.platform = b'bar'

        def gcv(v):
            if v == b'CC':
                return b'cc'
            if v == b'GNULD':
                return b'no'
            return

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), b'-R/foo')
        sys.platform = b'aix'

        def gcv(v):
            return b'xxx'

        sysconfig.get_config_var = gcv
        self.assertEqual(self.cc.rpath_foo(), b'-R/foo')
        return

    @unittest.skipUnless(sys.platform == b'darwin', b'test only relevant for OS X')
    def test_osx_cc_overrides_ldshared(self):

        def gcv(v):
            if v == b'LDSHARED':
                return b'gcc-4.2 -bundle -undefined dynamic_lookup '
            return b'gcc-4.2'

        sysconfig.get_config_var = gcv
        with EnvironmentVarGuard() as env:
            env[b'CC'] = b'my_cc'
            del env[b'LDSHARED']
            sysconfig.customize_compiler(self.cc)
        self.assertEqual(self.cc.linker_so[0], b'my_cc')
        return

    @unittest.skipUnless(sys.platform == b'darwin', b'test only relevant for OS X')
    def test_osx_explicit_ldshared(self):

        def gcv(v):
            if v == b'LDSHARED':
                return b'gcc-4.2 -bundle -undefined dynamic_lookup '
            return b'gcc-4.2'

        sysconfig.get_config_var = gcv
        with EnvironmentVarGuard() as env:
            env[b'CC'] = b'my_cc'
            env[b'LDSHARED'] = b'my_ld -bundle -dynamic'
            sysconfig.customize_compiler(self.cc)
        self.assertEqual(self.cc.linker_so[0], b'my_ld')
        return


def test_suite():
    return unittest.makeSuite(UnixCCompilerTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
