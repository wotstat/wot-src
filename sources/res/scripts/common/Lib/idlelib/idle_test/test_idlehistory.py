import unittest
from test.test_support import requires
import Tkinter as tk
from Tkinter import Text as tkText
from idlelib.idle_test.mock_tk import Text as mkText
from idlelib.IdleHistory import History
from idlelib.configHandler import idleConf
line1 = b'a = 7'
line2 = b'b = a'

class StoreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = mkText()
        cls.history = History(cls.text)
        return

    def tearDown(self):
        self.text.delete(b'1.0', b'end')
        self.history.history = []
        return

    def test_init(self):
        self.assertIs(self.history.text, self.text)
        self.assertEqual(self.history.history, [])
        self.assertIsNone(self.history.prefix)
        self.assertIsNone(self.history.pointer)
        self.assertEqual(self.history.cyclic, idleConf.GetOption(b'main', b'History', b'cyclic', 1, b'bool'))
        return

    def test_store_short(self):
        self.history.store(b'a')
        self.assertEqual(self.history.history, [])
        self.history.store(b'  a  ')
        self.assertEqual(self.history.history, [])
        return

    def test_store_dup(self):
        self.history.store(line1)
        self.assertEqual(self.history.history, [line1])
        self.history.store(line2)
        self.assertEqual(self.history.history, [line1, line2])
        self.history.store(line1)
        self.assertEqual(self.history.history, [line2, line1])
        return

    def test_store_reset(self):
        self.history.prefix = line1
        self.history.pointer = 0
        self.history.store(line2)
        self.assertIsNone(self.history.prefix)
        self.assertIsNone(self.history.pointer)
        return


class TextWrapper:

    def __init__(self, master):
        self.text = tkText(master=master)
        self._bell = False
        return

    def __getattr__(self, name):
        return getattr(self.text, name)

    def bell(self):
        self._bell = True
        return


class FetchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        requires(b'gui')
        cls.root = tk.Tk()
        cls.root.withdraw()
        return

    def setUp(self):
        self.text = text = TextWrapper(self.root)
        text.insert(b'1.0', b'>>> ')
        text.mark_set(b'iomark', b'1.4')
        text.mark_gravity(b'iomark', b'left')
        self.history = History(text)
        self.history.history = [line1, line2]
        return

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()
        del cls.root
        return

    def fetch_test(self, reverse, line, prefix, index, bell=False):
        History = self.history
        History.fetch(reverse)
        Equal = self.assertEqual
        Equal(self.text.get(b'iomark', b'end-1c'), line)
        Equal(self.text._bell, bell)
        if bell:
            self.text._bell = False
        Equal(History.prefix, prefix)
        Equal(History.pointer, index)
        Equal(self.text.compare(b'insert', b'==', b'end-1c'), 1)
        return

    def test_fetch_prev_cyclic(self):
        prefix = b''
        test = self.fetch_test
        test(True, line2, prefix, 1)
        test(True, line1, prefix, 0)
        test(True, prefix, None, None, bell=True)
        return

    def test_fetch_next_cyclic(self):
        prefix = b''
        test = self.fetch_test
        test(False, line1, prefix, 0)
        test(False, line2, prefix, 1)
        test(False, prefix, None, None, bell=True)
        return

    def test_fetch_prev_prefix(self):
        prefix = b'a'
        self.text.insert(b'iomark', prefix)
        self.fetch_test(True, line1, prefix, 0)
        self.fetch_test(True, prefix, None, None, bell=True)
        return

    def test_fetch_next_prefix(self):
        prefix = b'a'
        self.text.insert(b'iomark', prefix)
        self.fetch_test(False, line1, prefix, 0)
        self.fetch_test(False, prefix, None, None, bell=True)
        return

    def test_fetch_prev_noncyclic(self):
        prefix = b''
        self.history.cyclic = False
        test = self.fetch_test
        test(True, line2, prefix, 1)
        test(True, line1, prefix, 0)
        test(True, line1, prefix, 0, bell=True)
        return

    def test_fetch_next_noncyclic(self):
        prefix = b''
        self.history.cyclic = False
        test = self.fetch_test
        test(False, prefix, None, None, bell=True)
        test(True, line2, prefix, 1)
        test(False, prefix, None, None, bell=True)
        test(False, prefix, None, None, bell=True)
        return

    def test_fetch_cursor_move(self):
        self.history.fetch(reverse=True)
        self.text.mark_set(b'insert', b'iomark')
        self.fetch_test(True, line2, None, None, bell=True)
        return

    def test_fetch_edit(self):
        self.history.fetch(reverse=True)
        self.text.delete(b'iomark', b'insert')
        self.text.insert(b'iomark', b'a =')
        self.fetch_test(True, line1, b'a =', 0)
        return

    def test_history_prev_next(self):
        self.history.history_prev(b'dummy event')
        self.assertEqual(self.history.pointer, 1)
        self.history.history_next(b'dummy event')
        self.assertEqual(self.history.pointer, None)
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=2)
