import unittest
from test.test_support import requires
from _tkinter import TclError

class TextTest(object):
    hw = b'hello\nworld'
    hwn = hw + b'\n'
    Text = None

    def setUp(self):
        self.text = self.Text()
        return

    def test_init(self):
        self.assertEqual(self.text.get(b'1.0'), b'\n')
        self.assertEqual(self.text.get(b'end'), b'')
        return

    def test_index_empty(self):
        index = self.text.index
        for dex in (-1.0, 0.3, b'1.-1', b'1.0', b'1.0 lineend', b'1.end', b'1.33', b'insert'):
            self.assertEqual(index(dex), b'1.0')

        for dex in (b'end', 2.0, b'2.1', b'33.44'):
            self.assertEqual(index(dex), b'2.0')

        return

    def test_index_data(self):
        index = self.text.index
        self.text.insert(b'1.0', self.hw)
        for dex in (-1.0, 0.3, b'1.-1', b'1.0'):
            self.assertEqual(index(dex), b'1.0')

        for dex in (b'1.0 lineend', b'1.end', b'1.33'):
            self.assertEqual(index(dex), b'1.5')

        for dex in (b'end', b'33.44'):
            self.assertEqual(index(dex), b'3.0')

        return

    def test_get(self):
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert(b'1.0', self.hw)
        Equal(get(b'end'), b'')
        Equal(get(b'end', b'end'), b'')
        Equal(get(b'1.0'), b'h')
        Equal(get(b'1.0', b'1.1'), b'h')
        Equal(get(b'1.0', b'1.3'), b'hel')
        Equal(get(b'1.1', b'1.3'), b'el')
        Equal(get(b'1.0', b'1.0 lineend'), b'hello')
        Equal(get(b'1.0', b'1.10'), b'hello')
        Equal(get(b'1.0 lineend'), b'\n')
        Equal(get(b'1.1', b'2.3'), b'ello\nwor')
        Equal(get(b'1.0', b'2.5'), self.hw)
        Equal(get(b'1.0', b'end'), self.hwn)
        Equal(get(b'0.0', b'5.0'), self.hwn)
        return

    def test_insert(self):
        insert = self.text.insert
        get = self.text.get
        Equal = self.assertEqual
        insert(b'1.0', self.hw)
        Equal(get(b'1.0', b'end'), self.hwn)
        insert(b'1.0', b'')
        Equal(get(b'1.0', b'end'), self.hwn)
        insert(b'1.0', b'*')
        Equal(get(b'1.0', b'end'), b'*hello\nworld\n')
        insert(b'1.0 lineend', b'*')
        Equal(get(b'1.0', b'end'), b'*hello*\nworld\n')
        insert(b'2.3', b'*')
        Equal(get(b'1.0', b'end'), b'*hello*\nwor*ld\n')
        insert(b'end', b'x')
        Equal(get(b'1.0', b'end'), b'*hello*\nwor*ldx\n')
        insert(b'1.4', b'x\n')
        Equal(get(b'1.0', b'end'), b'*helx\nlo*\nwor*ldx\n')
        return

    def test_no_delete(self):
        delete = self.text.delete
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert(b'1.0', self.hw)
        delete(b'insert')
        Equal(get(b'1.0', b'end'), self.hwn)
        delete(b'end')
        Equal(get(b'1.0', b'end'), self.hwn)
        delete(b'insert', b'end')
        Equal(get(b'1.0', b'end'), self.hwn)
        delete(b'insert', b'5.5')
        Equal(get(b'1.0', b'end'), self.hwn)
        delete(b'1.4', b'1.0')
        Equal(get(b'1.0', b'end'), self.hwn)
        delete(b'1.4', b'1.4')
        Equal(get(b'1.0', b'end'), self.hwn)
        return

    def test_delete_char(self):
        delete = self.text.delete
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert(b'1.0', self.hw)
        delete(b'1.0')
        Equal(get(b'1.0', b'1.end'), b'ello')
        delete(b'1.0', b'1.1')
        Equal(get(b'1.0', b'1.end'), b'llo')
        delete(b'1.end')
        Equal(get(b'1.0', b'1.end'), b'lloworld')
        self.text.insert(b'1.3', b'\n')
        delete(b'1.10')
        Equal(get(b'1.0', b'1.end'), b'lloworld')
        self.text.insert(b'1.3', b'\n')
        delete(b'1.3', b'2.0')
        Equal(get(b'1.0', b'1.end'), b'lloworld')
        return

    def test_delete_slice(self):
        delete = self.text.delete
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert(b'1.0', self.hw)
        delete(b'1.0', b'1.0 lineend')
        Equal(get(b'1.0', b'end'), b'\nworld\n')
        delete(b'1.0', b'end')
        Equal(get(b'1.0', b'end'), b'\n')
        self.text.insert(b'1.0', self.hw)
        delete(b'1.0', b'2.0')
        Equal(get(b'1.0', b'end'), b'world\n')
        delete(b'1.0', b'end')
        Equal(get(b'1.0', b'end'), b'\n')
        self.text.insert(b'1.0', self.hw)
        delete(b'1.2', b'2.3')
        Equal(get(b'1.0', b'end'), b'held\n')
        return

    def test_multiple_lines(self):
        self.text.insert(b'1.0', b'hello')
        self.text.insert(b'1.3', b'1\n2\n3\n4\n5')
        self.assertEqual(self.text.get(b'1.0', b'end'), b'hel1\n2\n3\n4\n5lo\n')
        self.text.delete(b'1.3', b'5.1')
        self.assertEqual(self.text.get(b'1.0', b'end'), b'hello\n')
        return

    def test_compare(self):
        compare = self.text.compare
        Equal = self.assertEqual
        self.text.insert(b'1.0', b'First\nSecond\nThird\n')
        self.assertRaises(TclError, compare, b'2.2', b'op', b'2.2')
        for op, less1, less0, equal, greater0, greater1 in (
         (
          b'<', True, True, False, False, False),
         (
          b'<=', True, True, True, False, False),
         (
          b'>', False, False, False, True, True),
         (
          b'>=', False, False, True, True, True),
         (
          b'==', False, False, True, False, False),
         (
          b'!=', True, True, False, True, True)):
            Equal(compare(b'1.1', op, b'2.2'), less1, op)
            Equal(compare(b'2.1', op, b'2.2'), less0, op)
            Equal(compare(b'2.2', op, b'2.2'), equal, op)
            Equal(compare(b'2.3', op, b'2.2'), greater0, op)
            Equal(compare(b'3.3', op, b'2.2'), greater1, op)

        return


class MockTextTest(TextTest, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from idlelib.idle_test.mock_tk import Text
        cls.Text = Text
        return

    def test_decode(self):
        decode = self.text._decode
        Equal = self.assertEqual
        self.text.insert(b'1.0', self.hw)
        Equal(decode(b'end', -1), (2, 5))
        Equal(decode(b'3.1', -1), (2, 5))
        Equal(decode(b'end', 0), (2, 6))
        Equal(decode(b'3.1', 0), (2, 6))
        return


class TkTextTest(TextTest, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        requires(b'gui')
        from Tkinter import Tk, Text
        cls.Text = Text
        cls.root = Tk()
        return

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()
        del cls.root
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
