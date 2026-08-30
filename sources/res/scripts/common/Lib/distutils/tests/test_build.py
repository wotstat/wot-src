import unittest, os, sys
from test.test_support import run_unittest
from distutils.command.build import build
from distutils.tests import support
from sysconfig import get_platform

class BuildTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_finalize_options(self):
        pkg_dir, dist = self.create_dist()
        cmd = build(dist)
        cmd.finalize_options()
        self.assertEqual(cmd.plat_name, get_platform())
        wanted = os.path.join(cmd.build_base, b'lib')
        self.assertEqual(cmd.build_purelib, wanted)
        plat_spec = b'.%s-%s' % (cmd.plat_name, sys.version[0:3])
        if hasattr(sys, b'gettotalrefcount'):
            self.assertTrue(cmd.build_platlib.endswith(b'-pydebug'))
            plat_spec += b'-pydebug'
        wanted = os.path.join(cmd.build_base, b'lib' + plat_spec)
        self.assertEqual(cmd.build_platlib, wanted)
        self.assertEqual(cmd.build_lib, cmd.build_purelib)
        wanted = os.path.join(cmd.build_base, b'temp' + plat_spec)
        self.assertEqual(cmd.build_temp, wanted)
        wanted = os.path.join(cmd.build_base, b'scripts-' + sys.version[0:3])
        self.assertEqual(cmd.build_scripts, wanted)
        self.assertEqual(cmd.executable, os.path.normpath(sys.executable))
        return


def test_suite():
    return unittest.makeSuite(BuildTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
