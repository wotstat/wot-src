import unittest
from test.support import cpython_only
from ctypes import *

class AnonTest(unittest.TestCase):

    def test_anon(self):

        class ANON(Union):
            _fields_ = [
             (
              b'a', c_int),
             (
              b'b', c_int)]

        class Y(Structure):
            _fields_ = [
             (
              b'x', c_int),
             (
              b'_', ANON),
             (
              b'y', c_int)]
            _anonymous_ = [b'_']

        self.assertEqual(Y.a.offset, sizeof(c_int))
        self.assertEqual(Y.b.offset, sizeof(c_int))
        self.assertEqual(ANON.a.offset, 0)
        self.assertEqual(ANON.b.offset, 0)
        return

    def test_anon_nonseq(self):
        self.assertRaises(TypeError, (lambda : type(Structure)(b'Name', (
         Structure,), {b'_fields_': [], b'_anonymous_': 42})))
        return

    def test_anon_nonmember(self):
        self.assertRaises(AttributeError, (lambda : type(Structure)(b'Name', (
         Structure,), {b'_fields_': [], b'_anonymous_': [
                          b'x']})))
        return

    @cpython_only
    def test_issue31490(self):
        with self.assertRaises(AttributeError):

            class Name(Structure):
                _fields_ = []
                _anonymous_ = [b'x']
                x = 42

        return

    def test_nested(self):

        class ANON_S(Structure):
            _fields_ = [(b'a', c_int)]

        class ANON_U(Union):
            _fields_ = [
             (
              b'_', ANON_S),
             (
              b'b', c_int)]
            _anonymous_ = [b'_']

        class Y(Structure):
            _fields_ = [
             (
              b'x', c_int),
             (
              b'_', ANON_U),
             (
              b'y', c_int)]
            _anonymous_ = [b'_']

        self.assertEqual(Y.x.offset, 0)
        self.assertEqual(Y.a.offset, sizeof(c_int))
        self.assertEqual(Y.b.offset, sizeof(c_int))
        self.assertEqual(Y._.offset, sizeof(c_int))
        self.assertEqual(Y.y.offset, sizeof(c_int) * 2)
        return


if __name__ == b'__main__':
    unittest.main()
