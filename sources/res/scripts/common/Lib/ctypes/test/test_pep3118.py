import unittest
from ctypes import *
import re, sys
if sys.byteorder == b'little':
    THIS_ENDIAN = b'<'
    OTHER_ENDIAN = b'>'
else:
    THIS_ENDIAN = b'>'
    OTHER_ENDIAN = b'<'

def normalize(format):
    if format is None:
        return b''
    else:
        format = format.replace(OTHER_ENDIAN, THIS_ENDIAN)
        return re.sub(b'\\s', b'', format)


class Test(unittest.TestCase):

    def test_native_types(self):
        for tp, fmt, shape, itemtp in native_types:
            ob = tp()
            v = memoryview(ob)
            try:
                self.assertEqual(normalize(v.format), normalize(fmt))
                if shape is not None:
                    self.assertEqual(len(v), shape[0])
                else:
                    self.assertEqual(len(v) * sizeof(itemtp), sizeof(ob))
                self.assertEqual(v.itemsize, sizeof(itemtp))
                self.assertEqual(v.shape, shape)
                self.assertEqual(v.strides, None)
                self.assertFalse(v.readonly)
                if v.shape:
                    n = 1
                    for dim in v.shape:
                        n = n * dim

                    self.assertEqual(n * v.itemsize, len(v.tobytes()))
            except:
                print tp
                raise

        return

    def test_endian_types(self):
        for tp, fmt, shape, itemtp in endian_types:
            ob = tp()
            v = memoryview(ob)
            try:
                self.assertEqual(v.format, fmt)
                if shape is not None:
                    self.assertEqual(len(v), shape[0])
                else:
                    self.assertEqual(len(v) * sizeof(itemtp), sizeof(ob))
                self.assertEqual(v.itemsize, sizeof(itemtp))
                self.assertEqual(v.shape, shape)
                self.assertEqual(v.strides, None)
                self.assertFalse(v.readonly)
                if v.shape:
                    n = 1
                    for dim in v.shape:
                        n = n * dim

                    self.assertEqual(n, len(v))
            except:
                print tp
                raise

        return


class Point(Structure):
    _fields_ = [
     (
      b'x', c_long), (b'y', c_long)]


class PackedPoint(Structure):
    _pack_ = 2
    _fields_ = [(b'x', c_long), (b'y', c_long)]


class Point2(Structure):
    pass


Point2._fields_ = [
 (
  b'x', c_long), (b'y', c_long)]

class EmptyStruct(Structure):
    _fields_ = []


class aUnion(Union):
    _fields_ = [
     (
      b'a', c_int)]


class StructWithArrays(Structure):
    _fields_ = [
     (
      b'x', c_long * 3 * 2), (b'y', Point * 4)]


class Incomplete(Structure):
    pass


class Complete(Structure):
    pass


PComplete = POINTER(Complete)
Complete._fields_ = [(b'a', c_long)]
s_bool = {1: b'?', 2: b'H', 4: b'L', 8: b'Q'}[sizeof(c_bool)]
s_short = {2: b'h', 4: b'l', 8: b'q'}[sizeof(c_short)]
s_ushort = {2: b'H', 4: b'L', 8: b'Q'}[sizeof(c_ushort)]
s_int = {2: b'h', 4: b'i', 8: b'q'}[sizeof(c_int)]
s_uint = {2: b'H', 4: b'I', 8: b'Q'}[sizeof(c_uint)]
s_long = {4: b'l', 8: b'q'}[sizeof(c_long)]
s_ulong = {4: b'L', 8: b'Q'}[sizeof(c_ulong)]
s_longlong = b'q'
s_ulonglong = b'Q'
s_float = b'f'
s_double = b'd'
s_longdouble = b'g'
if c_int is c_long:
    s_int = s_long
if c_uint is c_ulong:
    s_uint = s_ulong
if c_longlong is c_long:
    s_longlong = s_long
