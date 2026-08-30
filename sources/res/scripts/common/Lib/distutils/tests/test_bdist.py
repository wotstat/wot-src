import os, unittest
from test.test_support import run_unittest
from distutils.command.bdist import bdist
from distutils.tests import support

class BuildTestCase(support.TempdirManager, unittest.TestCase):

    def test_formats(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.formats = [b'msi']
        cmd.ensure_finalized()
        self.assertEqual(cmd.formats, [b'msi'])
        formats = [
         3, 4, 2, 5, 6, 
         7, 8, 9]
        found = sorted(cmd.format_command)
        self.assertEqual(found, formats)
        return

    def test_skip_build(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.skip_build = 1
        cmd.ensure_finalized()
        dist.command_obj[b'bdist'] = cmd
        names = [
         b'bdist_dumb', b'bdist_wininst']
        if os.name == b'nt':
            names.append(b'bdist_msi')
        for name in names:
            subcmd = cmd.get_finalized_command(name)
            self.assertTrue(subcmd.skip_build, b'%s should take --skip-build from bdist' % name)

        return


def test_suite():
    return unittest.makeSuite(BuildTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
