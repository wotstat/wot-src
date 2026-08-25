import unittest
from ctypes import *
from ctypes.test import need_symbol
from struct import calcsize
import _testcapi, _ctypes_test

class SubclassesTest(unittest.TestCase):

    def test_subclass(self):

        class X(Structure):
            _fields_ = [
             (
              b'a', c_int)]

        class Y(X):
            _fields_ = [
             (
              b'b', c_int)]

        class Z(X):
            pass

        self.assertEqual(sizeof(X), sizeof(c_int))
        self.assertEqual(sizeof(Y), sizeof(c_int) * 2)
        self.assertEqual(sizeof(Z), sizeof(c_int))
        self.assertEqual(X._fields_, [(b'a', c_int)])
        self.assertEqual(Y._fields_, [(b'b', c_int)])
        self.assertEqual(Z._fields_, [(b'a', c_int)])
        return

    def test_subclass_delayed(self):

        class X(Structure):
            pass

        self.assertEqual(sizeof(X), 0)
        X._fields_ = [(b'a', c_int)]

        class Y(X):
            pass

        self.assertEqual(sizeof(Y), sizeof(X))
        Y._fields_ = [(b'b', c_int)]

        class Z(X):
            pass

        self.assertEqual(sizeof(X), sizeof(c_int))
        self.assertEqual(sizeof(Y), sizeof(c_int) * 2)
        self.assertEqual(sizeof(Z), sizeof(c_int))
        self.assertEqual(X._fields_, [(b'a', c_int)])
        self.assertEqual(Y._fields_, [(b'b', c_int)])
        self.assertEqual(Z._fields_, [(b'a', c_int)])
        return


