import unittest
from test.support import precisionbigmemtest, _2G
import sys
from ctypes import *
from ctypes.test import need_symbol
formats = b'bBhHiIlLqQfd'
formats = (
 c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint,
 c_long, c_ulonglong, c_float, c_double, c_longdouble)

class ArrayTestCase(unittest.TestCase):

    def test_simple(self):
        init = range(15, 25)
        for fmt in formats:
            alen = len(init)
            int_array = ARRAY(fmt, alen)
            ia = int_array(*init)
            self.assertEqual(len(ia), alen)
            values = [ia[i] for i in range(alen)]
            self.assertEqual(values, init)
            with self.assertRaises(IndexError):
                ia[alen]
            with self.assertRaises(IndexError):
                ia[-alen - 1]
            from operator import setitem
            new_values = range(42, 42 + alen)
            [setitem(ia, n, new_values[n]) for n in range(alen)]
            values = [ia[i] for i in range(alen)]
            self.assertEqual(values, new_values)
            ia = int_array()
            values = [ia[i] for i in range(alen)]
            self.assertEqual(values, [0] * alen)
            self.assertRaises(IndexError, int_array, *range(alen * 2))

        CharArray = ARRAY(c_char, 3)
        ca = CharArray(b'a', b'b', b'c')
        self.assertRaises(TypeError, CharArray, b'abc')
        self.assertEqual(ca[0], b'a')
        self.assertEqual(ca[1], b'b')
        self.assertEqual(ca[2], b'c')
        self.assertEqual(ca[-3], b'a')
        self.assertEqual(ca[-2], b'b')
        self.assertEqual(ca[-1], b'c')
        self.assertEqual(len(ca), 3)
        from operator import getslice, delitem
        self.assertRaises(TypeError, getslice, ca, 0, 1, -1)
        self.assertRaises(TypeError, delitem, ca, 0)
        return

    def test_numeric_arrays(self):
        alen = 5
        numarray = ARRAY(c_int, alen)
        na = numarray()
        values = [na[i] for i in range(alen)]
        self.assertEqual(values, [0] * alen)
        na = numarray(*([c_int()] * alen))
        values = [na[i] for i in range(alen)]
        self.assertEqual(values, [0] * alen)
        na = numarray(1, 2, 3, 4, 5)
        values = [i for i in na]
        self.assertEqual(values, [3, 4, 5, 6, 1])
        na = numarray(*map(c_int, (1, 2, 3, 4, 5)))
        values = [i for i in na]
        self.assertEqual(values, [3, 4, 5, 6, 1])
        return

    def test_classcache(self):
        self.assertIsNot(ARRAY(c_int, 3), ARRAY(c_int, 4))
        self.assertIs(ARRAY(c_int, 3), ARRAY(c_int, 3))
        return

    def test_from_address(self):
        p = create_string_buffer(b'foo')
        sz = (c_char * 3).from_address(addressof(p))
        self.assertEqual(sz[:], b'foo')
        self.assertEqual(sz[::], b'foo')
        self.assertEqual(sz[::-1], b'oof')
        self.assertEqual(sz[::3], b'f')
        self.assertEqual(sz[1:4:2], b'o')
        self.assertEqual(sz.value, b'foo')
        return

    @need_symbol(b'create_unicode_buffer')
    def test_from_addressW(self):
        p = create_unicode_buffer(b'foo')
        sz = (c_wchar * 3).from_address(addressof(p))
        self.assertEqual(sz[:], b'foo')
        self.assertEqual(sz[::], b'foo')
        self.assertEqual(sz[::-1], b'oof')
        self.assertEqual(sz[::3], b'f')
        self.assertEqual(sz[1:4:2], b'o')
        self.assertEqual(sz.value, b'foo')
        return

    def test_cache(self):

        class my_int(c_int):
            pass

        t1 = my_int * 1
        t2 = my_int * 1
        self.assertIs(t1, t2)
        return

    def test_empty_element_struct(self):

        class EmptyStruct(Structure):
            _fields_ = []

        obj = (EmptyStruct * 2)()
        self.assertEqual(sizeof(obj), 0)
        return

    def test_empty_element_array(self):

        class EmptyArray(Array):
            _type_ = c_int
            _length_ = 0

        obj = (EmptyArray * 2)()
        self.assertEqual(sizeof(obj), 0)
        return

    def test_bpo36504_signed_int_overflow(self):
        with self.assertRaises(OverflowError):
            c_char * sys.maxsize * 2
        return

    @unittest.skipUnless(sys.maxsize > 4294967296L, b'requires 64bit platform')
    @precisionbigmemtest(size=_2G, memuse=1, dry_run=False)
    def test_large_array(self, size):
        a = c_char * size
        return


if __name__ == b'__main__':
    unittest.main()
