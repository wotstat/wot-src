import unittest, os, sys
from test.test_support import run_unittest
from distutils.command.config import dump_file, config
from distutils.tests import support
from distutils import log

class ConfigTestCase(support.LoggingSilencer, support.TempdirManager, unittest.TestCase):

    def _info(self, msg, *args):
        for line in msg.splitlines():
            self._logs.append(line)

        return

    def setUp(self):
        super(ConfigTestCase, self).setUp()
        self._logs = []
        self.old_log = log.info
        log.info = self._info
        return

    def tearDown(self):
        log.info = self.old_log
        super(ConfigTestCase, self).tearDown()
        return

    def test_dump_file(self):
        this_file = os.path.splitext(__file__)[0] + b'.py'
        f = open(this_file)
        try:
            numlines = len(f.readlines())
        finally:
            f.close()

        dump_file(this_file, b'I am the header')
        self.assertEqual(len(self._logs), numlines + 1)
        return

    @unittest.skipIf(sys.platform == b'win32', b"can't test on Windows")
    def test_search_cpp(self):
        pkg_dir, dist = self.create_dist()
        cmd = config(dist)
        match = cmd.search_cpp(pattern=b'xxx', body=b'/* xxx */')
        self.assertEqual(match, 0)
        match = cmd.search_cpp(pattern=b'_configtest', body=b'/* xxx */')
        self.assertEqual(match, 1)
        return

    def test_finalize_options(self):
        pkg_dir, dist = self.create_dist()
        cmd = config(dist)
        cmd.include_dirs = b'one%stwo' % os.pathsep
        cmd.libraries = b'one'
        cmd.library_dirs = b'three%sfour' % os.pathsep
        cmd.ensure_finalized()
        self.assertEqual(cmd.include_dirs, [b'one', b'two'])
        self.assertEqual(cmd.libraries, [b'one'])
        self.assertEqual(cmd.library_dirs, [b'three', b'four'])
        return

    def test_clean(self):
        tmp_dir = self.mkdtemp()
        f1 = os.path.join(tmp_dir, b'one')
        f2 = os.path.join(tmp_dir, b'two')
        self.write_file(f1, b'xxx')
        self.write_file(f2, b'xxx')
        for f in (f1, f2):
            self.assertTrue(os.path.exists(f))

        pkg_dir, dist = self.create_dist()
        cmd = config(dist)
        cmd._clean(f1, f2)
        for f in (f1, f2):
            self.assertFalse(os.path.exists(f))

        return


def test_suite():
    return unittest.makeSuite(ConfigTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
