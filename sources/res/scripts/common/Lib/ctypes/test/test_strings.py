import unittest
from ctypes import *
from ctypes.test import need_symbol
from test import test_support

class StringArrayTestCase(unittest.TestCase):

    def test(self):
        BUF = c_char * 4
        buf = BUF(b'a', b'b', b'c')
        self.assertEqual(buf.value, b'abc')
        self.assertEqual(buf.raw, b'abc\x00')
        buf.value = b'ABCD'
        self.assertEqual(buf.value, b'ABCD')
        self.assertEqual(buf.raw, b'ABCD')
        buf.value = b'x'
        self.assertEqual(buf.value, b'x')
        self.assertEqual(buf.raw, b'x\x00CD')
        buf[1] = b'Z'
        self.assertEqual(buf.value, b'xZCD')
        self.assertEqual(buf.raw, b'xZCD')
        self.assertRaises(ValueError, setattr, buf, b'value', b'aaaaaaaa')
        self.assertRaises(TypeError, setattr, buf, b'value', 42)
        return

    def test_c_buffer_value(self, memoryview=memoryview):
        buf = c_buffer(32)
        buf.value = b'Hello, World'
        self.assertEqual(buf.value, b'Hello, World')
        self.assertRaises(TypeError, setattr, buf, b'value', memoryview(b'Hello, World'))
        self.assertRaises(TypeError, setattr, buf, b'value', memoryview(b'abc'))
        self.assertRaises(ValueError, setattr, buf, b'raw', memoryview(b'x' * 100))
        return

    def test_c_buffer_raw(self, memoryview=memoryview):
        buf = c_buffer(32)
        buf.raw = memoryview(b'Hello, World')
        self.assertEqual(buf.value, b'Hello, World')
        self.assertRaises(TypeError, setattr, buf, b'value', memoryview(b'abc'))
        self.assertRaises(ValueError, setattr, buf, b'raw', memoryview(b'x' * 100))
        return

    def test_c_buffer_deprecated(self):
        with test_support.check_py3k_warnings():
            self.test_c_buffer_value(buffer)
            self.test_c_buffer_raw(buffer)
        return

    def test_param_1(self):
        BUF = c_char * 4
        buf = BUF()
        return

    def test_param_2(self):
        BUF = c_char * 4
        buf = BUF()
        return

    def test_del_segfault(self):
        BUF = c_char * 4
        buf = BUF()
        with self.assertRaises(AttributeError):
            del buf.raw
        return


@need_symbol(b'c_wchar')
class WStringArrayTestCase(unittest.TestCase):

    def test(self):
        BUF = c_wchar * 4
        buf = BUF(u'a', u'b', u'c')
        self.assertEqual(buf.value, u'abc')
        buf.value = u'ABCD'
        self.assertEqual(buf.value, u'ABCD')
        buf.value = u'x'
        self.assertEqual(buf.value, u'x')
        buf[1] = u'Z'
        self.assertEqual(buf.value, u'xZCD')
        return


class StringTestCase(unittest.TestCase):

    @unittest.skip(b'test disabled')
    def test_basic_strings(self):
        cs = c_string(b'abcdef')
        self.assertRaises(TypeError, len, cs)
        self.assertEqual(sizeof(cs), 7)
        self.assertEqual(cs.value, b'abcdef')
        self.assertEqual(c_string(b'abc\x00def').value, b'abc')
        self.assertEqual(cs.raw, b'abcdef\x00')
        self.assertEqual(c_string(b'abc\x00def').raw, b'abc\x00def\x00')
        cs.value = b'ab'
        self.assertEqual(cs.value, b'ab')
        self.assertEqual(cs.raw, b'ab\x00\x00\x00\x00\x00')
        cs.raw = b'XY'
        self.assertEqual(cs.value, b'XY')
        self.assertEqual(cs.raw, b'XY\x00\x00\x00\x00\x00')
        self.assertRaises(TypeError, c_string, u'123')
        return

    @unittest.skip(b'test disabled')
    def test_sized_strings(self):
        self.assertRaises(TypeError, c_string, None)
        self.assertEqual(len(c_string(32).raw), 32)
        self.assertRaises(ValueError, c_string, -1)
        self.assertRaises(ValueError, c_string, 0)
        self.assertEqual(c_string(2).raw[-1], b'\x00')
        self.assertEqual(len(c_string(2).raw), 2)
        return

    @unittest.skip(b'test disabled')
    def test_initialized_strings(self):
        self.assertEqual(c_string(b'ab', 4).raw[:2], b'ab')
        self.assertEqual(c_string(b'ab', 4).raw[:2:], b'ab')
        self.assertEqual(c_string(b'ab', 4).raw[:2:-1], b'ba')
        self.assertEqual(c_string(b'ab', 4).raw[:2:2], b'a')
        self.assertEqual(c_string(b'ab', 4).raw[-1], b'\x00')
        self.assertEqual(c_string(b'ab', 2).raw, b'a\x00')
        return

    @unittest.skip(b'test disabled')
    def test_toolong(self):
        cs = c_string(b'abcdef')
        self.assertRaises(ValueError, setattr, cs, b'value', b'123456789012345')
        self.assertRaises(ValueError, setattr, cs, b'value', b'1234567')
        return

    @unittest.skip(b'test disabled')
    def test_perf(self):
        check_perf()
        return


@need_symbol(b'c_wchar')
class WStringTestCase(unittest.TestCase):

    def test_wchar(self):
        c_wchar(u'x')
        repr(byref(c_wchar(u'x')))
        c_wchar(b'x')
        return

    @unittest.skip(b'test disabled')
    def test_basic_wstrings(self):
        cs = c_wstring(u'abcdef')
        self.assertEqual(sizeof(cs), 14)
        self.assertEqual(cs.value, u'abcdef')
        self.assertEqual(c_wstring(u'abc\x00def').value, u'abc')
        self.assertEqual(c_wstring(u'abc\x00def').value, u'abc')
        self.assertEqual(cs.raw, u'abcdef\x00')
        self.assertEqual(c_wstring(u'abc\x00def').raw, u'abc\x00def\x00')
        cs.value = u'ab'
        self.assertEqual(cs.value, u'ab')
        self.assertEqual(cs.raw, u'ab\x00\x00\x00\x00\x00')
        self.assertRaises(TypeError, c_wstring, b'123')
        self.assertRaises(ValueError, c_wstring, 0)
        return

    @unittest.skip(b'test disabled')
    def test_toolong(self):
        cs = c_wstring(u'abcdef')
        self.assertRaises(ValueError, setattr, cs, b'value', u'123456789012345')
        self.assertRaises(ValueError, setattr, cs, b'value', u'1234567')
        return


def run_test(rep, msg, func, arg):
    items = range(rep)
    from time import clock
    start = clock()
    for i in items:
        func(arg)
        func(arg)
        func(arg)
        func(arg)
        func(arg)

    stop = clock()
    print b'%20s: %.2f us' % (msg, (stop - start) * 1000000.0 / 5 / rep)
    return


def check_perf():
    REP = 200000
    run_test(REP, b'c_string(None)', c_string, None)
    run_test(REP, b"c_string('abc')", c_string, b'abc')
    return


if __name__ == b'__main__':
    unittest.main()
