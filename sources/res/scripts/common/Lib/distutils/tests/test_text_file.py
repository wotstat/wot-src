import os, unittest
from distutils.text_file import TextFile
from distutils.tests import support
from test.test_support import run_unittest
TEST_DATA = b'# test file\n\nline 3 \\\n# intervening comment\n  continues on next line\n'

class TextFileTestCase(support.TempdirManager, unittest.TestCase):

    def test_class(self):
        result1 = [
         1, 2, 3, 
         4, 
         5]
        result2 = [
         b'\n',
         b'line 3 \\\n',
         b'  continues on next line\n']
        result3 = [
         b'# test file\n',
         b'line 3 \\\n',
         b'# intervening comment\n',
         b'  continues on next line\n']
        result4 = [
         b'line 3 \\',
         b'  continues on next line']
        result5 = [
         b'line 3   continues on next line']
        result6 = [
         b'line 3 continues on next line']

        def test_input(count, description, file, expected_result):
            result = file.readlines()
            self.assertEqual(result, expected_result)
            return

        tmpdir = self.mkdtemp()
        filename = os.path.join(tmpdir, b'test.txt')
        out_file = open(filename, b'w')
        try:
            out_file.write(TEST_DATA)
        finally:
            out_file.close()

        in_file = TextFile(filename, strip_comments=0, skip_blanks=0, lstrip_ws=0, rstrip_ws=0)
        try:
            test_input(1, b'no processing', in_file, result1)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=1, skip_blanks=0, lstrip_ws=0, rstrip_ws=0)
        try:
            test_input(2, b'strip comments', in_file, result2)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=0, skip_blanks=1, lstrip_ws=0, rstrip_ws=0)
        try:
            test_input(3, b'strip blanks', in_file, result3)
        finally:
            in_file.close()

        in_file = TextFile(filename)
        try:
            test_input(4, b'default processing', in_file, result4)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=1, skip_blanks=1, join_lines=1, rstrip_ws=1)
        try:
            test_input(5, b'join lines without collapsing', in_file, result5)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=1, skip_blanks=1, join_lines=1, rstrip_ws=1, collapse_join=1)
        try:
            test_input(6, b'join lines with collapsing', in_file, result6)
        finally:
            in_file.close()

        return


def test_suite():
    return unittest.makeSuite(TextFileTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
