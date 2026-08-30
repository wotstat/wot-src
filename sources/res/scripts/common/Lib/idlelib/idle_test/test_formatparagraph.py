import unittest
from idlelib import FormatParagraph as fp
from idlelib.EditorWindow import EditorWindow
from Tkinter import Tk, Text
from test.test_support import requires

class Is_Get_Test(unittest.TestCase):
    test_comment = b'# This is a comment'
    test_nocomment = b'This is not a comment'
    trailingws_comment = b'# This is a comment   '
    leadingws_comment = b'    # This is a comment'
    leadingws_nocomment = b'    This is not a comment'

    def test_is_all_white(self):
        self.assertTrue(fp.is_all_white(b''))
        self.assertTrue(fp.is_all_white(b'\t\n\r\x0c\x0b'))
        self.assertFalse(fp.is_all_white(self.test_comment))
        return

    def test_get_indent(self):
        Equal = self.assertEqual
        Equal(fp.get_indent(self.test_comment), b'')
        Equal(fp.get_indent(self.trailingws_comment), b'')
        Equal(fp.get_indent(self.leadingws_comment), b'    ')
        Equal(fp.get_indent(self.leadingws_nocomment), b'    ')
        return

    def test_get_comment_header(self):
        Equal = self.assertEqual
        Equal(fp.get_comment_header(self.test_comment), b'#')
        Equal(fp.get_comment_header(self.trailingws_comment), b'#')
        Equal(fp.get_comment_header(self.leadingws_comment), b'    #')
        Equal(fp.get_comment_header(self.leadingws_nocomment), b'    ')
        Equal(fp.get_comment_header(self.test_nocomment), b'')
        return


class FindTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from idlelib.idle_test.mock_tk import Text
        cls.text = Text()
        return

    def runcase(self, inserttext, stopline, expected):
        text = self.text
        text.insert(b'1.0', inserttext)
        for line in range(1, stopline):
            linelength = int(text.index(b'%d.end' % line).split(b'.')[1])
            for col in (0, linelength // 2, linelength):
                tempindex = b'%d.%d' % (line, col)
                self.assertEqual(fp.find_paragraph(text, tempindex), expected)

        text.delete(b'1.0', b'end')
        return

    def test_find_comment(self):
        comment = b'# Comment block with no blank lines before\n# Comment line\n\n'
        self.runcase(comment, 3, (b'1.0', b'3.0', b'#', comment[0:58]))
        comment = b'\n# Comment block with whitespace line before and after\n# Comment line\n\n'
        self.runcase(comment, 4, (b'2.0', b'4.0', b'#', comment[1:70]))
        comment = b'\n    # Indented comment block with whitespace before and after\n    # Comment line\n\n'
        self.runcase(comment, 4, (b'2.0', b'4.0', b'    #', comment[1:82]))
        comment = b'\n# Single line comment\n\n'
        self.runcase(comment, 3, (b'2.0', b'3.0', b'#', comment[1:23]))
        comment = b'\n    # Single line comment with leading whitespace\n\n'
        self.runcase(comment, 3, (b'2.0', b'3.0', b'    #', comment[1:51]))
        comment = b'\n# Comment immediately followed by code\nx = 42\n\n'
        self.runcase(comment, 3, (b'2.0', b'3.0', b'#', comment[1:40]))
        comment = b'\n    # Indented comment immediately followed by code\nx = 42\n\n'
        self.runcase(comment, 3, (b'2.0', b'3.0', b'    #', comment[1:53]))
        comment = b'\n# Comment immediately followed by indented code\n    x = 42\n\n'
        self.runcase(comment, 3, (b'2.0', b'3.0', b'#', comment[1:49]))
        return

    def test_find_paragraph(self):
        teststring = b'"""String with no blank lines before\nString line\n"""\n\n'
        self.runcase(teststring, 4, (b'1.0', b'4.0', b'', teststring[0:53]))
        teststring = b'\n"""String with whitespace line before and after\nString line.\n"""\n\n'
        self.runcase(teststring, 5, (b'2.0', b'5.0', b'', teststring[1:66]))
        teststring = b'\n    """Indented string with whitespace before and after\n    Comment string.\n    """\n\n'
        self.runcase(teststring, 5, (b'2.0', b'5.0', b'    ', teststring[1:85]))
        teststring = b'\n"""Single line string."""\n\n'
        self.runcase(teststring, 3, (b'2.0', b'3.0', b'', teststring[1:27]))
        teststring = b'\n    """Single line string with leading whitespace."""\n\n'
        self.runcase(teststring, 3, (b'2.0', b'3.0', b'    ', teststring[1:55]))
        return


class ReformatFunctionTest(unittest.TestCase):

    def test_reformat_paragraph(self):
        Equal = self.assertEqual
        reform = fp.reformat_paragraph
        hw = b'O hello world'
        Equal(reform(b' ', 1), b' ')
        Equal(reform(b'Hello    world', 20), b'Hello  world')
        Equal(reform(hw, 1), b'O\nhello\nworld')
        Equal(reform(hw, 6), b'O\nhello\nworld')
        Equal(reform(hw, 7), b'O hello\nworld')
        Equal(reform(hw, 12), b'O hello\nworld')
        Equal(reform(hw, 13), b'O hello world')
        hw = b'\nO hello world'
        Equal(reform(hw, 1), b'\nO\nhello\nworld')
        Equal(reform(hw, 6), b'\nO\nhello\nworld')
        Equal(reform(hw, 7), b'\nO hello\nworld')
        Equal(reform(hw, 12), b'\nO hello\nworld')
        Equal(reform(hw, 13), b'\nO hello world')
        return


class ReformatCommentTest(unittest.TestCase):

    def test_reformat_comment(self):
        Equal = self.assertEqual
        test_string = b'    """this is a test of a reformat for a triple quoted string will it reformat to less than 70 characters for me?"""'
        result = fp.reformat_comment(test_string, 70, b'    ')
        expected = b'    """this is a test of a reformat for a triple quoted string will it\n    reformat to less than 70 characters for me?"""'
        Equal(result, expected)
        test_comment = b'# this is a test of a reformat for a triple quoted string will it reformat to less than 70 characters for me?'
        result = fp.reformat_comment(test_comment, 70, b'#')
        expected = b'# this is a test of a reformat for a triple quoted string will it\n# reformat to less than 70 characters for me?'
        Equal(result, expected)
        return


class FormatClassTest(unittest.TestCase):

    def test_init_close(self):
        instance = fp.FormatParagraph(b'editor')
        self.assertEqual(instance.editwin, b'editor')
        instance.close()
        self.assertEqual(instance.editwin, None)
        return


class TextWrapper:

    def __init__(self, master):
        self.text = Text(master=master)
        return

    def __getattr__(self, name):
        return getattr(self.text, name)

    def undo_block_start(self):
        return

    def undo_block_stop(self):
        return


class Editor:

    def __init__(self, root):
        self.text = TextWrapper(root)
        return

    get_selection_indices = EditorWindow.get_selection_indices.im_func


class FormatEventTest(unittest.TestCase):
    test_string = b"    '''this is a test of a reformat for a triple quoted string will it reformat to less than 70 characters for me?'''\n"
    multiline_test_string = b"    '''The first line is under the max width.\n    The second line's length is way over the max width. It goes on and on until it is over 100 characters long.\n    Same thing with the third line. It is also way over the max width, but FormatParagraph will fix it.\n    '''\n"
    multiline_test_comment = b"# The first line is under the max width.\n# The second line's length is way over the max width. It goes on and on until it is over 100 characters long.\n# Same thing with the third line. It is also way over the max width, but FormatParagraph will fix it.\n# The fourth line is short like the first line."

    @classmethod
    def setUpClass(cls):
        requires(b'gui')
        cls.root = Tk()
        editor = Editor(root=cls.root)
        cls.text = editor.text.text
        cls.formatter = fp.FormatParagraph(editor).format_paragraph_event
        return

    @classmethod
    def tearDownClass(cls):
        del cls.text
        del cls.formatter
        cls.root.destroy()
        del cls.root
        return

    def test_short_line(self):
        self.text.insert(b'1.0', b'Short line\n')
        self.formatter(b'Dummy')
        self.assertEqual(self.text.get(b'1.0', b'insert'), b'Short line\n')
        self.text.delete(b'1.0', b'end')
        return

    def test_long_line(self):
        text = self.text
        text.insert(b'1.0', self.test_string)
        text.mark_set(b'insert', b'1.0')
        self.formatter(b'ParameterDoesNothing', limit=70)
        result = text.get(b'1.0', b'insert')
        expected = b"    '''this is a test of a reformat for a triple quoted string will it\n    reformat to less than 70 characters for me?'''\n"
        self.assertEqual(result, expected)
        text.delete(b'1.0', b'end')
        text.insert(b'1.0', self.test_string)
        text.tag_add(b'sel', b'1.11', b'1.end')
        self.formatter(b'ParameterDoesNothing', limit=70)
        result = text.get(b'1.0', b'insert')
        expected = b"    '''this is a test of a reformat for a triple quoted string will it reformat\n to less than 70 characters for me?'''"
        self.assertEqual(result, expected)
        text.delete(b'1.0', b'end')
        return

    def test_multiple_lines(self):
        text = self.text
        text.insert(b'1.0', self.multiline_test_string)
        text.tag_add(b'sel', b'2.0', b'4.0')
        self.formatter(b'ParameterDoesNothing', limit=70)
        result = text.get(b'2.0', b'insert')
        expected = b"    The second line's length is way over the max width. It goes on and\n    on until it is over 100 characters long. Same thing with the third\n    line. It is also way over the max width, but FormatParagraph will\n    fix it.\n"
        self.assertEqual(result, expected)
        text.delete(b'1.0', b'end')
        return

    def test_comment_block(self):
        text = self.text
        text.insert(b'1.0', self.multiline_test_comment)
        self.formatter(b'ParameterDoesNothing', limit=70)
        result = text.get(b'1.0', b'insert')
        expected = b"# The first line is under the max width. The second line's length is\n# way over the max width. It goes on and on until it is over 100\n# characters long. Same thing with the third line. It is also way over\n# the max width, but FormatParagraph will fix it. The fourth line is\n# short like the first line.\n"
        self.assertEqual(result, expected)
        text.delete(b'1.0', b'end')
        text.insert(b'1.0', self.multiline_test_comment)
        text.tag_add(b'sel', b'2.0', b'3.0')
        self.formatter(b'ParameterDoesNothing', limit=70)
        result = text.get(b'1.0', b'insert')
        expected = b"# The first line is under the max width.\n# The second line's length is way over the max width. It goes on and\n# on until it is over 100 characters long.\n"
        self.assertEqual(result, expected)
        text.delete(b'1.0', b'end')
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=2)
