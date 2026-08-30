import unittest, os.path, sys
from test import test_support
from ctypes import *
from ctypes.util import find_library
from ctypes.test import is_resource_enabled
if sys.platform == b'win32':
    lib_gl = find_library(b'OpenGL32')
    lib_glu = find_library(b'Glu32')
    lib_gle = None
elif sys.platform == b'darwin':
    lib_gl = lib_glu = find_library(b'OpenGL')
    lib_gle = None
else:
    lib_gl = find_library(b'GL')
    lib_glu = find_library(b'GLU')
    lib_gle = find_library(b'gle')
if is_resource_enabled(b'printing'):
    if lib_gl or lib_glu or lib_gle:
        print b'OpenGL libraries:'
        for item in ((b'GL', lib_gl),
         (
          b'GLU', lib_glu),
         (
          b'gle', lib_gle)):
            print b'\t', item

class Test_OpenGL_libs(unittest.TestCase):

    def setUp(self):
        self.gl = self.glu = self.gle = None
        if lib_gl:
            try:
                self.gl = CDLL(lib_gl, mode=RTLD_GLOBAL)
            except OSError:
                pass

        if lib_glu:
            try:
                self.glu = CDLL(lib_glu, RTLD_GLOBAL)
            except OSError:
                pass

        if lib_gle:
            try:
                self.gle = CDLL(lib_gle)
            except OSError:
                pass

        return

    def tearDown(self):
        self.gl = self.glu = self.gle = None
        return

    @unittest.skipUnless(lib_gl, b'lib_gl not available')
    def test_gl(self):
        if self.gl:
            self.gl.glClearIndex
        return

    @unittest.skipUnless(lib_glu, b'lib_glu not available')
    def test_glu(self):
        if self.glu:
            self.glu.gluBeginCurve
        return

    @unittest.skipUnless(lib_gle, b'lib_gle not available')
    def test_gle(self):
        if self.gle:
            self.gle.gleGetJoinStyle
        return

    def test_shell_injection(self):
        result = find_library(b'; echo Hello shell > ' + test_support.TESTFN)
        self.assertFalse(os.path.lexists(test_support.TESTFN))
        self.assertIsNone(result)
        return


if __name__ == b'__main__':
    unittest.main()