class StructureTestCase(unittest.TestCase):
    formats = {b'c': c_char, b'b': c_byte, 
       b'B': c_ubyte, 
       b'h': c_short, 
       b'H': c_ushort, 
       b'i': c_int, 
       b'I': c_uint, 
       b'l': c_long, 
       b'L': c_ulong, 
       b'q': c_longlong, 
       b'Q': c_ulonglong, 
       b'f': c_float, 
       b'd': c_double}

    def test_simple_structs(self):
        for code, tp in self.formats.items():

            class X(Structure):
                _fields_ = [
                 (
                  b'x', c_char),
                 (
                  b'y', tp)]

            self.assertEqual((sizeof(X), code), (
             calcsize(b'c%c0%c' % (code, code)), code))

        return

    def test_unions(self):
        for code, tp in self.formats.items():

            class X(Union):
                _fields_ = [
                 (
                  b'x', c_char),
                 (
                  b'y', tp)]

            self.assertEqual((sizeof(X), code), (
             calcsize(b'%c' % code), code))

        return

    def test_struct_alignment(self):

        class X(Structure):
            _fields_ = [(b'x', c_char * 3)]

        self.assertEqual(alignment(X), calcsize(b's'))
        self.assertEqual(sizeof(X), calcsize(b'3s'))

        class Y(Structure):
            _fields_ = [
             (
              b'x', c_char * 3),
             (
              b'y', c_int)]

        self.assertEqual(alignment(Y), alignment(c_int))
        self.assertEqual(sizeof(Y), calcsize(b'3si'))

        class SI(Structure):
            _fields_ = [
             (
              b'a', X),
             (
              b'b', Y)]

        self.assertEqual(alignment(SI), max(alignment(Y), alignment(X)))
        self.assertEqual(sizeof(SI), calcsize(b'3s0i 3si 0i'))

        class IS(Structure):
            _fields_ = [
             (
              b'b', Y),
             (
              b'a', X)]

        self.assertEqual(alignment(SI), max(alignment(X), alignment(Y)))
        self.assertEqual(sizeof(IS), calcsize(b'3si 3s 0i'))

        class XX(Structure):
            _fields_ = [
             (
              b'a', X),
             (
              b'b', X)]

        self.assertEqual(alignment(XX), alignment(X))
        self.assertEqual(sizeof(XX), calcsize(b'3s 3s 0s'))
        return

    def test_empty(self):

        class X(Structure):
            _fields_ = []

        class Y(Union):
            _fields_ = []

        self.assertTrue(alignment(X) == alignment(Y) == 1)
        self.assertTrue(sizeof(X) == sizeof(Y) == 0)

        class XX(Structure):
            _fields_ = [
             (
              b'a', X),
             (
              b'b', X)]

        self.assertEqual(alignment(XX), 1)
        self.assertEqual(sizeof(XX), 0)
        return

    def test_fields(self):

        class X(Structure):
            _fields_ = [
             (
              b'x', c_int),
             (
              b'y', c_char)]

        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, sizeof(c_int))
        self.assertEqual(X.y.offset, sizeof(c_int))
        self.assertEqual(X.y.size, sizeof(c_char))
        self.assertRaises((TypeError, AttributeError), setattr, X.x, b'offset', 92)
        self.assertRaises((TypeError, AttributeError), setattr, X.x, b'size', 92)

        class X(Union):
            _fields_ = [
             (
              b'x', c_int),
             (
              b'y', c_char)]

        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, sizeof(c_int))
        self.assertEqual(X.y.offset, 0)
        self.assertEqual(X.y.size, sizeof(c_char))
        self.assertRaises((TypeError, AttributeError), setattr, X.x, b'offset', 92)
        self.assertRaises((TypeError, AttributeError), setattr, X.x, b'size', 92)
        return

    def test_packed(self):

        class X(Structure):
            _fields_ = [
             (
              b'a', c_byte),
             (
              b'b', c_longlong)]
            _pack_ = 1

        self.assertEqual(sizeof(X), 9)
        self.assertEqual(X.b.offset, 1)

        class X(Structure):
            _fields_ = [
             (
              b'a', c_byte),
             (
              b'b', c_longlong)]
            _pack_ = 2

        self.assertEqual(sizeof(X), 10)
        self.assertEqual(X.b.offset, 2)
        import struct
        longlong_size = struct.calcsize(b'q')
        longlong_align = struct.calcsize(b'bq') - longlong_size

        class X(Structure):
            _fields_ = [
             (
              b'a', c_byte),
             (
              b'b', c_longlong)]
            _pack_ = 4

        self.assertEqual(sizeof(X), min(4, longlong_align) + longlong_size)
        self.assertEqual(X.b.offset, min(4, longlong_align))

        class X(Structure):
            _fields_ = [
             (
              b'a', c_byte),
             (
              b'b', c_longlong)]
            _pack_ = 8

        self.assertEqual(sizeof(X), min(8, longlong_align) + longlong_size)
        self.assertEqual(X.b.offset, min(8, longlong_align))
        d = {b'_fields_': [(b'a', b'b'),
                       (b'b', b'q')], 
           b'_pack_': (-1)}
        self.assertRaises(ValueError, type(Structure), b'X', (Structure,), d)
        d = {b'_fields_': [(b'a', c_byte)], b'_pack_': (_testcapi.INT_MAX + 1)}
        self.assertRaises(ValueError, type(Structure), b'X', (Structure,), d)
        d = {b'_fields_': [(b'a', c_byte)], b'_pack_': (_testcapi.UINT_MAX + 2)}
        self.assertRaises(ValueError, type(Structure), b'X', (Structure,), d)
        return

    def test_initializers(self):

        class Person(Structure):
            _fields_ = [
             (
              b'name', c_char * 6),
             (
              b'age', c_int)]

        self.assertRaises(TypeError, Person, 42)
        self.assertRaises(ValueError, Person, b'asldkjaslkdjaslkdj')
        self.assertRaises(TypeError, Person, b'Name', b'HI')
        self.assertEqual(Person(b'12345', 5).name, b'12345')
        self.assertEqual(Person(b'123456', 5).name, b'123456')
        self.assertRaises(ValueError, Person, b'1234567', 5)
        return

    def test_conflicting_initializers(self):

        class POINT(Structure):
            _fields_ = [
             (
              b'x', c_int), (b'y', c_int)]

        self.assertRaises(TypeError, POINT, 2, 3, x=4)
        self.assertRaises(TypeError, POINT, 2, 3, y=4)
        self.assertRaises(TypeError, POINT, 2, 3, 4)
        return

    def test_keyword_initializers(self):

        class POINT(Structure):
            _fields_ = [
             (
              b'x', c_int), (b'y', c_int)]

        pt = POINT(1, 2)
        self.assertEqual((pt.x, pt.y), (1, 2))
        pt = POINT(y=2, x=1)
        self.assertEqual((pt.x, pt.y), (1, 2))
        return

    def test_invalid_field_types(self):

        class POINT(Structure):
            pass

        self.assertRaises(TypeError, setattr, POINT, b'_fields_', [(b'x', 1), (b'y', 2)])
        return

    def test_invalid_name(self):

        def declare_with_name(name):

            class S(Structure):
                _fields_ = [
                 (
                  name, c_int)]

            return

        self.assertRaises(TypeError, declare_with_name, u'x\xe9')
        return

    def test_intarray_fields(self):

        class SomeInts(Structure):
            _fields_ = [
             (
              b'a', c_int * 4)]

        self.assertEqual(SomeInts((1, 2)).a[:], [1, 2, 0, 0])
        self.assertEqual(SomeInts((1, 2)).a[::], [1, 2, 0, 0])
        self.assertEqual(SomeInts((1, 2)).a[::-1], [0, 0, 2, 1])
        self.assertEqual(SomeInts((1, 2)).a[::2], [1, 0])
        self.assertEqual(SomeInts((1, 2)).a[1:5:6], [2])
        self.assertEqual(SomeInts((1, 2)).a[6:4:-1], [])
        self.assertEqual(SomeInts((1, 2, 3, 4)).a[:], [1, 2, 3, 4])
        self.assertEqual(SomeInts((1, 2, 3, 4)).a[::], [1, 2, 3, 4])
        self.assertRaises(RuntimeError, SomeInts, (1, 2, 3, 4, 5))
        return

    def test_nested_initializers(self):

        class Phone(Structure):
            _fields_ = [
             (
              b'areacode', c_char * 6),
             (
              b'number', c_char * 12)]

        class Person(Structure):
            _fields_ = [
             (
              b'name', c_char * 12),
             (
              b'phone', Phone),
             (
              b'age', c_int)]

        p = Person(b'Someone', (b'1234', b'5678'), 5)
        self.assertEqual(p.name, b'Someone')
        self.assertEqual(p.phone.areacode, b'1234')
        self.assertEqual(p.phone.number, b'5678')
        self.assertEqual(p.age, 5)
        return

    @need_symbol(b'c_wchar')
    def test_structures_with_wchar(self):

        class PersonW(Structure):
            _fields_ = [
             (
              b'name', c_wchar * 12),
             (
              b'age', c_int)]

        p = PersonW(u'Someone')
        self.assertEqual(p.name, b'Someone')
        self.assertEqual(PersonW(u'1234567890').name, u'1234567890')
        self.assertEqual(PersonW(u'12345678901').name, u'12345678901')
        self.assertEqual(PersonW(u'123456789012').name, u'123456789012')
        self.assertRaises(ValueError, PersonW, u'1234567890123')
        return

    def test_init_errors(self):

        class Phone(Structure):
            _fields_ = [
             (
              b'areacode', c_char * 6),
             (
              b'number', c_char * 12)]

        class Person(Structure):
            _fields_ = [
             (
              b'name', c_char * 12),
             (
              b'phone', Phone),
             (
              b'age', c_int)]

        cls, msg = self.get_except(Person, b'Someone', (1, 2))
        self.assertEqual(cls, RuntimeError)
        if issubclass(Exception, object):
            self.assertEqual(msg, b"(Phone) <type 'exceptions.TypeError'>: expected string or Unicode object, int found")
        else:
            self.assertEqual(msg, b'(Phone) exceptions.TypeError: expected string or Unicode object, int found')
        cls, msg = self.get_except(Person, b'Someone', (b'a', b'b', b'c'))
        self.assertEqual(cls, RuntimeError)
        if issubclass(Exception, object):
            self.assertEqual(msg, b"(Phone) <type 'exceptions.TypeError'>: too many initializers")
        else:
            self.assertEqual(msg, b'(Phone) exceptions.TypeError: too many initializers')
        return

    def test_huge_field_name(self):

        def create_class(length):

            class S(Structure):
                _fields_ = [
                 (
                  b'x' * length, c_int)]

            return

        for length in [10 ** i for i in range(0, 8)]:
            try:
                create_class(length)
            except MemoryError:
                pass

        return

    def get_except(self, func, *args):
        try:
            func(*args)
        except Exception as detail:
            return (
             detail.__class__, str(detail))

        return

    @unittest.skip(b'test disabled')
    def test_subclass_creation(self):
        meta = type(Structure)
        cls, msg = self.get_except(meta, b'X', (Structure,), {})
        self.assertEqual((cls, msg), (
         AttributeError, b"class must define a '_fields_' attribute"))
        return

    def test_abstract_class(self):

        class X(Structure):
            _abstract_ = b'something'

        cls, msg = self.get_except(eval, b'X()', locals())
        self.assertEqual((cls, msg), (TypeError, b'abstract class'))
        return

    def test_methods(self):
        self.assertIn(b'in_dll', dir(type(Structure)))
        self.assertIn(b'from_address', dir(type(Structure)))
        self.assertIn(b'in_dll', dir(type(Structure)))
        return

    def test_positional_args(self):

        class W(Structure):
            _fields_ = [
             (
              b'a', c_int), (b'b', c_int)]

        class X(W):
            _fields_ = [
             (
              b'c', c_int)]

        class Y(X):
            pass

        class Z(Y):
            _fields_ = [
             (
              b'd', c_int), (b'e', c_int), (b'f', c_int)]

        z = Z(1, 2, 3, 4, 5, 6)
        self.assertEqual((z.a, z.b, z.c, z.d, z.e, z.f), (1, 2, 3, 4, 5, 6))
        z = Z(1)
        self.assertEqual((z.a, z.b, z.c, z.d, z.e, z.f), (1, 0, 0, 0, 0, 0))
        self.assertRaises(TypeError, (lambda : Z(1, 2, 3, 4, 5, 6, 7)))
        return

    def test_pass_by_value(self):

        class X(Structure):
            _fields_ = [
             (
              b'first', c_ulong),
             (
              b'second', c_ulong),
             (
              b'third', c_ulong)]

        s = X()
        s.first = 3735928559L
        s.second = 3405691582L
        s.third = 195894762
        dll = CDLL(_ctypes_test.__file__)
        func = dll._testfunc_large_struct_update_value
        func.argtypes = (X,)
        func.restype = None
        func(s)
        self.assertEqual(s.first, 3735928559L)
        self.assertEqual(s.second, 3405691582L)
        self.assertEqual(s.third, 195894762)
        return


