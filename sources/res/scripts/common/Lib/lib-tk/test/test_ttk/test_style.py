import unittest, Tkinter as tkinter, ttk
from test.test_support import requires, run_unittest
from test_ttk.support import AbstractTkTest
requires(b'gui')

class StyleTest(AbstractTkTest, unittest.TestCase):

    def setUp(self):
        super(StyleTest, self).setUp()
        self.style = ttk.Style(self.root)
        return

    def test_configure(self):
        style = self.style
        style.configure(b'TButton', background=b'yellow')
        self.assertEqual(style.configure(b'TButton', b'background'), b'yellow')
        self.assertIsInstance(style.configure(b'TButton'), dict)
        return

    def test_map(self):
        style = self.style
        style.map(b'TButton', background=[(b'active', b'background', b'blue')])
        self.assertEqual(style.map(b'TButton', b'background'), [(b'active', b'background', b'blue')] if self.wantobjects else [
         (b'active background', b'blue')])
        self.assertIsInstance(style.map(b'TButton'), dict)
        return

    def test_lookup(self):
        style = self.style
        style.configure(b'TButton', background=b'yellow')
        style.map(b'TButton', background=[(b'active', b'background', b'blue')])
        self.assertEqual(style.lookup(b'TButton', b'background'), b'yellow')
        self.assertEqual(style.lookup(b'TButton', b'background', [
         b'active', b'background']), b'blue')
        self.assertEqual(style.lookup(b'TButton', b'optionnotdefined', default=b'iknewit'), b'iknewit')
        return

    def test_layout(self):
        style = self.style
        self.assertRaises(tkinter.TclError, style.layout, b'NotALayout')
        tv_style = style.layout(b'Treeview')
        style.layout(b'Treeview', b'')
        self.assertEqual(style.layout(b'Treeview'), [
         (
          b'null', {b'sticky': b'nswe'})])
        style.layout(b'Treeview', tv_style)
        self.assertEqual(style.layout(b'Treeview'), tv_style)
        self.assertIsInstance(style.layout(b'TButton'), list)
        self.assertRaises(tkinter.TclError, style.layout, b'Treeview', [
         (
          b'name', {b'option': b'inexistent'})])
        return

    def test_theme_use(self):
        self.assertRaises(tkinter.TclError, self.style.theme_use, b'nonexistingname')
        curr_theme = self.style.theme_use()
        new_theme = None
        for theme in self.style.theme_names():
            if theme != curr_theme:
                new_theme = theme
                self.style.theme_use(theme)
                break
        else:
            return

        self.assertFalse(curr_theme == new_theme)
        self.assertFalse(new_theme != self.style.theme_use())
        self.style.theme_use(curr_theme)
        return


tests_gui = (
 StyleTest,)
if __name__ == b'__main__':
    run_unittest(*tests_gui)
