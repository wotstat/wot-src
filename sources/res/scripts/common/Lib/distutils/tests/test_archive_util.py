__revision__ = b'$Id$'
import unittest, os, sys, tarfile
from os.path import splitdrive
import warnings
from distutils.archive_util import check_archive_formats, make_tarball, make_zipfile, make_archive, ARCHIVE_FORMATS
from distutils.spawn import find_executable, spawn
from distutils.tests import support
from test.test_support import check_warnings, run_unittest
try:
    import grp, pwd
    UID_GID_SUPPORT = True
except ImportError:
    UID_GID_SUPPORT = False

try:
    import zipfile
    ZIP_SUPPORT = True
except ImportError:
    ZIP_SUPPORT = find_executable(b'zip')

try:
    import zlib
except ImportError:
    zlib = None

def can_fs_encode(filename):
    if os.path.supports_unicode_filenames:
        return True
    try:
        filename.encode(sys.getfilesystemencoding())
    except UnicodeEncodeError:
        return False

    return True


class ArchiveUtilTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    @unittest.skipUnless(zlib, b'requires zlib')
    def test_make_tarball(self):
        self._make_tarball(b'archive')
        return

    def _make_tarball(self, target_name):
        tmpdir = self.mkdtemp()
        self.write_file([tmpdir, b'file1'], b'xxx')
        self.write_file([tmpdir, b'file2'], b'xxx')
        os.mkdir(os.path.join(tmpdir, b'sub'))
        self.write_file([tmpdir, b'sub', b'file3'], b'xxx')
        tmpdir2 = self.mkdtemp()
        unittest.skipUnless(splitdrive(tmpdir)[0] == splitdrive(tmpdir2)[0], b'source and target should be on same drive')
        base_name = os.path.join(tmpdir2, target_name)
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            make_tarball(splitdrive(base_name)[1], b'.')
        finally:
            os.chdir(old_dir)

        tarball = base_name + b'.tar.gz'
        self.assertTrue(os.path.exists(tarball))
        base_name = os.path.join(tmpdir2, target_name)
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            make_tarball(splitdrive(base_name)[1], b'.', compress=None)
        finally:
            os.chdir(old_dir)

        tarball = base_name + b'.tar'
        self.assertTrue(os.path.exists(tarball))
        return

    def _tarinfo(self, path):
        tar = tarfile.open(path)
        try:
            names = tar.getnames()
            names.sort()
            return names
        finally:
            tar.close()

        return

    def _create_files(self):
        tmpdir = self.mkdtemp()
        dist = os.path.join(tmpdir, b'dist')
        os.mkdir(dist)
        self.write_file([dist, b'file1'], b'xxx')
        self.write_file([dist, b'file2'], b'xxx')
        os.mkdir(os.path.join(dist, b'sub'))
        self.write_file([dist, b'sub', b'file3'], b'xxx')
        os.mkdir(os.path.join(dist, b'sub2'))
        tmpdir2 = self.mkdtemp()
        base_name = os.path.join(tmpdir2, b'archive')
        return (tmpdir, tmpdir2, base_name)

    @unittest.skipUnless(zlib, b'Requires zlib')
    @unittest.skipUnless(find_executable(b'tar') and find_executable(b'gzip'), b'Need the tar command to run')
    def test_tarfile_vs_tar(self):
        tmpdir, tmpdir2, base_name = self._create_files()
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            make_tarball(base_name, b'dist')
        finally:
            os.chdir(old_dir)

        tarball = base_name + b'.tar.gz'
        self.assertTrue(os.path.exists(tarball))
        tarball2 = os.path.join(tmpdir, b'archive2.tar.gz')
        tar_cmd = [b'tar', b'-cf', b'archive2.tar', b'dist']
        gzip_cmd = [b'gzip', b'-f9', b'archive2.tar']
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            spawn(tar_cmd)
            spawn(gzip_cmd)
        finally:
            os.chdir(old_dir)

        self.assertTrue(os.path.exists(tarball2))
        self.assertEqual(self._tarinfo(tarball), self._tarinfo(tarball2))
        base_name = os.path.join(tmpdir2, b'archive')
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            make_tarball(base_name, b'dist', compress=None)
        finally:
            os.chdir(old_dir)

        tarball = base_name + b'.tar'
        self.assertTrue(os.path.exists(tarball))
        base_name = os.path.join(tmpdir2, b'archive')
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            make_tarball(base_name, b'dist', compress=None, dry_run=True)
        finally:
            os.chdir(old_dir)

        tarball = base_name + b'.tar'
        self.assertTrue(os.path.exists(tarball))
        return

    @unittest.skipUnless(find_executable(b'compress'), b'The compress program is required')
    def test_compress_deprecated(self):
        tmpdir, tmpdir2, base_name = self._create_files()
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            with check_warnings() as w:
                warnings.simplefilter(b'always')
                make_tarball(base_name, b'dist', compress=b'compress')
        finally:
            os.chdir(old_dir)

        tarball = base_name + b'.tar.Z'
        self.assertTrue(os.path.exists(tarball))
        self.assertEqual(len(w.warnings), 1)
        os.remove(tarball)
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            with check_warnings() as w:
                warnings.simplefilter(b'always')
                make_tarball(base_name, b'dist', compress=b'compress', dry_run=True)
        finally:
            os.chdir(old_dir)

        self.assertFalse(os.path.exists(tarball))
        self.assertEqual(len(w.warnings), 1)
        return

    @unittest.skipUnless(zlib, b'Requires zlib')
    @unittest.skipUnless(ZIP_SUPPORT, b'Need zip support to run')
    def test_make_zipfile(self):
        tmpdir = self.mkdtemp()
        self.write_file([tmpdir, b'file1'], b'xxx')
        self.write_file([tmpdir, b'file2'], b'xxx')
        tmpdir2 = self.mkdtemp()
        base_name = os.path.join(tmpdir2, b'archive')
        make_zipfile(base_name, tmpdir)
        tarball = base_name + b'.zip'
        return

    def test_check_archive_formats(self):
        self.assertEqual(check_archive_formats([b'gztar', b'xxx', b'zip']), b'xxx')
        self.assertEqual(check_archive_formats([b'gztar', b'zip']), None)
        return

    def test_make_archive(self):
        tmpdir = self.mkdtemp()
        base_name = os.path.join(tmpdir, b'archive')
        self.assertRaises(ValueError, make_archive, base_name, b'xxx')
        return

    @unittest.skipUnless(zlib, b'Requires zlib')
    def test_make_archive_owner_group(self):
        if UID_GID_SUPPORT:
            group = grp.getgrgid(0)[0]
            owner = pwd.getpwuid(0)[0]
        else:
            group = owner = b'root'
        base_dir, root_dir, base_name = self._create_files()
        base_name = os.path.join(self.mkdtemp(), b'archive')
        res = make_archive(base_name, b'zip', root_dir, base_dir, owner=owner, group=group)
        self.assertTrue(os.path.exists(res))
        res = make_archive(base_name, b'zip', root_dir, base_dir)
        self.assertTrue(os.path.exists(res))
        res = make_archive(base_name, b'tar', root_dir, base_dir, owner=owner, group=group)
        self.assertTrue(os.path.exists(res))
        res = make_archive(base_name, b'tar', root_dir, base_dir, owner=b'kjhkjhkjg', group=b'oihohoh')
        self.assertTrue(os.path.exists(res))
        return

    @unittest.skipUnless(zlib, b'Requires zlib')
    @unittest.skipUnless(UID_GID_SUPPORT, b'Requires grp and pwd support')
    def test_tarfile_root_owner(self):
        tmpdir, tmpdir2, base_name = self._create_files()
        old_dir = os.getcwd()
        os.chdir(tmpdir)
        group = grp.getgrgid(0)[0]
        owner = pwd.getpwuid(0)[0]
        try:
            archive_name = make_tarball(base_name, b'dist', compress=None, owner=owner, group=group)
        finally:
            os.chdir(old_dir)

        self.assertTrue(os.path.exists(archive_name))
        archive = tarfile.open(archive_name)
        try:
            for member in archive.getmembers():
                self.assertEqual(member.uid, 0)
                self.assertEqual(member.gid, 0)

        finally:
            archive.close()

        return

    def test_make_archive_cwd(self):
        current_dir = os.getcwd()

        def _breaks(*args, **kw):
            raise RuntimeError()
            return

        ARCHIVE_FORMATS[b'xxx'] = (
         _breaks, [], b'xxx file')
        try:
            try:
                make_archive(b'xxx', b'xxx', root_dir=self.mkdtemp())
            except:
                pass

            self.assertEqual(os.getcwd(), current_dir)
        finally:
            del ARCHIVE_FORMATS[b'xxx']

        return

    @unittest.skipUnless(zlib, b'requires zlib')
    def test_make_tarball_unicode(self):
        self._make_tarball(u'archive')
        return

    @unittest.skipUnless(zlib, b'requires zlib')
    @unittest.skipUnless(can_fs_encode(u'\xe5rchiv'), b'File system cannot handle this filename')
    def test_make_tarball_unicode_latin1(self):
        self._make_tarball(u'\xe5rchiv')
        return

    @unittest.skipUnless(zlib, b'requires zlib')
    @unittest.skipUnless(can_fs_encode(u'\u306e\u30a2\u30fc\u30ab\u30a4\u30d6'), b'File system cannot handle this filename')
    def test_make_tarball_unicode_extended(self):
        self._make_tarball(u'\u306e\u30a2\u30fc\u30ab\u30a4\u30d6')
        return


def test_suite():
    return unittest.makeSuite(ArchiveUtilTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
