import unittest, pickle
from ctypes import *
import _ctypes_test
dll = CDLL(_ctypes_test.__file__)

class X(Structure):
    _fields_ = [
     (
      b'a', c_int), (b'b', c_double)]
    init_called = 0

    def __init__(self, *args, **kw):
        X.init_called += 1
        self.x = 42
        return


class Y(X):
    _fields_ = [
     (
      b'str', c_char_p)]


class PickleTest:

    def dumps(self, item):
        return pickle.dumps(item, self.proto)

    def loads(self, item):
        return pickle.loads(item)

    def test_simple(self):
        for src in [
         c_int(42),
         c_double(3.14)]:
            dst = self.loads(self.dumps(src))
            self.assertEqual(src.__dict__, dst.__dict__)
            self.assertEqual(memoryview(src).tobytes(), memoryview(dst).tobytes())

        return

    def test_struct(self):
        X.init_called = 0
        x = X()
        x.a = 42
        self.assertEqual(X.init_called, 1)
        y = self.loads(self.dumps(x))
        self.assertEqual(X.init_called, 1)
        self.assertEqual(y.__dict__, x.__dict__)
        self.assertEqual(memoryview(y).tobytes(), memoryview(x).tobytes())
        return

    def test_unpickable(self):
        self.assertRaises(ValueError, (lambda : self.dumps(Y())))
        prototype = CFUNCTYPE(c_int)
        for item in [
         c_char_p(),
         c_wchar_p(),
         c_void_p(),
         pointer(c_int(42)),
         dll._testfunc_p_p,
         prototype((lambda : 42))]:
            self.assertRaises(ValueError, (lambda : self.dumps(item)))

        return

    def test_wchar(self):
        self.dumps(c_char(b'x'))
        self.dumps(c_wchar(u'x'))
        return


for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    name = b'PickleTest_%s' % proto
    globals()[name] = type(name, (
     PickleTest, unittest.TestCase), {b'proto': proto})

if __name__ == b'__main__':
    unittest.main()
