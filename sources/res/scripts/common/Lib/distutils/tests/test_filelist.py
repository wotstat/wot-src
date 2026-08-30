import os, re, unittest
from distutils import debug
from distutils.log import WARN
from distutils.errors import DistutilsTemplateError
from distutils.filelist import glob_to_re, translate_pattern, FileList
from test.test_support import captured_stdout, run_unittest
from distutils.tests import support
MANIFEST_IN = b'include ok\ninclude xo\nexclude xo\ninclude foo.tmp\ninclude buildout.cfg\nglobal-include *.x\nglobal-include *.txt\nglobal-exclude *.tmp\nrecursive-include f *.oo\nrecursive-exclude global *.x\ngraft dir\nprune dir3\n'

def make_local_path(s):
    return s.replace(b'/', os.sep)


class FileListTestCase(support.LoggingSilencer, unittest.TestCase):

    def assertNoWarnings(self):
        self.assertEqual(self.get_logs(WARN), [])
        self.clear_logs()
        return

    def assertWarnings(self):
        self.assertGreater(len(self.get_logs(WARN)), 0)
        self.clear_logs()
        return

    def test_glob_to_re(self):
        sep = os.sep
        if os.sep == b'\\':
            sep = re.escape(os.sep)
        for glob, regex in (
         (b'foo*', b'foo[^%(sep)s]*\\Z(?ms)'),
         (b'foo?', b'foo[^%(sep)s]\\Z(?ms)'),
         (b'foo??', b'foo[^%(sep)s][^%(sep)s]\\Z(?ms)'),
         (b'foo\\\\*', b'foo\\\\\\\\[^%(sep)s]*\\Z(?ms)'),
         (b'foo\\\\\\*', b'foo\\\\\\\\\\\\[^%(sep)s]*\\Z(?ms)'),
         (b'foo????', b'foo[^%(sep)s][^%(sep)s][^%(sep)s][^%(sep)s]\\Z(?ms)'),
         (b'foo\\\\??', b'foo\\\\\\\\[^%(sep)s][^%(sep)s]\\Z(?ms)')):
            regex = regex % {b'sep': sep}
            self.assertEqual(glob_to_re(glob), regex)

        return

    def test_process_template_line(self):
        file_list = FileList()
        l = make_local_path
        file_list.allfiles = [
         b'foo.tmp', b'ok', b'xo', b'four.txt',
         b'buildout.cfg',
         l(b'.hg/last-message.txt'),
         l(b'global/one.txt'),
         l(b'global/two.txt'),
         l(b'global/files.x'),
         l(b'global/here.tmp'),
         l(b'f/o/f.oo'),
         l(b'dir/graft-one'),
         l(b'dir/dir2/graft2'),
         l(b'dir3/ok'),
         l(b'dir3/sub/ok.txt')]
        for line in MANIFEST_IN.split(b'\n'):
            if line.strip() == b'':
                continue
            file_list.process_template_line(line)

        wanted = [b'ok',
         b'buildout.cfg',
         b'four.txt',
         l(b'.hg/last-message.txt'),
         l(b'global/one.txt'),
         l(b'global/two.txt'),
         l(b'f/o/f.oo'),
         l(b'dir/graft-one'),
         l(b'dir/dir2/graft2')]
        self.assertEqual(file_list.files, wanted)
        return

    def test_debug_print(self):
        file_list = FileList()
        with captured_stdout() as stdout:
            file_list.debug_print(b'xxx')
        self.assertEqual(stdout.getvalue(), b'')
        debug.DEBUG = True
        try:
            with captured_stdout() as stdout:
                file_list.debug_print(b'xxx')
            self.assertEqual(stdout.getvalue(), b'xxx\n')
        finally:
            debug.DEBUG = False

        return

    def test_set_allfiles(self):
        file_list = FileList()
        files = [b'a', b'b', b'c']
        file_list.set_allfiles(files)
        self.assertEqual(file_list.allfiles, files)
        return

    def test_remove_duplicates(self):
        file_list = FileList()
        file_list.files = [1, 2, 1, 3, 4, 3]
        file_list.sort()
        file_list.remove_duplicates()
        self.assertEqual(file_list.files, [b'a', b'b', b'c', b'g'])
        return

    def test_translate_pattern(self):
        self.assertTrue(hasattr(translate_pattern(b'a', anchor=True, is_regex=False), b'search'))
        regex = re.compile(b'a')
        self.assertEqual(translate_pattern(regex, anchor=True, is_regex=True), regex)
        self.assertTrue(hasattr(translate_pattern(b'a', anchor=True, is_regex=True), b'search'))
        self.assertTrue(translate_pattern(b'*.py', anchor=True, is_regex=False).search(b'filelist.py'))
        return

    def test_exclude_pattern(self):
        file_list = FileList()
        self.assertFalse(file_list.exclude_pattern(b'*.py'))
        file_list = FileList()
        file_list.files = [b'a.py', b'b.py']
        self.assertTrue(file_list.exclude_pattern(b'*.py'))
        file_list = FileList()
        file_list.files = [b'a.py', b'a.txt']
        file_list.exclude_pattern(b'*.py')
        self.assertEqual(file_list.files, [b'a.txt'])
        return

    def test_include_pattern(self):
        file_list = FileList()
        file_list.set_allfiles([])
        self.assertFalse(file_list.include_pattern(b'*.py'))
        file_list = FileList()
        file_list.set_allfiles([b'a.py', b'b.txt'])
        self.assertTrue(file_list.include_pattern(b'*.py'))
        file_list = FileList()
        self.assertIsNone(file_list.allfiles)
        file_list.set_allfiles([b'a.py', b'b.txt'])
        file_list.include_pattern(b'*')
        self.assertEqual(file_list.allfiles, [b'a.py', b'b.txt'])
        return

    def test_process_template(self):
        l = make_local_path
        file_list = FileList()
        for action in (b'include', b'exclude', b'global-include', b'global-exclude', b'recursive-include', b'recursive-exclude', b'graft', b'prune', b'blarg'):
            self.assertRaises(DistutilsTemplateError, file_list.process_template_line, action)

        file_list = FileList()
        file_list.set_allfiles([b'a.py', b'b.txt', l(b'd/c.py')])
        file_list.process_template_line(b'include *.py')
        self.assertEqual(file_list.files, [b'a.py'])
        self.assertNoWarnings()
        file_list.process_template_line(b'include *.rb')
        self.assertEqual(file_list.files, [b'a.py'])
        self.assertWarnings()
        file_list = FileList()
        file_list.files = [b'a.py', b'b.txt', l(b'd/c.py')]
        file_list.process_template_line(b'exclude *.py')
        self.assertEqual(file_list.files, [b'b.txt', l(b'd/c.py')])
        self.assertNoWarnings()
        file_list.process_template_line(b'exclude *.rb')
        self.assertEqual(file_list.files, [b'b.txt', l(b'd/c.py')])
        self.assertWarnings()
        file_list = FileList()
        file_list.set_allfiles([b'a.py', b'b.txt', l(b'd/c.py')])
        file_list.process_template_line(b'global-include *.py')
        self.assertEqual(file_list.files, [b'a.py', l(b'd/c.py')])
        self.assertNoWarnings()
        file_list.process_template_line(b'global-include *.rb')
        self.assertEqual(file_list.files, [b'a.py', l(b'd/c.py')])
        self.assertWarnings()
        file_list = FileList()
        file_list.files = [b'a.py', b'b.txt', l(b'd/c.py')]
        file_list.process_template_line(b'global-exclude *.py')
        self.assertEqual(file_list.files, [b'b.txt'])
        self.assertNoWarnings()
        file_list.process_template_line(b'global-exclude *.rb')
        self.assertEqual(file_list.files, [b'b.txt'])
        self.assertWarnings()
        file_list = FileList()
        file_list.set_allfiles([b'a.py', l(b'd/b.py'), l(b'd/c.txt'),
         l(b'd/d/e.py')])
        file_list.process_template_line(b'recursive-include d *.py')
        self.assertEqual(file_list.files, [l(b'd/b.py'), l(b'd/d/e.py')])
        self.assertNoWarnings()
        file_list.process_template_line(b'recursive-include e *.py')
        self.assertEqual(file_list.files, [l(b'd/b.py'), l(b'd/d/e.py')])
        self.assertWarnings()
        file_list = FileList()
        file_list.files = [b'a.py', l(b'd/b.py'), l(b'd/c.txt'), l(b'd/d/e.py')]
        file_list.process_template_line(b'recursive-exclude d *.py')
        self.assertEqual(file_list.files, [b'a.py', l(b'd/c.txt')])
        self.assertNoWarnings()
        file_list.process_template_line(b'recursive-exclude e *.py')
        self.assertEqual(file_list.files, [b'a.py', l(b'd/c.txt')])
        self.assertWarnings()
        file_list = FileList()
        file_list.set_allfiles([b'a.py', l(b'd/b.py'), l(b'd/d/e.py'),
         l(b'f/f.py')])
        file_list.process_template_line(b'graft d')
        self.assertEqual(file_list.files, [l(b'd/b.py'), l(b'd/d/e.py')])
        self.assertNoWarnings()
        file_list.process_template_line(b'graft e')
        self.assertEqual(file_list.files, [l(b'd/b.py'), l(b'd/d/e.py')])
        self.assertWarnings()
        file_list = FileList()
        file_list.files = [b'a.py', l(b'd/b.py'), l(b'd/d/e.py'), l(b'f/f.py')]
        file_list.process_template_line(b'prune d')
        self.assertEqual(file_list.files, [b'a.py', l(b'f/f.py')])
        self.assertNoWarnings()
        file_list.process_template_line(b'prune e')
        self.assertEqual(file_list.files, [b'a.py', l(b'f/f.py')])
        self.assertWarnings()
        return


def test_suite():
    return unittest.makeSuite(FileListTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
