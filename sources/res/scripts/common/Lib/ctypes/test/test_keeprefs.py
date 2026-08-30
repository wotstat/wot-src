from ctypes import *
import unittest

class SimpleTestCase(unittest.TestCase):

    def test_cint(self):
        x = c_int()
        self.assertEqual(x._objects, None)
        x.value = 42
        self.assertEqual(x._objects, None)
        x = c_int(99)
        self.assertEqual(x._objects, None)
        return

    def test_ccharp(self):
        x = c_char_p()
        self.assertEqual(x._objects, None)
        x.value = b'abc'
        self.assertEqual(x._objects, b'abc')
        x = c_char_p(b'spam')
        self.assertEqual(x._objects, b'spam')
        return


class StructureTestCase(unittest.TestCase):

    def test_cint_struct(self):

        class X(Structure):
            _fields_ = [
             (
              b'a', c_int),
             (
              b'b', c_int)]

        x = X()
        self.assertEqual(x._objects, None)
        x.a = 42
        x.b = 99
        self.assertEqual(x._objects, None)
        return

    def test_ccharp_struct(self):

        class X(Structure):
            _fields_ = [
             (
              b'a', c_char_p),
             (
              b'b', c_char_p)]

        x = X()
        self.assertEqual(x._objects, None)
        x.a = b'spam'
        x.b = b'foo'
        self.assertEqual(x._objects, {b'0': b'spam', b'1': b'foo'})
        return

    def test_struct_struct(self):

        class POINT(Structure):
            _fields_ = [
             (
              b'x', c_int), (b'y', c_int)]

        class RECT(Structure):
            _fields_ = [
             (
              b'ul', POINT), (b'lr', POINT)]

        r = RECT()
        r.ul.x = 0
        r.ul.y = 1
        r.lr.x = 2
        r.lr.y = 3
        self.assertEqual(r._objects, None)
        r = RECT()
        pt = POINT(1, 2)
        r.ul = pt
        self.assertEqual(r._objects, {b'0': {}})
        r.ul.x = 22
        r.ul.y = 44
        self.assertEqual(r._objects, {b'0': {}})
        r.lr = POINT()
        self.assertEqual(r._objects, {b'0': {}, b'1': {}})
        return


class ArrayTestCase(unittest.TestCase):

    def test_cint_array(self):
        INTARR = c_int * 3
        ia = INTARR()
        self.assertEqual(ia._objects, None)
        ia[0] = 1
        ia[1] = 2
        ia[2] = 3
        self.assertEqual(ia._objects, None)

        class X(Structure):
            _fields_ = [
             (
              b'x', c_int),
             (
              b'a', INTARR)]

        x = X()
        x.x = 1000
        x.a[0] = 42
        x.a[1] = 96
        self.assertEqual(x._objects, None)
        x.a = ia
        self.assertEqual(x._objects, {b'1': {}})
        return


class PointerTestCase(unittest.TestCase):

    def test_p_cint(self):
        i = c_int(42)
        x = pointer(i)
        self.assertEqual(x._objects, {b'1': i})
        return


class DeletePointerTestCase(unittest.TestCase):

    @unittest.skip(b'test disabled')
    def test_X(self):

        class X(Structure):
            _fields_ = [
             (
              b'p', POINTER(c_char_p))]

        x = X()
        i = c_char_p(b'abc def')
        from sys import getrefcount as grc
        print b'2?', grc(i)
        x.p = pointer(i)
        print b'3?', grc(i)
        for i in range(320):
            c_int(99)
            x.p[0]

        print x.p[0]
        import gc
        gc.collect()
        for i in range(320):
            c_int(99)
            x.p[0]

        print x.p[0]
        print x.p.contents
        x.p[0] = b'spam spam'
        print b'+' * 42
        print x._objects
        return


class PointerToStructure(unittest.TestCase):

    def test(self):

        class POINT(Structure):
            _fields_ = [
             (
              b'x', c_int), (b'y', c_int)]

        class RECT(Structure):
            _fields_ = [
             (
              b'a', POINTER(POINT)),
             (
              b'b', POINTER(POINT))]

        r = RECT()
        p1 = POINT(1, 2)
        r.a = pointer(p1)
        r.b = pointer(p1)
        r.a[0].x = 42
        r.a[0].y = 99
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[POINT]
        return


if __name__ == b'__main__':
    unittest.main()
