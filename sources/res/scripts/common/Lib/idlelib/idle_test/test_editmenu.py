from test.test_support import requires
import Tkinter as tk, unittest
from idlelib import PyShell

class PasteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        requires(b'gui')
        cls.root = root = tk.Tk()
        root.withdraw()
        PyShell.fix_x11_paste(root)
        cls.text = tk.Text(root)
        cls.entry = tk.Entry(root)
        cls.spin = tk.Spinbox(root)
        root.clipboard_clear()
        root.clipboard_append(b'two')
        return

    @classmethod
    def tearDownClass(cls):
        del cls.text
        del cls.entry
        del cls.spin
        cls.root.clipboard_clear()
        cls.root.update_idletasks()
        cls.root.update()
        cls.root.destroy()
        del cls.root
        return

    def test_paste_text_no_selection(self):
        text = self.text
        tag, ans = (b'', b'onetwo\n')
        text.delete(b'1.0', b'end')
        text.insert(b'1.0', b'one', tag)
        text.event_generate(b'<<Paste>>')
        self.assertEqual(text.get(b'1.0', b'end'), ans)
        return

    def test_paste_text_selection(self):
        text = self.text
        tag, ans = (b'sel', b'two\n')
        text.delete(b'1.0', b'end')
        text.insert(b'1.0', b'one', tag)
        text.event_generate(b'<<Paste>>')
        self.assertEqual(text.get(b'1.0', b'end'), ans)
        return

    def test_paste_entry_no_selection(self):
        entry = self.entry
        end, ans = (0, b'onetwo')
        entry.delete(0, b'end')
        entry.insert(0, b'one')
        entry.select_range(0, end)
        entry.event_generate(b'<<Paste>>')
        self.assertEqual(entry.get(), ans)
        return

    def test_paste_entry_selection(self):
        entry = self.entry
        end, ans = (b'end', b'two')
        entry.delete(0, b'end')
        entry.insert(0, b'one')
        entry.select_range(0, end)
        entry.event_generate(b'<<Paste>>')
        self.assertEqual(entry.get(), ans)
        return

    def test_paste_spin_no_selection(self):
        spin = self.spin
        end, ans = (0, b'onetwo')
        spin.delete(0, b'end')
        spin.insert(0, b'one')
        spin.selection(b'range', 0, end)
        spin.event_generate(b'<<Paste>>')
        self.assertEqual(spin.get(), ans)
        return

    def test_paste_spin_selection(self):
        spin = self.spin
        end, ans = (b'end', b'two')
        spin.delete(0, b'end')
        spin.insert(0, b'one')
        spin.selection(b'range', 0, end)
        spin.event_generate(b'<<Paste>>')
        self.assertEqual(spin.get(), ans)
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2)
