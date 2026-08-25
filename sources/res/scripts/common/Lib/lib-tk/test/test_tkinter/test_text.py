import unittest, Tkinter as tkinter
from test.test_support import requires, run_unittest
from test_ttk.support import AbstractTkTest
requires(b'gui')

class TextTest(AbstractTkTest, unittest.TestCase):

    def setUp(self):
        super(TextTest, self).setUp()
        self.text = tkinter.Text(self.root)
        return

    def test_debug(self):
        text = self.text
        olddebug = text.debug()
        try:
            text.debug(0)
            self.assertEqual(text.debug(), 0)
            text.debug(1)
            self.assertEqual(text.debug(), 1)
        finally:
            text.debug(olddebug)
            self.assertEqual(text.debug(), olddebug)

        return

    def test_search(self):
        text = self.text
        self.assertRaises(tkinter.TclError, text.search, None, b'1.0')
        self.assertRaises(tkinter.TclError, text.search, b'a', None)
        self.assertRaises(tkinter.TclError, text.search, None, None)
        self.assertRaises(tkinter.TclError, text.search, b'', 0)
        text.insert(b'1.0', b'hi-test')
        self.assertEqual(text.search(b'-test', b'1.0', b'end'), b'1.2')
        self.assertEqual(text.search(b'test', b'1.0', b'end'), b'1.3')
        return


tests_gui = (
 TextTest,)
if __name__ == b'__main__':
    run_unittest(*tests_gui)
