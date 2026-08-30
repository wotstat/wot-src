import unittest
from idlelib.idle_test.mock_tk import Var, Mbox
from idlelib import configSectionNameDialog as name_dialog_module
name_dialog = name_dialog_module.GetCfgSectionNameDialog

class Dummy_name_dialog(object):
    name_ok = name_dialog.name_ok.im_func
    Ok = name_dialog.Ok.im_func
    Cancel = name_dialog.Cancel.im_func
    used_names = [
     b'used']
    name = Var()
    result = None
    destroyed = False

    def grab_release(self):
        return

    def destroy(self):
        self.destroyed = True
        return


orig_mbox = name_dialog_module.tkMessageBox
showerror = Mbox.showerror

class ConfigNameTest(unittest.TestCase):
    dialog = Dummy_name_dialog()

    @classmethod
    def setUpClass(cls):
        name_dialog_module.tkMessageBox = Mbox
        return

    @classmethod
    def tearDownClass(cls):
        name_dialog_module.tkMessageBox = orig_mbox
        return

    def test_blank_name(self):
        self.dialog.name.set(b' ')
        self.assertEqual(self.dialog.name_ok(), b'')
        self.assertEqual(showerror.title, b'Name Error')
        self.assertIn(b'No', showerror.message)
        return

    def test_used_name(self):
        self.dialog.name.set(b'used')
        self.assertEqual(self.dialog.name_ok(), b'')
        self.assertEqual(showerror.title, b'Name Error')
        self.assertIn(b'use', showerror.message)
        return

    def test_long_name(self):
        self.dialog.name.set(b'good' * 8)
        self.assertEqual(self.dialog.name_ok(), b'')
        self.assertEqual(showerror.title, b'Name Error')
        self.assertIn(b'too long', showerror.message)
        return

    def test_good_name(self):
        self.dialog.name.set(b'  good ')
        showerror.title = b'No Error'
        self.assertEqual(self.dialog.name_ok(), b'good')
        self.assertEqual(showerror.title, b'No Error')
        return

    def test_ok(self):
        self.dialog.destroyed = False
        self.dialog.name.set(b'good')
        self.dialog.Ok()
        self.assertEqual(self.dialog.result, b'good')
        self.assertTrue(self.dialog.destroyed)
        return

    def test_cancel(self):
        self.dialog.destroyed = False
        self.dialog.Cancel()
        self.assertEqual(self.dialog.result, b'')
        self.assertTrue(self.dialog.destroyed)
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