class PointerMemberTestCase(unittest.TestCase):

    def test(self):

        class S(Structure):
            _fields_ = [
             (
              b'array', POINTER(c_int))]

        s = S()
        s.array = (c_int * 3)(1, 2, 3)
        items = [s.array[i] for i in range(3)]
        self.assertEqual(items, [1, 2, 3])
        s.array[0] = 42
        items = [s.array[i] for i in range(3)]
        self.assertEqual(items, [42, 2, 3])
        s.array[0] = 1
        items = [s.array[i] for i in range(3)]
        self.assertEqual(items, [1, 2, 3])
        return

    def test_none_to_pointer_fields(self):

        class S(Structure):
            _fields_ = [
             (
              b'x', c_int),
             (
              b'p', POINTER(c_int))]

        s = S()
        s.x = 12345678
        s.p = None
        self.assertEqual(s.x, 12345678)
        return


class TestRecursiveStructure(unittest.TestCase):

    def test_contains_itself(self):

        class Recursive(Structure):
            pass

        try:
            Recursive._fields_ = [
             (
              b'next', Recursive)]
        except AttributeError as details:
            self.assertIn(b'Structure or union cannot contain itself', str(details))
        else:
            self.fail(b'Structure or union cannot contain itself')

        return

    def test_vice_versa(self):

        class First(Structure):
            pass

        class Second(Structure):
            pass

        First._fields_ = [
         (
          b'second', Second)]
        try:
            Second._fields_ = [(b'first', First)]
        except AttributeError as details:
            self.assertIn(b'_fields_ is final', str(details))
        else:
            self.fail(b'AttributeError not raised')

        return


if __name__ == b'__main__':
    unittest.main()
