from ctypes import *
from ctypes.test import need_symbol
import sys, unittest
try:
    WINFUNCTYPE
except NameError:
    WINFUNCTYPE = CFUNCTYPE

import _ctypes_test
dll = CDLL(_ctypes_test.__file__)
if sys.platform == b'win32':
    windll = WinDLL(_ctypes_test.__file__)

class POINT(Structure):
    _fields_ = [
     (
      b'x', c_int), (b'y', c_int)]


class RECT(Structure):
    _fields_ = [
     (
      b'left', c_int), (b'top', c_int),
     (
      b'right', c_int), (b'bottom', c_int)]


class FunctionTestCase(unittest.TestCase):

    def test_mro(self):
        try:

            class X(object, Array):
                _length_ = 5
                _type_ = b'i'

        except TypeError:
            pass

        from _ctypes import _Pointer
        try:

            class X(object, _Pointer):
                pass

        except TypeError:
            pass

        from _ctypes import _SimpleCData
        try:

            class X(object, _SimpleCData):
                _type_ = b'i'

        except TypeError:
            pass

        try:

            class X(object, Structure):
                _fields_ = []

        except TypeError:
            pass

        return

    @need_symbol(b'c_wchar')
    def test_wchar_parm(self):
        f = dll._testfunc_i_bhilfd
        f.argtypes = [c_byte, c_wchar, c_int, c_long, c_float, c_double]
        result = f(1, u'x', 3, 4, 5.0, 6.0)
        self.assertEqual(result, 139)
        self.assertEqual(type(result), int)
        return

    @need_symbol(b'c_wchar')
    def test_wchar_result(self):
        f = dll._testfunc_i_bhilfd
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_double]
        f.restype = c_wchar
        result = f(0, 0, 0, 0, 0, 0)
        self.assertEqual(result, u'\x00')
        return

    def test_voidresult(self):
        f = dll._testfunc_v
        f.restype = None
        f.argtypes = [c_int, c_int, POINTER(c_int)]
        result = c_int()
        self.assertEqual(None, f(1, 2, byref(result)))
        self.assertEqual(result.value, 3)
        return

    def test_intresult(self):
        f = dll._testfunc_i_bhilfd
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_double]
        f.restype = c_int
        result = f(1, 2, 3, 4, 5.0, 6.0)
        self.assertEqual(result, 21)
        self.assertEqual(type(result), int)
        result = f(-1, -2, -3, -4, -5.0, -6.0)
        self.assertEqual(result, -21)
        self.assertEqual(type(result), int)
        f.restype = c_short
        result = f(1, 2, 3, 4, 5.0, 6.0)
        self.assertEqual(result, 21)
        self.assertEqual(type(result), int)
        result = f(1, 2, 3, 65540, 5.0, 6.0)
        self.assertEqual(result, 21)
        self.assertEqual(type(result), int)
        self.assertRaises(TypeError, setattr, f, b'restype', b'i')
        return

    def test_floatresult(self):
        f = dll._testfunc_f_bhilfd
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_double]
        f.restype = c_float
        result = f(1, 2, 3, 4, 5.0, 6.0)
        self.assertEqual(result, 21)
        self.assertEqual(type(result), float)
        result = f(-1, -2, -3, -4, -5.0, -6.0)
        self.assertEqual(result, -21)
        self.assertEqual(type(result), float)
        return

    def test_doubleresult(self):
        f = dll._testfunc_d_bhilfd
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_double]
        f.restype = c_double
        result = f(1, 2, 3, 4, 5.0, 6.0)
        self.assertEqual(result, 21)
        self.assertEqual(type(result), float)
        result = f(-1, -2, -3, -4, -5.0, -6.0)
        self.assertEqual(result, -21)
        self.assertEqual(type(result), float)
        return

    def test_longdoubleresult(self):
        f = dll._testfunc_D_bhilfD
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_longdouble]
        f.restype = c_longdouble
        result = f(1, 2, 3, 4, 5.0, 6.0)
        self.assertEqual(result, 21)
        self.assertEqual(type(result), float)
        result = f(-1, -2, -3, -4, -5.0, -6.0)
        self.assertEqual(result, -21)
        self.assertEqual(type(result), float)
        return

    @need_symbol(b'c_longlong')
    def test_longlongresult(self):
        f = dll._testfunc_q_bhilfd
        f.restype = c_longlong
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_double]
        result = f(1, 2, 3, 4, 5.0, 6.0)
        self.assertEqual(result, 21)
        f = dll._testfunc_q_bhilfdq
        f.restype = c_longlong
        f.argtypes = [c_byte, c_short, c_int, c_long, c_float, c_double, c_longlong]
        result = f(1, 2, 3, 4, 5.0, 6.0, 21)
        self.assertEqual(result, 42)
        return

    def test_stringresult(self):
        f = dll._testfunc_p_p
        f.argtypes = None
        f.restype = c_char_p
        result = f(b'123')
        self.assertEqual(result, b'123')
        result = f(None)
        self.assertEqual(result, None)
        return

    def test_pointers(self):
        f = dll._testfunc_p_p
        f.restype = POINTER(c_int)
        f.argtypes = [POINTER(c_int)]
        v = c_int(42)
        self.assertEqual(pointer(v).contents.value, 42)
        result = f(pointer(v))
        self.assertEqual(type(result), POINTER(c_int))
        self.assertEqual(result.contents.value, 42)
        result = f(pointer(v))
        self.assertEqual(result.contents.value, v.value)
        p = pointer(c_int(99))
        result = f(p)
        self.assertEqual(result.contents.value, 99)
        arg = byref(v)
        result = f(arg)
        self.assertNotEqual(result.contents, v.value)
        self.assertRaises(ArgumentError, f, byref(c_short(22)))
        result = f(byref(c_int(99)))
        self.assertNotEqual(result.contents, 99)
        return

    def test_errors(self):
        f = dll._testfunc_p_p
        f.restype = c_int

        class X(Structure):
            _fields_ = [
             (
              b'y', c_int)]

        self.assertRaises(TypeError, f, X())
        return

    def test_shorts(self):
        f = dll._testfunc_callback_i_if
        args = []
        expected = [
         1, 2, 3, 4, 5, 6, 7, 8, 
         9, 
         10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        def callback(v):
            args.append(v)
            return v

        CallBack = CFUNCTYPE(c_int, c_int)
        cb = CallBack(callback)
        f(262144, cb)
        self.assertEqual(args, expected)
        return

    def test_callbacks(self):
        f = dll._testfunc_callback_i_if
        f.restype = c_int
        f.argtypes = None
        MyCallback = CFUNCTYPE(c_int, c_int)

        def callback(value):
            return value

        cb = MyCallback(callback)
        result = f(-10, cb)
        self.assertEqual(result, -18)
        f.argtypes = [
         c_int, MyCallback]
        cb = MyCallback(callback)
        result = f(-10, cb)
        self.assertEqual(result, -18)
        AnotherCallback = WINFUNCTYPE(c_int, c_int, c_int, c_int, c_int)
        cb = AnotherCallback(callback)
        self.assertRaises(ArgumentError, f, -10, cb)
        return

    def test_callbacks_2(self):
        f = dll._testfunc_callback_i_if
        f.restype = c_int
        MyCallback = CFUNCTYPE(c_int, c_int)
        f.argtypes = [
         c_int, MyCallback]

        def callback(value):
            self.assertEqual(type(value), int)
            return value

        cb = MyCallback(callback)
        result = f(-10, cb)
        self.assertEqual(result, -18)
        return

    @need_symbol(b'c_longlong')
    def test_longlong_callbacks(self):
        f = dll._testfunc_callback_q_qf
        f.restype = c_longlong
        MyCallback = CFUNCTYPE(c_longlong, c_longlong)
        f.argtypes = [
         c_longlong, MyCallback]

        def callback(value):
            self.assertIsInstance(value, (int, long))
            return value & 2147483647

        cb = MyCallback(callback)
        self.assertEqual(13577625587L, f(1000000000000L, cb))
        return

    def test_errors(self):
        self.assertRaises(AttributeError, getattr, dll, b'_xxx_yyy')
        self.assertRaises(ValueError, c_int.in_dll, dll, b'_xxx_yyy')
        return

    def test_byval(self):
        ptin = POINT(1, 2)
        ptout = POINT()
        result = dll._testfunc_byval(ptin, byref(ptout))
        got = (result, ptout.x, ptout.y)
        expected = (3, 1, 2)
        self.assertEqual(got, expected)
        ptin = POINT(101, 102)
        ptout = POINT()
        dll._testfunc_byval.argtypes = (POINT, POINTER(POINT))
        dll._testfunc_byval.restype = c_int
        result = dll._testfunc_byval(ptin, byref(ptout))
        got = (result, ptout.x, ptout.y)
        expected = (203, 101, 102)
        self.assertEqual(got, expected)
        return

    def test_struct_return_2H(self):

        class S2H(Structure):
            _fields_ = [
             (
              b'x', c_short),
             (
              b'y', c_short)]

        dll.ret_2h_func.restype = S2H
        dll.ret_2h_func.argtypes = [S2H]
        inp = S2H(99, 88)
        s2h = dll.ret_2h_func(inp)
        self.assertEqual((s2h.x, s2h.y), (198, 264))
        return

    @unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
    def test_struct_return_2H_stdcall(self):

        class S2H(Structure):
            _fields_ = [
             (
              b'x', c_short),
             (
              b'y', c_short)]

        windll.s_ret_2h_func.restype = S2H
        windll.s_ret_2h_func.argtypes = [S2H]
        s2h = windll.s_ret_2h_func(S2H(99, 88))
        self.assertEqual((s2h.x, s2h.y), (198, 264))
        return

    def test_struct_return_8H(self):

        class S8I(Structure):
            _fields_ = [
             (
              b'a', c_int),
             (
              b'b', c_int),
             (
              b'c', c_int),
             (
              b'd', c_int),
             (
              b'e', c_int),
             (
              b'f', c_int),
             (
              b'g', c_int),
             (
              b'h', c_int)]

        dll.ret_8i_func.restype = S8I
        dll.ret_8i_func.argtypes = [S8I]
        inp = S8I(9, 8, 7, 6, 5, 4, 3, 2)
        s8i = dll.ret_8i_func(inp)
        self.assertEqual((s8i.a, s8i.b, s8i.c, s8i.d, s8i.e, s8i.f, s8i.g, s8i.h), (
         18, 24, 28, 30, 30, 28, 24, 18))
        return

    @unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
    def test_struct_return_8H_stdcall(self):

        class S8I(Structure):
            _fields_ = [
             (
              b'a', c_int),
             (
              b'b', c_int),
             (
              b'c', c_int),
             (
              b'd', c_int),
             (
              b'e', c_int),
             (
              b'f', c_int),
             (
              b'g', c_int),
             (
              b'h', c_int)]

        windll.s_ret_8i_func.restype = S8I
        windll.s_ret_8i_func.argtypes = [S8I]
        inp = S8I(9, 8, 7, 6, 5, 4, 3, 2)
        s8i = windll.s_ret_8i_func(inp)
        self.assertEqual((
         s8i.a, s8i.b, s8i.c, s8i.d, s8i.e, s8i.f, s8i.g, s8i.h), (
         18, 24, 28, 30, 30, 28, 24, 18))
        return

    def test_sf1651235(self):
        proto = CFUNCTYPE(c_int, RECT, POINT)

        def callback(*args):
            return 0

        callback = proto(callback)
        self.assertRaises(ArgumentError, (lambda : callback((1, 2, 3, 4), POINT())))
        return


if __name__ == b'__main__':
    unittest.main()
