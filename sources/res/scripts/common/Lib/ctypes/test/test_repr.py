from ctypes import *
import unittest
subclasses = []
for base in [c_byte, c_short, c_int, c_long, c_longlong, 
 c_ubyte, c_ushort, c_uint, 
 c_ulong, c_ulonglong, 
 c_float, c_double, c_longdouble, c_bool]:

    class X(base):
        pass


    subclasses.append(X)

class X(c_char):
    pass


class ReprTest(unittest.TestCase):

    def test_numbers(self):
        for typ in subclasses:
            base = typ.__bases__[0]
            self.assertTrue(repr(base(42)).startswith(base.__name__))
            self.assertEqual(b'<X object at', repr(typ(42))[:12])

        return

    def test_char(self):
        self.assertEqual(b"c_char('x')", repr(c_char(b'x')))
        self.assertEqual(b'<X object at', repr(X(b'x'))[:12])
        return


if __name__ == b'__main__':
    unittest.main()