if c_ulonglong is c_ulong:
    s_ulonglong = s_ulong
if c_longdouble is c_double:
    s_longdouble = s_double
native_types = [
 (
  c_char, b'<c', None, c_char),
 (
  c_byte, b'<b', None, c_byte),
 (
  c_ubyte, b'<B', None, c_ubyte),
 (
  c_short, b'<' + s_short, None, c_short),
 (
  c_ushort, b'<' + s_ushort, None, c_ushort),
 (
  c_int, b'<' + s_int, None, c_int),
 (
  c_uint, b'<' + s_uint, None, c_uint),
 (
  c_long, b'<' + s_long, None, c_long),
 (
  c_ulong, b'<' + s_ulong, None, c_ulong),
 (
  c_longlong, b'<' + s_longlong, None, c_longlong),
 (
  c_ulonglong, b'<' + s_ulonglong, None, c_ulonglong),
 (
  c_float, b'<f', None, c_float),
 (
  c_double, b'<d', None, c_double),
 (
  c_longdouble, b'<' + s_longdouble, None, c_longdouble),
 (
  c_bool, b'<' + s_bool, None, c_bool),
 (
  py_object, b'<O', None, py_object),
 (
  POINTER(c_byte), b'&<b', None, POINTER(c_byte)),
 (
  POINTER(POINTER(c_long)), b'&&<' + s_long, None, POINTER(POINTER(c_long))),
 (
  c_double * 4, b'<d', (4,), c_double),
 (
  c_float * 4 * 3 * 2, b'<f', (2, 3, 4), c_float),
 (
  POINTER(c_short) * 2, b'&<' + s_short, (2,), POINTER(c_short)),
 (
  POINTER(c_short) * 2 * 3, b'&<' + s_short, (3, 2), POINTER(c_short)),
 (
  POINTER(c_short * 2), b'&(2)<' + s_short, None, POINTER(c_short)),
 (
  Point, (b'T{<l:x:<l:y:}').replace(b'l', s_long), None, Point),
 (
  PackedPoint, b'B', None, PackedPoint),
 (
  Point2, (b'T{<l:x:<l:y:}').replace(b'l', s_long), None, Point2),
 (
  EmptyStruct, b'T{}', None, EmptyStruct),
 (
  aUnion, b'B', None, aUnion),
 (
  StructWithArrays, (b'T{(2,3)<l:x:(4)T{<l:x:<l:y:}:y:}').replace(b'l', s_long), None, StructWithArrays),
 (
  StructWithArrays * 3, (b'T{(2,3)<l:x:(4)T{<l:x:<l:y:}:y:}').replace(b'l', s_long), (3,), StructWithArrays),
 (
  Incomplete, b'B', None, Incomplete),
 (
  POINTER(Incomplete), b'&B', None, POINTER(Incomplete)),
 (
  Complete, (b'T{<l:a:}').replace(b'l', s_long), None, Complete),
 (
  POINTER(Complete), b'&B', None, POINTER(Complete)),
 (
  CFUNCTYPE(None), b'X{}', None, CFUNCTYPE(None))]

class BEPoint(BigEndianStructure):
    _fields_ = [
     (
      b'x', c_long), (b'y', c_long)]


class LEPoint(LittleEndianStructure):
    _fields_ = [
     (
      b'x', c_long), (b'y', c_long)]


endian_types = [
 (
  BEPoint, (b'T{>l:x:>l:y:}').replace(b'l', s_long), None, BEPoint),
 (
  LEPoint, (b'T{<l:x:<l:y:}').replace(b'l', s_long), None, LEPoint),
 (
  POINTER(BEPoint), (b'&T{>l:x:>l:y:}').replace(b'l', s_long), None, POINTER(BEPoint)),
 (
  POINTER(LEPoint), (b'&T{<l:x:<l:y:}').replace(b'l', s_long), None, POINTER(LEPoint))]
if __name__ == b'__main__':
    unittest.main()
