import sys, unittest
from ctypes import *
from ctypes.test import need_symbol

class MemFunctionsTest(unittest.TestCase):

    @unittest.skip(b'test disabled')
    def test_overflow(self):
        self.assertRaises((OverflowError, MemoryError, SystemError), (lambda : wstring_at(u'foo', sys.maxint - 1)))
        self.assertRaises((OverflowError, MemoryError, SystemError), (lambda : string_at(b'foo', sys.maxint - 1)))
        return

    def test_memmove(self):
        a = create_string_buffer(1000000)
        p = b'Hello, World'
        result = memmove(a, p, len(p))
        self.assertEqual(a.value, b'Hello, World')
        self.assertEqual(string_at(result), b'Hello, World')
        self.assertEqual(string_at(result, 5), b'Hello')
        self.assertEqual(string_at(result, 16), b'Hello, World\x00\x00\x00\x00')
        self.assertEqual(string_at(result, 0), b'')
        return

    def test_memset(self):
        a = create_string_buffer(1000000)
        result = memset(a, ord(b'x'), 16)
        self.assertEqual(a.value, b'xxxxxxxxxxxxxxxx')
        self.assertEqual(string_at(result), b'xxxxxxxxxxxxxxxx')
        self.assertEqual(string_at(a), b'xxxxxxxxxxxxxxxx')
        self.assertEqual(string_at(a, 20), b'xxxxxxxxxxxxxxxx\x00\x00\x00\x00')
        return

    def test_cast(self):
        a = (c_ubyte * 32)(*map(ord, b'abcdef'))
        self.assertEqual(cast(a, c_char_p).value, b'abcdef')
        self.assertEqual(cast(a, POINTER(c_byte))[:7], [
         4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(cast(a, POINTER(c_byte))[:7:], [
         4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(cast(a, POINTER(c_byte))[6:-1:-1], [
         10, 9, 8, 7, 6, 5, 4])
        self.assertEqual(cast(a, POINTER(c_byte))[:7:2], [
         97, 99, 101, 0])
        self.assertEqual(cast(a, POINTER(c_byte))[:7:7], [
         97])
        return

    def test_string_at(self):
        s = string_at(b'foo bar')
        self.assertEqual(2, sys.getrefcount(s))
        self.assertTrue(s, b'foo bar')
        self.assertEqual(string_at(b'foo bar', 8), b'foo bar\x00')
        self.assertEqual(string_at(b'foo bar', 3), b'foo')
        return

    @need_symbol(b'create_unicode_buffer')
    def test_wstring_at(self):
        p = create_unicode_buffer(b'Hello, World')
        a = create_unicode_buffer(1000000)
        result = memmove(a, p, len(p) * sizeof(c_wchar))
        self.assertEqual(a.value, b'Hello, World')
        self.assertEqual(wstring_at(a), b'Hello, World')
        self.assertEqual(wstring_at(a, 5), b'Hello')
        self.assertEqual(wstring_at(a, 16), b'Hello, World\x00\x00\x00\x00')
        self.assertEqual(wstring_at(a, 0), b'')
        return


if __name__ == b'__main__':
    unittest.main()
