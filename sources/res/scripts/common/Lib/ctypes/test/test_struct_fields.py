import unittest
from ctypes import *

class StructFieldsTestCase(unittest.TestCase):

    def test_1_A(self):

        class X(Structure):
            pass

        self.assertEqual(sizeof(X), 0)
        X._fields_ = []
        self.assertRaises(AttributeError, setattr, X, b'_fields_', [])
        return

    def test_1_B(self):

        class X(Structure):
            _fields_ = []

        self.assertRaises(AttributeError, setattr, X, b'_fields_', [])
        return

    def test_2(self):

        class X(Structure):
            pass

        X()
        self.assertRaises(AttributeError, setattr, X, b'_fields_', [])
        return

    def test_3(self):

        class X(Structure):
            pass

        class Y(Structure):
            _fields_ = [
             (
              b'x', X)]

        self.assertRaises(AttributeError, setattr, X, b'_fields_', [])
        return

    def test_4(self):

        class X(Structure):
            pass

        class Y(X):
            pass

        self.assertRaises(AttributeError, setattr, X, b'_fields_', [])
        Y._fields_ = []
        self.assertRaises(AttributeError, setattr, X, b'_fields_', [])
        return

    def test___set__(self):

        class MyCStruct(Structure):
            _fields_ = (
             (
              b'field', c_int),)

        self.assertRaises(TypeError, MyCStruct.field.__set__, b'wrong type self', 42)

        class MyCUnion(Union):
            _fields_ = (
             (
              b'field', c_int),)

        self.assertRaises(TypeError, MyCUnion.field.__set__, b'wrong type self', 42)
        return

    def test___get__(self):

        class MyCStruct(Structure):
            _fields_ = (
             (
              b'field', c_int),)

        self.assertRaises(TypeError, MyCStruct.field.__get__, b'wrong type self', 42)

        class MyCUnion(Union):
            _fields_ = (
             (
              b'field', c_int),)

        self.assertRaises(TypeError, MyCUnion.field.__get__, b'wrong type self', 42)
        return


if __name__ == b'__main__':
    unittest.main()
