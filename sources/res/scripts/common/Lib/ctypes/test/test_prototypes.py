from ctypes import *
from ctypes.test import need_symbol
import unittest, _ctypes_test
testdll = CDLL(_ctypes_test.__file__)

def positive_address(a):
    if a >= 0:
        return a
    import struct
    num_bits = struct.calcsize(b'P') * 8
    a += 1L << num_bits
    return a


def c_wbuffer(init):
    n = len(init) + 1
    return (c_wchar * n)(*init)


class CharPointersTestCase(unittest.TestCase):

    def setUp(self):
        func = testdll._testfunc_p_p
        func.restype = c_long
        func.argtypes = None
        return

    def test_paramflags(self):
        prototype = CFUNCTYPE(c_void_p, c_void_p)
        func = prototype((b'_testfunc_p_p', testdll), ((1, b'input'),))
        try:
            func()
        except TypeError as details:
            self.assertEqual(str(details), b"required argument 'input' missing")
        else:
            self.fail(b'TypeError not raised')

        self.assertEqual(func(None), None)
        self.assertEqual(func(input=None), None)
        return

    def test_int_pointer_arg(self):
        func = testdll._testfunc_p_p
        func.restype = c_long
        self.assertEqual(0, func(0))
        ci = c_int(0)
        func.argtypes = (
         POINTER(c_int),)
        self.assertEqual(positive_address(addressof(ci)), positive_address(func(byref(ci))))
        func.argtypes = (
         c_char_p,)
        self.assertRaises(ArgumentError, func, byref(ci))
        func.argtypes = (
         POINTER(c_short),)
        self.assertRaises(ArgumentError, func, byref(ci))
        func.argtypes = (
         POINTER(c_double),)
        self.assertRaises(ArgumentError, func, byref(ci))
        return

    def test_POINTER_c_char_arg(self):
        func = testdll._testfunc_p_p
        func.restype = c_char_p
        func.argtypes = (POINTER(c_char),)
        self.assertEqual(None, func(None))
        self.assertEqual(b'123', func(b'123'))
        self.assertEqual(None, func(c_char_p(None)))
        self.assertEqual(b'123', func(c_char_p(b'123')))
        self.assertEqual(b'123', func(c_buffer(b'123')))
        ca = c_char(b'a')
        self.assertEqual(b'a', func(pointer(ca))[0])
        self.assertEqual(b'a', func(byref(ca))[0])
        return

    def test_c_char_p_arg(self):
        func = testdll._testfunc_p_p
        func.restype = c_char_p
        func.argtypes = (c_char_p,)
        self.assertEqual(None, func(None))
        self.assertEqual(b'123', func(b'123'))
        self.assertEqual(None, func(c_char_p(None)))
        self.assertEqual(b'123', func(c_char_p(b'123')))
        self.assertEqual(b'123', func(c_buffer(b'123')))
        ca = c_char(b'a')
        self.assertEqual(b'a', func(pointer(ca))[0])
        self.assertEqual(b'a', func(byref(ca))[0])
        return

    def test_c_void_p_arg(self):
        func = testdll._testfunc_p_p
        func.restype = c_char_p
        func.argtypes = (c_void_p,)
        self.assertEqual(None, func(None))
        self.assertEqual(b'123', func(b'123'))
        self.assertEqual(b'123', func(c_char_p(b'123')))
        self.assertEqual(None, func(c_char_p(None)))
        self.assertEqual(b'123', func(c_buffer(b'123')))
        ca = c_char(b'a')
        self.assertEqual(b'a', func(pointer(ca))[0])
        self.assertEqual(b'a', func(byref(ca))[0])
        func(byref(c_int()))
        func(pointer(c_int()))
        func((c_int * 3)())
        return

    @need_symbol(b'c_wchar_p')
    def test_c_void_p_arg_with_c_wchar_p(self):
        func = testdll._testfunc_p_p
        func.restype = c_wchar_p
        func.argtypes = (c_void_p,)
        self.assertEqual(None, func(c_wchar_p(None)))
        self.assertEqual(u'123', func(c_wchar_p(u'123')))
        return

    def test_instance(self):
        func = testdll._testfunc_p_p
        func.restype = c_void_p

        class X:
            _as_parameter_ = None

        func.argtypes = (
         c_void_p,)
        self.assertEqual(None, func(X()))
        func.argtypes = None
        self.assertEqual(None, func(X()))
        return


@need_symbol(b'c_wchar')
class WCharPointersTestCase(unittest.TestCase):

    def setUp(self):
        func = testdll._testfunc_p_p
        func.restype = c_int
        func.argtypes = None
        return

    def test_POINTER_c_wchar_arg(self):
        func = testdll._testfunc_p_p
        func.restype = c_wchar_p
        func.argtypes = (POINTER(c_wchar),)
        self.assertEqual(None, func(None))
        self.assertEqual(u'123', func(u'123'))
        self.assertEqual(None, func(c_wchar_p(None)))
        self.assertEqual(u'123', func(c_wchar_p(u'123')))
        self.assertEqual(u'123', func(c_wbuffer(u'123')))
        ca = c_wchar(b'a')
        self.assertEqual(u'a', func(pointer(ca))[0])
        self.assertEqual(u'a', func(byref(ca))[0])
        return

    def test_c_wchar_p_arg(self):
        func = testdll._testfunc_p_p
        func.restype = c_wchar_p
        func.argtypes = (c_wchar_p,)
        c_wchar_p.from_param(u'123')
        self.assertEqual(None, func(None))
        self.assertEqual(b'123', func(u'123'))
        self.assertEqual(None, func(c_wchar_p(None)))
        self.assertEqual(b'123', func(c_wchar_p(b'123')))
        self.assertEqual(b'123', func(c_wbuffer(b'123')))
        ca = c_wchar(b'a')
        self.assertEqual(b'a', func(pointer(ca))[0])
        self.assertEqual(b'a', func(byref(ca))[0])
        return


class ArrayTest(unittest.TestCase):

    def test(self):
        func = testdll._testfunc_ai8
        func.restype = POINTER(c_int)
        func.argtypes = (c_int * 8,)
        func((c_int * 8)(1, 2, 3, 4, 5, 6, 7, 8))

        def func():
            return

        CFUNCTYPE(None, c_int * 3)(func)
        return


if __name__ == b'__main__':
    unittest.main()
