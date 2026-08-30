import os, test, unittest, shutil, subprocess, sys, textwrap
from distutils import sysconfig
from distutils.ccompiler import get_default_compiler
from distutils.tests import support
from test.test_support import TESTFN, swap_item

class SysconfigTestCase(support.EnvironGuard, unittest.TestCase):

    def setUp(self):
        super(SysconfigTestCase, self).setUp()
        self.makefile = None
        return

    def tearDown(self):
        if self.makefile is not None:
            os.unlink(self.makefile)
        self.cleanup_testfn()
        super(SysconfigTestCase, self).tearDown()
        return

    def cleanup_testfn(self):
        path = test.test_support.TESTFN
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        return

    def test_get_python_lib(self):
        lib_dir = sysconfig.get_python_lib()
        self.assertNotEqual(sysconfig.get_python_lib(), sysconfig.get_python_lib(prefix=TESTFN))
        _sysconfig = __import__(b'sysconfig')
        res = sysconfig.get_python_lib(True, True)
        self.assertEqual(_sysconfig.get_path(b'platstdlib'), res)
        return

    def test_get_python_inc(self):
        inc_dir = sysconfig.get_python_inc()
        self.assertTrue(os.path.isdir(inc_dir), inc_dir)
        python_h = os.path.join(inc_dir, b'Python.h')
        self.assertTrue(os.path.isfile(python_h), python_h)
        return

    def customize_compiler(self):

        class compiler:
            compiler_type = b'unix'

            def set_executables(self, **kw):
                self.exes = kw
                return

        sysconfig_vars = {b'AR': b'sc_ar', 
           b'CC': b'sc_cc', 
           b'CXX': b'sc_cxx', 
           b'ARFLAGS': b'--sc-arflags', 
           b'CFLAGS': b'--sc-cflags', 
           b'CCSHARED': b'--sc-ccshared', 
           b'LDSHARED': b'sc_ldshared', 
           b'SO': b'sc_shutil_suffix'}
        comp = compiler()
        old_vars = dict(sysconfig._config_vars)
        try:
            sysconfig._config_vars[b'CUSTOMIZED_OSX_COMPILER'] = b'True'
            for key, value in sysconfig_vars.items():
                sysconfig._config_vars[key] = value

            sysconfig.customize_compiler(comp)
        finally:
            sysconfig._config_vars.clear()
            sysconfig._config_vars.update(old_vars)

        return comp

    @unittest.skipUnless(get_default_compiler() == b'unix', b'not testing if default compiler is not unix')
    def test_customize_compiler(self):
        sysconfig.get_config_vars()
        os.environ[b'AR'] = b'env_ar'
        os.environ[b'CC'] = b'env_cc'
        os.environ[b'CPP'] = b'env_cpp'
        os.environ[b'CXX'] = b'env_cxx --env-cxx-flags'
        os.environ[b'LDSHARED'] = b'env_ldshared'
        os.environ[b'LDFLAGS'] = b'--env-ldflags'
        os.environ[b'ARFLAGS'] = b'--env-arflags'
        os.environ[b'CFLAGS'] = b'--env-cflags'
        os.environ[b'CPPFLAGS'] = b'--env-cppflags'
        comp = self.customize_compiler()
        self.assertEqual(comp.exes[b'archiver'], b'env_ar --env-arflags')
        self.assertEqual(comp.exes[b'preprocessor'], b'env_cpp --env-cppflags')
        self.assertEqual(comp.exes[b'compiler'], b'env_cc --sc-cflags --env-cflags --env-cppflags')
        self.assertEqual(comp.exes[b'compiler_so'], b'env_cc --sc-cflags --env-cflags --env-cppflags --sc-ccshared')
        self.assertEqual(comp.exes[b'compiler_cxx'], b'env_cxx --env-cxx-flags')
        self.assertEqual(comp.exes[b'linker_exe'], b'env_cc')
        self.assertEqual(comp.exes[b'linker_so'], b'env_ldshared --env-ldflags --env-cflags --env-cppflags')
        self.assertEqual(comp.shared_lib_extension, b'sc_shutil_suffix')
        del os.environ[b'AR']
        del os.environ[b'CC']
        del os.environ[b'CPP']
        del os.environ[b'CXX']
        del os.environ[b'LDSHARED']
        del os.environ[b'LDFLAGS']
        del os.environ[b'ARFLAGS']
        del os.environ[b'CFLAGS']
        del os.environ[b'CPPFLAGS']
        comp = self.customize_compiler()
        self.assertEqual(comp.exes[b'archiver'], b'sc_ar --sc-arflags')
        self.assertEqual(comp.exes[b'preprocessor'], b'sc_cc -E')
        self.assertEqual(comp.exes[b'compiler'], b'sc_cc --sc-cflags')
        self.assertEqual(comp.exes[b'compiler_so'], b'sc_cc --sc-cflags --sc-ccshared')
        self.assertEqual(comp.exes[b'compiler_cxx'], b'sc_cxx')
        self.assertEqual(comp.exes[b'linker_exe'], b'sc_cc')
        self.assertEqual(comp.exes[b'linker_so'], b'sc_ldshared')
        self.assertEqual(comp.shared_lib_extension, b'sc_shutil_suffix')
        return

    def test_parse_makefile_base(self):
        self.makefile = test.test_support.TESTFN
        fd = open(self.makefile, b'w')
        try:
            fd.write(b"CONFIG_ARGS=  '--arg1=optarg1' 'ENV=LIB'\n")
            fd.write(b'VAR=$OTHER\nOTHER=foo')
        finally:
            fd.close()

        d = sysconfig.parse_makefile(self.makefile)
        self.assertEqual(d, {b'CONFIG_ARGS': b"'--arg1=optarg1' 'ENV=LIB'", b'OTHER': b'foo'})
        return

    def test_parse_makefile_literal_dollar(self):
        self.makefile = test.test_support.TESTFN
        fd = open(self.makefile, b'w')
        try:
            fd.write(b"CONFIG_ARGS=  '--arg1=optarg1' 'ENV=\\$$LIB'\n")
            fd.write(b'VAR=$OTHER\nOTHER=foo')
        finally:
            fd.close()

        d = sysconfig.parse_makefile(self.makefile)
        self.assertEqual(d, {b'CONFIG_ARGS': b"'--arg1=optarg1' 'ENV=\\$LIB'", b'OTHER': b'foo'})
        return

    def test_sysconfig_module(self):
        import sysconfig as global_sysconfig
        self.assertEqual(global_sysconfig.get_config_var(b'CFLAGS'), sysconfig.get_config_var(b'CFLAGS'))
        self.assertEqual(global_sysconfig.get_config_var(b'LDFLAGS'), sysconfig.get_config_var(b'LDFLAGS'))
        return

    @unittest.skipIf(sysconfig.get_config_var(b'CUSTOMIZED_OSX_COMPILER'), b'compiler flags customized')
    def test_sysconfig_compiler_vars(self):
        import sysconfig as global_sysconfig
        if sysconfig.get_config_var(b'CUSTOMIZED_OSX_COMPILER'):
            self.skipTest(b'compiler flags customized')
        self.assertEqual(global_sysconfig.get_config_var(b'LDSHARED'), sysconfig.get_config_var(b'LDSHARED'))
        self.assertEqual(global_sysconfig.get_config_var(b'CC'), sysconfig.get_config_var(b'CC'))
        return

    def test_customize_compiler_before_get_config_vars(self):
        with open(TESTFN, b'w') as f:
            f.writelines(textwrap.dedent(b"                from distutils.core import Distribution\n                config = Distribution().get_command_obj('config')\n                # try_compile may pass or it may fail if no compiler\n                # is found but it should not raise an exception.\n                rc = config.try_compile('int x;')\n                "))
        p = subprocess.Popen([str(sys.executable), TESTFN], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        outs, errs = p.communicate()
        self.assertEqual(0, p.returncode, b'Subprocess failed: ' + outs)
        return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SysconfigTestCase))
    return suite


if __name__ == b'__main__':
    test.test_support.run_unittest(test_suite())
