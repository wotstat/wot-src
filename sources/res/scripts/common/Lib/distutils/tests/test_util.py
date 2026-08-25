import os, sys, unittest
from test.test_support import run_unittest, swap_attr
from distutils.errors import DistutilsByteCompileError
from distutils.tests import support
from distutils import util
from distutils.util import byte_compile, grok_environment_error, check_environ, get_platform

class UtilTestCase(support.EnvironGuard, unittest.TestCase):

    def test_dont_write_bytecode(self):
        old_dont_write_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            self.assertRaises(DistutilsByteCompileError, byte_compile, [])
        finally:
            sys.dont_write_bytecode = old_dont_write_bytecode

        return

    def test_grok_environment_error(self):
        exc = IOError(b'Unable to find batch file')
        msg = grok_environment_error(exc)
        self.assertEqual(msg, b'error: Unable to find batch file')
        return

    def test_check_environ(self):
        util._environ_checked = 0
        os.environ.pop(b'HOME', None)
        check_environ()
        self.assertEqual(os.environ[b'PLAT'], get_platform())
        self.assertEqual(util._environ_checked, 1)
        return

    @unittest.skipUnless(os.name == b'posix', b'specific to posix')
    def test_check_environ_getpwuid(self):
        util._environ_checked = 0
        os.environ.pop(b'HOME', None)
        import pwd

        def mock_getpwuid(uid):
            return pwd.struct_passwd((None, None, None, None, None, b'/home/distutils', None))

        with swap_attr(pwd, b'getpwuid', mock_getpwuid):
            check_environ()
            self.assertEqual(os.environ[b'HOME'], b'/home/distutils')
        util._environ_checked = 0
        os.environ.pop(b'HOME', None)

        def getpwuid_err(uid):
            raise KeyError
            return

        with swap_attr(pwd, b'getpwuid', getpwuid_err):
            check_environ()
            self.assertNotIn(b'HOME', os.environ)
        return


def test_suite():
    return unittest.makeSuite(UtilTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
