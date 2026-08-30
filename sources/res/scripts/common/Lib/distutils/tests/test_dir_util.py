import unittest, os, stat, shutil, sys
from distutils.dir_util import mkpath, remove_tree, create_tree, copy_tree, ensure_relative
from distutils import log
from distutils.tests import support
from test.test_support import run_unittest

class DirUtilTestCase(support.TempdirManager, unittest.TestCase):

    def _log(self, msg, *args):
        if len(args) > 0:
            self._logs.append(msg % args)
        else:
            self._logs.append(msg)
        return

    def setUp(self):
        super(DirUtilTestCase, self).setUp()
        self._logs = []
        tmp_dir = self.mkdtemp()
        self.root_target = os.path.join(tmp_dir, b'deep')
        self.target = os.path.join(self.root_target, b'here')
        self.target2 = os.path.join(tmp_dir, b'deep2')
        self.old_log = log.info
        log.info = self._log
        return

    def tearDown(self):
        log.info = self.old_log
        super(DirUtilTestCase, self).tearDown()
        return

    def test_mkpath_remove_tree_verbosity(self):
        mkpath(self.target, verbose=0)
        wanted = []
        self.assertEqual(self._logs, wanted)
        remove_tree(self.root_target, verbose=0)
        mkpath(self.target, verbose=1)
        wanted = [b'creating %s' % self.root_target,
         b'creating %s' % self.target]
        self.assertEqual(self._logs, wanted)
        self._logs = []
        remove_tree(self.root_target, verbose=1)
        wanted = [b"removing '%s' (and everything under it)" % self.root_target]
        self.assertEqual(self._logs, wanted)
        return

    @unittest.skipIf(sys.platform.startswith(b'win'), b'This test is only appropriate for POSIX-like systems.')
    def test_mkpath_with_custom_mode(self):
        umask = os.umask(2)
        os.umask(umask)
        mkpath(self.target, 448)
        self.assertEqual(stat.S_IMODE(os.stat(self.target).st_mode), 448 & ~umask)
        mkpath(self.target2, 365)
        self.assertEqual(stat.S_IMODE(os.stat(self.target2).st_mode), 365 & ~umask)
        return

    def test_create_tree_verbosity(self):
        create_tree(self.root_target, [b'one', b'two', b'three'], verbose=0)
        self.assertEqual(self._logs, [])
        remove_tree(self.root_target, verbose=0)
        wanted = [
         b'creating %s' % self.root_target]
        create_tree(self.root_target, [b'one', b'two', b'three'], verbose=1)
        self.assertEqual(self._logs, wanted)
        remove_tree(self.root_target, verbose=0)
        return

    def test_copy_tree_verbosity(self):
        mkpath(self.target, verbose=0)
        copy_tree(self.target, self.target2, verbose=0)
        self.assertEqual(self._logs, [])
        remove_tree(self.root_target, verbose=0)
        mkpath(self.target, verbose=0)
        a_file = os.path.join(self.target, b'ok.txt')
        f = open(a_file, b'w')
        try:
            f.write(b'some content')
        finally:
            f.close()

        wanted = [b'copying %s -> %s' % (a_file, self.target2)]
        copy_tree(self.target, self.target2, verbose=1)
        self.assertEqual(self._logs, wanted)
        remove_tree(self.root_target, verbose=0)
        remove_tree(self.target2, verbose=0)
        return

    def test_copy_tree_skips_nfs_temp_files(self):
        mkpath(self.target, verbose=0)
        a_file = os.path.join(self.target, b'ok.txt')
        nfs_file = os.path.join(self.target, b'.nfs123abc')
        for f in (a_file, nfs_file):
            fh = open(f, b'w')
            try:
                fh.write(b'some content')
            finally:
                fh.close()

        copy_tree(self.target, self.target2)
        self.assertEqual(os.listdir(self.target2), [b'ok.txt'])
        remove_tree(self.root_target, verbose=0)
        remove_tree(self.target2, verbose=0)
        return

    def test_ensure_relative(self):
        if os.sep == b'/':
            self.assertEqual(ensure_relative(b'/home/foo'), b'home/foo')
            self.assertEqual(ensure_relative(b'some/path'), b'some/path')
        else:
            self.assertEqual(ensure_relative(b'c:\\home\\foo'), b'c:home\\foo')
            self.assertEqual(ensure_relative(b'home\\foo'), b'home\\foo')
        return


def test_suite():
    return unittest.makeSuite(DirUtilTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
