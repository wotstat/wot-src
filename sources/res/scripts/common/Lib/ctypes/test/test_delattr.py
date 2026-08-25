import unittest
from ctypes import *

class X(Structure):
    _fields_ = [
     (
      b'foo', c_int)]


class TestCase(unittest.TestCase):

    def test_simple(self):
        self.assertRaises(TypeError, delattr, c_int(42), b'value')
        return

    def test_chararray(self):
        self.assertRaises(TypeError, delattr, (c_char * 5)(), b'value')
        return

    def test_struct(self):
        self.assertRaises(TypeError, delattr, X(), b'foo')
        return


if __name__ == b'__main__':
    unittest.main()
