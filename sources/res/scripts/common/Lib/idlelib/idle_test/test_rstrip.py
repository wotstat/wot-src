import unittest, idlelib.RstripExtension as rs
from idlelib.idle_test.mock_idle import Editor

class rstripTest(unittest.TestCase):

    def test_rstrip_line(self):
        editor = Editor()
        text = editor.text
        do_rstrip = rs.RstripExtension(editor).do_rstrip
        do_rstrip()
        self.assertEqual(text.get(b'1.0', b'insert'), b'')
        text.insert(b'1.0', b'     ')
        do_rstrip()
        self.assertEqual(text.get(b'1.0', b'insert'), b'')
        text.insert(b'1.0', b'     \n')
        do_rstrip()
        self.assertEqual(text.get(b'1.0', b'insert'), b'\n')
        return

    def test_rstrip_multiple(self):
        editor = Editor()
        text = editor.text
        do_rstrip = rs.RstripExtension(editor).do_rstrip
        original = b'Line with an ending tab    \nLine ending in 5 spaces     \nLinewithnospaces\n    indented line\n    indented line with trailing space \n    '
        stripped = b'Line with an ending tab\nLine ending in 5 spaces\nLinewithnospaces\n    indented line\n    indented line with trailing space\n'
        text.insert(b'1.0', original)
        do_rstrip()
        self.assertEqual(text.get(b'1.0', b'insert'), stripped)
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
