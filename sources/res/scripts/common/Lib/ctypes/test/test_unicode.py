import unittest, ctypes
from ctypes.test import need_symbol
import _ctypes_test

@need_symbol(b'c_wchar')
class UnicodeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dll = ctypes.CDLL(_ctypes_test.__file__)
        cls.wcslen = dll.my_wcslen
        cls.wcslen.argtypes = [ctypes.c_wchar_p]
        return

    def setUp(self):
        self.prev_conv_mode = ctypes.set_conversion_mode(b'ascii', b'strict')
        return

    def tearDown(self):
        ctypes.set_conversion_mode(*self.prev_conv_mode)
        return

    def test_ascii_strict(self):
        wcslen = self.wcslen
        ctypes.set_conversion_mode(b'ascii', b'strict')
        self.assertEqual(wcslen(u'abc'), 3)
        self.assertEqual(wcslen(u'ab\u2070'), 3)
        self.assertEqual(wcslen(b'abc'), 3)
        self.assertRaises(ctypes.ArgumentError, wcslen, b'ab\xe4')
        return

    def test_ascii_replace(self):
        wcslen = self.wcslen
        ctypes.set_conversion_mode(b'ascii', b'replace')
        self.assertEqual(wcslen(u'abc'), 3)
        self.assertEqual(wcslen(u'ab\u2070'), 3)
        self.assertEqual(wcslen(b'abc'), 3)
        self.assertEqual(wcslen(b'ab\xe4'), 3)
        return

    def test_ascii_ignore(self):
        wcslen = self.wcslen
        ctypes.set_conversion_mode(b'ascii', b'ignore')
        self.assertEqual(wcslen(u'abc'), 3)
        self.assertEqual(wcslen(u'ab\u2070'), 3)
        self.assertEqual(wcslen(b'abc'), 3)
        self.assertEqual(wcslen(b'\xe4\xf6\xfc\xdf'), 0)
        return

    def test_latin1_strict(self):
        wcslen = self.wcslen
        ctypes.set_conversion_mode(b'latin-1', b'strict')
        self.assertEqual(wcslen(u'abc'), 3)
        self.assertEqual(wcslen(u'ab\u2070'), 3)
        self.assertEqual(wcslen(b'abc'), 3)
        self.assertEqual(wcslen(b'\xe4\xf6\xfc\xdf'), 4)
        return

    def test_buffers(self):
        ctypes.set_conversion_mode(b'ascii', b'strict')
        buf = ctypes.create_unicode_buffer(b'abc')
        self.assertEqual(len(buf), 4)
        ctypes.set_conversion_mode(b'ascii', b'replace')
        buf = ctypes.create_unicode_buffer(b'ab\xe4\xf6\xfc')
        self.assertEqual(buf[:], u'ab\ufffd\ufffd\ufffd\x00')
        self.assertEqual(buf[::], u'ab\ufffd\ufffd\ufffd\x00')
        self.assertEqual(buf[::-1], u'\x00\ufffd\ufffd\ufffdba')
        self.assertEqual(buf[::2], u'a\ufffd\ufffd')
        self.assertEqual(buf[6:5:-1], u'')
        ctypes.set_conversion_mode(b'ascii', b'ignore')
        buf = ctypes.create_unicode_buffer(b'ab\xe4\xf6\xfc')
        self.assertEqual(buf[:], u'ab\x00\x00\x00\x00')
        self.assertEqual(buf[::], u'ab\x00\x00\x00\x00')
        self.assertEqual(buf[::-1], u'\x00\x00\x00\x00ba')
        self.assertEqual(buf[::2], u'a\x00\x00')
        self.assertEqual(buf[6:5:-1], u'')
        return


@need_symbol(b'c_wchar')
class StringTestCase(UnicodeTestCase):

    @classmethod
    def setUpClass(cls):
        super(StringTestCase, cls).setUpClass()
        cls.func = ctypes.CDLL(_ctypes_test.__file__)._testfunc_p_p
        return

    def setUp(self):
        func = self.func
        self.prev_conv_mode = ctypes.set_conversion_mode(b'ascii', b'strict')
        func.argtypes = [ctypes.c_char_p]
        func.restype = ctypes.c_char_p
        return

    def tearDown(self):
        func = self.func
        ctypes.set_conversion_mode(*self.prev_conv_mode)
        func.argtypes = None
        func.restype = ctypes.c_int
        return

    def test_ascii_strict(self):
        func = self.func
        ctypes.set_conversion_mode(b'ascii', b'strict')
        self.assertEqual(func(b'abc'), b'abc')
        self.assertEqual(func(u'abc'), b'abc')
        self.assertRaises(ctypes.ArgumentError, func, u'ab\xe4')
        return

    def test_ascii_ignore(self):
        func = self.func
        ctypes.set_conversion_mode(b'ascii', b'ignore')
        self.assertEqual(func(b'abc'), b'abc')
        self.assertEqual(func(u'abc'), b'abc')
        self.assertEqual(func(u'\xe4\xf6\xfc\xdf'), b'')
        return

    def test_ascii_replace(self):
        func = self.func
        ctypes.set_conversion_mode(b'ascii', b'replace')
        self.assertEqual(func(b'abc'), b'abc')
        self.assertEqual(func(u'abc'), b'abc')
        self.assertEqual(func(u'\xe4\xf6\xfc\xdf'), b'????')
        return

    def test_buffers(self):
        ctypes.set_conversion_mode(b'ascii', b'strict')
        buf = ctypes.create_string_buffer(u'abc')
        self.assertEqual(len(buf), 4)
        ctypes.set_conversion_mode(b'ascii', b'replace')
        buf = ctypes.create_string_buffer(u'ab\xe4\xf6\xfc')
        self.assertEqual(buf[:], b'ab???\x00')
        self.assertEqual(buf[::], b'ab???\x00')
        self.assertEqual(buf[::-1], b'\x00???ba')
        self.assertEqual(buf[::2], b'a??')
        self.assertEqual(buf[6:5:-1], b'')
        ctypes.set_conversion_mode(b'ascii', b'ignore')
        buf = ctypes.create_string_buffer(u'ab\xe4\xf6\xfc')
        self.assertEqual(buf[:], b'ab\x00\x00\x00\x00')
        self.assertEqual(buf[::], b'ab\x00\x00\x00\x00')
        self.assertEqual(buf[::-1], b'\x00\x00\x00\x00ba')
        return


if __name__ == b'__main__':
    unittest.main()
