import unittest
from test.test_support import captured_stdout, findfile
from idlelib.idle_test.mock_tk import Var
from idlelib.GrepDialog import GrepDialog
import re
__file__ = findfile(b'idlelib/idle_test') + b'/test_grep.py'

class Dummy_searchengine:

    def getpat(self):
        return self._pat


searchengine = Dummy_searchengine()

class Dummy_grep:
    grep_it = GrepDialog.grep_it.im_func
    findfiles = GrepDialog.findfiles.im_func
    recvar = Var(False)
    engine = searchengine

    def close(self):
        return


grep = Dummy_grep()

class FindfilesTest(unittest.TestCase):
    pass


class Grep_itTest(unittest.TestCase):

    def report(self, pat):
        grep.engine._pat = pat
        with captured_stdout() as s:
            grep.grep_it(re.compile(pat), __file__)
        lines = s.getvalue().split(b'\n')
        lines.pop()
        return lines

    def test_unfound(self):
        pat = b'xyz*' * 7
        lines = self.report(pat)
        self.assertEqual(len(lines), 2)
        self.assertIn(pat, lines[0])
        self.assertEqual(lines[1], b'No hits.')
        return

    def test_found(self):
        pat = b'""" !Changing this line will break Test_findfile.test_found!'
        lines = self.report(pat)
        self.assertEqual(len(lines), 5)
        self.assertIn(pat, lines[0])
        self.assertIn(b'py: 1:', lines[1])
        self.assertIn(b'2', lines[3])
        self.assertTrue(lines[4].startswith(b'(Hint:'))
        return


class Default_commandTest(unittest.TestCase):
    pass


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
