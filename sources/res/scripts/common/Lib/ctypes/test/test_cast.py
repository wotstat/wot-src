from ctypes import *
from ctypes.test import need_symbol
import unittest, sys

class Test(unittest.TestCase):

    def test_array2pointer(self):
        array = (c_int * 3)(42, 17, 2)
        ptr = cast(array, POINTER(c_int))
        self.assertEqual([ptr[i] for i in range(3)], [42, 17, 2])
        if 2 * sizeof(c_short) == sizeof(c_int):
            ptr = cast(array, POINTER(c_short))
            if sys.byteorder == b'little':
                self.assertEqual([ptr[i] for i in range(6)], [
                 2, 7, 3, 7, 4, 7])
            else:
                self.assertEqual([ptr[i] for i in range(6)], [
                 7, 2, 7, 3, 7, 4])
        return

    def test_address2pointer(self):
        array = (c_int * 3)(42, 17, 2)
        address = addressof(array)
        ptr = cast(c_void_p(address), POINTER(c_int))
        self.assertEqual([ptr[i] for i in range(3)], [42, 17, 2])
        ptr = cast(address, POINTER(c_int))
        self.assertEqual([ptr[i] for i in range(3)], [42, 17, 2])
        return

    def test_p2a_objects(self):
        array = (c_char_p * 5)()
        self.assertEqual(array._objects, None)
        array[0] = b'foo bar'
        self.assertEqual(array._objects, {b'0': b'foo bar'})
        p = cast(array, POINTER(c_char_p))
        self.assertIs(p._objects, array._objects)
        self.assertEqual(array._objects, {b'0': b'foo bar', (id(array)): array})
        p[0] = b'spam spam'
        self.assertEqual(p._objects, {b'0': b'spam spam', (id(array)): array})
        self.assertIs(array._objects, p._objects)
        p[1] = b'foo bar'
        self.assertEqual(p._objects, {b'1': b'foo bar', b'0': b'spam spam', (id(array)): array})
        self.assertIs(array._objects, p._objects)
        return

    def test_other(self):
        p = cast((c_int * 4)(1, 2, 3, 4), POINTER(c_int))
        self.assertEqual(p[:4], [1, 2, 3, 4])
        self.assertEqual(p[:4:], [1, 2, 3, 4])
        self.assertEqual(p[3:-1:-1], [4, 3, 2, 1])
        self.assertEqual(p[:4:3], [1, 4])
        c_int()
        self.assertEqual(p[:4], [1, 2, 3, 4])
        self.assertEqual(p[:4:], [1, 2, 3, 4])
        self.assertEqual(p[3:-1:-1], [4, 3, 2, 1])
        self.assertEqual(p[:4:3], [1, 4])
        p[2] = 96
        self.assertEqual(p[:4], [1, 2, 96, 4])
        self.assertEqual(p[:4:], [1, 2, 96, 4])
        self.assertEqual(p[3:-1:-1], [4, 96, 2, 1])
        self.assertEqual(p[:4:3], [1, 4])
        c_int()
        self.assertEqual(p[:4], [1, 2, 96, 4])
        self.assertEqual(p[:4:], [1, 2, 96, 4])
        self.assertEqual(p[3:-1:-1], [4, 96, 2, 1])
        self.assertEqual(p[:4:3], [1, 4])
        return

    def test_char_p(self):
        s = c_char_p(b'hiho')
        self.assertEqual(cast(cast(s, c_void_p), c_char_p).value, b'hiho')
        return

    @need_symbol(b'c_wchar_p')
    def test_wchar_p(self):
        s = c_wchar_p(b'hiho')
        self.assertEqual(cast(cast(s, c_void_p), c_wchar_p).value, b'hiho')
        return


if __name__ == b'__main__':
    unittest.main()
