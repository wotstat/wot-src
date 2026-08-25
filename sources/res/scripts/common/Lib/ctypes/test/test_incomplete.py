import unittest
from ctypes import *

class MyTestCase(unittest.TestCase):

    def test_incomplete_example(self):
        lpcell = POINTER(b'cell')

        class cell(Structure):
            _fields_ = [
             (
              b'name', c_char_p),
             (
              b'next', lpcell)]

        SetPointerType(lpcell, cell)
        c1 = cell()
        c1.name = b'foo'
        c2 = cell()
        c2.name = b'bar'
        c1.next = pointer(c2)
        c2.next = pointer(c1)
        p = c1
        result = []
        for i in range(8):
            result.append(p.name)
            p = p.next[0]

        self.assertEqual(result, [b'foo', b'bar'] * 4)
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[cell]
        return


if __name__ == b'__main__':
    unittest.main()
