from ctypes import *
from ctypes.test import requires
import unittest, sys
from test import test_support as support
import _ctypes_test

@unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
@unittest.skipUnless(sizeof(c_void_p) == sizeof(c_int), b'sizeof c_void_p and c_int differ')
class WindowsTestCase(unittest.TestCase):

    def test_callconv_1(self):
        IsWindow = windll.user32.IsWindow
        self.assertRaises(ValueError, IsWindow)
        self.assertEqual(0, IsWindow(0))
        self.assertRaises(ValueError, IsWindow, 0, 0, 0)
        return

    def test_callconv_2(self):
        IsWindow = cdll.user32.IsWindow
        self.assertRaises(ValueError, IsWindow, None)
        return


@unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
class FunctionCallTestCase(unittest.TestCase):

    @unittest.skipUnless(b'MSC' in sys.version, b'SEH only supported by MSC')
    @unittest.skipIf(sys.executable.endswith(b'_d.exe'), b'SEH not enabled in debug builds')
    def test_SEH(self):
        requires(b'SEH')
        self.assertRaises(WindowsError, windll.kernel32.GetModuleHandleA, 32)
        return

    def test_noargs(self):
        windll.user32.GetDesktopWindow()
        return


@unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
class ReturnStructSizesTestCase(unittest.TestCase):

    def test_sizes(self):
        dll = CDLL(_ctypes_test.__file__)
        for i in range(1, 11):
            fields = [(b'f%d' % f, c_char) for f in range(1, i + 1)]

            class S(Structure):
                _fields_ = fields

            f = getattr(dll, b'TestSize%d' % i)
            f.restype = S
            res = f()
            for i, f in enumerate(fields):
                value = getattr(res, f[0])
                expected = chr(ord(b'a') + i)
                self.assertEquals(value, expected)

        return


@unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
class TestWintypes(unittest.TestCase):

    def test_HWND(self):
        from ctypes import wintypes
        self.assertEqual(sizeof(wintypes.HWND), sizeof(c_void_p))
        return

    def test_PARAM(self):
        from ctypes import wintypes
        self.assertEqual(sizeof(wintypes.WPARAM), sizeof(c_void_p))
        self.assertEqual(sizeof(wintypes.LPARAM), sizeof(c_void_p))
        return

    def test_COMError(self):
        from _ctypes import COMError
        if support.HAVE_DOCSTRINGS:
            self.assertEqual(COMError.__doc__, b'Raised when a COM method call failed.')
        ex = COMError(-1, b'text', (b'details',))
        self.assertEqual(ex.hresult, -1)
        self.assertEqual(ex.text, b'text')
        self.assertEqual(ex.details, (b'details',))
        return


class Structures(unittest.TestCase):

    def test_struct_by_value(self):

        class POINT(Structure):
            _fields_ = [
             (
              b'x', c_long),
             (
              b'y', c_long)]

        class RECT(Structure):
            _fields_ = [
             (
              b'left', c_long),
             (
              b'top', c_long),
             (
              b'right', c_long),
             (
              b'bottom', c_long)]

        dll = CDLL(_ctypes_test.__file__)
        pt = POINT(15, 25)
        left = c_long.in_dll(dll, b'left')
        top = c_long.in_dll(dll, b'top')
        right = c_long.in_dll(dll, b'right')
        bottom = c_long.in_dll(dll, b'bottom')
        rect = RECT(left, top, right, bottom)
        PointInRect = dll.PointInRect
        PointInRect.argtypes = [POINTER(RECT), POINT]
        self.assertEqual(1, PointInRect(byref(rect), pt))
        ReturnRect = dll.ReturnRect
        ReturnRect.argtypes = [c_int, RECT, POINTER(RECT), POINT, RECT,
         POINTER(RECT), POINT, RECT]
        ReturnRect.restype = RECT
        for i in range(4):
            ret = ReturnRect(i, rect, pointer(rect), pt, rect, byref(rect), pt, rect)
            self.assertEqual(ret.left, left.value)
            self.assertEqual(ret.right, right.value)
            self.assertEqual(ret.top, top.value)
            self.assertEqual(ret.bottom, bottom.value)

        from ctypes import _pointer_type_cache
        del _pointer_type_cache[RECT]
        return


if __name__ == b'__main__':
    unittest.main()
