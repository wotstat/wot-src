import unittest
from ctypes import *
from ctypes.test import need_symbol
import _ctypes_test
dll = CDLL(_ctypes_test.__file__)
try:
    CALLBACK_FUNCTYPE = WINFUNCTYPE
except NameError:
    CALLBACK_FUNCTYPE = CFUNCTYPE

class POINT(Structure):
    _fields_ = [
     (
      b'x', c_int), (b'y', c_int)]


class BasicWrapTestCase(unittest.TestCase):

    def wrap(self, param):
        return param

    @need_symbol(b'c_wchar')
    def test_wchar_parm(self):
        f = dll._testfunc_i_bhilfd
        f.argtypes = [c_byte, c_wchar, c_int, c_long, c_float, c_double]
        result = f(self.wrap(1), self.wrap(u'x'), self.wrap(3), self.wrap(4), self.wrap(5.0), self.wrap(6.0))
        self.assertEqual(result, 139)
        self.assertIs(type(result), int)
        return

    def test_pointers(self):
        f = dll._testfunc_p_p
        f.restype = POINTER(c_int)
        f.argtypes = [POINTER(c_int)]
        v = c_int(42)
        self.assertEqual(pointer(v).contents.value, 42)
        result = f(self.wrap(pointer(v)))
        self.assertEqual(type(result), POINTER(c_int))
        self.assertEqual(result.contents.value, 42)
        result = f(self.wrap(pointer(v)))
        self.assertEqual(result.contents.value, v.value)
        p = pointer(c_int(99))
        result = f(self.wrap(p))
        self.assertEqual(result.contents.value, 99)
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
        f(self.wrap(262144), self.wrap(cb))
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
        result = f(self.wrap(-10), self.wrap(cb))
        self.assertEqual(result, -18)
        f.argtypes = [
         c_int, MyCallback]
        cb = MyCallback(callback)
        result = f(self.wrap(-10), self.wrap(cb))
        self.assertEqual(result, -18)
        result = f(self.wrap(-10), self.wrap(cb))
        self.assertEqual(result, -18)
        AnotherCallback = CALLBACK_FUNCTYPE(c_int, c_int, c_int, c_int, c_int)
        cb = AnotherCallback(callback)
        self.assertRaises(ArgumentError, f, self.wrap(-10), self.wrap(cb))
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
        result = f(self.wrap(-10), self.wrap(cb))
        self.assertEqual(result, -18)
        return

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
        self.assertEqual(13577625587L, int(f(self.wrap(1000000000000L), self.wrap(cb))))
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
        result = dll._testfunc_byval(self.wrap(ptin), byref(ptout))
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
        s2h = dll.ret_2h_func(self.wrap(inp))
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
        s8i = dll.ret_8i_func(self.wrap(inp))
        self.assertEqual((s8i.a, s8i.b, s8i.c, s8i.d, s8i.e, s8i.f, s8i.g, s8i.h), (
         18, 24, 28, 30, 30, 28, 24, 18))
        return

    def test_recursive_as_param(self):
        from ctypes import c_int

        class A(object):
            pass

        a = A()
        a._as_parameter_ = a
        with self.assertRaises(RuntimeError):
            c_int.from_param(a)
        return


class AsParamWrapper(object):

    def __init__(self, param):
        self._as_parameter_ = param
        return


class AsParamWrapperTestCase(BasicWrapTestCase):
    wrap = AsParamWrapper


class AsParamPropertyWrapper(object):

    def __init__(self, param):
        self._param = param
        return

    def getParameter(self):
        return self._param

    _as_parameter_ = property(getParameter)


class AsParamPropertyWrapperTestCase(BasicWrapTestCase):
    wrap = AsParamPropertyWrapper


if __name__ == b'__main__':
    unittest.main()
