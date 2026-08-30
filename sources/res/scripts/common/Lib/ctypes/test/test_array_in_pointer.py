import unittest
from ctypes import *
from binascii import hexlify
import re

def dump(obj):
    h = hexlify(memoryview(obj))
    return re.sub(b'(..)', b'\\1-', h)[:-1]


class Value(Structure):
    _fields_ = [
     (
      b'val', c_byte)]


class Container(Structure):
    _fields_ = [
     (
      b'pvalues', POINTER(Value))]


class Test(unittest.TestCase):

    def test(self):
        val_array = (Value * 4)()
        c = Container()
        c.pvalues = val_array
        self.assertEqual(b'00-00-00-00', dump(val_array))
        for i in range(4):
            c.pvalues[i].val = i + 1

        values = [c.pvalues[i].val for i in range(4)]
        self.assertEqual((
         values, dump(val_array)), (
         [
          1, 2, 3, 4], b'01-02-03-04'))
        return

    def test_2(self):
        val_array = (Value * 4)()
        self.assertEqual(b'00-00-00-00', dump(val_array))
        ptr = cast(val_array, POINTER(Value))
        for i in range(4):
            ptr[i].val = i + 1

        values = [ptr[i].val for i in range(4)]
        self.assertEqual((
         values, dump(val_array)), (
         [
          1, 2, 3, 4], b'01-02-03-04'))
        return


if __name__ == b'__main__':
    unittest.main()
