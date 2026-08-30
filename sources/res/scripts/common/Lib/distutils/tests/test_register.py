import os, unittest, getpass, urllib2, warnings
from test.test_support import check_warnings, run_unittest
from distutils.command import register as register_module
from distutils.command.register import register
from distutils.errors import DistutilsSetupError
from distutils.tests.test_config import PyPIRCCommandTestCase
try:
    import docutils
except ImportError:
    docutils = None

PYPIRC_NOPASSWORD = b'[distutils]\n\nindex-servers =\n    server1\n\n[server1]\nusername:me\n'
WANTED_PYPIRC = b'[distutils]\nindex-servers =\n    pypi\n\n[pypi]\nusername:tarek\npassword:password\n'

class RawInputs(object):

    def __init__(self, *answers):
        self.answers = answers
        self.index = 0
        return

    def __call__(self, prompt=b''):
        try:
            return self.answers[self.index]
        finally:
            self.index += 1

        return


class FakeOpener(object):

    def __init__(self):
        self.reqs = []
        return

    def __call__(self, *args):
        return self

    def open(self, req):
        self.reqs.append(req)
        return self

    def read(self):
        return b'xxx'


class RegisterTestCase(PyPIRCCommandTestCase):

    def setUp(self):
        super(RegisterTestCase, self).setUp()
        self._old_getpass = getpass.getpass

        def _getpass(prompt):
            return b'password'

        getpass.getpass = _getpass
        self.old_opener = urllib2.build_opener
        self.conn = urllib2.build_opener = FakeOpener()
        return

    def tearDown(self):
        getpass.getpass = self._old_getpass
        urllib2.build_opener = self.old_opener
        super(RegisterTestCase, self).tearDown()
        return

    def _get_cmd(self, metadata=None):
        if metadata is None:
            metadata = {b'url': b'xxx', b'author': b'xxx', b'author_email': b'xxx', b'name': b'xxx', 
               b'version': b'xxx'}
        pkg_info, dist = self.create_dist(**metadata)
        return register(dist)

    def test_create_pypirc(self):
        cmd = self._get_cmd()
        self.assertFalse(os.path.exists(self.rc))
        inputs = RawInputs(b'1', b'tarek', b'y')
        register_module.raw_input = inputs.__call__
        try:
            cmd.run()
        finally:
            del register_module.raw_input

        self.assertTrue(os.path.exists(self.rc))
        f = open(self.rc)
        try:
            content = f.read()
            self.assertEqual(content, WANTED_PYPIRC)
        finally:
            f.close()

        def _no_way(prompt=b''):
            raise AssertionError(prompt)
            return

        register_module.raw_input = _no_way
        cmd.show_response = 1
        cmd.run()
        self.assertEqual(len(self.conn.reqs), 2)
        req1 = dict(self.conn.reqs[0].headers)
        req2 = dict(self.conn.reqs[1].headers)
        self.assertEqual(req2[b'Content-length'], req1[b'Content-length'])
        self.assertIn(b'xxx', self.conn.reqs[1].data)
        return

    def test_password_not_in_file(self):
        self.write_file(self.rc, PYPIRC_NOPASSWORD)
        cmd = self._get_cmd()
        cmd._set_config()
        cmd.finalize_options()
        cmd.send_metadata()
        self.assertEqual(cmd.distribution.password, b'password')
        return

    def test_registering(self):
        cmd = self._get_cmd()
        inputs = RawInputs(b'2', b'tarek', b'tarek@ziade.org')
        register_module.raw_input = inputs.__call__
        try:
            cmd.run()
        finally:
            del register_module.raw_input

        self.assertEqual(len(self.conn.reqs), 1)
        req = self.conn.reqs[0]
        headers = dict(req.headers)
        self.assertEqual(headers[b'Content-length'], b'608')
        self.assertIn(b'tarek', req.data)
        return

    def test_password_reset(self):
        cmd = self._get_cmd()
        inputs = RawInputs(b'3', b'tarek@ziade.org')
        register_module.raw_input = inputs.__call__
        try:
            cmd.run()
        finally:
            del register_module.raw_input

        self.assertEqual(len(self.conn.reqs), 1)
        req = self.conn.reqs[0]
        headers = dict(req.headers)
        self.assertEqual(headers[b'Content-length'], b'290')
        self.assertIn(b'tarek', req.data)
        return

    @unittest.skipUnless(docutils is not None, b'needs docutils')
    def test_strict(self):
        cmd = self._get_cmd({})
        cmd.ensure_finalized()
        cmd.strict = 1
        self.assertRaises(DistutilsSetupError, cmd.run)
        metadata = {b'url': b'xxx', b'author': b'xxx', b'author_email': u'\xe9x\xe9x\xe9', 
           b'name': b'xxx', 
           b'version': b'xxx', b'long_description': b'title\n==\n\ntext'}
        cmd = self._get_cmd(metadata)
        cmd.ensure_finalized()
        cmd.strict = 1
        self.assertRaises(DistutilsSetupError, cmd.run)
        metadata[b'long_description'] = b'title\n=====\n\ntext'
        cmd = self._get_cmd(metadata)
        cmd.ensure_finalized()
        cmd.strict = 1
        inputs = RawInputs(b'1', b'tarek', b'y')
        register_module.raw_input = inputs.__call__
        try:
            cmd.run()
        finally:
            del register_module.raw_input

        cmd = self._get_cmd()
        cmd.ensure_finalized()
        inputs = RawInputs(b'1', b'tarek', b'y')
        register_module.raw_input = inputs.__call__
        try:
            cmd.run()
        finally:
            del register_module.raw_input

        metadata = {b'url': u'xxx', b'author': u'\xc9ric', b'author_email': u'xxx', 
           u'name': b'xxx', b'version': u'xxx', 
           b'description': u'Something about esszet \xdf', 
           b'long_description': u'More things about esszet \xdf'}
        cmd = self._get_cmd(metadata)
        cmd.ensure_finalized()
        cmd.strict = 1
        inputs = RawInputs(b'1', b'tarek', b'y')
        register_module.raw_input = inputs.__call__
        try:
            cmd.run()
        finally:
            del register_module.raw_input

        return

    @unittest.skipUnless(docutils is not None, b'needs docutils')
    def test_register_invalid_long_description(self):
        description = b':funkie:`str`'
        metadata = {b'url': b'xxx', b'author': b'xxx', b'author_email': b'xxx', 
           b'name': b'xxx', 
           b'version': b'xxx', b'long_description': description}
        cmd = self._get_cmd(metadata)
        cmd.ensure_finalized()
        cmd.strict = True
        inputs = RawInputs(b'2', b'tarek', b'tarek@ziade.org')
        register_module.raw_input = inputs
        self.addCleanup(delattr, register_module, b'raw_input')
        self.assertRaises(DistutilsSetupError, cmd.run)
        return

    def test_check_metadata_deprecated(self):
        cmd = self._get_cmd()
        with check_warnings() as w:
            warnings.simplefilter(b'always')
            cmd.check_metadata()
            self.assertEqual(len(w.warnings), 1)
        return


def test_suite():
    return unittest.makeSuite(RegisterTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
