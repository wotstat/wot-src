import sys, os, unittest, tempfile, shutil
from distutils.core import PyPIRCCommand
from distutils.core import Distribution
from distutils.log import set_threshold
from distutils.log import WARN
from distutils.tests import support
from test.test_support import run_unittest
PYPIRC = b'[distutils]\n\nindex-servers =\n    server1\n    server2\n\n[server1]\nusername:me\npassword:secret\n\n[server2]\nusername:meagain\npassword: secret\nrealm:acme\nrepository:http://another.pypi/\n'
PYPIRC_OLD = b'[server-login]\nusername:tarek\npassword:secret\n'
WANTED = b'[distutils]\nindex-servers =\n    pypi\n\n[pypi]\nusername:tarek\npassword:xxx\n'

class PyPIRCCommandTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def setUp(self):
        super(PyPIRCCommandTestCase, self).setUp()
        self.tmp_dir = self.mkdtemp()
        os.environ[b'HOME'] = self.tmp_dir
        self.rc = os.path.join(self.tmp_dir, b'.pypirc')
        self.dist = Distribution()

        class command(PyPIRCCommand):

            def __init__(self, dist):
                PyPIRCCommand.__init__(self, dist)
                return

            def initialize_options(self):
                return

            finalize_options = initialize_options

        self._cmd = command
        self.old_threshold = set_threshold(WARN)
        return

    def tearDown(self):
        set_threshold(self.old_threshold)
        super(PyPIRCCommandTestCase, self).tearDown()
        return

    def test_server_registration(self):
        self.write_file(self.rc, PYPIRC)
        cmd = self._cmd(self.dist)
        config = cmd._read_pypirc()
        config = config.items()
        config.sort()
        waited = [13, 14, 
         15, 
         16, 17]
        self.assertEqual(config, waited)
        self.write_file(self.rc, PYPIRC_OLD)
        config = cmd._read_pypirc()
        config = config.items()
        config.sort()
        waited = [18, 19, 
         20, 
         21, 22]
        self.assertEqual(config, waited)
        return

    def test_server_empty_registration(self):
        cmd = self._cmd(self.dist)
        rc = cmd._get_rc_file()
        self.assertFalse(os.path.exists(rc))
        cmd._store_pypirc(b'tarek', b'xxx')
        self.assertTrue(os.path.exists(rc))
        f = open(rc)
        try:
            content = f.read()
            self.assertEqual(content, WANTED)
        finally:
            f.close()

        return


def test_suite():
    return unittest.makeSuite(PyPIRCCommandTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
