import unittest, os, shutil
from distutils.file_util import move_file, write_file, copy_file
from distutils import log
from distutils.tests import support
from test.test_support import run_unittest
requires_os_link = unittest.skipUnless(hasattr(os, b'link'), b'test requires os.link()')

class FileUtilTestCase(support.TempdirManager, unittest.TestCase):

    def _log(self, msg, *args):
        if len(args) > 0:
            self._logs.append(msg % args)
        else:
            self._logs.append(msg)
        return

    def setUp(self):
        super(FileUtilTestCase, self).setUp()
        self._logs = []
        self.old_log = log.info
        log.info = self._log
        tmp_dir = self.mkdtemp()
        self.source = os.path.join(tmp_dir, b'f1')
        self.target = os.path.join(tmp_dir, b'f2')
        self.target_dir = os.path.join(tmp_dir, b'd1')
        return

    def tearDown(self):
        log.info = self.old_log
        super(FileUtilTestCase, self).tearDown()
        return

    def test_move_file_verbosity(self):
        f = open(self.source, b'w')
        try:
            f.write(b'some content')
        finally:
            f.close()

        move_file(self.source, self.target, verbose=0)
        wanted = []
        self.assertEqual(self._logs, wanted)
        move_file(self.target, self.source, verbose=0)
        move_file(self.source, self.target, verbose=1)
        wanted = [b'moving %s -> %s' % (self.source, self.target)]
        self.assertEqual(self._logs, wanted)
        move_file(self.target, self.source, verbose=0)
        self._logs = []
        os.mkdir(self.target_dir)
        move_file(self.source, self.target_dir, verbose=1)
        wanted = [b'moving %s -> %s' % (self.source, self.target_dir)]
        self.assertEqual(self._logs, wanted)
        return

    def test_write_file(self):
        lines = [b'a', b'b', b'c']
        dir = self.mkdtemp()
        foo = os.path.join(dir, b'foo')
        write_file(foo, lines)
        content = [line.strip() for line in open(foo).readlines()]
        self.assertEqual(content, lines)
        return

    def test_copy_file(self):
        src_dir = self.mkdtemp()
        foo = os.path.join(src_dir, b'foo')
        write_file(foo, b'content')
        dst_dir = self.mkdtemp()
        copy_file(foo, dst_dir)
        self.assertTrue(os.path.exists(os.path.join(dst_dir, b'foo')))
        return

    @requires_os_link
    def test_copy_file_hard_link(self):
        with open(self.source, b'w') as f:
            f.write(b'some content')
        st = os.stat(self.source)
        copy_file(self.source, self.target, link=b'hard')
        st2 = os.stat(self.source)
        st3 = os.stat(self.target)
        self.assertTrue(os.path.samestat(st, st2), (st, st2))
        self.assertTrue(os.path.samestat(st2, st3), (st2, st3))
        with open(self.source, b'r') as f:
            self.assertEqual(f.read(), b'some content')
        return

    @requires_os_link
    def test_copy_file_hard_link_failure(self):
        with open(self.source, b'w') as f:
            f.write(b'some content')
        st = os.stat(self.source)

        def _os_link(*args):
            raise OSError(0, b'linking unsupported')
            return

        old_link = os.link
        os.link = _os_link
        try:
            copy_file(self.source, self.target, link=b'hard')
        finally:
            os.link = old_link

        st2 = os.stat(self.source)
        st3 = os.stat(self.target)
        self.assertTrue(os.path.samestat(st, st2), (st, st2))
        self.assertFalse(os.path.samestat(st2, st3), (st2, st3))
        for fn in (self.source, self.target):
            with open(fn, b'r') as f:
                self.assertEqual(f.read(), b'some content')

        return


def test_suite():
    return unittest.makeSuite(FileUtilTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
